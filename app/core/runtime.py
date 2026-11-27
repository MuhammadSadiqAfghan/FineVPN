from __future__ import annotations
import asyncio, json, logging, os, secrets, time, hashlib, ipaddress
from collections import defaultdict, deque
from datetime import datetime, timedelta
from pathlib import Path
from app.core.config import DATA_DIR, APP_VERSION, PUBLIC_BASE_URL, DEFAULT_HOST
from app.core import database
from app.core.security import hash_password

logger=logging.getLogger('FineVPN')
LINKS: dict[str,dict]={}; SUBS: dict[str,dict]={}; CATEGORIES: dict[str,dict]={}
LINKS_LOCK=asyncio.Lock(); SUBS_LOCK=asyncio.Lock(); CATEGORIES_LOCK=asyncio.Lock()
USAGE_LOCKS: dict[str, asyncio.Lock] = {}
connections: dict[str,dict]={}; SPEED_SAMPLES={}
stats={'total_bytes':0,'upload_bytes':0,'download_bytes':0,'total_requests':0,'total_errors':0,'start_time':time.time()}
error_logs=deque(maxlen=100); activity_logs=deque(maxlen=500); hourly_traffic=defaultdict(int)
AUTH={'username':os.getenv('ADMIN_USERNAME','admin'),'password_hash':''}
SESSION_COOKIE='finevpn_session'; PROTOCOLS=('vless-ws','xhttp-packet-up','xhttp-stream-up'); DEFAULT_PROTOCOL='vless-ws'
FINGERPRINTS=('chrome','firefox','safari','ios','android','edge','random'); DEFAULT_FINGERPRINT='chrome'
DEFAULT_SPEED_LIMIT=0; SAVE_LOCK=asyncio.Lock()

def new_id():
    import uuid; return str(uuid.uuid4())

def log_activity(kind,message,level='info',meta=None):
    item={'kind':kind,'level':level,'message':str(message)[:500],'time':datetime.now().isoformat(),**(meta or {})}
    activity_logs.appendleft(item)
    try: database.add_event(item['time'],kind,level,item['message'],meta)
    except Exception: logger.exception('event persistence failed')

def parse_size_to_bytes(value,unit='GB'):
    return max(0,int(float(value or 0)*{'B':1,'KB':1024,'MB':1024**2,'GB':1024**3,'TB':1024**4}.get(str(unit).upper(),1024**3)))

def parse_speed_to_bytes(value, unit='Mbps'):
    # Preserve the difference between megabits (Mbps) and megabytes (MBps).
    factors = {
        'Bps': 1, 'KBps': 1024, 'MBps': 1024**2, 'GBps': 1024**3,
        'Kbps': 1024 / 8, 'Mbps': 1024**2 / 8, 'Gbps': 1024**3 / 8,
    }
    return max(0, int(float(value or 0) * factors.get(str(unit), factors['Mbps'])))

def fmt_bytes(n):
    n=max(0,int(n or 0)); units=['B','KB','MB','GB','TB']; x=float(n)
    for u in units:
        if x<1024 or u=='TB': return f'{x:.2f} {u}'
        x/=1024
    return f'{x:.2f} TB'

def generate_uuid(): return new_id()
def now_ir(): return datetime.now()
def is_link_expired(link):
    exp=(link or {}).get('expires_at')
    if not exp: return False
    try: return datetime.fromisoformat(str(exp).replace('Z','+00:00')).timestamp() <= time.time()
    except Exception: return True

def is_sub_expired(sub):
    if not sub:
        return True
    exp = sub.get('expires_at')
    if exp:
        try:
            return datetime.fromisoformat(str(exp).replace('Z', '+00:00')).timestamp() <= time.time()
        except Exception:
            return True
    days = int(sub.get('total_days') or 0)
    created = sub.get('created_at')
    if days > 0 and created:
        try:
            return datetime.fromisoformat(str(created).replace('Z', '+00:00')).timestamp() + days * 86400 <= time.time()
        except Exception:
            return True
    return False

