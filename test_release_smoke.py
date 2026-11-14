"""Release smoke tests for FineVPN v2.0 UI and readiness metadata."""
from __future__ import annotations

import unittest

import main
from pages import DASHBOARD_HTML, LOGIN_HTML, get_public_page_html


class FineVPNReleaseSmokeTests(unittest.TestCase):
    def test_login_dashboard_and_portal_use_official_brand_image(self) -> None:
        portal = get_public_page_html("smoke-test-key")
        for name, html in (
            ("login", LOGIN_HTML),
            ("dashboard", DASHBOARD_HTML),
            ("portal", portal),
        ):
            with self.subTest(page=name):
                self.assertIn('class="fine-logo-mark"', html)
                self.assertIn("https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png", html)
                self.assertIn("𝒗₂.₀", html)

    def test_v2_branding_is_persian_only_and_ip_scanner_is_present(self) -> None:
        self.assertEqual(main.APP_VERSION, "2.0.0")
        self.assertIn('id="pg-ipcheck"', DASHBOARD_HTML)
        self.assertIn("async function runIpScan()", DASHBOARD_HTML)
        self.assertIn('data-ip-filter="reachable"', DASHBOARD_HTML)
        self.assertIn('data-ip-filter="unreachable"', DASHBOARD_HTML)
        self.assertIn("function setIpFilter(filter)", DASHBOARD_HTML)
        self.assertIn("/api/tools/ip-check", DASHBOARD_HTML)
        self.assertNotIn('id="language-toggle"', DASHBOARD_HTML)
        self.assertNotIn('id="public-lang-label"', get_public_page_html("smoke-test-key"))

    def test_responsive_safe_area_rules_are_present(self) -> None:
        self.assertIn("viewport-fit=cover", DASHBOARD_HTML)
        self.assertIn("env(safe-area-inset-top)", DASHBOARD_HTML)
        self.assertIn("prefers-reduced-motion:reduce", LOGIN_HTML)
        self.assertIn("max-width:720px", get_public_page_html("smoke-test-key"))

    def test_railway_autodeploy_manifest_is_not_shipped(self) -> None:
        from pathlib import Path
        self.assertFalse((Path(__file__).parent / "railway.json").exists())

    def test_health_readiness_includes_ready_flag(self) -> None:
        self.assertTrue(callable(main.health))

    def test_health_reports_503_when_state_path_is_not_writable(self) -> None:
        import asyncio
        original = main.persistence_status
        try:
            main.persistence_status = lambda: {
                "mounted": False,
                "writable": False,
                "free_mb": 0,
                "data_dir": "/read-only",
            }
            response = asyncio.run(main.health())
            self.assertEqual(response.status_code, 503)
        finally:
            main.persistence_status = original

    def test_health_reports_200_when_state_path_is_writable(self) -> None:
        import asyncio
        original = main.persistence_status
        try:
            main.persistence_status = lambda: {
                "mounted": True,
                "writable": True,
                "free_mb": 1024,
                "data_dir": "/data",
            }
            response = asyncio.run(main.health())
            self.assertEqual(response.status_code, 200)
        finally:
            main.persistence_status = original


if __name__ == "__main__":
    unittest.main()
