from __future__ import annotations
import os, sys, time, logging, asyncio, ipaddress, socket
from contextlib import asynccontextmanager
from pathlib import Path
from urllib.parse import urlsplit
import httpx
from fastapi import FastAPI, Request, HTTPException, Depends, WebSocket
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# Runtime objects form a small compatibility boundary for the protocol transports.
from app.core.runtime import *
from app.core.config import APP_NAME, APP_VERSION, DATA_DIR, DEFAULT_PORT, SESSION_COOKIE, COOKIE_SECURE, LOGO_URL
from app.core import database
from app.core.security import require_auth
from app.services.maintenance import maintenance_loop

logging.basicConfig(level=os.getenv('LOG_LEVEL','INFO'),format='%(asctime)s [%(levelname)s] %(name)s: %(message)s')
logger=logging.getLogger('FineVPN')

@asynccontextmanager
async def lifespan(app: FastAPI):
    await load_state()
    ensure_protocol_tasks()
    maintenance=asyncio.create_task(maintenance_loop())
    log_activity('system','FineVPN 2.0 راه‌اندازی شد','ok')
    try:
        yield
    finally:
        maintenance.cancel()
        try: await maintenance
        except asyncio.CancelledError: pass
        await save_state()

app=FastAPI(title='FineVPN 2.0',version=APP_VERSION,docs_url=None,redoc_url=None,openapi_url=None,lifespan=lifespan)
origins=[x.strip() for x in os.getenv('CORS_ORIGINS','').split(',') if x.strip()]
if origins:
    app.add_middleware(CORSMiddleware,allow_origins=origins,allow_credentials=True,allow_methods=['GET','POST','PATCH','PUT','DELETE','OPTIONS'],allow_headers=['Content-Type','X-Requested-With'])

STATIC_DIR=Path(__file__).resolve().parent/'app'/'static'
app.mount('/assets',StaticFiles(directory=STATIC_DIR),name='assets')

from app.api.auth import router as auth_router
from app.api.admin import router as admin_router
from app.api.subscriptions import router as subscriptions_router
from app.api.public import router as public_router
from app.api.engine import router as engine_router
app.include_router(auth_router); app.include_router(admin_router); app.include_router(subscriptions_router); app.include_router(public_router); app.include_router(engine_router)

# VLESS WebSocket and XHTTP transports are isolated from the HTTP control plane.
from app.transports.relay_vless import websocket_tunnel
from app.transports.xhttp_siz10 import router as xhttp_router, ensure_reaper as ensure_xhttp_reaper
app.add_api_websocket_route('/ws/{uuid}',websocket_tunnel)
app.include_router(xhttp_router)

def ensure_protocol_tasks():
    try: ensure_xhttp_reaper()
    except Exception: logger.exception('XHTTP reaper initialization failed')

@app.get('/',response_class=HTMLResponse)
async def root():
    return HTMLResponse((STATIC_DIR/'landing.html').read_text(encoding='utf-8').replace('__LOGO__',LOGO_URL))

@app.get('/stats')
async def legacy_stats(_=Depends(require_auth)):
    from app.api.admin import get_stats as _get_stats
    return await _get_stats()

@app.get('/health')
async def health():
    return {'status':'ok','app':APP_NAME,'version':APP_VERSION}

@app.get('/login',response_class=HTMLResponse)
async def login_page(request:Request):
    from app.core.database import valid_session
    if valid_session(request.cookies.get(SESSION_COOKIE)): return RedirectResponse('/dashboard')
    html=(STATIC_DIR/'login.html').read_text(encoding='utf-8').replace('__LOGO__',LOGO_URL)
    return HTMLResponse(html)

@app.get('/dashboard',response_class=HTMLResponse)
async def dashboard(request:Request):
    if not database.valid_session(request.cookies.get(SESSION_COOKIE)): return RedirectResponse('/login')
    return HTMLResponse((STATIC_DIR/'index.html').read_text(encoding='utf-8'))