def is_link_allowed(link):
    if not link or not link.get('active', True) or is_link_expired(link):
        return False
    sub_id = link.get('sub_id')
    if sub_id:
        sub = SUBS.get(sub_id)
        if not sub or not sub.get('active', True) or is_sub_expired(sub):
            return False
        sub_limit = int(sub.get('total_limit_bytes') or 0)
        if sub_limit > 0 and int(sub.get('total_used_bytes') or 0) >= sub_limit:
            return False
    lim = int(link.get('limit_bytes') or 0)
    used = int(link.get('used_bytes') or 0)
    return not (lim > 0 and used >= lim)

def unique_ips_for_uuid(uid):
    return {c.get('ip') for c in connections.values() if c.get('uuid') == uid and c.get('ip')}

def is_ip_allowed(link, uid, ip):
    link_ips = unique_ips_for_uuid(uid)
    link_cap = int((link or {}).get('ip_limit') or 0)
    if link_cap > 0 and ip not in link_ips and len(link_ips) >= link_cap:
        return False
    sub_id = (link or {}).get('sub_id')
    sub = SUBS.get(sub_id) if sub_id else None
    sub_cap = int((sub or {}).get('ip_limit') or 0)
    if sub_cap > 0:
        member_ids = set((sub or {}).get('link_ids') or [uid])
        group_ips = {c.get('ip') for c in connections.values()
                     if c.get('uuid') in member_ids and c.get('ip')}
        if ip not in group_ips and len(group_ips) >= sub_cap:
            return False
    return True

def resolve_client_ip(request):
    # Only accept forwarded headers when explicitly configured for a trusted deployment.
    peer=request.client.host if request.client else 'unknown'
    trusted={x.strip() for x in os.getenv('TRUSTED_PROXIES','').split(',') if x.strip()}
    if peer in trusted:
        raw=request.headers.get('x-forwarded-for','').split(',')[0].strip()
        try: return str(ipaddress.ip_address(raw))
        except ValueError: pass
    try: return str(ipaddress.ip_address(peer))
    except ValueError: return peer

def _migrate_old_state(data):
    migrated={'links':data.get('links',{}),'subs':data.get('subs',{}),'categories':data.get('categories',{})}
    for item in migrated['links'].values():
        if item.get('protocol')=='xhttp-stream-one': item['protocol']='xhttp-stream-up'
        item.setdefault('used_bytes',0); item.setdefault('upload_bytes',0); item.setdefault('download_bytes',0)
        item.setdefault('active',True); item.setdefault('speed_limit_bytes',0); item.setdefault('ip_limit',0)
    for s in migrated['subs'].values():
        s.setdefault('link_ids',[]); s.setdefault('total_used_bytes',0); s.setdefault('total_upload_bytes',0); s.setdefault('total_download_bytes',0); s.setdefault('total_limit_bytes',0)
    return migrated

async def _github_pull():
    token=os.getenv('GH_PERSIST_TOKEN','').strip(); repo=os.getenv('GH_PERSIST_REPO','').strip()
    if not token or not repo: return None
    import httpx, base64
    path=os.getenv('GH_PERSIST_PATH','state/panel_state.json').strip(); branch=os.getenv('GH_PERSIST_BRANCH','state').strip()
    url=f'https://api.github.com/repos/{repo}/contents/{path}'
    try:
        async with httpx.AsyncClient(timeout=20) as client:
            r=await client.get(url,params={'ref':branch},headers={'Authorization':f'token {token}','Accept':'application/vnd.github+json'})
            if r.status_code==200: return base64.b64decode(r.json()['content']).decode('utf-8')
    except Exception: logger.exception('GitHub state restore failed')
    return None

_LAST_GH_PUSH=0.0
async def _github_push(data):
    global _LAST_GH_PUSH
    token=os.getenv('GH_PERSIST_TOKEN','').strip(); repo=os.getenv('GH_PERSIST_REPO','').strip()
    if not token or not repo or time.time()-_LAST_GH_PUSH<60: return
    _LAST_GH_PUSH=time.time()
    import httpx, base64
    path=os.getenv('GH_PERSIST_PATH','state/panel_state.json').strip(); branch=os.getenv('GH_PERSIST_BRANCH','state').strip()
    url=f'https://api.github.com/repos/{repo}/contents/{path}'; headers={'Authorization':f'token {token}','Accept':'application/vnd.github+json'}
    try:
        async with httpx.AsyncClient(timeout=20) as client:
            prev=await client.get(url,params={'ref':branch},headers=headers); body={'message':'FineVPN 2.0 state sync','branch':branch,'content':base64.b64encode(json.dumps(data,ensure_ascii=False).encode()).decode()}
            if prev.status_code==200: body['sha']=prev.json().get('sha')
            r=await client.put(url,json=body,headers=headers)
            if r.status_code not in (200,201): logger.warning('GitHub persistence returned HTTP %s',r.status_code)
    except Exception: logger.exception('GitHub state sync failed')

