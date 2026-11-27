from __future__ import annotations
import os, time, json, psutil, secrets, shutil
from datetime import datetime, timedelta
from pathlib import Path
from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.responses import JSONResponse, FileResponse
from app.core.runtime import *
from app.core.config import DATA_DIR, EXPORT_DIR, APP_VERSION
from app.core.security import require_auth
from app.core import database

router=APIRouter(prefix='/api',tags=['panel'])
CAT_COLORS=['#e60023','#ffffff','#8b8b8b','#a1a1aa','#dc2626']

@router.get('/ping')
async def ping(): return {'ok':True,'version':APP_VERSION}

@router.get('/system')
async def system(_=Depends(require_auth)):
    vm=psutil.virtual_memory(); disk=psutil.disk_usage(str(DATA_DIR)); cpu=psutil.cpu_percent(interval=.1)
    return {'version':APP_VERSION,'uptime_seconds':int(time.time()-stats['start_time']),'cpu_percent':cpu,
            'memory_total':vm.total,'memory_used':vm.used,'memory_percent':vm.percent,'disk_total':disk.total,
            'disk_used':disk.used,'disk_percent':disk.percent,'links':len(LINKS),'subscriptions':len(SUBS),
            'active_connections':len(connections),'data_dir':str(DATA_DIR)}

@router.get('/telemetry')
async def telemetry(_=Depends(require_auth)):
    vm=psutil.virtual_memory()
    return {'cpu':psutil.cpu_percent(interval=.1),'memory_percent':vm.percent,'memory_used':vm.used,'memory_total':vm.total,
            'active_connections':len(connections),'total_bytes':stats['total_bytes'],'total_requests':stats['total_requests'],
            'total_errors':stats['total_errors'],'uptime':int(time.time()-stats['start_time'])}

@router.get('/stats')
async def get_stats(_=Depends(require_auth)):
    total_used=sum(int(x.get('used_bytes',0)) for x in LINKS.values())
    return {'links':len(LINKS),'subscriptions':len(SUBS),'active_links':sum(1 for x in LINKS.values() if is_link_allowed(x)),
            'active_connections':len(connections),'traffic_bytes':total_used,'traffic_fmt':fmt_bytes(total_used),
            'upload_bytes':sum(int(x.get('upload_bytes',0)) for x in LINKS.values()),
            'download_bytes':sum(int(x.get('download_bytes',0)) for x in LINKS.values()),'total_requests':stats['total_requests'],
            'total_errors':stats['total_errors'],'uptime_seconds':int(time.time()-stats['start_time'])}

@router.get('/activity')
async def activity(limit:int=100,_=Depends(require_auth)):
    rows=database.get_events(limit)
    return {'events':rows}

@router.get('/connections')
async def get_connections(_=Depends(require_auth)):
    return {'connections':list(connections.values())}

@router.get('/links')
async def list_links(request: Request,_=Depends(require_auth)):
    host=get_host(request)
    rows=[]
    for uid,item in LINKS.items():
        x=dict(item); x.update({'uuid':uid,'allowed':is_link_allowed(item),'used_fmt':fmt_bytes(item.get('used_bytes',0)),
            'limit_fmt':'نامحدود' if not item.get('limit_bytes') else fmt_bytes(item['limit_bytes']),
            'vless_link':make_vless_link(item,uid,host),'connections':sum(1 for c in connections.values() if c.get('uuid')==uid)})
        rows.append(x)
    rows.sort(key=lambda x:x.get('created_at',''),reverse=True)
    return {'links':rows}

@router.post('/links')
async def create_link(request:Request,_=Depends(require_auth)):
    b=await request.json(); days=max(0,min(3650,int(b.get('days') or 0)))
    expiry=(datetime.now()+timedelta(days=days)).isoformat() if days else None
    size=parse_size_to_bytes(b.get('limit_value',0),b.get('limit_unit','GB')) if b.get('limit_value') else int(b.get('limit_bytes') or 0)
    speed=parse_speed_to_bytes(b.get('speed_value',0),b.get('speed_unit','Mbps')) if b.get('speed_value') else int(b.get('speed_limit_bytes') or 0)
    if b.get('sub_id') and b.get('sub_id') not in SUBS: raise HTTPException(404,'گروه اشتراک پیدا نشد')
    uid,item=await make_link(label=b.get('label'),limit_bytes=size,expires_at=expiry,note=b.get('note'),sub_id=b.get('sub_id'),
        protocol=b.get('protocol'),fingerprint=b.get('fingerprint'),alpn=b.get('alpn'),port=b.get('port',443),
        ip_limit=b.get('ip_limit',0),speed_limit_bytes=speed,category_id=b.get('category_id'))
    return {'ok':True,'uuid':uid,'link':item}

