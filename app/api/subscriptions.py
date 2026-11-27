from __future__ import annotations
import secrets, time
from datetime import datetime, timedelta
from fastapi import APIRouter, Request, HTTPException, Depends
from app.core.runtime import *
from app.core.security import require_auth, hash_password

router=APIRouter(prefix='/api/subs',tags=['subscriptions'])

def _sub_expiry(sub):
    if sub.get('expires_at'): return sub['expires_at']
    days=int(sub.get('total_days') or 0)
    if days and sub.get('created_at'):
        try: return (datetime.fromisoformat(sub['created_at'])+timedelta(days=days)).isoformat()
        except Exception: pass
    return None

def _summary(sid,s,host,base_url):
    ids=s.get('link_ids',[]); links=[LINKS[x] for x in ids if x in LINKS]
    used=sum(int(x.get('used_bytes',0)) for x in links)
    active=sum(1 for x in links if is_link_allowed(x))
    return {'sub_id':sid,**{k:v for k,v in s.items() if k!='password_hash'},'has_password':bool(s.get('password_hash')),
            'links_count':len(ids),'active_count':active,'total_used_bytes':int(s.get('total_used_bytes',used)),'total_upload_bytes':int(s.get('total_upload_bytes',0)),'total_download_bytes':int(s.get('total_download_bytes',0)),'ip_limit':int(s.get('ip_limit',0)),
            'total_used_fmt':fmt_bytes(s.get('total_used_bytes',used)),'expires_at':_sub_expiry(s),
            'public_url':f'{base_url}/p/{s["uuid_key"]}','sub_url':f'{base_url}/sub-group/{s["uuid_key"]}'}

@router.get('')
async def list_subs(request:Request,_=Depends(require_auth)):
    host=get_host(request); base_url=get_base_url(request); return {'subs':[_summary(sid,s,host,base_url) for sid,s in sorted(SUBS.items(),key=lambda kv:kv[1].get('created_at',''),reverse=True)]}

@router.post('')
async def create_sub(request:Request,_=Depends(require_auth)):
    b=await request.json()
    if b.get('password') and len(str(b['password'])) < 10: raise HTTPException(400,'رمز اشتراک باید حداقل ۱۰ نویسه داشته باشد')
    sid,s=await create_sub_group(b.get('name','گروه جدید'),b.get('desc',''),b.get('password',''))
    if 'total_limit_bytes' in b: s['total_limit_bytes']=max(0,int(b['total_limit_bytes']))
    if 'ip_limit' in b: s['ip_limit']=max(0,min(100,int(b['ip_limit'] or 0)))
    if b.get('limit_value'): s['total_limit_bytes']=parse_size_to_bytes(b['limit_value'],b.get('limit_unit','GB'))
    days=max(0,min(3650,int(b.get('days') or 0))); s['total_days']=days
    s['expires_at']=(datetime.now()+timedelta(days=days)).isoformat() if days else None
    await save_state(); return {'ok':True,'sub_id':sid,'sub':s}

@router.get('/{sub_id}')
async def get_sub(sub_id:str,request:Request,_=Depends(require_auth)):
    s=SUBS.get(sub_id)
    if not s: raise HTTPException(404,'اشتراک پیدا نشد')
    return _summary(sub_id,s,get_host(request),get_base_url(request))

@router.patch('/{sub_id}')
async def update_sub(sub_id:str,request:Request,_=Depends(require_auth)):
    s=SUBS.get(sub_id)
    if not s: raise HTTPException(404,'اشتراک پیدا نشد')
    b=await request.json()
    for key in ('name','desc','active'):
        if key in b: s[key]=str(b[key])[:200] if key in ('name','desc') else bool(b[key])
    if 'password' in b:
        if b['password'] and len(str(b['password'])) < 10: raise HTTPException(400,'رمز اشتراک باید حداقل ۱۰ نویسه داشته باشد')
        s['password_hash']=hash_password(b['password']) if b['password'] else None
    if 'total_limit_bytes' in b: s['total_limit_bytes']=max(0,int(b['total_limit_bytes']))
    if 'ip_limit' in b: s['ip_limit']=max(0,min(100,int(b['ip_limit'] or 0)))
    if 'days' in b:
        days=max(0,min(3650,int(b['days'] or 0))); s['total_days']=days; s['expires_at']=(datetime.now()+timedelta(days=days)).isoformat() if days else None
        for lid in s.get('link_ids', []):
            if lid in LINKS and LINKS[lid].get('inherits_sub_expiry'):
                LINKS[lid]['expires_at'] = s['expires_at']
    if 'link_ids' in b:
        old=list(s.get('link_ids',[])); s['link_ids']=list(dict.fromkeys(str(x) for x in b['link_ids'] if str(x) in LINKS))
        for lid in old:
            if lid in LINKS and LINKS[lid].get('sub_id')==sub_id: LINKS[lid]['sub_id']=None
        for lid in s['link_ids']: LINKS[lid]['sub_id']=sub_id
    await save_state(); log_activity('subscription',f"اشتراک {s.get('name')} ویرایش شد")
    return {'ok':True}

