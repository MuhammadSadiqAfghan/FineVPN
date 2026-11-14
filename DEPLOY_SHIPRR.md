<div align="center"><strong style="font-size:28px">shiprr.</strong></div>

# راهنمای استقرار 𝑭𝒊𝒏𝒆𝑽𝑷𝑵 روی Shiprr.app

Shiprr استقرار سورس Python/FastAPI را اعلام کرده است. در حال حاضر استقرار source-based است و Dockerfile سفارشی/prebuilt Docker image در فهرست پشتیبانی‌شدهٔ فعلی نیست. فایل‌سیستم سرویس موقت است؛ persistence باید بیرونی باشد.

## 1 — اتصال repository

1. ZIP را extract کنید و محتوا را در ریشهٔ repository قرار دهید.
2. از Shiprr گزینهٔ ساخت App از GitHub را انتخاب کنید.
3. Runtime را Python قرار دهید.
4. Build Command:

```bash
pip install -r requirements.txt
```

5. Start Command:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

6. Health path را `/health` تعیین کنید و از دامنهٔ مدیریت‌شده یا دامنهٔ اختصاصی استفاده کنید.

## 2 — Environment

```dotenv
DATA_DIR=/tmp/finevpn-state
ADMIN_USERNAME=Admin
ADMIN_PASSWORD=YOUR-UNIQUE-LONG-PASSWORD
SECRET_KEY=YOUR-OWN-RANDOM-SECRET
GH_PERSIST_TOKEN=YOUR-RESTRICTED-GITHUB-TOKEN
GH_PERSIST_REPO=YOUR-PRIVATE-OWNER/PRIVATE-REPO
GH_PERSIST_BRANCH=state
GH_PERSIST_PATH=state/panel_state.json
```

> مسیر `/tmp` فقط در طول عمر همان instance قابل نوشتن است و persistence ندارد. مقادیر `GH_PERSIST_*` برای ذخیرهٔ جایگزین state در یک مخزن خصوصی استفاده می‌شوند. توکن را با حداقل مجوز لازم بسازید، مخزن را Private نگه دارید و توکن را در کد نگذارید.

## 3 — replica و داده

برای مدل persistence فعلی، تعداد replica را روی **1** نگه دارید. این روش GitHub-backed یک پایگاه دادهٔ تراکنشی چندنویسنده نیست و ممکن است با درخواست‌های هم‌زمان/چند replica دچار conflict شود. برای سرویس پرفشار یا چند replica به دیتابیس مشترک واقعی نیاز است.

## 4 — ورود اولیه

اگر `ADMIN_USERNAME` و `ADMIN_PASSWORD` تنظیم نشده باشند و state قبلی وجود نداشته باشد، ورود اولیه `Admin` / `Admin` است. قبل از عمومی‌کردن سرویس رمز را به مقدار اختصاصی تغییر دهید. در صورت فعال‌بودن GH persistence، اعتبارنامهٔ ذخیره‌شده از state قبلی ممکن است روی مقدار پیش‌فرض اولویت داشته باشد.

## 5 — آزمایش واقعی

- `GET /health` باید `status: ok` بدهد.
- `/login` و ساخت یک گروه آزمایشی را تست کنید.
- WebSocket Upgrade و درخواست‌های XHTTP را از کلاینت واقعی بررسی کنید.
- این راهنما پشتیبانی runtime از FastAPI را مستند می‌کند؛ **موفقیت full-tunnel روی شبکهٔ Shiprr تا وقتی جداگانه تست نشده باشد تضمین نمی‌شود.**

## English

Connect the repository to Shiprr, choose Python, build with `pip install -r requirements.txt`, and start with `uvicorn main:app --host 0.0.0.0 --port $PORT`. Set a health check at `/health`. Shiprr supports source-based FastAPI applications, but its filesystem is ephemeral and custom Dockerfile deploys are not currently supported. Use the app's GitHub persistence fallback with a private repository and restricted token, keep one replica, and keep backups. Fresh installs default to `Admin` / `Admin` if no credentials or prior state exist; change this before public exposure. Verify WebSocket/XHTTP tunnel compatibility on a real deployment before relying on it.

Official docs: [Supported Apps](https://shiprr.app/supported-apps) · [Deploy](https://shiprr.app/docs/deploy) · [Limits](https://shiprr.app/docs/limits)
