<div align="center"><img src="https://cdn.simpleicons.org/render/46E3B7" height="44" alt="Render" /></div>

# راهنمای استقرار 𝑭𝒊𝒏𝒆𝑽𝑷𝑵 روی Render

Render می‌تواند سرویس FastAPI را به‌صورت Web Service اجرا کند. مسیرهای HTTP و WebSocket با مدل وب آن هم‌خوان هستند؛ برای نگهداری فایل محلی state پس از restart/redeploy باید Disk واقعی attach شود. بدون Disk، فایل‌سیستم موقت است.

## مرحله 1 — انتشار سورس

1. پروژه را در یک GitHub repository قرار دهید.
2. در Render گزینهٔ **New → Web Service** و repository را انتخاب کنید.
3. Runtime زبان Python را انتخاب کنید.
4. Build Command:

```bash
pip install -r requirements.txt
```

5. Start Command:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

## مرحله 2 — متغیرهای محیطی

در بخش Environment این مقادیر را وارد کنید:

```dotenv
DATA_DIR=/data
ADMIN_USERNAME=Admin
ADMIN_PASSWORD=YOUR-UNIQUE-LONG-PASSWORD
SECRET_KEY=YOUR-OWN-RANDOM-SECRET
```

مقادیر محرمانه را در GitHub commit نکنید.

## مرحله 3 — ذخیره‌سازی پایدار

در سرویس خود یک Persistent Disk ایجاد و Mount Path را `/data` تنظیم کنید. فقط نوشتن `DATA_DIR=/data` کافی نیست؛ Disk باید واقعاً attach شده باشد. سرویس‌های بدون Disk ممکن است پس از redeploy یا restart دادهٔ محلی را از دست بدهند. Diskهای پایدار به نوع سرویس/پلن Render وابسته‌اند؛ پیش از خرید محدودیت‌های جاری را بررسی کنید.

## مرحله 4 — دامنه و تست

دامنهٔ Render یا دامنهٔ سفارشی را فعال کنید. پس از Deploy:

- `/health` باید JSON با `status: ok` بدهد.
- `/login` باید صفحه ورود را نشان دهد.
- وارد داشبورد شوید و از پنل یک backup بگیرید.
- برای آزمون tunnel، کانفیگ واقعی را در کلاینت سازگار import و اتصال را تست کنید.

## اعتبار ورود اولیه

نصب تازه با نبود credentialهای سفارشی از `Admin` / `Admin` استفاده می‌کند. **رمز را قبل از عمومی‌کردن سرویس تغییر دهید.** اگر از state قبلی استفاده می‌کنید، رمز ذخیره‌شده قدیمی حفظ می‌شود.

## محدودیت‌های مهم Render

- نوع سرویس، پلن، Region، محدودیت پورت و قابلیت Disk بر دسترسی و پایداری اثر دارد.
- سرویس رایگان ممکن است idle شود و شروع دوباره تأخیر داشته باشد؛ برای سرویس always-on و دادهٔ پایدار، پلن و Disk مناسب را بررسی کنید.
- صرفاً بالا آمدن پنل به معنای تأیید تونل کامل یا latency مناسب برای کاربران نیست.

## English

Create a Render Web Service from the repository. Use `pip install -r requirements.txt` as the build command and `uvicorn main:app --host 0.0.0.0 --port $PORT` as the start command. Set `DATA_DIR=/data`, a unique `ADMIN_PASSWORD`, and `SECRET_KEY`. Attach a persistent disk mounted at `/data`; without a disk, local files are ephemeral. Fresh installations default to `Admin` / `Admin` if no credentials are configured—change the password before public exposure.

Official docs: [Web Services](https://render.com/docs/web-services) · [Persistent Disks](https://render.com/docs/disks) · [Deploys](https://render.com/docs/deploys)