@router.post('/{sub_id}/renew')
async def renew_sub(sub_id:str,request:Request,_=Depends(require_auth)):
    s=SUBS.get(sub_id)
    if not s: raise HTTPException(404,'اشتراک پیدا نشد')
    b=await request.json(); days=max(1,min(3650,int(b.get('days') or 30)))
    now=datetime.now(); current=_sub_expiry(s)
    try: current_dt=datetime.fromisoformat(current) if current else now
    except Exception: current_dt=now
    start=max(now,current_dt)
    s['created_at']=now.isoformat(); s['total_days']=max(0,int((start+timedelta(days=days)-now).total_seconds()/86400))
    s['expires_at']=(start+timedelta(days=days)).isoformat(); s['active']=True
    # Profiles generated for a subscription inherit its expiry, so renewal
    # extends the actual client profiles too (not merely the portal date).
    for lid in s.get('link_ids', []):
        if lid in LINKS and LINKS[lid].get('inherits_sub_expiry'):
            LINKS[lid]['expires_at'] = s['expires_at']
            LINKS[lid]['active'] = True if LINKS[lid].get('auto_disabled_by_expiry') else LINKS[lid].get('active', True)
            LINKS[lid].pop('auto_disabled_by_expiry', None)
    # Renew can optionally reset shared quota and per-link quotas.
    if b.get('reset_usage'):
        s['total_used_bytes']=0; s['total_upload_bytes']=0; s['total_download_bytes']=0
        for lid in s.get('link_ids',[]):
            if lid in LINKS: LINKS[lid].update({'used_bytes':0,'upload_bytes':0,'download_bytes':0})
    await save_state(); log_activity('subscription',f"اشتراک {s.get('name')} به مدت {days} روز تمدید شد",'ok')
    return {'ok':True,'expires_at':s['expires_at'],'total_days':s['total_days']}

@router.post('/{sub_id}/bandwidth')
async def set_sub_bandwidth(sub_id:str,request:Request,_=Depends(require_auth)):
    s=SUBS.get(sub_id)
    if not s: raise HTTPException(404,'اشتراک پیدا نشد')
    b=await request.json(); s['total_limit_bytes']=parse_size_to_bytes(b.get('value',0),b.get('unit','GB')) if b.get('value') else max(0,int(b.get('total_limit_bytes') or 0))
    await save_state(); return {'ok':True,'total_limit_bytes':s['total_limit_bytes']}

@router.get('/{sub_id}/bandwidth')
async def get_sub_bandwidth(sub_id:str,_=Depends(require_auth)):
    s=SUBS.get(sub_id)
    if not s: raise HTTPException(404,'اشتراک پیدا نشد')
    return {'total_limit_bytes':s.get('total_limit_bytes',0),'total_used_bytes':s.get('total_used_bytes',0)}

@router.post('/{sub_id}/quick-create')
async def quick_create(sub_id:str,request:Request,_=Depends(require_auth)):
    s=SUBS.get(sub_id)
    if not s: raise HTTPException(404,'اشتراک پیدا نشد')
    b=await request.json(); days=max(0,min(3650,int(b.get('days') or s.get('total_days') or 30)))
    expiry=(datetime.now()+timedelta(days=days)).isoformat() if days else s.get('expires_at')
    ip_limit=max(0,min(100,int(b.get('ip_limit', s.get('ip_limit', 0)) or 0)))
    speed=parse_speed_to_bytes(b.get('speed_value',0),b.get('speed_unit','Mbps')) if b.get('speed_value') else int(b.get('speed_limit_bytes') or 0)
    # Six owner-confirmed WebSocket profiles: Chrome/iOS x default, h2, HTTP/1.1.
    matrix=[('chrome',''),('chrome','h2'),('chrome','http/1.1'),('ios',''),('ios','h2'),('ios','http/1.1')]
    created=[]
    if b.get('replace',True):
        for lid in list(s.get('link_ids',[])): await remove_link(lid)
    for i,(fp,alpn) in enumerate(matrix,1):
        uid,_=await make_link(label=f"WS-{fp.upper()}-{alpn or 'DEFAULT'}-{i:02d}",expires_at=expiry,sub_id=sub_id,
            protocol='vless-ws',fingerprint=fp,alpn=alpn,port=443,ip_limit=ip_limit,speed_limit_bytes=speed,inherits_sub_expiry=True)
        created.append(uid)
    s['total_days']=days; s['expires_at']=expiry; s['active']=True
    s['ip_limit']=ip_limit
    if 'total_limit_bytes' in b: s['total_limit_bytes']=max(0,int(b['total_limit_bytes']))
    await save_state(); log_activity('subscription',f"۶ پروفایل برای {s['name']} ساخته شد",'ok')
    return {'ok':True,'count':len(created),'links':created}

@router.post('/{sub_id}/links')
async def assign_link(sub_id:str,request:Request,_=Depends(require_auth)):
    s=SUBS.get(sub_id)
    if not s: raise HTTPException(404,'اشتراک پیدا نشد')
    b=await request.json(); lid=str(b.get('link_id','')); action=b.get('action','add')
    if lid not in LINKS: raise HTTPException(404,'کانفیگ پیدا نشد')
    ids=s.setdefault('link_ids',[])
    if action=='add':
        if lid not in ids: ids.append(lid)
        LINKS[lid]['sub_id']=sub_id
    else:
        if lid in ids: ids.remove(lid)
        if LINKS[lid].get('sub_id')==sub_id: LINKS[lid]['sub_id']=None
    await save_state(); return {'ok':True}

@router.delete('/{sub_id}')
async def delete_sub(sub_id:str,_=Depends(require_auth)):
    s=SUBS.pop(sub_id,None)
    if not s: raise HTTPException(404,'اشتراک پیدا نشد')
    for lid in list(s.get('link_ids',[])):
        if lid in LINKS: LINKS.pop(lid,None)
    await save_state(); log_activity('subscription',f"اشتراک {s.get('name')} حذف شد",'warn'); return {'ok':True}
