# نصب FineVPN روی VPS و سرور اختصاصی Linux

<sup>[بازگشت به راهنمای استقرار](DEPLOYMENT.md) · [Amazon EC2](GUIDE_AMAZON_EC2.md)</sup>

این گزینه برای اجرای مداوم پنل و Relay توصیه می‌شود؛ چون کنترل بیشتری روی فایروال، TCP خروجی، WebSocket، TLS و ذخیره‌سازی دارید. مراحل زیر برای Ubuntu/Debian نوشته شده‌اند.

## ۱. آماده‌سازی

با کاربر دارای دسترسی sudo وارد سرور شوید:

```bash
sudo apt update
sudo apt install -y git python3 python3-venv python3-pip curl
```

## ۲. ساخت کاربر و دریافت پروژه

```bash
sudo adduser --system --group --home /var/lib/finevpn finevpn
sudo mkdir -p /opt/finevpn /var/lib/finevpn
sudo chown -R finevpn:finevpn /opt/finevpn /var/lib/finevpn
sudo -u finevpn git clone https://github.com/MuhammadSadiqAfghan/FineVPN.git /opt/finevpn
sudo -u finevpn python3 -m venv /opt/finevpn/.venv
sudo -u finevpn /opt/finevpn/.venv/bin/pip install --upgrade pip
sudo -u finevpn /opt/finevpn/.venv/bin/pip install -r /opt/finevpn/requirements.txt
```

## ۳. تنظیم متغیرهای امن

```bash
sudo install -d -m 700 /etc/finevpn
sudo nano /etc/finevpn/finevpn.env
```

این موارد را داخل فایل قرار دهید و نمونه‌ها را عوض کنید:

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

Secret تصادفی را با این فرمان تولید کنید:

```bash
python3 -c 'import secrets; print(secrets.token_urlsafe(48))'
sudo chmod 600 /etc/finevpn/finevpn.env
```

## ۴. ایجاد سرویس دائمی

```bash
sudo nano /etc/systemd/system/finevpn.service
```

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

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now finevpn
sudo systemctl status finevpn
sudo journalctl -u finevpn -f
```

## ۵. اتصال دامنه و HTTPS با Caddy

رکورد DNS دامنه را به IP سرور متصل کنید. Caddy را طبق [راهنمای رسمی](https://caddyserver.com/docs/install) نصب کنید و `/etc/caddy/Caddyfile` را با دامنهٔ خود تنظیم کنید:

```caddy
vpn.example.com {
    reverse_proxy 127.0.0.1:8000
}
```

```bash
sudo systemctl reload caddy
```

Caddy عبور WebSocket را از طریق reverse proxy پشتیبانی می‌کند. پورت 8000 را عمومی نکنید؛ برنامه روی localhost اجرا شده و HTTPS از Caddy ارائه می‌شود.

## ۶. فایروال

پیش از فعال‌کردن UFW مطمئن شوید پورت SSH فعلی مجاز است:

```bash
sudo ufw allow OpenSSH
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
sudo ufw status
```

برای عملکرد Relay، دسترسی TCP خروجی به مقصدهای مجاز لازم است. محدودیت‌های شبکهٔ ارائه‌دهنده را هم بررسی کنید.

## ۷. نصب هسته‌های تست

```bash
sudo bash /opt/finevpn/scripts-install-cores.sh
command -v xray
command -v sing-box
```

تست واقعی کانفیگ‌ها فقط وقتی قابل انجام است که هسته‌های مربوط روی همین سرور نصب باشند.

## ۸. آزمون و به‌روزرسانی

پس از راه‌اندازی، `/health` و `/login` را بررسی کنید، اشتراک آزمایشی بسازید و با کلاینت واقعی اتصال و انتقال داده را آزمایش کنید.

پیش از به‌روزرسانی:

```bash
sudo systemctl stop finevpn
sudo tar -czf "$HOME/finevpn-data-$(date +%Y%m%d-%H%M%S).tar.gz" -C /var/lib finevpn
sudo -u finevpn git -C /opt/finevpn pull --ff-only
sudo -u finevpn /opt/finevpn/.venv/bin/pip install -r /opt/finevpn/requirements.txt
sudo systemctl start finevpn
sudo journalctl -u finevpn -n 100 --no-pager
```

## نکات مهم

- برنامه را با یک Worker اجرا کنید؛ اجرای چند Worker یا چند Replica بدون اشتراک وضعیت می‌تواند شمارش نشست‌ها و ترافیک را ناسازگار کند.
- `DATA_DIR` باید برای کاربر `finevpn` قابل نوشتن و روی دیسک پایدار باشد.
- پیش از جایگزینی نسخه، از تمام پوشهٔ داده و فایل `panel_secret.key` پشتیبان بگیرید.
- `/api/ping` فقط RTT پنل است و پینگ واقعی داخل تونل محسوب نمی‌شود.
