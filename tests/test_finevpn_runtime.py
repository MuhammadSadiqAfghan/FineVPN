import hashlib
from app.core import runtime
from app.core.config import SECRET_KEY
from app.core.security import verify_password


def test_legacy_finevpn_password_hash_remains_valid():
    password = 'Existing-FineVPN-Pass!'
    legacy = hashlib.sha256(f'{password}{SECRET_KEY}'.encode()).hexdigest()
    assert verify_password(password, legacy)
    assert not verify_password('wrong-password', legacy)


def test_subscription_ip_cap_is_shared_across_profiles(monkeypatch):
    monkeypatch.setitem(runtime.SUBS, 'sub-test', {
        'ip_limit': 1,
        'link_ids': ['link-a', 'link-b'],
    })
    monkeypatch.setitem(runtime.LINKS, 'link-a', {'sub_id': 'sub-test', 'ip_limit': 0})
    monkeypatch.setitem(runtime.LINKS, 'link-b', {'sub_id': 'sub-test', 'ip_limit': 0})
    monkeypatch.setitem(runtime.connections, 'conn-test', {'uuid': 'link-a', 'ip': '203.0.113.10'})
    assert runtime.is_ip_allowed(runtime.LINKS['link-b'], 'link-b', '203.0.113.10')
    assert not runtime.is_ip_allowed(runtime.LINKS['link-b'], 'link-b', '203.0.113.11')
    monkeypatch.delitem(runtime.connections, 'conn-test')
    monkeypatch.delitem(runtime.LINKS, 'link-a')
    monkeypatch.delitem(runtime.LINKS, 'link-b')
    monkeypatch.delitem(runtime.SUBS, 'sub-test')


def test_speed_units_distinguish_megabits_from_megabytes():
    assert runtime.parse_speed_to_bytes(8, 'Mbps') == 1024**2
    assert runtime.parse_speed_to_bytes(1, 'MBps') == 1024**2
    assert runtime.parse_speed_to_bytes(1, 'KBps') == 1024


def test_shared_subscription_quota_is_reserved_atomically(monkeypatch):
    import asyncio
    from app.core import runtime
    import main  # initialise the transport compatibility boundary first
    from app.transports import relay_vless

    sub_id = 'quota-sub-test'
    link_ids = ['quota-link-a', 'quota-link-b']
    monkeypatch.setitem(runtime.SUBS, sub_id, {
        'active': True,
        'total_limit_bytes': 100,
        'total_used_bytes': 0,
        'link_ids': link_ids,
    })
    for lid in link_ids:
        monkeypatch.setitem(runtime.LINKS, lid, {
            'active': True, 'sub_id': sub_id, 'limit_bytes': 0,
            'used_bytes': 0, 'upload_bytes': 0, 'download_bytes': 0,
        })
    monkeypatch.setattr(relay_vless, '_schedule_usage_persist', lambda: None)

    async def exercise():
        return await asyncio.gather(
            relay_vless.check_and_use(link_ids[0], 60, 'upload'),
            relay_vless.check_and_use(link_ids[1], 60, 'upload'),
        )

    try:
        outcomes = asyncio.run(exercise())
        assert sorted(outcomes) == [False, True]
        assert runtime.SUBS[sub_id]['total_used_bytes'] == 60
    finally:
        runtime.SUBS.pop(sub_id, None)
        for lid in link_ids:
            runtime.LINKS.pop(lid, None)
            runtime.USAGE_LOCKS.pop(f'link:{lid}', None)
        runtime.USAGE_LOCKS.pop(f'sub:{sub_id}', None)


def test_renew_reactivates_profiles_disabled_by_expiry(monkeypatch):
    import asyncio
    from datetime import datetime, timedelta
    from app.core import runtime
    from app.api import subscriptions

    sub_id = 'renew-sub-test'
    link_id = 'renew-link-test'
    yesterday = (datetime.now() - timedelta(days=1)).isoformat()
    monkeypatch.setitem(runtime.SUBS, sub_id, {
        'name': 'renew-test', 'active': False, 'expires_at': yesterday,
        'total_days': 30, 'link_ids': [link_id],
    })
    monkeypatch.setitem(runtime.LINKS, link_id, {
        'active': False, 'inherits_sub_expiry': True,
        'auto_disabled_by_expiry': True, 'sub_id': sub_id,
    })

    class Request:
        async def json(self):
            return {'days': 30, 'reset_usage': False}

    monkeypatch.setattr(subscriptions, 'save_state', _noop_async)
    try:
        result = asyncio.run(subscriptions.renew_sub(sub_id, Request()))
        assert result['ok'] is True
        assert runtime.SUBS[sub_id]['active'] is True
        assert runtime.LINKS[link_id]['active'] is True
        assert 'auto_disabled_by_expiry' not in runtime.LINKS[link_id]
        assert datetime.fromisoformat(runtime.LINKS[link_id]['expires_at']) > datetime.now()
    finally:
        runtime.SUBS.pop(sub_id, None)
        runtime.LINKS.pop(link_id, None)


async def _noop_async():
    return None


def test_finevpn_ui_uses_requested_black_white_red_responsive_shell():
    from pathlib import Path
    root = Path(__file__).resolve().parents[1]
    html = (root / 'app' / 'static' / 'index.html').read_text(encoding='utf-8')
    css = (root / 'app' / 'static' / 'app.css').read_text(encoding='utf-8')
    js = (root / 'app' / 'static' / 'app.js').read_text(encoding='utf-8')
    for page in ('dashboard', 'subscriptions', 'links', 'groups', 'connections',
                 'sources', 'engine', 'exports', 'reports', 'backups', 'settings'):
        assert f'data-page="{page}"' in html
    assert '#000' in css and '#fff' in css and '#e60023' in css
    assert '@media(max-width:640px)' in css
    assert 'copilot-image-1793563203439.png' in js
    assert 'linear-gradient' not in css
