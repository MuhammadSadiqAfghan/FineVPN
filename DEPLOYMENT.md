<div align="center">
  <h1>راهنمای استقرار FineVPN 2.0</h1>
  <p>برای بازکردن آموزش، روی لوگوی محیط موردنظر کلیک کنید.</p>
</div>

<div align="center">
  <a href="GUIDE_AMAZON_EC2.md"><img src="https://img.shields.io/badge/Amazon%20EC2-آموزش%20استقرار-FF9900?style=for-the-badge&amp;logo=amazonaws&amp;logoColor=white" alt="Amazon EC2" /></a>
  <a href="GUIDE_VPS.md"><img src="https://img.shields.io/badge/VPS-سرور%20اختصاصی-24292F?style=for-the-badge&amp;logo=linux&amp;logoColor=white" alt="VPS" /></a>
  <a href="GUIDE_VM.md"><img src="https://img.shields.io/badge/VM-ماشین%20مجازی-183A61?style=for-the-badge&amp;logo=virtualbox&amp;logoColor=white" alt="ماشین مجازی" /></a>
  <a href="GUIDE_SHARED_HOSTING.md"><img src="https://img.shields.io/badge/Hosting-هاست%20اشتراکی-FF6C2C?style=for-the-badge&amp;logo=cpanel&amp;logoColor=white" alt="هاست اشتراکی" /></a>
  <a href="GUIDE_RAILWAY.md"><img src="https://img.shields.io/badge/Railway-استقرار%20ابری-0B0D0E?style=for-the-badge&amp;logo=railway&amp;logoColor=white" alt="Railway" /></a>
  <a href="GUIDE_RENDER.md"><img src="https://img.shields.io/badge/Render-استقرار%20ابری-46E3B7?style=for-the-badge&amp;logo=render&amp;logoColor=111111" alt="Render" /></a>
</div>

## انتخاب محیط مناسب

| محیط | مناسب برای | نکتهٔ مهم |
|---|---|---|
| Amazon EC2 | اجرای لینوکس با کنترل کامل در AWS | Security Group، کلید SSH، IP عمومی، دیسک EBS و هزینهٔ مصرفی را مدیریت کنید. |
| VPS / سرور اختصاصی | انتخاب پیشنهادی برای پنل و تونل واقعی | کنترل کامل‌تر روی TCP خروجی، WebSocket، فایروال، TLS و فرایند دائمی. |
| ماشین مجازی | تست، شبکهٔ داخلی یا میزبانی روی سخت‌افزار خودتان | برای دسترسی اینترنتی به IP قابل‌دسترسی، Bridged یا Port Forward درست نیاز دارید. |
| Railway | میزبانی پنل FastAPI با Container و Volume | Volume را به `/data` وصل کنید و یک Replica/Worker نگه دارید. تست هسته‌ها نیازمند نصب Xray و Sing-box است. |
| هاست اشتراکی | میزبانی سایت ثابت و مستندات؛ پنل فقط در صورت پشتیبانی کامل میزبان | بیشتر هاست‌های اشتراکی برای Relay دائمی، WebSocket و TCP خروجی طراحی نشده‌اند. |
| Render | سرویس وب و آزمایش پنل | محدودیت دیسک پایدار و خواب سرویس را در پلن انتخابی بررسی کنید. |

## راهنمای مستقل هر محیط

1. [Amazon EC2 با Ubuntu](GUIDE_AMAZON_EC2.md)
2. [VPS و سرور اختصاصی Linux](GUIDE_VPS.md)
3. [ماشین مجازی VirtualBox / VMware / Proxmox](GUIDE_VM.md)
4. [هاست اشتراکی و cPanel](GUIDE_SHARED_HOSTING.md)
5. [Railway.app](GUIDE_RAILWAY.md)
6. [Render](GUIDE_RENDER.md)

## چک‌لیست مشترک پس از استقرار

- مقدارهای `ADMIN_USERNAME`، `ADMIN_PASSWORD` و `SECRET_KEY` را از طریق تنظیمات امن میزبان تعریف کنید.
- `DATA_DIR` را روی مسیر Volume یا دیسک واقعاً پایدار قرار دهید.
- برای دسترسی عمومی HTTPS را فعال کنید و `COOKIE_SECURE=true` بگذارید.
- سرویس را با یک Worker اجرا کنید.
- مسیر `/health` و صفحهٔ `/login` را بررسی کنید.
- یک گروه آزمایشی بسازید و خروجی اشتراک را با کلاینت واقعی آزمایش کنید.
- پس از انتقال داده، Restart/Deploy را انجام دهید و ماندگاری اطلاعات را دوباره بررسی کنید.
- برای اطمینان از سلامت کانفیگ‌های جمع‌آوری‌شده، Xray و Sing-box را روی میزبان نصب کنید و تست اتصال واقعی را اجرا کنید.

## منابع رسمی پلتفرم‌ها

- [مستندات Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) · [Security Group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-security-group.html)
- [مستندات Railway](https://docs.railway.com/) · [Volumeها](https://docs.railway.com/volumes) · [سرویس‌ها](https://docs.railway.com/services)
- [مستندات Render](https://render.com/docs)
- [مستندات Docker](https://docs.docker.com/)
