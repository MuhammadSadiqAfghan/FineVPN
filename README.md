<div align="center">
  <a href="https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png">
    <img src="https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png" width="210" alt="لوگوی اصلی FineVPN" />
  </a>
  <h1>𝑭𝒊𝒏𝒆𝑽𝑷𝑵</h1>
  <h3>نسخهٔ ᵛ²⋅⁰ · پنل مدیریت اشتراک و موتور پردازش پروکسی</h3>
  <p>طراحی کاملاً مشکی، سفید و قرمز · رابط فارسی و راست‌چین · سازگار با موبایل، آیفون، آیپد، تبلت و لپ‌تاپ</p>
  <p>
    <img src="https://img.shields.io/badge/نسخه-2.0.0-E60023?style=for-the-badge" alt="نسخه 2.0.0" />
    <img src="https://img.shields.io/badge/زبان-فارسی-FFFFFF?style=for-the-badge&amp;labelColor=111111" alt="زبان فارسی" />
    <img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&amp;logo=python&amp;logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/FastAPI-API-009688?style=for-the-badge&amp;logo=fastapi&amp;logoColor=white" alt="FastAPI" />
    <img src="https://img.shields.io/badge/رابط-واکنش_گرا-E60023?style=for-the-badge" alt="رابط واکنش گرا" />
  </p>
  <p>
    <a href="INSTALL.md">نصب و راه‌اندازی</a> ·
    <a href="DEPLOYMENT.md">همهٔ روش‌های استقرار</a> ·
    <a href="GUIDE_PANEL_SUBSCRIPTIONS.md">راهنمای پنل و اشتراک</a> ·
    <a href="GUIDE_PROXY_ENGINE.md">راهنمای موتور پروکسی</a> ·
    <a href="SECURITY.md">امنیت</a>
  </p>
</div>

---

## روش‌های اجرا و استقرار

برای دیدن آموزش هر محیط، روی نشان همان پلتفرم کلیک کنید. هر راهنما جداگانه و به زبان فارسی نوشته شده است.

<div align="center">
  <a href="GUIDE_AMAZON_EC2.md"><img src="https://img.shields.io/badge/Amazon%20EC2-استقرار%20روی%20AWS-FF9900?style=for-the-badge&amp;logo=amazonaws&amp;logoColor=white" alt="راهنمای سرور آمازون EC2" /></a>
  <a href="GUIDE_VPS.md"><img src="https://img.shields.io/badge/VPS-سرور%20لینوکس-24292F?style=for-the-badge&amp;logo=linux&amp;logoColor=white" alt="راهنمای VPS" /></a>
  <a href="GUIDE_SHARED_HOSTING.md"><img src="https://img.shields.io/badge/Shared%20Hosting-هاست%20اشتراکی-FF6C2C?style=for-the-badge&amp;logo=cpanel&amp;logoColor=white" alt="راهنمای هاست اشتراکی" /></a>
  <a href="GUIDE_VM.md"><img src="https://img.shields.io/badge/Virtual%20Machine-ماشین%20مجازی-183A61?style=for-the-badge&amp;logo=virtualbox&amp;logoColor=white" alt="راهنمای ماشین مجازی" /></a>
  <a href="GUIDE_RAILWAY.md"><img src="https://img.shields.io/badge/Railway-استقرار%20ابری-0B0D0E?style=for-the-badge&amp;logo=railway&amp;logoColor=white" alt="راهنمای Railway" /></a>
  <a href="GUIDE_RENDER.md"><img src="https://img.shields.io/badge/Render-استقرار%20ابری-46E3B7?style=for-the-badge&amp;logo=render&amp;logoColor=111111" alt="راهنمای Render" /></a>
</div>

| محیط | مناسب برای | راهنمای فارسی |
|---|---|---|
| Amazon EC2 | سرور لینوکسی ابری با دسترسی کامل به سیستم‌عامل و شبکه | [آموزش EC2](GUIDE_AMAZON_EC2.md) |
| VPS یا سرور اختصاصی | اجرای دائمی پنل و Relay با کنترل فایروال و شبکه | [آموزش VPS](GUIDE_VPS.md) |
| ماشین مجازی | آزمایش، شبکهٔ داخلی یا سرور مجازی روی Proxmox / VMware / VirtualBox | [آموزش ماشین مجازی](GUIDE_VM.md) |
| Railway | اجرای سرویس FastAPI با Volume پایدار | [آموزش Railway](GUIDE_RAILWAY.md) |
| هاست اشتراکی | فقط در صورت پشتیبانی واقعی از Python ASGI، WebSocket و فرایند دائمی | [بررسی سازگاری هاست](GUIDE_SHARED_HOSTING.md) |
| Render | اجرای پنل وب؛ محدودیت‌های دیسک و خواب سرویس را بررسی کنید | [آموزش Render](GUIDE_RENDER.md) |

