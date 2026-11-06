# 𝑭𝒊𝒏𝒆𝑽𝑷𝑵 — Login, dashboard, and public subscription pages.

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><link rel="icon" href="https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png"><meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>𝑭𝒊𝒏𝒆𝑽𝑷𝑵 — ورود امن</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#09090b;--panel:#121217;--border:rgba(255,255,255,.08);
  --accent:#10b981;--accent-hover:#059669;--text:#f4f4f5;--muted:#a1a1aa;
  --font:'Vazirmatn',sans-serif;
}
body{
  min-height:100vh;display:flex;align-items:center;justify-content:center;
  background:radial-gradient(ellipse at 50% 20%, rgba(16,185,129,0.15), transparent 45%), var(--bg);
  font-family:var(--font);color:var(--text);padding:20px;
}
.card{
  width:100%;max-width:400px;background:var(--panel);border:1px solid var(--border);
  border-radius:24px;padding:36px 28px;box-shadow:0 25px 60px rgba(0,0,0,0.5);
  backdrop-filter:blur(16px);
}
.brand{text-align:center;margin-bottom:28px}
.brand-logo{
  width:56px;height:56px;border-radius:16px;background:linear-gradient(135deg,#10b981,#047857);
  display:flex;align-items:center;justify-content:center;margin:0 auto 14px;
  color:#fff;font-size:26px;box-shadow:0 8px 24px rgba(16,185,129,0.3);
}
.brand-title{font-size:22px;font-weight:800;color:#fff;margin-bottom:4px}
.brand-sub{font-size:12px;color:var(--muted)}
.fg{margin-bottom:18px}
.fl{display:block;font-size:12px;font-weight:600;color:var(--muted);margin-bottom:7px}
.fi-wrap{position:relative;display:flex;align-items:center}
.fi-wrap i{position:absolute;right:14px;color:#71717a;font-size:18px;pointer-events:none}
.fi{
  width:100%;padding:12px 42px 12px 14px;background:rgba(255,255,255,0.04);
  border:1px solid var(--border);border-radius:12px;color:#fff;
  font-family:inherit;font-size:13.5px;outline:none;transition:all .2s;
}
.fi:focus{border-color:var(--accent);background:rgba(255,255,255,0.07);box-shadow:0 0 0 3px rgba(16,185,129,0.15)}
.btn-p{
  width:100%;padding:13px;border-radius:12px;border:none;background:linear-gradient(135deg,#10b981,#059669);
  color:#fff;font-family:inherit;font-size:14px;font-weight:700;cursor:pointer;
  display:flex;align-items:center;justify-content:center;gap:8px;box-shadow:0 8px 20px rgba(16,185,129,0.3);
  transition:all .2s;margin-top:8px;
}
.btn-p:hover{transform:translateY(-1px);box-shadow:0 10px 25px rgba(16,185,129,0.4)}
.hint-box{
  margin-top:20px;padding:12px 14px;border-radius:12px;background:rgba(16,185,129,0.06);
  border:1px solid rgba(16,185,129,0.15);display:flex;align-items:center;justify-content:space-between;
  font-size:11.5px;color:var(--accent);cursor:pointer;transition:background .2s;
}
.hint-box:hover{background:rgba(16,185,129,0.12)}
.err-box{
  margin-top:14px;padding:10px 14px;border-radius:10px;background:rgba(239,68,68,0.12);
  border:1px solid rgba(239,68,68,0.25);color:#f87171;font-size:12px;display:none;align-items:center;gap:8px;
}
.vol-steps{display:flex;flex-direction:column;gap:10px}
.vol-step{display:flex;gap:12px;align-items:flex-start;padding:10px 12px;background:var(--card, #0d1c18);border:1px solid var(--line, rgba(255,255,255,.07));border-radius:12px}
.vs-n{flex:0 0 26px;height:26px;border-radius:50%;background:linear-gradient(135deg,#10B981,#047857);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:12px}
.vs-s{font-size:11.5px;color:var(--t3,#7d8b86);margin-top:2px}
.vol-step code{background:rgba(16,185,129,.14);color:#34d399;padding:1px 6px;border-radius:5px;font-size:11.5px}
.vol-note{margin-top:12px;font-size:11.5px;color:#93a59f;display:flex;gap:7px;align-items:flex-start;padding:10px;background:rgba(59,130,246,.08);border:1px solid rgba(59,130,246,.25);border-radius:10px}
.vol-note i{color:#60a5fa;margin-top:1px}
.cat-filter{width:auto;min-width:130px;font-size:11.5px;padding:6px 10px;border-radius:9px}
.cat-pill{display:inline-flex;align-items:center;gap:5px;font-size:10.5px;padding:2px 9px;border-radius:20px;font-weight:600;white-space:nowrap}
.cat-dot{width:7px;height:7px;border-radius:50%;flex:0 0 7px}
.cat-mgr{display:flex;flex-direction:column;gap:8px}
.cat-mgr-row{display:flex;gap:8px;align-items:center}
.cat-mgr-row input{flex:1}
.tel-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:10px}
.tel-tile{background:var(--card,#0d1c18);border:1px solid var(--line,rgba(255,255,255,.07));border-radius:12px;padding:12px}
.tel-tile .tt-l{font-size:10.5px;color:var(--t3,#7d8b86);display:flex;align-items:center;gap:5px}
.tel-tile .tt-v{font-size:17px;font-weight:700;color:var(--t1,#e8f5f0);margin-top:4px;direction:ltr}
.tel-tile .tt-s{font-size:10px;color:var(--t3,#7d8b86);margin-top:2px}
.tel-bar{height:5px;border-radius:3px;background:rgba(255,255,255,.08);margin-top:7px;overflow:hidden}
.tel-bar i{display:block;height:100%;border-radius:3px;background:linear-gradient(90deg,#10B981,#34d399);transition:width .5s}
.cat-del{padding:5px 10px;font-size:11px}
.badge.b-ok{background:rgba(16,185,129,.15);color:#34d399;border:1px solid rgba(16,185,129,.4)}
.badge.b-warn{background:rgba(245,158,11,.15);color:#fbbf24;border:1px solid rgba(245,158,11,.4)}

/* 𝑭𝒊𝒏𝒆𝑽𝑷𝑵 login — polished glass, starlight and gold */
:root{--bg:#030713;--panel:rgba(12,20,42,.72);--border:rgba(240,196,91,.22);--accent:#f0c45b;--accent-hover:#d4a333;--text:#f5f4ff;--muted:#a7b0d0}
html,body{min-height:100%;background-color:#030713}
body{background-color:#030713;background-image:
 radial-gradient(1px 1px at 17px 23px,rgba(255,255,255,.86) 55%,transparent 100%),
 radial-gradient(1.4px 1.4px at 71px 101px,rgba(255,225,164,.72) 55%,transparent 100%),
 linear-gradient(rgba(2,6,18,.78),rgba(2,6,18,.83)),url("https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png");
 background-size:109px 109px,173px 173px,100% 100%,min(66vw,680px) auto;background-position:0 0,35px 61px,center,center;
 background-repeat:repeat,repeat,no-repeat,no-repeat;background-attachment:fixed;font-family:'Vazirmatn',sans-serif}
.card{max-width:430px;background:linear-gradient(145deg,rgba(18,29,57,.83),rgba(6,12,29,.77));border:1px solid rgba(240,196,91,.26);border-radius:28px;box-shadow:0 30px 90px rgba(0,0,0,.48),0 0 36px rgba(240,196,91,.08);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px)}
.brand-logo{width:80px;height:80px;border-radius:50%;background:rgba(240,196,91,.1);border:1px solid rgba(255,220,125,.45);box-shadow:0 0 28px rgba(240,196,91,.2);overflow:hidden}
.brand-logo img{width:100%;height:100%;object-fit:cover;display:block}
.brand-title{color:#fff0bd;font-size:22px;letter-spacing:.02em}
.brand-sub{color:#b5bfdc;line-height:1.8}
.fl{color:#c9cde0}
.fi{background:rgba(4,9,24,.58);border-color:rgba(240,196,91,.2);color:#f5f4ff}
.fi:focus{border-color:#f0c45b;background:rgba(4,9,24,.78);box-shadow:0 0 0 3px rgba(240,196,91,.12)}
.fi-wrap i{color:#e4c36f}
.btn-p{background:linear-gradient(135deg,#fff0b8 0%,#f1ca62 42%,#bd8a25 100%);color:#211805;box-shadow:0 0 20px rgba(240,196,91,.18),0 8px 22px rgba(0,0,0,.24);border:1px solid rgba(255,233,164,.6)}
.btn-p:hover{background:linear-gradient(135deg,#fff6d6 0%,#ffe18a 45%,#d7a63a 100%);box-shadow:0 0 28px rgba(240,196,91,.3)}
.login-contact{border-top:1px solid rgba(240,196,91,.17);margin-top:22px;padding-top:17px;text-align:center}
.login-provider{font-size:11.5px;color:#c8cce0}
.login-provider strong{color:#ffe5a0;font-weight:800}
.login-signature{font-size:12px;color:#f4d98c;letter-spacing:.04em;margin-top:4px}
.login-links{display:flex;justify-content:center;gap:9px;flex-wrap:wrap;margin-top:13px}
.login-links a{display:inline-flex;align-items:center;gap:6px;padding:8px 10px;border:1px solid rgba(240,196,91,.23);border-radius:11px;background:rgba(240,196,91,.07);color:#ffe5a0;text-decoration:none;font-size:11px;font-weight:700}
.login-links a:hover{background:rgba(240,196,91,.16)}.login-links i{font-size:16px}
@media(max-width:420px){body{padding:12px}.card{padding:28px 19px;border-radius:22px}.brand-logo{width:72px;height:72px}}

/* FineVPN premium visual system — static background, light effects, no motion-heavy layers */
:root{--bg:#050b18;--panel:rgba(12,25,49,.82);--border:rgba(76,177,255,.23);--accent:#36bffa;--accent-hover:#238de5;--text:#eef7ff;--muted:#9ab1cc;--font:'Vazirmatn','Inter',system-ui,sans-serif}
html,body{min-height:100%;background:#050b18}
body{background:radial-gradient(ellipse at 50% 12%,rgba(20,112,209,.22),transparent 42%),radial-gradient(ellipse at 80% 82%,rgba(105,65,220,.12),transparent 35%),#050b18;font-family:var(--font);}
.card{max-width:460px;background:linear-gradient(150deg,rgba(17,36,68,.88),rgba(7,16,34,.9));border:1px solid rgba(87,185,255,.28);border-radius:28px;box-shadow:0 24px 70px rgba(0,0,0,.46),0 0 30px rgba(39,145,255,.1);backdrop-filter:blur(13px);-webkit-backdrop-filter:blur(13px)}
.brand-logo{width:88px;height:88px;border-radius:23px;background:rgba(26,91,155,.2);border:1px solid rgba(80,185,255,.45);box-shadow:0 0 26px rgba(42,151,255,.18);overflow:hidden}
.brand-logo img{width:100%;height:100%;object-fit:cover;display:block}
.brand-title{font-size:25px;font-weight:900;letter-spacing:.02em;color:#f3f9ff}
.brand-sub{font-size:12.5px;color:#a9c8e7;line-height:1.9}
.fl{color:#b6cbe2;font-weight:700}.fi{background:rgba(3,12,28,.58);border-color:rgba(100,183,255,.22);border-radius:13px;color:#f4f9ff;padding-top:13px;padding-bottom:13px}.fi:focus{border-color:#42bfff;background:rgba(4,17,38,.82);box-shadow:0 0 0 3px rgba(55,176,255,.14)}.fi-wrap i{color:#79caff}
.btn-p{background:linear-gradient(120deg,#36c3ff,#2476ef 62%,#4d5ef4);color:#04142a;border:1px solid rgba(151,220,255,.55);border-radius:14px;box-shadow:0 9px 26px rgba(18,117,237,.28);font-size:14px;font-weight:900;min-height:48px}.btn-p:hover{background:linear-gradient(120deg,#72d5ff,#3d8df8 62%,#7180ff);box-shadow:0 10px 28px rgba(18,117,237,.34)}
.login-contact{border-top:1px solid rgba(94,180,255,.18)}.login-provider{color:#a8bfd9}.login-provider strong{color:#e8f5ff}.login-signature{color:#7fcaff}.login-links a{border-color:rgba(85,177,255,.25);background:rgba(40,123,205,.1);color:#bce4ff;border-radius:12px}
button,input{font-family:var(--font)}
.brand-logo,.logo-img,.mob-logo,.brand-img{position:relative;display:grid;place-items:center;background:linear-gradient(145deg,rgba(26,125,204,.19),rgba(99,91,230,.13))}
.logo-fallback{position:absolute;inset:0;display:grid;place-items:center;color:#9cddff;font-weight:950;font-size:25px;letter-spacing:-.08em;text-shadow:0 0 18px rgba(57,180,255,.6);pointer-events:none}
.brand-logo .logo-fallback{font-size:42px}.mob-logo .logo-fallback{font-size:17px}.brand-img .logo-fallback{font-size:26px}.logo-img .logo-fallback{font-size:25px}
.brand-logo img,.logo-img img,.mob-logo img,.brand-img img{position:relative;z-index:1}
@media(max-width:480px){.card{padding:28px 20px;border-radius:23px}.brand-logo{width:78px;height:78px}}
.login-password-wrap .fi{padding-left:48px;padding-right:44px;direction:ltr;text-align:left}
.login-password-wrap .login-lock-icon{right:14px;left:auto;position:absolute;pointer-events:none;color:#79caff}
.login-password-toggle{position:absolute;left:8px;top:50%;transform:translateY(-50%);width:36px;height:36px;border:1px solid rgba(91,180,255,.2);border-radius:10px;background:rgba(56,153,226,.09);color:#9edfff;display:grid;place-items:center;cursor:pointer;z-index:2}
.login-password-toggle:hover{background:rgba(56,153,226,.18);border-color:rgba(112,197,255,.42)}
.login-password-toggle i,.login-password-toggle span{position:static!important;right:auto!important;pointer-events:none!important;color:inherit!important;font-size:19px;line-height:1;font-weight:900}
.login-password-toggle:focus-visible{outline:2px solid #53c5ff;outline-offset:2px}
@media(max-width:360px){.card{padding:24px 16px}.brand-title{font-size:22px}}
/* Glossy glass finish: static highlights keep mobile rendering inexpensive. */
.card{position:relative;overflow:hidden;background:linear-gradient(148deg,rgba(21,48,85,.92),rgba(7,17,39,.94) 58%,rgba(11,21,48,.92));border-color:rgba(111,197,255,.34);box-shadow:0 28px 76px rgba(0,0,0,.48),0 0 42px rgba(52,164,255,.12),inset 0 1px rgba(255,255,255,.12)}
.card:before{content:"";position:absolute;inset:0 0 auto;height:1px;background:linear-gradient(90deg,transparent,rgba(220,246,255,.7),transparent);pointer-events:none}
.fi{box-shadow:inset 0 1px 8px rgba(0,0,0,.18)}
.login-password-toggle{box-shadow:inset 0 1px rgba(255,255,255,.1),0 4px 14px rgba(0,0,0,.16)}
.btn-p{position:relative;overflow:hidden;text-shadow:0 1px rgba(255,255,255,.18);box-shadow:0 12px 28px rgba(26,125,234,.28),inset 0 1px rgba(255,255,255,.58)}
.btn-p:active{transform:translateY(1px)}
</style>
</head>
<body>
<div class="card">
  <div class="brand">
    <div class="brand-logo"><span class="logo-fallback" aria-hidden="true">F</span><img src="https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png" alt="𝑭𝒊𝒏𝒆𝑽𝑷𝑵" onerror="this.remove()"></div>
    <div class="brand-title">𝑭𝒊𝒏𝒆𝑽𝑷𝑵</div>
    <div class="brand-sub">ورود امن به پنل مدیریت 𝑭𝒊𝒏𝒆𝑽𝑷𝑵</div>
  </div>
  <form id="lf">
    <div class="fg">
      <label class="fl">نام کاربری</label>
      <div class="fi-wrap"><input type="text" id="username" class="fi" placeholder="نام کاربری..." required autocomplete="username"><i class="ti ti-user"></i></div>
    </div>
    <div class="fg">
      <label class="fl">رمز عبور</label>
      <div class="fi-wrap login-password-wrap">
        <input type="password" id="password" class="fi" placeholder="••••••••" autocomplete="current-password" required aria-label="رمز عبور">
        <i class="ti ti-lock login-lock-icon" aria-hidden="true"></i>
        <button type="button" class="login-password-toggle" onclick="toggleLoginPassword()" aria-label="نمایش رمز" aria-pressed="false" title="نمایش / پنهان کردن رمز"><span id="login-password-eye" aria-hidden="true">◉</span></button>
      </div>
    </div>
    <button type="submit" class="btn-p" id="lbtn"><i class="ti ti-login"></i> <span>ورود به پنل مدیریت</span></button>
    <div class="err-box" id="err-box"><i class="ti ti-alert-circle"></i><span id="err-text">ورود ناموفق</span></div>
  </form>
  <div class="login-contact">
    <div class="login-provider">ارائه‌دهنده: <strong>مـحـمـدصـادق افـغـان</strong></div>
    <div class="login-signature">𝑀𝑢ℎ𝑎𝑚𝑚𝑎𝑑𝒔𝒂𝒅𝒊𝒒</div>
    <div class="login-links"><a href="https://t.me/sadiq_AFG1" target="_blank" rel="noopener noreferrer"><i class="ti ti-brand-telegram"></i> پشتیبانی @sadiq_AFG1</a></div>
  </div>
</div>
<script>
function toggleLoginPassword(){
  const input=document.getElementById('password');
  const button=document.querySelector('.login-password-toggle');
  const icon=document.getElementById('login-password-eye');
  if(!input||!button||!icon)return;
  const reveal=input.type==='password';
  input.type=reveal?'text':'password';
  icon.textContent=reveal?'⊘':'◉';
  button.setAttribute('aria-pressed',String(reveal));
  button.setAttribute('aria-label',reveal?'پنهان کردن رمز':'نمایش رمز');
  button.title=reveal?'پنهان کردن رمز':'نمایش رمز';
}

document.getElementById('lf').addEventListener('submit',async(e)=>{
  e.preventDefault();
  const b=document.getElementById('lbtn'),eb=document.getElementById('err-box');
  eb.style.display='none';
  const password=document.getElementById('password').value.trim();
  if(!password){eb.style.display='flex';document.getElementById('err-text').textContent='رمز را وارد کنید';document.getElementById('password').focus();return;}
  b.disabled=true;b.innerHTML='<i class="ti ti-loader"></i> <span>در حال بررسی...</span>';
  try{
    const r=await fetch('/api/login',{
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body:JSON.stringify({username:document.getElementById('username').value.trim(),password:document.getElementById('password').value.trim()})
    });
    const d=await r.json();
    if(d.ok){location.href='/dashboard';}
    else{
      eb.style.display='flex';
      document.getElementById('err-text').textContent=d.detail||'نام کاربری یا رمز عبور اشتباه است';
      b.disabled=false;b.innerHTML='<i class="ti ti-login"></i> <span>ورود به پنل مدیریت</span>';
    }
  }catch(err){
    eb.style.display='flex';
    document.getElementById('err-text').textContent='خطا در اتصال به سرور';
    b.disabled=false;b.innerHTML='<i class="ti ti-login"></i> <span>ورود به پنل مدیریت</span>';
  }
});
</script>
</body>
</html>"""


DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><link rel="icon" href="https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>𝑭𝒊𝒏𝒆𝑽𝑷𝑵</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#070d0b;--bg2:#0b1613;--bg3:#0f1f1a;
  --card:#0d1c18;--card-b:rgba(16,185,129,0.14);--card-bh:rgba(16,185,129,0.32);
  --accent:#10B981;--accent2:#34D399;--accent-d:rgba(16,185,129,0.12);
  --green:#10B981;--green-bg:rgba(16,185,129,0.1);--green-t:#34D399;
  --red:#EF4444;--red-bg:rgba(239,68,68,0.1);--red-t:#F87171;
  --amber:#F59E0B;--amber-bg:rgba(245,158,11,0.1);--amber-t:#FCD34D;
  --purple:#10B981;--purple-bg:rgba(16,185,129,0.1);
  --t1:#E8F4FF;--t2:#7BAED4;--t3:#3D6B8E;
  --sidebar-w:248px;--radius:16px;
  --shadow:0 4px 24px rgba(0,0,0,0.35);
}
[data-theme="light"]{
  --bg:#F0FDF9;--bg2:#E1FBEF;--bg3:#D2F5E6;
  --card:#FFFFFF;--card-b:rgba(16,185,129,0.15);--card-bh:rgba(16,185,129,0.35);
  --accent:#10B981;--accent2:#047857;--accent-d:rgba(37,99,235,0.08);
  --green:#059669;--green-bg:rgba(5,150,105,0.08);--green-t:#065F46;
  --red:#DC2626;--red-bg:rgba(220,38,38,0.08);--red-t:#991B1B;
  --amber:#D97706;--amber-bg:rgba(217,119,6,0.08);--amber-t:#92400E;
  --purple:#059669;--purple-bg:rgba(5,150,105,0.08);
  --t1:#0F172A;--t2:#334155;--t3:#64748B;
  --shadow:0 4px 20px rgba(0,0,0,0.1);
}
html,body{height:100%;overflow-x:hidden}
body{font-family:'Vazirmatn',sans-serif;background:var(--bg);color:var(--t1);min-height:100vh;display:flex;font-size:14px;transition:background .3s,color .3s}
::-webkit-scrollbar{width:5px;height:5px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--bg3);border-radius:3px}
a{color:inherit;text-decoration:none}
.sidebar{width:var(--sidebar-w);min-height:100vh;background:var(--bg2);border-left:1px solid var(--card-b);display:flex;flex-direction:column;flex-shrink:0;position:fixed;right:0;top:0;bottom:0;z-index:200;transition:transform .25s cubic-bezier(.4,0,.2,1),background .3s,border-color .3s}
.logo{display:flex;align-items:center;gap:12px;padding:20px 16px 16px;border-bottom:1px solid var(--card-b)}
.logo-img{width:38px;height:38px;border-radius:50%;overflow:hidden;border:1px solid var(--card-b);box-shadow:0 0 14px rgba(16,185,129,.35),0 0 8px rgba(16,185,129,.25);flex-shrink:0}
.logo-img img{width:100%;height:100%;object-fit:cover}
.logo-name{font-size:13.5px;font-weight:700;color:var(--t1)}
.logo-sub{font-size:10px;color:var(--t3);margin-top:1px}
.sb-close{display:none;position:absolute;left:12px;top:20px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:8px;font-size:16px;align-items:center;justify-content:center;cursor:pointer}
.nav-wrap{flex:1;overflow-y:auto;padding:6px 0 8px}
.nav-sec{padding:14px 14px 4px;font-size:9px;letter-spacing:.14em;text-transform:uppercase;color:var(--t3);font-weight:700}
.nav-it{display:flex;align-items:center;gap:9px;padding:9px 14px;color:var(--t3);font-size:12.5px;cursor:pointer;border-right:2px solid transparent;transition:all .15s;margin:1px 6px}
.nav-it i{font-size:16px;width:18px;text-align:center;flex-shrink:0}
.nav-it:hover{background:var(--accent-d);color:var(--t2)}
.nav-it.on{background:var(--accent-d);color:var(--t1);border-right-color:var(--accent);font-weight:600}
.nav-badge{margin-right:auto;background:rgba(16,185,129,0.15);color:var(--accent2);font-size:9px;padding:1px 6px;border-radius:20px;font-weight:700}
.sb-foot{padding:12px 14px;border-top:1px solid var(--card-b)}
.theme-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--accent-d);color:var(--t2);border-radius:9px;padding:8px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid var(--card-b);cursor:pointer;width:100%;transition:.15s;margin-bottom:7px}
.theme-btn:hover{background:var(--card-b);color:var(--t1)}
.logout-btn{display:flex;align-items:center;justify-content:center;gap:7px;background:var(--red-bg);color:var(--red-t);border-radius:9px;padding:8px;font-size:12px;font-weight:500;font-family:inherit;border:1px solid rgba(239,68,68,0.2);cursor:pointer;width:100%;transition:.15s;margin-top:6px}
.logout-btn:hover{background:rgba(239,68,68,0.2)}
.mob-top{display:none;position:fixed;top:0;right:0;left:0;height:52px;background:var(--bg2);border-bottom:1px solid var(--card-b);z-index:150;align-items:center;justify-content:space-between;padding:0 14px;transition:background .3s}
.mob-top .ml{display:flex;align-items:center;gap:9px}
.mob-logo{width:28px;height:28px;border-radius:50%;overflow:hidden;box-shadow:0 0 8px rgba(16,185,129,.35)}
.mob-logo img{width:100%;height:100%;object-fit:cover}
.mob-title{color:var(--t1);font-size:13px;font-weight:700}
.mob-right{display:flex;gap:6px}
.menu-btn{background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;color:#fff;width:36px;height:36px;border-radius:10px;font-size:18px;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:all .2s;box-shadow:0 4px 14px rgba(16,185,129,.35)}
.menu-btn:hover{transform:scale(1.08);box-shadow:0 6px 18px rgba(16,185,129,.5)}
.menu-btn:active{transform:scale(.94)}
.menu-btn i{transition:transform .25s}
.menu-btn.open i{transform:rotate(90deg)}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:190;backdrop-filter:blur(3px)}
.overlay.show{display:block}
.main{margin-right:var(--sidebar-w);flex:1;padding:28px 28px 60px;min-width:0;transition:margin .25s}
.pg{display:none}
.pg.on{display:block;animation:fi .2s ease}
@keyframes fi{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
.topbar{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:22px;flex-wrap:wrap;gap:12px}
.tb-title{font-size:18px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:8px;letter-spacing:-.02em}
.tb-title i{color:var(--accent);font-size:20px}
.tb-sub{font-size:11px;color:var(--t3);margin-top:4px}
.tb-right{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.badge{font-size:10px;padding:3px 10px;border-radius:20px;font-weight:700;display:inline-flex;align-items:center;gap:5px;white-space:nowrap}
.bg-green{background:var(--green-bg);color:var(--green-t)}
.bg-blue{background:var(--accent-d);color:var(--accent2)}
.bg-amber{background:var(--amber-bg);color:var(--amber-t)}
.bg-red{background:var(--red-bg);color:var(--red-t)}
.bg-purple{background:var(--purple-bg);color:#34D399}
.dot{width:6px;height:6px;border-radius:50%;flex-shrink:0;display:inline-block}
.dg{background:var(--green)}.dr{background:var(--red)}.da{background:var(--amber)}.db{background:var(--accent)}
.pulse{animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}}
.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:13px;margin-bottom:18px}
.metric{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:17px 17px 14px;transition:all .2s;position:relative;overflow:hidden;cursor:default}
.metric::after{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--accent);opacity:0;transition:.2s}
.metric:hover{border-color:var(--card-bh);transform:translateY(-2px);box-shadow:var(--shadow)}
.metric:hover::after{opacity:1}
.metric.suc::after{background:var(--green)}
.metric.dan::after{background:var(--red)}
/* ══════ صفحه ترافیک - ریدیزاین ══════ */
.traf-hero{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:13px;margin-bottom:18px}
.traf-main-stat{background:linear-gradient(155deg,var(--bg3) 0%,var(--card) 60%);border:1px solid var(--card-b);border-radius:20px;padding:22px 24px;position:relative;overflow:hidden}
.traf-main-stat::before{content:'';position:absolute;top:-50px;left:-50px;width:200px;height:200px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none}
.traf-main-label{font-size:10.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.08em;display:flex;align-items:center;gap:6px;margin-bottom:10px;position:relative;z-index:1}
.traf-main-val{font-size:34px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.02em;display:flex;align-items:baseline;gap:6px;position:relative;z-index:1}
.traf-main-val span{font-size:14px;font-weight:500;color:var(--t3)}
.traf-trend{display:inline-flex;align-items:center;gap:4px;font-size:11px;font-weight:700;padding:4px 10px;border-radius:20px;margin-top:12px;position:relative;z-index:1}
.traf-trend.up{background:var(--green-bg);color:var(--green-t)}
.traf-trend.down{background:var(--red-bg);color:var(--red-t)}
.traf-mini{background:var(--card);border:1px solid var(--card-b);border-radius:20px;padding:18px 19px;display:flex;flex-direction:column;justify-content:space-between;transition:.2s}
.traf-mini:hover{border-color:var(--card-bh);transform:translateY(-2px)}
.traf-mini-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
.traf-mini-icon{width:32px;height:32px;border-radius:9px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:15px}
.traf-mini-icon.pk{background:var(--amber-bg);color:var(--amber)}
.traf-mini-icon.lo{background:var(--purple-bg);color:var(--purple)}
.traf-mini-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.traf-mini-val{font-size:21px;font-weight:800;color:var(--t1);letter-spacing:-.01em}
.traf-mini-sub{font-size:9.5px;color:var(--t3);margin-top:3px}

.traf-chart-card{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:22px 24px 18px;box-shadow:var(--shadow);margin-bottom:16px}
.traf-chart-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:6px;flex-wrap:wrap;gap:10px}
.traf-chart-title{font-size:14px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:8px}
.traf-chart-title i{color:var(--accent);font-size:18px}
.traf-chart-sub{font-size:10.5px;color:var(--t3);margin-top:3px}
.traf-legend{display:flex;gap:14px;align-items:center}
.traf-legend-item{display:flex;align-items:center;gap:6px;font-size:10.5px;color:var(--t2);font-weight:600}
.traf-legend-dot{width:8px;height:8px;border-radius:3px}
.traf-range-tabs{display:flex;gap:4px;background:var(--accent-d);padding:3px;border-radius:10px;border:1px solid var(--card-b)}
.traf-range-tab{padding:6px 13px;border-radius:8px;font-size:10.5px;font-weight:700;color:var(--t3);cursor:pointer;transition:.15s;border:none;background:transparent;font-family:inherit}
.traf-range-tab.on{background:var(--accent);color:#fff;box-shadow:0 2px 8px rgba(16,185,129,.35)}
.traf-chart-body{height:320px;margin-top:14px;position:relative}

@media(max-width:900px){.traf-hero{grid-template-columns:1fr 1fr}}
@media(max-width:520px){.traf-hero{grid-template-columns:1fr}.traf-chart-body{height:260px}}
.m-icon{width:34px;height:34px;border-radius:8px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;margin-bottom:11px;color:var(--accent);font-size:17px}
.m-icon.suc{background:var(--green-bg);color:var(--green)}
.m-icon.dan{background:var(--red-bg);color:var(--red)}
.m-icon.pur{background:var(--purple-bg);color:var(--purple)}
.m-label{font-size:10px;color:var(--t3);margin-bottom:4px;font-weight:600;text-transform:uppercase;letter-spacing:.05em}
.m-val{font-size:25px;font-weight:700;color:var(--t1);line-height:1;letter-spacing:-.02em}
.m-unit{font-size:12px;font-weight:400;color:var(--t3)}
.m-sub{font-size:10px;color:var(--t3);margin-top:6px;display:flex;align-items:center;gap:3px}
.vless-box{background:linear-gradient(135deg,var(--bg3) 0%,var(--bg2) 100%);border:1px solid var(--card-b);border-radius:18px;padding:20px 22px;margin-bottom:18px;box-shadow:var(--shadow);position:relative;overflow:hidden;transition:background .3s}
.vless-box::before{content:'';position:absolute;top:-50px;left:-50px;width:180px;height:180px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none}
.vl-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:13px;flex-wrap:wrap;gap:8px}
.vl-title{color:var(--t2);font-size:11px;display:flex;align-items:center;gap:6px;font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.vl-title i{color:var(--accent);font-size:15px}
.vl-code{background:rgba(0,0,0,.18);border:1px solid var(--card-b);border-radius:9px;padding:13px 15px;font-size:11px;font-family:ui-monospace,monospace;color:var(--accent2);word-break:break-all;line-height:1.8;letter-spacing:.01em}
[data-theme="light"] .vl-code{background:rgba(0,0,0,.04)}
.vl-actions{display:flex;gap:8px;margin-top:13px;flex-wrap:wrap}
.btn{font-family:inherit;font-size:12px;font-weight:500;border-radius:9px;padding:8px 14px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:all .15s;white-space:nowrap}
.btn i{font-size:13px}
.btn:disabled{opacity:.4;cursor:not-allowed}
.btn-o:hover{background:var(--accent-d);border-color:rgba(16,185,129,.3)}
.btn-g{background:var(--accent-d);color:var(--accent2);border:1px solid rgba(16,185,129,.15)}
.btn-g:hover{background:rgba(16,185,129,.22)}
.btn-d{background:var(--red-bg);color:var(--red-t);border:1px solid rgba(239,68,68,.2)}
.btn-d:hover{background:rgba(239,68,68,.2)}
.btn-pur{background:var(--purple-bg);color:#34D399;border:1px solid rgba(16,185,129,.2)}
.btn-pur:hover{background:rgba(16,185,129,.22)}
.btn-amber{background:var(--amber-bg);color:var(--amber-t);border:1px solid rgba(245,158,11,.2)}
.btn-amber:hover{background:rgba(245,158,11,.22)}
.btn-sm{padding:5px 9px;font-size:10.5px;border-radius:7px}
.btn-icon{width:30px;height:30px;padding:0;justify-content:center;border-radius:5px}
.card{background:var(--card);border:1px solid var(--card-b);border-radius:var(--radius);padding:18px 20px;transition:border-color .2s,background .3s}
.card:hover{border-color:var(--card-bh)}
.card-title{font-size:12.5px;font-weight:700;color:var(--t1);margin-bottom:15px;display:flex;align-items:center;gap:7px}
.card-title i{font-size:16px;color:var(--accent)}
.ml-auto{margin-right:auto}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-bottom:16px}
.g3{display:grid;grid-template-columns:2fr 1fr;gap:13px;margin-bottom:16px}
.mb16{margin-bottom:16px}
.sr{display:flex;align-items:center;justify-content:space-between;padding:9px 0;border-bottom:1px solid rgba(16,185,129,0.05);font-size:12px}
.sr:last-child{border-bottom:none}
.sr-k{color:var(--t2);display:flex;align-items:center;gap:6px}
.sr-k i{font-size:13px;color:var(--t3)}
.sr-v{color:var(--t1);font-weight:600;font-size:11.5px}
.ch{position:relative;height:230px}
.ch-lg{position:relative;height:330px}
.ch-sm{position:relative;height:185px}
.exp-chip{font-size:9px;padding:3px 8px;border-radius:6px;font-weight:700;display:inline-flex;align-items:center;gap:3px}
.ec-ok{background:var(--green-bg);color:var(--green-t)}
.ec-warn{background:var(--amber-bg);color:var(--amber-t)}
.ec-exp{background:var(--red-bg);color:var(--red-t)}
.ec-inf{background:var(--accent-d);color:var(--accent2)}
.tog{width:19px;height:34px;border-radius:19px;background:rgba(100,116,139,0.25);position:relative;cursor:pointer;transition:.2s;flex-shrink:0;border:none}
.tog::after{content:'';position:absolute;width:13px;height:13px;border-radius:50%;background:#fff;left:3px;bottom:3px;transition:.2s;box-shadow:0 1px 3px rgba(0,0,0,.3)}
.tog.on{background:var(--green)}
.tog.on::after{bottom:18px}
.form-row{display:flex;gap:9px;flex-wrap:wrap;align-items:flex-end}
.fg{display:flex;flex-direction:column;gap:5px}
.fg label{font-size:10px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.fi,.fs{padding:9px 12px;border-radius:9px;border:1px solid var(--card-b);background:rgba(0,0,0,.18);color:var(--t1);font-family:inherit;font-size:12px;outline:none;transition:.15s;min-width:100px}
[data-theme="light"] .fi,[data-theme="light"] .fs{background:rgba(0,0,0,.04)}
.fi::placeholder{color:var(--t3)}
.fi:focus,.fs:focus{border-color:rgba(16,185,129,.45);background:rgba(0,0,0,.25);box-shadow:0 0 0 3px rgba(16,185,129,.08)}
.fs option{background:var(--bg2)}
[data-theme="light"] .fs option{background:#fff}
.cl{background:var(--accent-d);border:1px solid rgba(16,185,129,.15);border-radius:10px;padding:11px 13px;font-size:11px;color:var(--t2);display:flex;gap:9px;align-items:flex-start;line-height:1.8;margin-top:12px}
.cl i{font-size:15px;color:var(--accent);margin-top:1px;flex-shrink:0}
.cl.amber{background:var(--amber-bg);border-color:rgba(245,158,11,.2);color:var(--amber-t)}
/* ══════ پنل ساخت کانفیگ - طراحی جدید ══════ */
.create-panel{background:linear-gradient(155deg,var(--bg3) 0%,var(--card) 55%);border:1px solid var(--card-b);border-radius:22px;padding:0;overflow:hidden;box-shadow:var(--shadow);margin-bottom:16px;position:relative}
.create-panel::before{content:'';position:absolute;top:-60px;left:-60px;width:220px;height:220px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none}
.cp-head{display:flex;align-items:center;gap:13px;padding:22px 24px 18px;position:relative;z-index:1}
.cp-head-icon{width:44px;height:44px;border-radius:13px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;flex-shrink:0;box-shadow:0 6px 18px rgba(16,185,129,.35)}
.cp-head-text{flex:1;min-width:0}
.cp-head-title{font-size:15px;font-weight:800;color:var(--t1);letter-spacing:-.01em}
.cp-head-sub{font-size:11px;color:var(--t3);margin-top:2px}
.cp-body{padding:2px 24px 22px;position:relative;z-index:1}
.cp-row{display:grid;grid-template-columns:1.3fr 1fr;gap:14px;margin-bottom:16px}
.cp-block{background:rgba(0,0,0,.14);border:1px solid var(--card-b);border-radius:14px;padding:14px 16px}
[data-theme="light"] .cp-block{background:rgba(37,99,235,.03)}
.cp-block-label{font-size:10px;font-weight:800;color:var(--t2);text-transform:uppercase;letter-spacing:.08em;display:flex;align-items:center;gap:6px;margin-bottom:11px}
.cp-block-label i{color:var(--accent);font-size:14px}
.cp-input-full{width:100%;padding:10px 13px;border-radius:10px;border:1px solid var(--card-b);background:rgba(0,0,0,.18);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.15s}
[data-theme="light"] .cp-input-full{background:#fff}
.cp-input-full:focus{border-color:rgba(16,185,129,.5);box-shadow:0 0 0 3px rgba(16,185,129,.1)}
.cp-input-full::placeholder{color:var(--t3)}
.cp-mini-row{display:flex;gap:8px;margin-top:9px}
.cp-quota-inputs{display:flex;gap:8px}
.cp-quota-inputs .cp-input-full{flex:1}
.cp-quota-inputs select.cp-input-full{flex:0 0 76px}
.chip-row{display:flex;gap:6px;flex-wrap:wrap;margin-top:9px}
.chip{font-size:10.5px;font-weight:700;padding:5px 12px;border-radius:8px;background:var(--accent-d);color:var(--t2);border:1px solid var(--card-b);cursor:pointer;transition:.15s;white-space:nowrap}
.chip:hover{background:rgba(16,185,129,.18);color:var(--accent2)}
.chip.active{background:var(--accent);color:#fff;border-color:var(--accent);box-shadow:0 3px 10px rgba(16,185,129,.35)}
.proto-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:9px}
.proto-card{border:1.5px solid var(--card-b);border-radius:13px;padding:13px 12px;cursor:pointer;transition:.18s;text-align:center;position:relative;background:rgba(0,0,0,.1)}
[data-theme="light"] .proto-card{background:#fff}
.proto-card:hover{border-color:var(--card-bh);transform:translateY(-1px)}
.proto-card.active{border-color:var(--accent);background:var(--accent-d);box-shadow:0 0 0 3px rgba(16,185,129,.1)}
.proto-card.active .proto-card-check{opacity:1;transform:scale(1)}
.proto-card-check{position:absolute;top:7px;left:7px;width:16px;height:16px;border-radius:50%;background:var(--accent);color:#fff;font-size:10px;display:flex;align-items:center;justify-content:center;opacity:0;transform:scale(.5);transition:.18s}
.proto-card-icon{width:32px;height:32px;border-radius:9px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:16px;margin:0 auto 8px}
.proto-card.active .proto-card-icon{background:var(--accent);color:#fff}
.proto-card-title{font-size:11px;font-weight:800;color:var(--t1)}
.proto-card-desc{font-size:9px;color:var(--t3);margin-top:3px;line-height:1.5}
.cp-footer{display:flex;align-items:center;justify-content:space-between;gap:12px;padding-top:16px;border-top:1px solid var(--card-b);flex-wrap:wrap}
.cp-footer-note{display:flex;align-items:center;gap:8px;font-size:10.5px;color:var(--t3);line-height:1.7;flex:1;min-width:220px}
.cp-footer-note i{color:var(--accent);font-size:15px;flex-shrink:0}
.cp-submit-btn{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border:none;border-radius:13px;padding:13px 26px;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;box-shadow:0 6px 20px rgba(16,185,129,.35);transition:.18s;white-space:nowrap}
.cp-submit-btn:hover{transform:translateY(-2px);box-shadow:0 10px 26px rgba(16,185,129,.45)}
.cp-submit-btn:active{transform:translateY(0) scale(.98)}
@media(max-width:760px){
  .cp-row{grid-template-columns:1fr}
  .proto-cards{grid-template-columns:1fr}
  .cp-footer{flex-direction:column;align-items:stretch}
  .cp-submit-btn{justify-content:center}
}
/* ══════ پنل اطلاعات سرور ══════ */
.srv-panel{background:linear-gradient(155deg,var(--bg3) 0%,var(--card) 60%);border:1px solid var(--card-b);border-radius:22px;overflow:hidden;box-shadow:var(--shadow);position:relative}
.srv-panel::before{content:'';position:absolute;top:-60px;left:-60px;width:200px;height:200px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none}
.srv-hero{display:flex;align-items:center;gap:14px;padding:22px 24px;position:relative;z-index:1;border-bottom:1px solid var(--card-b)}
.srv-hero-icon{width:50px;height:50px;border-radius:14px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;flex-shrink:0;box-shadow:0 6px 18px rgba(16,185,129,.35)}
.srv-hero-text{flex:1;min-width:0}
.srv-hero-domain{font-size:15px;font-weight:800;color:var(--t1);word-break:break-all}
.srv-hero-sub{font-size:10.5px;color:var(--t3);margin-top:4px;display:flex;align-items:center;gap:6px}
.srv-tiles{display:grid;grid-template-columns:1fr 1fr;gap:11px;padding:20px 22px 22px;position:relative;z-index:1}
.srv-tile{display:flex;align-items:center;gap:11px;background:rgba(0,0,0,.14);border:1px solid var(--card-b);border-radius:13px;padding:12px 14px;transition:.18s}
[data-theme="light"] .srv-tile{background:rgba(37,99,235,.03)}
.srv-tile:hover{border-color:var(--card-bh);transform:translateY(-1px)}
.srv-tile-icon{width:34px;height:34px;border-radius:10px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0}
.srv-tile-text{min-width:0}
.srv-tile-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-bottom:3px}
.srv-tile-val{font-size:12px;font-weight:700;color:var(--t1);word-break:break-word}

/* ══════ پنل تغییر رمز ══════ */
.pw-panel{background:linear-gradient(155deg,var(--bg3) 0%,var(--card) 60%);border:1px solid var(--card-b);border-radius:22px;overflow:hidden;box-shadow:var(--shadow);position:relative}
.pw-panel::before{content:'';position:absolute;top:-60px;right:-60px;width:200px;height:200px;background:radial-gradient(circle,var(--purple-bg),transparent 70%);pointer-events:none}
.pw-hero{display:flex;align-items:center;gap:14px;padding:22px 24px 18px;position:relative;z-index:1}
.pw-hero-icon{width:50px;height:50px;border-radius:14px;background:linear-gradient(135deg,var(--purple),#047857);display:flex;align-items:center;justify-content:center;color:#fff;font-size:22px;flex-shrink:0;box-shadow:0 6px 18px rgba(16,185,129,.35)}
.pw-hero-text{flex:1;min-width:0}
.pw-hero-title{font-size:15px;font-weight:800;color:var(--t1)}
.pw-hero-sub{font-size:10.5px;color:var(--t3);margin-top:3px}
.pw-body{padding:2px 24px 22px;position:relative;z-index:1}
.pw-field{position:relative;margin-bottom:13px}
.pw-field label{display:block;font-size:10px;font-weight:700;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:7px}
.pw-input{width:100%;padding:11px 42px 11px 14px;border-radius:11px;border:1px solid var(--card-b);background:rgba(0,0,0,.18);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.15s}
[data-theme="light"] .pw-input{background:#fff}
.pw-input:focus{border-color:rgba(16,185,129,.5);box-shadow:0 0 0 3px rgba(16,185,129,.1)}
.pw-eye{position:absolute;left:12px;top:34px;background:none;border:none;color:var(--t3);cursor:pointer;font-size:16px;padding:4px;display:flex}
.pw-eye:hover{color:var(--purple)}
.pw-strength{height:4px;border-radius:3px;background:var(--accent-d);margin-top:8px;overflow:hidden;display:flex;gap:3px}
.pw-strength-seg{flex:1;height:100%;border-radius:3px;background:rgba(100,116,139,.2);transition:.25s}
.pw-strength-label{font-size:9.5px;color:var(--t3);margin-top:5px;display:flex;align-items:center;gap:5px}
.pw-reqs{display:flex;flex-wrap:wrap;gap:6px;margin-top:11px;margin-bottom:16px}
.pw-req{font-size:9.5px;padding:4px 10px;border-radius:7px;background:var(--accent-d);color:var(--t3);font-weight:600;display:flex;align-items:center;gap:4px;transition:.18s}
.pw-req.met{background:var(--green-bg);color:var(--green-t)}
.pw-submit{width:100%;justify-content:center;background:linear-gradient(135deg,var(--purple),#047857);color:#fff;border:none;border-radius:12px;padding:12px;font-family:inherit;font-size:13px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:8px;box-shadow:0 6px 18px rgba(16,185,129,.32);transition:.18s}
.pw-submit:hover{transform:translateY(-2px);box-shadow:0 10px 24px rgba(16,185,129,.42)}
.pw-submit:active{transform:translateY(0) scale(.98)}

/* ══════ اتصالات فعال - نسخه پیشرفته ══════ */
.conn-hero{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:18px}
.conn-hero-tile{background:var(--card);border:1px solid var(--card-b);border-radius:16px;padding:16px 18px;position:relative;overflow:hidden;transition:.2s}
.conn-hero-tile:hover{border-color:var(--card-bh);transform:translateY(-2px);box-shadow:var(--shadow)}
.conn-hero-tile::after{content:'';position:absolute;bottom:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--green),transparent)}
.conn-hero-icon{width:32px;height:32px;border-radius:9px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;justify-content:center;font-size:15px;margin-bottom:10px}
.conn-hero-tile:nth-child(2) .conn-hero-icon{background:var(--accent-d);color:var(--accent)}
.conn-hero-tile:nth-child(3) .conn-hero-icon{background:var(--purple-bg);color:var(--purple)}
.conn-hero-tile:nth-child(4) .conn-hero-icon{background:var(--amber-bg);color:var(--amber)}
.conn-hero-label{font-size:9.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em;margin-bottom:4px}
.conn-hero-val{font-size:21px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.02em}
.conn-hero-unit{font-size:11px;color:var(--t3);font-weight:500}

.conn-toolbar{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:14px;flex-wrap:wrap}
.conn-toolbar-title{font-size:12px;font-weight:800;color:var(--t2);display:flex;align-items:center;gap:7px;text-transform:uppercase;letter-spacing:.06em}
.conn-toolbar-title i{color:var(--green);font-size:15px}
.conn-live-badge{display:flex;align-items:center;gap:6px;font-size:10.5px;font-weight:700;color:var(--green-t);background:var(--green-bg);padding:5px 12px;border-radius:20px;border:1px solid rgba(16,185,129,.2)}
.conn-live-dot{width:6px;height:6px;border-radius:50%;background:var(--green);animation:pulse 1.6s infinite}

.conn-grid-v2{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px}
.conn-card-v2{background:var(--card);border:1px solid var(--card-b);border-radius:18px;padding:0;overflow:hidden;transition:all .22s cubic-bezier(.4,0,.2,1);position:relative}
.conn-card-v2:hover{border-color:var(--card-bh);transform:translateY(-3px);box-shadow:0 14px 32px rgba(0,0,0,.22)}
.conn-card-v2-glow{position:absolute;top:-40px;left:-40px;width:140px;height:140px;background:radial-gradient(circle,rgba(16,185,129,.1),transparent 70%);pointer-events:none}
.conn-card-v2-top{display:flex;align-items:center;gap:12px;padding:16px 17px 13px;position:relative;z-index:1}
.conn-avatar{width:42px;height:42px;border-radius:13px;background:linear-gradient(135deg,var(--green),#0D9668);display:flex;align-items:center;justify-content:center;color:#fff;font-size:18px;flex-shrink:0;position:relative;box-shadow:0 4px 14px rgba(16,185,129,.3)}
.conn-avatar::after{content:'';position:absolute;inset:-4px;border-radius:16px;border:1.5px solid var(--green);opacity:.4;animation:breathe2 2.4s ease-in-out infinite}
@keyframes breathe2{0%,100%{transform:scale(1);opacity:.4}50%{transform:scale(1.12);opacity:0}}
.conn-card-v2-id{flex:1;min-width:0}
.conn-ip-v2{font-family:ui-monospace,monospace;font-size:14px;font-weight:800;color:var(--t1);display:flex;align-items:center;gap:6px}
.conn-ip-copy{background:none;border:none;color:var(--t3);cursor:pointer;font-size:12px;padding:2px;display:flex;transition:.15s}
.conn-ip-copy:hover{color:var(--accent)}
.conn-label-v2{font-size:10.5px;color:var(--t3);margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.conn-status-pill{font-size:9px;font-weight:800;padding:4px 9px;border-radius:20px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;gap:4px;white-space:nowrap;flex-shrink:0}
.conn-card-v2-divider{height:1px;background:linear-gradient(90deg,transparent,var(--card-b) 15%,var(--card-b) 85%,transparent);margin:0 17px}
.conn-card-v2-body{padding:14px 17px 16px}
.conn-proto-row{margin-bottom:12px}
.conn-stat-row{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:12px}
.conn-stat-box{display:flex;align-items:center;gap:8px}
.conn-stat-icon{width:26px;height:26px;border-radius:8px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:12px;flex-shrink:0}
.conn-stat-icon.time{background:var(--purple-bg);color:var(--purple)}
.conn-stat-text-label{font-size:8.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.04em}
.conn-stat-text-val{font-size:11.5px;font-weight:700;color:var(--t1);margin-top:1px}
.conn-duration-track{height:5px;border-radius:4px;background:var(--accent-d);overflow:hidden;position:relative}
.conn-duration-fill{height:100%;border-radius:4px;background:linear-gradient(90deg,var(--green),#3FD79C);position:relative;overflow:hidden}
.conn-duration-fill::after{content:'';position:absolute;inset:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,.35),transparent);width:40%;animation:shimmer 1.8s linear infinite}
@keyframes shimmer{0%{transform:translateX(-120%)}100%{transform:translateX(280%)}}

.conn-empty-v2{text-align:center;padding:70px 20px;background:var(--card);border:1px dashed var(--card-b);border-radius:20px}
.conn-empty-v2-icon{width:64px;height:64px;border-radius:18px;background:var(--accent-d);display:flex;align-items:center;justify-content:center;font-size:28px;color:var(--t3);margin:0 auto 16px}
.conn-empty-v2-title{font-size:13.5px;font-weight:700;color:var(--t2);margin-bottom:5px}
.conn-empty-v2-sub{font-size:11px;color:var(--t3)}

@media(max-width:760px){.conn-hero{grid-template-columns:1fr 1fr}}
@media(max-width:500px){.conn-grid-v2{grid-template-columns:1fr}}

@media(max-width:560px){.srv-tiles{grid-template-columns:1fr}}
.cl.amber i{color:var(--amber)}
.sub-box{background:rgba(16,185,129,.07);border:1px solid rgba(16,185,129,.2);border-radius:10px;padding:14px 16px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;margin-top:11px}
.sub-url{font-family:ui-monospace,monospace;font-size:10.5px;color:#34D399;word-break:break-all;flex:1}
.spbar{height:4px;border-radius:3px;background:var(--accent-d);margin-top:5px;overflow:hidden}
.spfill{height:100%;border-radius:3px;background:linear-gradient(90deg,var(--accent),var(--accent2));transition:width 1s}
.empty{text-align:center;padding:50px 20px;color:var(--t3)}
.empty i{font-size:40px;opacity:.3;margin-bottom:12px;display:block}
.empty p{font-size:12.5px;margin-top:4px}
/* ══════ گروه‌های ساب - ریدیزاین کامل ══════ */
.subs-toolbar{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:16px;flex-wrap:wrap}
.subs-search{flex:1;min-width:200px;position:relative}
.subs-search input{width:100%;padding:11px 40px 11px 15px;border-radius:12px;border:1px solid var(--card-b);background:var(--card);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.15s}
.subs-search input:focus{border-color:rgba(16,185,129,.5);box-shadow:0 0 0 3px rgba(16,185,129,.1)}
.subs-search i{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:15px}

.sub-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:16px;margin-bottom:18px}
.sub-card{background:var(--card);border:1px solid var(--card-b);border-radius:20px;padding:0;overflow:hidden;transition:all .25s cubic-bezier(.4,0,.2,1);position:relative}
.sub-card:hover{border-color:var(--card-bh);transform:translateY(-4px);box-shadow:0 16px 36px rgba(0,0,0,.24)}
.sub-card-top{background:linear-gradient(155deg,var(--purple-bg) 0%,transparent 65%);padding:20px 20px 16px;position:relative}
.sub-card-top::before{content:'';position:absolute;top:-30px;left:-30px;width:130px;height:130px;background:radial-gradient(circle,rgba(16,185,129,.14),transparent 70%);pointer-events:none}
.sub-card-head-v2{display:flex;align-items:flex-start;gap:13px;position:relative;z-index:1}
.sub-card-icon{width:46px;height:46px;border-radius:14px;background:linear-gradient(135deg,var(--purple),#047857);display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;flex-shrink:0;box-shadow:0 6px 16px rgba(16,185,129,.35)}
.sub-card-titles{flex:1;min-width:0}
.sub-card-name-v2{font-size:15.5px;font-weight:800;color:var(--t1);letter-spacing:-.01em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sub-card-desc-v2{font-size:11px;color:var(--t3);margin-top:3px;line-height:1.6;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.sub-card-lock-badge{flex-shrink:0;width:26px;height:26px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:12px}
.sub-card-lock-badge.locked{background:var(--amber-bg);color:var(--amber-t)}
.sub-card-lock-badge.open{background:var(--green-bg);color:var(--green-t)}

.sub-card-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:0;position:relative;z-index:1;margin-top:16px;background:rgba(0,0,0,.14);border:1px solid var(--card-b);border-radius:13px;overflow:hidden}
[data-theme="light"] .sub-card-stats{background:rgba(5,150,105,.03)}
.sub-card-stat{padding:11px 8px;text-align:center;border-left:1px solid var(--card-b)}
.sub-card-stat:last-child{border-left:none}
.sub-card-stat-val{font-size:15px;font-weight:800;color:var(--t1);line-height:1.2}
.sub-card-stat-label{font-size:8.5px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-top:4px}

.sub-card-url-row{margin:14px 20px 0;background:rgba(16,185,129,.08);border:1px dashed rgba(16,185,129,.25);border-radius:11px;padding:9px 12px;display:flex;align-items:center;gap:8px}
.sub-card-url-text{font-family:ui-monospace,monospace;font-size:9.5px;color:#34D399;flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sub-card-url-copy{background:none;border:none;color:var(--purple);cursor:pointer;font-size:13px;padding:3px;display:flex;flex-shrink:0;transition:.15s}
.sub-card-url-copy:hover{color:#34D399;transform:scale(1.1)}

.sub-card-bottom{padding:14px 20px 18px;display:flex;gap:7px;flex-wrap:wrap}
.sub-card-bottom .btn{flex:1;justify-content:center;min-width:fit-content}

.subs-empty-v2{text-align:center;padding:70px 20px;background:var(--card);border:1px dashed var(--card-b);border-radius:20px;grid-column:1/-1}
.subs-empty-v2-icon{width:64px;height:64px;border-radius:18px;background:var(--purple-bg);display:flex;align-items:center;justify-content:center;font-size:28px;color:var(--purple);margin:0 auto 16px}
.subs-empty-v2-title{font-size:13.5px;font-weight:700;color:var(--t2);margin-bottom:5px}
.subs-empty-v2-sub{font-size:11px;color:var(--t3)}

/* ══════ مودال ساخت گروه - نسخه فشرده ══════ */
.modal-v2{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:0;max-width:430px;width:calc(100% - 32px);max-height:92vh;overflow-y:auto;position:relative;animation:fi .2s ease;box-shadow:0 24px 70px rgba(0,0,0,.5)}
.modal-v2-head{background:linear-gradient(155deg,rgba(16,185,129,.14) 0%,transparent 65%);padding:18px 22px 14px;position:relative;overflow:hidden}
.modal-v2-head::before{content:'';position:absolute;top:-50px;left:-50px;width:160px;height:160px;background:radial-gradient(circle,rgba(16,185,129,.2),transparent 70%);pointer-events:none}
.modal-v2-close{position:absolute;top:14px;left:14px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:9px;font-size:15px;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:2;transition:.15s}
.modal-v2-close:hover{background:var(--red-bg);color:var(--red-t);border-color:rgba(239,68,68,.25)}
.modal-v2-icon{width:42px;height:42px;border-radius:13px;background:linear-gradient(135deg,var(--purple),#047857);display:flex;align-items:center;justify-content:center;color:#fff;font-size:19px;margin-bottom:10px;position:relative;z-index:1;box-shadow:0 8px 18px rgba(16,185,129,.4)}
.modal-v2-title{font-size:15.5px;font-weight:800;color:var(--t1);position:relative;z-index:1;letter-spacing:-.01em}
.modal-v2-sub{font-size:10.5px;color:var(--t3);margin-top:3px;position:relative;z-index:1;line-height:1.6}
.modal-v2-body{padding:16px 22px 20px;border-top:1px solid var(--card-b)}
.modal-v2-field{margin-bottom:11px}
.modal-v2-field label{display:flex;align-items:center;gap:5px;font-size:9.5px;font-weight:800;color:var(--t2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:6px}
.modal-v2-field label i{color:var(--purple);font-size:13px}
.modal-v2-input-wrap{position:relative}
.modal-v2-input-wrap>i{position:absolute;right:13px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:14px;pointer-events:none;transition:.15s;z-index:1}
.modal-v2-input{width:100%;padding:9px 38px 9px 13px;border-radius:11px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:12.5px;outline:none;transition:.18s}
[data-theme="light"] .modal-v2-input{background:rgba(5,150,105,.04)}
.modal-v2-input::placeholder{color:var(--t3)}
.modal-v2-input:focus{border-color:rgba(16,185,129,.55);box-shadow:0 0 0 3px rgba(16,185,129,.12);background:rgba(0,0,0,.28)}
[data-theme="light"] .modal-v2-input:focus{background:#fff}
.modal-v2-input:focus~i{color:var(--purple)}
.modal-v2-hint{background:rgba(16,185,129,.08);border:1px solid rgba(16,185,129,.18);border-radius:11px;padding:9px 12px;font-size:10px;color:var(--t2);display:flex;gap:7px;align-items:flex-start;line-height:1.6;margin-top:2px}
.modal-v2-hint i{font-size:14px;color:var(--accent);margin-top:1px;flex-shrink:0}
.modal-v2-footer{display:flex;gap:8px;margin-top:15px}
.modal-v2-btn-cancel{flex:.75;justify-content:center;padding:10px;border-radius:11px;background:transparent;border:1px solid var(--card-b);color:var(--t2);font-family:inherit;font-size:12px;font-weight:700;cursor:pointer;transition:.15s;display:flex;align-items:center}
.modal-v2-btn-cancel:hover{background:var(--accent-d);color:var(--t1)}
.modal-v2-btn-submit{flex:1;justify-content:center;padding:10px;border-radius:11px;background:linear-gradient(135deg,var(--purple),#047857);color:#fff;border:none;font-family:inherit;font-size:12px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:6px;box-shadow:0 6px 18px rgba(16,185,129,.4);transition:.18s}
.modal-v2-btn-submit:hover{transform:translateY(-2px);box-shadow:0 10px 24px rgba(16,185,129,.5)}
.modal-v2-btn-submit:active{transform:translateY(0) scale(.98)}

/* ══════ مودال انتخاب کانفیگ - نسخه پیشرفته ══════ */
.lmodal-head{background:linear-gradient(155deg,var(--accent-d) 0%,transparent 70%);padding:22px 24px 18px;position:relative;border-bottom:1px solid var(--card-b)}
.lmodal-icon-row{display:flex;align-items:center;gap:12px;position:relative;z-index:1}
.lmodal-icon{width:44px;height:44px;border-radius:13px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff;font-size:19px;flex-shrink:0;box-shadow:0 6px 16px rgba(16,185,129,.35)}
.lmodal-title-v2{font-size:14.5px;font-weight:800;color:var(--t1)}
.lmodal-sub-v2{font-size:10.5px;color:var(--t3);margin-top:2px}
.lmodal-search{margin-top:14px;position:relative}
.lmodal-search input{width:100%;padding:10px 38px 10px 13px;border-radius:11px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:12px;outline:none}
[data-theme="light"] .lmodal-search input{background:#fff}
.lmodal-search input:focus{border-color:rgba(16,185,129,.5);box-shadow:0 0 0 3px rgba(16,185,129,.1)}
.lmodal-search i{position:absolute;left:12px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:14px}
.lmodal-quickbar{display:flex;gap:8px;margin-top:11px;position:relative;z-index:1}
.lmodal-qbtn{font-size:10px;font-weight:700;padding:5px 11px;border-radius:8px;background:var(--accent-d);color:var(--accent2);border:1px solid var(--card-b);cursor:pointer;transition:.15s;font-family:inherit}
.lmodal-qbtn:hover{background:rgba(16,185,129,.2)}
.lmodal-count{margin-right:auto;font-size:10.5px;color:var(--t3);display:flex;align-items:center}

.lmodal-list{padding:10px 14px;max-height:360px;overflow-y:auto}
.lrow-v2{display:flex;align-items:center;gap:11px;padding:11px 12px;border-radius:13px;cursor:pointer;transition:.15s;margin-bottom:4px;border:1px solid transparent}
.lrow-v2:hover{background:var(--accent-d)}
.lrow-v2.checked{background:rgba(16,185,129,.1);border-color:rgba(16,185,129,.25)}
.lrow-v2-check{width:20px;height:20px;border-radius:7px;border:2px solid var(--card-b);flex-shrink:0;display:flex;align-items:center;justify-content:center;transition:.15s;background:rgba(0,0,0,.14)}
.lrow-v2.checked .lrow-v2-check{background:var(--accent);border-color:var(--accent)}
.lrow-v2-check i{font-size:12px;color:#fff;opacity:0;transform:scale(.5);transition:.15s}
.lrow-v2.checked .lrow-v2-check i{opacity:1;transform:scale(1)}
.lrow-v2-avatar{width:34px;height:34px;border-radius:10px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0}
.lrow-v2.checked .lrow-v2-avatar{background:var(--accent);color:#fff}
.lrow-v2-info{flex:1;min-width:0}
.lrow-v2-name{font-size:12.5px;font-weight:700;color:var(--t1);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.lrow-v2-meta{font-size:9.5px;color:var(--t3);margin-top:2px;display:flex;align-items:center;gap:6px}
.lrow-v2-status{font-size:9px;font-weight:800;padding:3px 9px;border-radius:20px;flex-shrink:0;white-space:nowrap}
.lrow-v2-status.on{background:var(--green-bg);color:var(--green-t)}
.lrow-v2-status.on{background:var(--green-bg);color:var(--green-t)}
.lrow-links{display:flex;gap:4px;margin-top:6px;flex-wrap:wrap}
.lrow-link-btn{background:rgba(16,185,129,.08);border:1px solid rgba(16,185,129,.22);color:#34D399;border-radius:7px;padding:3px 7px;font-size:9.5px;font-family:ui-monospace,monospace;cursor:pointer;display:inline-flex;align-items:center;gap:4px;transition:.15s;max-width:100%}
.lrow-link-btn:hover{background:rgba(16,185,129,.18);transform:translateY(-1px)}
.lrow-link-btn span{white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:180px}
.lrow-v2-status.off{background:var(--red-bg);color:var(--red-t)}

.lmodal-footer{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:16px 24px;border-top:1px solid var(--card-b)}
.lmodal-footer-info{font-size:10.5px;color:var(--t3);display:flex;align-items:center;gap:6px}
.lmodal-footer-info i{color:var(--accent)}
.lmodal-footer-btns{display:flex;gap:8px}

@media(max-width:500px){.sub-grid{grid-template-columns:1fr}.sub-card-stats{grid-template-columns:repeat(3,1fr)}}

.modal-bg{display:none;position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:500;align-items:center;justify-content:center;backdrop-filter:blur(4px)}
.modal-bg.open{display:flex}
.modal{background:var(--card);border:1px solid var(--card-b);border-radius:20px;padding:28px 26px;max-width:520px;width:calc(100% - 32px);max-height:90vh;overflow-y:auto;position:relative;animation:fi .2s ease}
.modal-close{position:absolute;top:14px;left:14px;background:var(--accent-d);border:1px solid var(--card-b);color:var(--t2);width:30px;height:30px;border-radius:8px;font-size:16px;display:flex;align-items:center;justify-content:center;cursor:pointer;border:none}
.modal-title{font-size:16px;font-weight:700;color:var(--t1);margin-bottom:18px;display:flex;align-items:center;gap:8px}
.modal-title i{color:var(--accent)}
.lrow{display:flex;align-items:center;gap:8px;padding:7px 0;border-bottom:1px solid rgba(16,185,129,.05)}
.lrow:last-child{border-bottom:none}
.lrow-check{width:16px;height:16px;border-radius:4px;cursor:pointer;accent-color:var(--accent)}
.lrow-label{flex:1;font-size:12px;color:var(--t1)}
.lrow-badge{font-size:9px;padding:2px 7px;border-radius:5px;background:var(--green-bg);color:var(--green-t);font-weight:700}
.toast{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);border:1px solid var(--card-b);color:var(--t1);border-radius:10px;padding:10px 18px;font-size:12.5px;opacity:0;transition:all .25s;z-index:999;pointer-events:none;display:flex;align-items:center;gap:8px;box-shadow:var(--shadow);white-space:nowrap}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
.toast.ok{border-color:rgba(16,185,129,.3);background:var(--green-bg);color:var(--green-t)}
.toast.err{border-color:rgba(239,68,68,.3);background:var(--red-bg);color:var(--red-t)}
.dash-footer{border-top:1px solid var(--card-b);margin-top:14px;padding-top:14px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}
.df-text{font-size:10px;color:var(--t3)}
.df-link{font-size:11.5px;color:var(--accent2);display:flex;align-items:center;gap:5px;font-weight:600}

/* ══════ کانفیگ‌ها - طراحی ردیفی حرفه‌ای ══════ */
.cfg-grid{display:flex;flex-direction:column;gap:10px}
.cfg-card{background:var(--card);border:1px solid var(--card-b);border-radius:14px;padding:0;transition:all .2s cubic-bezier(.4,0,.2,1);position:relative;overflow:hidden}
.cfg-card:hover{border-color:var(--card-bh);box-shadow:0 6px 24px rgba(0,0,0,.18)}
.cfg-card.is-off{opacity:.6}
.cfg-card.is-exp{opacity:.78}
.cfg-row{display:flex;align-items:center;gap:16px;padding:14px 18px}
.cfg-status-dot{width:9px;height:9px;border-radius:50%;background:var(--green);flex-shrink:0;box-shadow:0 0 0 3px var(--green-bg)}
.cfg-card.is-off .cfg-status-dot{background:var(--red);box-shadow:0 0 0 3px var(--red-bg)}
.cfg-card.is-exp .cfg-status-dot{background:var(--amber);box-shadow:0 0 0 3px var(--amber-bg)}
.cfg-identity{display:flex;flex-direction:column;gap:3px;min-width:150px;flex-shrink:0}
.cfg-label{font-size:13.5px;font-weight:700;color:var(--t1);display:flex;align-items:center;gap:7px}
.cfg-sub-meta{display:flex;align-items:center;gap:8px;font-size:10px;color:var(--t3)}
.cfg-uuid-mini{font-family:ui-monospace,monospace;font-size:9.5px;color:var(--accent2);background:var(--accent-d);padding:2px 7px;border-radius:5px;cursor:pointer;transition:.15s}
.cfg-uuid-mini:hover{background:rgba(16,185,129,.2)}
.cfg-divider-v{width:1px;align-self:stretch;background:var(--card-b);flex-shrink:0}
.cfg-usage-col{flex:1;min-width:160px;display:flex;flex-direction:column;gap:5px}
.ubar{height:5px;border-radius:4px;background:rgba(16,185,129,0.1);overflow:hidden}
.ubar-f{height:100%;border-radius:4px;transition:width .4s ease}
.utxt{font-size:10px;color:var(--t3);display:flex;justify-content:space-between}
.cfg-exp-col{flex-shrink:0;min-width:110px}
.cfg-badges-col{display:flex;flex-direction:column;gap:5px;flex-shrink:0;align-items:flex-end}
.cfg-actions{display:flex;gap:5px;flex-shrink:0}
.proto-chip{font-size:9px;padding:3px 8px;border-radius:6px;font-weight:700;white-space:nowrap}
.pc-ws{background:var(--accent-d);color:var(--accent2)}
.pc-xhttp{background:var(--purple-bg);color:#34D399}
.pc-ultra{background:var(--green-bg);color:var(--green-t)}
.cfg-sub-tag{font-size:9.5px;color:var(--t3);display:flex;align-items:center;gap:4px;white-space:nowrap}
.cfg-sub-tag i{color:var(--purple);font-size:11px}
.tog{width:19px;height:30px;border-radius:19px;background:rgba(100,116,139,0.25);position:relative;cursor:pointer;transition:.2s;flex-shrink:0;border:none}
.tog::after{content:'';position:absolute;width:13px;height:13px;border-radius:50%;background:#fff;left:3px;top:3px;transition:.2s;box-shadow:0 1px 3px rgba(0,0,0,.3)}
.tog.on::after{top:14px}
.tog.on{background:var(--green)}

@media(max-width:880px){
  .cfg-row{flex-wrap:wrap}
  .cfg-divider-v{display:none}
  .cfg-usage-col{min-width:100%;order:5}
}

/* ── زیر ۷۶۸px: تبدیل کامل به کارت موبایل ── */
@media(max-width:768px){
  .cfg-grid{display:grid;grid-template-columns:1fr;gap:13px}
  .cfg-card{border-radius:16px}
  .cfg-row{flex-direction:column;align-items:stretch;gap:12px;padding:16px}
  .cfg-row-top{display:flex;align-items:center;justify-content:space-between;gap:10px}
  .cfg-identity{min-width:0;flex:1}
  .cfg-usage-col{min-width:0}
  .cfg-exp-col{min-width:0}
  .cfg-badges-col{flex-direction:row;align-items:center;flex-wrap:wrap}
  .cfg-actions{flex-wrap:wrap;border-top:1px solid var(--card-b);padding-top:10px;margin-top:2px;width:100%}
}

/* ══════ اتصالات فعال با IP ══════ */
.conn-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px}
.conn-card{background:var(--card);border:1px solid var(--card-b);border-radius:16px;padding:15px 17px;transition:.2s;position:relative;overflow:hidden}
.conn-card:hover{border-color:var(--card-bh);transform:translateY(-1px)}
.conn-card::before{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--green)}
.conn-ip-row{display:flex;align-items:center;gap:8px;margin-bottom:10px}
.conn-ip-icon{width:32px;height:32px;border-radius:9px;background:var(--green-bg);color:var(--green-t);display:flex;align-items:center;justify-content:center;font-size:15px;flex-shrink:0}
.conn-ip{font-family:ui-monospace,monospace;font-size:13px;font-weight:700;color:var(--t1)}
.conn-label{font-size:10.5px;color:var(--t3);margin-top:1px}
.conn-meta{display:flex;justify-content:space-between;align-items:center;font-size:10px;color:var(--t3);padding-top:10px;border-top:1px solid var(--card-b)}

/* ══════ لاگ فعالیت‌ها ══════ */
.log-timeline{display:flex;flex-direction:column}
.log-item{display:flex;gap:12px;padding:11px 0;border-bottom:1px solid rgba(16,185,129,.05);position:relative}
.log-item:last-child{border-bottom:none}
.log-ic{width:30px;height:30px;border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:14px;flex-shrink:0}
.log-ic.ok{background:var(--green-bg);color:var(--green-t)}
.log-ic.err{background:var(--red-bg);color:var(--red-t)}
.log-ic.warn{background:var(--amber-bg);color:var(--amber-t)}
.log-ic.info{background:var(--accent-d);color:var(--accent2)}
.log-body{flex:1;min-width:0}
.log-msg{font-size:12.5px;color:var(--t1);line-height:1.6}
.log-time{font-size:9.5px;color:var(--t3);margin-top:2px;display:flex;align-items:center;gap:5px}
.log-kind{font-size:8.5px;padding:1px 7px;border-radius:10px;background:var(--accent-d);color:var(--accent2);font-weight:700;text-transform:uppercase;letter-spacing:.04em}
.erow{padding:9px 0;border-bottom:1px solid rgba(16,185,129,.05)}
.erow:last-child{border-bottom:none}
.etime{color:var(--t3);font-size:9.5px;margin-bottom:3px;display:flex;align-items:center;gap:4px}
.emsg{color:var(--red-t);font-family:ui-monospace,monospace;background:var(--red-bg);padding:6px 9px;border-radius:6px;word-break:break-all;font-size:10.5px}

@media(max-width:1050px){
  .sidebar{transform:translateX(100%);visibility:hidden;pointer-events:none}
  .sidebar.open{transform:translateX(0);visibility:visible;pointer-events:auto;box-shadow:-10px 0 40px rgba(0,0,0,.4)}
  .sb-close{display:none}
  .sidebar.open .sb-close{display:flex}
  .main{margin-right:0;padding-top:70px}
  .mob-top{display:flex}
  .metrics{grid-template-columns:1fr 1fr}
  .g2,.g3{grid-template-columns:1fr}
}
@media(max-width:560px){
  .form-row{grid-template-columns:1fr 1fr !important}
}
@media(max-width:500px){
  .metrics{grid-template-columns:1fr}
  .main{padding:62px 12px 50px}
  .sub-grid,.cfg-grid,.conn-grid{grid-template-columns:1fr}
}
/* 𝑭𝒊𝒏𝒆𝑽𝑷𝑵 — midnight glass / luminous gold visual system */



.v-metrics{grid-template-columns:repeat(4,1fr)!important}
.v-metric{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:22px 14px!important;gap:8px}
.m-ring{width:52px;height:52px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:22px;color:#10B981;background:rgba(16,185,129,.12);border:1.5px solid rgba(16,185,129,.35);box-shadow:0 0 18px rgba(16,185,129,.15)}
.m-ring.r2{color:#34D399;background:rgba(52,211,153,.1);border-color:rgba(52,211,153,.3)}
.m-ring.r3{color:#0D9488;background:rgba(13,148,136,.12);border-color:rgba(13,148,136,.32)}
.m-ring.r4{color:#6EE7B7;background:rgba(110,231,183,.1);border-color:rgba(110,231,183,.3)}
.v-metric .m-label{font-size:11.5px!important}
.v-metric .m-val{font-size:26px!important;line-height:1.1}
.v-metric .m-sub{font-size:10.5px!important;display:flex;align-items:center;gap:5px}
@media(max-width:900px){.v-metrics{grid-template-columns:repeat(2,1fr)!important}}
@media(max-width:480px){.v-metrics{grid-template-columns:repeat(2,1fr)!important;gap:10px!important}.v-metric{padding:16px 10px!important}.m-ring{width:42px;height:42px;font-size:18px}.m-val{font-size:22px!important}}

.sr-tile{background:rgba(16,185,129,.05);border:1px solid var(--card-b);border-radius:14px;padding:14px;display:flex;flex-direction:column;gap:6px;transition:all .2s}
.sr-tile:hover{background:rgba(16,185,129,.1);border-color:var(--card-bh);transform:translateY(-2px)}
.sr-tile-ico{width:34px;height:34px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:17px}
.sr-tile-name{font-size:11.5px;font-weight:700;color:var(--t2)}
.sr-tile-val{font-size:11px;color:var(--green-t);display:flex;align-items:center;gap:6px}

/* ══════ کارت ساب قابل کلیک ══════ */
.sub-exp-card{cursor:pointer;transition:all .25s cubic-bezier(.4,0,.2,1)}
.sub-exp-card:hover{border-color:var(--card-bh);transform:translateY(-3px);box-shadow:0 14px 34px rgba(0,0,0,.3)}
.sub-exp-card.open{border-color:rgba(16,185,129,.45);box-shadow:0 0 0 3px rgba(16,185,129,.1)}
.sub-exp-body{display:none;padding:14px 0 0;border-top:1px dashed var(--card-b);margin-top:14px}
.sub-exp-card.open .sub-exp-body{display:block;animation:fi .2s ease}
.sub-exp-hint{font-size:9.5px;color:var(--t3);display:flex;align-items:center;gap:4px;margin-top:10px;justify-content:center}
.sub-exp-card.open .sub-exp-hint{display:none}
.sub-ip-row{display:flex;align-items:center;gap:9px;padding:8px 10px;border-radius:10px;background:rgba(16,185,129,.05);border:1px solid var(--card-b);margin-bottom:7px;direction:ltr}
.sub-ip-row .dot{flex-shrink:0}
.sub-ip-addr{font-family:ui-monospace,monospace;font-size:12px;font-weight:700;color:var(--t1)}
.sub-ip-meta{font-size:10px;color:var(--t3);margin-right:auto;white-space:nowrap}
.sub-log-list{max-height:220px;overflow-y:auto}
.sub-log-item{display:flex;gap:9px;padding:7px 2px;border-bottom:1px solid rgba(16,185,129,.05);font-size:11px}
.sub-log-item:last-child{border-bottom:none}
.sub-log-ic{width:24px;height:24px;border-radius:7px;display:flex;align-items:center;justify-content:center;font-size:11px;flex-shrink:0}
.sub-log-ic.ok{background:var(--green-bg);color:var(--green-t)}
.sub-log-ic.err{background:var(--red-bg);color:var(--red-t)}
.sub-log-ic.info{background:var(--accent-d);color:var(--accent2)}
.sub-log-msg{color:var(--t2);line-height:1.5;flex:1;min-width:0}
.sub-log-time{font-size:9px;color:var(--t3);white-space:nowrap}
.sub-sec-label{font-size:10px;font-weight:800;color:var(--t3);text-transform:uppercase;letter-spacing:.06em;margin:14px 0 8px;display:flex;align-items:center;gap:6px}

/* ══════ استایل یکپارچه بخش‌ها (v3) ══════ */
.pg .card{border-radius:18px}
.sec-hero{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:13px;margin-bottom:18px}
.sec-hero-tile{background:linear-gradient(155deg,var(--bg3) 0%,var(--card) 60%);border:1px solid var(--card-b);border-radius:18px;padding:18px 20px;position:relative;overflow:hidden;transition:all .2s}
.sec-hero-tile:hover{border-color:var(--card-bh);transform:translateY(-2px);box-shadow:var(--shadow)}
.sec-hero-tile::before{content:'';position:absolute;top:-40px;left:-40px;width:130px;height:130px;background:radial-gradient(circle,var(--accent-d),transparent 70%);pointer-events:none}
.sec-hero-ico{width:38px;height:38px;border-radius:11px;background:var(--accent-d);color:var(--accent);display:flex;align-items:center;justify-content:center;font-size:17px;margin-bottom:11px;position:relative;z-index:1}
.sec-hero-ico.red{background:var(--red-bg);color:var(--red-t)}
.sec-hero-ico.pur{background:var(--purple-bg);color:#34D399}
.sec-hero-ico.amb{background:var(--amber-bg);color:var(--amber-t)}
.sec-hero-label{font-size:10px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.06em;position:relative;z-index:1}
.sec-hero-val{font-size:23px;font-weight:800;color:var(--t1);line-height:1.15;margin-top:4px;position:relative;z-index:1}
.sec-hero-sub{font-size:10px;color:var(--t3);margin-top:3px;position:relative;z-index:1}
.sec-panel{background:linear-gradient(155deg,var(--bg3) 0%,var(--card) 55%);border:1px solid var(--card-b);border-radius:20px;padding:0;overflow:hidden;box-shadow:var(--shadow);margin-bottom:16px;position:relative}
.sec-panel-head{display:flex;align-items:center;gap:12px;padding:18px 22px;border-bottom:1px solid var(--card-b);position:relative;z-index:1}
.sec-panel-ico{width:40px;height:40px;border-radius:12px;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center;color:#fff;font-size:18px;flex-shrink:0;box-shadow:0 6px 16px rgba(16,185,129,.35)}
.sec-panel-ico.red{background:linear-gradient(135deg,#EF4444,#B91C1C);box-shadow:0 6px 16px rgba(239,68,68,.35)}
.sec-panel-ico.pur{background:linear-gradient(135deg,#10B981,#065F46);box-shadow:0 6px 16px rgba(16,185,129,.35)}
.sec-panel-title{font-size:14.5px;font-weight:800;color:var(--t1)}
.sec-panel-sub{font-size:10.5px;color:var(--t3);margin-top:2px;line-height:1.6}
.sec-panel-body{padding:18px 22px 20px;position:relative;z-index:1}
.sec-log-box{background:rgba(0,0,0,.22);border:1px solid var(--card-b);border-radius:12px;padding:14px;height:260px;overflow-y:auto;font-family:ui-monospace,monospace;font-size:10.5px;line-height:1.9}
.sec-log-box p{color:var(--t3)}
.sec-log-box .ok{color:var(--green-t)}
.sec-log-box .err{color:var(--red-t)}
.sec-log-box .info{color:var(--accent2)}
.sec-log-box .warn{color:var(--amber-t)}
@media(max-width:600px){.sec-panel-head{padding:15px 16px}.sec-panel-body{padding:14px 16px 16px}}



.card-title{display:flex;align-items:center;gap:9px}
.qr-modal{display:none;position:fixed;inset:0;background:rgba(0,0,0,.72);z-index:600;align-items:center;justify-content:center;backdrop-filter:blur(4px);padding:20px}
.qr-modal.open{display:flex}
.qr-box{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:26px;text-align:center;max-width:340px;width:100%;box-shadow:var(--shadow)}
.qr-title{font-size:13.5px;font-weight:800;margin-bottom:16px;color:var(--t1)}
.btn-p{background:linear-gradient(135deg,#10b981,#059669);color:#fff;box-shadow:0 4px 16px rgba(16,185,129,.3)}
.btn-p:hover{background:linear-gradient(135deg,#34d399,#10b981);box-shadow:0 6px 20px rgba(16,185,129,.4)}

/* 𝑭𝒊𝒏𝒆𝑽𝑷𝑵 — glassmorphism, deep-star sky, luminous gold */
:root, [data-theme="light"]{
  --bg:#030713;--bg2:rgba(5,11,28,.88);--bg3:rgba(17,27,52,.72);
  --card:rgba(13,22,45,.68);--card-b:rgba(231,190,82,.20);--card-bh:rgba(255,218,115,.48);
  --accent:#f0c45b;--accent2:#ffe5a0;--accent-d:rgba(240,196,91,.13);
  --green:#55d7ad;--green-bg:rgba(85,215,173,.12);--green-t:#88f0ce;
  --red:#fb7185;--red-bg:rgba(251,113,133,.12);--red-t:#fda4af;
  --amber:#f5c451;--amber-bg:rgba(245,196,81,.12);--amber-t:#ffe29a;
  --purple:#d9b968;--purple-bg:rgba(217,185,104,.13);
  --t1:#f5f4ff;--t2:#c7cbe0;--t3:#8290b6;--shadow:0 16px 44px rgba(0,0,0,.38);
}
html,body{background-color:#030713}
body{
  background-color:#030713;
  background-image:
    radial-gradient(1px 1px at 17px 23px,rgba(255,255,255,.86) 55%,transparent 100%),
    radial-gradient(1.4px 1.4px at 71px 101px,rgba(255,225,164,.72) 55%,transparent 100%),
    linear-gradient(rgba(2,6,18,.79),rgba(2,6,18,.84)),
    url("https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png");
  background-size:109px 109px,173px 173px,100% 100%,min(66vw,680px) auto;
  background-position:0 0,35px 61px,center,center;
  background-repeat:repeat,repeat,no-repeat,no-repeat;background-attachment:fixed;
}
.sidebar{background:rgba(4,10,27,.84);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);border-color:rgba(240,196,91,.2)}
.mob-top{background:rgba(4,10,27,.86);backdrop-filter:blur(22px);-webkit-backdrop-filter:blur(22px);border-color:rgba(240,196,91,.2)}
.logo{border-color:rgba(240,196,91,.18)}
.logo-img{width:44px;height:44px;border-radius:13px;border-color:rgba(255,220,125,.5);box-shadow:0 0 22px rgba(240,196,91,.22)}
.logo-img img,.mob-logo img{object-fit:cover}
.mob-logo{width:32px;height:32px;border-radius:10px;border:1px solid rgba(255,220,125,.48);box-shadow:0 0 16px rgba(240,196,91,.22)}
.card,.metric,.vless-box,.traf-main-stat,.traf-mini,.traf-chart-card,.cfg-card,.conn-card,.sec-panel,.sec-hero-tile,.modal,.qr-box,.sr-tile,.sub-exp-card{
  background:linear-gradient(145deg,rgba(18,29,57,.73),rgba(6,12,29,.69))!important;
  border-color:rgba(240,196,91,.18)!important;box-shadow:0 16px 42px rgba(0,0,0,.24);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px)
}
.card:hover,.metric:hover,.cfg-card:hover,.sec-hero-tile:hover{border-color:rgba(255,221,132,.42)!important;box-shadow:0 18px 48px rgba(0,0,0,.31),0 0 26px rgba(240,196,91,.06)}
.btn-p,.btn-pur,.menu-btn{background:linear-gradient(135deg,#fff0b8 0%,#f1ca62 42%,#bd8a25 100%)!important;color:#211805!important;border:1px solid rgba(255,233,164,.56)!important;box-shadow:0 0 18px rgba(240,196,91,.19),0 7px 22px rgba(0,0,0,.24)!important}
.btn-p:hover,.btn-pur:hover,.menu-btn:hover{background:linear-gradient(135deg,#fff6d6 0%,#ffe18a 45%,#d7a63a 100%)!important;box-shadow:0 0 26px rgba(240,196,91,.33)!important;transform:translateY(-1px)}
.btn-p i,.btn-pur i{color:#211805!important}
.btn-g,.btn-o,.theme-btn{background:rgba(240,196,91,.08)!important;color:#ffe5a0!important;border-color:rgba(240,196,91,.24)!important;backdrop-filter:blur(12px)}
.btn-g:hover,.btn-o:hover,.theme-btn:hover{background:rgba(240,196,91,.17)!important;border-color:rgba(255,221,132,.48)!important}
.fi,.fs,.modal-v2-input,textarea,input[type="text"],input[type="number"],input[type="password"]{background:rgba(4,9,24,.55)!important;border-color:rgba(240,196,91,.18)!important;color:#f5f4ff!important}
.fi:focus,.fs:focus,.modal-v2-input:focus,textarea:focus{border-color:#f0c45b!important;box-shadow:0 0 0 3px rgba(240,196,91,.12)!important}
.nav-it:hover,.nav-it.on{background:rgba(240,196,91,.1);color:#fff0bd;border-right-color:#f0c45b}
.nav-badge{background:rgba(240,196,91,.15);color:#ffe5a0}
.m-ring,.sec-panel-ico,.sec-hero-ico{color:#ffe5a0!important;border-color:rgba(240,196,91,.26)!important;box-shadow:0 0 22px rgba(240,196,91,.1)}
.m-ring.r2,.m-ring.r3,.m-ring.r4{color:#ffe5a0;background:rgba(240,196,91,.09);border-color:rgba(240,196,91,.21)}
.brand-contact{margin-top:22px;padding:18px 20px;border:1px solid rgba(240,196,91,.24);border-radius:22px;background:linear-gradient(135deg,rgba(22,31,56,.82),rgba(6,12,28,.74));box-shadow:0 18px 45px rgba(0,0,0,.28);backdrop-filter:blur(22px);display:flex;align-items:center;justify-content:space-between;gap:18px;flex-wrap:wrap}
.brand-contact-identity{display:flex;align-items:center;gap:13px;min-width:0}
.brand-contact-logo{width:60px;height:60px;object-fit:cover;border-radius:16px;border:1px solid rgba(255,220,125,.44);box-shadow:0 0 22px rgba(240,196,91,.15)}
.brand-contact-title{font-size:15px;font-weight:900;color:#fff0bd;letter-spacing:.02em}
.brand-contact-provider{font-size:11px;color:#d0d5e9;margin-top:4px}
.brand-contact-signature{font-size:12px;color:#f4d98c;margin-top:3px;letter-spacing:.04em}
.brand-contact-links{display:flex;gap:9px;flex-wrap:wrap}
.fine-tg-link{display:inline-flex;align-items:center;gap:8px;padding:10px 13px;border-radius:13px;border:1px solid rgba(240,196,91,.24);background:rgba(240,196,91,.07);color:#ffe5a0;font-size:11.5px;font-weight:700;transition:all .2s}
.fine-tg-link i{font-size:18px;color:#f6cf67}
.fine-tg-link:hover{transform:translateY(-2px);background:rgba(240,196,91,.15);box-shadow:0 0 20px rgba(240,196,91,.12)}
@media(max-width:600px){.brand-contact{padding:15px;gap:14px}.brand-contact-logo{width:50px;height:50px;border-radius:13px}.brand-contact-links{width:100%}.fine-tg-link{flex:1;justify-content:center;min-width:130px}}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;scroll-behavior:auto!important;transition-duration:.01ms!important}}







.logo-img,.mob-logo img,.brand-contact-logo{border-radius:50%!important}

/* FineVPN / admin: complete blue-cyan glass refresh; fixed ambient background */
:root{--bg:#050b18;--bg2:rgba(7,18,38,.94);--bg3:rgba(13,31,58,.82);--card:rgba(12,28,54,.72);--card-b:rgba(70,170,255,.2);--card-bh:rgba(83,190,255,.45);--accent:#38bdf8;--accent2:#77d4ff;--accent-d:rgba(56,189,248,.13);--green:#20c997;--green-bg:rgba(32,201,151,.12);--green-t:#65e7bd;--red:#fb7185;--red-bg:rgba(251,113,133,.12);--red-t:#ff9aaa;--amber:#f5b942;--amber-bg:rgba(245,185,66,.12);--amber-t:#ffd27a;--purple:#a78bfa;--purple-bg:rgba(167,139,250,.13);--t1:#eff7ff;--t2:#b7cce3;--t3:#7897b8;--shadow:0 14px 36px rgba(0,0,0,.27);--radius:20px;--sidebar-w:264px}
[data-theme="light"]{--bg:#eef5fc;--bg2:rgba(247,251,255,.96);--bg3:#e5effa;--card:rgba(255,255,255,.82);--card-b:rgba(38,126,211,.16);--card-bh:rgba(38,126,211,.32);--accent:#147ed0;--accent2:#1769bd;--accent-d:rgba(20,126,208,.09);--green:#059669;--green-bg:rgba(5,150,105,.1);--green-t:#047857;--red:#dc4b63;--red-bg:rgba(220,75,99,.1);--red-t:#b4233c;--amber:#b7791f;--amber-bg:rgba(183,121,31,.1);--amber-t:#93600f;--purple:#7c5ad6;--purple-bg:rgba(124,90,214,.1);--t1:#13253b;--t2:#36516d;--t3:#71869d;--shadow:0 10px 28px rgba(19,49,81,.09)}
html,body{background:var(--bg);color:var(--t1)}
body{font-family:'Vazirmatn','Inter',system-ui,sans-serif;background-image:radial-gradient(ellipse at 18% 8%,rgba(24,126,224,.12),transparent 32%),radial-gradient(ellipse at 88% 80%,rgba(122,79,229,.08),transparent 28%),linear-gradient(145deg,#050b18,#08142a 58%,#080f20);background-attachment:fixed;background-repeat:no-repeat;background-size:cover;}
.sidebar{background:rgba(6,17,36,.94);border-left:1px solid rgba(77,170,255,.2);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);box-shadow:-14px 0 46px rgba(0,0,0,.18)}
[data-theme="light"] .sidebar{background:rgba(248,252,255,.95)}
.logo{padding:22px 18px 19px;border-bottom:1px solid var(--card-b);gap:13px}.logo-img{width:48px;height:48px;border-radius:15px;border:1px solid rgba(94,187,255,.45);box-shadow:0 0 20px rgba(45,153,255,.17)}.logo-name{font-size:15px;font-weight:900;letter-spacing:.015em}.logo-sub{font-size:10px;color:var(--t3)}
.nav-wrap{padding:10px 0 18px}.nav-sec{padding:15px 22px 7px;font-size:9px;letter-spacing:.12em;color:var(--t3)}.nav-it{margin:3px 11px;padding:11px 14px;border:1px solid transparent;border-radius:13px;border-right:1px solid transparent;font-size:12px;font-weight:700;color:var(--t2);gap:11px}.nav-it i{font-size:17px;width:20px;color:#85b8e4}.nav-it:hover{background:rgba(56,189,248,.08);color:var(--t1);border-color:rgba(70,170,255,.14)}.nav-it.on{background:linear-gradient(105deg,rgba(30,126,219,.26),rgba(56,189,248,.1));color:#f2faff;border:1px solid rgba(77,181,255,.34);border-right:1px solid rgba(77,181,255,.34);box-shadow:0 5px 18px rgba(20,111,211,.12)}.nav-it.on i{color:#55c7ff}.nav-badge{background:rgba(45,158,239,.16);color:#9cddff;border:1px solid rgba(84,180,255,.18);padding:2px 7px}
.sb-foot{padding:13px 14px 16px;border-top:1px solid var(--card-b)}.theme-btn,.logout-btn{border-radius:12px;min-height:40px;font-weight:800}.theme-btn{background:rgba(56,189,248,.1);color:#bde8ff;border:1px solid rgba(76,174,255,.23)}.logout-btn{margin-top:7px}
.mob-top{background:rgba(6,17,36,.92);border-bottom:1px solid var(--card-b);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);padding:10px 14px}.mob-logo{width:38px;height:38px;border-radius:12px;border:1px solid rgba(94,187,255,.4)}.mob-title{font-size:14px;font-weight:900}.menu-btn{background:linear-gradient(130deg,#38bdf8,#2563eb);border-radius:12px;width:40px;height:40px;box-shadow:0 6px 16px rgba(25,115,220,.22)}
.main{padding:30px clamp(16px,2.3vw,36px) 64px}.pg{max-width:1540px;margin:0 auto}.topbar{align-items:center;padding:0 0 17px;border-bottom:1px solid var(--card-b);margin-bottom:22px}.tb-title{font-size:19px;font-weight:900;letter-spacing:-.025em}.tb-title i{color:#55c7ff}.tb-sub{font-size:11.5px}.tb-right{align-items:center}
.card,.metric,.vless-box,.traf-main-stat,.traf-mini,.traf-chart-card,.cfg-card,.conn-card,.sec-panel,.sec-hero-tile,.modal,.qr-box,.sr-tile,.sub-exp-card,.sub-card,.conn-card-v2,.create-panel{background:linear-gradient(145deg,rgba(17,39,72,.77),rgba(7,19,40,.8))!important;border:1px solid rgba(81,172,245,.2)!important;border-radius:20px!important;box-shadow:0 12px 35px rgba(0,0,0,.22)!important;backdrop-filter:blur(11px);-webkit-backdrop-filter:blur(11px)}
[data-theme="light"] .card,[data-theme="light"] .metric,[data-theme="light"] .vless-box,[data-theme="light"] .traf-main-stat,[data-theme="light"] .traf-mini,[data-theme="light"] .traf-chart-card,[data-theme="light"] .cfg-card,[data-theme="light"] .conn-card,[data-theme="light"] .sec-panel,[data-theme="light"] .sec-hero-tile,[data-theme="light"] .modal,[data-theme="light"] .qr-box,[data-theme="light"] .sr-tile,[data-theme="light"] .sub-exp-card,[data-theme="light"] .sub-card,[data-theme="light"] .conn-card-v2,[data-theme="light"] .create-panel{background:linear-gradient(145deg,rgba(255,255,255,.96),rgba(239,247,255,.92))!important;border-color:rgba(35,121,207,.16)!important}
.metric,.v-metric{padding:19px 17px!important}.m-ring{background:rgba(56,189,248,.12);color:#5bcaff;border-color:rgba(86,190,255,.32);box-shadow:0 0 14px rgba(44,158,247,.11)}
.btn{font-family:inherit;font-size:12px;font-weight:800;border-radius:12px;padding:9px 14px;min-height:36px;gap:7px;letter-spacing:0;transition:background .16s,border-color .16s,box-shadow .16s,color .16s}.btn i{font-size:15px}.btn-p{background:linear-gradient(120deg,#42c5fb,#2878ea 70%,#5b62ed)!important;color:#05182d!important;border:1px solid rgba(147,218,255,.55)!important;box-shadow:0 7px 19px rgba(31,127,230,.2)!important}.btn-p:hover{background:linear-gradient(120deg,#82dcff,#4d98fa 70%,#817aff)!important;box-shadow:0 9px 23px rgba(31,127,230,.28)!important}.btn-g,.btn-o{background:rgba(56,189,248,.09)!important;color:#bdeaff!important;border:1px solid rgba(77,179,255,.25)!important}.btn-g:hover,.btn-o:hover{background:rgba(56,189,248,.16)!important;border-color:rgba(104,197,255,.42)!important}.btn-pur{background:rgba(143,113,236,.13)!important;color:#d8ccff!important;border:1px solid rgba(160,135,255,.28)!important}.btn-d{background:rgba(225,72,101,.12)!important;color:#ffadbb!important;border:1px solid rgba(239,92,117,.23)!important}.btn-amber{background:rgba(238,176,68,.12)!important;color:#ffda91!important;border:1px solid rgba(238,176,68,.25)!important}.btn-sm{min-height:31px;padding:6px 10px}.btn-icon{width:34px;height:34px;border-radius:10px}
.fi,.fs,.cp-input-full,.subs-search input,.modal-v2-input{border:1px solid rgba(88,172,235,.2)!important;border-radius:12px!important;background:rgba(3,13,30,.38)!important;color:var(--t1)!important;font-family:inherit!important;font-size:12.5px!important;min-height:40px}.fi:focus,.fs:focus,.cp-input-full:focus,.modal-v2-input:focus{border-color:#45bfff!important;box-shadow:0 0 0 3px rgba(56,189,248,.12)!important}.fg label{font-size:11px;text-transform:none;letter-spacing:0;color:var(--t2)}
.sec-panel{overflow:hidden}.sec-panel-head{padding:18px 21px;border-bottom:1px solid var(--card-b)}.sec-panel-title{font-size:14px;font-weight:900}.sec-panel-ico{background:linear-gradient(135deg,#38bdf8,#2866e9)!important;box-shadow:0 5px 16px rgba(31,117,225,.2)!important;border-radius:13px}.sec-panel-ico.pur{background:linear-gradient(135deg,#9d88ff,#6f59d9)!important}.sec-panel-ico.amb{background:linear-gradient(135deg,#f6c15d,#d18a2e)!important}
.badge{border-radius:999px;padding:6px 10px;font-weight:800;border:1px solid var(--card-b)}.bg-blue{background:rgba(56,189,248,.12);color:#aee5ff}.bg-purple{background:rgba(167,139,250,.13);color:#d3c5ff}
.modal{border-radius:23px!important}.modal-head{border-bottom:1px solid var(--card-b)}.qr-modal{background:rgba(1,7,17,.76)}.qr-box{border:1px solid rgba(84,181,255,.3)!important}
.brand-contact{border-color:rgba(80,176,255,.2)!important;background:linear-gradient(145deg,rgba(16,38,70,.78),rgba(6,17,37,.78))!important}.brand-contact-title{color:#f0f8ff}.fine-tg-link{border-color:rgba(65,171,244,.25);background:rgba(36,131,214,.1);color:#c7ecff}.fine-tg-link i{color:#58c6ff}
.footer{color:var(--t3)}
button,a{ -webkit-tap-highlight-color:transparent }button:focus-visible,a:focus-visible,input:focus-visible,select:focus-visible{outline:2px solid #53c5ff;outline-offset:2px}
*,*::before,*::after{animation:none!important;scroll-behavior:auto!important;transition-duration:.16s!important}.card:hover,.metric:hover,.cfg-card:hover,.sec-hero-tile:hover,.sub-card:hover,.conn-card-v2:hover,.sr-tile:hover{transform:none!important}.card,.metric,.cfg-card,.sec-panel,.nav-it,.btn,.fi,.fs{transition-duration:.16s!important}
@media(max-width:900px){.main{padding:74px 16px 45px}.sidebar{box-shadow:-16px 0 42px rgba(0,0,0,.28)}}
@media(max-width:560px){.main{padding:70px 12px 38px}.topbar{align-items:flex-start}.tb-title{font-size:16px}.tb-right{width:100%;justify-content:flex-start;flex-wrap:wrap}.card{padding:15px!important}.sec-panel-head{padding:14px}.sec-panel-body{padding:14px}.btn{white-space:normal}.v-metrics{gap:9px!important}}


/* FineVPN 2026 — Midnight Glass design system */
:root{color-scheme:dark;--bg:#050914;--bg2:#081326;--bg3:#0d1d36;--card:rgba(12,26,49,.88);--card-b:rgba(87,169,255,.20);--card-bh:rgba(91,190,255,.40);--accent:#44c5ff;--accent2:#8bdcff;--accent-d:rgba(68,197,255,.12);--green:#20d7a0;--green-bg:rgba(32,215,160,.12);--green-t:#8af2d1;--red:#ff647f;--red-bg:rgba(255,100,127,.12);--red-t:#ff9aab;--amber:#f5bd5a;--amber-bg:rgba(245,189,90,.12);--amber-t:#ffda92;--purple:#aa9aff;--purple-bg:rgba(170,154,255,.12);--t1:#f2f7ff;--t2:#b6c7df;--t3:#7890b0;--shadow:0 16px 42px rgba(0,0,0,.34)}
html,body{background:#050914!important;color:var(--t1)!important;color-scheme:dark}
body{background-image:radial-gradient(ellipse at 12% 0%,rgba(29,125,221,.17),transparent 34%),radial-gradient(ellipse at 88% 86%,rgba(91,71,220,.10),transparent 30%)!important;background-attachment:fixed!important}
.sidebar{background:linear-gradient(180deg,rgba(8,18,36,.98),rgba(5,12,26,.98))!important;border-left:1px solid rgba(86,169,255,.17)!important;box-shadow:18px 0 48px rgba(0,0,0,.22)!important}
.topbar{background:rgba(7,16,33,.90)!important;border:1px solid rgba(86,169,255,.16)!important;border-radius:18px!important;box-shadow:0 12px 34px rgba(0,0,0,.18)!important;backdrop-filter:blur(18px)!important;-webkit-backdrop-filter:blur(18px)!important}
.card,.metric,.vless-box,.traf-main-stat,.traf-mini,.traf-chart-card,.cfg-card,.conn-card,.sec-panel,.sec-hero-tile,.modal,.qr-box,.sr-tile,.sub-exp-card,.sub-card,.conn-card-v2,.create-panel{background:linear-gradient(145deg,rgba(15,34,63,.94),rgba(7,17,35,.97))!important;border:1px solid rgba(85,171,255,.19)!important;box-shadow:0 12px 32px rgba(0,0,0,.24),inset 0 1px rgba(255,255,255,.025)!important;backdrop-filter:blur(16px)!important;-webkit-backdrop-filter:blur(16px)!important}
.sec-panel-head,.modal-head{border-color:rgba(85,171,255,.16)!important}
.card-title,.sec-panel-title,.sub-card-name-v2,.tb-title,.metric-val,.stat-val{color:#f3f8ff!important}
.card-subtitle,.metric-label,.sub-card-desc-v2,.stat-label,.stat-sub{color:#a9bfd9!important}
.btn{font-family:inherit!important;font-size:11.5px!important;font-weight:850!important;min-height:35px!important;padding:7px 12px!important;border-radius:11px!important;letter-spacing:0!important;white-space:nowrap}
.btn-p{background:linear-gradient(120deg,#39bdf6,#2778e9 70%,#5a62ea)!important;color:#06172c!important;border:1px solid rgba(142,216,255,.48)!important;box-shadow:0 6px 18px rgba(39,120,233,.20)!important}
.btn-pur,.btn-g,.btn-o,.sub-card-url-copy,.lrow-link-btn{background:rgba(56,153,226,.105)!important;color:#c9edff!important;border:1px solid rgba(91,180,244,.24)!important}
.btn-d{background:rgba(244,83,112,.12)!important;color:#ffb1bf!important;border:1px solid rgba(244,110,133,.23)!important}
.btn-amber{background:rgba(245,189,90,.12)!important;color:#ffdc9b!important;border:1px solid rgba(245,189,90,.23)!important}
.btn-sm{min-height:30px!important;padding:5px 9px!important;font-size:10.5px!important}.btn-icon{width:32px!important;height:32px!important;padding:0!important}
.fi,.fs,.cp-input-full,.subs-search input,.modal-v2-input{background:rgba(3,12,27,.78)!important;border:1px solid rgba(91,169,236,.22)!important;color:#f2f7ff!important}
.fi::placeholder,.modal-v2-input::placeholder{color:#7892b2!important}
.metric,.v-metric{border-radius:17px!important}.sub-card{border-radius:19px!important;overflow:hidden}.sub-card-stats{background:rgba(48,137,216,.075)!important;border-color:rgba(85,171,255,.14)!important}.sub-card-bottom{gap:7px!important;flex-wrap:wrap}
.nav-it{border-radius:11px!important;margin:3px 7px!important}.nav-it.active,.nav-it.on{background:linear-gradient(100deg,rgba(44,157,233,.18),rgba(75,99,227,.12))!important;border:1px solid rgba(84,173,244,.19)!important;color:#d8f2ff!important}
.sb-foot{border-color:rgba(85,171,255,.16)!important}.language-btn,.logout-btn{width:100%;display:flex;align-items:center;justify-content:center;gap:8px;border-radius:11px!important;min-height:36px!important;font-family:inherit!important;font-size:11.5px!important;font-weight:850!important;cursor:pointer}.language-btn{background:rgba(56,153,226,.10)!important;color:#c7eaff!important;border:1px solid rgba(91,180,244,.22)!important;margin-bottom:7px}.language-btn:hover{background:rgba(56,153,226,.17)!important;border-color:rgba(112,197,255,.38)!important}.logout-btn{background:rgba(244,83,112,.10)!important;color:#ffb1bf!important;border:1px solid rgba(244,110,133,.21)!important}.logout-btn:hover{background:rgba(244,83,112,.16)!important}
.toast{background:rgba(10,24,46,.97)!important;border:1px solid rgba(85,171,255,.25)!important;color:#eef7ff!important;backdrop-filter:blur(16px)!important}
@media(max-width:700px){.topbar{border-radius:14px!important}.main{padding-inline:12px!important}.btn{font-size:10.5px!important;padding:6px 9px!important}.sub-card-bottom .btn{flex:1 1 auto}}

/* FineVPN responsive glass refinement: consistent on phones, tablets and desktop */
.logo-img,.mob-logo{position:relative;display:grid;place-items:center;background:linear-gradient(145deg,rgba(26,125,204,.2),rgba(99,91,230,.14))}
.logo-img img,.mob-logo img{position:relative;z-index:1}
.logo-fallback{position:absolute;inset:0;display:grid;place-items:center;color:#9cddff;font-weight:950;font-size:24px;text-shadow:0 0 18px rgba(57,180,255,.6);pointer-events:none}
html{min-width:320px;overflow-x:hidden;scrollbar-gutter:stable}
body{min-width:320px;overflow-x:hidden;-webkit-text-size-adjust:100%;text-size-adjust:100%}
body::after{content:"";position:fixed;z-index:0;pointer-events:none;width:clamp(230px,34vw,520px);aspect-ratio:1;left:50%;top:54%;transform:translate(-50%,-50%);border-radius:50%;background:url("https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png") center/contain no-repeat;opacity:.035;filter:grayscale(1);mix-blend-mode:screen}
.sidebar,.mob-top,.main,.overlay,.modal-bg,.qr-modal,.toast{isolation:isolate}
.main{position:relative;z-index:1;min-width:0}
.pg{min-width:0;width:100%}
.topbar{gap:12px;min-width:0}
.tb-left,.tb-right,.card,.sec-panel,.metric,.sub-card,.conn-card-v2,.create-panel,.srv-panel,.pw-panel{min-width:0}
.card,.metric,.sec-panel,.sub-card,.conn-card-v2,.create-panel,.srv-panel,.pw-panel,.traf-chart-card,.traf-mini,.traf-main-stat{border-radius:20px!important}
.metric,.v-metric{background:linear-gradient(145deg,rgba(17,43,76,.93),rgba(7,19,40,.96))!important;border:1px solid rgba(80,174,255,.22)!important;box-shadow:0 12px 32px rgba(0,0,0,.22),inset 0 1px rgba(255,255,255,.035)!important}
.btn,.menu-btn,.theme-btn,.logout-btn,.language-btn{touch-action:manipulation;-webkit-tap-highlight-color:transparent}
.btn{max-width:100%;min-width:0;min-height:38px!important;border-radius:12px!important;letter-spacing:0!important}
.btn:disabled{opacity:.55!important;filter:saturate(.6);cursor:wait}
input,select,textarea{max-width:100%;min-width:0}
.form-row,.cp-row,.cp-mini-row,.cp-quota-inputs,.cfg-actions,.sub-card-bottom,.tb-right{min-width:0;flex-wrap:wrap}
.form-row>.fg,.cp-row>*{min-width:0}
.sub-card-url-text,.vl-code,.cfg-link,.lrow-link,.mono,.srv-tile-val{overflow-wrap:anywhere;word-break:break-word}
.ch,.ch-lg,.ch-sm,.traf-chart-body{min-width:0;max-width:100%}
canvas{max-width:100%}
.table-wrap,.tbl-wrap,.logs-table-wrap{max-width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch}
.modal-bg{padding:14px;align-items:center;overflow-y:auto}
.modal-v2,.modal{max-width:min(100%,760px);max-height:min(92dvh,900px);overflow-y:auto;overscroll-behavior:contain}
.modal-v2-body{min-width:0}
.modal-v2-footer,.lmodal-footer-btns{display:flex;gap:8px;flex-wrap:wrap}
.modal-v2-footer .btn{flex:1 1 150px}
.logo-img,.mob-logo,.brand-contact-logo{flex-shrink:0}
@media(min-width:1500px){.main{padding-left:clamp(32px,3vw,64px);padding-right:clamp(32px,3vw,64px)}.pg{max-width:1680px}}
@media(max-width:1100px){:root{--sidebar-w:245px}.main{padding:24px 18px 48px}.g2{gap:11px}.card{padding:16px!important}}
@media(max-width:900px){.sidebar{z-index:220}.main{margin-right:0!important;padding:72px 16px 44px!important}.mob-top{display:flex!important}.topbar{padding:12px 14px;margin-bottom:16px}.pg.on{animation:none}.v-metrics{grid-template-columns:repeat(2,minmax(0,1fr))!important}.overlay{z-index:210}}
@media(max-width:640px){.main{padding:68px 11px 34px!important}.topbar{align-items:flex-start!important}.tb-left{width:100%}.tb-right{width:100%;justify-content:flex-start!important;gap:6px}.tb-title{font-size:15px!important}.tb-sub{font-size:10px}.card,.sec-panel,.create-panel,.srv-panel,.pw-panel{padding:14px!important;border-radius:17px!important}.sec-panel-head{padding:13px!important}.sec-panel-body{padding:13px!important}.g2,.g3,.cp-row{grid-template-columns:minmax(0,1fr)!important}.cp-body{padding:0 14px 15px}.cp-head{padding:16px 14px}.cp-block{padding:12px}.proto-cards{grid-template-columns:repeat(2,minmax(0,1fr))}.srv-tiles{grid-template-columns:repeat(2,minmax(0,1fr));padding:13px}.v-metrics{gap:8px!important}.v-metric{padding:13px 10px!important}.m-val{font-size:21px!important}.metric{min-width:0}.sub-grid{grid-template-columns:minmax(0,1fr)!important}.sub-card-bottom .btn{flex:1 1 105px}.cfg-actions .btn{flex:1 1 125px}.brand-contact{padding:13px!important}.brand-contact-links{width:100%}.fine-tg-link{flex:1 1 140px;justify-content:center}.modal-bg{padding:8px}.modal-v2,.modal{max-height:94dvh;border-radius:18px!important}.modal-v2-head{padding:16px 14px 12px}.modal-v2-body{padding:13px}.modal-v2-footer{position:sticky;bottom:0;background:rgba(6,17,35,.96);padding:10px 0 calc(8px + env(safe-area-inset-bottom));z-index:3}}
@media(max-width:420px){.main{padding-inline:9px!important}.mob-top{padding-inline:10px}.mob-title{font-size:12px}.mob-right{gap:4px}.menu-btn{width:36px;height:36px}.v-metrics{grid-template-columns:repeat(2,minmax(0,1fr))!important}.v-metric{padding:11px 8px!important}.m-ring{width:38px!important;height:38px!important;font-size:16px!important}.m-val{font-size:18px!important}.m-label{font-size:9px}.cp-head-title{font-size:13px}.proto-cards{grid-template-columns:repeat(2,minmax(0,1fr))}.srv-tiles{grid-template-columns:1fr}.sub-card-stats{grid-template-columns:repeat(3,minmax(0,1fr))}.sub-card-stat-val{font-size:14px}.btn{font-size:10px!important;padding:7px 8px!important}.lmodal-quickbar{flex-wrap:wrap}.lmodal-qbtn{flex:1 1 110px}}
@media(max-width:350px){.main{padding-inline:7px!important}.v-metrics{grid-template-columns:1fr 1fr!important}.tb-right .btn{flex:1 1 100px}.brand-contact-identity{gap:8px}.brand-contact-logo{width:42px;height:42px}.fine-tg-link{min-width:0}}
@media(hover:none){.btn:hover,.nav-it:hover,.card:hover,.metric:hover{transform:none!important}}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important;scroll-behavior:auto!important}}
/* Premium jelly-glass surfaces with restrained glow and crisp touch targets. */
.card,.sec-panel,.metric,.v-metric,.sub-card,.conn-card-v2,.create-panel,.srv-panel,.pw-panel,.traf-chart-card,.traf-mini,.traf-main-stat{background-image:linear-gradient(145deg,rgba(34,91,143,.18),rgba(7,20,43,.12))!important;border-color:rgba(104,190,255,.27)!important;box-shadow:0 16px 38px rgba(0,0,0,.24),inset 0 1px rgba(255,255,255,.075),inset 0 -1px rgba(56,151,227,.08)!important;backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px)}
.btn,.language-btn,.logout-btn,.menu-btn{box-shadow:inset 0 1px rgba(255,255,255,.14),0 6px 18px rgba(0,0,0,.18);transition:filter .16s ease,box-shadow .16s ease,transform .16s ease}
.btn-pur,.btn-primary,.btn-ok{box-shadow:0 8px 22px rgba(29,132,237,.24),inset 0 1px rgba(255,255,255,.32)!important}
.btn:active{transform:translateY(1px)!important;filter:brightness(1.08)}
.fi,.fs,.cp-input-full,.subs-search input,.modal-v2-input{box-shadow:inset 0 2px 8px rgba(0,0,0,.2),inset 0 1px rgba(255,255,255,.04)!important}
.nav-it.active,.nav-it.on{box-shadow:inset 0 1px rgba(255,255,255,.08),0 5px 16px rgba(24,125,216,.08)!important}
@media(prefers-reduced-motion:reduce){.btn,.language-btn,.logout-btn,.menu-btn{transition:none!important}}

</style>
</head>
<body>
<div class="toast" id="toast"></div>
<div class="qr-modal" id="qr-modal" onclick="this.classList.remove('open')">
  <div class="qr-box" onclick="event.stopPropagation()">
    <div class="qr-title" id="qr-label">QR Code</div>
    <div class="qr-img"><img id="qr-img" src="" alt="QR"></div>
    <button class="btn btn-g" style="width:100%;justify-content:center" onclick="document.getElementById('qr-modal').classList.remove('open')"><i class="ti ti-x"></i> بستن</button>
  </div>
</div>
<div class="modal-bg" id="modal-links">
  <div class="modal-v2" style="max-width:500px">
    <div class="lmodal-head">
      <button class="modal-v2-close" onclick="closeModal('modal-links')"><i class="ti ti-x"></i></button>
      <div class="lmodal-icon-row">
        <div class="lmodal-icon"><i class="ti ti-link-plus"></i></div>
        <div>
          <div class="lmodal-title-v2">مدیریت کانفیگ‌های <span id="modal-sub-name" style="color:var(--accent2)">—</span></div>
          <div class="lmodal-sub-v2">کانفیگ‌هایی که می‌خواهید در این گروه باشند را انتخاب کنید</div>
        </div>
      </div>
      <div class="lmodal-search">
        <i class="ti ti-search"></i>
        <input type="text" id="lmodal-search-inp" placeholder="جستجوی کانفیگ..." oninput="filterLmodal(this.value)">
      </div>
      <div class="lmodal-quickbar">
        <button class="lmodal-qbtn" onclick="lmodalSelectAll(true)"><i class="ti ti-checks"></i> انتخاب همه</button>
        <button class="lmodal-qbtn" onclick="lmodalSelectAll(false)"><i class="ti ti-x"></i> لغو همه</button>
        <span class="lmodal-count" id="lmodal-count">۰ انتخاب شده</span>
      </div>
    </div>
    <div class="lmodal-list" id="modal-links-body">در حال بارگذاری...</div>
    <div class="lmodal-footer">
      <div class="lmodal-footer-info"><i class="ti ti-info-circle"></i> تغییرات بلافاصله اعمال می‌شود</div>
      <div class="lmodal-footer-btns">
        <button class="btn btn-o" onclick="closeModal('modal-links')">بستن</button>
        <button class="btn btn-p" id="modal-save-btn" onclick="saveSubLinks()"><i class="ti ti-check"></i> ذخیره</button>
      </div>
    </div>
  </div>
</div>
<div class="modal-bg" id="modal-create-sub">
  <div class="modal-v2" style="max-width:520px">
    <div class="modal-v2-head">
      <button class="modal-v2-close" onclick="closeModal('modal-create-sub')"><i class="ti ti-x"></i></button>
      <div class="modal-v2-icon"><i class="ti ti-folder-plus"></i></div>
      <div class="modal-v2-title">ساخت گروه ساب</div>
      <div class="modal-v2-sub">یک صفحه پابلیک مجزا با ۲۴ کانفیگ خودکار بسازید</div>
    </div>
    <div class="modal-v2-body">
      <div class="modal-v2-field">
        <label><i class="ti ti-tag"></i> نام گروه</label>
        <input class="modal-v2-input" id="ns-name" placeholder="مثلاً: کانال اختصاصی">
      </div>
      <div class="modal-v2-field">
        <label><i class="ti ti-align-left"></i> توضیحات (اختیاری)</label>
        <input class="modal-v2-input" id="ns-desc" placeholder="توضیح کوتاه درباره این گروه">
      </div>
      <div class="modal-v2-field" style="margin-bottom:0">
        <label><i class="ti ti-lock"></i> رمز صفحه پابلیک (اختیاری)</label>
        <input class="modal-v2-input" id="ns-pw" type="password" placeholder="خالی بگذارید = بدون رمز">
      </div>
      
      <div class="cl" style="margin-top:16px;padding:12px;background:rgba(16,185,129,.1);border-radius:10px;border:1px solid rgba(16,185,129,.3)">
        <strong style="color:var(--purple-t)"><i class="ti ti-magic-wand"></i> ساخت سریع ۲۴ کانفیگ</strong>
        <p style="font-size:10.5px;color:var(--t3);margin:4px 0 8px 0">۳ پروتکل × ۲ فینگرپرینت × ۴ ALPN = ۲۴ کانفیگ (VWS/XPU/XHS)</p>
      </div>
      
      <div class="modal-v2-field">
        <label><i class="ti ti-database"></i> حجم مشترک کل (GB)</label>
        <input class="modal-v2-input" id="ns-vol" type="number" min="0" step="0.5" value="1" placeholder="مثلا 1 (خالی = نامحدود)">
      </div>
      <div class="modal-v2-field">
        <label><i class="ti ti-calendar"></i> روزهای اعتبار</label>
        <input class="modal-v2-input" id="ns-days" type="number" min="0" step="1" value="30" placeholder="مثلا 30 (۰ = بدون انقضا)">
      </div>
      <div class="modal-v2-field" style="margin-bottom:0">
        <label><i class="ti ti-users"></i> حداکثر کاربر هم‌زمان (IP Limit)</label>
        <input class="modal-v2-input" id="ns-iplimit" type="number" min="0" step="1" value="2" placeholder="مثلا 2 (۰ = نامحدود)">
      </div>
      
      <div class="cl" style="margin-top:14px"><i class="ti ti-info-circle"></i><span>حجم مشترک بین تمام ۲۴ کانفیگ تقسیم می‌شود. هر کاربر از هر کانفیگی مصرف کند، از همین حجم کم می‌شود.</span></div>
      <div id="qs-preview" style="margin-top:10px;font-size:11px;color:var(--t3);padding:8px 10px;background:rgba(16,185,129,.08);border:1px solid rgba(16,185,129,.25);border-radius:8px"></div>
      <div class="modal-v2-footer">
        <button class="btn btn-o" onclick="closeModal('modal-create-sub')" style="flex:.6">انصراف</button>
        <button class="btn btn-pur" onclick="createSubQuick()"><i class="ti ti-magic-wand"></i> ساخت گروه + ۲۴ کانفیگ</button>
      </div>
    </div>
  </div>
</div>
<div class="modal-bg" id="modal-edit-link">
  <div class="modal">
    <button class="modal-close" onclick="closeModal('modal-edit-link')"><i class="ti ti-x"></i></button>
    <div class="modal-title"><i class="ti ti-edit"></i> ویرایش کانفیگ</div>
    <input type="hidden" id="el-uuid">
    <div class="fg" style="margin-bottom:13px"><label>عنوان</label><input class="fi" id="el-label" style="width:100%"></div>
    <div class="form-row" style="margin-bottom:13px">
      <div class="fg" style="flex:1"><label>سهمیه (0 = نامحدود)</label><input class="fi" id="el-val" type="number" min="0" step="0.1" style="width:100%"></div>
      <div class="fg"><label>واحد</label><select class="fs" id="el-unit"><option value="GB">GB</option><option value="MB">MB</option></select></div>
    </div>
    <div class="fg" style="margin-bottom:13px"><label>انقضا (روز از الان، 0 = بدون تغییر/نامحدود)</label><input class="fi" id="el-exp" type="number" min="0" step="1" style="width:100%"></div>
    <div class="fg" style="margin-bottom:13px"><label>یادداشت</label><input class="fi" id="el-note" style="width:100%"></div>
    <div class="form-row" style="margin-bottom:13px">
      <div class="fg" style="flex:1"><label>Fingerprint (uTLS)</label>
        <select class="fs" id="el-fp" style="width:100%">
          <option value="chrome">chrome</option>
          <option value="firefox">firefox</option>
          <option value="safari">safari</option>
          <option value="ios">ios</option>
          <option value="android">android</option>
          <option value="edge">edge</option>
          <option value="360">360</option>
          <option value="qq">qq</option>
          <option value="random">random</option>
          <option value="randomized">randomized</option>
        </select>
      </div>
      <div class="fg" style="flex:1"><label>ALPN (خالی = پیش‌فرض)</label><input class="fi" id="el-alpn" placeholder="مثلاً: h2,http/1.1" style="width:100%"></div>
    </div>
    <div class="form-row" style="margin-bottom:16px">
      <div class="fg" style="flex:1"><label>پورت اتصال</label><input class="fi" id="el-port" type="number" min="1" max="65535" style="width:100%"></div>
      <div class="fg" style="flex:1"><label>محدودیت آی‌پی (0 = نامحدود)</label><input class="fi" id="el-iplimit" type="number" min="0" step="1" style="width:100%"></div>
    </div>
    <div class="form-row" style="margin-bottom:16px">
      <div class="fg" style="flex:1"><label>محدودیت سرعت (0 = نامحدود)</label><input class="fi" id="el-speed" type="number" min="0" step="0.5" style="width:100%"></div>
      <div class="fg"><label>واحد</label><select class="fs" id="el-speed-unit"><option value="MBIT">Mbps</option><option value="KB">KB/s</option><option value="MB">MB/s</option></select></div>
    </div>
    <div class="cl"><i class="ti ti-info-circle"></i><span>برای حفظ انقضای فعلی، فیلد انقضا را صفر بگذارید.</span></div>
    <div style="margin-top:16px;display:flex;gap:8px;justify-content:flex-end">
      <button class="btn btn-o" onclick="closeModal('modal-edit-link')">انصراف</button>
      <button class="btn btn-p" onclick="saveEditLink()"><i class="ti ti-check"></i> ذخیره تغییرات</button>
    </div>
  </div>
</div>
<div class="mob-top">
  <div class="ml">
    <div class="mob-logo"><span class="logo-fallback" aria-hidden="true">F</span><img src="https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png" alt="𝑭𝒊𝒏𝒆𝑽𝑷𝑵" onerror="this.remove()"></div>
    <span class="mob-title">𝑭𝒊𝒏𝒆𝑽𝑷𝑵</span>
  </div>
  <div class="mob-right">
    <button class="menu-btn" id="open-sb"><i class="ti ti-menu-2"></i></button>
  </div>
</div>
<div class="overlay" id="overlay"></div>
<aside class="sidebar" id="sb">
  <button class="sb-close" id="close-sb"><i class="ti ti-x"></i></button>
  <div class="logo">
    <div class="logo-img"><span class="logo-fallback" aria-hidden="true">F</span><img src="https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png" alt="𝑭𝒊𝒏𝒆𝑽𝑷𝑵" onerror="this.remove()"></div>
    <div><div class="logo-name">𝑭𝒊𝒏𝒆𝑽𝑷𝑵</div><div class="logo-sub">Secure Tunnel Manager</div></div>
  </div>
  <div class="nav-wrap">
    <div class="nav-sec">مدیریت سرویس</div>
    <div class="nav-it on" data-pg="overview"><i class="ti ti-layout-dashboard"></i> نمای کلی</div>
    <div class="nav-it" data-pg="links"><i class="ti ti-key"></i> کانفیگ‌ها <span class="nav-badge" id="links-nb">0</span></div>
    <div class="nav-it" data-pg="subgroups"><i class="ti ti-folders"></i> گروه‌های اشتراک <span class="nav-badge" id="subs-nb">0</span></div>
    <div class="nav-it" data-pg="subscriptions"><i class="ti ti-rss"></i> مدیریت اشتراک</div>
    <div class="nav-sec">پایش و گزارش</div>
    <div class="nav-it" data-pg="traffic"><i class="ti ti-chart-area-line"></i> ترافیک و مصرف</div>
    <div class="nav-it" data-pg="connections"><i class="ti ti-network"></i> اتصال‌های فعال <span class="nav-badge" id="conns-nb">0</span></div>
    <div class="nav-it" data-pg="logs"><i class="ti ti-history"></i> رویدادها</div>
    <div class="nav-it" data-pg="errors"><i class="ti ti-alert-triangle"></i> گزارش خطا</div>
    <div class="nav-sec">ابزارها و سیستم</div>
    <div class="nav-it" data-pg="categories"><i class="ti ti-category-2"></i> دسته‌بندی‌ها</div>
    <div class="nav-it" data-pg="testws"><i class="ti ti-plug-connected"></i> آزمایش WebSocket</div>
    <div class="nav-it" data-pg="settings"><i class="ti ti-adjustments-cog"></i> تنظیمات و امنیت</div>
  </div>
  <div class="sb-foot">
    <button class="language-btn" type="button" onclick="toggleLanguage()" id="language-toggle"><i class="ti ti-language"></i> English</button>
    <button class="logout-btn" id="logout-btn"><i class="ti ti-logout"></i> خروج امن</button>
  </div>
</aside>
<main class="main">
<section class="pg on" id="pg-overview">

  <!-- Quick Sub Creator Wizard -->
  <div class="card" style="border:1px solid var(--border-red, rgba(16,185,129,.35));background:linear-gradient(145deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01));position:relative;overflow:hidden;margin-bottom:20px">
    <div style="position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,transparent,#10b981,#34d399,transparent)"></div>
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px">
      <div style="width:40px;height:40px;border-radius:12px;background:linear-gradient(135deg,#10b981,#047857);display:flex;align-items:center;justify-content:center;color:#fff;font-size:20px;box-shadow:0 6px 16px rgba(16,185,129,0.35)"><i class="ti ti-wand"></i></div>
      <div>
        <div style="font-size:15px;font-weight:800;color:var(--t1,#fff)">ساخت سریع گروه ساب (۲۴ کانفیگ)</div>
        <div style="font-size:11.5px;color:var(--muted,#94a3b8)">ساخت خودکار گروه ساب، تنظیم حجم مشترک و تولید ۲۴ کانفیگ با یک کلیک</div>
      </div>
    </div>
    <div class="form-row" style="display:grid;grid-template-columns:repeat(auto-fit, minmax(130px, 1fr));gap:12px;margin-bottom:16px;flex-wrap:wrap">
      <div class="fg" style="margin-bottom:0">
        <label style="font-size:11px;font-weight:700;color:var(--muted,#94a3b8);margin-bottom:5px;display:block">نام گروه ساب</label>
        <input type="text" class="fi" id="qs-name" placeholder="مثلاً: سرویس VIP" style="width:100%">
      </div>
      <div class="fg" style="margin-bottom:0">
        <label style="font-size:11px;font-weight:700;color:var(--muted,#94a3b8);margin-bottom:5px;display:block">حجم مشترک (GB) — <span style="opacity:.8">۰ = نامحدود</span></label>
        <input type="number" class="fi" id="qs-vol" placeholder="20" min="0" step="0.5" value="20" style="width:100%">
      </div>
      <div class="fg" style="margin-bottom:0">
        <label style="font-size:11px;font-weight:700;color:var(--muted,#94a3b8);margin-bottom:5px;display:block">مدت اعتبار (روز) — <span style="opacity:.8">۰ = نامحدود</span></label>
        <input type="number" class="fi" id="qs-days" placeholder="30" min="0" step="1" value="30" style="width:100%">
      </div>
      <div class="fg" style="margin-bottom:0">
        <label style="font-size:11px;font-weight:700;color:var(--muted,#94a3b8);margin-bottom:5px;display:block">سقف کاربر (IP) — <span style="opacity:.8">۰ = نامحدود</span></label>
        <input type="number" class="fi" id="qs-ip" placeholder="2" min="0" step="1" value="2" style="width:100%">
      </div>
    </div>
    <div id="qs-summary" style="font-size:11.5px;color:var(--muted,#94a3b8);background:rgba(16,185,129,.07);border:1px solid rgba(16,185,129,.18);border-radius:12px;padding:10px 13px;margin-bottom:13px;display:flex;align-items:center;gap:8px;flex-wrap:wrap"></div>
    <script>
    function qsPreviewUpdate(){
      const el=document.getElementById('qs-summary'); if(!el) return;
      const vol=parseFloat(document.getElementById('qs-vol').value)||0;
      const days=parseInt(document.getElementById('qs-days').value)||0;
      const ip=parseInt(document.getElementById('qs-ip').value)||0;
      const parts=[];
      parts.push(vol>0?('💾 حجم مشترک: <b style="color:var(--t1,#fff)">'+vol+' GB</b> بین ۲۴ کانفیگ ≈ '+(vol/24).toFixed(2)+' GB هر کانفیگ'):'💾 حجم: <b style="color:var(--t1,#fff)">نامحدود</b>');
      parts.push(days>0?('⏱ اعتبار: <b style="color:var(--t1,#fff)">'+days+' روز</b>'):'⏱ اعتبار: <b style="color:var(--t1,#fff)">نامحدود</b>');
      parts.push(ip>0?('📱 حداکثر <b style="color:var(--t1,#fff)">'+ip+' کاربر</b> هم‌زمان'):'📱 کاربر: <b style="color:var(--t1,#fff)">نامحدود</b>');
      el.innerHTML=parts.join(' <span style="opacity:.4">•</span> ');
    }
    ['qs-vol','qs-days','qs-ip'].forEach(id=>{
      const e=document.getElementById(id); if(e){ e.addEventListener('input',qsPreviewUpdate); }
    });
    qsPreviewUpdate();
    </script>
    <button class="btn btn-p" onclick="quickSubCreate()" id="qs-submit-btn" style="width:100%;padding:12px;font-size:13.5px;font-weight:700;display:flex;align-items:center;justify-content:center;gap:8px;white-space:normal;text-align:center;line-height:1.6;flex-wrap:wrap">
      <i class="ti ti-plus"></i> ساخت گروه ساب + ۲۴ کانفیگ با حجم مشترک
    </button>
    <div id="qs-result" style="display:none;margin-top:16px;padding:14px;border-radius:12px;background:rgba(31,184,126,0.1);border:1px solid rgba(31,184,126,0.25)">
      <div style="font-size:12px;font-weight:700;color:#3fd79c;margin-bottom:6px"><i class="ti ti-check"></i> گروه ساب و ۲۴ کانفیگ با موفقیت ساخته شد!</div>
      <div style="display:flex;gap:8px;align-items:center">
        <input type="text" id="qs-pub-link" readonly class="fi" style="font-size:11px;direction:ltr;background:rgba(0,0,0,0.3);flex:1">
        <button class="btn btn-sm btn-p" onclick="navigator.clipboard.writeText(document.getElementById('qs-pub-link').value);toast('لینک کپی شد','ok')"><i class="ti ti-copy"></i> کپی</button>
      </div>
    </div>
  </div>

  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-layout-dashboard"></i> داشبورد</div><div class="tb-sub" id="last-upd">در حال بارگذاری...</div></div>
    <div class="tb-right">
      <span class="badge bg-blue" id="server-status-badge"><span class="dot db"></span> در حال بررسی</span>
      <span class="badge" id="vol-badge" title="وضعیت ذخیره‌سازی">…</span>
      <span class="badge bg-blue" id="uptime-badge">—</span>
      <button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button>
    </div>
  </div>
  <div class="metrics v-metrics">
    <div class="metric v-metric"><div class="m-ring"><i class="ti ti-users"></i></div><div class="m-label">کاربران متصل</div><div class="m-val" id="m-conns">—</div><div class="m-sub"><span id="m-sessions">—</span> نشست زنده · IP یکتا</div></div>
    <div class="metric v-metric"><div class="m-ring r2"><i class="ti ti-transfer"></i></div><div class="m-label">کل ترافیک</div><div class="m-val" id="m-traffic">—<span class="m-unit">MB</span></div><div class="m-sub">از راه‌اندازی</div></div>
    <div class="metric v-metric"><div class="m-ring r3"><i class="ti ti-link"></i></div><div class="m-label">کانفیگ فعال</div><div class="m-val" id="m-alinks">—</div><div class="m-sub" id="m-lsub">از کل</div></div>
    <div class="metric v-metric"><div class="m-ring r4"><i class="ti ti-folders"></i></div><div class="m-label">گروه‌های ساب</div><div class="m-val" id="m-subs">—</div><div class="m-sub">فعال</div></div>
  </div>
  <div class="vless-box">
    <div class="vl-header">
      <div class="vl-title"><i class="ti ti-link"></i> لینک پیش‌فرض (بدون محدودیت)</div>
      <span class="badge bg-blue"><span class="dot db"></span> TLS 443 · WS</span>
    </div>
    <div class="vl-code" id="vless-main">در حال دریافت...</div>
    <div class="vl-actions">
      <button class="btn btn-p" onclick="cpText('vless-main')"><i class="ti ti-copy"></i> کپی</button>
      <button class="btn btn-g" onclick="qrFor('vless-main')"><i class="ti ti-qrcode"></i> QR</button>
      <button class="btn btn-o" onclick="navTo('links')"><i class="ti ti-link-plus"></i> کانفیگ محدود</button>
      <button class="btn btn-pur" onclick="navTo('subgroups')"><i class="ti ti-folders"></i> گروه‌های ساب</button>
    </div>
  </div>
  <div class="g3">
    <div class="card"><div class="card-title"><i class="ti ti-chart-area"></i> ترافیک ساعتی (MB)</div><div class="ch"><canvas id="ch1"></canvas></div></div>
    <div class="card"><div class="card-title"><i class="ti ti-chart-bar"></i> توزیع پروتکل‌ها</div><div class="ch-sm" style="min-height:190px"><canvas id="ch2"></canvas></div></div>
  </div>
  <div class="g2" style="grid-template-columns:1fr">
    <div class="card">
      <div class="card-title"><i class="ti ti-heartbeat"></i> وضعیت سرویس</div>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px" id="sr-grid">
        <div class="sr-tile">
          <div class="sr-tile-ico" style="color:#34D399;background:rgba(52,211,153,.12)"><i class="ti ti-shield-check"></i></div>
          <div class="sr-tile-name">UUID Auth</div>
          <div class="sr-tile-val">ماژول فعال‌سازی هویت</div>
        </div>
        <div class="sr-tile">
          <div class="sr-tile-ico" style="color:#10B981;background:rgba(16,185,129,.12)"><i class="ti ti-circle-check"></i></div>
          <div class="sr-tile-name">VLESS / WS Tunnel</div>
          <div class="sr-tile-val">مسیر WebSocket در برنامه</div>
        </div>
        <div class="sr-tile">
          <div class="sr-tile-ico" style="color:#6EE7B7;background:rgba(110,231,183,.12)"><i class="ti ti-bolt"></i></div>
          <div class="sr-tile-name">Siz10a XHTTP Ultra</div>
          <div class="sr-tile-val">سه حالت انتقال پشتیبانی‌شده</div>
        </div>
        <div class="sr-tile">
          <div class="sr-tile-ico" style="color:#0D9488;background:rgba(13,148,136,.14)"><i class="ti ti-folders"></i></div>
          <div class="sr-tile-name">Sub Groups</div>
          <div class="sr-tile-val">مدیریت گروه اشتراک</div>
        </div>
        <div class="sr-tile">
          <div class="sr-tile-ico" style="color:#34D399;background:rgba(52,211,153,.12)"><i class="ti ti-rss"></i></div>
          <div class="sr-tile-name">Subscription API</div>
          <div class="sr-tile-val">API اشتراک در دسترس</div>
        </div>
        <div class="sr-tile">
          <div class="sr-tile-ico" style="color:#6EE7B7;background:rgba(110,231,183,.12)"><i class="ti ti-clock"></i></div>
          <div class="sr-tile-name">آپتایم</div>
          <div class="sr-tile-val" id="uptime-inline" style="direction:ltr">—</div>
        </div>
      </div>
      <div style="margin-top:16px;padding-top:14px;border-top:1px solid var(--card-b)">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
          <span style="font-size:12px;font-weight:700;color:var(--t2)"><i class="ti ti-gauge"></i> بار نسبی</span>
          <span class="sr-v" id="bw-pct">—%</span>
        </div>
        <div class="spbar" style="width:100%;height:8px"><div class="spfill" id="bw-bar" style="width:0%"></div></div>
      </div>
    </div>
  </div>
  <div class="brand-contact">
    <div class="brand-contact-identity">
      <img class="brand-contact-logo" src="https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png" alt="𝑭𝒊𝒏𝒆𝑽𝑷𝑵 logo" onerror="this.remove()">
      <div><div class="brand-contact-title">𝑭𝒊𝒏𝒆𝑽𝑷𝑵</div><div class="brand-contact-provider">ارائه‌دهنده: مـحـمـدصـادق افـغـان</div><div class="brand-contact-signature">𝑀𝑢ℎ𝑎𝑚𝑚𝑎𝑑𝒔𝒂𝒅𝒊𝒒</div></div>
    </div>
    <div class="brand-contact-links">
      <a class="fine-tg-link" href="https://t.me/sadiq_AFG1" target="_blank" rel="noopener noreferrer"><i class="ti ti-brand-telegram"></i><span>پشتیبانی <b>@sadiq_AFG1</b></span></a>
    </div>
  </div>
</section>
<section class="pg" id="pg-links">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-link-plus"></i> کانفیگ‌ها</div><div class="tb-sub">ساخت و مدیریت کانفیگ با سهمیه، انقضا و گروه‌بندی</div></div>
    <div class="tb-right">
      <select class="cp-input-full fs cat-filter" id="cat-filter" onchange="loadLinks()"><option value="">همه دسته‌ها</option></select>
      <span class="badge bg-blue" id="links-pg-cnt">۰ کانفیگ</span></div>
  </div>
  <div class="create-panel">
    <div class="cp-head">
      <div class="cp-head-icon"><i class="ti ti-square-rounded-plus"></i></div>
      <div class="cp-head-text">
        <div class="cp-head-title">ساخت کانفیگ جدید</div>
        <div class="cp-head-sub">UUID تصادفی · سهمیه، انقضا و پروتکل رو انتخاب کن</div>
      </div>
    </div>
    <div class="cp-body">
      <div class="cp-row">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-id-badge-2"></i> شناسه کانفیگ</div>
          <input class="cp-input-full" id="nl-label" placeholder="مثلاً: کاربر علی">
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-note" placeholder="یادداشت (اختیاری)">
          </div>
          <div class="cp-mini-row">
            <select class="cp-input-full fs" id="nl-cat"><option value="">— بدون دسته —</option></select>
          </div>
        </div>
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-folders"></i> گروه ساب و انقضا</div>
          <select class="cp-input-full fs" id="nl-sub"><option value="">— بدون گروه —</option></select>
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-exp" type="number" min="0" step="1" placeholder="انقضا (روز) · 0 = نامحدود">
          </div>
          <div class="chip-row" id="exp-chips">
            <span class="chip" onclick="setExpiry(0,this)">نامحدود</span>
            <span class="chip" onclick="setExpiry(7,this)">۷ روز</span>
            <span class="chip active" onclick="setExpiry(30,this)">۳۰ روز</span>
            <span class="chip" onclick="setExpiry(90,this)">۹۰ روز</span>
          </div>
        </div>
      </div>
      <div class="cp-block mb16">
        <div class="cp-block-label"><i class="ti ti-gauge"></i> سهمیه ترافیک</div>
        <div class="cp-quota-inputs">
          <input class="cp-input-full" id="nl-val" type="number" min="0" step="0.1" placeholder="0 = نامحدود">
          <select class="cp-input-full fs" id="nl-unit"><option value="GB">GB</option><option value="MB" selected>MB</option></select>
        </div>
        <div class="chip-row" id="quota-chips">
          <span class="chip" onclick="setQuota(0,'GB',this)">نامحدود</span>
          <span class="chip" onclick="setQuota(500,'MB',this)">۵۰۰ MB</span>
          <span class="chip active" onclick="setQuota(1,'GB',this)">۱ GB</span>
          <span class="chip" onclick="setQuota(5,'GB',this)">۵ GB</span>
          <span class="chip" onclick="setQuota(10,'GB',this)">۱۰ GB</span>
          <span class="chip" onclick="setQuota(50,'GB',this)">۵۰ GB</span>
        </div>
      </div>
      <div class="cp-block mb16">
        <div class="cp-block-label"><i class="ti ti-plug-connected"></i> پروتکل انتقال</div>
        <select id="nl-proto" style="display:none">
          <option value="vless-ws">VLESS / WebSocket</option>
          <option value="xhttp-packet-up">XHTTP Ultra · packet-up</option>
          <option value="xhttp-stream-up">XHTTP Ultra · stream-up</option>
        </select>
        <div class="proto-cards">
          <div class="proto-card active" data-val="vless-ws" onclick="selectProto('vless-ws',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-link"></i></div>
            <div class="proto-card-title">VLESS / WS</div>
            <div class="proto-card-desc">پایدار و همه‌منظوره</div>
          </div>
          <div class="proto-card" data-val="xhttp-packet-up" onclick="selectProto('xhttp-packet-up',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-bolt"></i></div>
            <div class="proto-card-title">XHTTP · packet-up</div>
            <div class="proto-card-desc">سازگار با CDN</div>
          </div>
          <div class="proto-card" data-val="xhttp-stream-up" onclick="selectProto('xhttp-stream-up',this)">
            <div class="proto-card-check"><i class="ti ti-check"></i></div>
            <div class="proto-card-icon"><i class="ti ti-rocket"></i></div>
            <div class="proto-card-title">XHTTP · stream-up</div>
            <div class="proto-card-desc">تاخیر پایین‌تر</div>
          </div>
        </div>
      </div>
      <div class="cp-row">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-fingerprint"></i> Fingerprint (uTLS)</div>
          <select class="cp-input-full fs" id="nl-fp">
            <option value="chrome" selected>chrome</option>
            <option value="firefox">firefox</option>
            <option value="safari">safari</option>
            <option value="ios">ios</option>
            <option value="android">android</option>
            <option value="edge">edge</option>
            <option value="360">360</option>
            <option value="qq">qq</option>
            <option value="random">random</option>
            <option value="randomized">randomized</option>
          </select>
        </div>
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-antenna-bars-5"></i> ALPN</div>
          <select class="cp-input-full fs" id="nl-alpn-preset" onchange="onAlpnPresetChange()">
            <option value="">پیش‌فرض پروتکل</option>
            <option value="h2,http/1.1">h2,http/1.1</option>
            <option value="http/1.1">http/1.1</option>
            <option value="h2">h2</option>
            <option value="__custom__">دستی...</option>
          </select>
          <div class="cp-mini-row">
            <input class="cp-input-full" id="nl-alpn" placeholder="مقدار دستی ALPN" style="display:none">
          </div>
        </div>
      </div>
      <div class="cp-row mb16">
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-route"></i> پورت اتصال</div>
          <input class="cp-input-full" id="nl-port" type="number" min="1" max="65535" placeholder="443" value="443">
        </div>
        <div class="cp-block">
          <div class="cp-block-label"><i class="ti ti-users"></i> محدودیت آی‌پی / کاربر هم‌زمان</div>
          <input class="cp-input-full" id="nl-iplimit" type="number" min="0" step="1" placeholder="0 = نامحدود" value="0">
          <div class="chip-row" id="iplimit-chips">
            <span class="chip active" onclick="setIpLimit(0,this)">نامحدود</span>
            <span class="chip" onclick="setIpLimit(1,this)">۱ کاربر</span>
            <span class="chip" onclick="setIpLimit(2,this)">۲ کاربر</span>
            <span class="chip" onclick="setIpLimit(5,this)">۵ کاربر</span>
          </div>
        </div>
      </div>
      <div class="cp-row mb16">
        <div class="cp-block" style="flex:1">
          <div class="cp-block-label"><i class="ti ti-gauge"></i> محدودیت سرعت</div>
          <div class="form-row">
            <input class="cp-input-full" id="nl-speed" type="number" min="0" step="0.5" placeholder="0 = نامحدود" value="0" style="flex:1">
            <select class="fs" id="nl-speed-unit" style="flex:0 0 100px">
              <option value="MBIT" selected>Mbps</option>
              <option value="KB">KB/s</option>
              <option value="MB">MB/s</option>
            </select>
          </div>
          <div class="chip-row" id="speed-chips">
            <span class="chip active" onclick="setSpeedLimit(0,this)">نامحدود</span>
            <span class="chip" onclick="setSpeedLimit(1,this)">۱ Mbps</span>
            <span class="chip" onclick="setSpeedLimit(5,this)">۵ Mbps</span>
            <span class="chip" onclick="setSpeedLimit(10,this)">۱۰ Mbps</span>
            <span class="chip" onclick="setSpeedLimit(25,this)">۲۵ Mbps</span>
          </div>
        </div>
      </div>
      <div class="cp-footer">
        <div class="cp-footer-note"><i class="ti ti-info-circle"></i> UUID کاملاً رندوم تولید می‌شود · فقط UUID‌های ثبت‌شده اجازه اتصال دارند · پروتکل پس از ساخت قابل تغییر نیست.</div>
        <button class="cp-submit-btn" onclick="createLink()"><i class="ti ti-link-plus"></i> ساخت کانفیگ</button>
      </div>
    </div>
  </div>
  <div class="bulk-toolbar" style="display:flex;gap:8px;align-items:center;flex-wrap:wrap;padding:12px 14px;margin:12px 0;border:1px solid var(--border);border-radius:14px;background:rgba(255,255,255,.025)">
    <label style="display:flex;align-items:center;gap:7px;font-size:12px"><input type="checkbox" id="bulk-select-all" onchange="selectAllConfigs(this.checked)"> انتخاب همه</label>
    <span id="bulk-selected-count" style="font-size:11px;color:var(--t3);margin-inline-end:auto">۰ انتخاب</span>
    <button class="btn btn-sm btn-g" onclick="bulkConfigAction('activate')"><i class="ti ti-check"></i> فعال‌سازی</button>
    <button class="btn btn-sm btn-g" onclick="bulkConfigAction('deactivate')"><i class="ti ti-ban"></i> غیرفعال‌سازی</button>
    <button class="btn btn-sm btn-g" onclick="bulkConfigAction('reset_usage')"><i class="ti ti-rotate"></i> ریست مصرف</button>
    <button class="btn btn-sm btn-d" onclick="bulkConfigAction('delete')"><i class="ti ti-trash"></i> حذف انتخاب‌شده‌ها</button>
  </div>
  <div class="cfg-grid" id="links-grid"></div>
  <div class="empty" id="links-empty" style="display:none"><i class="ti ti-link-off"></i><p>هنوز کانفیگی وجود ندارد</p></div>
</section>
<section class="pg" id="pg-subgroups">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-folders"></i> گروه‌های ساب</div><div class="tb-sub">هر گروه یک صفحه پابلیک مجزا با کانفیگ‌های خودش دارد</div></div>
    <div class="tb-right">
      <span class="badge bg-purple" id="subs-pg-cnt">۰ گروه</span>
      <button class="btn btn-pur" onclick="openModal('modal-create-sub')"><i class="ti ti-folder-plus"></i> گروه جدید</button>
    </div>
  </div>
  <div class="subs-toolbar">
    <div class="subs-search">
      <i class="ti ti-search"></i>
      <input type="text" id="subs-search-inp" placeholder="جستجو در گروه‌ها..." oninput="filterSubs(this.value)">
    </div>
  </div>
  <div class="sub-grid" id="subs-grid">
    <div class="subs-empty-v2"><div class="subs-empty-v2-icon"><i class="ti ti-folders"></i></div><div class="subs-empty-v2-title">هنوز گروهی وجود ندارد</div><div class="subs-empty-v2-sub">یک گروه جدید بسازید تا کانفیگ‌ها را دسته‌بندی کنید</div></div>
  </div>
</section>
<section class="pg" id="pg-subscriptions">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-rss"></i> سابسکریپشن</div><div class="tb-sub">لینک‌های اشتراک برای اپ‌های v2ray</div></div></div>
  <div class="sec-hero">
    <div class="sec-hero-tile"><div class="sec-hero-ico"><i class="ti ti-rss"></i></div><div class="sec-hero-label">سابسکریپشن‌های فعال</div><div class="sec-hero-val" id="sb-count">—</div><div class="sec-hero-sub">گروه‌های دارای لینک ساب</div></div>
    <div class="sec-hero-tile"><div class="sec-hero-ico pur"><i class="ti ti-link"></i></div><div class="sec-hero-label">کل کانفیگ‌ها</div><div class="sec-hero-val" id="sb-links">—</div><div class="sec-hero-sub">قابل اشتراک‌گذاری</div></div>
    <div class="sec-hero-tile"><div class="sec-hero-ico amb"><i class="ti ti-devices"></i></div><div class="sec-hero-label">اپ‌های پشتیبانی‌شده</div><div class="sec-hero-val" style="font-size:15px">v2rayNG · Streisand</div><div class="sec-hero-sub">و سایر کلاینت‌های VLESS</div></div>
  </div>
  <div class="g2">
    <div class="sec-panel">
      <div class="sec-panel-head"><div class="sec-panel-ico"><i class="ti ti-rss"></i></div><div><div class="sec-panel-title">سابسکریپشن تکی</div><div class="sec-panel-sub">هر کانفیگ URL سابسکریپشن مخصوص دارد</div></div></div>
      <div class="sec-panel-body"><p style="font-size:11.5px;color:var(--t3);line-height:1.9">از کارت کانفیگ روی آیکون <i class="ti ti-rss" style="color:var(--accent)"></i> کلیک کنید تا URL سابسکریپشن اون کانفیگ کپی شه.</p></div>
    </div>
    <div class="sec-panel">
      <div class="sec-panel-head"><div class="sec-panel-ico pur"><i class="ti ti-database"></i></div><div><div class="sec-panel-title">سابسکریپشن کامل (ادمین)</div><div class="sec-panel-sub">شامل تمام کانفیگ‌های فعال</div></div></div>
      <div class="sec-panel-body">
        <div class="sub-box"><span class="sub-url" id="sub-all-url">در حال دریافت...</span><div style="display:flex;gap:6px"><button class="btn btn-sm btn-g" onclick="cpSubAll()"><i class="ti ti-copy"></i></button><button class="btn btn-sm btn-g" onclick="window.open(location.protocol+'//'+location.host+'/sub-all')"><i class="ti ti-external-link"></i></button></div></div>
        <div class="cl amber" style="margin-top:11px"><i class="ti ti-alert-triangle"></i><span>این آدرس فقط در مرورگری که به پنل وارد شده کار می‌کند (نیاز به کوکی سشن).</span></div>
      </div>
    </div>
  </div>
  <div class="sec-panel">
    <div class="sec-panel-head"><div class="sec-panel-ico amb"><i class="ti ti-folders"></i></div><div><div class="sec-panel-title">لینک سابسکریپشن گروه‌ها</div><div class="sec-panel-sub">هر گروه یک صفحه پابلیک مجزا</div></div></div>
    <div class="sec-panel-body"><div id="sub-groups-list">در حال بارگذاری...</div></div>
  </div>
</section>
<section class="pg" id="pg-traffic">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-chart-area"></i> ترافیک</div><div class="tb-sub">تحلیل و مانیتورینگ مصرف پهنای باند</div></div>
    <div class="tb-right"><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button></div>
  </div>

  <div class="traf-hero">
    <div class="traf-main-stat">
      <div class="traf-main-label"><i class="ti ti-database"></i> کل ترافیک مصرفی</div>
      <div class="traf-main-val" id="t-traffic">—<span>MB</span></div>
      <div class="traf-trend up" id="t-trend"><i class="ti ti-trending-up"></i> <span id="t-trend-val">—</span></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon"><i class="ti ti-arrow-up-right"></i></div><span class="traf-mini-label">میانگین ساعتی</span></div>
      <div><div class="traf-mini-val" id="t-avg">—</div><div class="traf-mini-sub">MB در ساعت</div></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon pk"><i class="ti ti-chart-bar"></i></div><span class="traf-mini-label">پیک مصرف</span></div>
      <div><div class="traf-mini-val" id="t-peak">—</div><div class="traf-mini-sub" id="t-peak-time">بالاترین ساعت</div></div>
    </div>
    <div class="traf-mini">
      <div class="traf-mini-top"><div class="traf-mini-icon lo"><i class="ti ti-clock-hour-4"></i></div><span class="traf-mini-label">کمترین مصرف</span></div>
      <div><div class="traf-mini-val" id="t-low">—</div><div class="traf-mini-sub">MB در ساعت</div></div>
    </div>
  </div>

  <div class="traf-chart-card">
    <div class="traf-chart-head">
      <div>
        <div class="traf-chart-title"><i class="ti ti-activity"></i> روند مصرف ترافیک</div>
        <div class="traf-chart-sub">بر اساس مگابایت در هر ساعت</div>
      </div>
      <div class="traf-legend">
        <div class="traf-legend-item"><span class="traf-legend-dot" style="background:var(--accent)"></span> مصرف</div>
        <div class="traf-legend-item"><span class="traf-legend-dot" style="background:var(--amber)"></span> میانگین</div>
      </div>
    </div>
    <div class="traf-chart-body"><canvas id="ch3"></canvas></div>
  </div>
</section>
<section class="pg" id="pg-connections">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-plug-connected"></i> اتصالات فعال</div><div class="tb-sub">مانیتورینگ زنده‌ی آی‌پی و ترافیک هر اتصال</div></div>
    <div class="tb-right"><span class="badge bg-green" id="conns-live">—</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button></div>
  </div>

  <div class="conn-hero">
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-plug-connected"></i></div>
      <div class="conn-hero-label">اتصالات زنده</div>
      <div class="conn-hero-val" id="ch-count">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-transfer"></i></div>
      <div class="conn-hero-label">مجموع ترافیک لحظه‌ای</div>
      <div class="conn-hero-val" id="ch-traffic">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-clock"></i></div>
      <div class="conn-hero-label">میانگین مدت اتصال</div>
      <div class="conn-hero-val" id="ch-avgdur">—</div>
    </div>
    <div class="conn-hero-tile">
      <div class="conn-hero-icon"><i class="ti ti-map-pin"></i></div>
      <div class="conn-hero-label">آی‌پی‌های یکتا</div>
      <div class="conn-hero-val" id="ch-uniq">—</div>
    </div>
  </div>

  <div class="conn-toolbar">
    <div class="conn-toolbar-title"><i class="ti ti-list-details"></i> لیست اتصالات</div>
    <div class="conn-live-badge"><span class="conn-live-dot"></span> بروزرسانی خودکار هر ۵ ثانیه</div>
  </div>

  <div class="conn-grid-v2" id="conns-grid"></div>
  <div class="conn-empty-v2" id="conns-empty" style="display:none">
    <div class="conn-empty-v2-icon"><i class="ti ti-plug-off"></i></div>
    <div class="conn-empty-v2-title">هیچ اتصال فعالی نیست</div>
    <div class="conn-empty-v2-sub">به محض اتصال کلاینت‌ها، اینجا نمایش داده می‌شوند</div>
  </div>
</section>

<section class="pg" id="pg-logs">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-history"></i> فعالیت ساب‌ها</div><div class="tb-sub">کارتی ساب‌ها + اتصال زنده IP → کانفیگ + لاگ کامل</div></div><div class="tb-right"><button class="btn btn-p btn-sm" onclick="loadActivity()"><i class="ti ti-refresh"></i> رفرش</button></div></div>

  <!-- Sub cards -->
  <div id="act-subs" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px;margin-bottom:20px"></div>

  <!-- Live connections -->
  <div class="card" style="margin-bottom:20px">
    <div class="card-title"><span class="m-ring" style="width:34px;height:34px;font-size:15px"><i class="ti ti-plug-connected"></i></span> اتصال‌های زنده <span class="ml-auto badge bg-green" id="act-conns-badge">۰</span></div>
    <div id="act-conns"></div>
    <div class="empty" id="act-conns-empty" style="display:none"><i class="ti ti-plug-connected"></i><p>الان اتصال فعالی وجود ندارد</p></div>
  </div>

  <!-- Full activity log -->
  <div class="card">
    <div class="card-title"><span class="m-ring r3" style="width:34px;height:34px;font-size:15px"><i class="ti ti-history"></i></span> لاگ کامل فعالیت</div>
    <div style="display:flex;gap:8px;margin-bottom:12px;flex-wrap:wrap">
      <input id="log-search" oninput="loadActivity()" placeholder="🔍 جستجو در لاگ..." style="flex:1;min-width:150px;background:var(--card-b);border:1px solid var(--card-b);border-radius:9px;padding:8px 11px;color:var(--t1);font-size:11.5px;outline:none">
      <select id="log-kind" onchange="loadActivity()" style="background:var(--card-b);border:1px solid var(--card-b);border-radius:9px;padding:8px 11px;color:var(--t1);font-size:11.5px;outline:none">
        <option value="">همه نوعها</option><option value="link">کانفیگ</option><option value="sub">گروه</option><option value="auth">ورود</option><option value="connection">اتصال</option><option value="system">سیستم</option>
      </select>
    </div>
    <div class="log-timeline" id="logs-list">—</div>
    <div class="empty" id="logs-empty" style="display:none"><i class="ti ti-history-toggle"></i><p>هنوز لاگی ثبت نشده</p></div>
  </div>
</section>
<section class="pg" id="pg-errors">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-alert-triangle"></i> خطاها</div><div class="tb-sub">خطاهای ثبت‌شده‌ی سیستم</div></div><div class="tb-right"><span class="badge bg-red" id="errs-badge">۰</span><button class="btn btn-p btn-sm" onclick="refreshAll()"><i class="ti ti-refresh"></i> رفرش</button></div></div>
  <div class="sec-hero">
    <div class="sec-hero-tile"><div class="sec-hero-ico red"><i class="ti ti-bug"></i></div><div class="sec-hero-label">تعداد خطاها</div><div class="sec-hero-val" id="er-count">—</div><div class="sec-hero-sub">از زمان راه‌اندازی</div></div>
    <div class="sec-hero-tile"><div class="sec-hero-ico amb"><i class="ti ti-alert-triangle"></i></div><div class="sec-hero-label">آخرین خطا</div><div class="sec-hero-val" id="er-last" style="font-size:14px">—</div><div class="sec-hero-sub" id="er-last-time">—</div></div>
    <div class="sec-hero-tile"><div class="sec-hero-ico"><i class="ti ti-shield-check"></i></div><div class="sec-hero-label">وضعیت سیستم</div><div class="sec-hero-val" style="font-size:15px;color:var(--green-t)">سالم</div><div class="sec-hero-sub">همه سرویس‌ها فعال</div></div>
  </div>
  <div class="sec-panel">
    <div class="sec-panel-head"><div class="sec-panel-ico red"><i class="ti ti-bug"></i></div><div><div class="sec-panel-title">لاگ خطاها</div><div class="sec-panel-sub">خطاهای ثبت‌شده‌ی سیستم از زمان آخرین ریست</div></div></div>
    <div class="sec-panel-body"><div id="errs-full">—</div></div>
  </div>
</section>
<section class="pg" id="pg-testws">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-wifi"></i> تست WebSocket</div></div></div>
  <div class="sec-panel" style="max-width:760px">
    <div class="sec-panel-head"><div class="sec-panel-ico"><i class="ti ti-wifi"></i></div><div><div class="sec-panel-title">تست WebSocket</div><div class="sec-panel-sub">تست اتصال VLESS/WS روی UUID فعال</div></div></div>
    <div class="sec-panel-body">
      <div class="cl amber" style="margin-top:0;margin-bottom:14px"><i class="ti ti-alert-triangle"></i><span>فقط UUID‌های ثبت‌شده و فعال اتصال برقرار می‌کنند (این فقط تست VLESS/WS است؛ تست XHTTP از خود کلاینت انجام می‌شود).</span></div>
      <div class="form-row" style="margin-bottom:12px">
        <div class="fg" style="flex:1"><label>UUID (باید در کانفیگ‌ها وجود داشته باشد)</label><input class="fi" id="ws-uuid" placeholder="UUID یک کانفیگ فعال" style="width:100%"></div>
        <button class="btn btn-p" onclick="wsConn()"><i class="ti ti-plug-connected"></i> اتصال</button>
        <button class="btn btn-d" onclick="wsDisc()"><i class="ti ti-plug-x"></i> قطع</button>
      </div>
      <div class="form-row" style="margin-bottom:14px">
        <input class="fi" id="ws-msg" placeholder="پیام تست..." style="flex:1">
        <button class="btn btn-o" onclick="wsSend()"><i class="ti ti-send"></i> ارسال</button>
      </div>
      <div class="sec-log-box" id="ws-log"><p>منتظر اتصال...</p></div>
    </div>
  </div>
</section>
<section class="pg" id="pg-categories">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-category"></i> دسته‌بندی کانفیگ‌ها</div><div class="tb-sub">کانفیگ‌ها را به دسته‌های منطقی تقسیم کنید</div></div>
    <div class="tb-right"><span class="badge bg-purple" id="cats-pg-cnt">۰ دسته</span></div>
  </div>
  <div class="sec-panel">
    <div class="sec-panel-head"><div class="sec-panel-ico amb"><i class="ti ti-plus"></i></div><div><div class="sec-panel-title">ساخت دسته جدید</div><div class="sec-panel-sub">نام و رنگ دسته را انتخاب کنید</div></div></div>
    <div class="sec-panel-body">
      <div class="cat-mgr-row" style="margin-bottom:12px">
        <input class="fi" id="cat-new-name" placeholder="نام دسته جدید (مثلاً: VIP)" style="flex:1">
        <input class="fi" id="cat-new-color" type="color" value="#10B981" style="width:46px;height:38px;padding:4px;border-radius:9px">
        <button class="btn btn-p" onclick="createCat()"><i class="ti ti-plus"></i> ساخت</button>
      </div>
    </div>
  </div>
  <div class="sec-panel">
    <div class="sec-panel-head"><div class="sec-panel-ico"><i class="ti ti-category"></i></div><div><div class="sec-panel-title">دسته‌های ساخته‌شده</div><div class="sec-panel-sub">هر دسته تعداد کانفیگ‌های متعلق به خود را نشان می‌دهد</div></div><div class="sec-panel-side"><button class="btn btn-p btn-sm" onclick="loadCats()"><i class="ti ti-refresh"></i> رفرش</button></div></div>
    <div class="sec-panel-body">
      <div class="cat-mgr" id="cat-list">در حال بارگذاری...</div>
    </div>
  </div>
</section>
<section class="pg" id="pg-settings">
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-settings"></i> تنظیمات</div><div class="tb-sub">پیکربندی پنل و اطلاعات سرور</div></div></div>
  <div class="sec-hero">
    <div class="sec-hero-tile"><div class="sec-hero-ico"><i class="ti ti-server"></i></div><div class="sec-hero-label">نسخه پنل</div><div class="sec-hero-val" style="font-size:16px">𝑭𝒊𝒏𝒆𝑽𝑷𝑵 v1.0.0</div><div class="sec-hero-sub">ساختار ۲۴ کانفیگ پرفورمنت</div></div>
    <div class="sec-hero-tile"><div class="sec-hero-ico pur"><i class="ti ti-clock-hour-4"></i></div><div class="sec-hero-label">آپتایم سرور</div><div class="sec-hero-val" id="st-uptime" style="font-size:16px">—</div><div class="sec-hero-sub">از آخرین ریست</div></div>
    <div class="sec-hero-tile"><div class="sec-hero-ico amb"><i class="ti ti-world"></i></div><div class="sec-hero-label">هاست پابلیک</div><div class="sec-hero-val" id="server-public-host" style="font-size:13px;overflow-wrap:anywhere">—</div><div class="sec-hero-sub">لینک‌های ساب از اینجا</div></div>
  </div>
  <div class="sec-panel">
    <div class="sec-panel-head"><div class="sec-panel-ico"><i class="ti ti-server"></i></div><div><div class="sec-panel-title">اطلاعات سرور</div><div class="sec-panel-sub">مشخصات زیرساخت فعال</div></div></div>
    <div class="sec-panel-body" id="set-server">در حال بارگذاری...</div>
  </div>
  <div class="sec-panel">
    <div class="sec-panel-head"><div class="sec-panel-ico amb"><i class="ti ti-database"></i></div><div><div class="sec-panel-title">ذخیره‌سازی و ماندگاری داده</div><div class="sec-panel-sub">کانفیگ‌ها، ساب‌ها و مصرف حجم بعد از دیپلوی حفظ می‌شوند؟</div></div></div>
    <div class="sec-panel-body" id="set-volume"></div>
  </div>
  <div class="sec-panel">
    <div class="sec-panel-head"><div class="sec-panel-ico pur"><i class="ti ti-user-circle"></i></div><div><div class="sec-panel-title">تغییر نام کاربری و رمز عبور</div><div class="sec-panel-sub">مدیریت دسترسی پنل</div></div></div>
    <div class="sec-panel-body">
      <div class="form-row" style="margin-top:0">
        <div class="fg" style="flex:1"><label><i class="ti ti-user"></i> نام کاربری جدید</label><input class="fi" id="cred-username-v2" placeholder="نام کاربری فعلی را نگه دارید" style="width:100%"></div>
      </div>
      <div class="form-row" style="margin-top:12px">
        <div class="fg" style="flex:1"><label><i class="ti ti-lock"></i> رمز فعلی</label><input class="fi" id="cred-current-v2" type="password" placeholder="رمز فعلی" style="width:100%"></div>
        <div class="fg" style="flex:1"><label><i class="ti ti-key"></i> رمز جدید</label><input class="fi" id="cred-new-v2" type="password" placeholder="خالی = بدون تغییر" style="width:100%"></div>
      </div>
      <div class="form-row" style="margin-top:14px;align-items:center">
        <button class="btn btn-p" onclick="saveCredentialsV2()"><i class="ti ti-device-floppy"></i> ذخیره تغییرات</button>
        <span id="cred-status-v2" style="font-size:11px;color:var(--t3)"></span>
      </div>
    </div>
  </div>
  <div class="sec-panel">
    <div class="sec-panel-head"><div class="sec-panel-ico amb"><i class="ti ti-database-export"></i></div><div><div class="sec-panel-title">پشتیبان‌گیری و بازیابی</div><div class="sec-panel-sub">بکاپ کامل کانفیگ‌ها و ساب‌ها</div></div></div>
    <div class="sec-panel-body">
      <div class="cl" style="margin-top:0"><i class="ti ti-info-circle"></i><span>فایل بکاپ شامل کانفیگ‌ها، گروه‌ها، حجم مصرفی و تنظیمات است. برای حفظ اطلاعات پس از استقرار مجدد، ذخیره‌سازی پایدار را فعال کنید و پشتیبان را جداگانه نگه دارید.</span></div>
      <div class="form-row" style="margin-top:14px;flex-wrap:wrap">
        <button class="btn btn-p" onclick="downloadBackupV2()"><i class="ti ti-download"></i> دانلود بکاپ</button>
        <button class="btn btn-o" onclick="document.getElementById('restore-file-v2').click()"><i class="ti ti-upload"></i> بارگذاری بکاپ</button>
        <input type="file" id="restore-file-v2" accept=".json" style="display:none" onchange="restoreBackupV2(this)">
        <span id="backup-status-v2" style="font-size:11px;color:var(--t3);align-self:center"></span>
      </div>
    </div>
  </div>
  <div class="sec-panel">
    <div class="sec-panel-head"><div class="sec-panel-ico red"><i class="ti ti-shield-lock"></i></div><div><div class="sec-panel-title">امنیت و نشست‌ها</div><div class="sec-panel-sub">مدیریت دستگاه‌های واردشده به پنل</div></div></div>
    <div class="sec-panel-body">
      <div class="log-timeline" id="sess-list">در حال بارگذاری...</div>
      <div style="margin-top:12px;display:flex;gap:8px;flex-wrap:wrap">
        <button class="btn btn-d btn-sm" onclick="revokeSessions()"><i class="ti ti-logout"></i> خروج از سایر دستگاه‌ها</button>
      </div>
    </div>
  </div>
  <div class="sec-panel">
    <div class="sec-panel-head"><div class="sec-panel-ico pur"><i class="ti ti-activity-heartbeat"></i></div><div><div class="sec-panel-title">منابع سرور</div><div class="sec-panel-sub">CPU، RAM و شبکه‌ی همین سرویس</div></div><div class="sec-panel-side"><span class="badge bg-warn" id="tel-live">در انتظار داده</span></div></div>
    <div class="sec-panel-body">
      <div class="tel-grid" id="tel-grid">در حال بارگذاری...</div>
    </div>
  </div>
</section>


</main>
<script>
let currentLang='fa';try{currentLang=localStorage.getItem('finevpn-lang')||'fa'}catch(e){}
const isDark=true;
function applyTheme(){document.documentElement.setAttribute('data-theme','dark');}
function toggleTheme(){applyTheme();}
applyTheme();
async function loadCats(){
  try{
    const d=await (await authF('/api/categories')).json();
    const el=document.getElementById('cat-list');if(!el)return;
    const cats=d.categories||[];
    const cc=document.getElementById('cats-pg-cnt');if(cc)cc.textContent=toFa(cats.length)+' دسته';
    if(!cats.length){el.innerHTML='<div class="empty"><i class="ti ti-category"></i><p>هنوز دسته‌ای ساخته نشده</p></div>';return}
    el.innerHTML='<div class="cat-mgr">'+cats.map(c=>`<div class="cat-mgr-row" style="padding:9px 12px;background:var(--card,#0d1c18);border:1px solid var(--line,rgba(255,255,255,.07));border-radius:11px">
      <span class="cat-dot" style="background:${esc(c.color||'#10B981')};width:9px;height:9px;flex:0 0 9px"></span>
      <b style="font-size:12.5px">${esc(c.name)}</b>
      <span class="badge bg-blue" style="font-size:10px">${toFa(c.links_count||0)} کانفیگ</span>
      <button class="btn btn-d btn-sm cat-del" onclick="delCat('${esc(c.id)}')"><i class="ti ti-trash"></i></button>
    </div>`).join('')+'</div>';
  }catch(e){}
}
async function createCat(){
  const name=(document.getElementById('cat-new-name').value||'').trim();
  if(!name){toast('نام دسته الزامی است','err');return}
  const color=document.getElementById('cat-new-color').value;
  try{
    const r=await authF('/api/categories',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name,color})});
    if(!r.ok)throw 0;
    document.getElementById('cat-new-name').value='';
    toast('دسته ساخته شد ✓','ok');loadCats();
  }catch(e){toast('خطا در ساخت دسته','err')}
}
async function delCat(id){
  if(!confirm('حذف این دسته؟ کانفیگ‌ها به «عمومی» برمی‌گردند.'))return;
  try{
    const r=await authF('/api/categories/'+id,{method:'DELETE'});
    if(!r.ok)throw 0;
    toast('دسته حذف شد','ok');loadCats();loadLinks();
  }catch(e){toast('خطا در حذف','err')}
}
async function loadSessions(){
  try{
    const d=await (await authF('/api/sessions')).json();
    const el=document.getElementById('sess-list');if(!el)return;
    const ss=d.sessions||[];
    if(!ss.length){el.innerHTML='<div class="empty"><i class="ti ti-login"></i><p>نشست فعلی شما است</p></div>';return}
    el.innerHTML=ss.map(s=>{
      const lt=s.login_at?new Date(s.login_at*1000).toLocaleString('fa-IR',{dateStyle:'short',timeStyle:'short'}):'—';
      const dev=s.device||'نامشخص';
      const devIc=/iphone|ipad/.test(dev.toLowerCase())?'ti-device-mobile':/android/.test(dev.toLowerCase())?'ti-device-mobile':/windows/.test(dev.toLowerCase())?'ti-device-desktop':/mac/.test(dev.toLowerCase())?'ti-device-laptop':'ti-device-question';
      return `<div class="log-item"><div class="log-ic ${s.current?'ok':'warn'}"><i class="ti ${devIc}"></i></div>
        <div class="log-body" style="display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:6px">
          <span class="log-msg"><b>${esc(dev)}</b> <code style="opacity:.55;font-size:10px">${esc(s.token)}</code></span>
          <span style="display:flex;gap:10px;align-items:center;font-size:10.5px;color:var(--t3)">
            <span title="آی‌پی"><i class="ti ti-world" style="font-size:11px"></i> ${esc(s.ip||'نامشخص')}</span>
            <span title="زمان ورود"><i class="ti ti-login" style="font-size:11px"></i> ${esc(lt)}</span>
            <b style="font-size:11px;color:var(--t3)">${toFa(s.expires_in_hours)} ساعت</b>
          </span>
        </div></div>`;}).join('');
  }catch(e){}
}
async function revokeSessions(){
  if(!confirm('از همه‌ی دستگاه‌های دیگر خارج می‌شوید. ادامه؟'))return;
  try{
    const r=await authF('/api/security/revoke-other-sessions',{method:'POST'});
    const d=await r.json();
    toast((d.revoked||0)+' نشست لغو شد','ok');loadSessions();
  }catch(e){toast('خطا','err')}
}
let telTimer=null;
async function loadTelemetry(){
  const badge=document.getElementById('tel-live');
  try{
    const response=await authF('/api/telemetry');
    if(!response.ok)throw new Error('telemetry request failed');
    const d=await response.json();
    const el=document.getElementById('tel-grid');
    if(!el||!d.ok)throw new Error('telemetry data unavailable');
    if(badge){badge.className='badge bg-green';badge.innerHTML='<span class="dot dg"></span> داده تازه دریافت شد';}
    const cpuPct=Math.min(100,Math.max(0,d.cpu.host_pct||0));
    const memPct=d.mem.rss_mb&&d.mem.host_total_mb?Math.min(100,d.mem.rss_mb/d.mem.host_total_mb*100):0;
    el.innerHTML=[
      ['ti-cpu','پردازنده',d.cpu.host_pct+'%','روی '+toFa(d.cpu.cores)+' هسته · لود '+d.cpu.load_pct+'%',cpuPct],
      ['ti-memory','حافظه (این سرویس)',d.mem.rss_mb+' MB','از '+d.mem.host_total_mb+' MB کل سرور',memPct],
      ['ti-hard-drive','دیسک',d.disk.used_gb+' GB','از '+d.disk.total_gb+' GB · '+d.disk.free_pct+'% آزاد',100-d.disk.free_pct],
      ['ti-network','شبکه','↑ '+d.net.sent_mb+' MB','↓ '+d.net.recv_mb+' MB',null],
    ].map(t=>`<div class="tel-tile"><div class="tt-l"><i class="ti ${t[0]}"></i> ${t[1]}</div><div class="tt-v">${t[2]}</div><div class="tt-s">${t[3]}</div>${t[4]!==null?`<div class="tel-bar"><i style="width:${Math.min(100,t[4]).toFixed(0)}%"></i></div>`:''}</div>`).join('');
  }catch(e){
    if(badge){badge.className='badge bg-red';badge.textContent='داده در دسترس نیست';}
  }
}
function startTelemetry(){if(!telTimer)telTimer=setInterval(()=>{if(document.getElementById('pg-settings').classList.contains('on'))loadTelemetry()},3000)}

function toast(msg,type=''){
  const t=document.getElementById('toast');
  t.textContent=msg;t.className='toast show'+(type?' '+type:'');
  setTimeout(()=>t.classList.remove('show'),2400);
}
function fmtB(b){if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}
function toFa(n){return String(n).replace(/\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d])}
function esc(s){return String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function daysLeft(exp){if(!exp)return null;return Math.ceil((new Date(exp)-Date.now())/(864e5))}
function expChip(exp,expired){
  if(expired)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> منقضی</span>';
  if(!exp)return '<span class="exp-chip ec-inf"><i class="ti ti-infinity"></i> نامحدود</span>';
  const d=daysLeft(exp);
  if(d<=0)return '<span class="exp-chip ec-exp"><i class="ti ti-calendar-x"></i> منقضی</span>';
  if(d<=3)return `<span class="exp-chip ec-warn"><i class="ti ti-alert-triangle"></i> ${toFa(d)} روز مانده</span>`;
  return `<span class="exp-chip ec-ok"><i class="ti ti-calendar-check"></i> ${toFa(d)} روز مانده</span>`;
}
function protoBadge(p){
  const m={'vless-ws':['VLESS · WS','pc-ws'],'xhttp-packet-up':['XHTTP · packet-up','pc-xhttp'],'xhttp-stream-up':['XHTTP · stream-up','pc-xhttp']};
  const v=m[p]||m['vless-ws'];
  return `<span class="proto-chip ${v[1]}">${v[0]}</span>`;
}
const I18N={
'داشبورد':'Dashboard','کانفیگ‌ها':'Configurations','گروه‌های ساب':'Subscription Groups','سابسکریپشن':'Subscriptions','ترافیک':'Traffic','اتصالات':'Connections','امنیت':'Security','لاگ فعالیت‌ها':'Activity Logs','خطاها':'Errors','تست WebSocket':'WebSocket Test','تنظیمات':'Settings','پشتیبانی':'Support','ورود به داشبورد':'Sign in to dashboard','ورود به پنل':'Panel Sign In','ساخت کانفیگ جدید':'Create New Configuration','گروه‌های ساب':'Subscription Groups','پشتیبانی':'Support','تنظیمات سیستم':'System Settings','تغییر رمز عبور':'Change Password','ذخیره تغییرات':'Save Changes','ذخیره رمز جدید':'Save New Password','انصراف':'Cancel','ذخیره':'Save','بستن':'Close','رفرش':'Refresh','کپی':'Copy','دانلود Backup':'Download Backup','Export لینک‌ها':'Export Links','پشتیبانی مستقیم':'Direct Support','وب‌سایت رسمی':'Official Website','تلگرام':'Telegram','اینستاگرام':'Instagram','یوتیوب':'YouTube','توییتر / X':'Twitter / X','سازنده':'Creator','فعال':'Active','نامحدود':'Unlimited','در حال بارگذاری...':'Loading...','پیش‌فرض اولیه · Initial defaults':'Initial defaults','نام کاربری':'Username','رمز عبور · Password':'Password','کد امنیتی · Security code':'Security code','کد / code':'Code','در حال ورود...':'Signing in...','خروج':'Logout','پنل':'Panel','سیستم':'System','کانفیگ‌ها':'Configurations','گروه جدید':'New Group','ساخت کانفیگ':'Create Configuration','ساخت سریع گروه ساب (۲۴ کانفیگ)':'Quick Subscription Group (24 Configs)','ساخت خودکار گروه ساب، تنظیم حجم مشترک و تولید ۲۴ کانفیگ با یک کلیک':'Create a subscription group with shared quota and 24 configs in one click','گروه دسترسی':'Access Group','کپی همه‌ی کانفیگ‌ها':'Copy All Configurations','کپی همه':'Copy All','اتصالات زنده':'Live Connections','کل مصرف':'Total Usage','سهمیه و اعتبار گروه':'Group Quota and Validity','کانفیگ‌های فعال':'Active Configurations','ذخیره‌سازی و ماندگاری داده':'Storage and Data Persistence','پشتیبان‌گیری و بازیابی':'Backup and Restore','امنیت و نشست‌ها':'Security and Sessions','تغییر نام کاربری و رمز عبور':'Change Username and Password','دانلود بکاپ':'Download Backup','بارگذاری بکاپ':'Upload Backup','حذف':'Delete','فعال':'Active','غیرفعال':'Inactive','ساخت':'Create','هر گروه یک صفحه پابلیک مجزا با کانفیگ‌های خودش دارد':'Each group has its own public page and configurations','نام کانفیگ':'Configuration name','عنوان':'Title','نام گروه ساب':'Subscription group name','گروه‌های اشتراک':'Subscription groups','گروه اشتراک':'Subscription group','توضیحات':'Description','حجم':'Traffic quota','حجم مشترک':'Shared quota','مدت اعتبار':'Validity period','روز':'days','بدون محدودیت':'Unlimited','مصرف‌شده':'Used','باقی‌مانده':'Remaining','آمار':'Statistics','عملیات':'Actions','ذخیره':'Save','بازگشت':'Back','بستن':'Close','لغو':'Cancel','حذف گروه':'Delete group','حذف کانفیگ':'Delete configuration','تأیید':'Confirm','بله':'Yes','خیر':'No','در حال ذخیره...':'Saving...','خطا':'Error','موفقیت':'Success','اطلاعات ذخیره شد':'Information saved','کشور خروجی':'Exit-country label','پرچم کشور':'Country flag','انتخاب همه':'Select all','انتخاب‌شده':'Selected','حذف انتخاب‌شده‌ها':'Delete selected','فعال‌سازی':'Activate','غیرفعال‌سازی':'Deactivate','ریست مصرف':'Reset usage','تازه‌سازی':'Refresh','پشتیبانی @sadiq_AFG1':'Support @sadiq_AFG1'

,'مدیریت کانفیگ‌های':'Manage configurations','کانفیگ‌هایی که می‌خواهید در این گروه باشند را انتخاب کنید':'Choose the configurations to include in this group','انتخاب همه':'Select all','لغو همه':'Clear all','۰ انتخاب شده':'0 selected','تغییرات بلافاصله اعمال می‌شود':'Changes take effect immediately','ساخت گروه ساب':'Create subscription group','یک صفحه پابلیک مجزا با ۲۴ کانفیگ خودکار بسازید':'Create a separate public page with 24 automatically generated configurations','نام گروه':'Group name','توضیحات (اختیاری)':'Description (optional)','رمز صفحه پابلیک (اختیاری)':'Public page password (optional)','ساخت سریع ۲۴ کانفیگ':'Quick-create 24 configurations','۳ پروتکل × ۲ فینگرپرینت × ۴ ALPN = ۲۴ کانفیگ (VWS/XPU/XHS)':'3 protocols × 2 fingerprints × 4 ALPN options = 24 configurations','حجم مشترک کل (GB)':'Total shared quota (GB)','روزهای اعتبار':'Validity days','حداکثر کاربر هم‌زمان (IP Limit)':'Maximum simultaneous users (IP limit)','حجم مشترک بین تمام ۲۴ کانفیگ تقسیم می‌شود. هر کاربر از هر کانفیگی مصرف کند، از همین حجم کم می‌شود.':'The shared quota is used by all 24 configurations. Traffic from any configuration reduces this same quota.','ساخت گروه + ۲۴ کانفیگ':'Create group + 24 configurations','ویرایش کانفیگ':'Edit configuration','سهمیه (0 = نامحدود)':'Quota (0 = unlimited)','واحد':'Unit','انقضا (روز از الان، 0 = بدون تغییر/نامحدود)':'Expiry (days from now; 0 = unchanged/unlimited)','یادداشت':'Note','ALPN (خالی = پیش‌فرض)':'ALPN (blank = default)','پورت اتصال':'Connection port','محدودیت آی‌پی (0 = نامحدود)':'IP limit (0 = unlimited)','محدودیت سرعت (0 = نامحدود)':'Speed limit (0 = unlimited)','برای حفظ انقضای فعلی، فیلد انقضا را صفر بگذارید.':'Set expiry to 0 to keep the current expiry.','ساخت خودکار گروه ساب، تنظیم حجم مشترک و تولید ۲۴ کانفیگ با یک کلیک':'Create a subscription group, set a shared quota, and generate 24 configurations in one click','نام گروه ساب':'Subscription group name','حجم مشترک (GB) —':'Shared quota (GB) —','۰ = نامحدود':'0 = unlimited','مدت اعتبار (روز) —':'Validity period (days) —','سقف کاربر (IP) —':'User limit (IP) —','ساخت گروه ساب + ۲۴ کانفیگ با حجم مشترک':'Create subscription group + 24 configurations with shared quota','گروه ساب و ۲۴ کانفیگ با موفقیت ساخته شد!':'Subscription group and 24 configurations created successfully!','رفرش':'Refresh','اتصالات فعال':'Active connections','زنده':'Live','کل ترافیک':'Total traffic','از راه‌اندازی':'Since startup','کانفیگ فعال':'Active configuration','از کل':'of total','لینک پیش‌فرض (بدون محدودیت)':'Default link (unlimited)','در حال دریافت...':'Loading...','کانفیگ محدود':'Limited configuration','ترافیک ساعتی (MB)':'Hourly traffic (MB)','توزیع پروتکل‌ها':'Protocol distribution','وضعیت سرویس':'Service status','فعال · سخت‌گیرانه':'Active · strict','فعال · 3 mode':'Active · 3 modes','فعال v9':'Active v9','آپتایم':'Uptime','بار نسبی':'Relative load','ارائه‌دهنده: مـحـمـدصـادق افـغـان':'Provider: Muhammad Sadiq Afghan','ساخت و مدیریت کانفیگ با سهمیه، انقضا و گروه‌بندی':'Create and manage configurations with quotas, expiry, and groups','همه دسته‌ها':'All categories','ساخت کانفیگ جدید':'Create new configuration','UUID تصادفی · سهمیه، انقضا و پروتکل رو انتخاب کن':'Random UUID · choose quota, expiry, and protocol','شناسه کانفیگ':'Configuration ID','— بدون دسته —':'— No category —','گروه ساب و انقضا':'Subscription group and expiry','— بدون گروه —':'— No group —','۷ روز':'7 days','۳۰ روز':'30 days','۹۰ روز':'90 days','سهمیه ترافیک':'Traffic quota','۵۰۰ MB':'500 MB','۱ GB':'1 GB','۵ GB':'5 GB','۱۰ GB':'10 GB','۵۰ GB':'50 GB','پروتکل انتقال':'Transport protocol','پایدار و همه‌منظوره':'Stable and general-purpose','سازگار با CDN':'CDN compatible','تاخیر پایین‌تر':'Lower latency','پیش‌فرض پروتکل':'Protocol default','دستی...':'Manual...','محدودیت آی‌پی / کاربر هم‌زمان':'IP limit / simultaneous users','۱ کاربر':'1 user','۲ کاربر':'2 users','۵ کاربر':'5 users','۱ Mbps':'1 Mbps','۵ Mbps':'5 Mbps','۱۰ Mbps':'10 Mbps','۲۵ Mbps':'25 Mbps','UUID کاملاً رندوم تولید می‌شود · فقط UUID‌های ثبت‌شده اجازه اتصال دارند · پروتکل پس از ساخت قابل تغییر نیست.':'UUIDs are random · only registered UUIDs can connect · protocol cannot be changed after creation.','هنوز کانفیگی وجود ندارد':'No configurations yet','هر گروه یک صفحه پابلیک مجزا با کانفیگ‌های خودش دارد':'Each group has its own public page and configurations','۰ گروه':'0 groups','گروه جدید':'New group','هنوز گروهی وجود ندارد':'No groups yet','یک گروه جدید بسازید تا کانفیگ‌ها را دسته‌بندی کنید':'Create a group to organize configurations','لینک‌های اشتراک برای اپ‌های v2ray':'Subscription links for V2Ray apps','سابسکریپشن‌های فعال':'Active subscriptions','گروه‌های دارای لینک ساب':'Groups with subscription links','کل کانفیگ‌ها':'Total configurations','قابل اشتراک‌گذاری':'Shareable','اپ‌های پشتیبانی‌شده':'Supported apps','و سایر کلاینت‌های VLESS':'and other VLESS clients','سابسکریپشن تکی':'Individual subscription','هر کانفیگ URL سابسکریپشن مخصوص دارد':'Each configuration has its own subscription URL','از کارت کانفیگ روی آیکون':'On a configuration card, click the icon','کلیک کنید تا URL سابسکریپشن اون کانفیگ کپی شه.':'to copy that configuration’s subscription URL.','سابسکریپشن کامل (ادمین)':'Full subscription (admin)','شامل تمام کانفیگ‌های فعال':'Includes all active configurations','این آدرس فقط در مرورگری که به پنل وارد شده کار می‌کند (نیاز به کوکی سشن).':'This URL works only in a browser signed in to the panel (session cookie required).','لینک سابسکریپشن گروه‌ها':'Group subscription links','هر گروه یک صفحه پابلیک مجزا':'Each group has a separate public page','تحلیل و مانیتورینگ مصرف پهنای باند':'Bandwidth usage analytics and monitoring','کل ترافیک مصرفی':'Total traffic used','میانگین ساعتی':'Hourly average','MB در ساعت':'MB per hour','پیک مصرف':'Peak usage','بالاترین ساعت':'Highest hour','کمترین مصرف':'Lowest usage','روند مصرف ترافیک':'Traffic usage trend','بر اساس مگابایت در هر ساعت':'Megabytes per hour','مصرف':'Usage','میانگین':'Average','مانیتورینگ زنده‌ی آی‌پی و ترافیک هر اتصال':'Live IP and traffic monitoring for each connection','مجموع ترافیک لحظه‌ای':'Current total traffic','میانگین مدت اتصال':'Average connection duration','آی‌پی‌های یکتا':'Unique IPs','لیست اتصالات':'Connection list','بروزرسانی خودکار هر ۵ ثانیه':'Auto-refresh every 5 seconds','هیچ اتصال فعالی نیست':'No active connections','به محض اتصال کلاینت‌ها، اینجا نمایش داده می‌شوند':'Clients appear here when they connect','فعالیت ساب‌ها':'Subscription activity','کارتی ساب‌ها + اتصال زنده IP → کانفیگ + لاگ کامل':'Subscription cards + live IP-to-config connections + full logs','اتصال‌های زنده':'Live connections','الان اتصال فعالی وجود ندارد':'There are no active connections right now','لاگ کامل فعالیت':'Full activity log','همه نوعها':'All types','کانفیگ':'Configuration','گروه':'Group','ورود':'Login','اتصال':'Connection','هنوز لاگی ثبت نشده':'No logs recorded yet','خطاهای ثبت‌شده‌ی سیستم':'System errors recorded','تعداد خطاها':'Error count','از زمان راه‌اندازی':'Since startup','آخرین خطا':'Latest error','وضعیت سیستم':'System status','سالم':'Healthy','همه سرویس‌ها فعال':'All services are active','لاگ خطاها':'Error log','خطاهای ثبت‌شده‌ی سیستم از زمان آخرین ریست':'System errors since the last reset','تست اتصال VLESS/WS روی UUID فعال':'Test VLESS/WS connection using an active UUID','فقط UUID‌های ثبت‌شده و فعال اتصال برقرار می‌کنند (این فقط تست VLESS/WS است؛ تست XHTTP از خود کلاینت انجام می‌شود).':'Only registered, active UUIDs can connect (this tests VLESS/WS; test XHTTP from the client app).','UUID (باید در کانفیگ‌ها وجود داشته باشد)':'UUID (must exist in configurations)','قطع':'Disconnect','ارسال':'Send','منتظر اتصال...':'Waiting for connection...','دسته‌بندی کانفیگ‌ها':'Configuration categories','کانفیگ‌ها را به دسته‌های منطقی تقسیم کنید':'Organize configurations into logical categories','۰ دسته':'0 categories','ساخت دسته جدید':'Create category','نام و رنگ دسته را انتخاب کنید':'Choose a category name and color','دسته‌های ساخته‌شده':'Created categories','هر دسته تعداد کانفیگ‌های متعلق به خود را نشان می‌دهد':'Each category shows how many configurations belong to it','پیکربندی پنل و اطلاعات سرور':'Panel configuration and server information','نسخه پنل':'Panel version','ساختار ۲۴ کانفیگ پرفورمنت':'24-configuration performance setup','آپتایم سرور':'Server uptime','از آخرین ریست':'Since last reset','هاست پابلیک':'Public host','لینک‌های ساب از اینجا':'Subscription links from here','اطلاعات سرور':'Server information','مشخصات زیرساخت فعال':'Active infrastructure details','کانفیگ‌ها، ساب‌ها و مصرف حجم بعد از دیپلوی حفظ می‌شوند؟':'Do configurations, subscriptions, and traffic usage persist after deployment?','مدیریت دسترسی پنل':'Panel access management','نام کاربری جدید':'New username','رمز فعلی':'Current password','رمز جدید':'New password','بکاپ کامل کانفیگ‌ها و ساب‌ها':'Full backup of configurations and subscriptions','فایل بکاپ شامل کانفیگ‌ها، گروه‌ها، حجم مصرفی و تنظیمات است. برای حفظ اطلاعات پس از استقرار مجدد، ذخیره‌سازی پایدار را فعال کنید و پشتیبان را جداگانه نگه دارید.':'The backup contains configurations, groups, traffic usage, and settings. Enable persistent storage and keep a separate backup to retain data after redeployments.','بارگذاری بکاپ':'Upload backup','مدیریت دستگاه‌های واردشده به پنل':'Manage devices signed in to the panel','خروج از سایر دستگاه‌ها':'Sign out of other devices','منابع سرور':'Server resources','CPU، RAM و شبکه‌ی همین سرویس':'CPU, RAM, and network usage for this service'
};
Object.assign(I18N, {"دسته‌بندی‌ها":"Categories","۰ کانفیگ":"0 configurations","محدودیت سرعت":"Speed limit","۰ انتخاب":"0 selected","۰":"0","جستجوی کانفیگ...":"Search configurations...","مثلاً: کانال اختصاصی":"e.g. VIP group","توضیح کوتاه درباره این گروه":"Short description of this group","خالی بگذارید = بدون رمز":"Leave blank = no password","مثلا 1 (خالی = نامحدود)":"e.g. 1 (blank = unlimited)","مثلا 30 (۰ = بدون انقضا)":"e.g. 30 (0 = no expiry)","مثلا 2 (۰ = نامحدود)":"e.g. 2 (0 = unlimited)","مثلاً: h2,http/1.1":"e.g. h2,http/1.1","مثلاً: سرویس VIP":"e.g. VIP service","مثلاً: کاربر علی":"e.g. User Ali","یادداشت (اختیاری)":"Note (optional)","انقضا (روز) · 0 = نامحدود":"Expiry (days) · 0 = unlimited","0 = نامحدود":"0 = unlimited","مقدار دستی ALPN":"Manual ALPN value","جستجو در گروه‌ها...":"Search groups...","🔍 جستجو در لاگ...":"🔍 Search logs...","UUID یک کانفیگ فعال":"UUID of an active configuration","پیام تست...":"Test message...","نام دسته جدید (مثلاً: VIP)":"New category name (e.g. VIP)","نام کاربری فعلی را نگه دارید":"Keep current username","خالی = بدون تغییر":"Blank = no change","وضعیت ذخیره‌سازی":"Storage status","دسته":"Category","هنوز دسته‌ای ساخته نشده":"No categories have been created yet","نام دسته الزامی است":"Category name is required","دسته ساخته شد ✓":"Category created ✓","خطا در ساخت دسته":"Failed to create category","حذف این دسته؟ کانفیگ‌ها به «عمومی» برمی‌گردند.":"Delete this category? Configurations will be moved to General.","دسته حذف شد":"Category deleted","خطا در حذف":"Delete failed","نشست فعلی شما است":"This is your current session","نامشخص":"Unknown","آی‌پی":"IP address","زمان ورود":"Login time","از همه‌ی دستگاه‌های دیگر خارج می‌شوید. ادامه؟":"You will be signed out from all other devices. Continue?","نشست لغو شد":"Session revoked","پردازنده":"CPU","روی":"on","هسته · لود":"cores · load","حافظه (این سرویس)":"Memory (this service)","MB کل سرور":"MB total server memory","دیسک":"Disk","% آزاد":"% free","شبکه":"Network","منقضی":"Expired","نامحدود":"Unlimited","حالت فارسی فعال شد":"Persian mode enabled","رمز فعلی را وارد کنید":"Enter the current password","چیزی برای تغییر وارد نشده":"Nothing to change was entered","رمز جدید حداقل ۶ کاراکتر":"New password must be at least 6 characters","در حال ذخیره...":"Saving...","خطا در به‌روزرسانی":"Update failed","✓ ذخیره شد":"✓ Saved","اعلان ورود به‌روزرسانی شد ✓":"Login notice updated ✓","در حال ساخت بکاپ...":"Creating backup...","خطا در ساخت بکاپ":"Backup creation failed","✓ بکاپ دانلود شد":"✓ Backup downloaded","بازگردانی بکاپ، تمام کانفیگ‌ها و ساب‌های فعلی را جایگزین می‌کند. ادامه می‌دهید؟":"Restoring this backup will replace all current configurations and subscriptions. Continue?","در حال بازگردانی...":"Restoring...","خطا در بازگردانی":"Restore failed","کانفیگ و":"Configuration and","ساب بازگردانی شد":"subscription restored","بکاپ بازگردانی شد ✓":"Backup restored ✓","فایل پشتیبان دانلود شد":"Backup file downloaded","دانلود پشتیبان ناموفق بود":"Backup download failed","Export لینک‌ها ناموفق بود":"Failed to export links","ولوم دائمی":"Persistent volume","ذخیره موقت":"Temporary storage","دیسک دائمی:":"Persistent storage:","مگابایت آزاد":"MB free","هیچ Volume پایداری شناسایی نشد؛ یک Volume به سرویس متصل کنید و Mount Path را /data قرار دهید.":"No persistent Volume detected. Attach a Volume to the service and set its mount path to /data.","آخرین بروزرسانی:":"Last updated:","همین الان":"just now","دقیقه پیش":"minutes ago","ساعت پیش":"hours ago","روز پیش":"days ago","روشن/خاموش":"Enable/disable","هنوز سابی وجود ندارد":"No subscriptions yet","در حال بارگذاری...":"Loading...","الان اتصال فعالی برای این ساب وجود ندارد":"There is no active connection for this subscription right now","مصرف به تفکیک کانفیگ":"Usage by configuration","هنوز رویدادی ثبت نشده":"No events recorded yet","ساب روشن شد ✓":"Subscription enabled ✓","ساب خاموش شد":"Subscription disabled","خطا در تغییر وضعیت":"Failed to change status","انتخاب کانفیگ":"Select configuration","UUID کپی شد":"UUID copied","آی‌پی‌های متصل / محدودیت":"Connected IPs / limit","فعال/غیرفعال":"Enable/disable","لینک کپی شد":"Link copied","Sub کپی شد":"Sub copied","ویرایش":"Edit","انتخاب":"Select","ابتدا کانفیگ‌ها را انتخاب کنید":"Select configurations first","فعال‌کردن":"Activate","غیرفعال‌کردن":"Deactivate","صفرکردن مصرف":"Reset usage","این کانفیگ‌ها برای همیشه حذف می‌شوند. ادامه می‌دهید؟":"These configurations will be permanently deleted. Continue?","برای کانفیگ اجرا شود؟":"Apply to the selected configurations?","مورد انجام شد ✓":"items processed ✓","عملیات گروهی ناموفق بود:":"Bulk operation failed:","کانفیگ جدید":"New configuration","کانفیگ ساخته شد ✓":"Configuration created ✓","خطا در ساخت":"Creation failed","کانفیگ ویرایش شد ✓":"Configuration updated ✓","خطا در ویرایش":"Update failed","فعال شد ✓":"Enabled ✓","غیرفعال شد":"Disabled","مصرف ریست شد ✓":"Usage reset ✓","حذف این کانفیگ؟":"Delete this configuration?","حذف شد ✓":"Deleted ✓","بدون توضیحات":"No description","رمزدار":"Password-protected","پابلیک":"Public","صفحه پابلیک":"Public page","لینک پابلیک کپی شد":"Public link copied","کپی پابلیک":"Copy public link","باز کردن":"Open","لینک ساب (base64)":"Subscription link (base64)","لینک ساب کپی شد":"Subscription link copied","کپی ساب":"Copy subscription","QR ساب":"Subscription QR","گروه ساخته شد ✓":"Group created ✓","خطا در ساخت گروه":"Failed to create group","گروه سریع":"Quick group","نام گروه را وارد کنید":"Enter a group name","مقادیر نمی‌توانند منفی باشند":"Values cannot be negative","حجم مشترک حداقل ۱ مگابایت باید باشد":"Shared quota must be at least 1 MB","در حال ساخت...":"Creating...","ساخت گروه شکست خورد":"Group creation failed","هشدار: تنظیم حجم مشترک ناموفق بود":"Warning: failed to set shared quota","هشدار: حجم مشترک درست ثبت نشد":"Warning: shared quota was not saved correctly","کانفیگ ساخته شد":"Configuration created","گروه ساخته شد. لینک سابسکریپشن کپی شود؟":"Group created. Copy the subscription link?","خطا در ساخت سریع":"Quick creation failed","این گروه و فقط کانفیگ‌های وابسته به همین گروه حذف می‌شوند. کانفیگ‌های گروه‌های دیگر باقی می‌مانند. ادامه می‌دهید؟":"This group and only its associated configurations will be deleted. Configurations in other groups will remain. Continue?","گروه حذف شد ✓":"Group deleted ✓","خطا در بارگذاری":"Loading failed","کپی لینک VLESS":"Copy VLESS link","ساب کپی شد":"Subscription copied","کپی Sub URL":"Copy Sub URL","QR کد":"QR code","انتخاب شده":"selected","کانفیگ‌های گروه ذخیره شدند ✓":"Group configurations saved ✓","خطا در ذخیره":"Save failed","کپی شد":"Copied","کپی شد ✓":"Copied ✓","ثانیه":"seconds","دقیقه":"minutes","ساعت":"hours","IP کپی شد":"IP copied","کپی IP":"Copy IP","بدون خطا":"No errors","سیستم پایدار":"System stable","رفرش شد":"Refreshed","UUID را وارد کنید":"Enter a UUID","اتصال:":"Connection:","✓ متصل - UUID معتبر":"✓ Connected - valid UUID","✗ خطا - UUID نامعتبر یا غیرفعال":"✗ Error - invalid or inactive UUID","دریافت":"Receive","- دسترسی رد شد":"- Access denied","ارسال:":"Send:","ساب گروه جدید":"New subscription group","در حال ساخت ۲۴ کانفیگ...":"Creating 24 configurations...","ساخت کانفیگ‌ها ناقص بود (":"Configuration creation was incomplete (","گروه ساب با ۲۴ کانفیگ ساخته شد":"Subscription group created with 24 configurations","خطا در ساخت ساب:":"Failed to create subscription:"});
Object.assign(I18N, {"دسته‌بندی‌ها":"Categories","محدودیت سرعت":"Speed limit","۰ کانفیگ":"0 configurations","۰ انتخاب":"0 selected","۰":"0"});
const I18N_TEXT_ORIGINALS=new WeakMap();
const I18N_ATTRIBUTE_ORIGINALS=new WeakMap();
function translatePage(lang){
  const walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);const nodes=[];
  while(walker.nextNode())nodes.push(walker.currentNode);
  for(const node of nodes){
    const parent=node.parentElement;if(!parent||parent.closest('script,style,textarea,input,pre,code'))continue;
    if(!I18N_TEXT_ORIGINALS.has(node))I18N_TEXT_ORIGINALS.set(node,node.nodeValue||'');
    const original=I18N_TEXT_ORIGINALS.get(node);const match=original.match(/^(\s*)([\s\S]*?)(\s*)$/);if(!match)continue;
    const raw=match[2].trim();if(!raw)continue;
    const next=lang==='en'?(I18N[raw]||raw):raw;const value=match[1]+next+match[3];
    if(node.nodeValue!==value)node.nodeValue=value;
  }
  document.querySelectorAll('[placeholder],[title],[aria-label]').forEach(el=>{
    let originals=I18N_ATTRIBUTE_ORIGINALS.get(el);
    if(!originals){originals={};for(const attr of ['placeholder','title','aria-label'])if(el.hasAttribute(attr))originals[attr]=el.getAttribute(attr);I18N_ATTRIBUTE_ORIGINALS.set(el,originals);}
    for(const [attr,original] of Object.entries(originals)){if(original!==null&&original!==undefined)el.setAttribute(attr,lang==='en'?(I18N[original]||original):original);}
  });
  const btn=document.getElementById('language-toggle');const buttonHtml='<i class="ti ti-language"></i> '+(lang==='fa'?'English':'فارسی');if(btn&&btn.innerHTML!==buttonHtml)btn.innerHTML=buttonHtml;
}
function applyLanguage(lang){currentLang=lang==='en'?'en':'fa';try{localStorage.setItem('finevpn-lang',currentLang);document.documentElement.lang=currentLang;document.documentElement.dir=currentLang==='fa'?'rtl':'ltr';}catch(e){}translatePage(currentLang);}
function toggleLanguage(){applyLanguage(currentLang==='en'?'fa':'en');applyTheme(isDark);toast(currentLang==='en'?'English mode enabled':'حالت فارسی فعال شد');}
applyLanguage(currentLang);
const _i18nObserver=new MutationObserver(()=>{if(!document.documentElement.dataset.i18nUpdating){document.documentElement.dataset.i18nUpdating='1';translatePage(currentLang);delete document.documentElement.dataset.i18nUpdating;}});
_i18nObserver.observe(document.body,{subtree:true,childList:true});

async function saveCredentialsV2(){
  const username=document.getElementById('cred-username-v2').value.trim();
  const current_password=document.getElementById('cred-current-v2').value;
  const new_password=document.getElementById('cred-new-v2').value;
  const st=document.getElementById('cred-status-v2');
  if(!current_password){st.textContent='رمز فعلی را وارد کنید';st.style.color='var(--red-t)';return}
  if(!username&&!new_password){st.textContent='چیزی برای تغییر وارد نشده';st.style.color='var(--red-t)';return}
  if(new_password&&new_password.length<6){st.textContent='رمز جدید حداقل ۶ کاراکتر';st.style.color='var(--red-t)';return}
  st.innerHTML='<i class="ti ti-loader-2 ti-spin"></i> در حال ذخیره...';st.style.color='var(--t3)';
  try{
    const r=await authF('/api/change-credentials',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:username||undefined,current_password,new_password:new_password||undefined})});
    const d=await r.json();if(!r.ok)throw Error(d.detail||'خطا در به‌روزرسانی');
    st.textContent='✓ ذخیره شد';st.style.color='var(--green-t)';
    document.getElementById('cred-current-v2').value='';document.getElementById('cred-new-v2').value='';
    toast('اعلان ورود به‌روزرسانی شد ✓','ok');
    if(username)setTimeout(()=>location.reload(),1200);
  }catch(e){st.textContent=e.message;st.style.color='var(--red-t)'}
}
async function downloadBackupV2(){
  const st=document.getElementById('backup-status-v2');
  st.innerHTML='<i class="ti ti-loader-2 ti-spin"></i> در حال ساخت بکاپ...';st.style.color='var(--t3)';
  try{
    const r=await authF('/api/backup');
    if(!r.ok)throw Error('خطا در ساخت بکاپ');
    const blob=await r.blob();
    const a=document.createElement('a');
    a.href=URL.createObjectURL(blob);
    a.download='finevpn-backup-'+new Date().toISOString().slice(0,10)+'.json';
    document.body.appendChild(a);a.click();a.remove();
    st.textContent='✓ بکاپ دانلود شد';st.style.color='var(--green-t)';
  }catch(e){st.textContent=e.message;st.style.color='var(--red-t)'}
}
async function restoreBackupV2(input){
  const file=input.files[0];if(!file)return;
  const st=document.getElementById('backup-status-v2');
  if(!confirm('بازگردانی بکاپ، تمام کانفیگ‌ها و ساب‌های فعلی را جایگزین می‌کند. ادامه می‌دهید؟')){input.value='';return}
  st.innerHTML='<i class="ti ti-loader-2 ti-spin"></i> در حال بازگردانی...';st.style.color='var(--t3)';
  try{
    const text=await file.text();
    const data=JSON.parse(text);
    const r=await authF('/api/restore',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)});
    const d=await r.json();if(!r.ok)throw Error(d.detail||'خطا در بازگردانی');
    st.textContent='✓ '+d.links+' کانفیگ و '+d.subs+' ساب بازگردانی شد';st.style.color='var(--green-t)';
    toast('بکاپ بازگردانی شد ✓','ok');
    setTimeout(()=>location.reload(),1500);
  }catch(e){st.textContent=e.message;st.style.color='var(--red-t)'}
  input.value='';
}


async function checkAuth(){try{const r=await fetch('/api/me');const d=await r.json();if(!d.authenticated)location.href='/login';}catch(e){location.href='/login'}}
async function logout(){try{await fetch('/api/logout',{method:'POST'})}catch(e){}location.href='/login'}
document.getElementById('logout-btn').addEventListener('click',logout);
async function authF(url,opts={}){
  const r=await fetch(url,opts);
  if(r.status===401){location.href='/login';throw new Error('unauthorized')}
  return r;
}
async function downloadBackup(){
  try{
    const r=await authF('/api/backup');
    if(!r.ok)throw new Error('backup failed');
    const blob=await r.blob(), a=document.createElement('a');
    a.href=URL.createObjectURL(blob);a.download='finevpn-backup.json';a.click();URL.revokeObjectURL(a.href);
    toast('فایل پشتیبان دانلود شد','ok');
  }catch(e){toast('دانلود پشتیبان ناموفق بود','err')}
}
async function exportActiveLinks(){
  try{
    const r=await authF('/api/links/export'), d=await r.json();
    const blob=new Blob([(d.links||[]).join('\\n')+'\\n'],{type:'text/plain;charset=utf-8'}), a=document.createElement('a');
    a.href=URL.createObjectURL(blob);a.download='finevpn-active-links.txt';a.click();URL.revokeObjectURL(a.href);
    toast(`${d.count||0} لینک export شد`,'ok');
  }catch(e){toast('Export لینک‌ها ناموفق بود','err')}
}
function setQuota(val,unit,el){
  document.getElementById('nl-val').value = val===0?'':val;
  document.getElementById('nl-unit').value = unit;
  document.querySelectorAll('#quota-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function setExpiry(days,el){
  document.getElementById('nl-exp').value = days===0?'':days;
  document.querySelectorAll('#exp-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function selectProto(val,el){
  document.getElementById('nl-proto').value = val;
  document.querySelectorAll('.proto-card').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function setIpLimit(n,el){
  document.getElementById('nl-iplimit').value = n;
  document.querySelectorAll('#iplimit-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function setSpeedLimit(n,el){
  document.getElementById('nl-speed').value = n;
  document.getElementById('nl-speed-unit').value = 'MBIT';
  document.querySelectorAll('#speed-chips .chip').forEach(c=>c.classList.remove('active'));
  el.classList.add('active');
}
function onAlpnPresetChange(){
  const p=document.getElementById('nl-alpn-preset').value;
  const inp=document.getElementById('nl-alpn');
  if(p==='__custom__'){inp.style.display='block';inp.value='';inp.focus();}
  else{inp.style.display='none';inp.value=p;}
}
const sb=document.getElementById('sb'),overlay=document.getElementById('overlay');
function openSb(){sb.classList.add('open');overlay.classList.add('show')}
function closeSb(){sb.classList.remove('open');overlay.classList.remove('show')}
document.getElementById('open-sb').addEventListener('click',openSb);
document.getElementById('close-sb').addEventListener('click',closeSb);
overlay.addEventListener('click',closeSb);
function navTo(name){
  document.querySelectorAll('.nav-it').forEach(n=>n.classList.toggle('on',n.dataset.pg===name));
  document.querySelectorAll('.pg').forEach(p=>p.classList.toggle('on',p.id==='pg-'+name));
  const loaders={links:loadLinks,connections:loadConns,errors:loadErrs,subscriptions:loadSubsPage,subgroups:loadSubs,logs:loadActivity,categories:loadCats,settings:()=>{loadSetServer();loadSessions();loadTelemetry();startTelemetry();},testws:null};
  if(loaders[name])loaders[name]();
  closeSb();window.scrollTo({top:0,behavior:'smooth'});
}
document.querySelectorAll('.nav-it').forEach(el=>el.addEventListener('click',()=>navTo(el.dataset.pg)));
function openModal(id){document.getElementById(id).classList.add('open')}
function closeModal(id){document.getElementById(id).classList.remove('open')}
let prevTraf=0,ch1,ch2,ch3;
function updateConnsBadge(count){
  const el=document.getElementById('conns-live');if(!el)return;
  const n=Math.max(0,Number(count)||0),active=n>0;
  el.className='badge '+(active?'bg-green':'bg-red');
  el.innerHTML=active?'<span class="dot dg"></span> '+toFa(n)+' IP یکتا متصل':'<span class="dot dr"></span> هیچ IP متصلی نیست';
}
async function fetchStats(){
  try{
    const r=await authF('/stats'),d=await r.json();
    const serverBadge=document.getElementById('server-status-badge');if(serverBadge){serverBadge.className='badge bg-green';serverBadge.innerHTML='<span class="dot dg"></span> پنل در دسترس';}
    document.getElementById('m-conns').textContent=toFa(d.active_users??0);
    const sessionEl=document.getElementById('m-sessions');if(sessionEl)sessionEl.textContent=toFa(d.active_sessions??d.active_connections??0);
    document.getElementById('conns-nb').textContent=d.active_sessions??d.active_connections??0;
    document.getElementById('m-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="m-unit">MB</span>';
    document.getElementById('m-alinks').textContent=d.active_links??'—';
    document.getElementById('m-lsub').textContent='از '+d.links_count+' کانفیگ';
    document.getElementById('m-subs').textContent=d.subs_count??'—';
    document.getElementById('errs-badge').textContent=d.total_errors+' خطا';
    document.getElementById('uptime-inline').textContent=d.uptime;
    if(d.volume){const vb=document.getElementById('vol-badge');
      if(vb){const ok=d.volume.mounted&&d.volume.writable;
        vb.className='badge '+(ok?'b-ok':'b-warn');
        vb.innerHTML='<i class="ti ti-'+(ok?'database-check':'alert-triangle')+'"></i> '+(ok?'ولوم دائمی':'ذخیره موقت');
        vb.title=ok?('دیسک دائمی: '+d.volume.data_dir+' · '+d.volume.free_mb+' مگابایت آزاد'):'هیچ Volume پایداری شناسایی نشد؛ یک Volume به سرویس متصل کنید و Mount Path را /data قرار دهید.';
      }}
    document.getElementById('uptime-badge').textContent='سرور · '+d.uptime;
    document.getElementById('last-upd').textContent='آخرین بروزرسانی: '+new Date().toLocaleTimeString('fa-IR');
    updateConnsBadge(d.active_users??0);
    document.getElementById('t-traffic').innerHTML=d.total_traffic_mb.toFixed(1)+'<span class="m-unit">MB</span>';
    const delta=d.total_traffic_mb-prevTraf,pct=Math.min(100,Math.round((delta/50)*100));
    document.getElementById('bw-pct').textContent=pct+'%';
    document.getElementById('bw-bar').style.width=pct+'%';
    prevTraf=d.total_traffic_mb;
    if(d.hourly){
      if(!ch1||!ch3)initCharts();
      const labels=Object.keys(d.hourly).sort(),vals=labels.map(k=>+(d.hourly[k]/1024**2).toFixed(2));
      [ch1,ch3].forEach(c=>{if(!c||!c.data)return;c.data.labels=labels;c.data.datasets[0].data=vals;c.update()});
      if(vals.length){const avg=vals.reduce((a,b)=>a+b,0)/vals.length,peak=Math.max(...vals);document.getElementById('t-avg').innerHTML=avg.toFixed(2)+'<span class="m-unit">MB</span>';document.getElementById('t-peak').innerHTML=peak.toFixed(2)+'<span class="m-unit">MB</span>';}
    }
    if(ch2&&d.protocol_counts){
      const labels=Object.keys(d.protocol_counts),values=labels.map(k=>Number(d.protocol_counts[k]||0));
      ch2.data.labels=labels.length?labels.map(k=>({'vless-ws':'VLESS / WS','xhttp-packet-up':'XHTTP Packet-up','xhttp-stream-up':'XHTTP Stream-up'}[k]||k)):['اتصال زنده‌ای نیست'];
      ch2.data.datasets[0].data=labels.length?values:[0];ch2.update();
    }
    renderErrs(d.recent_errors||[]);
  }catch(e){const serverBadge=document.getElementById('server-status-badge');if(serverBadge){serverBadge.className='badge bg-red';serverBadge.innerHTML='<span class="dot dr"></span> عدم دسترسی به پنل';}console.error(e)}
}
function renderErrs(errs){
  const el=document.getElementById('errs-full');if(!el)return;
  if(!errs.length){el.innerHTML='<div style="color:var(--green-t);padding:10px;font-size:12px;display:flex;align-items:center;gap:5px"><i class="ti ti-circle-check"></i> هیچ خطایی نیست</div>';return}
  el.innerHTML=errs.slice().reverse().map(e=>`<div class="erow"><div class="etime"><i class="ti ti-clock"></i>${new Date(e.time).toLocaleString('fa-IR')}</div><div class="emsg">${esc(e.error)}${e.url?' — '+esc(e.url):''}</div></div>`).join('');
}
let actLogPoll=null;
async function loadActivity(){
  try{
    const [ar,sr,cr]=await Promise.all([authF('/api/activity'),authF('/api/subs'),authF('/api/connections')]);
    const {logs=[]}=await ar.json();
    const {subs=[]}=await sr.json();
    const cd=await cr.json();
    const conns=cd.connections||[];

    // --- sub cards ---
    const subsBox=document.getElementById('act-subs');
    subsBox.innerHTML=subs.length?subs.map(s=>{
      const limitFmt=s.total_limit_bytes?fmtB(s.total_limit_bytes):'نامحدود';
      const usedPct=s.total_limit_bytes?Math.min(100,Math.round((s.total_used_bytes/s.total_limit_bytes)*100)):0;
      const age=Date.now()-new Date(s.created_at).getTime();
      const ageTxt=age<60000?'همین الان':age<3600000?Math.floor(age/60000)+' دقیقه پیش':age<86400000?Math.floor(age/3600000)+' ساعت پیش':Math.floor(age/86400000)+' روز پیش';
      const ipLimits=(s.link_ids||[]).map(lid=>{const L=(allLinksList||[]).find(x=>x.uuid===lid);return L?L.ip_limit:0});
      const ipMax=ipLimits.length?Math.max(...ipLimits):0;
      const subConns=conns.filter(c=>(s.link_ids||[]).some(lid=>(c.labels||[]).includes(labelOf(lid))));
      return `<div class="card sub-exp-card" style="padding:16px" onclick="toggleSubCard(this,'${esc(s.sub_id)}')">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px">
          <span class="m-ring" style="width:36px;height:36px;font-size:16px"><i class="ti ti-folder"></i></span>
          <div style="flex:1;min-width:0">
            <div style="font-size:14px;font-weight:800;color:var(--t1)">${esc(s.name)}</div>
            <div style="font-size:10.5px;color:var(--t3)"><i class="ti ti-clock"></i> ${ageTxt}</div>
          </div>
          <label class="switch" style="position:relative;display:inline-block;width:38px;height:21px;cursor:pointer" title="روشن/خاموش">
            <input type="checkbox" ${s.active_count>0?'checked':''} onchange="toggleSub('${esc(s.sub_id)}',this.checked)" style="opacity:0;width:0;height:0">
            <span class="slider" style="position:absolute;inset:0;background:rgba(255,255,255,.12);border-radius:20px;transition:.25s"></span>
          </label>
        </div>
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:12px">
          <div style="background:rgba(16,185,129,.06);border-radius:10px;padding:9px 6px;text-align:center">
            <div style="font-size:14px;font-weight:800;color:var(--green-t)">${esc(s.total_used_fmt||'0 B')}</div>
            <div style="font-size:9.5px;color:var(--t3)">مصرف</div>
          </div>
          <div style="background:rgba(16,185,129,.06);border-radius:10px;padding:9px 6px;text-align:center">
            <div style="font-size:14px;font-weight:800;color:var(--t1)">${toFa(s.links_count)}</div>
            <div style="font-size:9.5px;color:var(--t3)">کانفیگ</div>
          </div>
          <div style="background:rgba(16,185,129,.06);border-radius:10px;padding:9px 6px;text-align:center">
            <div style="font-size:14px;font-weight:800;color:var(--t1)">${ipMax?toFa(ipMax):'∞'}</div>
            <div style="font-size:9.5px;color:var(--t3)">سقف IP</div>
          </div>
        </div>
        <div style="font-size:10px;color:var(--t3);display:flex;justify-content:space-between;margin-bottom:5px">
          <span>حجم مشترک: ${limitFmt}</span><span>${usedPct}%</span>
        </div>
        <div class="spbar" style="width:100%;height:7px"><div class="spfill" style="width:${usedPct}%"></div></div>
        <div class="sub-exp-hint"><i class="ti ti-chevron-down"></i> برای جزئیات کلیک کنید</div>
        <div class="sub-exp-body" id="sub-body-${esc(s.sub_id)}"></div>
      </div>`;
    }).join(''):'<div class="empty"><i class="ti ti-folders"></i><p>هنوز سابی وجود ندارد</p></div>';

    // --- live connections ---
    const cb=document.getElementById('act-conns-badge');
    cb.textContent=toFa(cd.count||0)+' اتصال';
    const cBox=document.getElementById('act-conns'),cEm=document.getElementById('act-conns-empty');
    if(!conns.length){cBox.innerHTML='';cEm.style.display='block'}
    else{
      cEm.style.display='none';
      cBox.innerHTML=conns.map(c=>`
        <div style="display:flex;align-items:center;gap:10px;padding:10px 4px;border-bottom:1px solid var(--card-b);direction:ltr">
          <span class="dot dg pulse"></span>
          <span style="font-weight:700;color:var(--t1);font-size:12px">${esc(c.ip)}</span>
          <span style="font-size:11px;color:var(--t3)">→</span>
          <span style="font-size:11.5px;color:var(--t2);flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">${esc(c.label||'نامشخص')}</span>
          ${c.dest?`<span style="font-size:11px;color:var(--green-t)">⇢ ${esc(c.dest)}</span>`:''}
          <span style="font-size:10px;color:var(--purple-t);background:var(--purple-bg);padding:2px 7px;border-radius:6px;white-space:nowrap">${esc(c.device||'')}</span>
          <span style="font-size:10.5px;color:var(--t3);white-space:nowrap">${esc(c.bytes_fmt||'0 B')}</span>
        </div>`).join('');
    }

    // --- full log ---
    const q=(document.getElementById('log-search')||{value:''}).value.trim().toLowerCase();
    const f=(document.getElementById('log-kind')||{value:''}).value;
    const filtered=logs.filter(l=>{
      if(f&&l.kind!==f)return false;
      if(q&&!(l.message||'').toLowerCase().includes(q)&&!new Date(l.time).toLocaleString('fa-IR').includes(q))return false;
      return true;
    });
    const sorted=filtered.slice().reverse();
    const el=document.getElementById('logs-list'),em=document.getElementById('logs-empty');
    if(!sorted.length){el.innerHTML='';em.style.display='block'}
    else{
      em.style.display='none';
      const icMap={ok:'ti-circle-check',err:'ti-circle-x',warn:'ti-alert-triangle',info:'ti-info-circle'};
      const kindFa={link:'کانفیگ',sub:'گروه',auth:'ورود',connection:'اتصال',system:'سیستم'};
      el.innerHTML=sorted.map(l=>`
        <div class="log-item">
          <div class="log-ic ${l.level}"><i class="ti ${icMap[l.level]||'ti-info-circle'}"></i></div>
          <div class="log-body">
            <div class="log-msg">${esc(l.message)}</div>
            <div class="log-time"><i class="ti ti-clock"></i> ${new Date(l.time).toLocaleString('fa-IR')} <span class="log-kind">${kindFa[l.kind]||l.kind}</span></div>
          </div>
        </div>
      `).join('');
    }
  }catch(e){console.error(e)}
  if(!actLogPoll){actLogPoll=setInterval(()=>{
    if(document.getElementById('pg-logs').classList.contains('on')){
      // ═══ وقتی کارت جزئیات ساب باز است، re-render نکنید تا کارت بسته نشود ═══
      if(document.querySelector('.sub-exp-card.open')) return;
      loadActivity();
    }
  },5000)}
}
function labelOf(uuid){const L=(allLinksList||[]).find(x=>x.uuid===uuid);return L?L.label:''}
// ══════ کارت ساب: باز/بسته کردن + بارگذاری جزئیات ══════
let subDetailCache={};
async function toggleSubCard(el,subId){
  const body=document.getElementById('sub-body-'+subId);
  if(!body) return;
  const isOpen=el.classList.contains('open');
  if(isOpen){ el.classList.remove('open'); return; }
  el.classList.add('open');
  body.innerHTML='<div style="text-align:center;padding:14px;color:var(--t3);font-size:11px"><i class="ti ti-loader ti-spin"></i> در حال بارگذاری...</div>';
  try{
    const [ar,cr]=await Promise.all([authF('/api/activity'),authF('/api/connections')]);
    const {logs=[]}=await ar.json();
    const cd=await cr.json();
    const conns=cd.connections||[];
    // connections touching this sub (by label match)
    const sr=await authF('/api/subs'); const {subs=[]}=await sr.json();
    const s=subs.find(x=>x.sub_id===subId)||{};
    // ═══ allLinksList فقط بعد از ورود به صفحه links پر می‌شود؛ اینجا مستقل می‌گیریم ═══
    if(!allLinksList.length){
      try{const lr=await authF('/api/links'); const {links=[]}=await lr.json(); if(links.length) allLinksList=links;}catch(e){}
    }
    const myLabels=(s.link_ids||[]).map(labelOf).filter(Boolean);
    const myConns=conns.filter(c=>(c.labels||[]).some(l=>myLabels.includes(l)));
    // per-sub log: mentions any of my labels OR sub creation
    const myLogs=logs.filter(l=>l.message&&myLabels.some(lb=>l.message.includes(lb)));
    const subLogs=logs.filter(l=>l.sub_id===subId);
    const allLogs=[...myLogs,...subLogs].slice(-40).reverse();
    let h='';
    h+='<div class="sub-sec-label"><i class="ti ti-users"></i> آی‌پی‌های متصل ('+toFa(myConns.length)+')</div>';
    if(!myConns.length){h+='<div style="font-size:11px;color:var(--t3);padding:6px 2px">الان اتصال فعالی برای این ساب وجود ندارد</div>'}
    else{
      myConns.forEach(c=>{
        const cdev=c.device||'نامشخص';
        const cua=c.ua||c.user_agent||'';
        const uaShort=cua?cua.split(' ').slice(0,3).join(' '):'';
        h+='<div class="sub-ip-row" style="display:block;padding:9px 10px;border:1px solid var(--card-b);border-radius:10px;margin-bottom:6px">'
          +'<div style="display:flex;align-items:center;gap:8px;direction:ltr"><span class="dot dg pulse"></span><span class="sub-ip-addr">'+esc(c.ip)+'</span>'
          +'<span style="font-size:10px;color:var(--purple-t);background:var(--purple-bg);padding:2px 7px;border-radius:6px;white-space:nowrap"><i class="ti ti-device-mobile"></i> '+esc(cdev)+'</span>'
          +'<span style="font-size:10px;color:var(--t3);margin-right:auto;white-space:nowrap">'+esc(c.bytes_fmt||'0 B')+'</span></div>'
          +'<div style="display:flex;gap:8px;margin-top:5px;font-size:10px;color:var(--t2);direction:ltr;flex-wrap:wrap">'
          +'<span><i class="ti ti-router"></i> '+esc((c.labels||[]).filter(l=>myLabels.includes(l)).join(' · ')||'—')+'</span>'
          +(c.dest?'<span style="color:var(--green-t)"><i class="ti ti-world"></i> '+esc(c.dest)+'</span>':'')
          +(uaShort?'<span style="color:var(--t3);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;max-width:160px" title="'+esc(cua)+'"><i class="ti ti-code"></i> '+esc(uaShort)+'</span>':'')
          +'</div></div>';
      });
    }
    // per-config usage breakdown
    let perCfg=[];
    try{const lr=await authF('/api/links');const {links:allLinks=[]}=await lr.json();
      perCfg=(allLinks||[]).filter(l=>(s.link_ids||[]).includes(l.uuid)).map(l=>({label:l.label,used:l.used_bytes||0,active:l.active})).sort((a,b)=>b.used-a.used);
    }catch(e){}
    if(perCfg.length){
      h+='<div class="sub-sec-label"><i class="ti ti-chart-bar"></i> مصرف به تفکیک کانفیگ</div>';
      h+='<div class="sub-cfg-list">';
      const maxUsed=Math.max(1,...perCfg.map(x=>x.used));
      perCfg.forEach(x=>{
        h+='<div class="sub-cfg-row"><div style="display:flex;justify-content:space-between;font-size:10.5px;margin-bottom:3px"><span style="color:var(--t2);font-weight:600">'+esc(x.label)+(x.active?'':' <span style="color:var(--red-t)">⚫</span>')+'</span><span style="color:var(--t3)">'+fmtB(x.used)+'</span></div><div class="spbar" style="height:5px"><div class="spfill" style="width:'+Math.round(x.used/maxUsed*100)+'%"></div></div></div>';
      });
      h+='</div>';
    }
    h+='<div class="sub-sec-label"><i class="ti ti-history"></i> لاگ کامل این ساب ('+toFa(allLogs.length)+')</div>';
    if(!allLogs.length){h+='<div style="font-size:11px;color:var(--t3);padding:6px 2px">هنوز رویدادی ثبت نشده</div>'}
    else{
      h+='<div class="sub-log-list">';
      const icMap={ok:'ti-circle-check',err:'ti-circle-x',warn:'ti-alert-triangle',info:'ti-info-circle'};
      allLogs.forEach(l=>{
        h+='<div class="sub-log-item"><div class="sub-log-ic '+(l.level||'info')+'"><i class="ti '+(icMap[l.level]||'ti-info-circle')+'"></i></div><div class="sub-log-msg">'+esc(l.message)+'</div><div class="sub-log-time">'+new Date(l.time).toLocaleTimeString('fa-IR')+'</div></div>';
      });
      h+='</div>';
    }
    body.innerHTML=h;
    // ═══ کلیک داخل جزئیات کارت رو بلاک میکنیم تا کارت بسته نشه ═══
    body.querySelectorAll('.sub-ip-row,.sub-cfg-list,.sub-log-list,.sub-sec-label').forEach(r=>r.addEventListener('click',e=>e.stopPropagation()));
  }catch(e){console.error(e);body.innerHTML='<div style="font-size:11px;color:var(--red-t)">خطا در بارگذاری</div>'}
}

async function toggleSub(subId,on){
  try{
    const r=await authF('/api/subs/'+subId),s=await r.json();
    for(const lid of (s.link_ids||[])){
      await authF('/api/links/'+lid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:on})});
    }
    toast(on?'ساب روشن شد ✓':'ساب خاموش شد','ok');
  }catch(e){toast('خطا در تغییر وضعیت','err')}
}
let allSubsList=[],allLinksList=[];
async function loadLinks(){
  try{
    const [lr,sr]=await Promise.all([authF('/api/links'),authF('/api/subs')]);
    let {links=[]}=await lr.json();
    const {subs=[]}=await sr.json();
    allSubsList=subs;allLinksList=links;
    const nlSub=document.getElementById('nl-sub');
    nlSub.innerHTML='<option value="">— بدون گروه —</option>'+subs.map(s=>`<option value="${esc(s.sub_id)}">${esc(s.name)}</option>`).join('');
    const nlCat=document.getElementById('nl-cat');
    const cf=document.getElementById('cat-filter'), curCat=cf?cf.value:'';
    const cats=(await (await authF('/api/categories')).json()).categories||[];
    window._cats=Array.isArray(cats)?cats:[];
    if(nlCat)nlCat.innerHTML='<option value="">— بدون دسته —</option>'+window._cats.map(c=>`<option value="${esc(c.id)}">${esc(c.name)}</option>`).join('');
    if(cf)cf.innerHTML='<option value="">همه دسته‌ها</option>'+window._cats.map(c=>`<option value="${esc(c.id)}">${esc(c.name)}</option>`).join('');
    if(cf&&curCat)cf.value=curCat;
    document.getElementById('links-nb').textContent=links.length;
    const lpc=document.getElementById('links-pg-cnt');if(lpc)lpc.textContent=toFa(links.length)+' کانفیگ';
    if(!links.length){const grid0=document.getElementById('links-grid');
      if(grid0)grid0.innerHTML='<div class="empty"><i class="ti ti-link-off"></i><p>هنوز کانفیگی وجود ندارد</p></div>';
      return}
    const grid=document.getElementById('links-grid'),empty=document.getElementById('links-empty');
    if(!grid)return;
    if(empty)empty.style.display='none';
    const cf2=document.getElementById('cat-filter');
    const fCat=cf2?cf2.value:'';
    if(fCat)links=links.filter(l=>String((l.category||{}).id||'0')===fCat);
    const subMap=Object.fromEntries(subs.map(s=>[s.sub_id,s.name]));
    grid.innerHTML=links.map(l=>{
  const catPill=(l.category&&l.category.name)?`<span class="cat-pill" style="background:${(l.category.color||'#10B981')}22;color:${l.category.color||'#10B981'}"><span class="cat-dot" style="background:${l.category.color||'#10B981'}"></span>${esc(l.category.name)}</span>`:'';
  const lim=l.limit_bytes===0?'∞':fmtB(l.limit_bytes);
  const pct=l.limit_bytes===0?0:Math.min(100,l.used_bytes/l.limit_bytes*100);
  const bc=pct>90?'var(--red)':pct>70?'var(--amber)':'var(--accent)';
  const allowed=l.active&&!l.expired;
  const cardCls=!l.active?'is-off':(l.expired?'is-exp':'');
  return `<div class="cfg-card ${cardCls}" data-link-id="${esc(l.uuid)}">
    <div class="cfg-row">
      <label class="bulk-config-select" title="انتخاب کانفیگ" style="display:flex;align-items:center;padding-inline:5px"><input class="bulk-config-check" type="checkbox" value="${esc(l.uuid)}" onchange="updateBulkSelection()" aria-label="انتخاب کانفیگ"></label>
      <span class="cfg-status-dot ${allowed?'pulse':''}"></span>
      <div class="cfg-identity">
        <div class="cfg-label">${esc(l.label)}${catPill}</div>
        <div class="cfg-sub-meta">
          <span class="cfg-uuid-mini" onclick="navigator.clipboard.writeText('${l.uuid}').then(()=>toast('UUID کپی شد','ok'))" title="${l.uuid}"><i class="ti ti-fingerprint"></i> ${l.uuid.slice(0,10)}…</span>
          <span>${new Date(l.created_at).toLocaleDateString('fa-IR')}</span>
        </div>
      </div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-usage-col">
        <div class="ubar"><div class="ubar-f" style="width:${pct}%;background:${bc}"></div></div>
        <div class="utxt"><span>${fmtB(l.used_bytes)}</span><span>از ${lim}</span></div>
      </div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-exp-col">${expChip(l.expires_at,l.expired)}</div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-badges-col">
        ${protoBadge(l.protocol)}
        <span class="cfg-sub-tag" title="پورت اتصال"><i class="ti ti-route"></i> :${l.port||443}</span>
        <span class="cfg-sub-tag" title="Fingerprint"><i class="ti ti-fingerprint"></i> ${esc(l.fingerprint||'chrome')}</span>
        <span class="cfg-sub-tag" title="آی‌پی‌های متصل / محدودیت"><i class="ti ti-users"></i> ${l.connected_ips||0}${l.ip_limit?('/'+l.ip_limit):' (∞)'}</span>
        <span class="cfg-sub-tag" title="محدودیت سرعت"><i class="ti ti-gauge"></i> ${l.speed_limit_bytes?((l.speed_limit_bytes*8/1024/1024).toFixed(1)+' Mbps'):'نامحدود'}</span>
        ${l.sub_id&&allSubsList.find(s=>s.sub_id===l.sub_id)?`<span class="cfg-sub-tag"><i class="ti ti-folder"></i> ${esc(allSubsList.find(s=>s.sub_id===l.sub_id).name)}</span>`:''}
      </div>
      <div class="cfg-divider-v"></div>
      <div class="cfg-actions">
        <button class="tog${allowed?' on':''}" onclick="toggleActive('${l.uuid}',${!l.active})" title="فعال/غیرفعال"></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText('${esc(l.vless_link)}').then(()=>toast('لینک کپی شد','ok'))" title="کپی لینک"><i class="ti ti-copy"></i></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText('${esc(l.sub_url)}').then(()=>toast('Sub کپی شد','ok'))" title="Sub URL"><i class="ti ti-rss"></i></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="showQR('${esc(l.vless_link)}')" title="QR"><i class="ti ti-qrcode"></i></button>
        <button class="btn btn-sm btn-amber btn-icon" onclick="openEditLink('${l.uuid}')" title="ویرایش"><i class="ti ti-edit"></i></button>
        <button class="btn btn-sm btn-g btn-icon" onclick="resetUsage('${l.uuid}')" title="ریست مصرف"><i class="ti ti-rotate"></i></button>
        <button class="btn btn-sm btn-d btn-icon" onclick="deleteLink('${l.uuid}')" title="حذف"><i class="ti ti-trash"></i></button>
      </div>
    </div>
  </div>`;
}).join('');
  }catch(e){console.error(e)}
}
function selectedConfigIds(){return Array.from(document.querySelectorAll('.bulk-config-check:checked')).map(el=>el.value)}
function selectAllConfigs(checked){document.querySelectorAll('.bulk-config-check').forEach(el=>el.checked=!!checked);updateBulkSelection()}
function updateBulkSelection(){const ids=selectedConfigIds();const count=document.getElementById('bulk-selected-count');if(count)count.textContent=toFa(ids.length)+' انتخاب';const all=document.getElementById('bulk-select-all');if(all){const checks=Array.from(document.querySelectorAll('.bulk-config-check'));all.checked=checks.length>0&&checks.every(x=>x.checked);all.indeterminate=checks.some(x=>x.checked)&&!all.checked;}}
async function bulkConfigAction(action){
  const ids=selectedConfigIds();if(!ids.length){toast('ابتدا کانفیگ‌ها را انتخاب کنید','err');return}
  const labels={activate:'فعال‌کردن',deactivate:'غیرفعال‌کردن',reset_usage:'صفرکردن مصرف',delete:'حذف'};
  const warning=action==='delete'?'این '+ids.length+' کانفیگ برای همیشه حذف می‌شوند. ادامه می‌دهید؟':labels[action]+' برای '+ids.length+' کانفیگ اجرا شود؟';
  if(!confirm(warning))return;
  try{const r=await authF('/api/links/bulk',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({action,ids})});const d=await r.json();if(!r.ok)throw new Error(d.detail||'operation failed');toast(toFa(d.changed||0)+' مورد انجام شد ✓','ok');await loadLinks();}catch(e){toast('عملیات گروهی ناموفق بود: '+(e.message||''),'err')}
}

async function createLink(){
  const label=document.getElementById('nl-label').value.trim()||'کانفیگ جدید';
  const val=document.getElementById('nl-val').value;
  const unit=document.getElementById('nl-unit').value;
  const exp=document.getElementById('nl-exp').value;
  const note=document.getElementById('nl-note').value.trim();
  const sub_id=document.getElementById('nl-sub').value||null;
  const protocol=document.getElementById('nl-proto').value||'vless-ws';
  const fingerprint=document.getElementById('nl-fp').value||'chrome';
  const alpn=document.getElementById('nl-alpn').value.trim();
  const port=Number(document.getElementById('nl-port').value)||443;
  const ip_limit=Number(document.getElementById('nl-iplimit').value)||0;
  const speed_limit_value=Number(document.getElementById('nl-speed').value)||0;
  const speed_limit_unit=document.getElementById('nl-speed-unit').value;
  try{
    const category_id=document.getElementById('nl-cat')?document.getElementById('nl-cat').value||null:null;
    const r=await authF('/api/links',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({label,limit_value:val||0,limit_unit:unit,expires_days:exp||0,note,sub_id,category_id,protocol,fingerprint,alpn,port,ip_limit,speed_limit_value,speed_limit_unit})});
    if(!r.ok)throw new Error('failed');
    ['nl-label','nl-val','nl-exp','nl-note','nl-alpn'].forEach(id=>document.getElementById(id).value='');
    document.getElementById('nl-port').value='443';
    document.getElementById('nl-iplimit').value='0';
    document.getElementById('nl-speed').value='0';
    document.getElementById('nl-alpn-preset').value='';
    document.getElementById('nl-alpn').style.display='none';
    toast('کانفیگ ساخته شد ✓','ok');loadLinks();
  }catch(e){toast('خطا در ساخت','err')}
}
function openEditLink(uuid){
  const l=allLinksList.find(x=>x.uuid===uuid);
  if(!l)return;
  document.getElementById('el-uuid').value=uuid;
  document.getElementById('el-label').value=l.label;
  document.getElementById('el-note').value=l.note||'';
  if(l.limit_bytes===0){document.getElementById('el-val').value='';document.getElementById('el-unit').value='GB';}
  else{document.getElementById('el-val').value=(l.limit_bytes/1024/1024).toFixed(0);document.getElementById('el-unit').value='MB';}
  document.getElementById('el-exp').value='';
  document.getElementById('el-fp').value=l.fingerprint||'chrome';
  document.getElementById('el-alpn').value=l.alpn||'';
  document.getElementById('el-port').value=l.port||443;
  document.getElementById('el-iplimit').value=l.ip_limit||0;
  if(!l.speed_limit_bytes){document.getElementById('el-speed').value='0';document.getElementById('el-speed-unit').value='MBIT';}
  else{document.getElementById('el-speed').value=(l.speed_limit_bytes*8/1024/1024).toFixed(2);document.getElementById('el-speed-unit').value='MBIT';}
  openModal('modal-edit-link');
}
async function saveEditLink(){
  const uuid=document.getElementById('el-uuid').value;
  const label=document.getElementById('el-label').value.trim();
  const note=document.getElementById('el-note').value.trim();
  const val=document.getElementById('el-val').value;
  const unit=document.getElementById('el-unit').value;
  const exp=document.getElementById('el-exp').value;
  const fingerprint=document.getElementById('el-fp').value||'chrome';
  const alpn=document.getElementById('el-alpn').value.trim();
  const port=Number(document.getElementById('el-port').value)||443;
  const ip_limit=Number(document.getElementById('el-iplimit').value)||0;
  const speed_limit_value=Number(document.getElementById('el-speed').value)||0;
  const speed_limit_unit=document.getElementById('el-speed-unit').value;
  const body={label,note,limit_value:val||0,limit_unit:unit,fingerprint,alpn,port,ip_limit,speed_limit_value,speed_limit_unit};
  if(exp&&Number(exp)>0)body.expires_days=Number(exp);
  try{
    const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    if(!r.ok)throw new Error();
    closeModal('modal-edit-link');
    toast('کانفیگ ویرایش شد ✓','ok');loadLinks();
  }catch(e){toast('خطا در ویرایش','err')}
}
async function toggleActive(uuid,newState){
  try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({active:newState})});if(!r.ok)throw new Error();toast(newState?'فعال شد ✓':'غیرفعال شد','ok');loadLinks();}catch(e){toast('خطا','err')}
}
async function resetUsage(uuid){
  try{const r=await authF('/api/links/'+uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({reset_usage:true})});if(!r.ok)throw new Error();toast('مصرف ریست شد ✓','ok');loadLinks();}catch(e){toast('خطا','err')}
}
async function deleteLink(uuid){
  if(!confirm('حذف این کانفیگ؟'))return;
  try{const r=await authF('/api/links/'+uuid,{method:'DELETE'});if(!r.ok)throw new Error();toast('حذف شد ✓','ok');loadLinks();}catch(e){toast('خطا','err')}
}
function showQR(link){document.getElementById('qr-img').src='/api/qr?data='+encodeURIComponent(link);document.getElementById('qr-modal').classList.add('open')}
let allSubsRaw=[];
async function loadSubs(){
  try{
    const r=await authF('/api/subs'),d=await r.json();
    const subs=d.subs||[];
    allSubsRaw=subs;
    document.getElementById('subs-nb').textContent=subs.length;
    document.getElementById('subs-pg-cnt').textContent=toFa(subs.length)+' گروه';
    renderSubsGrid(subs);
  }catch(e){console.error(e)}
}
function renderSubsGrid(subs){
  const grid=document.getElementById('subs-grid');
  if(!subs.length){
    grid.innerHTML='<div class="subs-empty-v2"><div class="subs-empty-v2-icon"><i class="ti ti-folders"></i></div><div class="subs-empty-v2-title">هنوز گروهی وجود ندارد</div><div class="subs-empty-v2-sub">یک گروه جدید بسازید تا کانفیگ‌ها را دسته‌بندی کنید</div></div>';
    return;
  }
  grid.innerHTML=subs.map(s=>`
    <div class="sub-card">
      <div class="sub-card-top">
        <div class="sub-card-head-v2">
          <div class="sub-card-icon"><i class="ti ti-folder"></i></div>
          <div class="sub-card-titles">
            <div class="sub-card-name-v2">${esc(s.name)}</div>
            ${s.desc?`<div class="sub-card-desc-v2">${esc(s.desc)}</div>`:'<div class="sub-card-desc-v2" style="opacity:.5">بدون توضیحات</div>'}
          </div>
          <div class="sub-card-lock-badge ${s.has_password?'locked':'open'}" title="${s.has_password?'رمزدار':'پابلیک'}">
            <i class="ti ${s.has_password?'ti-lock':'ti-lock-open'}"></i>
          </div>
        </div>
        <div class="sub-card-stats">
          <div class="sub-card-stat"><div class="sub-card-stat-val">${toFa(s.links_count)}</div><div class="sub-card-stat-label">کانفیگ</div></div>
          <div class="sub-card-stat"><div class="sub-card-stat-val" style="color:var(--green-t)">${toFa(s.active_count)}</div><div class="sub-card-stat-label">فعال</div></div>
          <div class="sub-card-stat"><div class="sub-card-stat-val" style="font-size:12px">${esc(s.total_used_fmt)}</div><div class="sub-card-stat-label">مصرف</div></div>
        </div>
      </div>
      <div class="sub-card-url-row">
        <span class="sub-card-url-text" title="صفحه پابلیک">${esc(s.public_url)}</span>
        <button class="sub-card-url-copy" onclick="navigator.clipboard.writeText('${esc(s.public_url)}').then(()=>toast('لینک پابلیک کپی شد','ok'))" title="کپی پابلیک"><i class="ti ti-copy"></i></button>
        <button class="sub-card-url-copy" onclick="window.open('${esc(s.public_url)}','_blank')" title="باز کردن"><i class="ti ti-external-link"></i></button>
      </div>
      <div class="sub-card-url-row" style="margin-top:6px">
        <span class="sub-card-url-text" style="color:var(--purple-t)" title="لینک ساب (base64)">${esc(s.sub_url)}</span>
        <button class="sub-card-url-copy" onclick="navigator.clipboard.writeText('${esc(s.sub_url)}').then(()=>toast('لینک ساب کپی شد','ok'))" title="کپی ساب"><i class="ti ti-rss"></i></button>
        <button class="sub-card-url-copy" onclick="showQR('${esc(s.sub_url)}')" title="QR ساب"><i class="ti ti-qrcode"></i></button>
      </div>
      <div class="sub-card-bottom">
        <button class="btn btn-sm btn-g" onclick="openSubLinks('${esc(s.sub_id)}','${esc(s.name)}')"><i class="ti ti-link-plus"></i> کانفیگ‌ها</button>
        <button class="btn btn-sm btn-o" onclick="navigator.clipboard.writeText('${esc(s.sub_url)}').then(()=>toast('لینک ساب کپی شد','ok'))"><i class="ti ti-rss"></i> ساب</button>
        <button class="btn btn-sm btn-g btn-icon" onclick="showQR('${esc(s.sub_url)}')" title="QR"><i class="ti ti-qrcode"></i></button>
        <button class="btn btn-sm btn-d btn-icon" onclick="deleteSub('${esc(s.sub_id)}')" title="حذف"><i class="ti ti-trash"></i></button>
      </div>
    </div>
  `).join('');
}
function filterSubs(q){
  q=q.trim().toLowerCase();
  if(!q){renderSubsGrid(allSubsRaw);return}
  renderSubsGrid(allSubsRaw.filter(s=>s.name.toLowerCase().includes(q)||(s.desc||'').toLowerCase().includes(q)));
}
async function createSub(){
  const name=document.getElementById('ns-name').value.trim()||'گروه جدید';
  const desc=document.getElementById('ns-desc').value.trim();
  const pw=document.getElementById('ns-pw').value;
  try{
    const r=await authF('/api/subs',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name,desc,password:pw})});
    if(!r.ok)throw new Error('failed');
    ['ns-name','ns-desc','ns-pw'].forEach(id=>document.getElementById(id).value='');
    closeModal('modal-create-sub');
    toast('گروه ساخته شد ✓','ok');loadSubs();
  }catch(e){toast('خطا در ساخت گروه','err')}
}

function qsUpdatePreview(){
  const el=document.getElementById('qs-preview');if(!el)return;
  const vol=parseFloat(document.getElementById('ns-vol').value)||0;
  const days=parseInt(document.getElementById('ns-days').value)||0;
  const ip=parseInt(document.getElementById('ns-iplimit').value)||0;
  const parts=[];
  parts.push(vol>0?('💡 حجم مشترک: <b>'+vol+' GB</b> بین ۲۴ کانفیگ = '+( (vol/24).toFixed(2) )+' GB هر کانفیگ'):'💡 حجم <b>نامحدود</b>');
  parts.push(days>0?('⏱ اعتبار: <b>'+days+' روز</b>'):'⏱ بدون انقضا');
  parts.push(ip>0?('📱 حداکثر <b>'+ip+' کاربر</b> هم‌زمان'):'📱 کاربر نامحدود');
  el.innerHTML=parts.join(' &nbsp;•&nbsp; ');
}
['ns-vol','ns-days','ns-iplimit'].forEach(id=>{
  const e=document.getElementById(id);if(e)e.addEventListener('input',qsUpdatePreview);
});

async function createSubQuick(){
  const name=document.getElementById('ns-name').value.trim()||'گروه سریع';
  const desc=document.getElementById('ns-desc').value.trim();
  const pw=document.getElementById('ns-pw').value;
  const volRaw=document.getElementById('ns-vol').value.trim();
  const daysRaw=document.getElementById('ns-days').value.trim();
  const ipRaw=document.getElementById('ns-iplimit').value.trim();
  const vol=volRaw===''?0:Number(volRaw);
  const days=daysRaw===''?0:Number(daysRaw);
  const ipLimit=ipRaw===''?0:Number(ipRaw);
  const totalLimitBytes=vol>0?Math.round(vol*1024*1024*1024):0;
  if(!Number.isFinite(vol)||!Number.isFinite(days)||!Number.isFinite(ipLimit)||
     vol<0||days<0||ipLimit<0||!Number.isFinite(totalLimitBytes)||
     !Number.isInteger(days)||!Number.isInteger(ipLimit)){
    toast('مقادیر واردشده معتبر نیستند','err');return;
  }
  if(days>3650||ipLimit>100){toast('روزها حداکثر ۳۶۵۰ و IP حداکثر ۱۰۰ است','err');return;}
  if(totalLimitBytes>0&&totalLimitBytes<1024*1024){toast('حجم مشترک حداقل ۱ مگابایت باید باشد','err');return;}

  const btn=document.querySelector('#modal-create-sub .modal-v2-footer .btn-pur');
  const original=btn?btn.innerHTML:'';
  if(btn){btn.disabled=true;btn.innerHTML='<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> ساخت یک‌مرحله‌ای...';}
  try{
    // The backend creates the group, sets quota/expiry, and stores all 24 links
    // in one in-memory transaction followed by a single durable save.
    const r=await authF('/api/subs/quick',{
      method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({name,desc,password:pw,total_limit_bytes:totalLimitBytes,days,ip_limit:ipLimit,speed_limit_bytes:0})
    });
    const data=await r.json().catch(()=>({}));
    if(!r.ok||!data.ok)throw new Error(data.detail||data.message||'ساخت گروه ناموفق بود');
    closeModal('modal-create-sub');
    document.getElementById('ns-pw').value='';
    toast('گروه و '+toFa(data.count||24)+' کانفیگ با یک ذخیره ساخته شد ✓','ok');
    await Promise.all([loadSubs(),loadLinks()]);
    if(data.sub_url&&confirm('گروه ساخته شد. لینک سابسکریپشن کپی شود؟')){
      try{await navigator.clipboard.writeText(data.sub_url);toast('لینک سابسکریپشن کپی شد ✓','ok');}
      catch(e){prompt('لینک سابسکریپشن',data.sub_url);}
    }
  }catch(e){
    toast(e.message||'خطا در ساخت سریع','err');
  }finally{
    if(btn){btn.disabled=false;btn.innerHTML=original||'<i class="ti ti-magic-wand"></i> ساخت گروه + ۲۴ کانفیگ';}
  }
}
async function deleteSub(sub_id){
  if(!confirm('این گروه و فقط کانفیگ‌های وابسته به همین گروه حذف می‌شوند. کانفیگ‌های گروه‌های دیگر باقی می‌مانند. ادامه می‌دهید؟'))return;
  try{const r=await authF('/api/subs/'+sub_id,{method:'DELETE'});if(!r.ok)throw new Error();toast('گروه حذف شد ✓','ok');loadSubs();loadLinks();}catch(e){toast('خطا','err')}
}
let lmodalLinks=[],lmodalInSub=new Set();
async function openSubLinks(sub_id,name){
  currentSubId=sub_id;
  document.getElementById('modal-sub-name').textContent=name;
  document.getElementById('modal-links-body').innerHTML='<div style="color:var(--t3);font-size:12px;padding:20px;text-align:center"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite;font-size:20px"></i></div>';
  document.getElementById('lmodal-search-inp').value='';
  openModal('modal-links');
  try{
    const [lr,sr]=await Promise.all([authF('/api/links'),authF('/api/subs')]);
    const {links=[]}=await lr.json();
    const {subs=[]}=await sr.json();
    const thisSub=subs.find(s=>s.sub_id===sub_id);
    lmodalInSub=new Set(thisSub?.link_ids||[]);
    lmodalLinks=links;
    renderLmodalList(links);
  }catch(e){toast('خطا در بارگذاری','err')}
}
function renderLmodalList(links){
  const body=document.getElementById('modal-links-body');
  if(!links.length){body.innerHTML='<div class="empty" style="padding:30px"><i class="ti ti-link-off"></i><p>هنوز کانفیگی وجود ندارد</p></div>';updateLmodalCount();return}
  body.innerHTML=links.map(l=>{
    const checked=lmodalInSub.has(l.uuid);
    const on=l.active&&!l.expired;
    const vlink=l.vless_link||'';
    const surl=l.sub_url||'';
    return `<div class="lrow-v2 ${checked?'checked':''}" data-uuid="${l.uuid}" data-name="${esc(l.label).toLowerCase()}" onclick="toggleLrow('${l.uuid}',this)">
      <div class="lrow-v2-check"><i class="ti ti-check"></i></div>
      <div class="lrow-v2-avatar"><i class="ti ti-key"></i></div>
      <div class="lrow-v2-info">
        <div class="lrow-v2-name">${esc(l.label)}</div>
        <div class="lrow-v2-meta"><i class="ti ti-database" style="font-size:10px"></i> ${fmtB(l.used_bytes)}</div>
        <div class="lrow-links">
          <button class="lrow-link-btn" onclick="event.stopPropagation();navigator.clipboard.writeText('${esc(vlink)}').then(()=>toast('لینک کپی شد','ok'))" title="کپی لینک VLESS"><i class="ti ti-copy"></i><span>لینک</span></button>
          <button class="lrow-link-btn" onclick="event.stopPropagation();navigator.clipboard.writeText('${esc(surl)}').then(()=>toast('ساب کپی شد','ok'))" title="کپی Sub URL"><i class="ti ti-rss"></i><span>ساب</span></button>
          <button class="lrow-link-btn" onclick="event.stopPropagation();showQR('${esc(vlink)}')" title="QR کد"><i class="ti ti-qrcode"></i><span>QR</span></button>
        </div>
      </div>
      <span class="lrow-v2-status ${on?'on':'off'}">${on?'فعال':'غیرفعال'}</span>
    </div>`;
  }).join('');
  updateLmodalCount();
}
function toggleLrow(uuid,el){
  if(lmodalInSub.has(uuid)){lmodalInSub.delete(uuid);el.classList.remove('checked')}
  else{lmodalInSub.add(uuid);el.classList.add('checked')}
  updateLmodalCount();
}
function lmodalSelectAll(state){
  lmodalLinks.forEach(l=>{if(state)lmodalInSub.add(l.uuid);else lmodalInSub.delete(l.uuid)});
  renderLmodalList(lmodalLinks);
}
function updateLmodalCount(){
  const el=document.getElementById('lmodal-count');
  if(el)el.textContent=toFa(lmodalInSub.size)+' انتخاب شده';
}
function filterLmodal(q){
  q=q.trim().toLowerCase();
  document.querySelectorAll('#modal-links-body .lrow-v2').forEach(row=>{
    row.style.display = !q || row.dataset.name.includes(q) ? '' : 'none';
  });
}
async function saveSubLinks(){
  if(!currentSubId)return;
  const link_ids=[...lmodalInSub];
  try{
    const r=await authF('/api/subs/'+currentSubId,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({link_ids})});
    if(!r.ok)throw new Error();
    await Promise.all(lmodalLinks.map(l=>
      authF('/api/links/'+l.uuid,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify({sub_id:lmodalInSub.has(l.uuid)?currentSubId:null})})
    ));
    closeModal('modal-links');
    toast('کانفیگ‌های گروه ذخیره شدند ✓','ok');
    loadSubs();loadLinks();
  }catch(e){toast('خطا در ذخیره','err')}
}
async function loadSubsPage(){
  document.getElementById('sub-all-url').textContent=location.protocol+'//'+location.host+'/sub-all';
  try{
    const r=await authF('/api/subs'),d=await r.json();
    const subs=d.subs||[];
    const sbc=document.getElementById('sb-count');if(sbc)sbc.textContent=toFa(subs.length);
    const sbl=document.getElementById('sb-links');if(sbl)sbl.textContent=toFa(subs.reduce((a,s)=>a+(s.links_count||0),0));
    const el=document.getElementById('sub-groups-list');
    if(!subs.length){el.innerHTML='<div class="empty"><i class="ti ti-rss-off"></i><p>هنوز گروهی ندارید</p></div>';return}
    el.innerHTML=subs.map(s=>`
      <div style="padding:13px 15px;background:var(--accent-d);border:1px solid var(--card-b);border-radius:10px;margin-bottom:8px;display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap">
        <div>
          <div style="font-weight:700;font-size:13px;margin-bottom:3px">${esc(s.name)}</div>
          <div style="font-family:ui-monospace,monospace;font-size:10px;color:#34D399">${esc(s.sub_url)}</div>
          <div style="font-size:10px;color:var(--t3);margin-top:3px">${toFa(s.links_count)} کانفیگ · ${esc(s.total_used_fmt)} مصرف ${s.has_password?'· 🔒 رمزدار':''}</div>
        </div>
        <div style="display:flex;gap:5px;flex-wrap:wrap">
          <button class="btn btn-sm btn-pur" onclick="navigator.clipboard.writeText('${esc(s.sub_url)}').then(()=>toast('کپی شد','ok'))"><i class="ti ti-copy"></i> ساب</button>
          <button class="btn btn-sm btn-pur" onclick="navigator.clipboard.writeText('${esc(s.public_url)}').then(()=>toast('کپی شد','ok'))"><i class="ti ti-globe"></i> پابلیک</button>
          <button class="btn btn-sm btn-g" onclick="showQR('${esc(s.sub_url)}')"><i class="ti ti-qrcode"></i></button>
        </div>
      </div>
    `).join('');
  }catch(e){}
}
function cpSubAll(){navigator.clipboard.writeText(location.protocol+'//'+location.host+'/sub-all').then(()=>toast('کپی شد ✓','ok'))}
function parseBytesFmt(s){
  if(!s)return 0;
  const m=String(s).match(/([\d.]+)\s*([A-Za-z]+)/);
  if(!m)return 0;
  const n=parseFloat(m[1]),u=m[2].toUpperCase();
  const mult={B:1,KB:1024,MB:1024**2,GB:1024**3,TB:1024**4};
  return n*(mult[u]||1);
}
async function loadConns(){
  try{
    const r=await authF('/api/connections'),d=await r.json();
    const grid=document.getElementById('conns-grid'),ce=document.getElementById('conns-empty');
    updateConnsBadge(d.count);
    document.getElementById('ch-count').textContent=toFa(d.count);
    const conns=d.connections||[];
    if(!d.count){
      grid.innerHTML='';ce.style.display='block';
      document.getElementById('ch-traffic').textContent='—';
      document.getElementById('ch-avgdur').textContent='—';
      document.getElementById('ch-uniq').textContent='—';
      return;
    }
    ce.style.display='none';
    const totalBytes=conns.reduce((s,c)=>s+parseBytesFmt(c.bytes_fmt),0);
    document.getElementById('ch-traffic').textContent=fmtB(totalBytes);
    const uniqIps=new Set(conns.map(c=>c.ip)).size;
    document.getElementById('ch-uniq').textContent=toFa(uniqIps);
    const durs=conns.map(c=>c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0);
    const avgSec=durs.length?Math.floor(durs.reduce((a,b)=>a+b,0)/durs.length):0;
    document.getElementById('ch-avgdur').textContent=avgSec<60?avgSec+' ث':avgSec<3600?Math.floor(avgSec/60)+' د':Math.floor(avgSec/3600)+' س';
    const maxDur=Math.max(...durs,1);
    grid.innerHTML=conns.map(c=>{
      const secs=c.connected_at?Math.max(0,Math.floor((Date.now()-new Date(c.connected_at).getTime())/1000)):0;
      const dur=secs<60?secs+' ثانیه':secs<3600?Math.floor(secs/60)+' دقیقه':Math.floor(secs/3600)+' ساعت';
      const durPct=Math.min(100,Math.round((secs/maxDur)*100));
      const protoVal=c.transport==='vless-ws'?'vless-ws':(c.transport||'').replace('xhttp-','xhttp-');
      return `<div class="conn-card-v2">
        <div class="conn-card-v2-glow"></div>
        <div class="conn-card-v2-top">
          <div class="conn-avatar"><i class="ti ti-device-desktop"></i></div>
          <div class="conn-card-v2-id">
            <div class="conn-ip-v2">${esc(c.ip)}
              <button class="conn-ip-copy" onclick="navigator.clipboard.writeText('${esc(c.ip)}').then(()=>toast('IP کپی شد','ok'))" title="کپی IP"><i class="ti ti-copy"></i></button>
            </div>
            <div class="conn-label-v2">${esc(c.label)}</div>
          </div>
          <span class="conn-status-pill"><span class="dot dg pulse"></span> زنده</span>
        </div>
        <div class="conn-card-v2-divider"></div>
        <div class="conn-card-v2-body">
          <div class="conn-proto-row">${protoBadge(protoVal)}</div>
          <div class="conn-stat-row">
            <div class="conn-stat-box">
              <div class="conn-stat-icon"><i class="ti ti-transfer"></i></div>
              <div>
                <div class="conn-stat-text-label">ترافیک</div>
                <div class="conn-stat-text-val">${esc(c.bytes_fmt)}</div>
              </div>
            </div>
            <div class="conn-stat-box">
              <div class="conn-stat-icon time"><i class="ti ti-clock"></i></div>
              <div>
                <div class="conn-stat-text-label">مدت اتصال</div>
                <div class="conn-stat-text-val">${dur}</div>
              </div>
            </div>
          </div>
          <div class="conn-duration-track"><div class="conn-duration-fill" style="width:${durPct}%"></div></div>
        </div>
      </div>`;
    }).join('');
  }catch(e){console.error(e)}
}
async function loadErrs(){try{const r=await authF('/stats'),d=await r.json();renderErrs(d.recent_errors||[]);
  const ec=document.getElementById('er-count');if(ec)ec.textContent=toFa(d.recent_errors?d.recent_errors.length:0);
  const el=document.getElementById('er-last'),elt=document.getElementById('er-last-time');
  if(d.recent_errors&&d.recent_errors.length){const e0=d.recent_errors[d.recent_errors.length-1];if(el)el.textContent=String(e0.message||e0).slice(0,40);if(elt)elt.textContent=new Date(e0.time||Date.now()).toLocaleString('fa-IR');}
  else{if(el)el.textContent='بدون خطا';if(elt)elt.textContent='سیستم پایدار'}
}catch(e){}}
async function loadSetServer(){
  try{
    const r=await authF('/stats'),d=await r.json();
    const el=document.getElementById('set-server');if(!el)return;
    const rows=[['نسخه پنل','𝑭𝒊𝒏𝒆𝑽𝑷𝑵 v1.0.0'],['آپتایم',String(d.uptime||'—')],['اتصالات فعال',toFa(d.active_connections||0)],['کل کانفیگ‌ها',toFa(d.links_count||0)],['گروه‌های ساب',toFa(d.subs_count||0)],['کل ترافیک',(d.total_traffic_mb||0).toFixed(2)+' MB']];
    el.innerHTML='<div class="log-timeline">'+rows.map(k=>'<div class="log-item"><div class="log-ic info"><i class="ti ti-dot"></i></div><div class="log-body" style="display:flex;justify-content:space-between;align-items:center"><span class="log-msg">'+k[0]+'</span><b style="color:var(--t1);font-size:12px">'+k[1]+'</b></div></div>').join('')+'</div>';
    const up=document.getElementById('st-uptime');if(up)up.textContent=String(d.uptime||'—');
    try{const sr=await authF('/api/system'),sd=await sr.json();const hostEl=document.getElementById('server-public-host');if(hostEl)hostEl.textContent=sd.public_host||location.host||'—';}catch(hostErr){}
    // persistence panel (public /health — no auth needed, but reuse cookie)
    try{
      const hr=await authF('/health'),hv=await hr.json();
      const vel=document.getElementById('set-volume');
      if(vel&&hv&&hv.volume){
        const v=hv.volume, ok=v.mounted&&v.writable;
        if(ok){
          // volume active → hide this panel entirely
          const panel=vel.closest('.sec-panel'); if(panel) panel.style.display='none';
        }else{
          vel.innerHTML='<div class="vol-steps">'
            +'<div class="vol-step"><div class="vs-n"><i class="ti ti-alert-triangle" style="font-size:13px"></i></div><div><b>ولوم دائمی متصل نیست</b><div class="vs-s">داده‌ها روی فضای موقت هستند و ممکن است بعد از استقرار مجدد از بین بروند — کانفیگ‌ها، گروه‌ها و مصرف حجم مشترک.</div></div></div>'
            +'</div>'
            +'<div class="vol-note"><i class="ti ti-alert-triangle"></i> برای فعال‌سازی: در تنظیمات پلتفرم، یک Volume پایدار بسازید و به این سرویس متصل کنید<br>· <b>نام ولیم (Volume name):</b> <code dir="ltr">panel_data</code><br>· <b>Mount Path:</b> <code dir="ltr">/data</code><br>سپس سرویس را دوباره Deploy کنید و وضعیت ذخیره‌سازی را بررسی کنید.</div>';
        }
      }
    }catch(e2){}
  }catch(e){}
}


async function fetchDefaultVless(){
  try{const r=await authF('/api/links'),d=await r.json();const links=d.links||[];const def=links.find(l=>l.limit_bytes===0&&l.active&&!l.expired)||links.find(l=>l.active&&!l.expired)||links[0];document.getElementById('vless-main').textContent=def?def.vless_link:'هنوز کانفیگی وجود ندارد';}catch(e){}
}
function cpText(id){navigator.clipboard.writeText(document.getElementById(id).textContent).then(()=>toast('کپی شد ✓','ok'))}
function qrFor(id){showQR(document.getElementById(id).textContent)}
function refreshAll(){fetchStats();fetchDefaultVless();loadLinks();if(document.getElementById('pg-subgroups').classList.contains('on'))loadSubs();if(document.getElementById('pg-subscriptions').classList.contains('on'))loadSubsPage();if(document.getElementById('pg-connections').classList.contains('on'))loadConns();if(document.getElementById('pg-logs').classList.contains('on'))loadActivity();toast('رفرش شد','ok')}

function togglePwField(id,btn){
  const inp=document.getElementById(id);
  const icon=btn.querySelector('i');
  const toText=inp.type==='password';
  inp.type=toText?'text':'password';
  icon.className='ti '+(toText?'ti-eye-off':'ti-eye');
}

function makeGradient(ctx,color1,color2){
  const g=ctx.createLinearGradient(0,0,0,260);
  g.addColorStop(0,color1);g.addColorStop(1,color2);
  return g;
}
function initCharts(){
  if(typeof Chart==='undefined')return;
  const cv1=document.getElementById('ch1');if(!cv1)return;
  const c1=cv1.getContext('2d');
  const grad1=makeGradient(c1,'rgba(16,185,129,.38)','rgba(16,185,129,0)');
  const opts={
    responsive:true,maintainAspectRatio:false,
    interaction:{mode:'index',intersect:false},
    plugins:{
      legend:{display:false},
      tooltip:{
        backgroundColor:'rgba(13,27,46,.96)',borderColor:'rgba(16,185,129,.3)',borderWidth:1,
        titleColor:'#E8F4FF',bodyColor:'#7BAED4',padding:11,cornerRadius:10,displayColors:false,
        titleFont:{family:'Vazirmatn',size:11,weight:'700'},bodyFont:{family:'Vazirmatn',size:11},
        callbacks:{label:v=>`${v.parsed.y.toFixed(2)} مگابایت`}
      }
    },
    scales:{
      x:{grid:{display:false},border:{display:false},ticks:{color:'#3D6B8E',font:{size:9,family:'Vazirmatn'}}},
      y:{grid:{color:'rgba(16,185,129,.06)'},border:{display:false},ticks:{color:'#3D6B8E',font:{size:9,family:'Vazirmatn'},callback:v=>v+' MB'}}
    },
    elements:{line:{capBezierPoints:true}}
  };
  const ds1={label:'MB',data:[],borderColor:'#10B981',backgroundColor:grad1,fill:true,tension:.42,pointRadius:0,pointHoverRadius:6,pointHoverBackgroundColor:'#10B981',pointHoverBorderColor:'#fff',pointHoverBorderWidth:2,borderWidth:2.5};
  ch1=new Chart(document.getElementById('ch1'),{type:'line',data:{labels:[],datasets:[ds1]},options:opts});

  function makeGradientV2(ctx,c1,c2,c3){
    const g=ctx.createLinearGradient(0,0,0,320);
    g.addColorStop(0,c1);g.addColorStop(.6,c2);g.addColorStop(1,c3);
    return g;
  }
  const c3ctx=document.getElementById('ch3').getContext('2d');
  const gradFill3=makeGradientV2(c3ctx,'rgba(16,185,129,.45)','rgba(16,185,129,.08)','rgba(16,185,129,0)');
  ch3=new Chart(document.getElementById('ch3'),{
    type:'line',
    data:{labels:[],datasets:[
      {label:'مصرف',data:[],borderColor:'#10B981',backgroundColor:gradFill3,fill:true,tension:.45,pointRadius:0,pointHoverRadius:7,pointHoverBackgroundColor:'#fff',pointHoverBorderColor:'#10B981',pointHoverBorderWidth:3,borderWidth:3,order:2},
      {label:'میانگین',data:[],borderColor:'#F59E0B',borderDash:[6,5],borderWidth:1.6,pointRadius:0,fill:false,tension:0,order:1}
    ]},
    options:{
      responsive:true,maintainAspectRatio:false,
      interaction:{mode:'index',intersect:false},
      plugins:{
        legend:{display:false},
        tooltip:{
          backgroundColor:'rgba(13,27,46,.97)',borderColor:'rgba(16,185,129,.35)',borderWidth:1,
          titleColor:'#E8F4FF',bodyColor:'#9DC3E8',padding:13,cornerRadius:12,displayColors:true,boxPadding:4,
          titleFont:{family:'Vazirmatn',size:11.5,weight:'700'},bodyFont:{family:'Vazirmatn',size:11},
          callbacks:{label:v=>` ${v.dataset.label}: ${v.parsed.y.toFixed(2)} MB`}
        }
      },
      scales:{
        x:{grid:{display:false},border:{display:false},ticks:{color:'#3D6B8E',font:{size:9.5,family:'Vazirmatn'},maxRotation:0}},
        y:{grid:{color:'rgba(16,185,129,.05)'},border:{display:false},ticks:{color:'#3D6B8E',font:{size:9.5,family:'Vazirmatn'},callback:v=>v+' MB'}}
      }
    }
  });

  const cv2=document.getElementById('ch2');if(!cv2)return;
  ch2=new Chart(cv2,{
    type:'bar',
    data:{labels:[],datasets:[{
      data:[],
      backgroundColor:['#38bdf8','#a78bfa','#20d7a0','#f5bd5a'],
      borderRadius:8,
      barThickness:26,
      maxBarThickness:34
    }]},
    options:{
      indexAxis:'y',
      responsive:true,maintainAspectRatio:false,
      plugins:{
        legend:{display:false},
        tooltip:{backgroundColor:'rgba(13,27,46,.96)',borderColor:'rgba(16,185,129,.3)',borderWidth:1,padding:10,cornerRadius:10,bodyFont:{family:'Vazirmatn'},titleFont:{family:'Vazirmatn'}}
      }
    }
  });
}
let ws;
function wsLog(c,m){const l=document.getElementById('ws-log'),p=document.createElement('p');const colors={ok:'#34D399',err:'#F87171',info:'#7BAED4',sent:'#FCD34D'};p.style.color=colors[c]||'#fff';p.textContent='['+new Date().toLocaleTimeString('fa-IR')+'] '+m;l.appendChild(p);l.scrollTop=l.scrollHeight}
function wsConn(){const u=document.getElementById('ws-uuid').value.trim();if(!u){toast('UUID را وارد کنید','err');return}const url=(location.protocol==='https:'?'wss':'ws')+'://'+location.host+'/ws/'+u;wsLog('info','اتصال: '+url);ws=new WebSocket(url);ws.onopen=()=>wsLog('ok','✓ متصل - UUID معتبر');ws.onerror=()=>wsLog('err','✗ خطا - UUID نامعتبر یا غیرفعال');ws.onmessage=m=>wsLog('info','دریافت '+(m.data.size||m.data.length)+' byte');ws.onclose=e=>wsLog('err','قطع ('+e.code+')'+(e.code===1008?' - دسترسی رد شد':''))}
function wsSend(){const m=document.getElementById('ws-msg').value;if(!m||!ws||ws.readyState!==1)return;ws.send(m);wsLog('sent','ارسال: '+m);document.getElementById('ws-msg').value=''}
function wsDisc(){if(window.ws)window.ws.close()}
document.addEventListener('DOMContentLoaded',async()=>{
  await checkAuth();
  const sau=document.getElementById('sub-all-url');if(sau)sau.textContent=location.protocol+'//'+location.host+'/sub-all';
  loadSetServer();
  fetchStats();fetchDefaultVless();loadLinks();loadSubs();
  setInterval(fetchStats,4000);
  setInterval(()=>{
    if(document.getElementById('pg-links').classList.contains('on'))loadLinks();
    if(document.getElementById('pg-subgroups').classList.contains('on')&&!document.querySelector('.sub-exp-card.open'))loadSubs();
    if(document.getElementById('pg-subscriptions').classList.contains('on'))loadSubsPage();
    if(document.getElementById('pg-connections').classList.contains('on'))loadConns();
    if(document.getElementById('pg-logs').classList.contains('on'))loadActivity();
  },5000);
});

async function quickSubCreate(){
  const btn=document.getElementById('qs-submit-btn');
  const resBox=document.getElementById('qs-result');
  const linkInp=document.getElementById('qs-pub-link');
  const name=(document.getElementById('qs-name')?.value||'').trim()||'ساب گروه جدید';
  const rawVol=(document.getElementById('qs-vol')?.value||'').trim();
  const rawDays=(document.getElementById('qs-days')?.value||'').trim();
  const rawIp=(document.getElementById('qs-ip')?.value||'').trim();
  const volGb=rawVol===''?0:Number(rawVol);
  const days=rawDays===''?0:Number(rawDays);
  const ipLimit=rawIp===''?0:Number(rawIp);
  const totalLimitBytes=volGb>0?Math.round(volGb*1024*1024*1024):0;
  if(!Number.isFinite(volGb)||!Number.isFinite(days)||!Number.isFinite(ipLimit)||
     volGb<0||days<0||ipLimit<0||!Number.isInteger(days)||!Number.isInteger(ipLimit)||
     days>3650||ipLimit>100||!Number.isSafeInteger(totalLimitBytes)){
    toast('مقادیر واردشده معتبر نیستند','err');return;
  }
  if(totalLimitBytes>0&&totalLimitBytes<1024*1024){toast('حجم مشترک حداقل ۱ مگابایت باید باشد','err');return;}
  if(btn?.dataset.busy==='1')return;
  const original=btn?.innerHTML||'';
  if(btn){btn.dataset.busy='1';btn.disabled=true;btn.innerHTML='<i class="ti ti-loader animate-spin"></i> ساخت یک‌مرحله‌ای ۲۴ کانفیگ...';}
  try{
    // One request creates the group, its shared quota and all 24 configs.
    // No serial per-config fallback: partial groups and long waits are avoided.
    const response=await authF('/api/subs/quick',{
      method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({name,desc:'',password:'',total_limit_bytes:totalLimitBytes,days,ip_limit:ipLimit,speed_limit_bytes:0})
    });
    const data=await response.json().catch(()=>({}));
    if(!response.ok||!data.ok||Number(data.count)!==24){
      throw new Error(data.detail||data.message||'ساخت گروه کامل نشد؛ تغییری ناقص ثبت نشد');
    }
    linkInp.value=data.public_url||data.sub_url||'';
    resBox.style.display='block';
    toast('گروه ساب و ۲۴ کانفیگ ساخته شد ✓','ok');
    await Promise.all([loadLinks(),loadSubs()]);
  }catch(err){
    toast('خطا در ساخت ساب: '+(err?.message||'خطای نامشخص'),'err');
  }finally{
    if(btn){btn.dataset.busy='';btn.disabled=false;btn.innerHTML=original||'<i class="ti ti-plus"></i> ساخت گروه ساب + ۲۴ کانفیگ با حجم مشترک';}
  }
}

</script>
</body></html>"""


def get_public_page_html(uuid_key: str) -> str:
    """صفحه پابلیک ساب v3 — طراحی حرفه‌ای‌تر: لینک کانفیگ پنهان با دکمه نمایش، صفحه‌ی رمز با طراحی ویژه"""
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><link rel="icon" href="https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png"><meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>𝑭𝒊𝒏𝒆𝑽𝑷𝑵 — سابسکریپشن</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}}
:root{{
  --bg:#070d0b;--bg2:#0b1613;--bg3:#0f1f1a;
  --card:#0d1c18;--card-b:rgba(16,185,129,0.14);--card-bh:rgba(16,185,129,0.32);
  --accent:#10B981;--accent2:#34D399;--accent-d:rgba(16,185,129,0.12);
  --green:#1FB87E;--green-bg:rgba(31,184,126,0.1);--green-t:#3FD79C;
  --red:#EF4444;--red-bg:rgba(239,68,68,0.1);--red-t:#FB8585;
  --amber:#F2A33D;--amber-bg:rgba(242,163,61,0.1);--amber-t:#F9C988;
  --purple:#9D7BF0;--purple-bg:rgba(157,123,240,0.1);--purple-t:#BCA4F7;
  --t1:#EFF4FF;--t2:#8AA0C4;--t3:#48577A;
  --radius:18px;--shadow:0 12px 40px rgba(0,0,0,0.45);
  --serif:'Vazirmatn',sans-serif;
}}
[data-theme="light"]{{
  --bg:#F0FDF9;--bg2:#E1FBEF;--bg3:#D2F5E6;
  --card:#FFFFFF;--card-b:rgba(16,185,129,0.16);--card-bh:rgba(16,185,129,0.34);
  --accent:#059669;--accent2:#047857;--accent-d:rgba(5,150,105,0.10);
  --green:#0E9A6A;--green-bg:rgba(14,154,106,0.08);--green-t:#0A7553;
  --red:#DC2626;--red-bg:rgba(220,38,38,0.08);--red-t:#A51E1E;
  --amber:#C97A12;--amber-bg:rgba(201,122,18,0.08);--amber-t:#8F5A0C;
  --purple:#7350D6;--purple-bg:rgba(115,80,214,0.08);--purple-t:#5A3CAD;
  --t1:#101A30;--t2:#48577A;--t3:#8694B0;
  --shadow:0 12px 36px rgba(20,40,90,0.12);
}}
html,body{{min-height:100%;overflow-x:hidden;background:var(--bg);font-family:var(--serif);color:var(--t1);font-size:14px;transition:background .35s,color .35s}}
.bg-fx{{position:fixed;inset:0;background:radial-gradient(ellipse 70% 45% at 50% -8%,rgba(16,185,129,0.14),transparent 62%),var(--bg);z-index:0;pointer-events:none;transition:background .35s}}
.grid-fx{{position:fixed;inset:0;background-image:linear-gradient(rgba(16,185,129,0.03) 1px,transparent 1px),linear-gradient(90deg,rgba(16,185,129,0.03) 1px,transparent 1px);background-size:46px 46px;z-index:0;pointer-events:none}}
.wrap{{position:relative;z-index:10;max-width:800px;margin:0 auto;padding:24px 16px 64px}}
.top{{display:flex;align-items:center;justify-content:space-between;margin-bottom:26px;gap:10px}}
.brand{{display:flex;align-items:center;gap:11px;min-width:0}}
.brand-img{{width:40px;height:40px;border-radius:50%;overflow:hidden;border:1px solid var(--card-b);box-shadow:0 0 14px rgba(16,185,129,.35),0 0 8px rgba(16,185,129,.25);flex-shrink:0}}
.brand-img img{{width:100%;height:100%;object-fit:cover}}
.brand-name{{font-size:14.5px;font-weight:800;color:var(--t1);letter-spacing:-.01em}}
.brand-sub{{font-size:9.5px;color:var(--t3);font-weight:500}}
.top-actions{{display:flex;align-items:center;gap:6px;flex-shrink:0}}
.icon-btn{{width:36px;height:36px;border-radius:11px;background:var(--card);border:1px solid var(--card-b);color:var(--t2);display:flex;align-items:center;justify-content:center;font-size:16px;cursor:pointer;transition:.18s}}
.icon-btn:hover{{background:var(--accent-d);color:var(--accent2);border-color:var(--card-bh)}}

.sub-info{{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:24px 24px 22px;margin-bottom:16px;box-shadow:var(--shadow);position:relative;overflow:hidden}}
.sub-info::before{{content:'';position:absolute;top:0;right:0;width:160px;height:160px;background:radial-gradient(circle at top right,rgba(59,124,246,.1),transparent 70%);pointer-events:none}}
.sub-eyebrow{{font-size:10px;font-weight:700;color:var(--accent2);text-transform:uppercase;letter-spacing:.12em;margin-bottom:8px;display:flex;align-items:center;gap:6px}}
.sub-eyebrow i{{font-size:13px}}
.sub-name{{font-size:23px;font-weight:800;color:var(--t1);margin-bottom:6px;letter-spacing:-.02em}}
.sub-desc{{font-size:12.5px;color:var(--t2);line-height:1.8;margin-bottom:14px}}
.sub-meta-row{{font-size:10.5px;color:var(--t3);margin-bottom:14px;display:flex;align-items:center;gap:6px}}
.sub-sub-box{{background:var(--accent-d);border:1px solid var(--card-b);border-radius:13px;padding:12px 14px;display:flex;align-items:center;gap:9px;flex-wrap:wrap}}
.sub-sub-url{{font-family:ui-monospace,monospace;font-size:10px;color:var(--accent2);word-break:break-all;flex:1;min-width:140px}}

.stats-bar{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:18px}}
.stat-card{{background:var(--card);border:1px solid var(--card-b);border-radius:16px;padding:16px 17px;transition:.2s}}
.stat-card:hover{{border-color:var(--card-bh);transform:translateY(-1px)}}
.stat-label{{font-size:9px;color:var(--t3);font-weight:700;text-transform:uppercase;letter-spacing:.07em;margin-bottom:7px}}
.stat-val{{font-size:22px;font-weight:800;color:var(--t1);line-height:1;letter-spacing:-.01em}}
.stat-sub{{font-size:9.5px;color:var(--t3);margin-top:6px}}

.copy-all-bar{{display:flex;align-items:center;gap:12px;background:linear-gradient(120deg,var(--accent) 0%,#2952C8 100%);border-radius:18px;padding:16px 19px;margin-bottom:18px;box-shadow:0 10px 30px rgba(59,124,246,.28);flex-wrap:wrap}}
.copy-all-text{{flex:1;min-width:160px}}
.copy-all-title{{font-size:13.5px;font-weight:800;color:#fff;display:flex;align-items:center;gap:6px}}
.copy-all-sub{{font-size:10px;color:rgba(255,255,255,.78);margin-top:3px}}
.copy-all-btn{{background:#fff;color:#047857;border:none;border-radius:12px;padding:10px 19px;font-family:inherit;font-size:12.5px;font-weight:800;cursor:pointer;display:flex;align-items:center;gap:6px;transition:.18s;white-space:nowrap}}
.copy-all-btn:hover{{transform:translateY(-1px);box-shadow:0 6px 16px rgba(0,0,0,.22)}}
.copy-all-btn:active{{transform:translateY(0) scale(.98)}}

.cfg-title{{font-size:12px;font-weight:800;color:var(--t2);margin-bottom:13px;display:flex;align-items:center;gap:6px;text-transform:uppercase;letter-spacing:.07em}}
.cfg-title i{{color:var(--accent);font-size:15px}}
.cfg-grid{{display:grid;gap:13px}}

/* ── کارت کانفیگ به‌شکل بلیط دسترسی (signature element) ── */
.cfg-card{{background:var(--card);border:1px solid var(--card-b);border-radius:18px;transition:all .2s;position:relative;overflow:hidden}}
.cfg-card:hover{{border-color:var(--card-bh);box-shadow:var(--shadow)}}
.cfg-top{{padding:17px 19px 15px;position:relative}}
.cfg-top::after{{content:'';position:absolute;top:0;right:0;width:3px;height:100%;background:var(--green)}}
.cfg-card.inactive .cfg-top::after{{background:var(--red)}}
.cfg-head{{display:flex;align-items:flex-start;justify-content:space-between;gap:8px;margin-bottom:12px;flex-wrap:wrap}}
.cfg-label{{font-size:14.5px;font-weight:700;color:var(--t1)}}
.cfg-badges{{display:flex;gap:5px;flex-wrap:wrap;margin-top:6px}}
.proto-chip{{font-size:9px;padding:3px 8px;border-radius:7px;font-weight:800;letter-spacing:.02em}}
.pc-ws{{background:var(--accent-d);color:var(--accent2)}}
.pc-xhttp{{background:var(--purple-bg);color:var(--purple-t)}}
.pc-ultra{{background:var(--green-bg);color:var(--green-t)}}
.cfg-status{{display:flex;align-items:center;gap:5px;font-size:10px;font-weight:700;padding:4px 10px;border-radius:20px;white-space:nowrap}}
.cfg-status.ok{{background:var(--green-bg);color:var(--green-t)}}
.cfg-status.no{{background:var(--red-bg);color:var(--red-t)}}
.cfg-usage{{margin-bottom:4px}}
.ubar{{height:6px;border-radius:4px;background:rgba(96,148,246,0.1);overflow:hidden;margin-bottom:5px}}
.ubar-f{{height:100%;border-radius:4px;transition:width .5s ease}}
.utxt{{font-size:10px;color:var(--t3);display:flex;justify-content:space-between}}

/* خط جداکننده‌ی بلیطی با دندانه‌های گرد، شبیه پاره‌خط بُرد بلیط */
.cfg-tear{{position:relative;height:0;border-top:1.5px dashed var(--card-b);margin:0 19px}}
.cfg-tear::before,.cfg-tear::after{{content:'';position:absolute;top:50%;width:18px;height:18px;border-radius:50%;background:var(--bg);transform:translateY(-50%);border:1px solid var(--card-b)}}
.cfg-tear::before{{right:-28px}}
.cfg-tear::after{{left:-28px}}

.cfg-bottom{{padding:15px 19px 18px}}
.cfg-link-toggle{{width:100%;display:flex;align-items:center;justify-content:space-between;gap:10px;background:transparent;border:1px dashed var(--card-b);border-radius:11px;padding:10px 13px;cursor:pointer;font-family:inherit;color:var(--t2);font-size:11.5px;font-weight:600;transition:.15s}}
.cfg-link-toggle:hover{{background:var(--accent-d);border-color:var(--card-bh);color:var(--accent2)}}
.cfg-link-toggle .ltl{{display:flex;align-items:center;gap:7px}}
.cfg-link-toggle i.ti-chevron-down{{transition:transform .2s}}
.cfg-link-toggle.open i.ti-chevron-down{{transform:rotate(180deg)}}
.cfg-vless-wrap{{display:grid;grid-template-rows:0fr;transition:grid-template-rows .25s ease}}
.cfg-vless-wrap.open{{grid-template-rows:1fr}}
.cfg-vless-inner{{overflow:hidden}}
.cfg-vless{{background:rgba(0,0,0,.22);border:1px solid var(--card-b);border-radius:10px;padding:11px 13px;font-size:9.8px;font-family:ui-monospace,monospace;color:var(--accent2);word-break:break-all;line-height:1.7;margin-top:9px;max-height:90px;overflow-y:auto}}
[data-theme="light"] .cfg-vless{{background:rgba(46,99,214,.05)}}
.cfg-link-label{{font-size:9.5px;font-weight:800;color:var(--t2);display:flex;align-items:center;gap:5px;margin-top:11px;margin-bottom:5px;text-transform:uppercase;letter-spacing:.05em}}
.cfg-link-label i{{font-size:12px}}
.cfg-link-label .ll-vless i{{color:var(--accent2)}}
.cfg-link-label .ll-sub i{{color:var(--purple-t)}}
.cfg-vless.is-sub{{color:var(--purple-t);margin-top:5px}}
[data-theme="light"] .cfg-vless.is-sub{{background:rgba(157,123,240,.05)}}
.cfg-actions{{display:flex;gap:7px;flex-wrap:wrap;margin-top:11px}}
.btn{{font-family:inherit;font-size:11.5px;font-weight:700;border-radius:10px;padding:8px 15px;cursor:pointer;display:inline-flex;align-items:center;gap:5px;border:none;transition:all .15s;white-space:nowrap}}
.btn i{{font-size:13px}}
.btn-g{{background:var(--accent-d);color:var(--accent2);border:1px solid rgba(96,148,246,.16)}}
.btn-g:hover{{background:rgba(96,148,246,.2)}}
.btn-pur{{background:var(--purple-bg);color:var(--purple-t);border:1px solid rgba(157,123,240,.2)}}
.btn-pur:hover{{background:rgba(157,123,240,.22)}}
.conn-chip{{display:inline-flex;align-items:center;gap:4px;font-size:9.5px;padding:3px 8px;border-radius:20px;background:var(--green-bg);color:var(--green-t);font-weight:700}}
.dot{{width:5px;height:5px;border-radius:50%;background:var(--green);display:inline-block;animation:pulse 2s infinite}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.25}}}}

/* ── صفحه‌ی قفل / رمز ── */
.lock-stage{{display:flex;align-items:center;justify-content:center;min-height:78vh;padding:20px 0}}
.lock-card{{background:var(--card);border:1px solid var(--card-b);border-radius:26px;padding:0;text-align:center;max-width:380px;width:100%;box-shadow:var(--shadow);overflow:hidden;position:relative}}
.lock-banner{{background:linear-gradient(150deg,rgba(59,124,246,.16),rgba(59,124,246,.02) 70%);padding:38px 30px 26px;position:relative}}
.lock-shield{{width:64px;height:64px;border-radius:18px;background:var(--accent-d);border:1px solid var(--card-bh);display:flex;align-items:center;justify-content:center;margin:0 auto 18px;position:relative}}
.lock-shield::after{{content:'';position:absolute;inset:-7px;border-radius:22px;border:1px solid var(--card-b);animation:breathe 2.6s ease-in-out infinite}}
@keyframes breathe{{0%,100%{{transform:scale(1);opacity:.5}}50%{{transform:scale(1.08);opacity:0}}}}
.lock-shield i{{font-size:28px;color:var(--accent2)}}
.lock-title{{font-size:18px;font-weight:800;margin-bottom:6px;color:var(--t1);letter-spacing:-.01em}}
.lock-sub{{font-size:12px;color:var(--t3);line-height:1.7}}
.lock-form{{padding:24px 30px 30px}}
.lock-field{{position:relative;margin-bottom:13px}}
.lock-inp{{width:100%;padding:13px 44px 13px 44px;border-radius:13px;border:1px solid var(--card-b);background:rgba(0,0,0,.2);color:var(--t1);font-family:inherit;font-size:14px;outline:none;text-align:center;letter-spacing:.14em;transition:.18s}}
[data-theme="light"] .lock-inp{{background:rgba(46,99,214,.04)}}
.lock-inp:focus{{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-d)}}
.lock-eye{{position:absolute;left:13px;top:50%;transform:translateY(-50%);background:none;border:none;color:var(--t3);cursor:pointer;font-size:16px;padding:4px;display:flex}}
.lock-eye:hover{{color:var(--accent2)}}
.lock-lockicon{{position:absolute;right:14px;top:50%;transform:translateY(-50%);color:var(--t3);font-size:15px;pointer-events:none}}
.lock-err{{color:var(--red-t);font-size:11.5px;margin-bottom:10px;min-height:16px;display:flex;align-items:center;justify-content:center;gap:5px}}
.lock-btn{{width:100%;justify-content:center;padding:13px;font-size:13px;border-radius:13px}}
.lock-footer{{padding:14px 30px;border-top:1px solid var(--card-b);font-size:10px;color:var(--t3);display:flex;align-items:center;justify-content:center;gap:6px}}

.empty-state{{text-align:center;padding:80px 20px;color:var(--t3)}}
.empty-state i{{font-size:38px;display:block;margin-bottom:14px}}

.toast{{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(40px);background:var(--card);border:1px solid var(--card-b);color:var(--t1);border-radius:12px;padding:10px 20px;font-size:12.5px;font-weight:600;opacity:0;transition:all .25s;z-index:999;pointer-events:none;display:flex;align-items:center;gap:7px;box-shadow:var(--shadow);white-space:nowrap}}
.toast.show{{opacity:1;transform:translateX(-50%) translateY(0)}}
.toast.ok{{border-color:rgba(31,184,126,.35);background:var(--green-bg);color:var(--green-t)}}

.qr-modal{{display:none;position:fixed;inset:0;background:rgba(0,0,0,.72);z-index:600;align-items:center;justify-content:center;backdrop-filter:blur(6px);padding:20px}}
.qr-modal.open{{display:flex}}
.qr-box{{background:var(--card);border:1px solid var(--card-b);border-radius:22px;padding:26px;text-align:center;max-width:340px;width:100%;box-shadow:var(--shadow)}}
.qr-title{{font-size:13.5px;font-weight:800;margin-bottom:16px;color:var(--t1)}}
.qr-img{{border-radius:14px;overflow:hidden;margin-bottom:15px}}
.qr-img img{{width:100%;display:block;background:#fff;padding:10px;border-radius:14px}}

.footer{{text-align:center;padding-top:28px;font-size:10.5px;color:var(--t3)}}
.footer a{{color:var(--accent2);font-weight:700}}

@media(max-width:520px){{
  .stats-bar{{grid-template-columns:1fr 1fr}}
  .stats-bar .stat-card:nth-child(3){{grid-column:1/-1}}
  .sub-name{{font-size:19px}}
  .copy-all-bar{{flex-direction:column;align-items:stretch}}
  .copy-all-btn{{justify-content:center}}
  .wrap{{padding:16px 12px 50px}}
  .lock-banner{{padding:32px 22px 22px}}
  .lock-form{{padding:20px 22px 26px}}
}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
/* 𝑭𝒊𝒏𝒆𝑽𝑷𝑵 v1.0.0 — midnight glass / luminous gold visual system */



/* 𝑭𝒊𝒏𝒆𝑽𝑷𝑵 public page — starry glass and illuminated gold */
:root, [data-theme="light"]{{
  --bg:#030713;--bg2:rgba(5,11,28,.88);--bg3:rgba(17,27,52,.72);--card:rgba(13,22,45,.67);
  --card-b:rgba(231,190,82,.2);--card-bh:rgba(255,218,115,.48);--accent:#f0c45b;--accent2:#ffe5a0;--accent-d:rgba(240,196,91,.13);
  --green:#55d7ad;--green-bg:rgba(85,215,173,.12);--green-t:#88f0ce;--red:#fb7185;--red-bg:rgba(251,113,133,.12);--red-t:#fda4af;
  --amber:#f5c451;--amber-bg:rgba(245,196,81,.12);--amber-t:#ffe29a;--purple:#d9b968;--purple-bg:rgba(217,185,104,.13);--purple-t:#ffe5a0;
  --t1:#f5f4ff;--t2:#c7cbe0;--t3:#8290b6;--shadow:0 16px 44px rgba(0,0,0,.38)
}}
html,body{{background-color:#050b18;color:#eff7ff}}
.bg-fx{{background:radial-gradient(ellipse at 18% 8%,rgba(24,126,224,.14),transparent 34%),radial-gradient(ellipse at 88% 80%,rgba(122,79,229,.10),transparent 30%),linear-gradient(145deg,#050b18,#08142a 58%,#080f20)!important;background-image:none!important;opacity:1!important}}
.grid-fx{{display:none!important;background-image:none;opacity:0}}
.brand-img{{width:48px;height:48px;border-radius:14px;border-color:rgba(255,220,125,.48);box-shadow:0 0 20px rgba(240,196,91,.2)}}
.brand-name{{color:#fff0bd}}
.sub-info,.stat-card,.cfg-card,.lock-card,.qr-box,.copy-all-bar,.config-card,.sub-card{{background:linear-gradient(145deg,rgba(18,29,57,.78),rgba(6,12,29,.74))!important;border-color:rgba(240,196,91,.2)!important;box-shadow:0 16px 42px rgba(0,0,0,.24);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}}
.btn-p,.btn-g,.btn-o,.btn-pur,.copy-all-btn,.lock-btn{{background:linear-gradient(135deg,#fff0b8 0%,#f1ca62 42%,#bd8a25 100%)!important;color:#211805!important;border:1px solid rgba(255,233,164,.56)!important;box-shadow:0 0 18px rgba(240,196,91,.18),0 7px 22px rgba(0,0,0,.24)!important}}
.btn-p:hover,.btn-g:hover,.btn-o:hover,.btn-pur:hover,.copy-all-btn:hover,.lock-btn:hover{{background:linear-gradient(135deg,#fff6d6 0%,#ffe18a 45%,#d7a63a 100%)!important;transform:translateY(-1px);box-shadow:0 0 25px rgba(240,196,91,.31)!important}}
input,textarea,select,.lock-inp{{background:rgba(4,9,24,.65)!important;border-color:rgba(240,196,91,.2)!important;color:#f5f4ff!important}}
input:focus,textarea:focus,select:focus,.lock-inp:focus{{border-color:#f0c45b!important;box-shadow:0 0 0 3px rgba(240,196,91,.12)!important}}
.brand-contact{{margin-top:28px;padding:18px 20px;border:1px solid rgba(240,196,91,.24);border-radius:22px;background:linear-gradient(135deg,rgba(22,31,56,.82),rgba(6,12,28,.74));box-shadow:0 18px 45px rgba(0,0,0,.28);backdrop-filter:blur(22px);display:flex;align-items:center;justify-content:space-between;gap:18px;flex-wrap:wrap}}
.brand-contact-identity{{display:flex;align-items:center;gap:13px;min-width:0}}
.brand-contact-logo{{width:56px;height:56px;object-fit:cover;border-radius:15px;border:1px solid rgba(255,220,125,.44);box-shadow:0 0 22px rgba(240,196,91,.15)}}
.brand-contact-title{{font-size:15px;font-weight:900;color:#fff0bd;letter-spacing:.02em}}
.brand-contact-provider{{font-size:11px;color:#d0d5e9;margin-top:4px}}
.brand-contact-signature{{font-size:12px;color:#f4d98c;margin-top:3px;letter-spacing:.04em}}
.brand-contact-links{{display:flex;gap:9px;flex-wrap:wrap}}
.fine-tg-link{{display:inline-flex;align-items:center;gap:8px;padding:10px 13px;border-radius:13px;border:1px solid rgba(240,196,91,.24);background:rgba(240,196,91,.07);color:#ffe5a0;font-size:11.5px;font-weight:700;transition:all .2s}}
.fine-tg-link i{{font-size:18px;color:#f6cf67}}
.fine-tg-link:hover{{transform:translateY(-2px);background:rgba(240,196,91,.15);box-shadow:0 0 20px rgba(240,196,91,.12)}}
@media(max-width:560px){{.wrap{{padding:16px 12px 44px}}.brand-contact{{padding:14px;gap:14px}}.brand-contact-links{{width:100%}}.fine-tg-link{{flex:1;justify-content:center;min-width:125px}}.brand-contact-logo{{width:48px;height:48px}}}}
@media(prefers-reduced-motion:reduce){{*,*::before,*::after{{animation-duration:.01ms!important;animation-iteration-count:1!important;scroll-behavior:auto!important;transition-duration:.01ms!important}}}}





.top-actions{{display:flex;gap:8px;align-items:center;flex-wrap:wrap;justify-content:flex-end}}
.public-action{{padding:8px 11px;border-radius:11px;border:1px solid var(--card-b);background:rgba(13,22,45,.72);color:var(--t1);font-family:inherit;font-weight:700;font-size:11px;cursor:pointer;display:inline-flex;gap:6px;align-items:center}}
.download-section{{margin-top:24px;padding:18px;border:1px solid var(--card-b);border-radius:20px;background:linear-gradient(145deg,rgba(18,29,57,.72),rgba(6,12,29,.7));backdrop-filter:blur(20px)}}
.download-title{{font-size:15px;font-weight:900;margin-bottom:5px}}
.download-subtitle{{font-size:11px;color:var(--t2);margin-bottom:14px;line-height:1.8}}
.download-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:10px}}
.download-card{{display:flex;gap:11px;align-items:center;text-decoration:none;border:1px solid var(--card-b);background:rgba(255,255,255,.025);border-radius:14px;padding:13px;color:var(--t1);transition:transform .18s,border-color .18s}}
.download-card:hover{{transform:translateY(-2px);border-color:var(--card-bh)}}
.download-app-icon{{width:42px;height:42px;border-radius:12px;display:grid;place-items:center;background:var(--accent-d);color:var(--accent2);font-size:22px;flex-shrink:0}}
.download-app-name{{font-weight:800;font-size:12px}}
.download-app-platform{{font-size:10px;color:var(--t2);margin-top:3px}}
.speed-panel{{margin:18px 0;padding:16px;border:1px solid var(--card-b);border-radius:18px;background:linear-gradient(145deg,rgba(18,29,57,.72),rgba(6,12,29,.7))}}
.speed-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px;margin-bottom:12px}}
.speed-chip{{padding:12px;border:1px solid var(--card-b);border-radius:13px;background:rgba(255,255,255,.025)}}
.speed-chip label{{display:block;color:var(--t2);font-size:10px;margin-bottom:5px}}
.speed-chip strong{{font-size:17px;direction:ltr;display:block}}
#traffic-chart{{width:100%;height:90px;display:block}}

@media(prefers-reduced-motion:reduce){{.bg-fx{{animation:none!important}}}}

.brand-img,.brand-contact-logo{{border-radius:50%!important}}

/* FineVPN / subscription portal — matching glass palette, static and light */
:root{{--bg:#050b18;--bg2:#09172e;--bg3:#102544;--card:rgba(12,29,55,.75);--card-b:rgba(74,174,255,.2);--card-bh:rgba(86,190,255,.42);--accent:#38bdf8;--accent2:#7dd3fc;--accent-d:rgba(56,189,248,.13);--green:#20c997;--green-bg:rgba(32,201,151,.12);--green-t:#65e7bd;--red:#fb7185;--red-bg:rgba(251,113,133,.12);--red-t:#ff9aaa;--amber:#f5b942;--amber-bg:rgba(245,185,66,.12);--amber-t:#ffd27a;--purple:#a78bfa;--purple-bg:rgba(167,139,250,.13);--t1:#eff7ff;--t2:#b7cce3;--t3:#7897b8;--shadow:0 14px 36px rgba(0,0,0,.26)}}
[data-theme="light"]{{--bg:#eef5fc;--bg2:#f7fbff;--bg3:#e5effa;--card:rgba(255,255,255,.88);--card-b:rgba(38,126,211,.16);--card-bh:rgba(38,126,211,.32);--accent:#147ed0;--accent2:#1769bd;--accent-d:rgba(20,126,208,.09);--green:#059669;--green-bg:rgba(5,150,105,.1);--green-t:#047857;--red:#dc4b63;--red-bg:rgba(220,75,99,.1);--red-t:#b4233c;--amber:#b7791f;--amber-bg:rgba(183,121,31,.1);--amber-t:#93600f;--purple:#7c5ad6;--purple-bg:rgba(124,90,214,.1);--t1:#13253b;--t2:#36516d;--t3:#71869d;--shadow:0 10px 28px rgba(19,49,81,.09)}}
html,body{{background:var(--bg);color:var(--t1);font-family:'Vazirmatn','Inter',system-ui,sans-serif}}body{{background-image:radial-gradient(ellipse at 18% 8%,rgba(24,126,224,.12),transparent 32%),radial-gradient(ellipse at 88% 80%,rgba(122,79,229,.09),transparent 28%);background-attachment:fixed}}
.bg-fx{{background:radial-gradient(ellipse at 18% 8%,rgba(24,126,224,.12),transparent 34%),radial-gradient(ellipse at 88% 80%,rgba(122,79,229,.08),transparent 30%),#050b18!important;background-image:none!important;opacity:1!important}}.grid-fx{{display:none!important}}.bg-fx::after{{display:none!important}}
.wrap{{max-width:1160px;padding:24px 22px 54px}}.top{{padding:15px 18px;border:1px solid var(--card-b);border-radius:21px;background:linear-gradient(145deg,rgba(14,35,66,.85),rgba(7,18,39,.88));box-shadow:var(--shadow);backdrop-filter:blur(11px);-webkit-backdrop-filter:blur(11px);margin-bottom:20px}}
[data-theme="light"] .top{{background:rgba(255,255,255,.88)}}.brand-img{{width:54px;height:54px;border-radius:15px!important;border:1px solid rgba(83,184,255,.38);box-shadow:0 0 19px rgba(37,146,238,.15)}}.brand-name{{font-size:17px;font-weight:900;color:var(--t1);letter-spacing:.02em}}.brand-sub{{color:var(--t2)}}.top-actions{{gap:7px}}
.public-action{{padding:9px 12px;border-radius:12px;border:1px solid rgba(82,174,244,.23);background:rgba(45,134,210,.1);color:#c5eaff;font-family:inherit;font-weight:800;font-size:11px;cursor:pointer;display:inline-flex;gap:7px;align-items:center;min-height:38px}}.public-action:hover{{background:rgba(45,134,210,.18);border-color:rgba(82,190,255,.4)}}
.sub-info,.stat-card,.cfg-card,.lock-card,.qr-box,.copy-all-bar,.config-card,.sub-card,.speed-panel,.download-section{{background:linear-gradient(145deg,rgba(16,38,70,.82),rgba(7,19,40,.85))!important;border:1px solid rgba(79,171,245,.21)!important;border-radius:19px!important;box-shadow:var(--shadow)!important;backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)}}[data-theme="light"] .sub-info,[data-theme="light"] .stat-card,[data-theme="light"] .cfg-card,[data-theme="light"] .lock-card,[data-theme="light"] .qr-box,[data-theme="light"] .copy-all-bar,[data-theme="light"] .config-card,[data-theme="light"] .sub-card,[data-theme="light"] .speed-panel,[data-theme="light"] .download-section{{background:rgba(255,255,255,.9)!important;border-color:rgba(38,126,211,.16)!important}}
.sub-info{{padding:22px 24px}}.sub-name{{font-size:23px;font-weight:900;letter-spacing:-.02em;color:var(--t1)}}.sub-eyebrow{{color:#7ccfff;font-weight:800}}.sub-meta-row{{color:var(--t2)}}.sub-sub-box{{border-color:var(--card-b);border-radius:13px;background:rgba(50,141,222,.08)}}.sub-sub-url{{color:#9bdfff}}
.stats-bar{{grid-template-columns:repeat(5,minmax(0,1fr));gap:12px}}.stat-card{{padding:17px!important;min-width:0}}.stat-label{{font-size:10.5px;color:var(--t2);font-weight:800}}.stat-val{{font-size:21px;font-weight:900;color:var(--t1)}}.stat-sub{{color:var(--t3)}}
.cfg-title{{font-size:15px;font-weight:900;color:var(--t1)}}.cfg-card{{border-radius:18px!important}}.cfg-label{{font-weight:900;color:var(--t1)}}.cfg-vless{{background:rgba(0,0,0,.19);border:1px solid var(--card-b);border-radius:12px}}.cfg-actions{{gap:8px}}.btn{{border-radius:12px;min-height:36px;padding:8px 13px;font-family:inherit;font-size:11.5px;font-weight:850;transition:background .16s,border-color .16s,box-shadow .16s}}.btn-p,.copy-all-btn,.lock-btn{{background:linear-gradient(120deg,#42c5fb,#2878ea 70%,#5b62ed)!important;color:#05182d!important;border:1px solid rgba(147,218,255,.55)!important;box-shadow:0 7px 18px rgba(31,127,230,.2)!important}}.btn-pur{{background:rgba(143,113,236,.13)!important;color:#d8ccff!important;border:1px solid rgba(160,135,255,.28)!important}}.btn-g,.btn-o{{background:rgba(56,189,248,.09)!important;color:#bdeaff!important;border:1px solid rgba(77,179,255,.25)!important}}
input,textarea,select,.lock-inp{{background:rgba(3,13,30,.42)!important;border-color:rgba(88,172,235,.2)!important;color:var(--t1)!important;border-radius:12px!important;font-family:inherit!important}}input:focus,textarea:focus,select:focus,.lock-inp:focus{{border-color:#45bfff!important;box-shadow:0 0 0 3px rgba(56,189,248,.12)!important}}
.brand-contact{{margin-top:23px;padding:18px 20px;border:1px solid var(--card-b);border-radius:19px;background:linear-gradient(145deg,rgba(16,38,70,.82),rgba(7,19,40,.85));box-shadow:var(--shadow)}}.brand-contact-logo{{border:1px solid rgba(83,184,255,.38);box-shadow:0 0 18px rgba(37,146,238,.15)}}.brand-contact-title{{color:var(--t1)}}.brand-contact-provider{{color:var(--t2)}}.brand-contact-signature{{color:#7fcaff}}.fine-tg-link{{border-color:rgba(65,171,244,.25);background:rgba(36,131,214,.1);color:#c7ecff;border-radius:12px}}.fine-tg-link i{{color:#58c6ff}}
.download-section{{padding:20px}}.download-title{{font-size:16px;font-weight:900;color:var(--t1)}}.download-subtitle{{color:var(--t2)}}.download-card{{border-color:var(--card-b);background:rgba(255,255,255,.035);border-radius:14px;transition:border-color .16s,background .16s}}.download-card:hover{{transform:none;border-color:var(--card-bh);background:rgba(55,158,230,.07)}}
.toast{{border-radius:13px;box-shadow:0 10px 28px rgba(0,0,0,.24)}}.qr-modal{{background:rgba(1,7,17,.76)}}.qr-box{{border-color:var(--card-b)!important}}
*,*::before,*::after{{animation:none!important;scroll-behavior:auto!important}}.sub-card:hover,.cfg-card:hover,.download-card:hover{{transform:none!important}}
@media(max-width:850px){{.stats-bar{{grid-template-columns:repeat(3,minmax(0,1fr))}}}}
@media(max-width:600px){{.wrap{{padding:14px 12px 38px}}.top{{padding:12px;align-items:flex-start;gap:12px}}.top-actions{{width:100%;justify-content:flex-start}}.stats-bar{{grid-template-columns:repeat(2,minmax(0,1fr))}}.stats-bar .stat-card:nth-child(4),.stats-bar .stat-card:nth-child(5){{grid-column:auto!important}}.sub-info{{padding:17px}}.sub-name{{font-size:19px}}.cfg-actions .btn{{flex:1;justify-content:center}}.brand-contact{{padding:14px}}}}


/* FineVPN public subscription — fixed midnight glass and mobile-first layout */
:root{{color-scheme:dark;--bg:#050914;--bg2:#08152b;--bg3:#0d203c;--card:rgba(13,30,56,.94);--card-b:rgba(85,176,255,.23);--card-bh:rgba(89,194,255,.48);--accent:#42c2ff;--accent2:#93ddff;--accent-d:rgba(66,177,255,.12);--green:#29d9a4;--green-bg:rgba(41,217,164,.13);--green-t:#8bf0d0;--red:#ff6c87;--red-bg:rgba(255,108,135,.13);--red-t:#ffacba;--amber:#f6c15f;--amber-bg:rgba(246,193,95,.13);--amber-t:#ffdfa0;--purple:#ad9bff;--purple-bg:rgba(173,155,255,.14);--t1:#f4f8ff;--t2:#c0d0e7;--t3:#8ba3c1;--shadow:0 16px 40px rgba(0,0,0,.34)}}
html,body{{min-height:100%;background:#050914!important;color:#f4f8ff!important;color-scheme:dark}}
body{{background-image:radial-gradient(ellipse at 10% 0%,rgba(20,107,197,.16),transparent 34%),radial-gradient(ellipse at 95% 78%,rgba(87,63,199,.10),transparent 32%)!important;background-attachment:fixed}}
.bg-fx{{background:transparent!important;opacity:1!important}}.grid-fx{{opacity:.18!important}}
.wrap{{max-width:940px;padding:20px 18px 46px}}
.top{{display:grid;grid-template-columns:minmax(0,1fr) auto;align-items:center;gap:14px;padding:17px 19px;margin-bottom:17px;border:1px solid rgba(85,176,255,.25);border-radius:21px;background:linear-gradient(135deg,rgba(16,40,72,.96),rgba(7,17,37,.97));box-shadow:0 14px 34px rgba(0,0,0,.28),inset 0 1px rgba(255,255,255,.04);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px)}}
.brand{{min-width:0;gap:13px}}.brand-img{{width:50px;height:50px;border-radius:15px;overflow:hidden;border:1px solid rgba(100,197,255,.46);box-shadow:0 0 21px rgba(43,157,241,.22);flex:0 0 auto}}.brand-name{{font-size:18px;font-weight:900;color:#f5f9ff;line-height:1.45;white-space:nowrap}}.brand-sub{{font-size:10.5px;color:#adc4e0;line-height:1.65}}
.top-actions{{display:flex;align-items:center;justify-content:flex-end;gap:7px;flex-wrap:wrap}}.public-action{{min-height:33px;padding:6px 10px;border-radius:10px;border:1px solid rgba(92,180,245,.25);background:rgba(52,137,211,.12);color:#d7f1ff;font-family:inherit;font-weight:800;font-size:10px;text-decoration:none;display:inline-flex;align-items:center;justify-content:center;gap:6px;white-space:nowrap}}.public-action:hover{{background:rgba(52,137,211,.2);border-color:rgba(105,197,255,.45)}}.public-download-jump{{font-size:9.5px;min-height:30px;padding:5px 9px;color:#bde8ff}}
.sub-info,.stat-card,.cfg-card,.lock-card,.qr-box,.copy-all-bar,.speed-panel,.download-section,.brand-contact{{background:linear-gradient(145deg,rgba(15,35,64,.96),rgba(7,18,39,.97))!important;border:1px solid rgba(86,174,248,.24)!important;border-radius:19px!important;box-shadow:0 14px 34px rgba(0,0,0,.25),inset 0 1px rgba(255,255,255,.035)!important;backdrop-filter:blur(18px)!important;-webkit-backdrop-filter:blur(18px)!important;color:#f4f8ff!important}}
.sub-info{{padding:23px 24px;margin-bottom:14px}}.sub-eyebrow{{font-size:11px;color:#8bd8ff;font-weight:850;letter-spacing:0}}.sub-name{{font-size:24px;font-weight:950;color:#f7fbff;line-height:1.4}}.sub-desc{{font-size:12px;color:#bfd0e6}}.sub-meta-row{{font-size:10.5px;color:#a9bfd9}}
.sub-sub-box{{padding:11px 12px;border-radius:14px;border:1px solid rgba(84,169,235,.24);background:rgba(6,19,41,.68);gap:8px}}.sub-sub-url{{font-size:10px;line-height:1.65;color:#9bdfff;min-width:0;overflow-wrap:anywhere}}.sub-sub-box .btn{{flex:0 0 auto}}
.stats-bar{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin:0 0 15px}}.stat-card{{min-width:0;padding:15px 16px!important;border-radius:16px!important}}.stat-label{{font-size:10px;color:#b8cce5;font-weight:850;letter-spacing:0;text-transform:none}}.stat-val{{font-size:22px;line-height:1.35;color:#f5f9ff;font-weight:950;overflow-wrap:anywhere}}.stat-sub{{font-size:9.5px;color:#91a9c8;line-height:1.65}}.status-online-card .stat-val{{color:#73edc4}}.status-offline-card .stat-val{{color:#ff9aaf}}.usage-val{{font-size:18px}}.quota-value{{font-size:14px;direction:rtl}}.quota-track{{width:100%;height:6px;margin-top:9px;overflow:hidden;background:rgba(170,203,241,.12);border-radius:999px}}.quota-track span{{display:block;height:100%;border-radius:inherit;background:linear-gradient(90deg,#32c7fa,#5b75f0);box-shadow:0 0 12px rgba(63,166,255,.35)}}
.copy-all-bar{{display:flex;align-items:center;gap:12px;flex-wrap:wrap;padding:14px 16px;margin-bottom:16px}}.copy-all-title{{font-size:13px;color:#f3f8ff;font-weight:900}}.copy-all-sub{{font-size:10px;color:#b9cbe2}}.copy-all-btn{{min-height:36px;padding:8px 14px;border-radius:11px;background:linear-gradient(120deg,#40bff5,#367bea 68%,#635ee9)!important;border:1px solid rgba(160,220,255,.48)!important;color:#06172d!important;font-size:11px;font-weight:900;box-shadow:0 7px 17px rgba(42,130,237,.2)}}
.cfg-title{{font-size:14px;color:#eaf4ff;font-weight:900;margin:16px 2px 10px}}.cfg-grid{{display:grid;gap:10px}}.cfg-card{{border-radius:17px!important}}.cfg-top{{padding:15px 16px 13px}}.cfg-head{{align-items:center}}.cfg-label{{font-size:13px;font-weight:900;color:#f3f8ff}}.cfg-badges{{gap:5px}}.proto-chip{{font-size:9px}}.cfg-status-stack{{display:flex;flex-direction:column;align-items:flex-end;gap:5px;flex:0 0 auto}}.cfg-status{{font-size:9px;padding:4px 8px;border-radius:999px}}.cfg-status.live.online{{background:rgba(34,211,165,.13);color:#7bedc8;border:1px solid rgba(45,218,170,.2)}}.cfg-status.live.offline{{background:rgba(133,157,188,.12);color:#b6c8df;border:1px solid rgba(133,157,188,.2)}}.cfg-status.ok{{background:rgba(34,211,165,.11);color:#8de9ce}}.cfg-status.no{{background:rgba(255,100,127,.12);color:#ff9eaf}}.cfg-usage{{margin-top:9px}}.ubar{{height:5px;background:rgba(150,190,232,.13)}}.utxt{{font-size:9px;color:#9fb5d1;gap:8px;flex-wrap:wrap}}.cfg-tear{{border-color:rgba(92,174,241,.19)}}.cfg-tear:before,.cfg-tear:after{{background:#0a1a32;border-color:rgba(92,174,241,.23)}}.cfg-bottom{{padding:12px 16px 15px}}.cfg-link-toggle{{font-size:10.5px;padding:9px 11px;border:1px solid rgba(91,169,236,.2);background:rgba(4,15,34,.48);color:#c1d9f3}}.cfg-vless{{background:rgba(2,10,24,.72)!important;color:#9bdcff;border:1px solid rgba(91,169,236,.2)}}
.btn{{min-height:33px!important;padding:7px 10px!important;border-radius:10px!important;font-family:inherit!important;font-size:10px!important;font-weight:850!important;display:inline-flex;align-items:center;justify-content:center;gap:6px;white-space:nowrap;line-height:1.4}}.btn-p{{background:linear-gradient(120deg,#3dbff5,#3179e8 68%,#605fe9)!important;color:#07182e!important;border:1px solid rgba(154,219,255,.5)!important;box-shadow:0 6px 14px rgba(34,126,226,.17)!important}}.btn-pur,.btn-g,.btn-o{{background:rgba(56,147,216,.12)!important;color:#c8ecff!important;border:1px solid rgba(86,175,239,.25)!important}}.cfg-actions{{display:flex;gap:6px;flex-wrap:wrap}}.cfg-actions .btn{{flex:1 1 auto}}
.speed-panel{{margin:14px 0;padding:15px}}.speed-grid{{grid-template-columns:repeat(4,minmax(0,1fr));gap:8px}}.speed-chip{{padding:10px;border:1px solid rgba(86,174,248,.18);border-radius:12px;background:rgba(4,16,35,.54)}}.speed-chip label{{font-size:9px;color:#a9bfd9}}.speed-chip strong{{font-size:14px;color:#eaf6ff}}
.download-section{{margin-top:16px;padding:14px 15px;border-radius:17px!important}}.download-head{{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:9px}}.download-title{{font-size:13px;color:#f2f8ff;font-weight:900}}.download-subtitle{{font-size:9.5px;color:#9fb6d2;margin:2px 0 0}}.download-head-icon{{width:30px;height:30px;flex:0 0 auto;border-radius:10px;display:grid;place-items:center;background:rgba(55,158,230,.13);border:1px solid rgba(83,173,243,.24);color:#9bdfff;font-size:15px}}.download-grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:7px}}.download-card{{min-width:0;display:flex;align-items:center;gap:8px;padding:8px 9px;border:1px solid rgba(86,174,248,.18);border-radius:12px;background:rgba(4,16,35,.54);text-decoration:none;color:#eff7ff}}.download-card:hover{{background:rgba(53,144,217,.13);border-color:rgba(112,197,255,.38)}}.download-app-icon{{width:29px;height:29px;flex:0 0 29px;border-radius:9px;font-size:15px;background:rgba(55,158,230,.13);color:#91d9ff}}.download-app-copy{{display:flex;flex-direction:column;min-width:0}}.download-app-name{{font-size:10px;font-weight:900;color:#f1f7ff}}.download-app-platform{{font-size:8px;color:#9eb6d1;line-height:1.45;margin-top:2px}}.download-open{{font-size:11px;color:#79cfff;margin-inline-start:auto;flex:0 0 auto}}
.brand-contact{{margin-top:15px;padding:13px 15px}}.brand-contact-title{{color:#f0f8ff}}.brand-contact-provider{{color:#b5c9e2}}.brand-contact-signature{{color:#8bd7ff}}.fine-tg-link{{font-size:10px;padding:8px 10px;border-radius:10px;color:#c9ecff;background:rgba(45,143,220,.1);border-color:rgba(88,178,245,.22)}}
.toast{{border-radius:12px;background:rgba(7,19,39,.97)!important;border:1px solid rgba(86,174,248,.26)!important;box-shadow:0 12px 30px rgba(0,0,0,.32)}}.qr-modal{{background:rgba(1,6,17,.82)}}.qr-box{{padding:20px}}
@media(max-width:720px){{.wrap{{padding:14px 12px 34px}}.top{{grid-template-columns:1fr;gap:10px;padding:14px}}.brand{{width:100%}}.brand-name{{font-size:16px}}.top-actions{{width:100%;justify-content:flex-start}}.stats-bar{{grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}}.stat-card{{padding:13px!important}}.stat-val{{font-size:20px}}.quota-value{{font-size:12px}}.sub-info{{padding:17px}}.sub-name{{font-size:21px}}.copy-all-bar{{gap:8px;padding:13px}}.copy-all-btn{{width:100%}}.speed-grid{{grid-template-columns:repeat(2,minmax(0,1fr))}}.cfg-top{{padding:13px}}.cfg-head{{align-items:flex-start}}.cfg-bottom{{padding:10px 12px 13px}}.download-section{{padding:12px}}.download-grid{{grid-template-columns:repeat(2,minmax(0,1fr))}}.brand-contact{{padding:12px}}}}
@media(max-width:380px){{.download-grid{{grid-template-columns:1fr}}.sub-sub-box .btn{{font-size:9px!important;padding:6px 8px!important}}.stat-val{{font-size:18px}}}}
@media(prefers-reduced-motion:reduce){{*,*::before,*::after{{animation:none!important;transition:none!important;scroll-behavior:auto!important}}}}


/* FineVPN Aurora Glass v1.0.0 — compact live metrics */
body::after{{content:"";position:fixed;inset:0;z-index:1;pointer-events:none;background:url("https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png") center 52%/min(58vw,540px) no-repeat;opacity:.035;filter:grayscale(1);mix-blend-mode:screen}}
.wrap{{z-index:2}}
:root{{--accent:#39c8ff;--accent2:#8ddfff;--accent-d:rgba(57,200,255,.12);--green:#23d8a5;--green-t:#83f1d0;--purple:#a89cff;--card-b:rgba(91,183,255,.23);--card-bh:rgba(110,204,255,.48)}}
.bg-fx{{background:radial-gradient(ellipse 64% 42% at 50% -5%,rgba(45,155,255,.2),transparent 66%),radial-gradient(ellipse 36% 34% at 100% 45%,rgba(126,91,255,.12),transparent 72%),var(--bg)!important}}
.grid-fx{{opacity:.12;background-image:linear-gradient(rgba(75,177,255,.055) 1px,transparent 1px),linear-gradient(90deg,rgba(75,177,255,.055) 1px,transparent 1px)}}
.brand-img{{border-radius:50%;border-color:rgba(97,202,255,.55);box-shadow:0 0 0 4px rgba(55,153,255,.06),0 0 24px rgba(45,173,255,.3)}}
.portal-metrics{{display:grid;grid-template-columns:1.25fr 1fr 1fr;gap:11px;margin:0 0 16px}}
.portal-metric{{position:relative;overflow:hidden;min-width:0;padding:16px;border:1px solid rgba(94,184,255,.22);border-radius:19px;background:linear-gradient(145deg,rgba(15,37,69,.94),rgba(7,18,40,.97));box-shadow:0 15px 34px rgba(0,0,0,.25),inset 0 1px rgba(255,255,255,.045);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px)}}
.portal-metric:before{{content:"";position:absolute;width:150px;height:150px;left:-76px;top:-90px;border-radius:50%;background:radial-gradient(circle,rgba(58,185,255,.17),transparent 70%);pointer-events:none}}
.portal-metric-head{{display:flex;align-items:center;justify-content:space-between;gap:8px;margin-bottom:12px;color:#c9def5;font-size:10px;font-weight:900}}
.metric-tag{{font-size:8px;padding:4px 7px;border-radius:99px;border:1px solid rgba(93,188,255,.22);background:rgba(49,144,220,.11);color:#9cddff;white-space:nowrap}}
.metric-flex{{display:flex;align-items:center;gap:14px;min-width:0}}
.ring-gauge{{--ring-value:0;--ring-color:#38c6ff;width:112px;height:112px;flex:0 0 112px;border-radius:50%;display:grid;place-items:center;background:conic-gradient(from -90deg,var(--ring-color) calc(var(--ring-value)*1%),rgba(150,190,230,.12) 0);box-shadow:0 0 23px color-mix(in srgb,var(--ring-color) 18%,transparent);position:relative}}
.ring-gauge:before{{content:"";position:absolute;inset:8px;border-radius:50%;background:linear-gradient(145deg,#0c2341,#08172e);border:1px solid rgba(130,192,245,.14)}}
.ring-core{{position:relative;z-index:1;text-align:center;display:flex;flex-direction:column;align-items:center;gap:1px}}
.ring-core strong{{font-size:22px;line-height:1.25;font-weight:950;color:#f2f9ff;direction:ltr}}
.ring-core small{{font-size:9px;color:#91abc9;font-weight:800}}
.metric-detail{{min-width:0;display:flex;flex-direction:column;gap:6px}}
.metric-main-value{{font-size:19px;font-weight:950;color:#f3f8ff;line-height:1.3;overflow-wrap:anywhere}}
.metric-hint{{font-size:9px;color:#9ab2d0;line-height:1.7}}
.metric-remaining{{font-size:10px;color:#8debd0;font-weight:850;line-height:1.6}}
.metric-split{{display:flex;flex-wrap:wrap;gap:7px;margin-top:9px}}
.metric-split span{{font-size:9px;color:#b5cce7;background:rgba(63,143,212,.1);border:1px solid rgba(87,170,238,.14);border-radius:9px;padding:5px 7px}}.unclassified-note{{margin-top:8px;padding:6px 8px;border-radius:9px;background:rgba(245,158,11,.08);border:1px solid rgba(245,158,11,.2);color:#f4c77d;font-size:9px;line-height:1.6}}
.metric-live-number{{font-size:35px;font-weight:950;color:#86f1d1;line-height:1.1;text-shadow:0 0 22px rgba(35,216,165,.18)}}
.metric-live-caption{{font-size:9px;color:#9fb8d5;margin-top:4px}}
.metric-session-pill{{display:inline-flex;align-items:center;gap:5px;margin-top:12px;padding:6px 9px;border-radius:99px;background:rgba(35,216,165,.1);border:1px solid rgba(35,216,165,.2);font-size:9px;color:#8cebd0;font-weight:850}}
.metric-session-pill i{{font-size:11px}}
.expired-banner{{margin:0 0 12px;padding:10px 13px;border-radius:12px;border:1px solid rgba(255,100,127,.28);background:linear-gradient(100deg,rgba(255,75,108,.12),rgba(255,75,108,.04));color:#ff9dad;font-size:11px;font-weight:900;display:flex;align-items:center;gap:8px}}
.diag-open{{width:32px;height:32px;padding:0;display:inline-grid;place-items:center;border-radius:10px;background:rgba(45,185,255,.1);border:1px solid rgba(91,190,255,.3);color:#a9e5ff;cursor:pointer;font-size:15px}}
.diag-overlay{{display:none;position:fixed;inset:0;z-index:1000;align-items:center;justify-content:center;padding:16px;background:rgba(1,7,19,.78);backdrop-filter:blur(7px)}}
.diag-overlay.open{{display:flex}}
.diag-window{{width:min(100%,440px);border:1px solid rgba(55,214,174,.26);border-radius:17px;overflow:hidden;background:linear-gradient(150deg,rgba(6,21,36,.99),rgba(4,12,27,.99));box-shadow:0 24px 70px rgba(0,0,0,.56),0 0 30px rgba(30,210,160,.08);font-family:ui-monospace,Consolas,monospace}}
.diag-head{{display:flex;align-items:center;justify-content:space-between;padding:10px 12px;border-bottom:1px solid rgba(80,177,150,.16);background:rgba(35,210,162,.05)}}
.diag-title{{font-size:10px;color:#a5f3d2;font-weight:900;letter-spacing:.08em}}
.diag-head button{{border:0;background:transparent;color:#8ca9b8;font-size:17px;cursor:pointer}}
.diag-body{{padding:12px;display:grid;gap:7px}}
.diag-line{{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:7px 9px;border-radius:8px;background:rgba(84,125,151,.07);border:1px solid rgba(105,159,183,.1);font-size:9px;color:#a6c0cf}}
.diag-state{{font-weight:900;white-space:nowrap}}.diag-state.ok{{color:#5ee6aa}}.diag-state.err{{color:#ff788d}}.diag-state.na{{color:#8da1b0}}.diag-state.busy{{color:#65d5ff}}
.diag-foot{{display:flex;gap:7px;padding:0 12px 12px}}.diag-btn{{flex:1;padding:8px 10px;border-radius:9px;border:1px solid rgba(71,192,161,.24);background:rgba(35,177,137,.1);color:#a7f0d4;font:800 9px inherit;cursor:pointer}}
@media(max-width:760px){{.portal-metrics{{grid-template-columns:1fr 1fr}}.portal-metric:first-child{{grid-column:1/-1}}.portal-metric{{padding:13px}}}}
@media(max-width:390px){{.portal-metrics{{grid-template-columns:1fr}}.portal-metric:first-child{{grid-column:auto}}.ring-gauge{{width:98px;height:98px;flex-basis:98px}}.metric-main-value{{font-size:17px}}}}
/* Responsive portal refinements */
.brand-img{{position:relative;display:grid;place-items:center;background:linear-gradient(145deg,rgba(26,125,204,.2),rgba(99,91,230,.14))}}
.brand-img img{{position:relative;z-index:1}}
.logo-fallback{{position:absolute;inset:0;display:grid;place-items:center;color:#9cddff;font-weight:950;font-size:26px;text-shadow:0 0 18px rgba(57,180,255,.6);pointer-events:none}}
html,body{{min-width:320px;max-width:100%;overflow-x:hidden;color-scheme:dark;-webkit-text-size-adjust:100%;text-size-adjust:100%}}
.bg-fx:before{{content:"F";position:fixed;inset:0;margin:auto;width:min(52vw,520px);height:min(52vw,520px);display:grid;place-items:center;border:1px solid rgba(84,174,255,.045);border-radius:50%;font-size:min(38vw,390px);font-weight:950;color:rgba(86,167,255,.025);line-height:1;pointer-events:none;z-index:0}}
.wrap{{width:min(100% - 32px,1120px);margin-inline:auto;min-width:0}}
.top,.sub-info,.portal-metric,.stat-card,.cfg-card,.speed-panel,.download-section{{min-width:0}}
.top{{grid-template-columns:minmax(0,1fr) auto}}
.portal-metric{{min-width:0}}
.metric-detail{{min-width:0;overflow-wrap:anywhere}}
.metric-split{{flex-wrap:wrap;gap:7px}}
.cfg-actions .btn{{min-width:0;white-space:normal;overflow-wrap:anywhere}}
.cfg-vless{{overflow-wrap:anywhere;word-break:break-all}}
.diag-overlay,.qr-modal{{padding:max(10px,env(safe-area-inset-top)) max(10px,env(safe-area-inset-right)) max(10px,env(safe-area-inset-bottom)) max(10px,env(safe-area-inset-left))}}
@media(min-width:1500px){{.wrap{{width:min(100% - 56px,1220px)}}}}
@media(max-width:720px){{body{{background-attachment:scroll}}.wrap{{width:calc(100% - 24px);padding-top:12px}}.top{{grid-template-columns:1fr;gap:10px;padding:13px}}.top-actions{{justify-content:flex-start;gap:6px}}.sub-info{{padding:17px}}.portal-metrics{{grid-template-columns:repeat(2,minmax(0,1fr))}}.portal-metric:first-child{{grid-column:1/-1}}.metric-flex{{gap:10px}}.ring-gauge{{width:100px;height:100px;flex-basis:100px}}.cfg-head{{gap:10px}}.cfg-status-stack{{align-items:flex-start}}.cfg-actions{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr))}}.cfg-actions .btn{{width:100%;min-height:38px}}.speed-grid{{grid-template-columns:repeat(2,minmax(0,1fr))}}.copy-all-bar{{align-items:stretch}}.copy-all-btn{{width:100%}}}}
@media(max-width:460px){{.wrap{{width:calc(100% - 18px);padding-inline:0}}.brand-name{{font-size:15px}}.brand-img{{width:43px;height:43px}}.public-action{{min-height:35px;padding:6px 8px;font-size:9px}}.top-actions{{display:grid;grid-template-columns:36px repeat(2,minmax(0,1fr))}}.diag-open{{width:36px;height:35px}}.portal-metrics{{grid-template-columns:minmax(0,1fr)}}.portal-metric:first-child{{grid-column:auto}}.portal-metric{{padding:13px}}.metric-flex{{align-items:center}}.ring-gauge{{width:92px;height:92px;flex-basis:92px}}.metric-main-value{{font-size:16px}}.metric-remaining{{font-size:10px}}.stats-bar{{grid-template-columns:repeat(2,minmax(0,1fr))}}.stat-card{{padding:12px!important}}.stat-val{{font-size:18px}}.cfg-head{{flex-direction:column;align-items:stretch}}.cfg-status-stack{{flex-direction:row;flex-wrap:wrap;align-items:center}}.cfg-actions{{grid-template-columns:minmax(0,1fr)}}.download-grid{{grid-template-columns:minmax(0,1fr)}}.download-card{{min-height:48px}}.diag-window{{width:100%}}.diag-line{{font-size:8.5px}}}}
@media(max-width:350px){{.top-actions{{grid-template-columns:34px 1fr}}.top-actions .public-action:last-child{{grid-column:2}}.sub-name{{font-size:18px}}.metric-flex{{gap:8px}}.ring-gauge{{width:84px;height:84px;flex-basis:84px}}.stat-val{{font-size:16px}}.copy-all-title{{font-size:12px}}}}
@media(prefers-reduced-motion:reduce){{*,*::before,*::after{{animation:none!important;transition:none!important;scroll-behavior:auto!important}}}}
/* Subtle glossy glass surfaces; static gradients avoid continuous GPU animation. */
.top,.sub-info,.portal-metric,.stat-card,.cfg-card,.speed-panel,.download-section{{background-image:linear-gradient(145deg,rgba(37,107,163,.15),rgba(8,22,43,.1))!important;border-color:rgba(101,184,245,.25)!important;box-shadow:0 15px 38px rgba(0,0,0,.25),inset 0 1px rgba(255,255,255,.07),inset 0 -1px rgba(63,148,211,.07)!important;backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px)}}
.public-action,.diag-open,.diag-btn,.cfg-actions .btn,.copy-all-btn{{box-shadow:inset 0 1px rgba(255,255,255,.15),0 6px 17px rgba(0,0,0,.2);touch-action:manipulation}}
.portal-metric{{border-radius:20px!important}}
.ring-gauge{{filter:drop-shadow(0 5px 14px rgba(46,175,238,.12))}}
@media(max-width:460px){{.portal-metric,.cfg-card,.download-card{{border-radius:15px!important}}}}
</style>
</head>
<body>
<div class="bg-fx"></div><div class="grid-fx"></div>
<div class="toast" id="toast"></div>
<div class="diag-overlay" id="diag-overlay" onclick="if(event.target===this)closePortalDiagnostics()">
  <div class="diag-window" role="dialog" aria-modal="true" aria-label="عیب‌یابی FineVPN">
    <div class="diag-head"><span class="diag-title">FINEVPN // DIAGNOSTICS</span><button type="button" onclick="closePortalDiagnostics()" aria-label="بستن">×</button></div>
    <div class="diag-body" id="diag-results"><div class="diag-line"><span>آماده‌سازی تست‌ها</span><span class="diag-state na">NOT RUN</span></div></div>
    <div class="diag-foot"><button class="diag-btn" onclick="runPortalDiagnostics()">↻ اجرای دوباره</button><button class="diag-btn" onclick="copyPortalDiagnosticReport()">کپی گزارش</button></div>
  </div>
</div>
<div class="qr-modal" id="qr-modal" onclick="this.classList.remove('open')">
  <div class="qr-box" onclick="event.stopPropagation()">
    <div class="qr-title" id="qr-label">QR Code</div>
    <div class="qr-img"><img id="qr-img" src="" alt="QR"></div>
    <button class="btn btn-g" style="width:100%;justify-content:center" onclick="document.getElementById('qr-modal').classList.remove('open')"><i class="ti ti-x"></i> بستن</button>
  </div>
</div>
<div class="wrap">
  <div class="top">
    <div class="brand">
      <div class="brand-img"><span class="logo-fallback" aria-hidden="true">F</span><img src="https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png" alt="𝑭𝒊𝒏𝒆𝑽𝑷𝑵" onerror="this.remove()"></div>
      <div><div class="brand-name">𝑭𝒊𝒏𝒆𝑽𝑷𝑵</div><div class="brand-sub">Secure Subscription Portal</div></div>
    </div>
    <div class="top-actions">
      <button class="diag-open" type="button" onclick="openPortalDiagnostics()" title="عیب‌یابی اتصال"><i class="ti ti-terminal-2"></i></button>
      <button class="public-action" onclick="refreshSubscription()" id="refresh-sub-btn"><i class="ti ti-refresh"></i><span data-public-i18n="تازه‌سازی">تازه‌سازی</span></button>
      <button class="public-action" onclick="togglePublicLanguage()"><i class="ti ti-language"></i><span id="public-lang-label">English</span></button>
      <a class="public-action public-download-jump" href="#download-clients"><i class="ti ti-download"></i><span>دانلود برنامه</span></a>
    </div>
  </div>
  <div id="root">
    <div class="empty-state"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i>در حال بارگذاری...</div>
  </div>
  <div class="brand-contact public-brand-contact">
    <div class="brand-contact-identity"><img class="brand-contact-logo" src="https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png" alt="𝑭𝒊𝒏𝒆𝑽𝑷𝑵 logo" onerror="this.remove()"><div><div class="brand-contact-title">𝑭𝒊𝒏𝒆𝑽𝑷𝑵</div><div class="brand-contact-provider">ارائه‌دهنده: مـحـمـدصـادق افـغـان</div><div class="brand-contact-signature">𝑀𝑢ℎ𝑎𝑚𝑚𝑎𝑑𝒔𝒂𝒅𝒊𝒒</div></div></div>
    <div class="brand-contact-links"><a class="fine-tg-link" href="https://t.me/sadiq_AFG1" target="_blank" rel="noopener noreferrer"><i class="ti ti-brand-telegram"></i><span>پشتیبانی @sadiq_AFG1</span></a></div>
  </div>
  <section class="download-section" id="download-clients" aria-label="دانلود برنامه‌های سازگار">
    <div class="download-head">
      <div><div class="download-title">دانلود کلاینت‌های سازگار</div><div class="download-subtitle">نسخهٔ رسمی متناسب با دستگاهت را انتخاب کن</div></div>
      <span class="download-head-icon"><i class="ti ti-device-mobile-down"></i></span>
    </div>
    <div class="download-grid">
      <a class="download-card" href="https://github.com/2dust/v2rayNG/releases/latest" target="_blank" rel="noopener noreferrer"><span class="download-app-icon"><i class="ti ti-brand-android"></i></span><span class="download-app-copy"><span class="download-app-name">v2rayNG</span><span class="download-app-platform">Android · GitHub Releases</span></span><i class="ti ti-external-link download-open"></i></a>
      <a class="download-card" href="https://play.google.com/store/apps/details?id=app.hiddify.com" target="_blank" rel="noopener noreferrer"><span class="download-app-icon"><i class="ti ti-brand-android"></i></span><span class="download-app-copy"><span class="download-app-name">Hiddify</span><span class="download-app-platform">Android · Google Play</span></span><i class="ti ti-external-link download-open"></i></a>
      <a class="download-card" href="https://play.google.com/store/apps/details?id=dev.hexasoftware.v2box" target="_blank" rel="noopener noreferrer"><span class="download-app-icon"><i class="ti ti-brand-android"></i></span><span class="download-app-copy"><span class="download-app-name">V2Box</span><span class="download-app-platform">Android · Google Play</span></span><i class="ti ti-external-link download-open"></i></a>
      <a class="download-card" href="https://apps.apple.com/us/app/v2box-v2ray-client/id6446814690" target="_blank" rel="noopener noreferrer"><span class="download-app-icon"><i class="ti ti-brand-apple"></i></span><span class="download-app-copy"><span class="download-app-name">V2Box</span><span class="download-app-platform">iPhone · App Store</span></span><i class="ti ti-external-link download-open"></i></a>
      <a class="download-card" href="https://github.com/hiddify/hiddify-app/releases/latest" target="_blank" rel="noopener noreferrer"><span class="download-app-icon"><i class="ti ti-brand-windows"></i></span><span class="download-app-copy"><span class="download-app-name">Hiddify</span><span class="download-app-platform">Windows / Desktop · GitHub</span></span><i class="ti ti-external-link download-open"></i></a>
    </div>
  </section>
</div>
<script>
const UUID_KEY='{uuid_key}';
let savedPw='';

let publicLang='fa';try{{publicLang=localStorage.getItem('finevpn-lang')||'fa'}}catch(e){{}}
const isDark=true;
function applyTheme(){{document.documentElement.setAttribute('data-theme','dark');}}
function toggleTheme(){{applyTheme();}}
applyTheme();
const PUBLIC_I18N={{'تازه‌سازی':'Refresh','در حال بارگذاری...':'Loading...','گروه دسترسی':'Access Group','آخرین بروزرسانی:':'Last updated:','کپی لینک ساب':'Copy subscription link','QR کل':'Group QR','کپی همه‌ی کانفیگ‌ها':'Copy all configurations','تمام لینک‌های فعال این گروه را یک‌جا کپی کن':'Copy all active links at once','کپی همه':'Copy all','کانفیگ‌های فعال':'Active configs','اتصالات زنده':'Live connections','آنلاین':'Online','آفلاین':'Offline','کانفیگ آنلاین':'Online configs','کانفیگ آفلاین':'Offline configs','کانفیگ‌های مجاز':'Allowed configs','دارای اتصال واقعی در همین لحظه':'Connected right now','بدون نشست فعال':'No live session','مجموع آپلود و دانلود':'Upload + download total','سهم از حجم مشترک گروه':'Share of group quota','بدون محدودیت حجمی':'No traffic limit','کل مصرف':'Total usage','سهمیه و اعتبار گروه':'Group quota and validity','دانلود برنامه‌های سازگار':'Download compatible apps','برای واردکردن لینک اشتراک، برنامهٔ متناسب با دستگاه خود را از منبع رسمی دریافت کنید.':'Download a compatible client from its official store to import your subscription.','پشتیبانی @sadiq_AFG1':'Support @sadiq_AFG1','لینک کانفیگ':'Config link','لینک ساب کلاینت':'Client subscription link','کپی لینک':'Copy link','کپی ساب کلاینت':'Copy client subscription','نمایش لینک کانفیگ':'Show config link','پنهان کردن لینک':'Hide config link','ترافیک دانلود':'Download traffic','ترافیک آپلود':'Upload traffic','سرعت دانلود':'Download speed','سرعت آپلود':'Upload speed','آمار زندهٔ انتقال داده':'Live traffic statistics','حجم دانلود':'Download volume','حجم آپلود':'Upload volume','کانفیگ‌ها':'Configurations','عدد':'items','اتصال':'connection','مصرف شده':'used','سهمیه:':'Quota:','سهمیه: <b>نامحدود</b>':'Quota: <b>Unlimited</b>','اعتبار:':'Validity:','نامحدود':'Unlimited','روز مانده':'days left','اعتبار نامحدود':'Unlimited validity','محدودیت حجمی فعال نیست':'No traffic limit is active','مصرف‌شده:':'Used:','از':'of','QR کانفیگ':'Configuration QR','QR ساب':'Subscription QR','لینک کپی شد ✓':'Link copied ✓','لینک ساب کلاینت کپی شد ✓':'Client subscription copied ✓','همه‌ی':'all','کانفیگی برای کپی نیست':'No configurations to copy','داده تازه شد':'Data refreshed','تازه‌سازی ناموفق بود':'Refresh failed','خطا در بارگذاری':'Loading failed','آنلاین':'Online','فعال':'Active','غیرفعال':'Inactive','مصرف‌شده:':'Used:','سرعت از اختلاف شمارنده‌های واقعی بین درخواست‌های متوالی محاسبه می‌شود؛ در اولین بارگذاری ممکن است صفر باشد.':'Speed is calculated from real counter deltas between requests; it may be zero on first load.'}};
Object.assign(PUBLIC_I18N, {{"بستن":"Close","ارائه‌دهنده: مـحـمـدصـادق افـغـان":"Provider: Muhammad Sadiq Afghan","رمز اشتباه است":"Incorrect password","همه کانفیگ‌ها":"All configurations","نمودار سرعت واقعی":"Real-time speed chart","ساب گروه:":"Subscription group:","کانفیگ کپی شد ✓":"Configuration copied ✓","لینک ساب کپی شد ✓":"Subscription link copied ✓","اطلاعات تازه شد":"Information refreshed","خطا در بارگذاری":"Failed to load","کانفیگ کپی شد":"Configuration copied","تازه‌سازی ناموفق بود":"Refresh failed","همه‌ی":"all","داده تازه شد":"Data refreshed","آخرین بروزرسانی:":"Last updated:","محدودیت حجمی فعال نیست":"No traffic limit is active","مصرف شده":"used","سهمیه:":"Quota:","اعتبار:":"Validity:","مصرف‌شده:":"Used:","از":"of","اتصال":"connection","روز مانده":"days left","نامحدود":"Unlimited","فعال":"Active","غیرفعال":"Inactive","QR کانفیگ":"Configuration QR","QR ساب":"Subscription QR","آنلاین":"Online"}});
const PUBLIC_I18N_TEXT_ORIGINALS=new WeakMap();
function translatePublic(lang){{
  const walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);const nodes=[];
  while(walker.nextNode())nodes.push(walker.currentNode);
  for(const node of nodes){{
    const parent=node.parentElement;if(!parent||parent.closest('script,style,textarea,input,pre,code'))continue;
    if(!PUBLIC_I18N_TEXT_ORIGINALS.has(node))PUBLIC_I18N_TEXT_ORIGINALS.set(node,node.nodeValue||'');
    const original=PUBLIC_I18N_TEXT_ORIGINALS.get(node);const match=original.match(/^(\\s*)([\\s\\S]*?)(\\s*)$/);if(!match)continue;
    const raw=match[2].trim();if(!raw)continue;
    const next=lang==='en'?(PUBLIC_I18N[raw]||raw):raw;const value=match[1]+next+match[3];
    if(node.nodeValue!==value)node.nodeValue=value;
  }}
  document.documentElement.lang=lang;document.documentElement.dir=lang==='fa'?'rtl':'ltr';const lbl=document.getElementById('public-lang-label');if(lbl)lbl.textContent=lang==='fa'?'English':'فارسی';
}}
function togglePublicLanguage(){{publicLang=publicLang==='fa'?'en':'fa';try{{localStorage.setItem('finevpn-lang',publicLang)}}catch(e){{}}translatePublic(publicLang);applyTheme()}}
translatePublic(publicLang);

function toast(msg,type=''){{
  const t=document.getElementById('toast');
  t.textContent=msg;t.className='toast show'+(type?' '+type:'');
  setTimeout(()=>t.classList.remove('show'),2400);
}}
function esc(s){{return String(s||'').replace(/[&<>"']/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]))}}
function fmtB(b){{if(!b||b===0)return '0 B';if(b<1024)return b+' B';if(b<1024**2)return (b/1024).toFixed(1)+' KB';if(b<1024**3)return (b/1024**2).toFixed(2)+' MB';return (b/1024**3).toFixed(2)+' GB'}}
function fmtBps(b){{return fmtB(b)}}
function formatRemaining(seconds){{const n=Math.max(0,Math.floor(Number(seconds)||0));if(!n)return 'منقضی شده';const d=Math.floor(n/86400),h=Math.floor((n%86400)/3600),m=Math.floor((n%3600)/60);return (d?toFa(d)+' روز و ':'')+toFa(h)+' ساعت و '+toFa(m)+' دقیقه';}}
let trafficHistory=[];
function drawTrafficChart(d){{const c=document.getElementById('traffic-chart');if(!c)return;const ctx=c.getContext('2d');const vals=[Math.max(0,d.download_speed_bps||0),Math.max(0,d.upload_speed_bps||0)];trafficHistory.push(vals);if(trafficHistory.length>24)trafficHistory.shift();const w=c.width,h=c.height;ctx.clearRect(0,0,w,h);ctx.strokeStyle='rgba(148,163,184,.18)';ctx.lineWidth=1;for(let y=15;y<h;y+=25){{ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(w,y);ctx.stroke()}}const max=Math.max(1,...trafficHistory.flat());for(let series=0;series<2;series++){{ctx.beginPath();trafficHistory.forEach((pair,i)=>{{const x=trafficHistory.length<2?w/2:(i/(trafficHistory.length-1))*w;const y=h-5-(pair[series]/max)*(h-18);if(i===0)ctx.moveTo(x,y);else ctx.lineTo(x,y)}});ctx.strokeStyle=series===0?'#60a5fa':'#34d399';ctx.lineWidth=2;ctx.stroke()}}}}
function toFa(n){{return String(n).replace(/\\d/g,d=>'۰۱۲۳۴۵۶۷۸۹'[d])}}
function protoChip(p){{
  if(p==='xhttp-stream-up')return '<span class="proto-chip pc-ultra"><i class="ti ti-bolt"></i> XHTTP ULTRA</span>';
  if(p&&p.startsWith('xhttp'))return '<span class="proto-chip pc-xhttp">'+esc(p)+'</span>';
  return '<span class="proto-chip pc-ws">VLESS · WS</span>';
}}

function showQR(label,link){{
  document.getElementById('qr-label').textContent=label;
  document.getElementById('qr-img').src='/api/qr?data='+encodeURIComponent(link);
  document.getElementById('qr-modal').classList.add('open');
}}

function toggleLink(i){{
  const wrap=document.getElementById('vw-'+i);
  const btn=document.getElementById('vt-'+i);
  const open=wrap.classList.toggle('open');
  btn.classList.toggle('open',open);
  btn.querySelector('.ltl span').textContent = open ? 'پنهان کردن لینک' : 'نمایش لینک کانفیگ';
}}

async function loadData(pw=''){{
  const url='/api/public/sub/'+UUID_KEY+(pw?'?pw='+encodeURIComponent(pw):'');
  const started=performance.now();
  const r=await fetch(url,{{cache:'no-store'}});
  const data=await r.json();
  data.panel_rtt_ms=Math.max(0,Math.round(performance.now()-started));
  return data;
}}

function renderLock(name,errMsg=''){{
  document.getElementById('root').innerHTML=`
    <div class="lock-stage">
      <div class="lock-card">
        <div class="lock-banner">
          <div class="lock-shield"><i class="ti ti-shield-lock"></i></div>
          <div class="lock-title">${{esc(name)}}</div>
          <div class="lock-sub">این گروه با رمز محافظت شده. برای دیدن کانفیگ‌ها رمز رو وارد کنید.</div>
        </div>
        <div class="lock-form">
          <div class="lock-err" id="lock-err">${{errMsg ? '<i class="ti ti-alert-circle"></i> '+esc(errMsg) : ''}}</div>
          <div class="lock-field">
            <i class="ti ti-lock lock-lockicon"></i>
            <input class="lock-inp" type="password" id="lock-pw" placeholder="••••••••" autofocus>
            <button class="lock-eye" type="button" onclick="togglePwVis()"><i class="ti ti-eye" id="lock-eye-icon"></i></button>
          </div>
          <button class="btn btn-p lock-btn" onclick="submitLock()"><i class="ti ti-lock-open"></i> ورود به گروه</button>
        </div>
        <div class="lock-footer"><i class="ti ti-shield-check"></i> اتصال شما رمزنگاری‌شده است</div>
      </div>
    </div>
  `;
  const inp=document.getElementById('lock-pw');
  inp.addEventListener('keydown',e=>{{if(e.key==='Enter')submitLock()}});
}}

function togglePwVis(){{
  const inp=document.getElementById('lock-pw');
  const icon=document.getElementById('lock-eye-icon');
  const toText = inp.type==='password';
  inp.type = toText ? 'text' : 'password';
  icon.className = 'ti '+(toText ? 'ti-eye-off' : 'ti-eye');
}}

async function submitLock(){{
  const pw=document.getElementById('lock-pw').value;
  const data=await loadData(pw);
  if(data.locked){{renderLock(data.name,'رمز اشتباه است');return}}
  savedPw=pw;
  renderContent(data);
}}

function renderContent(d){{
  const activeCount=d.active_configs ?? d.links.filter(l=>l.active).length;
  const onlineCount=d.online_configs ?? d.links.filter(l=>l.online).length;
  const offlineCount=d.offline_configs ?? Math.max(0,d.links.length-onlineCount);
  const quotaPct=d.total_limit_bytes?Math.min(100,Math.max(0,(d.total_used_bytes||0)/d.total_limit_bytes*100)):0;
  const timePct=d.validity_seconds&&d.remaining_seconds!==null?Math.min(100,Math.max(0,(d.remaining_seconds||0)/d.validity_seconds*100)):0;
  window.latestPortalData=d;
  const baseSubUrl = d.sub_url || (window.location.protocol + '//' + window.location.host + '/sub-group/' + UUID_KEY);
  const subUrl = baseSubUrl + (savedPw ? '?pw=' + encodeURIComponent(savedPw) : '');

  window._finevpnSubUrl  = subUrl;
  window._finevpnSubName = d.name;
  window._finevpnLinks   = d.links.map(l => ({{
    vless : l.vless_link,
    sub   : l.sub_url + (savedPw ? '?pw=' + encodeURIComponent(savedPw) : ''),
    label : l.display_name || l.label,
  }}));

  document.getElementById('root').innerHTML=`
    <div class="sub-info">
      <div class="sub-eyebrow"><i class="ti ti-folders"></i> گروه دسترسی</div>
      <div class="sub-name">${{esc(d.name)}}</div>
      ${{d.desc ? `<div class="sub-desc">${{esc(d.desc)}}</div>` : ''}}
      <div class="sub-meta-row"><i class="ti ti-clock"></i> آخرین بروزرسانی: ${{new Date().toLocaleTimeString('fa-IR')}}</div>
      <div class="sub-sub-box">
        <span class="sub-sub-url">${{esc(subUrl)}}</span>
        <button class="btn btn-pur" style="padding:7px 12px;font-size:10.5px"
          onclick="navigator.clipboard.writeText(window._finevpnSubUrl).then(()=>toast('لینک ساب کپی شد ✓','ok'))">
          <i class="ti ti-copy"></i> کپی لینک ساب
        </button>
        <button class="btn btn-g" style="padding:7px 12px;font-size:10.5px"
          onclick="showQR(window._finevpnSubName + ' — کل گروه', window._finevpnSubUrl)">
          <i class="ti ti-qrcode"></i> QR کل
        </button>
      </div>
    </div>

    <div class="copy-all-bar">
      <div class="copy-all-text">
        <div class="copy-all-title"><i class="ti ti-copy"></i> کپی همه‌ی کانفیگ‌ها</div>
        <div class="copy-all-sub">تمام لینک‌های فعال این گروه را یک‌جا کپی کن</div>
      </div>
      <button class="copy-all-btn" onclick="copyAllConfigs()"><i class="ti ti-clipboard-copy"></i> کپی همه (${{toFa(activeCount)}})</button>
    </div>

    ${{d.expired ? '<div class="expired-banner"><i class="ti ti-alert-triangle"></i> اعتبار این اشتراک به پایان رسیده است؛ برای تمدید با پشتیبانی تماس بگیرید.</div>' : ''}}
    ${{d.quota_exhausted ? '<div class="expired-banner"><i class="ti ti-database-off"></i> سهمیهٔ حجمی این اشتراک تمام شده است.</div>' : ''}}
    <div class="portal-metrics" id="portal-metrics">
      <div class="portal-metric">
        <div class="portal-metric-head"><span><i class="ti ti-chart-donut-3"></i> مصرف سهمیهٔ مشترک</span><span class="metric-tag">LIVE USAGE</span></div>
        <div class="metric-flex">
          <div class="ring-gauge" style="--ring-value:${{quotaPct}};--ring-color:${{d.quota_exhausted?'#ff7189':'#39c8ff'}}"><div class="ring-core"><strong>${{d.total_limit_bytes?toFa(Math.round(quotaPct))+'٪':'∞'}}</strong><small>مصرف‌شده</small></div></div>
          <div class="metric-detail">
            <div class="metric-main-value">${{esc(d.total_used_fmt||fmtB(d.total_used_bytes||0))}}</div>
            <div class="metric-hint">از ${{d.total_limit_bytes?esc(d.total_limit_fmt):'حجم نامحدود'}}</div>
            <div class="metric-remaining">باقی‌مانده: ${{d.remaining_bytes===null?'نامحدود':esc(d.remaining_fmt||fmtB(d.remaining_bytes||0))}}</div>
          </div>
        </div>
        <div class="metric-split"><span>↑ آپلود: ${{esc(fmtB(d.upload_bytes||0))}}</span><span>↓ دانلود: ${{esc(fmtB(d.download_bytes||0))}}</span></div>
        ${{Number(d.unclassified_bytes||0)>0?`<div class="unclassified-note">${{esc(fmtB(d.unclassified_bytes))}} از مصرف تاریخی قبل از تفکیک دقیق آپلود/دانلود ثبت شده؛ به هیچ‌کدام از دو شمارنده نسبت داده نشده است.</div>`:''}}
      </div>
      <div class="portal-metric">
        <div class="portal-metric-head"><span><i class="ti ti-clock-hour-4"></i> اعتبار باقی‌مانده</span><span class="metric-tag">EXPIRY</span></div>
        <div class="metric-flex">
          <div class="ring-gauge" style="--ring-value:${{timePct}};--ring-color:${{d.expired?'#ff7189':'#a89cff'}}"><div class="ring-core"><strong>${{d.expires_at?(d.expired?'۰':toFa(Math.floor((d.remaining_seconds||0)/86400))):'∞'}}</strong><small>${{d.expires_at?'روز':'نامحدود'}}</small></div></div>
          <div class="metric-detail">
            <div class="metric-main-value" style="font-size:16px;color:${{d.expired?'#ff91a4':'#eeeaff'}}">${{d.expires_at?(d.expired?'منقضی شده':formatRemaining(d.remaining_seconds)):'نامحدود'}}</div>
            <div class="metric-hint">${{d.expires_at?'زمان دقیق تا پایان اعتبار':'بدون محدودیت زمانی'}}</div>
            <div class="metric-hint">${{d.expires_at?'تاریخ پایان: '+new Date((d.expires_at_unix||Math.floor(new Date(d.expires_at).getTime()/1000))*1000).toLocaleString('fa-IR'):'همیشه فعال از نظر زمان'}}</div>
          </div>
        </div>
      </div>
      <div class="portal-metric">
        <div class="portal-metric-head"><span><i class="ti ti-radar"></i> اتصال‌های زنده</span><span class="metric-tag">LIVE SESSIONS</span></div>
        <div class="metric-live-number">${{toFa(d.online_users??0)}}</div>
        <div class="metric-live-caption">IP یکتای متصل در همین لحظه</div>
        <div class="metric-session-pill"><i class="ti ti-plug-connected"></i> ${{toFa(d.active_sessions??d.active_connections??0)}} نشست فعال</div>
      </div>
    </div>

    <div class="speed-panel">
      <div class="cfg-title" style="margin:0 0 12px"><i class="ti ti-activity"></i> آمار زندهٔ انتقال داده</div>
      <div class="speed-grid">
        <div class="speed-chip"><label>سرعت دانلود</label><strong>${{esc(fmtBps(d.download_speed_bps||0))}}/s</strong></div>
        <div class="speed-chip"><label>سرعت آپلود</label><strong>${{esc(fmtBps(d.upload_speed_bps||0))}}/s</strong></div>
        <div class="speed-chip"><label>حجم دانلود</label><strong>${{esc(fmtB(d.download_bytes||0))}}</strong></div>
        <div class="speed-chip"><label>حجم آپلود</label><strong>${{esc(fmtB(d.upload_bytes||0))}}</strong></div>
      </div>
      <canvas id="traffic-chart" width="720" height="90" aria-label="نمودار سرعت واقعی" role="img"></canvas>
      <div class="stat-sub">سرعت از اختلاف شمارنده‌های واقعی بین درخواست‌های متوالی محاسبه می‌شود؛ در اولین بارگذاری ممکن است صفر باشد.</div>
    </div>

    <div class="cfg-title"><i class="ti ti-link"></i> کانفیگ‌ها (${{toFa(d.links.length)}} عدد)</div>
    <div class="cfg-grid">
      ${{d.links.map((l, i) => {{
        // A shared group quota belongs to the whole group, not to each config.
        // Only draw a per-config progress bar when that config has its own limit.
        const effectiveLimit = l.limit_bytes > 0 ? l.limit_bytes : 0;
        const pct = effectiveLimit > 0 ? Math.min(100, l.used_bytes / effectiveLimit * 100) : 0;
        const bc  = pct > 90 ? 'var(--red)' : pct > 70 ? 'var(--amber)' : 'var(--green)';
        const limitLabel = l.limit_bytes > 0 ? ('سهمیهٔ اختصاصی: ' + fmtB(l.limit_bytes)) : (d.total_limit_bytes > 0 ? 'حجم مشترک گروه · مصرف بالا جداگانه' : 'بدون محدودیت حجمی');
        return `
          <div class="cfg-card${{l.active ? '' : ' inactive'}}">
            <div class="cfg-top">
              <div class="cfg-head">
                <div>
                  <div class="cfg-label">${{esc(l.display_name || l.label)}}</div>
                  <div class="cfg-badges">
                    ${{protoChip(l.protocol)}}
                    ${{l.connections > 0 ? `<span class="conn-chip"><span class="dot"></span> ${{toFa(l.connections)}} اتصال</span>` : ''}}
                  </div>
                </div>
                <div class="cfg-status-stack">
                  <span class="cfg-status live ${{l.online ? 'online' : 'offline'}}">${{l.online ? '<i class="ti ti-wifi"></i> آنلاین' : '<i class="ti ti-wifi-off"></i> بدون نشست'}}</span>
                  <span class="cfg-status ${{l.expired ? 'no' : l.quota_exhausted ? 'no' : l.active ? 'ok' : 'no'}}">${{l.expired ? '<i class="ti ti-clock-x"></i> منقضی شده' : l.quota_exhausted ? '<i class="ti ti-database-off"></i> حجم تمام شده' : l.active ? '<i class="ti ti-circle-check"></i> مجاز' : '<i class="ti ti-circle-x"></i> غیرفعال'}}</span>
                </div>
              </div>
              <div class="cfg-usage">
                <div class="ubar"><div class="ubar-f" style="width:${{pct}}%;background:${{bc}}"></div></div>
                <div class="utxt"><span>مصرف این کانفیگ: ${{esc(l.used_fmt)}}</span><span>${{esc(limitLabel)}}</span></div>
              </div>
            </div>
            <div class="cfg-tear"></div>
            <div class="cfg-bottom">
              <button class="cfg-link-toggle" id="vt-${{i}}" onclick="toggleLink(${{i}})">
                <span class="ltl"><i class="ti ti-eye"></i> <span>نمایش لینک کانفیگ</span></span>
                <i class="ti ti-chevron-down"></i>
              </button>
              <div class="cfg-vless-wrap" id="vw-${{i}}">
                <div class="cfg-vless-inner">
                  <div class="cfg-link-label"><span class="ll-vless"><i class="ti ti-key"></i> لینک کانفیگ</span></div>
                  <div class="cfg-vless">${{esc(l.vless_link)}}</div>
                  <div class="cfg-link-label"><span class="ll-sub"><i class="ti ti-rss"></i> لینک ساب کلاینت</span></div>
                  <div class="cfg-vless is-sub">${{esc(l.sub_url)}}</div>
                </div>
              </div>
              <div class="cfg-actions">
                <button class="btn btn-p"
                  onclick="navigator.clipboard.writeText(window._finevpnLinks[${{i}}].vless).then(()=>toast('لینک کپی شد ✓','ok'))">
                  <i class="ti ti-copy"></i> کپی لینک
                </button>
                <button class="btn btn-pur"
                  onclick="navigator.clipboard.writeText(window._finevpnLinks[${{i}}].sub).then(()=>toast('لینک ساب کلاینت کپی شد ✓','ok'))">
                  <i class="ti ti-rss"></i> کپی ساب کلاینت
                </button>
                <button class="btn btn-g"
                  onclick="showQR(window._finevpnLinks[${{i}}].label, window._finevpnLinks[${{i}}].vless)">
                  <i class="ti ti-qrcode"></i> QR کانفیگ
                </button>
                <button class="btn btn-g"
                  onclick="showQR('ساب گروه: '+window._finevpnSubName, window._finevpnSubUrl)">
                  <i class="ti ti-rss"></i> QR ساب
                </button>
              </div>
            </div>
          </div>
        `;
      }}).join('')}}
    </div>
  `;
  drawTrafficChart(d);
  translatePublic(publicLang);
  setTimeout(() => autoRefresh(), 10000);
}}

function copyAllConfigs(){{
  const links=window._finevpnLinks||[];
  if(!links.length){{toast('کانفیگی برای کپی نیست','');return}}
  const text=links.map(l=>l.vless).join('\\n');
  navigator.clipboard.writeText(text).then(()=>toast('همه‌ی '+toFa(links.length)+' کانفیگ کپی شد ✓','ok'));
}}

let portalDiagnosticReport='';
function openPortalDiagnostics(){{const el=document.getElementById('diag-overlay');if(el)el.classList.add('open');runPortalDiagnostics();}}
function closePortalDiagnostics(){{const el=document.getElementById('diag-overlay');if(el)el.classList.remove('open');}}
function setDiagLine(label,state,text){{const cls=state==='ok'?'ok':state==='err'?'err':state==='busy'?'busy':'na';return `<div class="diag-line"><span>${{label}}</span><span class="diag-state ${{cls}}">${{text}}</span></div>`;}}
async function runPortalDiagnostics(){{
  const box=document.getElementById('diag-results');if(!box)return;
  box.innerHTML=setDiagLine('دسترسی اشتراک','busy','CHECKING')+setDiagLine('سلامت سرویس پنل','busy','CHECKING')+setDiagLine('اعتبار زمانی','busy','CHECKING')+setDiagLine('سهمیهٔ حجمی','busy','CHECKING')+setDiagLine('DNS مقصد / تونل VPN','na','NOT TESTED');
  const report=[];let subOk=false,healthOk=false,freshData=null;
  try{{
    const query=savedPw?'?pw='+encodeURIComponent(savedPw):'';
    const t=performance.now(),r=await fetch('/api/public/sub/'+UUID_KEY+query,{{cache:'no-store'}}),ms=Math.round(performance.now()-t),d=await r.json();
    subOk=r.ok&&!d.locked;report.push('Subscription endpoint: '+(subOk?'OK':'FAILED')+' · '+ms+' ms');
    if(subOk){{freshData=d;window.latestPortalData=d;}}
  }}catch(e){{report.push('Subscription endpoint: FAILED · '+String(e));}}
  try{{const t=performance.now(),r=await fetch('/health',{{cache:'no-store'}}),j=await r.json(),ms=Math.round(performance.now()-t);healthOk=r.ok&&j.status==='ok';report.push('Panel health: '+(healthOk?'OK':'FAILED')+' · '+ms+' ms');}}
  catch(e){{report.push('Panel health: FAILED · '+String(e));}}
  const d=freshData;
  const expiryOk=d?(!d.expires_at||(!d.expired&&Number(d.remaining_seconds)>0)):null;
  const quotaOk=d?(d.remaining_bytes===null||Number(d.remaining_bytes)>0):null;
  report.push('Expiry: '+(expiryOk===null?'NOT TESTED':expiryOk?'OK':'EXPIRED'));report.push('Quota: '+(quotaOk===null?'NOT TESTED':quotaOk?'OK':'EXHAUSTED'));
  box.innerHTML=setDiagLine('دسترسی اشتراک',subOk?'ok':'err',subOk?'OK':'FAILED')+
    setDiagLine('سلامت سرویس پنل',healthOk?'ok':'err',healthOk?'OK':'FAILED')+
    setDiagLine('اعتبار زمانی',expiryOk===null?'na':expiryOk?'ok':'err',expiryOk===null?'NOT TESTED':d.expires_at?(expiryOk?'VALID':'EXPIRED'):'UNLIMITED')+
    setDiagLine('سهمیهٔ حجمی',quotaOk===null?'na':quotaOk?'ok':'err',quotaOk===null?'NOT TESTED':d.remaining_bytes===null?'UNLIMITED':(quotaOk?'AVAILABLE':'EXHAUSTED'))+
    setDiagLine('DNS مقصد / تونل VPN','na','NOT TESTED')+
    setDiagLine('پینگ پنل',healthOk?'ok':'err',healthOk?'HTTP RTT؛ نه پینگ تونل':'UNAVAILABLE');
  report.push('DNS / VPN tunnel latency: NOT TESTED (browser cannot verify the remote tunnel from this page).');
  portalDiagnosticReport='FineVPN diagnostics\\n'+report.join('\\n');
}}
function copyPortalDiagnosticReport(){{if(!portalDiagnosticReport){{toast('ابتدا تست را اجرا کنید');return}}const clip=navigator.clipboard?.writeText;if(!clip){{toast('امکان کپی در این مرورگر نیست','err');return}}clip.call(navigator.clipboard,portalDiagnosticReport).then(()=>toast('گزارش عیب‌یابی کپی شد','ok')).catch(()=>toast('کپی گزارش ممکن نشد','err'));}}

async function refreshSubscription(){{
  const btn=document.getElementById('refresh-sub-btn');if(btn)btn.disabled=true;
  try{{const data=await loadData(savedPw);if(data.locked){{renderLock(data.name);return}}renderContent(data);toast(publicLang==='fa'?'اطلاعات تازه شد':'Data refreshed','ok')}}catch(e){{toast(publicLang==='fa'?'تازه‌سازی ناموفق بود':'Refresh failed','err')}}finally{{if(btn)btn.disabled=false}}
}}
async function autoRefresh(){{
  try{{
    const data = await loadData(savedPw);
    if (!data.locked) renderContent(data);
  }} catch(e) {{}}
}}

async function init(){{
  try{{
    const data = await loadData();
    if (data.locked) {{ renderLock(data.name); return; }}
    renderContent(data);
  }} catch(e) {{
    document.getElementById('root').innerHTML =
      '<div class="empty-state" style="color:var(--red-t)"><i class="ti ti-alert-circle"></i>خطا در بارگذاری</div>';
  }}
}}

init();
</script>
</body></html>"""
