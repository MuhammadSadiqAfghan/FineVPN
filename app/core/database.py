from __future__ import annotations
import sqlite3, json, time, hashlib
from contextlib import contextmanager
from app.core.config import DB_PATH

SCHEMA = '''
CREATE TABLE IF NOT EXISTS kv (key TEXT PRIMARY KEY, value TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS sessions (token_hash TEXT PRIMARY KEY, created_at REAL NOT NULL, expires_at REAL NOT NULL, ip TEXT, user_agent TEXT, device TEXT);
CREATE INDEX IF NOT EXISTS idx_sessions_exp ON sessions(expires_at);
CREATE TABLE IF NOT EXISTS login_attempts (key TEXT NOT NULL, at REAL NOT NULL);
CREATE INDEX IF NOT EXISTS idx_attempts_key ON login_attempts(key, at);
CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY AUTOINCREMENT, at TEXT NOT NULL, kind TEXT NOT NULL, level TEXT NOT NULL, message TEXT NOT NULL, meta TEXT NOT NULL DEFAULT '{}');
CREATE INDEX IF NOT EXISTS idx_events_at ON events(id DESC);
'''

def connect():
    con = sqlite3.connect(DB_PATH, timeout=20)
    con.row_factory = sqlite3.Row
    con.execute('PRAGMA journal_mode=WAL')
    con.execute('PRAGMA foreign_keys=ON')
    return con

def init_db():
    with connect() as con:
        con.executescript(SCHEMA)

def get_value(key, default=None):
    with connect() as con:
        row=con.execute('SELECT value FROM kv WHERE key=?',(key,)).fetchone()
        return json.loads(row['value']) if row else default

def set_value(key, value):
    raw=json.dumps(value,ensure_ascii=False,separators=(',',':'))
    with connect() as con:
        con.execute('INSERT INTO kv(key,value) VALUES(?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value',(key,raw))

def create_session(token, ttl, ip, ua, device):
    digest=hashlib.sha256(token.encode()).hexdigest(); now=time.time()
    with connect() as con:
        con.execute('INSERT INTO sessions VALUES(?,?,?,?,?,?)',(digest,now,now+ttl,ip,ua,device))

def valid_session(token):
    if not token: return False
    digest=hashlib.sha256(token.encode()).hexdigest(); now=time.time()
    with connect() as con:
        row=con.execute('SELECT expires_at FROM sessions WHERE token_hash=?',(digest,)).fetchone()
        if not row: return False
        if row['expires_at'] < now:
            con.execute('DELETE FROM sessions WHERE token_hash=?',(digest,)); return False
        return True

def delete_session(token):
    if not token: return
    digest=hashlib.sha256(token.encode()).hexdigest()
    with connect() as con: con.execute('DELETE FROM sessions WHERE token_hash=?',(digest,))

def prune_sessions():
    with connect() as con: con.execute('DELETE FROM sessions WHERE expires_at < ?', (time.time(),))

def record_login_attempt(key):
    now=time.time()
    with connect() as con:
        con.execute('DELETE FROM login_attempts WHERE at < ?', (now-300,))
        con.execute('INSERT INTO login_attempts(key,at) VALUES(?,?)',(key,now))

def login_limited(key, maximum=8):
    now=time.time()
    with connect() as con:
        con.execute('DELETE FROM login_attempts WHERE at < ?', (now-300,))
        row=con.execute('SELECT COUNT(*) n FROM login_attempts WHERE key=?',(key,)).fetchone()
        return row['n'] >= maximum

def clear_login_attempts(key):
    with connect() as con: con.execute('DELETE FROM login_attempts WHERE key=?',(key,))

def add_event(at, kind, level, message, meta=None):
    with connect() as con:
        con.execute('INSERT INTO events(at,kind,level,message,meta) VALUES(?,?,?,?,?)',
                    (at,kind,level,message,json.dumps(meta or {},ensure_ascii=False)))

def get_events(limit=200):
    with connect() as con:
        rows=con.execute('SELECT * FROM events ORDER BY id DESC LIMIT ?', (max(1,min(1000,int(limit))),)).fetchall()
    return [{**dict(r), 'meta': json.loads(r['meta'])} for r in rows]