@app.get('/test-ws', response_class=HTMLResponse)
async def websocket_test_page():
    return HTMLResponse('''<!doctype html><html lang="fa" dir="rtl"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>FineVPN · آزمایش اتصال</title><body style="margin:0;background:#000;color:#fff;font:16px Tahoma;padding:32px"><main style="max-width:700px;margin:auto;border:1px solid #333;border-radius:18px;padding:24px"><h1>FineVPN</h1><h2>آزمایش وضعیت WebSocket</h2><p>برای آزمایش واقعی، یک کانفیگ فعال FineVPN را در کلاینت خود وارد کنید. این صفحه به‌تنهایی اتصال تونل را شبیه‌سازی نمی‌کند.</p><a style="display:inline-block;background:#e60023;color:#fff;padding:12px 18px;border-radius:9px;text-decoration:none" href="/">بازگشت به صفحه اصلی</a></main></body></html>''')

@app.get('/api/qr')
async def qr(data:str):
    try:
        import qrcode
        from qrcode.image.svg import SvgImage
        import io
        image=qrcode.make(data,image_factory=SvgImage,box_size=5,border=2)
        out=io.BytesIO(); image.save(out)
        return Response(out.getvalue(),media_type='image/svg+xml')
    except Exception as e: raise HTTPException(400,'تولید QR ناموفق بود')

# The authenticated HTTP relay is deliberately restricted to public HTTP(S) destinations.
HOP_HEADERS={'connection','keep-alive','proxy-authenticate','proxy-authorization','te','trailers','transfer-encoding','upgrade','content-length','host'}
async def _safe_proxy_target(url:str):
    try:
        parts=urlsplit(url)
        if parts.scheme not in ('http','https') or not parts.hostname: return False
        infos=await asyncio.get_running_loop().getaddrinfo(parts.hostname,parts.port or (443 if parts.scheme=='https' else 80),type=socket.SOCK_STREAM)
        for info in infos:
            addr=ipaddress.ip_address(info[4][0])
            if not addr.is_global: return False
        return True
    except Exception: return False

@app.api_route('/proxy/{target_url:path}',methods=['GET','POST','PUT','PATCH','DELETE','HEAD','OPTIONS'])
async def http_proxy(target_url:str,request:Request,_=Depends(require_auth)):
    url=target_url if target_url.startswith(('http://','https://')) else 'https://'+target_url
    if not await _safe_proxy_target(url): raise HTTPException(400,'مقصد پراکسی مجاز نیست')
    body=await request.body()
    if len(body)>8*1024*1024: raise HTTPException(413,'درخواست بیش از حد بزرگ است')
    headers={k:v for k,v in request.headers.items() if k.lower() not in HOP_HEADERS}
    try:
        async with httpx.AsyncClient(timeout=30,follow_redirects=False) as client:
            r=await client.request(request.method,url,content=body,headers=headers,params=request.query_params)
        if r.is_redirect:
            location=r.headers.get('location','')
            if not await _safe_proxy_target(location): raise HTTPException(502,'ریدایرکت به مقصد غیرمجاز')
        out_headers={k:v for k,v in r.headers.items() if k.lower() not in HOP_HEADERS}
        return Response(r.content,status_code=r.status_code,headers=out_headers)
    except HTTPException: raise
    except Exception as e: raise HTTPException(502,'اتصال به مقصد ناموفق بود')

@app.get('/api/sessions')
async def list_sessions(_=Depends(require_auth)):
    with database.connect() as con:
        rows=con.execute('SELECT created_at,expires_at,ip,user_agent,device FROM sessions WHERE expires_at>? ORDER BY created_at DESC',(time.time(),)).fetchall()
    return {'sessions':[dict(x) for x in rows]}

@app.post('/api/security/revoke-other-sessions')
async def revoke_other_sessions(request:Request,_=Depends(require_auth)):
    token=request.cookies.get(SESSION_COOKIE)
    import hashlib
    keep=hashlib.sha256(token.encode()).hexdigest() if token else ''
    with database.connect() as con: con.execute('DELETE FROM sessions WHERE token_hash != ?', (keep,))
    return {'ok':True}

if __name__=='__main__':
    import uvicorn
    uvicorn.run('main:app',host='0.0.0.0',port=DEFAULT_PORT,log_level='info',workers=1)
