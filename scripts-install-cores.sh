#!/usr/bin/env bash
set -euo pipefail
mkdir -p "$HOME/.local/bin" "$RUNNER_TEMP/finevpn-xray" "$RUNNER_TEMP/finevpn-singbox"
export PATH="$HOME/.local/bin:$PATH"

XRAY_URL="$(curl -fsSL https://api.github.com/repos/XTLS/Xray-core/releases/latest | jq -r '.assets[] | select(.name == "Xray-linux-64.zip") | .browser_download_url' | head -n1)"
if [[ -z "$XRAY_URL" || "$XRAY_URL" == "null" ]]; then echo 'Xray release asset not found' >&2; exit 1; fi
curl -fL --retry 3 --retry-delay 3 "$XRAY_URL" -o "$RUNNER_TEMP/xray.zip"
unzip -oq "$RUNNER_TEMP/xray.zip" xray geoip.dat geosite.dat -d "$RUNNER_TEMP/finevpn-xray"
install -m 0755 "$RUNNER_TEMP/finevpn-xray/xray" "$HOME/.local/bin/xray"
mkdir -p "$HOME/.local/share/xray"
for f in geoip.dat geosite.dat; do [[ ! -f "$RUNNER_TEMP/finevpn-xray/$f" ]] || install -m 0644 "$RUNNER_TEMP/finevpn-xray/$f" "$HOME/.local/share/xray/$f"; done
xray version

SINGBOX_URL="$(curl -fsSL https://api.github.com/repos/SagerNet/sing-box/releases/latest | jq -r '.assets[] | select(.name | test("_linux_amd64\\.deb$")) | .browser_download_url' | head -n1)"
if [[ -z "$SINGBOX_URL" || "$SINGBOX_URL" == "null" ]]; then echo 'Sing-box release asset not found' >&2; exit 1; fi
curl -fL --retry 3 --retry-delay 3 "$SINGBOX_URL" -o "$RUNNER_TEMP/sing-box.deb"
dpkg-deb -x "$RUNNER_TEMP/sing-box.deb" "$RUNNER_TEMP/finevpn-singbox"
install -m 0755 "$RUNNER_TEMP/finevpn-singbox/usr/bin/sing-box" "$HOME/.local/bin/sing-box"
sing-box version
