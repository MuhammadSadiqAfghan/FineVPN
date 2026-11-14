"""Regression tests for FineVPN v2.0 additions."""
from __future__ import annotations

import asyncio
import unittest
from types import SimpleNamespace
from unittest.mock import patch

import main


class FineVPNV2LinkTests(unittest.TestCase):
    def test_normalize_server_ip(self) -> None:
        self.assertEqual(main.normalize_server_ip(" 8.8.8.8 "), "8.8.8.8")
        self.assertEqual(main.normalize_server_ip("2001:4860:4860::8888"), "2001:4860:4860::8888")
        self.assertIsNone(main.normalize_server_ip(""))
        with self.assertRaises(ValueError):
            main.normalize_server_ip("vpn.example.com")

    def test_custom_ipv4_changes_only_connection_address(self) -> None:
        link = main.generate_vless_link(
            "12345678-1234-1234-1234-123456789abc",
            "panel.example.com",
            port=8443,
            server_address="1.1.1.1",
        )
        self.assertIn("@1.1.1.1:8443?", link)
        self.assertIn("host=panel.example.com", link)
        self.assertIn("sni=panel.example.com", link)

    def test_custom_ipv6_is_bracketed(self) -> None:
        link = main.generate_vless_link(
            "12345678-1234-1234-1234-123456789abc",
            "panel.example.com",
            port=443,
            server_address="2001:4860:4860::8888",
        )
        self.assertIn("@[2001:4860:4860::8888]:443?", link)


class FineVPNV2IPCheckTests(unittest.IsolatedAsyncioTestCase):
    async def test_ip_check_returns_real_probe_results(self) -> None:
        async def fake_probe(ip_text: str) -> dict:
            return {
                "ip": ip_text,
                "status": "reachable" if ip_text == "1.1.1.1" else "unreachable",
                "latency_ms": 8.4 if ip_text == "1.1.1.1" else None,
                "message": "پاسخ آزمایشی",
            }

        class FakeRequest:
            async def json(self):
                return {"ips": ["1.1.1.1", "8.8.8.8", "1.1.1.1"]}

        old_last_at = main._IP_SCAN_LAST_AT
        main._IP_SCAN_LAST_AT = 0
        try:
            with patch.object(main, "_icmp_probe", fake_probe):
                result = await main.check_public_ips(FakeRequest(), None)
            self.assertEqual(result["tested"], 2)
            self.assertEqual(result["reachable"], 1)
            self.assertEqual(result["unreachable"], 1)
            self.assertEqual(result["results"][0]["latency_ms"], 8.4)
            self.assertEqual(result["method"], "ICMP")
        finally:
            main._IP_SCAN_LAST_AT = old_last_at

    async def test_ip_check_rejects_private_addresses(self) -> None:
        class FakeRequest:
            async def json(self):
                return {"ips": ["192.168.1.1"]}

        with self.assertRaises(main.HTTPException) as caught:
            await main.check_public_ips(FakeRequest(), None)
        self.assertEqual(caught.exception.status_code, 400)

    async def test_ip_check_rejects_more_than_500(self) -> None:
        class FakeRequest:
            async def json(self):
                return {"ips": ["1.1.1.1"] * 501}

        with self.assertRaises(main.HTTPException) as caught:
            await main.check_public_ips(FakeRequest(), None)
        self.assertEqual(caught.exception.status_code, 400)

    def test_scan_normalizer_accepts_public_and_private_and_rejects_special(self) -> None:
        targets = main._normalize_ip_scan_targets(["1.1.1.1", "192.168.1.8", "10.0.0.2", "fd00::1"])
        self.assertEqual([x["scope"] for x in targets], ["public", "private", "private", "private"])
        with self.assertRaises(main.HTTPException) as caught:
            main._normalize_ip_scan_targets(["127.0.0.1"])
        self.assertEqual(caught.exception.status_code, 400)

    async def test_streamed_scan_reports_incremental_public_and_private_results(self) -> None:
        async def fake_probe(ip_text: str) -> dict:
            return {
                "ip": ip_text,
                "status": "reachable" if ip_text != "192.168.1.1" else "unreachable",
                "latency_ms": 7.2 if ip_text != "192.168.1.1" else None,
                "message": "نتیجهٔ آزمایشی",
            }

        class FakeRequest:
            async def json(self):
                return {"ips": ["1.1.1.1", "192.168.1.1", "8.8.8.8"]}

        old_last_at, old_busy = main._IP_SCAN_LAST_AT, main._IP_SCAN_BUSY
        main._IP_SCAN_LAST_AT = 0
        main._IP_SCAN_BUSY = False
        try:
            with patch.object(main, "_icmp_probe", fake_probe):
                response = await main.check_ips_stream(FakeRequest(), None)
                chunks = []
                async for chunk in response.body_iterator:
                    chunks.append(chunk.decode() if isinstance(chunk, bytes) else str(chunk))
            events = [__import__("json").loads(line) for line in "".join(chunks).splitlines() if line.strip()]
            self.assertEqual(events[0]["type"], "start")
            results = [event["result"] for event in events if event["type"] == "result"]
            self.assertEqual(len(results), 3)
            self.assertEqual({row["scope"] for row in results}, {"public", "private"})
            self.assertTrue(any(row["ip"] == "192.168.1.1" and row["scope"] == "private" for row in results))
            self.assertEqual(events[-1]["type"], "done")
            self.assertEqual(events[-1]["tested"], 3)
        finally:
            main._IP_SCAN_LAST_AT, main._IP_SCAN_BUSY = old_last_at, old_busy

