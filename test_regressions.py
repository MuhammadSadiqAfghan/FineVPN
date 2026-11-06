"""Lightweight regression checks for FineVPN quota and subscription accounting.

Run from the project root with: python -m unittest -v test_regressions.py
The test state is written only under the operating system temporary directory.
"""
from __future__ import annotations

import asyncio
import os
import tempfile
import unittest
from datetime import datetime, timedelta
from pathlib import Path

os.environ.setdefault(
    "DATA_DIR",
    str(Path(tempfile.gettempdir()) / "finevpn-regression-test-state"),
)
os.environ.setdefault("SECRET_KEY", "finevpn-regression-tests-only")

import main  # noqa: E402
import relay_vless  # noqa: E402
import xhttp_siz10  # noqa: E402
from starlette.requests import Request  # noqa: E402


class _JSONRequest:
    def __init__(self, body: dict):
        self._body = body

    async def json(self) -> dict:
        return self._body


def _json_receive(payload: dict):
    import json
    sent = False
    async def receive():
        nonlocal sent
        if sent:
            return {"type": "http.request", "body": b"", "more_body": False}
        sent = True
        return {"type": "http.request", "body": json.dumps(payload).encode(), "more_body": False}
    return receive


class FineVPNQuotaRegressions(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        main.LINKS.clear()
        main.SUBS.clear()
        main.connections.clear()
        main.stats["total_bytes"] = 0
        main.hourly_traffic.clear()
        # Keep unit tests deterministic and prevent background persistence tasks.
        relay_vless.mark_usage_dirty = lambda: None

    def _group_and_link(self, *, group_limit: int = 10, link_limit: int = 0) -> None:
        main.SUBS["group-1"] = {
            "name": "Regression group",
            "uuid_key": "public-key",
            "created_at": datetime.now().isoformat(),
            "validity_started_at": datetime.now().isoformat(),
            "link_ids": ["link-1"],
            "total_limit_bytes": group_limit,
            "total_used_bytes": 0,
            "total_upload_bytes": 0,
            "total_download_bytes": 0,
            "total_days": 0,
            "expires_at": None,
        }
        main.LINKS["link-1"] = {
            "label": "Regression link",
            "active": True,
            "sub_id": "group-1",
            "limit_bytes": link_limit,
            "used_bytes": 0,
            "upload_bytes": 0,
            "download_bytes": 0,
            "expires_at": None,
        }

    async def test_shared_quota_rejects_overflowing_chunk(self) -> None:
        self._group_and_link(group_limit=10)
        self.assertTrue(await relay_vless.check_and_use("link-1", 8, "upload"))
        self.assertFalse(await relay_vless.check_and_use("link-1", 5, "upload"))
        self.assertEqual(main.SUBS["group-1"]["total_used_bytes"], 8)
        self.assertEqual(main.LINKS["link-1"]["used_bytes"], 8)

    async def test_concurrent_chunks_cannot_exceed_shared_quota(self) -> None:
        self._group_and_link(group_limit=10)
        results = await asyncio.gather(
            *(relay_vless.check_and_use("link-1", 6, "upload") for _ in range(12))
        )
        self.assertEqual(sum(results), 1)
        self.assertEqual(main.SUBS["group-1"]["total_used_bytes"], 6)

    async def test_upload_and_download_are_counted_separately(self) -> None:
        self._group_and_link(group_limit=100)
        self.assertTrue(await relay_vless.check_and_use("link-1", 3, "upload"))
        self.assertTrue(await relay_vless.check_and_use("link-1", 4, "download"))
        group = main.SUBS["group-1"]
        self.assertEqual(group["total_used_bytes"], 7)
        self.assertEqual(group["total_upload_bytes"], 3)
        self.assertEqual(group["total_download_bytes"], 4)

    async def test_group_reset_does_not_reset_individual_config_usage(self) -> None:
        self._group_and_link(group_limit=100, link_limit=60)
        main.SUBS["group-1"].update(
            total_used_bytes=90, total_upload_bytes=50, total_download_bytes=40
        )
        main.LINKS["link-1"].update(used_bytes=55, upload_bytes=30, download_bytes=25)
        await main.set_sub_bandwidth("group-1", _JSONRequest({"total_used_bytes": 0}), None)
        self.assertEqual(main.SUBS["group-1"]["total_used_bytes"], 0)
        self.assertEqual(main.LINKS["link-1"]["used_bytes"], 55)
        self.assertTrue(main.is_link_allowed(main.LINKS["link-1"]))

    async def test_group_renewal_updates_child_expiry(self) -> None:
        self._group_and_link(group_limit=0)
        expired = (datetime.now() - timedelta(days=1)).isoformat()
        main.SUBS["group-1"].update(total_days=1, expires_at=expired)
        main.LINKS["link-1"]["expires_at"] = expired
        await main.set_sub_bandwidth("group-1", _JSONRequest({"days": 30}), None)
        group_expiry = main.SUBS["group-1"]["expires_at"]
        self.assertEqual(main.LINKS["link-1"]["expires_at"], group_expiry)
        self.assertTrue(main.is_link_allowed(main.LINKS["link-1"]))

    async def test_zero_group_aggregate_is_not_rebuilt_from_old_child_counters(self) -> None:
        self._group_and_link(group_limit=0)
        main.LINKS["link-1"].update(used_bytes=80, upload_bytes=30, download_bytes=50)
        main.SUBS["group-1"].update(
            total_used_bytes=0, total_upload_bytes=0, total_download_bytes=0
        )
        main.normalize_sub_usage_state()
        self.assertEqual(main.SUBS["group-1"]["total_used_bytes"], 0)

    async def test_xhttp_stream_coalesces_small_frames_before_quota_lock(self) -> None:
        import socket
        import uuid as uuidlib

        link_id = str(uuidlib.uuid4())
        main.LINKS[link_id] = {
            "label": "XHTTP regression", "active": True, "sub_id": None,
            "ip_limit": 0, "limit_bytes": 0, "used_bytes": 0,
            "upload_bytes": 0, "download_bytes": 0, "expires_at": None,
        }
        # Valid VLESS request header targeting a documentation-only address.
        header = (b"\x00" + uuidlib.UUID(link_id).bytes + b"\x00\x01" +
                  (443).to_bytes(2, "big") + b"\x01" + socket.inet_aton("192.0.2.1") + b"A")
        chunks = [header + (b"a" * 199)] + [b"b" * 250 for _ in range(99)]
        messages = [
            {"type": "http.request", "body": part, "more_body": i < len(chunks) - 1}
            for i, part in enumerate(chunks)
        ]
        index = 0

        async def receive():
            nonlocal index
            if index < len(messages):
                item = messages[index]
                index += 1
                return item
            return {"type": "http.request", "body": b"", "more_body": False}

        scope = {
            "type": "http", "http_version": "1.1", "method": "POST",
            "scheme": "http", "path": f"/xhttp-siz10/stream-up/{link_id}/batch-test",
            "raw_path": f"/xhttp-siz10/stream-up/{link_id}/batch-test".encode(),
            "query_string": b"", "headers": [(b"host", b"localhost")],
            "client": ("127.0.0.1", 12345), "server": ("localhost", 80),
            "asgi": {"version": "3.0", "spec_version": "2.3"},
        }
        class _Transport:
            def get_write_buffer_size(self):
                return 0
        class _Writer:
            def __init__(self):
                self.transport = _Transport()
                self.written = bytearray()
            def write(self, data):
                self.written.extend(data)
            async def drain(self):
                return None
            def close(self):
                return None
            async def wait_closed(self):
                return None

        writer = _Writer()
        calls: list[int] = []
        old_ensure = xhttp_siz10.ensure_reaper
        old_check = xhttp_siz10.check_and_use
        old_throttle = xhttp_siz10.throttle
        old_open = xhttp_siz10._open_tcp_for_session
        async def fake_check(_uid, n, direction="upload"):
            calls.append(n)
            return True
        async def fake_throttle(_uid, _n):
            return None
        async def fake_open(_sid, _uid, sess, first_chunk):
            _cmd, _addr, _port, payload = await relay_vless.parse_vless_header(first_chunk)
            writer.write(payload)
            sess["writer"] = writer
            sess["tcp_open"] = True
        xhttp_siz10.ensure_reaper = lambda: None
        xhttp_siz10.check_and_use = fake_check
        xhttp_siz10.throttle = fake_throttle
        xhttp_siz10._open_tcp_for_session = fake_open
        try:
            result = await xhttp_siz10.stream_up_upload(
                link_id, "batch-test", Request(scope, receive)
            )
            self.assertIsNone(result)
            self.assertLess(len(calls), 10, "small ASGI frames should be coalesced")
            self.assertGreaterEqual(len(calls), 1, "the stream should authorize the coalesced payload")
            expected = header[26:] + (b"a" * 199) + (b"b" * 250 * 99)
            self.assertEqual(bytes(writer.written), expected)
        finally:
            xhttp_siz10.ensure_reaper = old_ensure
            xhttp_siz10.check_and_use = old_check
            xhttp_siz10.throttle = old_throttle
            xhttp_siz10._open_tcp_for_session = old_open
            await xhttp_siz10._teardown("batch-test")

    async def test_github_backup_is_queued_after_local_save(self) -> None:
        import time
        from pathlib import Path
        old_token, old_repo = main.GH_PERSIST_TOKEN, main.GH_PERSIST_REPO
        old_push = main._gh_persist_push
        old_dir = main.DATA_DIR
        called = asyncio.Event()
        async def slow_push(_payload: str) -> None:
            called.set()
            await asyncio.sleep(0.15)
        try:
            main.GH_PERSIST_TOKEN = "test-token"
            main.GH_PERSIST_REPO = "test-owner/test-repo"
            main.DATA_DIR = Path(tempfile.gettempdir()) / "finevpn-remote-save-test"
            main._gh_persist_push = slow_push
            started = time.perf_counter()
            await main.save_state()
            elapsed = time.perf_counter() - started
            self.assertLess(elapsed, 0.12, "local save must not wait on GitHub network")
            task = main._GH_PERSIST_TASK
            if task is not None:
                await task
            self.assertTrue(called.is_set(), "remote persistence should still be queued")
        finally:
            main.GH_PERSIST_TOKEN, main.GH_PERSIST_REPO = old_token, old_repo
            main._gh_persist_push = old_push
            main.DATA_DIR = old_dir
            main._GH_PERSIST_PENDING = None
            if main._GH_PERSIST_TASK is not None:
                main._GH_PERSIST_TASK.cancel()
                await asyncio.gather(main._GH_PERSIST_TASK, return_exceptions=True)
                main._GH_PERSIST_TASK = None

    async def test_xhttp_queues_and_socket_buffers_are_bounded(self) -> None:
        self.assertEqual(xhttp_siz10.XHTTP_BUF, 128 * 1024)
        self.assertLessEqual(xhttp_siz10.DOWNLINK_QUEUE_MAX * xhttp_siz10.XHTTP_BUF, 8 * 1024 * 1024)
        self.assertLessEqual(xhttp_siz10.SOCK_BUF_SIZE, 1024 * 1024)
        self.assertLessEqual(xhttp_siz10.FLOW_MAX_HW, 4 * 1024 * 1024)

    async def test_quick_group_creation_builds_24_configs_with_one_save(self) -> None:
        saves = 0
        async def fake_save_state() -> None:
            nonlocal saves
            saves += 1
        original_save = main.save_state
        main.save_state = fake_save_state
        scope = {
            "type": "http", "http_version": "1.1", "method": "POST",
            "scheme": "https", "path": "/api/subs/quick",
            "raw_path": b"/api/subs/quick", "query_string": b"",
            "headers": [(b"host", b"vpn.example")], "client": ("127.0.0.1", 12345),
            "server": ("vpn.example", 443), "asgi": {"version": "3.0", "spec_version": "2.3"},
        }
        try:
            payload = await main.create_sub_with_matrix(
                Request(scope, _json_receive({
                    "name": "Fast group", "desc": "created atomically", "password": "",
                    "total_limit_bytes": 5 * 1024**3, "days": 30, "ip_limit": 2,
                    "speed_limit_bytes": 0,
                })),
            )
        finally:
            main.save_state = original_save
        self.assertTrue(payload["ok"])
        self.assertEqual(payload["count"], 24)
        self.assertEqual(len(payload["links"]), 24)
        self.assertEqual(len(set(payload["links"])), 24)
        self.assertEqual(len(main.SUBS), 1)
        self.assertEqual(len(main.LINKS), 24)
        group = main.SUBS[payload["sub_id"]]
        self.assertEqual(group["link_ids"], payload["links"])
        self.assertEqual(group["total_limit_bytes"], 5 * 1024**3)
        self.assertEqual(group["total_days"], 30)
        self.assertEqual(saves, 1)
        self.assertTrue(all(main.LINKS[uid]["sub_id"] == payload["sub_id"] for uid in payload["links"]))

    async def test_quick_matrix_rebuild_is_batched_and_preserves_group_usage(self) -> None:
        self._group_and_link(group_limit=100)
        old_id = "link-1"
        main.SUBS["group-1"].update(total_used_bytes=21, total_upload_bytes=10, total_download_bytes=11)
        saves = 0
        async def fake_save_state() -> None:
            nonlocal saves
            saves += 1
        original_save = main.save_state
        main.save_state = fake_save_state
        try:
            result = await main.quick_create_links(
                "group-1", _JSONRequest({"days": 14, "ip_limit": 3, "speed_limit_bytes": 0}), None
            )
        finally:
            main.save_state = original_save
        self.assertEqual(result["count"], 24)
        self.assertEqual(len(main.SUBS["group-1"]["link_ids"]), 24)
        self.assertNotIn(old_id, main.LINKS)
        self.assertEqual(main.SUBS["group-1"]["total_used_bytes"], 21)
        self.assertEqual(saves, 1)

    async def test_public_subscription_reports_real_live_tunnels_and_expired_quota(self) -> None:
        self._group_and_link(group_limit=100)
        expired = (datetime.now() - timedelta(minutes=1)).isoformat()
        main.SUBS["group-1"].update(
            total_days=1, expires_at=expired, total_used_bytes=100,
            total_upload_bytes=40, total_download_bytes=50,
        )
        main.LINKS["link-1"].update(used_bytes=100, upload_bytes=40, download_bytes=50)
        main.connections["ready-1"] = {"uuid": "link-1", "ip": "203.0.113.10", "tunnel_ready": True}
        main.connections["pending-1"] = {"uuid": "link-1", "ip": "203.0.113.10", "tunnel_ready": False}
        scope = {
            "type": "http", "http_version": "1.1", "method": "GET",
            "scheme": "http", "path": "/api/public/sub/public-key",
            "raw_path": b"/api/public/sub/public-key", "query_string": b"",
            "headers": [(b"host", b"localhost")], "client": ("127.0.0.1", 12345),
            "server": ("localhost", 80), "asgi": {"version": "3.0", "spec_version": "2.3"},
        }
        payload = await main.public_sub_data("public-key", Request(scope))
        self.assertTrue(payload["expired"])
        self.assertIsInstance(payload["expires_at_unix"], int)
        self.assertTrue(payload["quota_exhausted"])
        self.assertEqual(payload["online_users"], 1)
        self.assertEqual(payload["active_sessions"], 1)
        self.assertEqual(payload["unclassified_bytes"], 10)
        self.assertTrue(payload["links"][0]["expired"])
        self.assertFalse(payload["links"][0]["active"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