> **پیشنهاد برای اجرای کامل تونل:** VPS لینوکس یا Amazon EC2 با دسترسی شبکه و ذخیره‌سازی پایدار، انتخاب قابل‌کنترل‌تری است. اجرای موفق صفحهٔ وب روی یک پلتفرم به‌تنهایی ثابت نمی‌کند همهٔ مسیرهای VLESS، WebSocket و XHTTP روی همان پلتفرم قابل استفاده‌اند؛ اتصال واقعی باید با کلاینت آزمایش شود.

## امکانات FineVPN 2.0

### پنل مدیریت و اشتراک

- داشبورد مدیریتی با آمار، وضعیت سیستم، مصرف ترافیک، رخدادها و اتصال‌های فعال.
- مدیریت لینک‌ها و پروفایل‌های VLESS WebSocket و XHTTP در حالت‌های Packet-up و Stream-up.
- ساخت گروه اشتراک با حجم مشترک، زمان اعتبار، محدودیت IP، رمز اختیاری و صفحهٔ عمومی.
- ساخت سریع شش پروفایل WebSocket تأییدشده برای هر گروه.
- تمدید اشتراک، حفظ یا صفرکردن مصرف، غیرفعال‌سازی و مدیریت لینک‌های وابسته.
- خروجی اشتراک Base64، لینک مستقیم، QR و صفحهٔ نمایش وضعیت اشتراک.
- مدیریت دسته‌بندی‌ها، نشست‌های مدیر، لغو نشست‌ها، گزارش فعالیت و آمار اتصال‌ها.
- پشتیبان‌گیری، بازیابی از فایل یا Snapshot و خروجی گرفتن از لینک‌ها.
- طراحی راست‌چین و واکنش‌گرا برای گوشی Android، آیفون، آیپد، تبلت و لپ‌تاپ.

### موتور دریافت و پردازش پروکسی

- دریافت منابع HTTP/HTTPS، لینک‌های GitHub Raw، صفحه‌های عمومی کانال تلگرام و ورودی‌های `ssconf`.
- استخراج و رمزگشایی Base64، تشخیص پروتکل، پاک‌سازی و اعتبارسنجی کانفیگ‌ها.
- حذف موارد تکراری بر اساس شناسهٔ محاسبه‌شده، غنی‌سازی اطلاعات کشور و نام‌گذاری.
- تست اتصال با Xray و Sing-box در صورت نصب بودن باینری‌های مربوط روی میزبان.
- فیلتر امنیتی و ساخت خروجی‌های Clash، Sing-box، Xray و Xray Fragment.
- خروجی تفکیک‌شده بر اساس کشور، پروفایل Hiddify، گزارش عملکرد منابع، آمار و نمودارها.
- اجرای موتور از داخل پنل یا با فرمان خط فرمان.

پروتکل‌های قابل‌شناسایی در موتور شامل VLESS، VMess، Trojan، Shadowsocks، Hysteria2، TUIC و WireGuard هستند. پشتیبانی هر فرمت خروجی به امکانات همان تبدیل‌کننده وابسته است؛ بنابراین ممکن است یک پروتکل در Parser شناسایی شود ولی در خروجی مشخصی صادر نشود.

**تست اتصال واقعی:** وجود کانفیگ در خروجی به معنی سالم‌بودن اتصال نیست. برای تست واقعی باید باینری‌های Xray و Sing-box روی میزبان نصب و در `PATH` قابل دسترسی باشند. اگر هسته‌ای نصب نباشد، برنامه آن مرحله را به‌عنوان تست اتصال موفق گزارش نمی‌کند.

## نصب سریع روی Linux

پیش‌نیازها: Python 3.11 یا جدیدتر، دسترسی ترمینال و امکان اجرای یک فرایند دائمی. برای اجرای عمومی، دامنه و HTTPS توصیه می‌شود.

```bash
git clone https://github.com/MuhammadSadiqAfghan/FineVPN.git
cd FineVPN
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

برای ساخت مقدارهای اختصاصی و اجرای برنامه:

```bash
export ADMIN_USERNAME='نام-کاربری-مدیر'
export ADMIN_PASSWORD='یک-رمز-عبور-طولانی-و-منحصر-به-فرد'
export SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(48))')"
export DATA_DIR="$PWD/data"
export COOKIE_SECURE=false
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 1
```

سپس `http://SERVER-IP:8000/login` را باز کنید. برای اجرای پشت HTTPS، مقدار `COOKIE_SECURE=true` باشد. دستورهای نصب دائمی و سرویس systemd در [راهنمای VPS](GUIDE_VPS.md) آمده است.