async def load_state():
    database.init_db()
    data=database.get_value('panel_state')
    if not data:
        pulled=await _github_pull()
        if pulled:
            try: data=json.loads(pulled)
            except Exception: data=None
    if not data:
        legacy=DATA_DIR/'panel_state.json'
        # old ZIP deployments may keep data beside app directory
        candidates=[legacy,Path(__file__).resolve().parents[3]/'data'/'panel_state.json']
        for p in candidates:
            if p.exists():
                try: data=json.loads(p.read_text(encoding='utf-8')); break
                except Exception: logger.exception('legacy state read failed')
    if data:
        m=_migrate_old_state(data); LINKS.update(m['links']); SUBS.update(m['subs']); CATEGORIES.update(m['categories'])
        AUTH['username']=data.get('username') or AUTH['username']; AUTH['password_hash']=data.get('password_hash') or ''
        database.set_value('panel_state',m|{'username':AUTH['username'],'password_hash':AUTH['password_hash']})
    if not AUTH['password_hash']:
        envpw=os.getenv('ADMIN_PASSWORD','')
        initial=envpw or secrets.token_urlsafe(16)
        AUTH['password_hash']=hash_password(initial)
        if not envpw:
            credential_file = DATA_DIR / 'INITIAL_ADMIN_CREDENTIALS.txt'
            try:
                credential_file.write_text(f"username: {AUTH['username']}\npassword: {initial}\n", encoding='utf-8')
                credential_file.chmod(0o600)
            except OSError:
                logger.exception('could not persist initial administrator credentials')
        log_activity('security','رمز اولیه مدیر ساخته شد؛ فایل INITIAL_ADMIN_CREDENTIALS.txt را امن نگه دارید','warn')
    if not LINKS:
        uid=generate_uuid(); LINKS[uid]={'label':'کانفیگ پیش‌فرض','limit_bytes':0,'used_bytes':0,'upload_bytes':0,'download_bytes':0,'created_at':datetime.now().isoformat(),'active':True,'expires_at':None,'note':'','is_default':True,'sub_id':None,'protocol':DEFAULT_PROTOCOL,'fingerprint':DEFAULT_FINGERPRINT,'alpn':'','port':443,'ip_limit':0,'speed_limit_bytes':0,'category_id':'0'}
    await save_state()

async def save_state():
    async with SAVE_LOCK:
        data={'links':LINKS,'subs':SUBS,'categories':CATEGORIES,'username':AUTH['username'],'password_hash':AUTH['password_hash'],'version':APP_VERSION,'saved_at':datetime.now().isoformat()}
        database.set_value('panel_state',data)
        if os.getenv('GH_PERSIST_TOKEN') and os.getenv('GH_PERSIST_REPO'):
            asyncio.create_task(_github_push(data))

async def add_sub_usage(sub_id,n):
    sub=SUBS.get(sub_id)
    if sub:
        total=int(sub.get('total_limit_bytes') or 0)
        used=int(sub.get('total_used_bytes') or 0)
        if total <= 0 or used + int(n) <= total:
            sub['total_used_bytes']=used+int(n)
            await save_state()

def make_vless_link(link,uid,host):
    from urllib.parse import quote
    proto=link.get('protocol','vless-ws')
    if proto=='vless-ws':
        transport='type=ws'; path=f'/ws/{uid}'
    else:
        mode='packet-up' if proto=='xhttp-packet-up' else 'stream-up'
        transport=f'type=xhttp&mode={mode}'; path=f'/xhttp-siz10/{mode}/{uid}'
    name=quote((link.get('label') or 'FineVPN').replace(' ','-'))
    alpn=(link.get('alpn') or '')
    extra=f'&alpn={quote(alpn)}' if alpn else ''
    return f"vless://{uid}@{host}:{int(link.get('port',443))}?encryption=none&security=tls&{transport}&host={host}&path={quote(path)}&fp={link.get('fingerprint','chrome')}{extra}#{name}"

