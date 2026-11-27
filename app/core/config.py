from __future__ import annotations
import os
from pathlib import Path

APP_NAME = "FineVPN"
APP_VERSION = "2.0.0"
BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = Path(os.getenv("DATA_DIR") or os.getenv("RAILWAY_VOLUME_MOUNT_PATH") or BASE_DIR / "data")
DATA_DIR.mkdir(parents=True, exist_ok=True)
ENGINE_DIR = DATA_DIR / "engine"
ENGINE_DIR.mkdir(parents=True, exist_ok=True)
EXPORT_DIR = DATA_DIR / "exports"
EXPORT_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH = DATA_DIR / "finevpn.sqlite3"
# Preserve FineVPN 1.x password-hash compatibility: the original deployment
# stored its stable secret beside panel_state.json.
_SECRET_FILE = DATA_DIR / "panel_secret.key"
SECRET_KEY = os.getenv("SECRET_KEY", "").strip()
if not SECRET_KEY:
    try:
        SECRET_KEY = _SECRET_FILE.read_text(encoding="utf-8").strip()
    except OSError:
        SECRET_KEY = ""
if not SECRET_KEY:
    import secrets
    SECRET_KEY = secrets.token_urlsafe(32)
    try:
        _SECRET_FILE.write_text(SECRET_KEY, encoding="utf-8")
        _SECRET_FILE.chmod(0o600)
    except OSError:
        pass
SESSION_COOKIE = "finevpn_session"
SESSION_TTL = max(3600, int(os.getenv("SESSION_TTL_SECONDS", str(60 * 60 * 24 * 30))))
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")
COOKIE_SECURE = os.getenv("COOKIE_SECURE", "false").lower() in {"1", "true", "yes"}
PUBLIC_BASE_URL = os.getenv("PUBLIC_BASE_URL", "").rstrip("/")
LOGO_URL = os.getenv("FINEVPN_LOGO_URL", "https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png")
DEFAULT_HOST = os.getenv("RAILWAY_PUBLIC_DOMAIN", "localhost")
DEFAULT_PORT = int(os.getenv("PORT", "8000"))