@router.patch('/links/{uid}')
async def update_link(uid:str,request:Request,_=Depends(require_auth)):
    if uid not in LINKS: raise HTTPException(404,'کانفیگ پیدا نشد')
    b=await request.json(); x=LINKS[uid]
    for key in ('label','note','active','fingerprint','alpn','category_id'):
        if key in b: x[key]=b[key]
    if 'protocol' in b:
        if b['protocol'] not in PROTOCOLS: raise HTTPException(400,'پروتکل نامعتبر است')
        x['protocol']=b['protocol']
    for key in ('ip_limit','limit_bytes','speed_limit_bytes'):
        if key in b: x[key]=max(0,int(b[key]))
    if 'port' in b: x['port']=max(1,min(65535,int(b['port'])))
    if 'days' in b:
        days=max(0,min(3650,int(b['days'] or 0))); x['expires_at']=(datetime.now()+timedelta(days=days)).isoformat() if days else None
    if 'expires_at' in b: x['expires_at']=b['expires_at']
    await save_state(); log_activity('link',f"کانفیگ {x.get('label')} ویرایش شد")
    return {'ok':True}

@router.delete('/links/{uid}')
async def delete_link(uid:str,_=Depends(require_auth)):
    if not await remove_link(uid): raise HTTPException(404,'کانفیگ پیدا نشد')
    return {'ok':True}

@router.post('/links/{uid}/toggle')
async def toggle_link(uid:str,request:Request,_=Depends(require_auth)):
    if uid not in LINKS: raise HTTPException(404,'کانفیگ پیدا نشد')
    body=await request.json(); LINKS[uid]['active']=bool(body.get('active',not LINKS[uid].get('active',True)))
    await save_state(); return {'ok':True,'active':LINKS[uid]['active']}

@router.get('/links/export')
async def export_links(request:Request,_=Depends(require_auth)):
    host=get_host(request); lines=[make_vless_link(l,u,host) for u,l in LINKS.items() if is_link_allowed(l)]
    return JSONResponse({'count':len(lines),'links':lines})

@router.post('/links/bulk')
async def bulk_links(request:Request,_=Depends(require_auth)):
    b=await request.json(); labels=b.get('labels') or []; created=[]
    for i,label in enumerate(labels[:200]):
        uid,_=await make_link(label=str(label)[:60],sub_id=b.get('sub_id'),protocol=b.get('protocol','vless-ws'))
        created.append(uid)
    return {'ok':True,'created':created,'count':len(created)}

@router.get('/categories')
async def list_categories(_=Depends(require_auth)):
    out=[]
    for cid,c in CATEGORIES.items(): out.append({'id':cid,**c,'links_count':sum(1 for l in LINKS.values() if l.get('category_id')==cid)})
    return {'categories':out}

@router.post('/categories')
async def create_category(request:Request,_=Depends(require_auth)):
    b=await request.json(); name=str(b.get('name') or '').strip()
    if not name: raise HTTPException(400,'نام دسته الزامی است')
    cid=generate_uuid(); CATEGORIES[cid]={'name':name[:40],'color':b.get('color') or CAT_COLORS[len(CATEGORIES)%len(CAT_COLORS)],'number':len(CATEGORIES)+1}
    await save_state(); return {'ok':True,'id':cid}

@router.patch('/categories/{cid}')
async def update_category(cid:str,request:Request,_=Depends(require_auth)):
    if cid not in CATEGORIES: raise HTTPException(404,'دسته پیدا نشد')
    b=await request.json(); CATEGORIES[cid].update({k:b[k] for k in ('name','color','number') if k in b}); await save_state(); return {'ok':True}

@router.delete('/categories/{cid}')
async def delete_category(cid:str,_=Depends(require_auth)):
    if cid not in CATEGORIES: raise HTTPException(404,'دسته پیدا نشد')
    CATEGORIES.pop(cid)
    for link in LINKS.values():
        if link.get('category_id')==cid: link['category_id']='0'
    await save_state(); return {'ok':True}

@router.get('/backups')
async def list_backups(_=Depends(require_auth)):
    files=sorted((DATA_DIR/'backups').glob('*.json'),reverse=True) if (DATA_DIR/'backups').exists() else []
    return {'backups':[{'name':p.name,'size':p.stat().st_size,'created_at':datetime.fromtimestamp(p.stat().st_mtime).isoformat()} for p in files]}

