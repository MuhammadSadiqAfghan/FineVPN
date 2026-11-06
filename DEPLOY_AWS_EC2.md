<div align="center"><img src="https://cdn.simpleicons.org/amazonaws/FF9900" height="46" alt="AWS" /></div>

# راهنمای استقرار 𝑭𝒊𝒏𝒆𝑽𝑷𝑵 روی AWS EC2

این راهنما اجرای کامل برنامه روی ماشین مجازی EC2 را توضیح می‌دهد. چون EC2 دسترسی سیستم‌عامل و شبکه می‌دهد، برای میزبانی کامل این پروژه مناسب‌ترین مسیر ابری در میان گزینه‌های فهرست‌شده است.

## پیش‌نیاز

- یک EC2 Linux instance (Amazon Linux 2023 یا Ubuntu LTS)
- IP عمومی ثابت / Elastic IP و دامنه
- دسترسی SSH و Security Group
- Docker Engine و Docker Compose plugin

## مرحله 1 — ساخت نمونه و شبکه

1. در AWS Console نمونه EC2 بسازید و یک Key Pair دانلود و امن نگهداری کنید.
2. برای Security Group فقط پورت‌های زیر را باز کنید:
   - TCP `22` از IP مدیریت خودتان، نه `0.0.0.0/0` در حالت دائمی.
   - TCP `80` و `443` از اینترنت برای HTTP redirect و HTTPS.
3. پورت `8000` را عمومی باز نکنید؛ Compose آن را فقط روی loopback میزبان bind می‌کند.
4. Elastic IP را متصل و دامنه را به آن اشاره دهید.

## مرحله 2 — آماده‌سازی سیستم

```bash
# Amazon Linux 2023
sudo dnf update -y
sudo dnf install -y docker git
sudo systemctl enable --now docker
sudo usermod -aG docker ec2-user
```

پس از `usermod` یک‌بار خارج و دوباره وارد شوید، یا دستورات Docker را با `sudo` اجرا کنید. Docker Compose plugin را طبق مستندات توزیع خود نصب کنید.

## مرحله 3 — انتقال پروژه

ZIP را روی سرور آپلود و استخراج کنید یا مخزن Git خصوصی/عمومی خودتان را clone کنید. وارد همان پوشه‌ای شوید که `compose.yaml` قرار دارد.

```bash
cp .env.example .env
nano .env
```

مقادیر پیشنهادی:

```dotenv
PORT=8000
DATA_DIR=/data
ADMIN_USERNAME=Admin
ADMIN_PASSWORD=CHANGE-THIS-TO-A-LONG-UNIQUE-PASSWORD
SECRET_KEY=REPLACE-WITH-A-LONG-RANDOM-SECRET
TRUST_PROXY_HEADERS=1
TRUSTED_PROXIES=127.0.0.1,::1
```

## مرحله 4 — اجرا

```bash
docker compose up -d --build
docker compose ps
docker compose logs --tail=100 finevpn
curl -fsS http://127.0.0.1:8000/health
```

## مرحله 5 — TLS با Caddy

1. DNS دامنه را به Elastic IP اشاره دهید.
2. Caddy را روی میزبان نصب کنید.
3. `Caddyfile` را در `/etc/caddy/Caddyfile` کپی و `DOMAIN` را با دامنهٔ واقعی جایگزین کنید:

```caddy
vpn.example.com {
    encode zstd gzip
    reverse_proxy 127.0.0.1:8000
}
```

4. سرویس Caddy را reload کنید و مطمئن شوید پورت‌های 80 و 443 از Security Group عبور می‌کنند.
5. از `https://your-domain/login` وارد شوید.

## ورود اولیه

اگر تنظیمات ورود را حذف کنید و `DATA_DIR` خالی باشد، نام کاربری و رمز اولیه هر دو `Admin` است. **این مقدار پیش‌فرض را قبل از عمومی‌کردن سرویس تغییر دهید.** اگر state قبلی وجود داشته باشد، credential ذخیره‌شده حفظ می‌شود.

## پایداری و نگهداری

- مسیر `/data` به bind mount محلی وصل است و پس از حذف/ساخت دوباره کانتینر باقی می‌ماند.
- از `docker compose logs`، `/health` و بکاپ پنل استفاده کنید.
- برای بروزرسانی: ابتدا backup، سپس `docker compose up -d --build`.
- دیسک، RAM، CPU و مصرف پهنای باند EC2 را بر اساس بار واقعی کاربران مانیتور کنید.
- کلید PEM، `.env`، بکاپ و لینک اشتراک را عمومی نکنید.

## English

Launch a Linux EC2 instance, attach an Elastic IP, allow SSH only from your administrator IP, and allow inbound TCP 80/443. Install Docker, upload the project, set a unique `ADMIN_PASSWORD` and `SECRET_KEY`, and run `docker compose up -d --build`. Caddy terminates TLS and proxies to `127.0.0.1:8000`. A fresh installation with no configured credentials defaults to `Admin` / `Admin`; change it before public exposure. Keep `/data` backed up.

منابع رسمی: [EC2 Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-security-group.html) · [EC2 User Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)
