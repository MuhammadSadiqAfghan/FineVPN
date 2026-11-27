# راهنمای نصب و اجرای FineVPN 2.0

<sup>[صفحهٔ اصلی](README.md) · [همهٔ روش‌های استقرار](DEPLOYMENT.md)</sup>

## ۱. پیش‌نیازها

- Python نسخهٔ ۳.۱۱ یا جدیدتر؛ Dockerfile پروژه از Python 3.12 استفاده می‌کند.
- دسترسی ترمینال برای ساخت محیط مجازی و نصب بسته‌ها.
- برای استفادهٔ عمومی از پنل و Relay: یک سرور Linux با فرایند دائمی، WebSocket ورودی و TCP خروجی.
- برای انتشار عمومی، دامنه و HTTPS توصیه می‌شود.

## ۲. دریافت سورس

```bash
git clone https://github.com/MuhammadSadiqAfghan/FineVPN.git
cd FineVPN
```

اگر از فایل ZIP استفاده می‌کنید، محتویات پوشهٔ پروژه را استخراج کنید. فایل `main.py` و `requirements.txt` باید در همان پوشهٔ جاری باشند.

## ۳. نصب وابستگی‌ها در Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## ۴. تنظیم محرمانهٔ مدیر و کلید

برای اجرا، متغیرهای زیر را در محیط پردازش تعریف کنید:

```bash
export ADMIN_USERNAME='admin-custom'
export ADMIN_PASSWORD='یک-رمز-حداقل-ده-نویسه-و-منحصر-به-فرد'
export SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(48))')"
export DATA_DIR="$PWD/data"
export COOKIE_SECURE=false
```

رمز مدیر باید دست‌کم ۱۰ نویسه داشته باشد. در سرور عمومی از رمز پیش‌فرض یا نمونهٔ داخل مستندات استفاده نکنید.

اگر `ADMIN_PASSWORD` تنظیم نشود و دادهٔ مدیریتی قبلی هم موجود نباشد، برنامه در اولین اجرا یک رمز تصادفی تولید می‌کند و آن را در فایل `DATA_DIR/INITIAL_ADMIN_CREDENTIALS.txt` می‌نویسد. آن فایل محرمانه است. نام کاربری پیش‌فرض در نصب تازه `admin` است.

**نکته دربارهٔ `.env`:** فایل `.env.example` فقط الگو است و برنامه به‌تنهایی آن را بارگذاری نمی‌کند. برای بارگذاری در Bash:

```bash
cp .env.example .env
nano .env
set -a
source .env
set +a
```

هرگز `.env` واقعی را در GitHub بارگذاری نکنید.

## ۵. اجرای محلی

```bash
uvicorn main:app --host 127.0.0.1 --port 8000 --workers 1
```

سپس آدرس‌های زیر را باز کنید:

- ورود مدیر: `http://127.0.0.1:8000/login`
- صفحهٔ اصلی: `http://127.0.0.1:8000/`
- سلامت سرویس: `http://127.0.0.1:8000/health`

## ۶. اجرای قابل‌دسترسی در شبکه

برای آزمون در شبکهٔ محلی:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 1
```

فقط در شبکهٔ قابل‌اعتماد این پورت را باز کنید. برای اینترنت عمومی، برنامه را پشت HTTPS و پراکسی معکوس مثل Caddy یا Nginx قرار دهید؛ پورت داخلی برنامه را مستقیماً عمومی نکنید.

## ۷. اجرای Docker

```bash
docker build -t finevpn:2.0 .
mkdir -p data
docker run -d \
  --name finevpn \
  --restart unless-stopped \
  -p 8000:8000 \
  -v "$(pwd)/data:/data" \
  -e PORT=8000 \
  -e DATA_DIR=/data \
  -e ADMIN_USERNAME='admin-custom' \
  -e ADMIN_PASSWORD='REPLACE_WITH_A_UNIQUE_PASSWORD' \
  -e SECRET_KEY="$(python3 -c 'import secrets; print(secrets.token_urlsafe(48))')" \
  finevpn:2.0
```

برای استقرار عمومی `COOKIE_SECURE=true` و HTTPS لازم است. در Railway دستور Docker با متغیر پورت میزبان سازگار است؛ جزئیات در [راهنمای Railway](GUIDE_RAILWAY.md) آمده است.

## ۸. مسیرهای ذخیره‌سازی و ارتقا

نسخهٔ ۲ اطلاعات پنل را در `DATA_DIR/finevpn.sqlite3` نگه می‌دارد. فایل‌های موتور پردازش نیز در زیرپوشه‌های `engine` و `exports` قرار می‌گیرند. پوشه باید برای کاربر اجرای برنامه قابل‌نوشتن و در استقرار ابری روی دیسک پایدار باشد.

در اولین اجرا، برنامه تلاش می‌کند دادهٔ قدیمی `panel_state.json` را وارد پایگاه دادهٔ جدید کند. پیش از ارتقا، کل پوشهٔ دادهٔ نسخهٔ قبلی را کپی کنید و `panel_secret.key` قدیمی را نگه دارید.

## ۹. نصب هسته‌های تست اتصال

تجزیه، پاک‌سازی و تبدیل کانفیگ‌ها به‌تنهایی به باینری Xray و Sing-box نیاز ندارد؛ اما تست دسترسی واقعی کانفیگ‌ها نیازمند نصب هسته‌ها روی میزبان است. روی Linux پشتیبانی‌شده:

```bash
sudo bash scripts-install-cores.sh
which xray
which sing-box
```

بعد از نصب، اجرای موتور را از پنل یا با فرمان زیر انجام دهید:

```bash
python -m app.engine.cli
```

اگر هسته نصب نباشد، نتیجهٔ تست واقعی قابل تأیید نیست.

## ۱۰. بررسی پس از اجرا

- `/health` باید JSON با وضعیت `ok` برگرداند.
- `/login` باید صفحهٔ ورود فارسی را نمایش دهد.
- پس از ورود، `/dashboard` باید پنل مدیریت را باز کند.
- یک گروه اشتراک و پروفایل آزمایشی بسازید.
- لینک را در کلاینت واقعی وارد کنید و ترافیک منتقل کنید.
- پس از Restart بررسی کنید داده‌ها باقی مانده‌اند.

## راهنماهای ادامه

[پنل و اشتراک](GUIDE_PANEL_SUBSCRIPTIONS.md) · [موتور پروکسی](GUIDE_PROXY_ENGINE.md) · [VPS](GUIDE_VPS.md) · [Amazon EC2](GUIDE_AMAZON_EC2.md) · [ماشین مجازی](GUIDE_VM.md) · [Railway](GUIDE_RAILWAY.md)