async def make_link(**kw):
    uid=generate_uuid(); sub_id=kw.get('sub_id')
    link={'label':str(kw.get('label') or 'کانفیگ جدید').strip()[:60],'limit_bytes':max(0,int(kw.get('limit_bytes') or 0)),
          'used_bytes':0,'upload_bytes':0,'download_bytes':0,'created_at':datetime.now().isoformat(),'active':True,
          'expires_at':kw.get('expires_at'),'note':str(kw.get('note') or '')[:200],'is_default':False,'sub_id':sub_id,
          'protocol':kw.get('protocol') if kw.get('protocol') in PROTOCOLS else DEFAULT_PROTOCOL,
          'fingerprint':kw.get('fingerprint') if kw.get('fingerprint') in FINGERPRINTS else DEFAULT_FINGERPRINT,
          'alpn':str(kw.get('alpn') or '')[:100],'port':max(1,min(65535,int(kw.get('port') or 443))),
          'ip_limit':max(0,int(kw.get('ip_limit') or 0)),'speed_limit_bytes':max(0,int(kw.get('speed_limit_bytes') or 0)),
          'category_id':str(kw.get('category_id') or '0'),'inherits_sub_expiry':bool(kw.get('inherits_sub_expiry',False))}
    LINKS[uid]=link
    if sub_id and sub_id in SUBS: SUBS[sub_id].setdefault('link_ids',[]).append(uid)
    await save_state(); log_activity('link',f"کانفیگ «{link['label']}» ساخته شد",'ok')
    return uid,link

async def create_sub_group(name='گروه جدید',desc='',password=''):
    sid=generate_uuid(); key=secrets.token_urlsafe(18)
    sub={'name':str(name or 'گروه جدید')[:60],'desc':str(desc or '')[:200],'password_hash':hash_password(password) if password else None,
         'uuid_key':key,'created_at':datetime.now().isoformat(),'link_ids':[],'total_used_bytes':0,'total_upload_bytes':0,'total_download_bytes':0,'total_limit_bytes':0,
         'expires_at':None,'total_days':0,'active':True}
    SUBS[sid]=sub; await save_state(); log_activity('subscription',f"گروه «{sub['name']}» ساخته شد",'ok')
    return sid,sub

async def remove_link(uid):
    l=LINKS.pop(uid,None)
    if not l: return None
    sid=l.get('sub_id')
    if sid in SUBS: SUBS[sid]['link_ids']=[x for x in SUBS[sid].get('link_ids',[]) if x!=uid]
    await save_state(); return l.get('label')

def detect_device(ua):
    ua=(ua or '').lower()
    if 'iphone' in ua: return 'iPhone'
    if 'ipad' in ua: return 'iPad'
    if 'android' in ua: return 'Android'
    if 'windows' in ua: return 'Windows'
    if 'mac os' in ua or 'macintosh' in ua: return 'Mac'
    if 'linux' in ua: return 'Linux'
    return 'Unknown'

def get_base_url(request=None):
    if PUBLIC_BASE_URL:
        return PUBLIC_BASE_URL.rstrip('/')
    if request is not None:
        return str(request.base_url).rstrip('/')
    host = os.getenv('RAILWAY_PUBLIC_DOMAIN') or os.getenv('PUBLIC_HOST') or DEFAULT_HOST
    scheme = 'https' if os.getenv('COOKIE_SECURE', '').lower() in {'1', 'true', 'yes'} else 'http'
    return f'{scheme}://{host}'

def get_host(request=None):
    if PUBLIC_BASE_URL:
        return PUBLIC_BASE_URL.replace('https://', '').replace('http://', '').split('/')[0]
    host = os.getenv('RAILWAY_PUBLIC_DOMAIN') or os.getenv('PUBLIC_HOST')
    if host:
        return host
    if request is not None:
        # Request Host is used only as a display/connection host fallback.
        # Production deployments should set PUBLIC_BASE_URL explicitly.
        return request.url.netloc
    return DEFAULT_HOST
