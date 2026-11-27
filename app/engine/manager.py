from __future__ import annotations

import json
import shutil
import threading
from datetime import datetime
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

from app.core.config import ENGINE_DIR
from app.engine.config import ProxyConfig, ChannelConfig
from app.engine.fetch_configs import ConfigFetcher, save_channel_stats
from app.engine.config_validator import ConfigValidator
from app.engine import config_parser

STATE_FILE = ENGINE_DIR / 'engine_state.json'
RAW_FILE = ENGINE_DIR / 'raw_configs.txt'
VALID_FILE = ENGINE_DIR / 'valid_configs.txt'
TESTED_FILE = ENGINE_DIR / 'tested_configs.txt'
LOCATION_FILE = ENGINE_DIR / 'locations.json'
SINGBOX_FILE = ENGINE_DIR / 'singbox.json'
CLASH_FILE = ENGINE_DIR / 'clash.yaml'
XRAY_FILE = ENGINE_DIR / 'xray.json'
SECURE_FILE = ENGINE_DIR / 'singbox_secure.json'


class EngineCancelled(Exception):
    """Raised between pipeline stages when an operator requests cancellation."""


class ProxyEngineManager:
    def __init__(self):
        self.last_state = self._load_state()
        self.cancel_requested = False
        self._state_lock = threading.RLock()

    def _load_state(self):
        try:
            state = json.loads(STATE_FILE.read_text(encoding='utf-8'))
            if isinstance(state, dict):
                return state
        except Exception:
            pass
        return {
            'status': 'idle', 'phase': 'آماده', 'raw_count': 0,
            'valid_count': 0, 'tested_count': 0, 'verified_count': 0,
            'last_run': None, 'logs': [], 'sources': [], 'protocol_counts': {},
            'test_status': {'xray': 'not_run', 'singbox': 'not_run'}
        }

    def _save_state(self):
        ENGINE_DIR.mkdir(parents=True, exist_ok=True)
        with self._state_lock:
            payload = json.dumps(self.last_state, ensure_ascii=False, indent=2)
            tmp = STATE_FILE.with_suffix('.tmp')
            tmp.write_text(payload, encoding='utf-8')
            tmp.replace(STATE_FILE)

    def snapshot(self):
        with self._state_lock:
            try:
                return json.loads(STATE_FILE.read_text(encoding='utf-8'))
            except Exception:
                return dict(self.last_state)

    def set_sources(self, urls):
        clean = []
        for raw in urls:
            url = str(raw).strip()
            if not url or url in clean:
                continue
            if url.startswith('ssconf://'):
                clean.append(url)
                continue
            parts = urlsplit(url)
            if parts.scheme in ('http', 'https') and parts.hostname:
                clean.append(url)
        self.last_state['sources'] = clean
        self._save_state()
        return clean

    def _log(self, msg, level='info'):
        self.last_state.setdefault('logs', []).append({
            'time': datetime.now().isoformat(),
            'level': level,
            'message': str(msg)[:500]
        })
        self.last_state['logs'] = self.last_state['logs'][-200:]
        self._save_state()

    def _set_phase(self, label):
        self.last_state['phase'] = label
        self._save_state()
        if self.cancel_requested:
            raise EngineCancelled('اجرای موتور به درخواست مدیر متوقف شد')

    @staticmethod
    def _dedupe_keep_order(items):
        result, seen = [], set()
        for item in items:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result

    def run(self, options=None):
        options = options or {}
        self.cancel_requested = False
        self.last_state.update({
            'status': 'running', 'phase': 'آماده‌سازی منابع',
            'started_at': datetime.now().isoformat(), 'error': None,
            'raw_count': 0, 'valid_count': 0, 'tested_count': 0,
            'verified_count': 0, 'test_status': {'xray': 'not_run', 'singbox': 'not_run'}
        })
        self._save_state()
        try:
            config = ProxyConfig()
            urls = self.last_state.get('sources') or [c.url for c in config.SOURCE_URLS]
            config.SOURCE_URLS = config._remove_duplicate_urls([ChannelConfig(u) for u in urls])
            config.OUTPUT_FILE = str(RAW_FILE)
            config.STATS_FILE = str(ENGINE_DIR / 'source_stats.json')
            config.use_maximum_power = bool(options.get('use_maximum_power', config.use_maximum_power))
            config.specific_config_count = max(1, min(10000, int(options.get('specific_config_count', config.specific_config_count) or 50)))
            config.MAX_CONFIG_AGE_DAYS = max(0, min(365, int(options.get('max_config_age_days', config.MAX_CONFIG_AGE_DAYS))))
            config._set_smart_limits()
            protocols = options.get('protocols') or {}
            for key, enabled in protocols.items():
                key = key if str(key).endswith('://') else str(key) + '://'
                if key in config.SUPPORTED_PROTOCOLS:
                    config.SUPPORTED_PROTOCOLS[key]['enabled'] = bool(enabled)

            self._set_phase('دریافت کانفیگ‌ها')
            self._log(f"شروع دریافت از {len(config.SOURCE_URLS)} منبع")
            fetcher = ConfigFetcher(config)
            raw = fetcher.fetch_all_configs()
            save_channel_stats(config, total_saved=len(raw) if raw else 0)
            self._set_phase('اعتبارسنجی و حذف تکراری‌ها')
            if not raw:
                raise RuntimeError('هیچ کانفیگ قابل‌دریافتی پیدا نشد')
            RAW_FILE.write_text('\n'.join(raw) + '\n', encoding='utf-8')

            validator = ConfigValidator()
            valid, seen, counts = [], set(), Counter()
            for line in raw:
                clean = validator.clean_config(line)
                if not validator.is_valid_config(clean):
                    continue
                proto = clean.split('://', 1)[0].lower()
                canonical = {'hy2': 'hysteria2'}.get(proto, proto)
                if not config.is_protocol_enabled(canonical + '://'):
                    continue
                if not validator.validate_protocol_config(clean, proto + '://') and proto != 'hy2':
                    continue
                ident = config_parser.compute_identity(clean)
                if ident in seen:
                    continue
                seen.add(ident)
                valid.append(clean)
                counts[canonical.upper()] += 1
            if not valid:
                raise RuntimeError('دریافت انجام شد اما هیچ کانفیگ معتبری باقی نماند')
            VALID_FILE.write_text('\n'.join(valid) + '\n', encoding='utf-8')
            self.last_state.update({
                'raw_count': len(raw), 'valid_count': len(valid),
                'protocol_counts': dict(counts)
            })
            self._save_state()

            self._set_phase('غنی‌سازی مکان و نام‌گذاری')
            if options.get('geolocate', True):
                try:
                    from app.engine.enrich_configs import ConfigEnricher
                    ConfigEnricher().process_configs(str(VALID_FILE), str(LOCATION_FILE))
                except Exception as exc:
                    self._log(f'غنی‌سازی موقعیت انجام نشد: {type(exc).__name__}: {exc}', 'warning')
            try:
                from app.engine.rename_configs import ConfigRenamer
                if LOCATION_FILE.exists():
                    ConfigRenamer(str(LOCATION_FILE)).process_configs(str(VALID_FILE), str(VALID_FILE))
            except Exception as exc:
                self._log(f'نام‌گذاری جغرافیایی انجام نشد: {type(exc).__name__}: {exc}', 'warning')
            valid = [x.strip() for x in VALID_FILE.read_text(encoding='utf-8').splitlines() if x.strip()]
            candidates = list(valid)
            verified_by = []
            test_status = {'xray': 'skipped', 'singbox': 'skipped'}
            legacy = options
            xray_cfg = options.get('xray') or {}
            singbox_cfg = options.get('singbox') or {}
            xray_common = {
                'max_workers': max(1, min(64, int(xray_cfg.get('workers', legacy.get('workers', config.XRAY_TESTER_MAX_WORKERS)))),),
                'timeout': max(2, min(60, int(xray_cfg.get('timeout', legacy.get('timeout', config.XRAY_TESTER_TIMEOUT_SECONDS))))),
                'rounds': max(1, min(5, int(xray_cfg.get('rounds', legacy.get('rounds', config.XRAY_TESTER_ROUNDS))))),
                'batch_size': max(1, min(500, int(xray_cfg.get('batch_size', legacy.get('batch_size', config.XRAY_TESTER_BATCH_SIZE))))),
            }
            singbox_common = {
                'max_workers': max(1, min(64, int(singbox_cfg.get('workers', config.TESTER_MAX_WORKERS)))),
                'timeout': max(2, min(60, int(singbox_cfg.get('timeout', config.TESTER_TIMEOUT_SECONDS)))),
                'rounds': max(1, min(5, int(singbox_cfg.get('rounds', config.TESTER_ROUNDS)))),
                'batch_size': max(1, min(500, int(singbox_cfg.get('batch_size', config.TESTER_BATCH_SIZE)))),
            }

            if options.get('test_xray', True):
                self._set_phase('تست واقعی با Xray')
                try:
                    from app.engine.xray_config_tester import ParallelXrayTester
                    tester = ParallelXrayTester(xray_path=options.get('xray_path', 'xray'), **xray_common)
                    candidates = self._dedupe_keep_order(tester.test_all(candidates))
                    test_status['xray'] = 'completed'
                    verified_by.append('xray')
                    self._log(f'تست Xray پایان یافت: {len(candidates)} کانفیگ باقی ماند')
                except Exception as exc:
                    text = str(exc).lower()
                    if 'not found' in text or 'no such file' in text or 'cannot find' in text:
                        test_status['xray'] = 'core_missing'
                        self._log('هسته Xray نصب نیست؛ تست واقعی این بخش اجرا نشد', 'warning')
                    else:
                        test_status['xray'] = 'error'
                        self._log(f'خطای تست Xray: {exc}', 'error')

            self._set_phase('تست واقعی با Sing-box') if options.get('test_singbox', True) else None
            if options.get('test_singbox', True):
                try:
                    from app.engine.config_to_singbox import ConfigToSingbox
                    converter = ConfigToSingbox()
                    mapped = []
                    for i, cfg in enumerate(candidates, 1):
                        kind = cfg.split('://', 1)[0].lower()
                        outbound = converter.convert_to_singbox(cfg, i, kind.upper())
                        if outbound:
                            tag = f'finevpn-{i}'
                            outbound['tag'] = tag
                            mapped.append((cfg, outbound, tag))
                    from app.engine.config_tester import ParallelConfigTester
                    tester = ParallelConfigTester(singbox_path=options.get('singbox_path', 'sing-box'), **singbox_common)
                    working = tester.test_all([x[1] for x in mapped])
                    allowed = {x.get('tag') for x in working if isinstance(x, dict)}
                    candidates = [cfg for cfg, _, tag in mapped if tag in allowed]
                    test_status['singbox'] = 'completed'
                    verified_by.append('singbox')
                    self._log(f'تست Sing-box پایان یافت: {len(candidates)} کانفیگ باقی ماند')
                except Exception as exc:
                    text = str(exc).lower()
                    if 'not found' in text or 'no such file' in text or 'cannot find' in text:
                        test_status['singbox'] = 'core_missing'
                        self._log('هسته Sing-box نصب نیست؛ تست واقعی این بخش اجرا نشد', 'warning')
                    else:
                        test_status['singbox'] = 'error'
                        self._log(f'خطای تست Sing-box: {exc}', 'error')

            self._set_phase('ساخت خروجی‌های نسخه اصلی و تست‌شده')
            verified = candidates if verified_by else []
            TESTED_FILE.write_text(('\n'.join(verified) + '\n') if verified else '', encoding='utf-8')
            self.last_state.update({
                'tested_count': len(verified), 'verified_count': len(verified),
                'test_status': test_status, 'verified_by': verified_by,
                'phase': 'ساخت خروجی‌ها'
            })
            self._save_state()
            self._export_formats(valid, verified)
            self._write_summary(valid, raw, verified, test_status)
            self.last_state.update({
                'status': 'completed', 'phase': 'پایان',
                'last_run': datetime.now().isoformat(),
                'tested_count': len(verified), 'verified_count': len(verified)
            })
            self._log(
                f"پایپلاین پایان یافت: {len(raw)} دریافت، {len(valid)} معتبر، {len(verified)} واقعاً تست‌شده"
            )
            self._save_state()
            return self.snapshot()
        except EngineCancelled as exc:
            self.last_state.update({'status': 'cancelled', 'phase': 'متوقف‌شده', 'error': str(exc), 'last_run': datetime.now().isoformat()})
            self._log(str(exc), 'warning')
            self._save_state()
            return self.snapshot()
        except Exception as exc:
            self.last_state.update({'status': 'failed', 'phase': 'خطا', 'error': str(exc), 'last_run': datetime.now().isoformat()})
            self._log(f'خطا: {exc}', 'error')
            self._save_state()
            raise

    def _build_singbox(self, configs, output_file):
        from app.engine.config_to_singbox import ConfigToSingbox
        converter = ConfigToSingbox()
        outbounds = []
        for i, cfg in enumerate(configs, 1):
            kind = cfg.split('://', 1)[0].lower()
            outbound = converter.convert_to_singbox(cfg, i, kind.upper())
            if outbound:
                outbound['tag'] = f'proxy-{i}'
                outbounds.append(outbound)
        tags = [x['tag'] for x in outbounds]
        config = {
            'log': {'level': 'warn', 'timestamp': True},
            'outbounds': [
                {'type': 'selector', 'tag': 'FineVPN Auto', 'outbounds': tags},
                {'type': 'urltest', 'tag': 'FineVPN Best Ping', 'outbounds': tags,
                 'url': 'https://www.gstatic.com/generate_204', 'interval': '3m'},
                {'type': 'direct', 'tag': 'direct'}
            ] + outbounds
        }
        Path(output_file).write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding='utf-8')
        return config

    def _build_clash(self, singbox_config, output_file):
        from app.engine.singbox_to_clash import singbox_outbound_to_clash_proxy, create_clash_config
        proxies, names = [], []
        for outbound in singbox_config.get('outbounds', []):
            item = singbox_outbound_to_clash_proxy(outbound)
            if item:
                proxies.append(item)
                names.append(item['name'])
        clash = create_clash_config(proxies, names) if proxies else {'proxies': [], 'proxy-groups': [], 'rules': ['MATCH,DIRECT']}
        import yaml
        Path(output_file).write_text(yaml.safe_dump(clash, allow_unicode=True, sort_keys=False), encoding='utf-8')
        return clash

    def _export_formats(self, all_configs, verified_configs):
        from app.engine.xray_balancer import ConfigToXray
        from app.engine.xray_fragment_balancer import ConfigToXrayFragment
        # Main exports use all structurally valid configs. Separate *_tested
        # artifacts are populated only after an actual Xray/Sing-box test pass.
        all_sb = self._build_singbox(all_configs, ENGINE_DIR / 'singbox.json')
        verified_sb = self._build_singbox(verified_configs, ENGINE_DIR / 'singbox_tested.json')
        shutil.copyfile(ENGINE_DIR / 'singbox.json', ENGINE_DIR / 'singbox_configs_all.json')
        shutil.copyfile(ENGINE_DIR / 'singbox_tested.json', ENGINE_DIR / 'singbox_configs_tested.json')
        self._build_clash(all_sb, ENGINE_DIR / 'clash.yaml')
        self._build_clash(verified_sb, ENGINE_DIR / 'clash_tested.yaml')
        shutil.copyfile(ENGINE_DIR / 'clash.yaml', ENGINE_DIR / 'clash_configs_all.yaml')
        shutil.copyfile(ENGINE_DIR / 'clash_tested.yaml', ENGINE_DIR / 'clash_configs_tested.yaml')
        secure_path = ENGINE_DIR / 'singbox_secure.json'
        if secure_path.is_file():
            try:
                secure_sb = json.loads(secure_path.read_text(encoding='utf-8'))
                self._build_clash(secure_sb, ENGINE_DIR / 'clash_secure.yaml')
                shutil.copyfile(ENGINE_DIR / 'clash_secure.yaml', ENGINE_DIR / 'clash_configs_secure.yaml')
                shutil.copyfile(secure_path, ENGINE_DIR / 'singbox_configs_secure.json')
            except Exception as exc:
                self._log(f'ساخت خروجی امن Clash انجام نشد: {exc}', 'warning')

        VALID_FILE.write_text(('\n'.join(all_configs) + '\n') if all_configs else '', encoding='utf-8')
        TESTED_FILE.write_text(('\n'.join(verified_configs) + '\n') if verified_configs else '', encoding='utf-8')
        (ENGINE_DIR / 'proxy_configs_all.txt').write_text(('\n'.join(all_configs) + '\n') if all_configs else '', encoding='utf-8')
        (ENGINE_DIR / 'proxy_configs.txt').write_text(('\n'.join(verified_configs) + '\n') if verified_configs else '', encoding='utf-8')
        shutil.copyfile(TESTED_FILE, ENGINE_DIR / 'proxy_configs_tested.txt')

        ConfigToXray(str(VALID_FILE), str(XRAY_FILE)).process_configs()
        ConfigToXray(str(TESTED_FILE), str(ENGINE_DIR / 'xray_tested.json')).process_configs()
        self._ensure_xray_output(XRAY_FILE, 'FineVPN Balanced')
        self._ensure_xray_output(ENGINE_DIR / 'xray_tested.json', 'FineVPN Tested')
        shutil.copyfile(XRAY_FILE, ENGINE_DIR / 'xray_loadbalanced_config.json')
        from app.engine.security_filter import SecurityFilter
        SecurityFilter(str(ENGINE_DIR / 'singbox.json'), str(SECURE_FILE), str(ENGINE_DIR / 'xray_secure.json')).filter_configs()
        self._ensure_xray_output(ENGINE_DIR / 'xray_secure.json', 'FineVPN Secure')
        shutil.copyfile(ENGINE_DIR / 'xray_secure.json', ENGINE_DIR / 'xray_secure_loadbalanced_config.json')
        ConfigToXrayFragment(str(VALID_FILE), str(ENGINE_DIR / 'xray_fragment.json')).process_configs()
        ConfigToXrayFragment(str(TESTED_FILE), str(ENGINE_DIR / 'xray_fragment_tested.json')).process_configs()
        self._ensure_xray_output(ENGINE_DIR / 'xray_fragment.json', 'FineVPN Balanced + Fragment')
        self._ensure_xray_output(ENGINE_DIR / 'xray_fragment_tested.json', 'FineVPN Tested + Fragment')
        shutil.copyfile(ENGINE_DIR / 'xray_fragment.json', ENGINE_DIR / 'xray_fragment_loadbalanced_config.json')
        self._write_hiddify_profile()
        self._write_country_exports(all_configs)

    @staticmethod
    def _ensure_xray_output(path, name):
        """Write a valid empty Xray profile when no target-format outbound exists."""
        path = Path(path)
        if path.is_file() and path.stat().st_size:
            try:
                json.loads(path.read_text(encoding='utf-8'))
                return
            except Exception:
                pass
        from app.engine.xray_template import get_xray_template
        config = get_xray_template(name)
        config['outbounds'] = []
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding='utf-8')

    def _write_hiddify_profile(self):
        """Publish the Hiddify FinalMask preset using FineVPN identity."""
        source = Path(__file__).resolve().parent / 'templates' / 'FineVPN_Serverless.jsonc'
        target_dir = ENGINE_DIR / 'hiddify'
        target_dir.mkdir(parents=True, exist_ok=True)
        if source.is_file():
            shutil.copyfile(source, target_dir / 'FineVPN_Serverless.jsonc')

    def _write_country_exports(self, configs):
        from app.engine.country_splitter import process
        try:
            process(str(VALID_FILE), str(LOCATION_FILE), str(ENGINE_DIR / 'by_country'))
            if LOCATION_FILE.is_file():
                shutil.copyfile(LOCATION_FILE, ENGINE_DIR / 'location_cache.json')
        except Exception as exc:
            self._log(f'خروجی تفکیک کشور انجام نشد: {exc}', 'warning')

    def _write_summary(self, valid, raw, verified, test_status):
        data = {
            'generated_at': datetime.now().isoformat(),
            'raw_count': len(raw), 'valid_count': len(valid),
            'tested_count': len(verified), 'verified_by': self.last_state.get('verified_by', []),
            'test_status': test_status,
            'protocol_counts': dict(Counter(x.split('://', 1)[0].upper() for x in valid))
        }
        (ENGINE_DIR / 'summary.json').write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
        try:
            from app.engine.generate_charts import generate_basic_svg, generate_html_report
            channel_stats = json.loads((ENGINE_DIR / 'source_stats.json').read_text(encoding='utf-8'))
            (ENGINE_DIR / 'source-performance.svg').write_text(generate_basic_svg(channel_stats), encoding='utf-8')
            (ENGINE_DIR / 'source-report.html').write_text(generate_html_report(channel_stats), encoding='utf-8')
        except Exception as exc:
            self._log(f'ساخت نمودار گزارش منابع انجام نشد: {exc}', 'warning')
