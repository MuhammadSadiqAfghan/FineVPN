<div align="center"><img src="https://cdn.simpleicons.org/cloudflare/F38020" height="44" alt="Cloudflare" /></div>

# راهنمای استفاده از Cloudflare در کنار 𝑭𝒊𝒏𝒆𝑽𝑷𝑵

**نکتهٔ کلیدی:** Cloudflare DNS، Proxy و Tunnel می‌توانند جلوی سرور اصلی قرار بگیرند؛ اما Cloudflare Workers جایگزین مستقیم VPS/EC2 برای اجرای کامل همین پروژه نیست. برنامه به فایل‌سیستم قابل نوشتن، پردازش FastAPI/Uvicorn و رفتار شبکه‌ای میزبان نیاز دارد. طبق مستندات فعلی Workers، ورودی HTTP و WebSocket در دسترس است، اما inbound raw TCP برای اتصال مستقیم به Worker هنوز پشتیبانی عمومی ندارد.

## روش پیشنهادی — Cloudflare DNS/Proxy جلوی VPS یا EC2

1. ابتدا 𝑭𝒊𝒏𝒆𝑽𝑷𝑵 را طبق `DEPLOY_AWS_EC2.md` یا `DEPLOY_VPS.md` روی سرور اصلی نصب کنید.
2. دامنه را به Cloudflare اضافه کنید و رکورد DNS به IP سرور اصلی بسازید.
3. TLS بین کاربر و Cloudflare فعال کنید. در origin، Caddy یا Nginx را با گواهی معتبر اجرا کنید.
4. حالت SSL/TLS را روی **Full (strict)** قرار دهید؛ از Flexible برای origin دارای TLS استفاده نکنید.
5. WebSocket را در تنظیمات Cloudflare فعال نگه دارید و قوانین WAF/Bot را طوری پیکربندی کنید که مسیرهای اشتراک و WebSocket به‌اشتباه مسدود نشوند.
6. دامنهٔ اصلی را در `ALLOWED_PUBLIC_HOSTS` وارد کنید تا URLهای ساخته‌شده به نام میزبان درست اشاره کنند.
7. اتصال را از طریق کلاینت واقعی بررسی کنید؛ درخواست سادهٔ `/health` فقط پنل وب را می‌آزماید.

## روش جایگزین — Cloudflare Tunnel

- `cloudflared` را روی همان VPS/EC2 نصب کنید.
- یک Tunnel بسازید و hostname عمومی را به سرویس origin روی `http://127.0.0.1:8000` هدایت کنید.
- پورت 8000 را به اینترنت باز نکنید؛ فقط tunnel به origin داخلی متصل شود.
- WebSocket و مسیرهای HTTP را با کلاینت واقعی آزمایش کنید.

## چرا Workers به‌تنهایی کافی نیست؟

FastAPI در Python Workers قابل استفاده است؛ بااین‌حال، پشتیبانی runtime برای HTTP/WebSocket مساوی با پشتیبانی کامل از رفتار شبکه‌ای و storage موردنیاز برنامه نیست. مسیر Workers برای این پروژه بیشتر به‌عنوان کد edge/API محدود یا reverse proxy مطرح است، نه میزبانی کامل backend همراه با state و تمام مسیرهای تونل.

## ورود اولیه

اگر backend روی VPS/EC2 تازه راه‌اندازی شده باشد و credential تنظیم نشده باشد، Username و Password اولیه هر دو `Admin` هستند. **قبل از قرار دادن hostname عمومی روی سرویس، رمز را تغییر دهید.**

## English

Use Cloudflare as DNS, reverse proxy, or Tunnel in front of an origin VPS/EC2 that runs the full application. Keep the origin's port 8000 private and forward traffic to `127.0.0.1:8000`. Enable WebSockets, use Full (strict) TLS, and avoid WAF rules that block legitimate subscription or WebSocket routes. Cloudflare Workers may run HTTP/WebSocket logic but are not a drop-in replacement for the full current application and its persistent local state/network requirements. Fresh origin installs default to `Admin` / `Admin` only when credentials are omitted; change them before public exposure.

Official docs: [Workers Protocols](https://developers.cloudflare.com/workers/reference/protocols/) · [FastAPI on Python Workers](https://developers.cloudflare.com/workers/languages/python/packages/fastapi/) · [TCP Sockets](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/)
