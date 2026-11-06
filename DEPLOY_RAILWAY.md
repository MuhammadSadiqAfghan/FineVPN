<div align="center"><img src="https://cdn.simpleicons.org/railway/FFFFFF" height="44" alt="Railway" /></div>

# راهنمای استقرار 𝑭𝒊𝒏𝒆𝑽𝑷𝑵 روی Railway

Railway سورس Python/FastAPI را build می‌کند و برای سرویس وب دامنهٔ عمومی می‌دهد. مسیرهای HTTP/WebSocket برنامه از سرویس وب استفاده می‌کنند. اگر سرویس TCP جداگانه‌ای نیاز شد، TCP Proxy را جداگانه پیکربندی کنید؛ این برنامه را با مسیرهای وب و پروتکل‌های موجود خودش تست کنید.

## 1 — ساخت سرویس

1. وارد Railway شوید و **New Project → Deploy from GitHub Repo** را انتخاب کنید.
2. repository پروژه را وصل کنید.
3. اگر Railway خودش Python را تشخیص نداد، Build Command را `pip install -r requirements.txt` قرار دهید.
4. Start Command:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

5. Healthcheck Path را `/health` قرار دهید و در بخش Networking دامنهٔ عمومی بسازید.

## 2 — ساخت Volume

در بخش **Volumes** یک Volume بسازید و Mount Path را دقیقاً `/data` قرار دهید. سپس متغیر `DATA_DIR=/data` را تعیین کنید. در صورت تنظیم خودکار Railway، `RAILWAY_VOLUME_MOUNT_PATH` نیز توسط پلتفرم ارائه می‌شود. Volume برای نگهداری state و secret فایل ضروری است.

## 3 — متغیرها

```dotenv
DATA_DIR=/data
ADMIN_USERNAME=Admin
ADMIN_PASSWORD=YOUR-UNIQUE-LONG-PASSWORD
SECRET_KEY=YOUR-OWN-RANDOM-SECRET
```

اگر دامنه به‌صورت خودکار به متغیر Railway داده شود، برنامه آن را برای تولید URL اشتراک استفاده می‌کند. در غیر این صورت دامنهٔ عمومی را با browser request و تنظیمات میزبان بررسی کنید.

## 4 — ورود و تست

در نصب تازه و بدون مقداردهی به credentialها، نام کاربری و رمز اولیه `Admin` / `Admin` است. **قبل از در دسترس قراردادن عمومی، رمز را تغییر دهید.** اگر state قبلی روی Volume موجود باشد، اطلاعات ورود ذخیره‌شده حفظ می‌شود.

پس از Deploy، `/health` و `/login` را باز کنید، سپس یک اشتراک آزمایشی بسازید و کلاینت واقعی را با کانفیگ WebSocket/XHTTP آزمایش کنید.

## 5 — persistence و مقیاس

برنامه یک فایل state محلی و قفل‌های درون‌پردازشی دارد. برای اجرای این نسخه، یک replica توصیه می‌شود؛ چند replica که هر کدام state محلی یا persistence ساده GitHub دارند ممکن است اطلاعات متناقض ایجاد کنند. قبل از scale-out به دیتابیس مشترک تراکنشی مهاجرت کنید.

## English

Deploy from GitHub, let Railway detect Python, then use `uvicorn main:app --host 0.0.0.0 --port $PORT`. Set `/health` as healthcheck and create a Railway Volume mounted at `/data`; also set `DATA_DIR=/data`. Configure a strong password and secret. A fresh install defaults to `Admin` / `Admin` only if you omit both credentials; change them before public exposure. Keep one replica with the current local/GitHub fallback state model unless you migrate to a shared transactional database.

Official docs: [TCP Proxy](https://docs.railway.com/networking/tcp-proxy) · [Volumes](https://docs.railway.com/volumes)
