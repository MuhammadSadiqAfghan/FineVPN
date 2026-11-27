from __future__ import annotations
import base64, time
from datetime import datetime, timedelta
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse, Response, JSONResponse
from app.core.runtime import *
from app.core.security import verify_password
from app.core.config import LOGO_URL
from app.core.web import render_public_page

router=APIRouter(tags=['public-subscriptions'])

def expiry_for_sub(sub):
    if sub.get('expires_at'): return sub['expires_at']
    days=int(sub.get('total_days') or 0)
    if days>0 and sub.get('created_at'):
        try: return (datetime.fromisoformat(sub['created_at'])+timedelta(days=days)).isoformat()
        except Exception: return None
    return None

def _get_sub_by_key(key):
    for sid,s in SUBS.items():
        if secrets.compare_digest(str(s.get('uuid_key','')),str(key)): return sid,s
    return None,None

@router.get('/sub/{uid}')
async def single_subscription(uid:str,request:Request):
    link=LINKS.get(uid)
    if not link or not is_link_allowed(link): raise HTTPException(404,'subscription not found')
    line=make_vless_link(link,uid,get_host(request))
    encoded=base64.b64encode((line+'\n').encode()).decode()
    uploaded=int(link.get('upload_bytes',0) or 0); downloaded=int(link.get('download_bytes',0) or 0)
    total=int(link.get('limit_bytes',0) or 0)
    try: expire=int(datetime.fromisoformat(link['expires_at']).timestamp()) if link.get('expires_at') else 0
    except Exception: expire=0
    info=f'upload={uploaded}; download={downloaded}; total={total}; expire={expire}'
    return Response(encoded,media_type='text/plain; charset=utf-8',headers={'profile-title':'base64:RmluZVZQTg==','subscription-userinfo':info,'profile-update-interval':'12','content-disposition':'attachment; filename="finevpn.txt"'})

@router.get('/sub-group/{uuid_key}')
async def group_subscription(uuid_key:str,request:Request):
    sid,sub=_get_sub_by_key(uuid_key)
    if not sub or not sub.get('active',True) or is_sub_expired(sub): raise HTTPException(404,'not found')
    if sub.get('password_hash'):
        pw=request.query_params.get('pw','')
        if not verify_password(pw,sub['password_hash']): raise HTTPException(403,'wrong password')
    lines=[make_vless_link(LINKS[lid],lid,get_host(request)) for lid in sub.get('link_ids',[]) if lid in LINKS and is_link_allowed(LINKS[lid])]
    encoded=base64.b64encode('\n'.join(lines).encode()).decode()
    used=int(sub.get('total_used_bytes',0)); uploaded=int(sub.get('total_upload_bytes',0)); downloaded=int(sub.get('total_download_bytes',0)); total=int(sub.get('total_limit_bytes',0)); exp=expiry_for_sub(sub)
    try: expire=int(datetime.fromisoformat(exp).timestamp()) if exp else 0
    except Exception: expire=0
    info=f'upload={uploaded}; download={downloaded}; total={total}; expire={expire}'
    return Response(encoded,media_type='text/plain; charset=utf-8',headers={'profile-title':'base64:RmluZVZQTiBTdWJzY3JpcHRpb24=','subscription-userinfo':info,'profile-update-interval':'12','content-disposition':'attachment; filename="finevpn-subscription.txt"'})

@router.get('/p/{uuid_key}',response_class=HTMLResponse)
async def public_page(uuid_key:str):
    sid,sub=_get_sub_by_key(uuid_key)
    if not sub: return HTMLResponse('<h2>اشتراک پیدا نشد</h2>',status_code=404)
    return HTMLResponse(render_public_page(uuid_key,LOGO_URL))

@router.get('/api/public/sub/{uuid_key}')
async def public_data(uuid_key:str,request:Request):
    sid,sub=_get_sub_by_key(uuid_key)
    if not sub or is_sub_expired(sub) or not sub.get('active', True): raise HTTPException(404,'اشتراک پیدا نشد')
    if sub.get('password_hash'):
        pw=request.query_params.get('pw','')
        if not verify_password(pw,sub['password_hash']): return {'locked':True,'name':sub.get('name','')}
    link_rows=[]
    for lid in sub.get('link_ids',[]):
        link=LINKS.get(lid)
        if not link: continue
        count=sum(1 for c in connections.values() if c.get('uuid')==lid)
        link_rows.append({'uuid':lid,'label':link.get('label'),'active':is_link_allowed(link),'protocol':link.get('protocol'),
          'used_bytes':link.get('used_bytes',0),'upload_bytes':link.get('upload_bytes',0),'download_bytes':link.get('download_bytes',0),
          'used_fmt':fmt_bytes(link.get('used_bytes',0)),'limit_bytes':link.get('limit_bytes',0),
          'expires_at':link.get('expires_at'),'vless_link':make_vless_link(link,lid,get_host(request)),
          'connections':count,'speed_limit_bytes':link.get('speed_limit_bytes',0)})
    used=int(sub.get('total_used_bytes',sum(x['used_bytes'] for x in link_rows)))
    uploaded=int(sub.get('total_upload_bytes',sum(x['upload_bytes'] for x in link_rows)))
    downloaded=int(sub.get('total_download_bytes',sum(x['download_bytes'] for x in link_rows)))
    total=int(sub.get('total_limit_bytes',0)); exp=expiry_for_sub(sub)
    days_left=None
    if exp:
        try: days_left=max(0,(datetime.fromisoformat(exp)-datetime.now()).days)
        except Exception: pass
    return {'locked':False,'name':sub.get('name'),'desc':sub.get('desc',''),'sub_url':f"{get_base_url(request)}/sub-group/{uuid_key}",
      'active':bool(sub.get('active',True)),'total_upload_bytes':uploaded,'total_download_bytes':downloaded,'total_limit_bytes':total,'total_limit_fmt':'نامحدود' if total==0 else fmt_bytes(total),'total_used_bytes':used,
      'total_used_fmt':fmt_bytes(used),'usage_percent':min(100,round(used*100/total)) if total else 0,
      'expires_at':exp,'days_left':days_left,'active_connections':sum(x['connections'] for x in link_rows),'links':link_rows}


@router.get('/sub-all')
async def subscription_all(request: Request):
    # Keep the legacy FineVPN aggregate subscription endpoint.
    from app.core.security import require_auth
    from app.core.database import valid_session
    from app.core.config import SESSION_COOKIE
    if not valid_session(request.cookies.get(SESSION_COOKIE)):
        raise HTTPException(401, 'نشست معتبر نیست')
    lines=[make_vless_link(link,uid,get_host(request)) for uid,link in LINKS.items() if is_link_allowed(link)]
    encoded=base64.b64encode('\n'.join(lines).encode()).decode()
    uploaded=sum(int(x.get('upload_bytes',0) or 0) for x in LINKS.values())
    downloaded=sum(int(x.get('download_bytes',0) or 0) for x in LINKS.values())
    info=f'upload={uploaded}; download={downloaded}; total=0; expire=0'
    return Response(encoded,media_type='text/plain; charset=utf-8',headers={'profile-title':'base64:RmluZVZQTiBBbGw=','subscription-userinfo':info,'profile-update-interval':'12','content-disposition':'attachment; filename="finevpn-all.txt"'})
