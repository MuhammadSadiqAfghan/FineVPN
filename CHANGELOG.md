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
