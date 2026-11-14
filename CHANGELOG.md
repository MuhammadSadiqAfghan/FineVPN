## FineVPN 𝒗₂.₀ — بازطراحی آبی شیشه‌ای و قابلیت‌های تازه

- بازطراحی ساختار واقعی داشبورد بر پایهٔ تصویر مرجع: نوار کناری، سربرگ شیشه‌ای، کارت‌های آماری نئونی، دو پنل بزرگ «پنل ساب» و «درگاه و پنل ورود»، جدول آخرین کانفیگ‌ها و کارت وضعیت سرور.
- اصلاح کنترل روشن/تاریک؛ انتخاب کاربر ذخیره می‌شود و پس از بارگذاری مجدد صفحه باقی می‌ماند.
- افزودن IP و پورت دلخواه به ساخت گروه سریع؛ هر ۲۴ کانفیگ یک گروه، مقصد سفارشی را می‌گیرند و زیر همان اشتراک باقی می‌مانند.
- بازطراحی صفحه ورود و پرتال اشتراک با تم آبی شیشه‌ای، حلقه‌های پس‌زمینه کم‌رنگ و چیدمان واکنش‌گرا.
- یکپارچه‌سازی نشان تجاری ارائه‌شده در سربرگ، صفحه ورود و پرتال اشتراک؛ نمایش نسخه 𝒗₂.₀ و رابط کاربری فارسی.
- افزودن مقصد IP دلخواه IPv4/IPv6 و درگاه دلخواه به هنگام ساخت و ویرایش کانفیگ؛ حفظ دامنه در SNI و Host برای سازگاری TLS/CDN.
- افزودن ابزار آزمایش ICMP برای حداکثر ۵۰۰ IP عمومی با سنجش زمان پاسخ، دسته‌بندی نتیجه‌ها، کپی تکی و کپی گروهی.
- محدودسازی ابزار آزمایش به IPهای عمومیِ واردشده توسط مدیر، یک اجرای هم‌زمان و فاصلهٔ زمانی بین آزمایش‌ها؛ این نتیجه سلامت تونل یا «تمیزبودن» IP را تضمین نمی‌کند.
- حفظ گروه‌های اشتراک، سهمیه مشترک، انقضا، QR، بکاپ، نشست‌ها، گزارش‌ها و منطق حسابداری ترافیک نسخه قبل.

## FineVPN 𝒗1.0 — official logo update

- Applied the user-provided FineVPN artwork consistently to login, admin sidebar/mobile header, subscription portal, contact areas, favicon, and Apple touch icon.
- Updated the GitHub README header and publishing guide to use the same official image URL.
- Kept the original responsive glass layout and application behavior unchanged.

## FineVPN 𝒗1.0 — UI and release polish (backend version 1.0.0)

- Unified the admin dashboard, login page, and public subscription portal under one midnight-glass visual system.
- Replaced externally hosted logo images with a built-in vector brand mark and local SVG favicon.
- Improved mobile safe-area spacing, touch targets, keyboard focus states, and reduced-motion behavior.
- Made `/health` reflect writable-state readiness and return HTTP 503 when persistent state cannot be written; added a matching Docker health check.
- Added a dedicated GitHub publishing and secret-handling guide.
- Corrected the README's Railway compatibility claims and removed the Railway auto-deploy manifest for the combined VPN/proxy workload.
- Preserved existing API behavior and quota/accounting logic.

# Changelog

## 1.0.0 — 2026-11-06

- Replaced serial 24-config group creation with one atomic API request and one local save; queued GitHub persistence separately from panel response time.
- Reduced repeated quota-lock work on small XHTTP upload frames and balanced the XHTTP queue/socket limits (32 × 128 KiB downlink queue per session) to reduce bufferbloat while retaining bounded throughput headroom.
- Optimized subscription live-session aggregation to scan active tunnels once per refresh.
- Added shutdown flushing for the final queued cloud backup snapshot.
- Improved responsive glass styling and made the login password visibility control independent of the external icon font.

