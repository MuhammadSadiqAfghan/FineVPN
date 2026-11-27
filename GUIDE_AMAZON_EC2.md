# استقرار FineVPN روی سرور آمازون Amazon EC2

<sup>[بازگشت به راهنمای استقرار](DEPLOYMENT.md) · [راهنمای VPS عمومی](GUIDE_VPS.md)</sup>

این راهنما اجرای FineVPN 2.0 روی یک نمونهٔ Linux در Amazon EC2 را توضیح می‌دهد. روش پیشنهادی، Ubuntu Server LTS با دسترسی SSH و دیسک EBS است.

## ۱. ساخت نمونهٔ EC2

۱. وارد [کنسول Amazon EC2](https://console.aws.amazon.com/ec2/) شوید.
۲. از بخش Instances گزینهٔ Launch instance را انتخاب کنید.
۳. برای Name مقدار `FineVPN` را وارد کنید.
۴. در Application and OS Images یک تصویر رسمی Ubuntu Server LTS را انتخاب کنید.
۵. نوع Instance را متناسب با تعداد کاربران، حجم ترافیک، حافظه و هزینهٔ موردنظر انتخاب کنید؛ یک اندازهٔ ثابت برای همهٔ استفاده‌ها مناسب نیست.
۶. یک Key Pair بسازید و فایل خصوصی `.pem` را دانلود کنید. این فایل را در GitHub یا فضای عمومی قرار ندهید.
۷. یک Security Group اختصاصی ایجاد کنید.
۸. یک دیسک EBS متناسب با داده و خروجی موتور در نظر بگیرید.
۹. نمونه را راه‌اندازی کنید و Public IPv4/DNS را یادداشت کنید.

راهنمای رسمی AWS برای ساخت و اتصال نمونه: [شروع با EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) · [ساخت Key Pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html).

## ۲. تنظیم Security Group

قواعد ورودی پیشنهادی:

| نوع | پورت | مبدأ | توضیح |
|---|---:|---|---|
| SSH | 22/TCP | فقط IP عمومی مدیر | دسترسی مدیریت سرور؛ از `0.0.0.0/0` استفاده نکنید. |
| HTTP | 80/TCP | `0.0.0.0/0` و `::/0` در صورت استفاده از HTTPS خودکار | برای هدایت به HTTPS و اعتبارسنجی دامنه |
| HTTPS | 443/TCP | `0.0.0.0/0` و `::/0` | دسترسی عمومی پنل و WebSocket روی HTTPS |

پورت داخلی `8000` را در اینترنت باز نکنید؛ برنامه پشت Caddy روی `127.0.0.1:8000` اجرا می‌شود. خروجی TCP نیز باید مطابق نیاز Relay و دسترسی به مقصدهای مجاز مسدود نشده باشد. AWS Security Group نقش فایروال نمونه را دارد؛ قواعد را محدود و هدفمند تنظیم کنید. [مستند رسمی Security Group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-security-group.html).

## ۳. اتصال SSH

روی Linux/macOS یا Windows Terminal:

```bash
chmod 600 finevpn-key.pem
ssh -i finevpn-key.pem ubuntu@EC2_PUBLIC_IP
```

اگر به‌جای Ubuntu از Amazon Linux استفاده کرده‌اید، نام کاربر پیش‌فرض معمولاً `ec2-user` است. نام کاربر به سیستم‌عامل تصویر انتخاب‌شده بستگی دارد.

## ۴. نصب FineVPN

```bash
sudo apt update
sudo apt install -y git python3 python3-venv python3-pip curl
sudo adduser --system --group --home /var/lib/finevpn finevpn
sudo mkdir -p /opt/finevpn /var/lib/finevpn
sudo chown -R finevpn:finevpn /opt/finevpn /var/lib/finevpn
sudo -u finevpn git clone https://github.com/MuhammadSadiqAfghan/FineVPN.git /opt/finevpn
sudo -u finevpn python3 -m venv /opt/finevpn/.venv
sudo -u finevpn /opt/finevpn/.venv/bin/pip install --upgrade pip
sudo -u finevpn /opt/finevpn/.venv/bin/pip install -r /opt/finevpn/requirements.txt
```

## ۵. ساخت تنظیمات محرمانه

```bash
sudo install -d -m 700 /etc/finevpn
sudo nano /etc/finevpn/finevpn.env
```

محتوا:

```ini
ADMIN_USERNAME=admin-custom
ADMIN_PASSWORD=REPLACE_WITH_A_LONG_UNIQUE_PASSWORD
SECRET_KEY=REPLACE_WITH_RANDOM_SECRET
DATA_DIR=/var/lib/finevpn
PORT=8000
COOKIE_SECURE=true
PUBLIC_BASE_URL=https://vpn.example.com
FINEVPN_LOGO_URL=https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png
```

برای ساخت Secret تصادفی روی یک ترمینال امن اجرا کنید:

```bash
python3 -c 'import secrets; print(secrets.token_urlsafe(48))'
```

نام دامنه و رمز نمونه را با مقدار واقعی و اختصاصی جایگزین کنید. مقدار `COOKIE_SECURE=true` را تنها زمانی قرار دهید که سرویس از طریق HTTPS ارائه می‌شود. سپس:

```bash
sudo chmod 600 /etc/finevpn/finevpn.env
```

## ۶. ساخت سرویس systemd

```bash
sudo nano /etc/systemd/system/finevpn.service
```

محتوا:

```ini
[Unit]
Description=FineVPN 2.0
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=finevpn
Group=finevpn
WorkingDirectory=/opt/finevpn
EnvironmentFile=/etc/finevpn/finevpn.env
Environment=PYTHONUNBUFFERED=1
ExecStart=/opt/finevpn/.venv/bin/uvicorn main:app --host 127.0.0.1 --port 8000 --workers 1
Restart=always
RestartSec=5
NoNewPrivileges=true
PrivateTmp=true
ProtectHome=true
ProtectSystem=full
ReadWritePaths=/var/lib/finevpn

[Install]
WantedBy=multi-user.target
```

فعال‌سازی:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now finevpn
sudo systemctl status finevpn
sudo journalctl -u finevpn -n 100 --no-pager
```

## ۷. دامنه و HTTPS

یک رکورد DNS نوع A برای زیردامنهٔ خود به IP عمومی EC2 متصل کنید. اگر لازم است IP پس از Stop/Start تغییر نکند، دربارهٔ تخصیص Elastic IP و هزینهٔ مربوط در AWS بررسی کنید.

Caddy را طبق [راهنمای رسمی نصب](https://caddyserver.com/docs/install) نصب و در `/etc/caddy/Caddyfile` قرار دهید:

```caddy
vpn.example.com {
    reverse_proxy 127.0.0.1:8000
}
```

سپس:

```bash
sudo systemctl reload caddy
```

در Security Group پورت‌های 80 و 443 باید مجاز باشند تا دامنه و گواهی HTTPS کار کنند. آدرس دامنه را با مقدار واقعی جایگزین کنید.

## ۸. نصب هسته‌های Xray و Sing-box

برای فعال‌شدن تست اتصال واقعی موتور، هسته‌ها باید روی همین سرور نصب و در PATH باشند:

```bash
sudo bash /opt/finevpn/scripts-install-cores.sh
command -v xray
command -v sing-box
```

این مرحله با اجرای پنل تفاوت دارد. پنل بدون نصب هسته‌ها هم می‌تواند اجرا شود، اما تست واقعی دسترسی کانفیگ‌ها به آن‌ها نیاز دارد.

## ۹. آزمون و پشتیبان‌گیری

۱. `https://vpn.example.com/health` را باز کنید.
۲. ورود مدیر در `/login` را بررسی کنید.
۳. یک اشتراک آزمایشی بسازید و آن را در کلاینت واقعی وارد کنید.
۴. ترافیک عبور دهید و آمار Relay را بررسی کنید.
۵. سرویس را Restart کنید و ماندگاری داده را بسنجید.
۶. از `/var/lib/finevpn` و Volume مربوط به EBS نسخهٔ پشتیبان رمزگذاری‌شده تهیه کنید.

## لینک‌های رسمی

- [شروع کار با EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)
- [ساخت Security Group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-security-group.html)
- [ساخت Key Pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html)