class FineVPNV2UIAndGroupTargetTests(unittest.TestCase):
    def test_group_matrix_applies_custom_destination_to_every_config(self) -> None:
        records = main._build_24_config_matrix(
            "test-sub", None, 2, 0, server_address="1.1.1.1", port=8443
        )
        self.assertEqual(len(records), 24)
        self.assertTrue(all(link["server_address"] == "1.1.1.1" for link in records.values()))
        self.assertTrue(all(link["port"] == 8443 for link in records.values()))
        self.assertTrue(all(link["sub_id"] == "test-sub" for link in records.values()))

    def test_dashboard_has_complete_glass_layout_and_real_theme_toggle(self) -> None:
        from pages import DASHBOARD_HTML, LOGIN_HTML
        self.assertIn('class="dash-feature-card dash-sub-feature', DASHBOARD_HTML)
        self.assertIn('class="dash-feature-card dash-portal-feature', DASHBOARD_HTML)
        self.assertIn('id="dash-recent-links"', DASHBOARD_HTML)
        self.assertIn('id="theme-toggle-top"', DASHBOARD_HTML)
        self.assertIn("localStorage.setItem('finevpn-theme',fineTheme)", DASHBOARD_HTML)
        self.assertNotIn("setAttribute('data-theme','dark')", DASHBOARD_HTML)
        self.assertIn('https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png', LOGIN_HTML)
        self.assertIn('id="subgroup-theme-toggle"', DASHBOARD_HTML)
        self.assertIn('dash-health-logo', DASHBOARD_HTML)
        self.assertIn('background-image:url("https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png")', DASHBOARD_HTML)
        self.assertIn('id="ns-address"', DASHBOARD_HTML)
        self.assertIn('id="ns-port"', DASHBOARD_HTML)
        self.assertIn("hour12:true", DASHBOARD_HTML)
        self.assertIn("/api/tools/ip-check/stream", DASHBOARD_HTML)
        self.assertIn('data-ip-filter="private"', DASHBOARD_HTML)
        from pages import get_public_page_html
        portal = get_public_page_html("ui-check")
        self.assertIn('id="public-theme-toggle"', portal)
        self.assertIn('class="diag-window"', portal)
        self.assertIn('فاین‌وی‌پی‌ان // پایش فنی', portal)
        self.assertNotIn('پشتیبانی @sadiq_AFG1', portal)
        self.assertIn('span>پشتیبانی</span>', portal)
        self.assertNotIn('CHECKING', portal)
        self.assertNotIn('NOT TESTED', portal)

if __name__ == "__main__":
    unittest.main()
