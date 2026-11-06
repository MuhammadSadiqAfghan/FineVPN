# relay_vless.py
# بخش VLESS Relay — جدا شده از main.py (منطق اصلی دست‌نخورده)
# تغییر: ثبت IP واقعی کلاینت (با احتساب هدر x-forwarded-for پشت پراکسی) در connections

import asyncio
import secrets
from datetime import datetime

from fastapi import WebSocket, WebSocketDisconnect

_active_ws: dict = {}

from main import (
    LINKS,
    LINKS_LOCK,
    detect_device as _device_from_ua,
    SUBS,
    SUBS_LOCK,
    is_sub_expired,
    is_link_expired,
    mark_usage_dirty,
    connections,
    error_logs,
    hourly_traffic,
    is_ip_allowed,
    is_link_allowed,
    log_activity,
    logger,
    now_ir,
    resolve_client_ip,
    save_state,
    stats,
)
from speed_limit import throttle

# ══════════════════════════════════════════════════════════════════════════════
# VLESS Relay — بهینه‌شده برای حداکثر throughput
# ══════════════════════════════════════════════════════════════════════════════

RELAY_BUF = 256 * 1024   # 256 KB buffer

def _ws_client_ip(ws: WebSocket) -> str:
    """IP that cannot be spoofed by the client.

    X-Forwarded-For / X-Real-IP are attacker-controlled headers; they are only read
    when the TCP peer is a trusted proxy, otherwise the socket peer is authoritative."""
    return resolve_client_ip(ws)

async def parse_vless_header(chunk: bytes):
    if len(chunk) < 24:
        raise ValueError("chunk too small")
    pos = 1
    pos += 16
    addon_len = chunk[pos]; pos += 1 + addon_len
    command = chunk[pos]; pos += 1
    port = int.from_bytes(chunk[pos:pos+2], "big"); pos += 2
    addr_type = chunk[pos]; pos += 1
    if addr_type == 1:
        address = ".".join(str(b) for b in chunk[pos:pos+4]); pos += 4
    elif addr_type == 2:
        dlen = chunk[pos]; pos += 1
        address = chunk[pos:pos+dlen].decode("utf-8", errors="ignore"); pos += dlen
    elif addr_type == 3:
        ab = chunk[pos:pos+16]; pos += 16
        address = ":".join(f"{ab[i]:02x}{ab[i+1]:02x}" for i in range(0, 16, 2))
    else:
        raise ValueError(f"unknown addr type: {addr_type}")
    return command, address, port, chunk[pos:]

async def check_and_use(uid: str, n: int, direction: str = "upload") -> bool:
    """Atomically authorize and account a payload before it is forwarded.

    A frame/chunk is accepted only when the whole amount fits both the per-config
    and shared-group remaining quota. This prevents concurrent tunnels from
    overshooting a quota. If the final remainder is smaller than a transport
    chunk, that chunk is rejected rather than silently forwarded unmetered.
    """
    amount = max(0, int(n or 0))
    if amount == 0:
        return True
    counter = "download_bytes" if direction == "download" else "upload_bytes"
    group_counter = "total_download_bytes" if direction == "download" else "total_upload_bytes"
    async with LINKS_LOCK:
        link = LINKS.get(uid)
        if link is None or not link.get("active", True) or is_link_expired(link):
            return False
        link_used = max(0, int(link.get("used_bytes", 0) or 0))
        link_limit = max(0, int(link.get("limit_bytes", 0) or 0))
        if link_limit > 0 and link_used + amount > link_limit:
            return False
        sub_id = link.get("sub_id")
        if sub_id:
            async with SUBS_LOCK:
                sub = SUBS.get(sub_id)
                if sub is None or is_sub_expired(sub):
                    return False
                group_used = max(0, int(sub.get("total_used_bytes", 0) or 0))
                group_limit = max(0, int(sub.get("total_limit_bytes", 0) or 0))
                if group_limit > 0 and group_used + amount > group_limit:
                    return False
                # Both ledgers are updated while the locks are held, so simultaneous
                # connections cannot reserve the same remaining bytes twice.
                link["used_bytes"] = link_used + amount
                link[counter] = max(0, int(link.get(counter, 0) or 0)) + amount
                sub["total_used_bytes"] = group_used + amount
                sub[group_counter] = max(0, int(sub.get(group_counter, 0) or 0)) + amount
        else:
            link["used_bytes"] = link_used + amount
            link[counter] = max(0, int(link.get(counter, 0) or 0)) + amount
        stats["total_bytes"] += amount
        hourly_traffic[now_ir().strftime("%H:00")] += amount
    mark_usage_dirty()
    return True

