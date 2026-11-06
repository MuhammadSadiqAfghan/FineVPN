# نصب عمومی 𝑭𝒊𝒏𝒆𝑽𝑷𝑵 1.0.0 | General Installation

<div align="center"><img src="https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png" width="84" alt="𝑭𝒊𝒏𝒆𝑽𝑷𝑵" /></div>

این سند راه‌اندازی محلی و Docker را توضیح می‌دهد. برای نصب روی سرویس مشخص، راهنمای همان پلتفرم را در README باز کنید.

## 1. پیش‌نیازها

- Python 3.11 یا جدیدتر (برای اجرای مستقیم)
- یا Docker Engine به‌همراه Docker Compose
- یک مسیر ذخیره‌سازی پایدار برای داده‌های پنل
- دامنه و TLS برای استفادهٔ عمومی

## 2. اجرای مستقیم با Python

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
cp .env.example .env          # Windows: copy .env.example .env
```

در `.env` حداقل `ADMIN_PASSWORD` و `SECRET_KEY` اختصاصی قرار دهید و `DATA_DIR` را به مسیری که باقی می‌ماند تنظیم کنید. سپس:

```bash
set -a
. ./.env
set +a
uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}
```

در Windows PowerShell متغیرها را از `.env` به‌صورت دستی یا با ابزار مدیریت محیط بارگذاری کنید.

## 3. اجرای Docker

```bash
cp .env.example .env
# .env را ویرایش کنید
docker compose up -d --build
docker compose logs -f finevpn
```

سرویس در حالت پیش‌فرض فقط روی `127.0.0.1:8000` میزبان bind می‌شود. Caddy/Nginx یا reverse proxy مشابه باید HTTPS را terminate کند و به پورت داخلی هدایت کند.

## 4. ورود اولیه

در نصب تازه و در صورتی که `ADMIN_USERNAME` و `ADMIN_PASSWORD` تنظیم نشده باشند:

- Username: `Admin`
- Password: `Admin`

**بلافاصله رمز را تغییر دهید و پیش از انتشار عمومی از رمز پیش‌فرض استفاده نکنید.** اگر state قبلی در `DATA_DIR` موجود باشد، اعتبارنامه‌های ذخیره‌شدهٔ آن حفظ می‌شوند؛ پیش‌فرض بالا برای نصب تازه است.

## 5. ذخیره‌سازی پایدار

برنامه فایل state و کلیدهای داخلی را در `DATA_DIR` نگه می‌دارد. برای Docker، Volume میزبان به `/data` متصل می‌شود. در سرویس‌های ابری نیز یک disk/volume واقعی بسازید و mount path را دقیقاً `/data` بگذارید. صرفاً تنظیم متغیر `DATA_DIR=/data` باعث ماندگاری نمی‌شود.

به‌عنوان راه جایگزین، کد از `GH_PERSIST_TOKEN`, `GH_PERSIST_REPO`, `GH_PERSIST_BRANCH` و `GH_PERSIST_PATH` برای ذخیرهٔ فایل state در مخزن GitHub پشتیبانی می‌کند. مخزن مقصد باید خصوصی باشد. state ممکن است UUID و لینک‌های حساس داشته باشد. این روش، دیتابیس تراکنشی چند replica نیست؛ برای حجم کم و یک replica نگه دارید و بکاپ جداگانه داشته باشید.

## 6. سلامت و مسیرها

- `GET /health` — بررسی سلامت API و وضعیت مسیر ذخیره‌سازی
- `GET /login` — صفحه ورود
- `GET /dashboard` — پنل مدیریت، نیازمند session
- `/p/<key>` — پرتال اشتراک
- `GET /sub-group/<key>` — خروجی subscription گروه

## 7. نکات شبکه و امنیت

- پورت عمومی 8000 را باز نکنید؛ reverse proxy را روی 80/443 قرار دهید.
- دسترسی SSH را فقط از IPهای مدیریتی مجاز کنید.
- `TRUST_PROXY_HEADERS=1` را فقط وقتی تنظیم کنید که reverse proxy مورد اعتماد دارید و IP آن در `TRUSTED_PROXIES` تعریف شده است.
- از فایل `.env`، بکاپ‌ها، UUIDها و GitHub token در Git عمومی محافظت کنید.
- کلید `SECRET_KEY` باید ثابت و محرمانه بماند.
- برای هر کاربر، تست اتصال را با کلاینت واقعی انجام دهید؛ پاسخ `/health` فقط سلامت برنامهٔ وب را نشان می‌دهد، نه کیفیت تونل VPN.

## English quick reference

Install Python 3.11 dependencies with `pip install -r requirements.txt`, then run `uvicorn main:app --host 0.0.0.0 --port $PORT`. Or use `docker compose up -d --build`. Put persistent storage at `/data`, terminate TLS at a reverse proxy, and set a unique admin password and secret key before public exposure. A clean installation with no configured credentials starts with `Admin` / `Admin`. Existing persisted credentials are not overwritten automatically.
