from __future__ import annotations
import hashlib, hmac, secrets, time
from fastapi import Request, HTTPException
from app.core import database
from app.core.config import SESSION_COOKIE, SESSION_TTL, SECRET_KEY

def hash_password(password: str) -> str:
    if len(password) < 10: raise ValueError('رمز عبور باید حداقل ۱۰ نویسه داشته باشد')
    iterations=310_000; salt=secrets.token_hex(16)
    digest=hashlib.pbkdf2_hmac('sha256',password.encode(),salt.encode(),iterations).hex()
    return f'pbkdf2_sha256${iterations}${salt}${digest}'

def verify_password(password: str, stored: str) -> bool:
    try:
        if stored.startswith('pbkdf2_sha256$'):
            _,it,salt,expected=stored.split('$',3)
            actual=hashlib.pbkdf2_hmac('sha256',password.encode(),salt.encode(),int(it)).hex()
            return hmac.compare_digest(actual,expected)
        # FineVPN 1.x used SHA-256(password + persistent SECRET_KEY) without a prefix.
        # Accept both the exact historical format and the short-lived prefixed variant.
        if stored.startswith('sha256:'):
            return hmac.compare_digest(hashlib.sha256(password.encode()).hexdigest(),stored[7:])
        legacy = hashlib.sha256(f'{password}{SECRET_KEY}'.encode()).hexdigest()
        return hmac.compare_digest(legacy, stored)
    except Exception: return False

def client_ip(request: Request) -> str:
    return request.client.host if request.client else 'unknown'

def detect_device(ua: str) -> str:
    ua=(ua or '').lower()
    if 'iphone' in ua: return 'iPhone'
    if 'ipad' in ua: return 'iPad'
    if 'android' in ua: return 'Android'
    if 'windows' in ua: return 'Windows'
    if 'mac os' in ua or 'macintosh' in ua: return 'Mac'
    if 'linux' in ua: return 'Linux'
    return 'Unknown'

async def require_auth(request: Request):
    token=request.cookies.get(SESSION_COOKIE)
    if not database.valid_session(token): raise HTTPException(status_code=401,detail='نشست معتبر نیست')
    return token
