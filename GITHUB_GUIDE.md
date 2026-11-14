# راهنمای انتشار FineVPN در GitHub

این راهنما برای نگهداری امن سورس و انتشار نسخهٔ `𝒗1.0` است. فایل‌های محرمانه، داده‌های واقعی کاربران و بکاپ‌ها نباید وارد مخزن عمومی شوند.

## نمایش لوگوی رسمی در GitHub

README مخزن از همان تصویر رسمی FineVPN استفاده می‌کند که در پنل ورود، داشبورد و پرتال اشتراک نمایش داده می‌شود. نشانی تصویر در README به‌صورت مستقیم از میزبان تصویر بارگذاری می‌شود؛ برای نمایش در GitHub باید تصویر در نشانی عمومی زیر قابل دسترس بماند:

- https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png

اگر نشانی تصویر تغییر کرد، مقدار `src` تصویر در سربرگ `README.md` و ثابت لوگو در `pages.py` را هم‌زمان به‌روزرسانی کنید.

## ۱) ساخت مخزن

1. در GitHub یک مخزن جدید بسازید؛ برای پروژه‌ای که احتمال دارد فایل state یا گزارش عملیاتی در آن قرار گیرد، مخزن `Private` انتخاب مطمئن‌تری است.
2. فایل ZIP را در یک پوشهٔ محلی استخراج کنید.
3. مطمئن شوید `.env`، پوشهٔ `data/`، `backups/`، کلیدها و فایل‌های نشست وارد مخزن نمی‌شوند؛ `.gitignore` این مسیرها را پوشش می‌دهد.
4. سورس را commit و به branch اصلی push کنید.

```bash
git init
git add .
git status --short
# پیش از commit خروجی را بررسی کنید؛ فایل .env یا data نباید دیده شود.
git commit -m "Release FineVPN v1.0"
git branch -M main
git remote add origin https://github.com/OWNER/REPOSITORY.git
git push -u origin main
```

## ۲) Secrets و داده‌ها

- `ADMIN_PASSWORD` و `SECRET_KEY` را فقط در بخش Secrets میزبان وارد کنید؛ هرگز در README، Issue، Screenshot یا commit نگذارید.
- مقدار `SECRET_KEY` باید تصادفی و در طول عمر نصب ثابت بماند.
- فایل `data/panel_state.json` می‌تواند شناسه‌های اشتراک، UUIDها، دادهٔ مصرف و هش رمز را در خود داشته باشد؛ آن را در GitHub منتشر نکنید.
- برای GitHub persistence از یک مخزن خصوصی و token با حداقل مجوز لازم استفاده کنید. Token را در GitHub Actions Secrets یا Environment Variables میزبان ذخیره کنید.
- فایل‌های Backup را جدا از مخزن سورس و با دسترسی محدود نگهداری کنید.

## ۳) تست قبل از انتشار

از ریشهٔ پروژه اجرا کنید:

```bash
python -m py_compile main.py pages.py relay_vless.py speed_limit.py xhttp_siz10.py test_regressions.py
python -m unittest -v test_regressions.py
```

هر دو دستور باید بدون خطا پایان یابند. پس از استقرار نیز `/health`، `/login`، ذخیره‌سازی پایدار و تهیه/بازیابی Backup را بررسی کنید.

## ۴) انتشار Release با برچسب v1.0

در GitHub به بخش **Releases → Draft a new release** بروید، یک tag با نام `v1.0` بسازید، عنوان `FineVPN v1.0` بگذارید و نکات `CHANGELOG.md` را در توضیحات Release قرار دهید. نسخهٔ پایتونی/ API همچنان `1.0.0` است؛ برچسب نمایشی محصول `𝒗1.0` است.

## ۵) استقرار و محدودیت میزبان

پیش از Deploy، سیاست قابل‌قبول استفادهٔ میزبان را بخوانید. مخزن فعلی یک برنامهٔ ترکیبی شامل پنل، API اشتراک و اجزای VPN/Proxy است. **این نسخه را روی Railway مستقر نکنید**؛ مستندات رسمی Railway VPN، Proxy و سرویس‌های ناشناس‌ساز را ممنوع می‌دانند. مخفی‌کردن پروتکل، تغییر دامنه یا تنظیم مجدد health check راه‌حل سازگار نیست. برای استقرار کامل، ارائه‌دهنده‌ای انتخاب کنید که این نوع سرویس را مجاز بداند.

- [سیاست استفادهٔ قابل‌قبول Railway](https://railway.com/legal/acceptable-use)
- [مستندات Trust & Safety Railway](https://docs.railway.com/platform/trust-and-safety)
- [راهنمای سازگاری Railway در این مخزن](DEPLOY_RAILWAY.md)

## ۶) چک‌لیست نهایی

- [ ] هیچ `.env`، token، UUID واقعی یا backup در commit نیست.
- [ ] رمز ورود پیش‌فرض قبل از عمومی‌شدن تعویض شده است.
- [ ] `SECRET_KEY` امن و پایدار است.
- [ ] Volume/Disk واقعاً mount شده و فقط به تنظیم `DATA_DIR` اکتفا نشده است.
- [ ] تست‌ها موفق هستند.
- [ ] سیاست میزبان برای همهٔ اجزای برنامه بررسی شده است.
