<div align="center"><img src="https://cdn.simpleicons.org/linux/FCC624" height="44" alt="Linux VPS / Dedicated Server" /></div>

# راهنمای استقرار 𝑭𝒊𝒏𝒆𝑽𝑷𝑵 روی VPS / سرور اختصاصی

این روش برای میزبانی کامل و پایدار توصیه می‌شود؛ به شرط آنکه ارائه‌دهنده اجازهٔ اجرای Docker/پایتون، WebSocket و دسترسی شبکهٔ موردنیاز را بدهد.

## 1 — آماده‌سازی سرور

یک Ubuntu LTS یا Debian stable با دسترسی sudo انتخاب کنید. یک IP ثابت و دامنه تنظیم کنید. حداقل منابع را با تعداد کاربران و ترافیک واقعی انتخاب کنید؛ ظرفیت مشخصی را بدون تست بار تضمین نمی‌کنیم.

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y ca-certificates curl git ufw
```

Docker Engine و Docker Compose را طبق راهنمای رسمی Docker نصب کنید. سپس firewall را محدود کنید:

```bash
sudo ufw allow from YOUR_ADMIN_IP to any port 22 proto tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

## 2 — بارگذاری و پیکربندی

ZIP را در یک مسیر مثل `/opt/finevpn` استخراج کنید و وارد ریشهٔ پروژه شوید.

```bash
cd /opt/finevpn
cp .env.example .env
nano .env
```

`DATA_DIR=/data`، یک `ADMIN_PASSWORD` طولانی و تصادفی، و یک `SECRET_KEY` مستقل تنظیم کنید. از بازکردن پورت 8000 به اینترنت خودداری کنید.

## 3 — اجرا

```bash
docker compose up -d --build
docker compose ps
curl -fsS http://127.0.0.1:8000/health
```

`compose.yaml` داده‌های برنامه را در `./data` نگه می‌دارد و پورت محلی 8000 را برای reverse proxy در دسترس قرار می‌دهد.

## 4 — دامنه و TLS

DNS دامنه را به IP سرور وصل کنید. Caddy را روی میزبان نصب و `Caddyfile` را با دامنهٔ خود ویرایش کنید، سپس آن را reload کنید. پورت‌های 80/443 باید از firewall و فایروال ارائه‌دهنده عبور کنند. بعد از دریافت TLS از `https://your-domain/login` وارد شوید.

## 5 — اطلاعات ورود

در نصب تازه، اگر `ADMIN_USERNAME` و `ADMIN_PASSWORD` را تنظیم نکنید، هر دو `Admin` هستند. این پیش‌فرض فقط برای راه‌اندازی اولیه است؛ قبل از عمومی‌کردن پنل عوضش کنید. state قبلی می‌تواند credentialهای ذخیره‌شده را حفظ کند.

## 6 — بکاپ، بروزرسانی و عیب‌یابی

- بکاپ داخلی پنل را دانلود کنید و نسخه‌ای خارج از سرور نگه دارید.
- قبل از بروزرسانی `docker compose down` لازم نیست؛ ابتدا بکاپ بگیرید و سپس image را rebuild کنید.
- `docker compose logs -f finevpn`، `curl /health` و لاگ reverse proxy را بررسی کنید.
- اگر صفحه بالا نمی‌آید، DNS، TLS، firewall و binding داخلی پورت 8000 را بررسی کنید.
- سلامت HTTP به‌تنهایی اثبات‌کنندهٔ اتصال تونل VLESS/XHTTP نیست؛ با کلاینت واقعی تست انجام دهید.

## English

Use a Linux VPS/dedicated server with root access, a static IP, DNS, firewall control, Docker, and persistent storage. Allow SSH only from your management IP and expose only 80/443 publicly. Configure `.env`, deploy with Docker Compose, then use Caddy for TLS. Fresh installs default to `Admin` / `Admin` only when credentials are omitted; change them before public access.
