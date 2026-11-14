<div align="center"><img src="https://cdn.simpleicons.org/cpanel/FF6C2C" height="44" alt="cPanel" /></div>

# راهنمای هاست اشتراکی برای 𝑭𝒊𝒏𝒆𝑽𝑷𝑵

هاست اشتراکی فقط وقتی قابل استفاده است که ارائه‌دهنده صریحاً **Python ASGI/Uvicorn، برنامهٔ long-running، WebSocket Upgrade، storage پایدار و outbound network موردنیاز** را پشتیبانی کند. وجود گزینهٔ «Setup Python App» در cPanel به‌تنهایی تضمین نمی‌کند که FastAPI/ASGI و تونل VPN به‌درستی اجرا شوند؛ بعضی میزبان‌ها فقط WSGI/Passenger را ارائه می‌کنند.

## 1 — قبل از خرید از میزبان بپرسید

- آیا Python 3.11 و اجرای ASGI با Uvicorn پشتیبانی می‌شود؟
- آیا WebSocket Upgrade برای مسیرهای برنامه مجاز است؟
- آیا فرآیند همیشه‌فعال و restart خودکار مجاز است؟
- آیا فایل‌سیستم در مسیر مشخص، بعد از restart و deploy باقی می‌ماند؟
- آیا outbound TCP و اتصال‌های طولانی مجازند؟
- آیا Reverse Proxy، TLS سفارشی و تنظیمات port قابل تغییر است؟

اگر پاسخ به موارد اصلی منفی است، این هاست برای اجرای کامل VPN مناسب نیست؛ از VPS استفاده کنید.

## 2 — در صورت پشتیبانی کامل

1. در cPanel یا پنل میزبان یک Python 3.11 application ایجاد کنید.
2. سورس را در ریشهٔ application آپلود کنید.
3. dependencyهای `requirements.txt` را در virtualenv نصب کنید.
4. اگر میزبان ASGI را به‌صورت مستقیم پشتیبانی نمی‌کند، فقط در صورتی از Passenger استفاده کنید که ارائه‌دهنده ASGI/ASGI adapter را رسماً تأیید کرده باشد؛ اجرای WSGI bridge بدون پشتیبانی رسمی راه‌حل تضمین‌شده‌ای نیست.
5. متغیرهای `DATA_DIR`, `ADMIN_USERNAME`, `ADMIN_PASSWORD`, `SECRET_KEY`, `PORT` را طبق قرارداد همان میزبان تنظیم کنید.
6. ASGI startup را به `main:app` هدایت کنید و WebSocket upgrade را فعال کنید.
7. TLS و hostname را تنظیم و درخواست `/health` و اتصال کلاینت واقعی را تست کنید.

## 3 — ورود اولیه

روی نصب تازه با credentialهای تنظیم‌نشده، نام کاربری و رمز هر دو `Admin` است. قبل از عمومی‌کردن حتماً رمز را عوض کنید؛ credential ذخیره‌شده در state قبلی ممکن است باقی بماند.

## چه زمانی استفاده نکنیم؟

اگر فقط PHP/CGI یا WSGI ساده در اختیار دارید، امکان WebSocket یا process پایدار ندارید، outbound connections محدود است، یا storage پس از deploy پاک می‌شود، این مسیر را برای تونل کامل به‌کار نبرید. ممکن است بتوانید فقط یک وب‌سایت ثابت/مستندات را در آن هاست منتشر کنید، ولی backend کامل باید روی VPS/سرویس سازگار اجرا شود.

## English

Shared hosting is conditional, not a guaranteed full deployment target. Confirm Python 3.11 ASGI/Uvicorn, long-running processes, WebSocket upgrades, durable writable storage, and required outbound network access with the provider. A generic cPanel Python/WSGI feature does not prove ASGI or VPN tunnel compatibility. If all requirements are confirmed, deploy the source with the provider's documented ASGI process and test real WebSocket/XHTTP clients. A fresh install defaults to `Admin` / `Admin` only when credentials are unset; change them before public exposure. Otherwise, use a VPS.

Official references: [cPanel Python applications](https://support.cpanel.net/hc/en-us/articles/4408475507479-Does-cPanel-support-Python-Java-or-other-frameworks) · [Passenger applications](https://docs.cpanel.net/knowledge-base/web-services/using-passenger-applications/)
