from __future__ import annotations
import asyncio, time, json
from datetime import datetime
from app.core.runtime import LINKS, SUBS, save_state, log_activity, is_link_expired
from app.core.config import DATA_DIR
from app.core import database

async def maintenance_loop():
    last_save=0.0; last_backup=0.0
    while True:
        try:
            changed=False
            for item in LINKS.values():
                if item.get('active',True) and is_link_expired(item):
                    item['active']=False
                    if item.get('inherits_sub_expiry'):
                        item['auto_disabled_by_expiry']=True
                    changed=True
                    log_activity('expiry',f"کانفیگ {item.get('label','')} به علت پایان اعتبار غیرفعال شد",'warn')
            for sub in SUBS.values():
                exp=sub.get('expires_at')
                if exp and sub.get('active',True):
                    try:
                        if datetime.fromisoformat(exp).timestamp()<=time.time():
                            sub['active']=False; changed=True
                            log_activity('expiry',f"اشتراک {sub.get('name','')} منقضی شد",'warn')
                    except Exception: pass
            if changed or time.time()-last_save>60:
                await save_state(); last_save=time.time()
            database.prune_sessions()
            # Automatic state backup; the persistent volume should be protected by deployment-level encryption. Retention is capped to 14 snapshots.
            if time.time()-last_backup>12*60*60:
                folder=DATA_DIR/'backups'; folder.mkdir(parents=True,exist_ok=True)
                data={'links':LINKS,'subs':SUBS,'categories':__import__('app.core.runtime',fromlist=['CATEGORIES']).CATEGORIES}
                name='automatic-'+datetime.now().strftime('%Y%m%d-%H%M%S')+'.json'
                (folder/name).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
                files=sorted(folder.glob('automatic-*.json'),key=lambda p:p.stat().st_mtime,reverse=True)
                for old in files[14:]: old.unlink(missing_ok=True)
                last_backup=time.time(); log_activity('backup',f'پشتیبان خودکار {name} ایجاد شد','ok')
        except Exception:
            pass
        await asyncio.sleep(30)