- Added established-tunnel and unique-IP metrics separately; removed the fixed protocol-distribution sample values.
- Reworked the public portal with quota and validity rings, exact remaining time, live sessions, and a compact diagnostic panel.
- Made shared quota accounting atomic across concurrent WS/XHTTP sessions and reject chunks that would exceed the remaining quota.
- Separated shared-group reset from per-config counters and propagated group renewals to child expiry dates.
- Added explicit expired/quota-exhausted states without overwriting an operator's manual enabled/disabled setting.
- Added regression tests for shared quota, concurrent usage, traffic directions, group reset and renewal.

## 1.0.0 — 2026-11-03

- Reworked the admin and public subscription page styling around a fixed midnight glass theme with stronger text contrast and compact, aligned controls.
- Removed light/dark theme switches; the interface now remains dark.
- Replaced the misleading browser response-time tile with per-configuration online/offline status and live-connection totals.
- Added compact official client links, including v2rayNG GitHub Releases and Android app-store destinations.
- Persisted group-level expiry explicitly and aligned the live access gate, public portal and `subscription-userinfo` expiry value.
- Added cumulative group upload/download counters and legacy-state normalization so traffic remains visible after an individual config is reset or removed.
- Batched persistence of high-frequency traffic updates for grouped and standalone links; no disk/GitHub write is triggered for every relay frame.
- Added readback of group duration/expiry, corrected per-config quota bars so shared quota is not misrepresented as an individual limit, and hardened quick-create verification.
- Added regression tests for Python compilation, quota accounting, session behavior, and group creation.
- Updated documentation and release metadata.

## 1.0.0

- Initial project release.

## 1.0.0 — UI refinement (responsive glass pass)

- Reworked the actual dashboard, login and public subscription selectors with one consistent midnight / cyan / violet design system.
- Corrected long subscription URL wrapping; links now stay on one line with ellipsis while copy/open controls remain separate and touch-friendly.
- Standardized dashboard group cards, config cards, status chips, forms, action buttons, sidebar and mobile navigation.
- Rebalanced responsive layouts for phone, tablet and desktop widths; added safe-area spacing and reduced-motion handling.
- Kept all API behavior and release version unchanged.

## 1.0.0 — UI refinement

- Refined the login, admin dashboard, and subscription portal with a unified dark glass visual system.
- Improved responsive spacing, focus visibility, form contrast, card hierarchy, and reduced-motion behavior.
- Kept the application version at 1.0.0.
- Clarified that the combined VPN/proxy application must not be deployed on Railway under its published usage policy.

### UI / QR reliability refinement (version remains 1.0.0)
- Fixed login password reveal control spacing so the eye button no longer overlaps entered text in RTL layouts.
- Added accessible reveal/hide controls to dashboard password fields, including dynamically opened forms.
- Switched dashboard and public-portal QR rendering to a POST request with an image-blob preview, avoiding long encoded links in query strings.
- Added QR loading/error states and reliable close/cleanup behavior for generated images.
- Consolidated final glass UI overrides for dashboard cards, action buttons, portal cards, and responsive mobile controls.

## 2.0.0 — Sub-panel and public portal refinement (2026-11-13)

- Rebuilt the subscription-group page cards with deeper liquid-glass layers, circular logo watermark, aligned action controls, and a persistent light/dark toggle.
- Restyled the group-creation modal and kept custom destination IP/port support for all 24 generated configurations.
- Reduced the quick-create interaction wait by refreshing the group/config lists in the background after the atomic create request returns; password hashing remains off the event loop.
- Kept one primary management and one delete action per group card; public-link and subscription-link actions remain attached to their respective link rows to avoid duplicate controls.
- Added progressive ICMP scan results for up to 500 public and RFC1918/ULA private addresses, with scope filters, live progress, latency display, and per-address / grouped copy.
- Enhanced the public portal's blue-violet-red glass effects for quota, remaining validity, and transfer metrics; added a persisted theme toggle and Persian diagnostic timing details.
- Removed the visible Telegram username from login and public support labels; the Telegram destination remains behind the support link.
- Switched the main dashboard clock to a 12-hour display and placed the official round logo in the service-status indicator.
- Added regression coverage for private/public IP scope validation and incremental scan streaming.
