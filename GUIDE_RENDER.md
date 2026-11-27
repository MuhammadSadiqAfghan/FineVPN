# استقرار FineVPN روی Render

<sup>[بازگشت به راهنمای استقرار](DEPLOYMENT.md) · [مستندات Web Service](https://render.com/docs/web-services)</sup>

Render می‌تواند برای میزبانی پنل وب آزمایش شود؛ اما پیش از انتخاب آن برای تونل دائمی، محدودیت‌های پلن، WebSocket، ذخیره‌سازی پایدار و چرخهٔ خاموش/روشن‌شدن سرویس را بررسی کنید.

## ۱. ساخت Web Service

۱. وارد [داشبورد Render](https://dashboard.render.com/) شوید.
۲. گزینهٔ New و سپس Web Service را انتخاب کنید.
۳. مخزن GitHub مربوط به FineVPN را متصل کنید.
۴. در صورت استفاده از Dockerfile، روش ساخت Docker را انتخاب کنید؛ یا تنظیمات Python را به شکل زیر قرار دهید:

| گزینه | مقدار |
|---|---|
| Build Command | `pip install -r requirements.txt` |
| Start Command | `uvicorn main:app --host 0.0.0.0 --port $PORT --workers 1` |
| Health Check Path | `/health` |

## ۲. متغیرهای محیطی

در بخش Environment این مقادیر را تعریف کنید:

| متغیر | مقدار |
|---|---|
| `ADMIN_USERNAME` | نام کاربری اختصاصی |
| `ADMIN_PASSWORD` | رمز یکتا با حداقل ۱۰ نویسه |
| `SECRET_KEY` | مقدار تصادفی بلند و ثابت |
| `COOKIE_SECURE` | `true` |
| `PUBLIC_BASE_URL` | دامنهٔ HTTPS سرویس |
| `FINEVPN_LOGO_URL` | نشانی لوگوی اصلی FineVPN |
| `DATA_DIR` | مسیر Mount واقعی Persistent Disk |

## ۳. ذخیره‌سازی پایدار

فایل‌سیستم موقت سرویس را به‌عنوان محل نگهداری دائمی SQLite و داده‌های موتور در نظر نگیرید. در صورت استفاده از Persistent Disk، آن را به سرویس وصل کنید و مسیر Mount واقعی آن را در `DATA_DIR` قرار دهید. پلن و شرایط فعلی Render را پیش از انتخاب بررسی کنید.

## ۴. آزمون

۱. `/health` را باز کنید.
۲. ورود مدیر را در `/login` بررسی کنید.
۳. اشتراک آزمایشی بسازید.
۴. WebSocket و انتقال TCP را با کلاینت واقعی بررسی کنید.
۵. سرویس را Restart/Deploy کنید و ماندگاری داده‌ها را تأیید کنید.

موفقیت Deploy یا بازشدن پنل به‌تنهایی تضمین‌کنندهٔ اتصال تونل در همهٔ پلن‌ها نیست. اگر محدودیت شبکه یا فرایند دائمی وجود دارد، از VPS/EC2 استفاده کنید.

## منابع رسمی

- [Render Web Services](https://render.com/docs/web-services)
- [Render WebSocket](https://render.com/docs/websocket)
- [Render Persistent Disks](https://render.com/docs/disks)
