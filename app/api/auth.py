from __future__ import annotations
import secrets, time
from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.responses import JSONResponse
from app.core import database
from app.core.config import SESSION_COOKIE, SESSION_TTL, COOKIE_SECURE
from app.core.runtime import AUTH, log_activity, save_state
from app.core.security import require_auth, client_ip, detect_device, hash_password, verify_password

router=APIRouter(prefix='/api',tags=['authentication'])

@router.post('/login')
async def login(request: Request):
    body=await request.json(); username=str(body.get('username') or '').strip(); password=str(body.get('password') or '')
    key='u:'+username.lower()+'|ip:'+client_ip(request)
    if database.login_limited(key): raise HTTPException(429,'تلاش ناموفق زیاد است؛ پنج دقیقه بعد دوباره امتحان کنید')
    if username.casefold()!=str(AUTH.get('username','admin')).casefold() or not verify_password(password,AUTH.get('password_hash','')):
        database.record_login_attempt(key); raise HTTPException(401,'نام کاربری یا رمز عبور اشتباه است')
    database.clear_login_attempts(key)
    if not AUTH.get('password_hash', '').startswith('pbkdf2_sha256$'):
        AUTH['password_hash'] = hash_password(password)
        await save_state()
    token=secrets.token_urlsafe(40); ua=request.headers.get('user-agent','')[:300]
    database.create_session(token,SESSION_TTL,client_ip(request),ua,detect_device(ua))
    response=JSONResponse({'ok':True,'username':AUTH['username']})
    response.set_cookie(SESSION_COOKIE,token,max_age=SESSION_TTL,httponly=True,samesite='lax',secure=COOKIE_SECURE,path='/')
    log_activity('security',f"ورود مدیر از {client_ip(request)}",'ok')
    return response

@router.post('/logout')
async def logout(request: Request):
    token=request.cookies.get(SESSION_COOKIE); database.delete_session(token)
    response=JSONResponse({'ok':True}); response.delete_cookie(SESSION_COOKIE,path='/'); return response

@router.get('/me')
async def me(_=Depends(require_auth)):
    return {'username':AUTH['username'],'version':'2.0.0'}

@router.post('/change-credentials')
async def change_credentials(request: Request,_=Depends(require_auth)):
    body=await request.json(); old=str(body.get('current_password') or ''); new_user=str(body.get('username') or AUTH['username']).strip(); new_pw=str(body.get('new_password') or '')
    if not verify_password(old,AUTH['password_hash']): raise HTTPException(403,'رمز فعلی درست نیست')
    if not new_user: raise HTTPException(400,'نام کاربری خالی است')
    if new_pw:
        try: AUTH['password_hash']=hash_password(new_pw)
        except ValueError as e: raise HTTPException(400,str(e))
    AUTH['username']=new_user[:64]; await save_state()
    log_activity('security','اطلاعات ورود مدیر تغییر کرد','warn')
    return {'ok':True}

@router.post('/security/revoke-sessions')
async def revoke_sessions(request: Request,_=Depends(require_auth)):
    token=request.cookies.get(SESSION_COOKIE)
    with database.connect() as con:
        import hashlib
        keep=hashlib.sha256(token.encode()).hexdigest() if token else ''
        con.execute('DELETE FROM sessions WHERE token_hash != ?', (keep,))
    return {'ok':True}

@router.post('/change-password')
async def change_password(request: Request, _=Depends(require_auth)):
    body=await request.json()
    old=str(body.get('current_password') or '')
    new=str(body.get('new_password') or '')
    if not verify_password(old,AUTH.get('password_hash','')):
        raise HTTPException(400,'رمز فعلی اشتباه است')
    if len(new)<10:
        raise HTTPException(400,'رمز جدید باید حداقل ۱۰ نویسه داشته باشد')
    AUTH['password_hash']=hash_password(new)
    await save_state()
    token=request.cookies.get(SESSION_COOKIE)
    import hashlib
    keep=hashlib.sha256(token.encode()).hexdigest() if token else ''
    with database.connect() as con:
        con.execute('DELETE FROM sessions WHERE token_hash != ?', (keep,))
    log_activity('security','رمز عبور مدیر تغییر کرد','warn')
    return {'ok':True}
