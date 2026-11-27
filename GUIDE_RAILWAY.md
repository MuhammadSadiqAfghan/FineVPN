# استقرار FineVPN روی Railway.app

<sup>[بازگشت به راهنمای استقرار](DEPLOYMENT.md) · [مستندات رسمی Railway](https://docs.railway.com/)</sup>

این راهنما اتصال مخزن GitHub به Railway و اجرای FineVPN با Dockerfile را توضیح می‌دهد. برای حفظ اطلاعات، باید Volume واقعی به مسیر `/data` متصل شود.

## ۱. ایجاد پروژه و Service

۱. وارد [داشبورد Railway](https://railway.com/) شوید.
۲. یک Project جدید ایجاد کنید.
۳. گزینهٔ Deploy from GitHub Repo را بزنید و مخزن FineVPN را انتخاب کنید.
۴. در تنظیم Build، از Dockerfile موجود در ریشهٔ پروژه استفاده کنید.
۵. پس از ساخت Service، در بخش Networking یک دامنهٔ عمومی بسازید یا دامنهٔ اختصاصی متصل کنید.

Railway سرویس‌ها را به‌صورت محیط اجرای کانتینری مدیریت می‌کند و از Dockerfile برای ساخت تصویر استفاده می‌کند. راهنمای رسمی: [Build & Deploy](https://docs.railway.com/build-deploy) و [FastAPI روی Railway](https://railway.com/guides/fastapi).

## ۲. ساخت Volume پایدار

۱. در Project، برای همان Web Service یک Volume اضافه کنید.
۲. Mount Path را دقیقاً `/data` قرار دهید.
۳. مطمئن شوید Volume به همان سرویسی متصل است که FineVPN در آن اجرا می‌شود.

در تنظیمات Service این متغیرها را تعریف کنید:

| متغیر | مقدار |
|---|---|
| `PORT` | `8000` |
| `DATA_DIR` | `/data` |
| `ADMIN_USERNAME` | نام کاربری اختصاصی مدیر |
| `ADMIN_PASSWORD` | رمز قوی و یکتا با حداقل ۱۰ نویسه |
| `SECRET_KEY` | خروجی تصادفی ثابت و بلند |
| `COOKIE_SECURE` | `true` |
| `PUBLIC_BASE_URL` | دامنهٔ HTTPS ساخته‌شده یا دامنهٔ شخصی |
| `FINEVPN_LOGO_URL` | `https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png` |

`PORT=8000` را در این راهنما صریحاً تنظیم کنید تا با Dockerfile پروژه هماهنگ باشد. اگر بعداً Dockerfile یا فرمان اجرا را تغییر دادید، پورت Service و پورت Listen برنامه را دوباره هماهنگ کنید.

Railway مقدار `RAILWAY_VOLUME_MOUNT_PATH` را نیز برای Volume فراهم می‌کند؛ با این حال `DATA_DIR=/data` را صریح نگه دارید. Volume هنگام اجرای کانتینر Mount می‌شود، نه هنگام Build؛ بنابراین فایل‌های داده را در مرحلهٔ Build ایجاد نکنید. [راهنمای Volume](https://docs.railway.com/volumes) · [جزئیات Volume](https://docs.railway.com/volumes/reference).

## ۳. Healthcheck و دامنه

در Service Settings بخش Deploy، مسیر Healthcheck را `/health` قرار دهید. سپس Deploy را اجرا کنید و این مسیرها را بررسی کنید:

- `https://YOUR_DOMAIN/health`
- `https://YOUR_DOMAIN/login`
- `https://YOUR_DOMAIN/` صفحهٔ عمومی

Healthcheck فقط پاسخ سلامت برنامه را تأیید می‌کند؛ کارکرد Relay، WebSocket یا دسترسی TCP خروجی را جداگانه با کلاینت واقعی آزمایش کنید.

## ۴. نصب Xray و Sing-box برای تست موتور

وجود موتور جمع‌آوری و تبدیل در برنامه به معنی نصب خودکار باینری‌های Xray و Sing-box روی هر پلتفرم نیست. برای تست اتصال واقعی، باید این دو باینری در محیط Runtime در دسترس باشند و دستورهای زیر مسیر آن‌ها را نشان دهند:

```bash
command -v xray
command -v sing-box
```

در صورت نیاز، روش نصب را در محیط سازگار با Container خودتان اضافه کنید یا از VPS/EC2 برای اجرای تست‌های زنده استفاده کنید. بدون باینری، خروجی‌ها را تست‌شده تلقی نکنید.

## ۵. تعداد Replica و Worker

با یک Replica و یک Worker شروع کنید. بخشی از رجیستری نشست‌های تونل و شمارش ترافیک در حافظهٔ همان فرایند قرار دارد؛ چند Replica می‌تواند وضعیت نشست‌ها و شمارنده‌ها را بین نمونه‌ها ناسازگار کند.

## ۶. بکاپ و به‌روزرسانی

- از Volume بکاپ دوره‌ای بگیرید.
- قبل از تعویض نسخه، فایل‌های داده را حذف یا Wipe نکنید.
- پس از Deploy، `/health`، ورود مدیر، گروه‌های اشتراک و یک اتصال واقعی را دوباره بررسی کنید.
- برای مهاجرت از نسخهٔ قبلی، ابتدا یک کپی از پوشهٔ داده و فایل `panel_secret.key` نگه دارید.

## منابع رسمی

- [Railway Build & Deploy](https://docs.railway.com/build-deploy)
- [Railway Volumes](https://docs.railway.com/volumes)
- [Railway Volume Reference](https://docs.railway.com/volumes/reference)
- [راهنمای FastAPI در Railway](https://railway.com/guides/fastapi)