async def relay_ws_to_tcp(ws: WebSocket, writer: asyncio.StreamWriter, conn_id: str, uid: str):
    try:
        while True:
            msg = await ws.receive()
            if msg["type"] == "websocket.disconnect":
                break
            data = msg.get("bytes") or (msg.get("text") or "").encode()
            if not data:
                continue
            if not await check_and_use(uid, len(data), direction="upload"):
                await ws.close(code=1008, reason="quota/disabled/unknown")
                break
            await throttle(uid, len(data))
            stats["total_requests"] += 1
            connections[conn_id]["bytes"] += len(data)
            # ── تشخیص مقصد جدید: هر پکت ممکنه هدر VLESS یه سایت جدید باشه ──
            try:
                if len(data) >= 24 and data[0] == 0:
                    _cmd, _addr, _port, _rest = await parse_vless_header(data)
                    if _addr:
                        _d = f"{_addr}:{_port}"
                        if connections.get(conn_id, {}).get("dest") != _d:
                            connections[conn_id]["dest"] = _d
                            logger.info(f"➡️  [{conn_id}] -> {_d}")
            except Exception:
                pass
            writer.write(data)
            if writer.transport.get_write_buffer_size() > RELAY_BUF:
                await writer.drain()
    except (WebSocketDisconnect, Exception):
        pass
    finally:
        try:
            writer.write_eof()
        except Exception:
            pass

async def relay_tcp_to_ws(ws: WebSocket, reader: asyncio.StreamReader, conn_id: str, uid: str):
    first = True
    try:
        while True:
            data = await reader.read(RELAY_BUF)
            if not data:
                break
            if not await check_and_use(uid, len(data), direction="download"):
                await ws.close(code=1008, reason="quota/disabled/unknown")
                break
            await throttle(uid, len(data))
            connections[conn_id]["bytes"] += len(data)
            payload = (b"\x00\x00" + data) if first else data
            first = False
            await ws.send_bytes(payload)
    except Exception:
        pass

async def websocket_tunnel(ws: WebSocket, uuid: str):
    await ws.accept()

    async with LINKS_LOCK:
        link = LINKS.get(uuid)

    if not is_link_allowed(link):
        logger.warning(f"🚫 WS rejected uuid={uuid[:8]}… (not allowed)")
        await ws.close(code=1008, reason="not authorized")
        return

    ip = _ws_client_ip(ws)

    if not is_ip_allowed(link, uuid, ip):
        logger.warning(f"🚫 WS rejected uuid={uuid[:8]}… ip={ip} (ip limit reached)")
        log_activity("connection", f"اتصال {ip} به کانفیگ «{link.get('label','?')}» رد شد (محدودیت تعداد آی‌پی)", "warn")
        await ws.close(code=1008, reason="ip limit reached")
        return

    _ua = ws.headers.get("user-agent") or ws.headers.get("User-Agent") or ""
    conn_id = secrets.token_urlsafe(6)
    _active_ws[conn_id] = ws
    connections[conn_id] = {
        "uuid": uuid,
        "ip": ip,
        "transport": "vless-ws",
        "connected_at": datetime.now().isoformat(),
        "bytes": 0,
        "user_agent": _ua,
        "tunnel_ready": False,
    }
    logger.info(f"✅ WS [{conn_id}] uuid={uuid[:8]}… ip={ip} total={len(connections)}")
    _dev = _device_from_ua(_ua)
    log_activity("connection", f"اتصال جدید از {ip} (کانفیگ {link.get('label','?')}) — {_dev}", "info",
                 meta={"ip": ip, "config": link.get('label','?'), "device": _dev, "user_agent": _ua})
    writer = None

    try:
        first_msg = await asyncio.wait_for(ws.receive(), timeout=15.0)
        if first_msg["type"] == "websocket.disconnect":
            return
        first_chunk = first_msg.get("bytes") or (first_msg.get("text") or "").encode()
        if not first_chunk:
            return

        command, address, port, payload = await parse_vless_header(first_chunk)

        if not await check_and_use(uuid, len(first_chunk), direction="upload"):
            await ws.close(code=1008, reason="quota/disabled")
            return

        stats["total_requests"] += 1
        connections[conn_id]["bytes"] += len(first_chunk)
        connections[conn_id]["dest"] = f"{address}:{port}"
        logger.info(f"➡️  [{conn_id}] → {address}:{port}")

        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(address, port),
            timeout=10.0
        )
        connections[conn_id]["tunnel_ready"] = True
        sock = writer.transport.get_extra_info('socket')
        if sock:
            import socket
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

        if payload:
            writer.write(payload)
            await writer.drain()

        done, pending = await asyncio.wait(
            {
                asyncio.create_task(relay_ws_to_tcp(ws, writer, conn_id, uuid)),
                asyncio.create_task(relay_tcp_to_ws(ws, reader, conn_id, uuid)),
            },
            return_when=asyncio.FIRST_COMPLETED,
        )
        for t in pending:
            t.cancel()
            try:
                await t
            except asyncio.CancelledError:
                pass

        asyncio.create_task(save_state())

    except WebSocketDisconnect:
        pass
    except asyncio.TimeoutError:
        stats["total_errors"] += 1
        error_logs.append({"error": "connection timeout", "time": datetime.now().isoformat()})
    except Exception as exc:
        stats["total_errors"] += 1
        error_logs.append({"error": str(exc), "time": datetime.now().isoformat()})
        logger.error(f"WS error [{conn_id}]: {exc}")
    finally:
        if writer:
            try:
                writer.close()
                await writer.wait_closed()
            except Exception:
                pass
        _active_ws.pop(conn_id, None)
        connections.pop(conn_id, None)
        logger.info(f"🔌 WS closed [{conn_id}] total={len(connections)}")