@router.post('/backup')
async def backup(_=Depends(require_auth)):
    folder=DATA_DIR/'backups'; folder.mkdir(parents=True,exist_ok=True)
    name='finevpn-'+datetime.now().strftime('%Y%m%d-%H%M%S')+'.json'; p=folder/name
    p.write_text(json.dumps({'links':LINKS,'subs':SUBS,'categories':CATEGORIES,'username':AUTH['username'],'password_hash':AUTH['password_hash']},ensure_ascii=False,indent=2),encoding='utf-8')
    log_activity('backup',f'پشتیبان {name} ساخته شد','ok'); return {'ok':True,'name':name}

@router.get('/backup')
async def download_backup(_=Depends(require_auth)):
    folder=DATA_DIR/'backups'; folder.mkdir(parents=True,exist_ok=True)
    p=folder/('finevpn-export-'+datetime.now().strftime('%Y%m%d-%H%M%S')+'.json')
    p.write_text(json.dumps({'links':LINKS,'subs':SUBS,'categories':CATEGORIES,'username':AUTH['username'],'password_hash':AUTH['password_hash']},ensure_ascii=False,indent=2),encoding='utf-8')
    return FileResponse(p,filename=p.name,media_type='application/json')

@router.post('/backups/restore/{name}')
async def restore_backup(name:str,_=Depends(require_auth)):
    if '/' in name or '\\' in name: raise HTTPException(400,'نام فایل نامعتبر است')
    p=DATA_DIR/'backups'/name
    if not p.is_file(): raise HTTPException(404,'فایل پشتیبان پیدا نشد')
    data=json.loads(p.read_text(encoding='utf-8'))
    if not all(k in data for k in ('links','subs','categories')): raise HTTPException(400,'ساختار پشتیبان نامعتبر است')
    LINKS.clear(); LINKS.update(data['links']); SUBS.clear(); SUBS.update(data['subs']); CATEGORIES.clear(); CATEGORIES.update(data['categories'])
    await save_state(); log_activity('backup',f'پشتیبان {name} بازیابی شد','warn'); return {'ok':True}


@router.post('/restore')
async def restore_uploaded_backup(request:Request,_=Depends(require_auth)):
    """Restore a JSON export downloaded from FineVPN or an older FineVPN release."""
    try:
        data=await request.json()
    except Exception:
        raise HTTPException(400,'فایل پشتیبان JSON معتبر نیست')
    if not isinstance(data,dict) or data.get('format') not in (None,'vpn-backup'):
        raise HTTPException(400,'فرمت پشتیبان نامعتبر است')
    links=data.get('links'); subs=data.get('subs'); cats=data.get('categories') or {}
    if not isinstance(links,dict) or not isinstance(subs,dict) or len(links)>5000 or len(subs)>1000:
        raise HTTPException(400,'ساختار پشتیبان نامعتبر است')
    if not isinstance(cats,dict) or len(cats)>500:
        cats={}
    if any(not isinstance(x,dict) for x in links.values()) or any(not isinstance(x,dict) for x in subs.values()):
        raise HTTPException(400,'ساختار رکوردهای پشتیبان نامعتبر است')
    normalized=_migrate_restore_state(links,subs,cats)
    LINKS.clear(); LINKS.update(normalized['links'])
    SUBS.clear(); SUBS.update(normalized['subs'])
    CATEGORIES.clear(); CATEGORIES.update(normalized['categories'])
    await save_state(); log_activity('backup','پشتیبان واردشده بازیابی شد','warn')
    return {'ok':True,'links':len(LINKS),'subs':len(SUBS),'categories':len(CATEGORIES)}

def _migrate_restore_state(links,subs,categories):
    clean_links={str(k):dict(v) for k,v in links.items()}
    clean_subs={str(k):dict(v) for k,v in subs.items()}
    for item in clean_links.values():
        if item.get('protocol')=='xhttp-stream-one': item['protocol']='xhttp-stream-up'
        item.setdefault('used_bytes',0); item.setdefault('upload_bytes',0); item.setdefault('download_bytes',0)
        item.setdefault('active',True); item.setdefault('ip_limit',0); item.setdefault('speed_limit_bytes',0)
    for item in clean_subs.values():
        item.setdefault('link_ids',[]); item.setdefault('total_used_bytes',0); item.setdefault('total_upload_bytes',0)
        item.setdefault('total_download_bytes',0); item.setdefault('total_limit_bytes',0)
    return {'links':clean_links,'subs':clean_subs,'categories':{str(k):dict(v) for k,v in categories.items() if isinstance(v,dict)}}