> فایل `.env.example` فقط نمونهٔ متغیرهاست؛ خود برنامه آن را به‌طور خودکار بارگذاری نمی‌کند. در راهنمای [متغیرهای محیطی](GUIDE_ENVIRONMENT_STORAGE.md) روش امن بارگذاری آن توضیح داده شده است.

## نشانی‌های مهم برنامه

| مسیر | کاربرد |
|---|---|
| `/` | صفحهٔ اصلی عمومی FineVPN |
| `/login` | ورود مدیر |
| `/dashboard` | پنل مدیریت پس از ورود |
| `/health` | بررسی سلامت برنامه |
| `/p/{uuid_key}` | صفحهٔ عمومی گروه اشتراک |
| `/sub-group/{uuid_key}` | خروجی متنی Base64 اشتراک گروه |
| `/sub/{uuid}` | خروجی اشتراک یک لینک |
| `/api/engine/status` | وضعیت موتور پردازش؛ نیازمند ورود مدیر |

## مالکیت برند و مجوز اجزای موتور

نام و هویت بصری FineVPN تابع اعلان مالکیت داخل [COPYRIGHT.md](COPYRIGHT.md) است. مجوز جزء موتور پردازش منتقل‌شده در [ENGINE_LICENSE.txt](ENGINE_LICENSE.txt) نگهداری شده است؛ مجوز یک جزء شخص ثالث را به معنی واگذاری خودکار حقوق برند و لوگوی FineVPN در نظر نگیرید.

## داده‌ها و ارتقا از نسخهٔ قبلی

نسخهٔ ۲ از SQLite در مسیر `DATA_DIR/finevpn.sqlite3` استفاده می‌کند. در نخستین اجرا، برنامه تلاش می‌کند فایل وضعیت قدیمی `panel_state.json` را از مسیر داده پیدا کند و لینک‌ها، گروه‌ها، دسته‌بندی‌ها و مشخصات مدیر را وارد پایگاه دادهٔ جدید کند. پیش از اولین اجرا، از پوشهٔ دادهٔ نسخهٔ قبل یک نسخهٔ پشتیبان جداگانه بگیرید و فایل پایدار `panel_secret.key` را نگه دارید.

در محیط عملیاتی از Volume یا دیسک پایدار استفاده کنید. برنامه را با یک Worker اجرا کنید؛ رجیستری نشست‌های تونل و بخشی از شمارش ترافیک در حافظهٔ فرایند نگهداری می‌شود.

## مستندات فارسی

- [نصب و راه‌اندازی](INSTALL.md)
- [فهرست روش‌های استقرار](DEPLOYMENT.md)
- [سرور آمازون EC2](GUIDE_AMAZON_EC2.md)
- [VPS و سرور اختصاصی](GUIDE_VPS.md)
- [ماشین مجازی](GUIDE_VM.md)
- [هاست اشتراکی](GUIDE_SHARED_HOSTING.md)
- [Railway](GUIDE_RAILWAY.md) · [Render](GUIDE_RENDER.md)
- [مدیریت پنل و گروه‌های اشتراک](GUIDE_PANEL_SUBSCRIPTIONS.md)
- [موتور جمع‌آوری و تبدیل پروکسی](GUIDE_PROXY_ENGINE.md)
- [نصب کلاینت‌ها روی Android / iPhone / iPad / Windows / macOS / Linux](GUIDE_CLIENTS.md)
- [متغیرهای محیطی و ذخیره‌سازی](GUIDE_ENVIRONMENT_STORAGE.md)
- [پشتیبان‌گیری و بازیابی](GUIDE_BACKUP_RESTORE.md)
- [آزمون اتصال و آمار](GUIDE_METRICS_TESTING.md)
- [عیب‌یابی](GUIDE_TROUBLESHOOTING.md) · [امنیت](SECURITY.md)
- [راهنمای بارگذاری در GitHub و نمایش لوگو](UPLOAD_GITHUB.md) · [گزارش آزمون](TEST_REPORT.md) · [اعلان حق نشر FineVPN](COPYRIGHT.md)

---

<div align="center">
  <a href="https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png">
    <img src="https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png" width="92" alt="FineVPN" />
  </a>
  <p><strong>𝑭𝒊𝒏𝒆𝑽𝑷𝑵 · ᵛ²⋅⁰</strong></p>
  <p>اتصال بدون مرز · پنل فارسی · مدیریت یکپارچهٔ اشتراک</p>
</div>
