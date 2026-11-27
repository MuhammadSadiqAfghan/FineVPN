from __future__ import annotations
import asyncio, json, os
from pathlib import Path
from fastapi import APIRouter, Request, HTTPException, Depends, BackgroundTasks
from fastapi.responses import FileResponse, JSONResponse
from app.core.security import require_auth
from app.core.config import ENGINE_DIR
from app.engine.manager import ProxyEngineManager
from app.engine.config_validator import ConfigValidator
from app.engine import config_parser

router=APIRouter(prefix='/api/engine',tags=['proxy-engine'])
manager=ProxyEngineManager()

async def _run(options):
    try: await asyncio.to_thread(manager.run,options)
    except Exception: pass

@router.get('/status')
async def status(_=Depends(require_auth)):
    state=manager.snapshot()
    files=[]
    ignored = {'engine_state.json', 'raw_configs.txt'}
    for p in sorted(ENGINE_DIR.rglob('*')):
        if p.is_file() and p.name not in ignored and p.suffix.lower() in {'.txt', '.json', '.jsonc', '.yaml', '.yml', '.svg', '.html'}:
            files.append({'name':p.relative_to(ENGINE_DIR).as_posix(),'size':p.stat().st_size,'updated_at':p.stat().st_mtime})
    state['files']=files
    return state

@router.get('/sources')
async def sources(_=Depends(require_auth)):
    from app.engine.settings import user_settings
    return {'sources':manager.snapshot().get('sources') or list(user_settings.SOURCE_URLS)}

@router.get('/settings')
async def engine_settings(_=Depends(require_auth)):
    from app.engine.settings import user_settings
    return {
        'protocols': dict(user_settings.ENABLED_PROTOCOLS),
        'use_maximum_power': bool(user_settings.USE_MAXIMUM_POWER),
        'test_xray': bool(user_settings.ENABLE_XRAY_TESTER),
        'test_singbox': bool(user_settings.ENABLE_SINGBOX_TESTER),
        'specific_config_count': int(user_settings.SPECIFIC_CONFIG_COUNT),
        'xray': {'workers': int(user_settings.XRAY_TESTER_MAX_WORKERS), 'timeout': int(user_settings.XRAY_TESTER_TIMEOUT_SECONDS), 'rounds': int(user_settings.XRAY_TESTER_ROUNDS), 'batch_size': int(user_settings.XRAY_TESTER_BATCH_SIZE)},
        'singbox': {'workers': int(user_settings.SINGBOX_TESTER_MAX_WORKERS), 'timeout': int(user_settings.SINGBOX_TESTER_TIMEOUT_SECONDS), 'rounds': int(user_settings.SINGBOX_TESTER_ROUNDS), 'batch_size': int(user_settings.SINGBOX_TESTER_BATCH_SIZE)},
        'max_config_age_days': int(user_settings.MAX_CONFIG_AGE_DAYS)
    }

@router.put('/sources')
async def set_sources(request:Request,_=Depends(require_auth)):
    b=await request.json(); urls=b.get('sources') or []
    try: result=manager.set_sources(urls)
    except Exception as e: raise HTTPException(400,str(e))
    if not result: raise HTTPException(400,'حداقل یک منبع معتبر لازم است')
    return {'ok':True,'sources':result}

@router.post('/sources')
async def add_source(request:Request,_=Depends(require_auth)):
    from app.engine.settings import user_settings
    b=await request.json(); url=str(b.get('url') or '').strip()
    current=manager.snapshot().get('sources') or list(user_settings.SOURCE_URLS)
    if url not in current: current.append(url)
    result=manager.set_sources(current)
    if url not in result: raise HTTPException(400,'آدرس منبع معتبر نیست')
    return {'ok':True,'sources':result}

@router.delete('/sources')
async def delete_source(request:Request,_=Depends(require_auth)):
    from app.engine.settings import user_settings
    b=await request.json(); url=str(b.get('url') or '')
    current=manager.snapshot().get('sources') or list(user_settings.SOURCE_URLS)
    result=manager.set_sources([x for x in current if x!=url])
    return {'ok':True,'sources':result}

@router.post('/run')
async def run_engine(request:Request,background:BackgroundTasks,_=Depends(require_auth)):
    state=manager.snapshot()
    if state.get('status') in ('running', 'queued'): raise HTTPException(409,'موتور در حال اجراست')
    options=await request.json()
    manager.last_state.update({'status':'queued','phase':'در صف اجرا','error':None})
    manager._save_state()
    background.add_task(_run,options)
    return {'ok':True,'status':'queued'}

@router.post('/cancel')
async def cancel_engine(_=Depends(require_auth)):
    # Current pipeline stages are blocking library calls; cancellation is cooperative between stages.
    state=manager.snapshot()
    if state.get('status') not in ('running','queued'):
        raise HTTPException(409,'موتور در حال اجرا نیست')
    manager.cancel_requested=True
    return {'ok':True,'message':'درخواست توقف ثبت شد؛ موتور در مرز مرحله جاری متوقف می‌شود'}

@router.post('/parse')
async def parse_config(request:Request,_=Depends(require_auth)):
    b=await request.json(); raw=str(b.get('config') or '').strip()
    validator=ConfigValidator(); clean=validator.clean_config(raw)
    if not validator.is_valid_config(clean): raise HTTPException(400,'فرمت کانفیگ پشتیبانی نمی‌شود')
    protocol=clean.split('://',1)[0].lower()
    parsers={'vless':config_parser.parse_vless,'vmess':config_parser.decode_vmess,'trojan':config_parser.parse_trojan,
             'hysteria2':config_parser.parse_hysteria2,'hy2':config_parser.parse_hysteria2,
             'ss':config_parser.parse_shadowsocks,'wireguard':config_parser.parse_wireguard,'tuic':config_parser.parse_tuic}
    parsed=parsers.get(protocol,lambda _:None)(clean)
    if parsed is None: raise HTTPException(400,'کانفیگ قابل تجزیه نیست')
    return {'ok':True,'protocol':protocol,'config':parsed,'identity':config_parser.compute_identity(clean)}

@router.get('/files/{name:path}')
async def download_engine_file(name:str,_=Depends(require_auth)):
    allowed={'raw_configs.txt','valid_configs.txt','tested_configs.txt','proxy_configs.txt','singbox.json','clash.yaml','xray.json','singbox_secure.json','xray_fragment.json','xray_fragment_tested.json','xray_tested.json','xray_loadbalanced_config.json','xray_fragment_loadbalanced_config.json','xray_secure_loadbalanced_config.json','singbox_tested.json','singbox_configs_all.json','singbox_configs_tested.json','clash_tested.yaml','clash_configs_all.yaml','clash_configs_tested.yaml','proxy_configs_all.txt','proxy_configs_tested.txt','singbox_configs_secure.json','clash_secure.yaml','clash_configs_secure.yaml','channel_stats.json','channel_stats_chart.svg','performance_report.html','location_cache.json','source_stats.json','source-performance.svg','source-report.html','summary.json','locations.json','FineVPN_Serverless.jsonc','hiddify/FineVPN_Serverless.jsonc'}
    if name not in allowed and not name.startswith('by_country/'):
        raise HTTPException(404,'فایل پیدا نشد')
    path = (ENGINE_DIR / name).resolve()
    if not path.is_relative_to(ENGINE_DIR.resolve()) or not path.is_file():
        raise HTTPException(404,'فایل هنوز ساخته نشده است')
    return FileResponse(path,filename=path.name)
