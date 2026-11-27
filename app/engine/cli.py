"""Command-line entry point for the FineVPN internal proxy discovery engine."""
from __future__ import annotations
import argparse
import json
import sys
from app.engine.manager import ProxyEngineManager


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="FineVPN proxy discovery and conversion engine")
    parser.add_argument("--workers", type=int, default=24)
    parser.add_argument("--timeout", type=int, default=5)
    parser.add_argument("--rounds", type=int, default=3)
    parser.add_argument("--batch-size", type=int, default=200)
    parser.add_argument("--xray-path", default="xray")
    parser.add_argument("--singbox-path", default="sing-box")
    parser.add_argument("--no-xray-test", action="store_true")
    parser.add_argument("--no-singbox-test", action="store_true")
    parser.add_argument("--no-geolocation", action="store_true")
    args = parser.parse_args(argv)
    options = {
        "workers": args.workers, "timeout": args.timeout,
        "rounds": args.rounds, "batch_size": args.batch_size,
        "xray_path": args.xray_path, "singbox_path": args.singbox_path,
        "test_xray": not args.no_xray_test,
        "test_singbox": not args.no_singbox_test,
        "geolocate": not args.no_geolocation,
    }
    manager = ProxyEngineManager()
    try:
        state = manager.run(options)
    except Exception as exc:
        print(json.dumps({"status": "failed", "error": str(exc)}, ensure_ascii=False))
        return 1
    summary = {key: state.get(key) for key in (
        "status", "raw_count", "valid_count", "tested_count", "verified_count",
        "test_status", "verified_by", "last_run", "error"
    )}
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if state.get("status") == "completed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
