# 𝑭𝒊𝒏𝒆𝑽𝑷𝑵 — Login, dashboard, and public subscription pages.

LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><link rel="icon" type="image/png" href="https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png"><link rel="apple-touch-icon" href="https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png"><meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
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
 linear-gradient(rgba(2,6,18,.78),rgba(2,6,18,.83));
 background-size:109px 109px,173px 173px,100% 100%;background-position:0 0,35px 61px,center;
 background-repeat:repeat,repeat,no-repeat;background-attachment:fixed;font-family:'Vazirmatn',sans-serif}
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

/* FineVPN visual refresh 1.0.0 */
:root{--bg:#070b18;--panel:#101a2d;--border:rgba(111,190,255,.16);--accent:#27c7f5;--accent-hover:#149dcc;--text:#edf6ff;--muted:#91a7c2;--glow:rgba(39,199,245,.18)}
body{background:radial-gradient(ellipse at 12% 8%,rgba(39,199,245,.13),transparent 34%),radial-gradient(ellipse at 88% 92%,rgba(135,92,255,.13),transparent 36%),#070b18!important;color:var(--text)}
.card{background:linear-gradient(145deg,rgba(19,33,56,.94),rgba(10,18,34,.96))!important;border:1px solid rgba(115,196,255,.2)!important;border-radius:26px!important;box-shadow:0 24px 80px rgba(0,0,0,.48),inset 0 1px rgba(255,255,255,.045)!important;backdrop-filter:blur(22px)}
.brand-logo{background:linear-gradient(135deg,#20c9f4,#6258e8)!important;box-shadow:0 8px 32px rgba(39,199,245,.28)!important}
.brand-title{letter-spacing:.02em;text-shadow:0 0 26px rgba(39,199,245,.18)}
.fi{background:rgba(4,12,25,.68)!important;border:1px solid rgba(126,183,229,.2)!important;border-radius:14px!important;min-height:48px}
.fi:focus{border-color:#27c7f5!important;box-shadow:0 0 0 4px rgba(39,199,245,.12)!important}
button,.btn-p{border-radius:14px!important;min-height:44px;transition:transform .18s ease,box-shadow .18s ease,filter .18s ease}
.btn-p{background:linear-gradient(115deg,#20c9f4,#5965ed)!important;box-shadow:0 10px 28px rgba(39,150,245,.22)!important;font-weight:800}
.btn-p:hover{transform:translateY(-2px);filter:brightness(1.08);box-shadow:0 14px 34px rgba(39,150,245,.3)!important}
a:focus-visible,button:focus-visible,input:focus-visible{outline:2px solid #57d8ff;outline-offset:3px}
@media(max-width:480px){body{padding:14px}.card{padding:28px 20px!important;border-radius:22px!important}.brand-title{font-size:21px}}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{scroll-behavior:auto!important;animation-duration:.01ms!important;transition-duration:.01ms!important}}

/* FineVPN 1.0.0 — unified login skin */
:root{--bg:#060b18;--panel:#0d1b31;--border:rgba(94,177,239,.22);--accent:#32c9f4;--text:#f2f8ff;--muted:#91aac7}
html,body{background:#060b18!important;color:#f2f8ff!important;font-family:'Vazirmatn',system-ui,sans-serif!important}
body{background:radial-gradient(ellipse at 14% 8%,rgba(42,174,238,.16),transparent 39%),radial-gradient(ellipse at 88% 90%,rgba(125,92,255,.12),transparent 36%),#060b18!important;padding:clamp(14px,4vw,28px)!important}
.card{width:min(100%,460px)!important;padding:clamp(24px,5vw,38px)!important;border-radius:26px!important;background:linear-gradient(145deg,rgba(17,37,65,.94),rgba(7,17,34,.97))!important;border:1px solid rgba(98,185,242,.24)!important;box-shadow:0 26px 82px rgba(0,0,0,.48),inset 0 1px rgba(255,255,255,.06)!important;backdrop-filter:blur(20px)!important;-webkit-backdrop-filter:blur(20px)!important}
.brand-logo{width:84px!important;height:84px!important;border-radius:22px!important;border:1px solid rgba(104,216,255,.38)!important;background:linear-gradient(145deg,rgba(38,180,234,.16),rgba(125,94,245,.16))!important;box-shadow:0 0 0 5px rgba(48,179,235,.06),0 0 28px rgba(45,174,239,.20)!important;overflow:hidden!important}
.brand-title{font-size:25px!important;font-weight:950!important;color:#f5faff!important;letter-spacing:.025em!important;text-shadow:0 0 25px rgba(51,201,244,.16)!important}
.brand-sub{color:#8da9c7!important;font-size:12px!important;line-height:1.9!important}
.fl{color:#b6cce4!important;font-size:12px!important;font-weight:800!important}
.fi{min-height:48px!important;padding:12px 44px 12px 14px!important;border-radius:13px!important;background:rgba(3,12,27,.72)!important;border:1px solid rgba(109,180,227,.23)!important;color:#f4f9ff!important;font-size:13px!important}
.fi:focus{border-color:#45d4ff!important;box-shadow:0 0 0 3px rgba(50,201,244,.14)!important}
.fi-wrap i{color:#71dfff!important}
.btn-p{min-height:48px!important;border-radius:14px!important;background:linear-gradient(120deg,#31c9f3,#397de9 58%,#6d69ef)!important;color:#06182a!important;border:1px solid rgba(160,230,255,.48)!important;font-weight:950!important;box-shadow:0 10px 27px rgba(37,152,234,.24),inset 0 1px rgba(255,255,255,.38)!important}
.btn-p:hover{filter:brightness(1.08)!important;transform:translateY(-1px)!important}
.hint-box{background:rgba(42,173,225,.08)!important;border:1px solid rgba(91,184,237,.22)!important;color:#9ee4ff!important;border-radius:13px!important}
.login-contact{border-top-color:rgba(98,181,237,.18)!important}
.login-provider{color:#a8bfd9!important}.login-provider strong,.login-signature{color:#8fe3ff!important}
.login-links a{background:rgba(43,149,207,.10)!important;border-color:rgba(92,187,238,.24)!important;color:#c0ebff!important;border-radius:11px!important}
.login-password-toggle{background:rgba(47,164,218,.12)!important;border:1px solid rgba(100,187,233,.24)!important;color:#a8e7ff!important;border-radius:9px!important}
@media(max-width:420px){.card{padding:25px 18px!important;border-radius:21px!important}.brand-logo{width:76px!important;height:76px!important}.brand-title{font-size:22px!important}}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important}}


/* Final login field alignment: keep the eye control clear of the password text. */
.login-password-wrap{position:relative!important;width:100%!important;min-width:0!important}
.login-password-wrap .fi{width:100%!important;min-width:0!important;direction:ltr!important;text-align:left!important;padding-left:56px!important;padding-right:46px!important;letter-spacing:.02em}
.login-password-wrap .login-lock-icon{right:13px!important;left:auto!important;width:20px;text-align:center;z-index:1}
.login-password-toggle{left:8px!important;right:auto!important;top:50%!important;transform:translateY(-50%)!important;width:38px!important;height:38px!important;min-height:38px!important;padding:0!important;border-radius:11px!important;display:grid!important;place-items:center!important;background:linear-gradient(145deg,rgba(43,190,241,.18),rgba(106,91,239,.17))!important;border:1px solid rgba(102,202,255,.35)!important;color:#a8eaff!important;box-shadow:inset 0 1px rgba(255,255,255,.13),0 5px 16px rgba(0,0,0,.22)!important}
.login-password-toggle i{font-size:18px!important;line-height:1!important;position:static!important;pointer-events:none!important}
.login-password-toggle:hover{filter:brightness(1.18);border-color:rgba(110,220,255,.62)!important}
.login-password-toggle:focus-visible{outline:2px solid #58d8ff!important;outline-offset:3px!important}
.btn-p{letter-spacing:0!important;font-size:13px!important}
@media(max-width:360px){.login-password-wrap .fi{padding-left:52px!important;padding-right:42px!important}.login-password-toggle{width:36px!important;height:36px!important}}


/* FineVPN v1.0 — unified glass identity and responsive polish */
:root{--fine-cyan:#73dcff;--fine-blue:#4c9dff;--fine-violet:#9885ff;--fine-glass:rgba(12,29,54,.84)}
body{position:relative;isolation:isolate;background:radial-gradient(ellipse 62% 42% at 12% 8%,rgba(45,158,240,.20),transparent 68%),radial-gradient(ellipse 48% 46% at 92% 92%,rgba(123,91,244,.16),transparent 70%),linear-gradient(145deg,#050b18,#08172c 58%,#0a1022)!important}
body:before,body:after{content:"";position:fixed;z-index:-1;pointer-events:none;border-radius:50%;filter:blur(2px)}
body:before{width:min(62vw,650px);height:min(62vw,650px);top:-34vw;right:-17vw;border:1px solid rgba(104,205,255,.12);box-shadow:0 0 0 32px rgba(104,205,255,.018),0 0 0 68px rgba(104,205,255,.012)}
body:after{width:min(48vw,480px);height:min(48vw,480px);bottom:-30vw;left:-15vw;border:1px solid rgba(160,137,255,.12);box-shadow:0 0 0 28px rgba(160,137,255,.018),0 0 0 62px rgba(160,137,255,.012)}
.card{position:relative;overflow:hidden;max-width:440px;padding:clamp(26px,5vw,38px)!important;border:1px solid rgba(113,194,245,.24)!important;border-radius:28px!important;background:linear-gradient(148deg,rgba(17,40,72,.91),rgba(6,17,36,.94))!important;box-shadow:0 28px 90px rgba(0,0,0,.48),inset 0 1px rgba(255,255,255,.09)!important;backdrop-filter:blur(24px)!important;-webkit-backdrop-filter:blur(24px)!important}
.card:before{content:"";position:absolute;top:0;left:12%;right:12%;height:1px;background:linear-gradient(90deg,transparent,#72dcff,#a99cff,transparent);opacity:.9}
.brand-logo{width:76px!important;height:76px!important;border-radius:23px!important;margin-bottom:18px!important;background:linear-gradient(145deg,rgba(66,190,246,.2),rgba(132,108,255,.18))!important;border:1px solid rgba(117,216,255,.38)!important;box-shadow:0 0 0 7px rgba(75,171,238,.06),0 14px 35px rgba(25,124,214,.22)!important}
.fine-logo-mark{display:block;width:100%;height:100%;filter:drop-shadow(0 5px 10px rgba(56,174,238,.22))}
.brand-title{font-size:25px!important;letter-spacing:.01em;text-shadow:0 4px 26px rgba(91,198,255,.2)}
.brand-version{display:inline-flex;align-items:center;justify-content:center;margin:3px auto 7px;padding:3px 10px;border-radius:99px;border:1px solid rgba(106,204,248,.24);background:rgba(55,162,220,.11);color:#a8eaff;font-size:10px;font-weight:900;letter-spacing:.06em}
.brand-sub{font-size:12px!important;color:#a9c8e5!important;line-height:1.9}
.fl{color:#b8cee5!important;font-size:12px!important}
.fi{min-height:48px!important;border-radius:14px!important;background:rgba(4,14,30,.64)!important;border-color:rgba(113,178,225,.23)!important;color:#f5fbff!important}
.fi:focus{border-color:rgba(102,216,255,.82)!important;box-shadow:0 0 0 4px rgba(77,188,245,.13)!important}
.btn-p{min-height:49px!important;border-radius:14px!important;background:linear-gradient(112deg,#77e4ff 0%,#55a9f8 54%,#8e82ff 100%)!important;color:#06172a!important;border:1px solid rgba(200,243,255,.58)!important;box-shadow:0 12px 28px rgba(44,150,230,.24),inset 0 1px rgba(255,255,255,.65)!important;font-weight:900!important}
.btn-p:hover{filter:brightness(1.06);transform:translateY(-1px)}
.login-contact{border-top-color:rgba(117,194,240,.16)!important}
.login-links a{border-color:rgba(117,194,240,.22)!important;background:rgba(56,148,215,.11)!important;color:#c9efff!important}
button:focus-visible,a:focus-visible,input:focus-visible{outline:2px solid #86e5ff!important;outline-offset:3px!important}
@media(max-width:480px){body{padding:max(12px,env(safe-area-inset-top)) 12px max(12px,env(safe-area-inset-bottom))}.card{padding:25px 19px!important;border-radius:23px!important}.brand-logo{width:68px!important;height:68px!important}.brand-title{font-size:22px!important}}
@media(prefers-reduced-motion:reduce){*,*:before,*:after{animation:none!important;transition:none!important}}


/* FineVPN 𝒗₂.₀ — blue glass login */
:root{--fine-blue:#55baff;--fine-cyan:#82e8ff;--fine-violet:#829cff}
html,body{background:#040b1b!important;color:#f4f9ff!important;font-family:'Vazirmatn',system-ui,sans-serif!important}
body{position:relative;isolation:isolate;overflow:hidden;background:radial-gradient(ellipse 70% 48% at 50% 0%,rgba(24,104,207,.25),transparent 68%),linear-gradient(145deg,#030817,#071a35 58%,#060c22)!important}
body:before,body:after{content:"";position:fixed;z-index:-1;pointer-events:none;border-radius:50%;border:1px solid rgba(102,204,255,.12);box-shadow:0 0 0 25px rgba(82,172,244,.025),0 0 0 58px rgba(82,172,244,.018),0 0 0 96px rgba(82,172,244,.012)}
body:before{width:min(72vw,720px);height:min(72vw,720px);right:-18vw;top:-34vw}
body:after{width:min(52vw,520px);height:min(52vw,520px);left:-17vw;bottom:-29vw;border-color:rgba(135,147,255,.12)}
.card{position:relative;isolation:isolate;overflow:hidden;width:min(100%,460px)!important;padding:clamp(25px,5vw,40px)!important;border-radius:30px!important;border:1px solid rgba(108,196,255,.28)!important;background:linear-gradient(145deg,rgba(15,43,78,.82),rgba(5,15,36,.91))!important;box-shadow:0 30px 100px rgba(0,0,0,.48),0 0 60px rgba(27,126,230,.12),inset 0 1px rgba(255,255,255,.12)!important;backdrop-filter:blur(28px)!important;-webkit-backdrop-filter:blur(28px)!important}
.card:before{content:"";position:absolute;z-index:-1;width:280px;height:280px;right:50%;top:-205px;transform:translateX(50%);border-radius:50%;border:1px solid rgba(103,211,255,.15);box-shadow:0 0 0 18px rgba(85,183,249,.025),0 0 0 42px rgba(85,183,249,.018)}
.brand-logo{width:88px!important;height:88px!important;border-radius:24px!important;overflow:hidden!important;background:rgba(53,151,225,.12)!important;border:1px solid rgba(127,221,255,.42)!important;box-shadow:0 0 0 7px rgba(60,165,237,.06),0 0 36px rgba(45,158,246,.25)!important}
.brand-logo img{object-fit:contain!important}
.brand-title{color:#f4fbff!important;text-shadow:0 0 30px rgba(101,201,255,.25)!important;letter-spacing:.025em!important}
.brand-version{border-color:rgba(119,208,255,.32)!important;background:rgba(48,149,223,.14)!important;color:#a9e8ff!important}
.brand-sub,.fl{color:#aac7e4!important}
.fi{background:rgba(3,15,35,.68)!important;border:1px solid rgba(119,185,237,.25)!important;color:#f5fbff!important;border-radius:15px!important;min-height:50px!important}
.fi:focus{border-color:rgba(109,218,255,.78)!important;box-shadow:0 0 0 4px rgba(58,166,240,.14)!important}
.btn-p{background:linear-gradient(115deg,#6ee0ff,#398ff0 58%,#817dff)!important;color:#04162d!important;border:1px solid rgba(199,244,255,.65)!important;box-shadow:0 12px 32px rgba(43,146,231,.3),inset 0 1px rgba(255,255,255,.68)!important;border-radius:15px!important;min-height:50px!important;font-weight:950!important}
.btn-p:hover{transform:translateY(-2px);filter:brightness(1.08)}
.login-contact{border-color:rgba(108,192,245,.18)!important}.login-provider,.login-signature{color:#a5c9e9!important}.login-provider strong{color:#9feaff!important}
.login-links a{background:rgba(52,147,224,.11)!important;border:1px solid rgba(104,196,248,.25)!important;color:#c9efff!important;border-radius:13px!important}
@media(max-width:480px){body{padding:max(12px,env(safe-area-inset-top)) 12px max(12px,env(safe-area-inset-bottom))!important}.card{border-radius:24px!important;padding:25px 18px!important}.brand-logo{width:76px!important;height:76px!important}}
.fine-logo-mark{object-fit:contain!important;display:block!important;width:100%!important;height:100%!important}

</style>
<style>

/* FineVPN v2.0 — login glass identity */
:root{--login-blue:#55caff;--login-ice:#9ceaff}
html,body{min-height:100%;background:#030916!important;color:#f2f8ff}
body{position:relative;isolation:isolate;overflow:hidden;background:
 radial-gradient(ellipse at 50% 0%,rgba(27,119,221,.28),transparent 42%),
 radial-gradient(ellipse at 5% 100%,rgba(17,193,213,.13),transparent 36%),
 linear-gradient(145deg,#020713,#071a35 55%,#030a1c)!important}
body:before,body:after{content:"";position:fixed;z-index:-1;pointer-events:none;border-radius:50%;border:1px solid rgba(103,205,255,.13);box-shadow:0 0 0 22px rgba(83,175,239,.025),0 0 0 54px rgba(83,175,239,.018),0 0 0 92px rgba(83,175,239,.012)}
body:before{width:min(82vw,760px);height:min(82vw,760px);right:-27vw;top:-42vw}
body:after{width:min(58vw,540px);height:min(58vw,540px);left:-20vw;bottom:-32vw;border-color:rgba(129,153,255,.15)}
.card{position:relative;overflow:hidden;max-width:470px;padding:38px 34px!important;border-radius:30px!important;background:linear-gradient(145deg,rgba(13,38,73,.84),rgba(4,15,34,.88))!important;border:1px solid rgba(103,194,255,.34)!important;box-shadow:0 30px 100px rgba(0,0,0,.46),0 0 45px rgba(40,143,237,.13),inset 0 1px rgba(255,255,255,.12)!important;backdrop-filter:blur(28px)!important;-webkit-backdrop-filter:blur(28px)!important}
.card:before{content:"";position:absolute;inset:0 12% auto;height:1px;background:linear-gradient(90deg,transparent,#8be8ff,transparent);pointer-events:none}
.brand{margin-bottom:30px}.brand-logo{width:104px!important;height:104px!important;border-radius:28px!important;background:rgba(31,133,211,.15)!important;border:1px solid rgba(112,214,255,.5)!important;box-shadow:0 0 0 8px rgba(62,157,228,.06),0 0 42px rgba(46,163,248,.25)!important;padding:8px}
.brand-logo img{object-fit:contain!important;filter:drop-shadow(0 0 12px rgba(83,194,255,.34))}
.brand-title{font-size:28px!important;font-weight:950!important;color:#f6fbff!important;text-shadow:0 0 24px rgba(82,191,255,.2)}
.brand-version{background:rgba(57,151,225,.15)!important;border:1px solid rgba(105,200,255,.3)!important;color:#b4edff!important}
.brand-sub{font-size:12.5px!important;color:#a9c9e8!important;line-height:2}
.fl{color:#bcd5ee!important}.fi{background:rgba(2,13,31,.65)!important;border:1px solid rgba(113,193,247,.24)!important;color:#f6fbff!important;border-radius:14px!important;padding-top:14px!important;padding-bottom:14px!important}
.fi:focus{border-color:#66d9ff!important;box-shadow:0 0 0 4px rgba(68,171,235,.14)!important}
.fi-wrap i{color:#88d9ff!important}.btn-p{min-height:48px;border-radius:14px!important;background:linear-gradient(110deg,#6de1ff,#348ce9 60%,#797fff)!important;color:#03172e!important;border:1px solid rgba(195,241,255,.58)!important;box-shadow:0 10px 30px rgba(36,133,222,.28),inset 0 1px rgba(255,255,255,.55)!important;font-weight:950!important}
.btn-p:hover{filter:brightness(1.08);box-shadow:0 14px 36px rgba(36,133,222,.36)!important}
.login-contact{border-color:rgba(106,190,244,.2)!important}.login-provider,.login-signature{color:#a5c5e4!important}.login-provider strong{color:#b9eeff!important}
.login-links a{background:rgba(46,143,219,.12)!important;border:1px solid rgba(111,197,250,.25)!important;color:#d2f2ff!important}
@media(max-width:520px){body{padding:14px!important}.card{padding:30px 22px!important;border-radius:24px!important}.brand-logo{width:88px!important;height:88px!important}.brand-title{font-size:24px!important}}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}


.brand-logo{border-radius:50%!important;padding:7px!important;overflow:hidden!important;border:1px solid rgba(128,224,255,.68)!important;background:linear-gradient(145deg,rgba(58,168,232,.28),rgba(75,96,210,.18))!important;box-shadow:0 0 0 8px rgba(59,164,232,.055),0 0 40px rgba(52,166,245,.3),inset 0 2px 8px rgba(255,255,255,.18)!important}
.brand-logo img{width:100%!important;height:100%!important;object-fit:contain!important;filter:drop-shadow(0 0 12px rgba(92,206,255,.42))}
</style>
</head>
<body>
<div class="card">
  <div class="brand">
    <div class="brand-logo"><img class="fine-logo-mark" src="https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png" alt="لوگوی اصلی FineVPN" loading="eager" decoding="async" style="width:100%;height:100%;object-fit:contain;display:block"></div>
    <div class="brand-title">𝑭𝒊𝒏𝒆𝑽𝑷𝑵</div>
    <div class="brand-version">𝒗₂.₀</div>
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
        <button type="button" class="login-password-toggle" onclick="toggleLoginPassword()" aria-label="نمایش رمز" aria-pressed="false" title="نمایش / پنهان کردن رمز"><i class="ti ti-eye" id="login-password-eye" aria-hidden="true"></i></button>
      </div>
    </div>
    <button type="submit" class="btn-p" id="lbtn"><i class="ti ti-login"></i> <span>ورود به پنل مدیریت</span></button>
    <div class="err-box" id="err-box"><i class="ti ti-alert-circle"></i><span id="err-text">ورود ناموفق</span></div>
  </form>
  <div class="login-contact">
    <div class="login-provider">ارائه‌دهنده: <strong>مـحـمـدصـادق افـغـان</strong></div>
    <div class="login-signature">𝑀𝑢ℎ𝑎𝑚𝑚𝑎𝑑𝒔𝒂𝒅𝒊𝒒</div>
    <div class="login-links"><a href="https://t.me/sadiq_AFG1" target="_blank" rel="noopener noreferrer"><i class="ti ti-brand-telegram"></i> پشتیبانی</a></div>
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
  icon.className='ti '+(reveal?'ti-eye-off':'ti-eye');
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
<meta charset="UTF-8"><link rel="icon" type="image/png" href="https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png"><link rel="apple-touch-icon" href="https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png"><meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>FineVPN · پنل مدیریت · 𝒗₂.₀</title>
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
    none;
  background-size:109px 109px,173px 173px,100% 100%;
  background-position:0 0,35px 61px,center;
  background-repeat:repeat,repeat,no-repeat;background-attachment:fixed;
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
body::after{content:"F";position:fixed;z-index:0;pointer-events:none;width:clamp(230px,34vw,520px);aspect-ratio:1;left:50%;top:54%;transform:translate(-50%,-50%);border:1px solid rgba(104,195,255,.045);border-radius:50%;display:grid;place-items:center;color:rgba(104,195,255,.035);font-size:clamp(180px,24vw,320px);font-weight:950;mix-blend-mode:screen}
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


/* FineVPN visual refresh 1.0.0 */
:root{--bg:#070b18;--bg2:#0b1426;--bg3:#12223a;--card:rgba(16,29,50,.88);--card-b:rgba(100,185,255,.17);--card-bh:rgba(50,202,245,.42);--accent:#27c7f5;--accent2:#67dcff;--accent-d:rgba(39,199,245,.11);--green:#25d6a2;--green-bg:rgba(37,214,162,.1);--green-t:#71f0c7;--purple:#a78bfa;--purple-bg:rgba(167,139,250,.12);--red:#fb7185;--red-bg:rgba(251,113,133,.1);--amber:#fbbf24;--amber-bg:rgba(251,191,36,.1);--t1:#edf6ff;--t2:#a5bad3;--t3:#7189a8;--shadow:0 16px 44px rgba(0,0,0,.28);--radius:18px}
html,body{background:#070b18!important}
body{background:radial-gradient(ellipse at 80% 0%,rgba(48,111,208,.11),transparent 34%),radial-gradient(ellipse at 0% 90%,rgba(39,199,245,.07),transparent 30%),#070b18!important}
.sidebar{background:rgba(9,18,34,.96)!important;border-left:1px solid rgba(100,185,255,.16)!important;backdrop-filter:blur(20px);box-shadow:12px 0 44px rgba(0,0,0,.18)}
.logo{border-bottom-color:rgba(100,185,255,.15)!important}
.logo-img{border-radius:14px!important;box-shadow:0 0 22px rgba(39,199,245,.24)!important}
.logo-name{font-size:15px!important;letter-spacing:.02em}
.nav-it{border-radius:11px!important;margin:3px 8px!important;padding:10px 13px!important;min-height:42px;transition:background .18s,border-color .18s,color .18s,transform .18s}
.nav-it:hover{transform:translateX(-2px);background:rgba(39,199,245,.09)!important;color:#dff8ff!important}
.nav-it.on{background:linear-gradient(100deg,rgba(39,199,245,.17),rgba(101,99,235,.09))!important;border-right-color:#27c7f5!important;color:#effbff!important;box-shadow:inset 0 0 0 1px rgba(39,199,245,.08)}
.sb-foot{border-top-color:rgba(100,185,255,.15)!important}
.theme-btn,.logout-btn{border-radius:12px!important;min-height:40px}
.main,.main-content,.content,.page-content{background:transparent}
.topbar,.header,.page-head{border-color:rgba(100,185,255,.12)!important}
.card,.stat-card,.panel,.modal,.modal-content,.table-wrap,.chart-card,.section-card{background:linear-gradient(145deg,rgba(17,32,55,.9),rgba(10,20,37,.92))!important;border:1px solid rgba(105,181,239,.16)!important;border-radius:18px!important;box-shadow:0 12px 34px rgba(0,0,0,.2),inset 0 1px rgba(255,255,255,.025)!important;backdrop-filter:blur(14px)}
button,.btn,.btn-primary,.btn-p,.action-btn,.icon-btn,.theme-btn,.logout-btn,select{border-radius:12px!important;font-family:inherit;transition:transform .16s ease,box-shadow .16s ease,background .16s ease,border-color .16s ease}
button:not(:disabled),.btn:not(:disabled),.btn-primary:not(:disabled),.btn-p:not(:disabled),.action-btn:not(:disabled){cursor:pointer}
button:hover:not(:disabled),.btn:hover:not(:disabled),.btn-primary:hover:not(:disabled),.btn-p:hover:not(:disabled),.action-btn:hover:not(:disabled){filter:brightness(1.08);transform:translateY(-1px)}
button:active:not(:disabled),.btn:active:not(:disabled){transform:translateY(0)}
input,select,textarea{border-radius:12px!important;border-color:rgba(120,175,225,.2)!important;background:rgba(4,12,25,.58)!important;color:var(--t1)!important;max-width:100%}
input:focus,select:focus,textarea:focus{border-color:#27c7f5!important;box-shadow:0 0 0 3px rgba(39,199,245,.12)!important;outline:none}
table{border-collapse:separate;border-spacing:0}
th{color:#9fc5e8!important}
td,th{border-color:rgba(110,170,220,.12)!important}
.badge,.pill,.status{border-radius:999px}
a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible{outline:2px solid #57d8ff;outline-offset:3px}
@media(max-width:1050px){:root{--sidebar-w:230px}}
@media(max-width:760px){body{font-size:13px}.sidebar{box-shadow:0 18px 50px rgba(0,0,0,.45)}.card,.stat-card,.panel,.chart-card,.section-card{border-radius:15px!important}.main,.main-content,.content{min-width:0;max-width:100%;overflow-x:hidden}button,.btn,.btn-primary,.btn-p,.action-btn{min-height:40px}.table-wrap{max-width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch}}
@media(max-width:420px){.logo{padding:16px 12px 13px}.nav-it{padding:9px 11px!important}.card,.panel{padding:14px!important}}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{scroll-behavior:auto!important;animation-duration:.01ms!important;transition-duration:.01ms!important}}

/* FineVPN 1.0.0 — coherent neon-glass system v2 */
:root{
  --bg:#060b18!important;--bg2:#0a1428!important;--bg3:#10213b!important;
  --card:rgba(13,27,49,.88)!important;--card-b:rgba(94,177,239,.20)!important;--card-bh:rgba(51,207,255,.48)!important;
  --accent:#32c9f4!important;--accent2:#86e7ff!important;--accent-d:rgba(50,201,244,.13)!important;
  --green:#35ddb2!important;--green-bg:rgba(53,221,178,.12)!important;--green-t:#76f0d0!important;
  --purple:#9c8aff!important;--purple-bg:rgba(156,138,255,.13)!important;
  --red:#ff718c!important;--red-bg:rgba(255,113,140,.12)!important;--red-t:#ff9caf!important;
  --amber:#ffc76b!important;--amber-bg:rgba(255,199,107,.12)!important;--amber-t:#ffda9a!important;
  --t1:#f2f8ff!important;--t2:#adc3de!important;--t3:#718aa9!important;
  --shadow:0 18px 48px rgba(0,0,0,.30)!important;--radius:20px!important;
}
html,body{background:#060b18!important;color:#f2f8ff!important}
body{
  background:
    radial-gradient(ellipse 60% 36% at 12% 0%,rgba(32,158,235,.13),transparent 70%),
    radial-gradient(ellipse 45% 38% at 92% 92%,rgba(116,88,255,.10),transparent 72%),
    #060b18!important;
  font-family:'Vazirmatn',system-ui,sans-serif!important;
}
body::after{opacity:.018!important;filter:grayscale(1)!important}
.sidebar{
  background:linear-gradient(180deg,rgba(11,23,43,.98),rgba(7,15,30,.98))!important;
  border-left:1px solid rgba(92,177,239,.20)!important;
  box-shadow:12px 0 44px rgba(0,0,0,.24)!important;
  backdrop-filter:blur(22px)!important;-webkit-backdrop-filter:blur(22px)!important;
}
.logo{padding:22px 18px 18px!important;border-bottom:1px solid rgba(95,180,242,.16)!important}
.logo-img,.mob-logo{
  border:1px solid rgba(91,214,255,.50)!important;
  box-shadow:0 0 0 4px rgba(44,177,238,.07),0 0 25px rgba(43,190,249,.28)!important;
  background:linear-gradient(145deg,rgba(39,188,244,.2),rgba(126,97,255,.2))!important;
}
.logo-name,.mob-title{font-weight:900!important;letter-spacing:.035em!important;color:#f1f8ff!important}
.logo-sub{color:#7f9bb9!important}
.nav-wrap{padding:12px 0!important}
.nav-sec{color:#6683a5!important;padding:17px 18px 7px!important;font-size:9px!important;letter-spacing:.14em!important}
.nav-it{
  margin:3px 10px!important;padding:11px 14px!important;min-height:44px!important;
  border:1px solid transparent!important;border-right:3px solid transparent!important;
  border-radius:12px!important;color:#91a9c4!important;font-weight:650!important;
}
.nav-it i{font-size:17px!important}
.nav-it:hover{background:rgba(47,190,244,.08)!important;color:#e3f7ff!important;transform:translateX(-2px)!important}
.nav-it.on{background:linear-gradient(105deg,rgba(37,188,242,.17),rgba(119,97,255,.10))!important;border-color:rgba(79,187,242,.15)!important;border-right-color:#42d4ff!important;color:#f3fbff!important;box-shadow:inset 0 1px rgba(255,255,255,.07),0 8px 20px rgba(0,0,0,.15)!important}
.nav-badge{background:rgba(53,221,178,.14)!important;color:#80f3d4!important}
.sb-foot{border-top:1px solid rgba(95,180,242,.15)!important;padding:14px!important}
.theme-btn,.logout-btn{min-height:42px!important;border-radius:12px!important;font-weight:750!important}
.theme-btn{background:rgba(46,175,232,.08)!important;border-color:rgba(89,178,235,.18)!important;color:#b9eaff!important}
.logout-btn{background:rgba(255,103,132,.09)!important;border-color:rgba(255,103,132,.20)!important;color:#ff9bad!important}
.mob-top{
  height:64px!important;padding:0 16px!important;
  background:rgba(7,16,32,.92)!important;border-bottom:1px solid rgba(91,180,240,.20)!important;
  box-shadow:0 8px 28px rgba(0,0,0,.20)!important;backdrop-filter:blur(18px)!important;-webkit-backdrop-filter:blur(18px)!important;
}
.menu-btn{
  width:42px!important;height:42px!important;border-radius:14px!important;
  background:linear-gradient(135deg,#31c9f3,#536be9 58%,#8268ed)!important;
  color:#fff!important;border:1px solid rgba(173,233,255,.48)!important;
  box-shadow:0 8px 22px rgba(43,159,239,.25),inset 0 1px rgba(255,255,255,.35)!important;
}
.menu-btn:hover{transform:translateY(-1px)!important;filter:brightness(1.08)!important}
.main{min-width:0!important;max-width:none!important;padding:30px clamp(18px,2.4vw,38px) 62px!important}
.pg{min-width:0!important}
.topbar{align-items:center!important;gap:14px!important;padding-bottom:14px!important;border-bottom:1px solid rgba(93,171,224,.12)!important;margin-bottom:20px!important}
.tb-title{font-size:clamp(16px,1.3vw,21px)!important;font-weight:900!important;letter-spacing:-.025em!important}
.tb-title i{color:#52d7ff!important;filter:drop-shadow(0 0 8px rgba(51,204,255,.25))}
.tb-sub{color:#7f9bb9!important;font-size:11px!important}
.tb-right{gap:8px!important}
.badge{border-radius:999px!important;padding:5px 10px!important;font-weight:800!important}
.card,.metric,.sec-panel,.sub-card,.conn-card-v2,.create-panel,.srv-panel,.pw-panel,.traf-chart-card,.traf-mini,.traf-main-stat,.modal,.modal-v2,.table-wrap,.chart-card{
  background:linear-gradient(145deg,rgba(17,37,65,.91),rgba(8,18,36,.96))!important;
  border:1px solid rgba(100,182,239,.20)!important;border-radius:20px!important;
  box-shadow:0 16px 42px rgba(0,0,0,.27),inset 0 1px rgba(255,255,255,.055)!important;
  backdrop-filter:blur(16px)!important;-webkit-backdrop-filter:blur(16px)!important;
}
.card{padding:20px!important}
.card-title{font-size:13px!important;font-weight:850!important;color:#ddecff!important;gap:9px!important}
.card-title>i,.card-title .ti{color:#54d6ff!important}
.metrics,.v-metrics{gap:12px!important;grid-template-columns:repeat(4,minmax(0,1fr))!important}
.metric,.v-metric{
  padding:18px 15px!important;min-width:0!important;min-height:140px!important;
  background:linear-gradient(145deg,rgba(20,44,76,.94),rgba(9,23,44,.98))!important;
  border:1px solid rgba(91,183,244,.22)!important;border-radius:19px!important;
}
.v-metric{gap:9px!important}
.m-ring{background:rgba(47,192,246,.11)!important;border:1px solid rgba(73,203,255,.32)!important;color:#67dcff!important;box-shadow:0 0 22px rgba(39,181,245,.10)!important}
.m-ring.r2{color:#9c91ff!important;background:rgba(156,145,255,.11)!important;border-color:rgba(156,145,255,.30)!important}
.m-ring.r3{color:#43e1b7!important;background:rgba(53,221,178,.10)!important;border-color:rgba(53,221,178,.28)!important}
.m-ring.r4{color:#ffc66d!important;background:rgba(255,198,109,.10)!important;border-color:rgba(255,198,109,.28)!important}
.v-metric .m-label{color:#90abc9!important;font-weight:750!important}
.v-metric .m-val{color:#f4f9ff!important;font-size:clamp(20px,2vw,28px)!important;font-weight:950!important}
.v-metric .m-sub{color:#7894b3!important}
.btn,button,.btn-primary,.action-btn,.icon-btn,.theme-btn,.logout-btn,select{
  font-family:'Vazirmatn',system-ui,sans-serif!important;font-weight:800!important;
  border-radius:12px!important;touch-action:manipulation!important;-webkit-tap-highlight-color:transparent!important;
}
.btn{min-height:40px!important;padding:9px 13px!important;font-size:11.5px!important;gap:7px!important;white-space:normal!important;line-height:1.45!important}
.btn-p,.btn-primary{background:linear-gradient(120deg,#31c9f3,#397de9 58%,#6d69ef)!important;color:#041629!important;border:1px solid rgba(154,229,255,.50)!important;box-shadow:0 8px 22px rgba(35,153,235,.22),inset 0 1px rgba(255,255,255,.42)!important}
.btn-g{background:rgba(44,190,238,.12)!important;color:#a9eaff!important;border:1px solid rgba(81,193,244,.27)!important}
.btn-o{background:rgba(125,146,181,.10)!important;color:#c5d5e8!important;border:1px solid rgba(120,155,196,.24)!important}
.btn-pur{background:rgba(144,121,255,.13)!important;color:#c7bbff!important;border:1px solid rgba(158,137,255,.30)!important}
.btn-d{background:rgba(255,103,132,.11)!important;color:#ff9bad!important;border:1px solid rgba(255,103,132,.27)!important}
.btn-amber{background:rgba(255,196,105,.12)!important;color:#ffdc9e!important;border:1px solid rgba(255,196,105,.28)!important}
.btn:hover:not(:disabled),button:hover:not(:disabled){filter:brightness(1.10)!important;transform:translateY(-1px)!important}
.btn:active,button:active{transform:translateY(0)!important}
.btn-icon{width:40px!important;min-width:40px!important;height:40px!important;min-height:40px!important;padding:0!important;display:inline-grid!important;place-items:center!important}
input,select,textarea,.fi,.fs,.cp-input-full,.subs-search input,.modal-v2-input{
  max-width:100%!important;min-width:0!important;min-height:42px!important;
  background:rgba(3,12,26,.72)!important;color:#eff7ff!important;
  border:1px solid rgba(108,177,225,.24)!important;border-radius:12px!important;
}
input:focus,select:focus,textarea:focus{border-color:#4cd3ff!important;box-shadow:0 0 0 3px rgba(50,201,244,.13)!important;outline:none!important}
.subs-toolbar{gap:10px!important}
.subs-search{min-width:min(100%,240px)!important}
.sub-grid{grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr))!important;gap:16px!important}
.sub-card{border-radius:20px!important;overflow:hidden!important}
.sub-card-top{background:linear-gradient(135deg,rgba(44,174,230,.13),rgba(125,98,245,.08))!important;padding:20px!important}
.sub-card-icon{background:linear-gradient(145deg,#28c4ef,#596bea 62%,#8568ed)!important;border:1px solid rgba(178,233,255,.34)!important;box-shadow:0 8px 22px rgba(48,162,237,.24)!important;border-radius:15px!important}
.sub-card-name-v2{font-size:16px!important;font-weight:900!important;color:#f3f8ff!important}
.sub-card-desc-v2{color:#91abc7!important;line-height:1.7!important}
.sub-card-stats{background:rgba(4,13,27,.46)!important;border-color:rgba(103,183,233,.18)!important;border-radius:14px!important}
.sub-card-stat{padding:13px 8px!important;border-color:rgba(103,183,233,.14)!important}
.sub-card-stat-val{color:#eff8ff!important;font-weight:950!important}
.sub-card-stat-label{color:#7f9bb9!important}
.sub-card-url-row{direction:ltr!important;min-width:0!important;gap:7px!important;margin-inline:16px!important;padding:8px 9px!important;background:rgba(36,173,222,.075)!important;border:1px solid rgba(89,184,231,.18)!important;border-radius:12px!important}
.sub-card-url-text{min-width:0!important;direction:ltr!important;text-align:left!important;font-size:10px!important;overflow:hidden!important;text-overflow:ellipsis!important;white-space:nowrap!important;word-break:normal!important;overflow-wrap:normal!important;color:#7ee3ff!important}
.sub-card-url-copy{flex:0 0 36px!important;width:36px!important;height:36px!important;border:1px solid rgba(105,190,237,.24)!important;background:rgba(60,166,221,.10)!important;color:#9de7ff!important;border-radius:10px!important}
.sub-card-bottom{display:grid!important;grid-template-columns:repeat(4,minmax(0,1fr))!important;gap:8px!important;padding:15px 16px 17px!important}
.sub-card-bottom .btn{min-width:0!important;width:100%!important;flex:initial!important;justify-content:center!important;padding:9px 7px!important;font-size:10px!important}
.cfg-grid{gap:13px!important}
.cfg-card{border-radius:19px!important;background:linear-gradient(145deg,rgba(15,34,59,.94),rgba(8,19,37,.98))!important;border-color:rgba(94,177,239,.20)!important}
.cfg-top{padding:18px 19px 15px!important}
.cfg-label{font-size:14px!important;font-weight:850!important}
.cfg-status{padding:5px 10px!important;border-radius:999px!important;font-weight:800!important}
.cfg-bottom{padding:15px 19px 18px!important}
.cfg-link-toggle{min-height:42px!important;border-style:solid!important;border-color:rgba(96,178,235,.24)!important;background:rgba(30,117,173,.08)!important;color:#b8dbf5!important}
.cfg-vless{font-size:10px!important;line-height:1.8!important;overflow-wrap:anywhere!important;word-break:break-word!important}
.cfg-actions{display:grid!important;grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:8px!important}
.cfg-actions .btn{min-width:0!important;width:100%!important;justify-content:center!important;min-height:42px!important}
.tog{width:42px!important;height:24px!important;border-radius:999px!important;background:rgba(117,143,174,.28)!important}
.tog::after{width:18px!important;height:18px!important;left:3px!important;top:3px!important}
.tog.on{background:#20c99a!important}.tog.on::after{top:3px!important;left:21px!important}
.modal-bg{padding:12px!important}.modal,.modal-v2{max-width:min(100%,820px)!important;border-radius:22px!important;box-shadow:0 28px 90px rgba(0,0,0,.54)!important}
.toast{max-width:calc(100vw - 28px)!important;white-space:normal!important;text-align:center!important;line-height:1.55!important}
.table-wrap,.tbl-wrap,.logs-table-wrap{border-radius:15px!important;border:1px solid rgba(94,177,239,.16)!important}
@media(min-width:1500px){.main{padding-inline:clamp(36px,3vw,64px)!important}.pg{max-width:1700px!important}}
@media(max-width:1100px){.metrics,.v-metrics{grid-template-columns:repeat(2,minmax(0,1fr))!important}.main{padding-inline:20px!important}}
@media(max-width:900px){.main{padding:78px 16px 48px!important}.mob-top{display:flex!important}.sidebar{z-index:230!important}.overlay{z-index:220!important}.metrics,.v-metrics{grid-template-columns:repeat(2,minmax(0,1fr))!important}}
@media(max-width:640px){
  .main{padding:76px 13px 38px!important}
  .topbar{align-items:flex-start!important;padding-bottom:12px!important;margin-bottom:16px!important}
  .tb-title{font-size:16px!important}.tb-right{width:100%;justify-content:flex-start!important}
  .card{padding:16px!important;border-radius:17px!important}
  .metrics,.v-metrics{grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:9px!important}
  .metric,.v-metric{min-height:124px!important;padding:14px 10px!important}
  .v-metric .m-val{font-size:21px!important}
  .sub-grid{grid-template-columns:minmax(0,1fr)!important;gap:12px!important}
  .sub-card-top{padding:16px!important}
  .sub-card-bottom{grid-template-columns:repeat(2,minmax(0,1fr))!important;padding:13px!important}
  .sub-card-bottom .btn{min-height:42px!important;font-size:10.5px!important}
  .sub-card-url-row{margin-inline:12px!important}
  .cfg-row{padding:15px!important}.cfg-actions{grid-template-columns:repeat(2,minmax(0,1fr))!important}
  .cfg-actions .btn{font-size:10.5px!important;min-height:42px!important}
  .form-row,.cp-row{grid-template-columns:minmax(0,1fr)!important}
  .modal-bg{padding:8px!important}.modal,.modal-v2{max-height:calc(100dvh - 16px)!important;border-radius:17px!important}
}
@media(max-width:380px){.main{padding-inline:9px!important}.mob-top{padding-inline:10px!important}.menu-btn{width:39px!important;height:39px!important}.metrics,.v-metrics{gap:7px!important}.v-metric{padding:12px 7px!important}.v-metric .m-val{font-size:18px!important}.m-ring{width:38px!important;height:38px!important;font-size:16px!important}.btn{font-size:10px!important;padding:8px 8px!important}.sub-card-bottom{gap:7px!important}}
@media(hover:none){.nav-it:hover,.btn:hover,.sub-card:hover,.metric:hover{transform:none!important}}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important;scroll-behavior:auto!important}}


/* FineVPN v1.0.0 — final midnight glass UI layer */
:root{--bg:#050b18!important;--bg2:#09162b!important;--bg3:#102541!important;--card:rgba(13,31,56,.88)!important;--card-b:rgba(85,185,245,.24)!important;--card-bh:rgba(67,214,255,.48)!important;--accent:#31c9f4!important;--accent2:#83e7ff!important;--accent-d:rgba(49,201,244,.13)!important;--purple:#a78bfa!important;--purple-bg:rgba(167,139,250,.14)!important;--green:#2dd4a5!important;--green-bg:rgba(45,212,165,.13)!important;--green-t:#7af0ce!important;--red:#fb7185!important;--red-bg:rgba(251,113,133,.13)!important;--red-t:#ffabb9!important;--amber:#f5bd68!important;--amber-bg:rgba(245,189,104,.13)!important;--amber-t:#ffdda5!important;--t1:#f2f8ff!important;--t2:#b8cde3!important;--t3:#7897b8!important;--shadow:0 18px 48px rgba(0,0,0,.32)!important}
html,body{background:#050b18!important;color:#f2f8ff!important;font-family:'Vazirmatn',system-ui,sans-serif!important}
body{background-image:radial-gradient(ellipse 65% 38% at 12% 0%,rgba(36,168,239,.16),transparent 70%),radial-gradient(ellipse 46% 40% at 96% 95%,rgba(124,91,255,.12),transparent 72%),linear-gradient(145deg,#050b18,#07152b 56%,#080d20)!important;background-attachment:fixed!important}
.sidebar{background:linear-gradient(180deg,rgba(8,21,42,.97),rgba(5,13,29,.98))!important;border-color:rgba(77,175,237,.2)!important;box-shadow:12px 0 46px rgba(0,0,0,.24)!important;backdrop-filter:blur(22px)!important;-webkit-backdrop-filter:blur(22px)!important}
.mob-top{background:rgba(7,18,37,.94)!important;border-bottom:1px solid rgba(82,177,235,.22)!important;backdrop-filter:blur(20px)!important;-webkit-backdrop-filter:blur(20px)!important}
.logo-img,.mob-logo{border:1px solid rgba(86,205,255,.5)!important;box-shadow:0 0 0 4px rgba(46,187,241,.07),0 0 24px rgba(43,184,246,.23)!important}
.nav-it{border-radius:13px!important;font-weight:750!important;min-height:43px!important}
.nav-it.on{background:linear-gradient(105deg,rgba(38,176,235,.19),rgba(125,94,245,.12))!important;border:1px solid rgba(77,185,243,.2)!important;border-right:3px solid #42d4ff!important;box-shadow:inset 0 1px rgba(255,255,255,.07),0 8px 20px rgba(0,0,0,.15)!important}
.card,.metric,.v-metric,.sec-panel,.sub-card,.conn-card-v2,.create-panel,.srv-panel,.pw-panel,.traf-chart-card,.traf-mini,.traf-main-stat,.modal,.modal-v2,.qr-box,.table-wrap,.chart-card{background:linear-gradient(145deg,rgba(17,42,72,.91),rgba(7,18,38,.96))!important;border:1px solid rgba(94,184,241,.22)!important;border-radius:19px!important;box-shadow:0 17px 44px rgba(0,0,0,.28),inset 0 1px rgba(255,255,255,.065)!important;backdrop-filter:blur(18px)!important;-webkit-backdrop-filter:blur(18px)!important}
.card-title,.tb-title{color:#eef8ff!important;font-weight:900!important}.card-title i,.tb-title i{color:#5dd9ff!important}
.btn,button,.btn-primary,.action-btn,.icon-btn,.menu-btn,.theme-btn,.logout-btn{font-family:'Vazirmatn',system-ui,sans-serif!important;font-weight:800!important;touch-action:manipulation!important;-webkit-tap-highlight-color:transparent!important}
.btn{min-width:0!important;min-height:40px!important;padding:8px 13px!important;border-radius:12px!important;display:inline-flex!important;align-items:center!important;justify-content:center!important;gap:7px!important;font-size:11px!important;line-height:1.45!important;white-space:normal!important;max-width:100%!important;box-shadow:inset 0 1px rgba(255,255,255,.12),0 6px 17px rgba(0,0,0,.18)!important}
.btn-p,.btn-primary{background:linear-gradient(120deg,#34cef5,#347fe9 58%,#7167ed)!important;color:#05182b!important;border:1px solid rgba(164,235,255,.56)!important;box-shadow:0 9px 23px rgba(36,142,234,.24),inset 0 1px rgba(255,255,255,.52)!important}
.btn-g{background:rgba(38,187,232,.12)!important;color:#b9efff!important;border:1px solid rgba(84,197,241,.29)!important}
.btn-o{background:rgba(130,159,193,.10)!important;color:#d3e4f6!important;border:1px solid rgba(134,173,214,.23)!important}
.btn-pur{background:rgba(145,119,246,.15)!important;color:#d4caff!important;border:1px solid rgba(165,140,255,.31)!important}
.btn-d{background:rgba(245,91,123,.13)!important;color:#ffb1bf!important;border:1px solid rgba(255,118,145,.3)!important}
.btn-amber{background:rgba(245,184,88,.14)!important;color:#ffe0a6!important;border:1px solid rgba(245,190,104,.31)!important}
.btn:hover:not(:disabled),button:hover:not(:disabled){filter:brightness(1.09)!important;box-shadow:0 9px 22px rgba(0,0,0,.24),inset 0 1px rgba(255,255,255,.16)!important}
.btn:active:not(:disabled),button:active:not(:disabled){transform:translateY(1px)!important}
.btn-icon{width:40px!important;min-width:40px!important;height:40px!important;min-height:40px!important;padding:0!important;display:inline-grid!important;place-items:center!important}
.btn-sm{min-height:34px!important;padding:6px 10px!important;font-size:10px!important}
.sub-card-top{background:linear-gradient(135deg,rgba(39,186,238,.14),rgba(124,95,243,.09))!important}
.sub-card-icon{background:linear-gradient(145deg,#28c8ef,#536bea 62%,#8468ed)!important;border:1px solid rgba(175,238,255,.38)!important;box-shadow:0 8px 23px rgba(41,161,234,.25)!important}
.sub-card-stats{background:rgba(3,14,31,.48)!important;border-color:rgba(94,182,238,.18)!important}
.sub-card-url-row{direction:ltr!important;min-width:0!important;background:rgba(13,83,123,.16)!important;border:1px solid rgba(80,184,234,.22)!important;border-radius:13px!important}
.sub-card-url-text{min-width:0!important;max-width:100%!important;overflow:hidden!important;text-overflow:ellipsis!important;white-space:nowrap!important;direction:ltr!important;text-align:left!important;color:#91e9ff!important}
.sub-card-url-copy{width:38px!important;height:38px!important;min-width:38px!important;border-radius:11px!important;background:rgba(42,171,222,.13)!important;border:1px solid rgba(91,192,238,.24)!important;display:grid!important;place-items:center!important}
.sub-card-bottom{display:grid!important;grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:9px!important}
.sub-card-bottom .btn{width:100%!important;min-width:0!important;min-height:42px!important;padding:8px 7px!important}
.cfg-card{background:linear-gradient(145deg,rgba(17,40,69,.92),rgba(7,19,39,.97))!important;border:1px solid rgba(91,180,237,.22)!important;border-radius:18px!important}
.cfg-actions{display:grid!important;grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:8px!important}
.cfg-actions .btn{width:100%!important;min-width:0!important;min-height:42px!important}
input,select,textarea,.fi,.fs,.cp-input-full,.subs-search input,.modal-v2-input{max-width:100%!important;min-width:0!important;border-radius:12px!important;background:rgba(3,13,29,.76)!important;border:1px solid rgba(102,178,226,.25)!important;color:#eff8ff!important}
input::placeholder,textarea::placeholder{color:#7894b2!important}
.fine-password-control{position:relative!important;display:block!important;width:100%!important;min-width:0!important}
.fine-password-control>.fine-password-input{width:100%!important;min-width:0!important;direction:ltr!important;text-align:left!important;padding-left:54px!important;padding-right:42px!important}
.fine-pw-toggle{position:absolute!important;left:7px!important;right:auto!important;top:50%!important;transform:translateY(-50%)!important;width:36px!important;height:36px!important;min-height:36px!important;padding:0!important;display:grid!important;place-items:center!important;border-radius:10px!important;border:1px solid rgba(86,195,240,.28)!important;background:linear-gradient(145deg,rgba(35,167,220,.16),rgba(119,98,232,.15))!important;color:#a9eaff!important;z-index:5!important}
.fine-pw-toggle i{font-size:17px!important;line-height:1!important;pointer-events:none!important}
.fine-password-control>.modal-v2-input{padding-left:50px!important;padding-right:42px!important}
.modal-v2-input-wrap>.fine-pw-toggle{left:7px!important}
.qr-modal{z-index:1200!important;padding:16px!important;background:rgba(1,7,18,.84)!important;backdrop-filter:blur(12px)!important;-webkit-backdrop-filter:blur(12px)!important}
.qr-box{width:min(100%,380px)!important;padding:22px!important;border-radius:24px!important;border-color:rgba(77,204,255,.32)!important;box-shadow:0 28px 90px rgba(0,0,0,.55),0 0 36px rgba(39,177,242,.10)!important}
.qr-img{display:grid!important;place-items:center!important;min-height:210px!important;padding:10px!important;border-radius:16px!important;background:rgba(255,255,255,.035)!important;border:1px solid rgba(98,184,236,.18)!important}
.qr-img img{width:min(100%,300px)!important;aspect-ratio:1/1!important;height:auto!important;object-fit:contain!important;display:block!important;padding:10px!important;background:#fff!important;border-radius:12px!important;image-rendering:pixelated!important}
.qr-img img[hidden]{display:none!important}
.qr-status{width:100%;min-height:170px;display:grid;place-items:center;padding:20px;text-align:center;color:#9bcbe5;font-size:12px;line-height:1.8}
.qr-status.is-loading:before{content:'';width:30px;height:30px;border:3px solid rgba(82,192,241,.2);border-top-color:#51d8ff;border-radius:50%;animation:fineQrSpin .8s linear infinite;margin-bottom:8px}
.qr-status.is-error{color:#ffb1bf;background:rgba(245,91,123,.08);border-radius:12px}
.qr-status[hidden]{display:none!important}
@keyframes fineQrSpin{to{transform:rotate(360deg)}}
.toast{max-width:calc(100vw - 24px)!important;white-space:normal!important;text-align:center!important;line-height:1.6!important}
@media(max-width:900px){.main{padding:76px 16px 44px!important}.sidebar{z-index:230!important}.overlay{z-index:220!important}}
@media(max-width:640px){.main{padding:76px 12px 38px!important}.topbar{align-items:flex-start!important;gap:10px!important}.tb-right{width:100%!important;display:flex!important;flex-wrap:wrap!important;gap:7px!important}.card,.sec-panel,.create-panel,.srv-panel,.pw-panel{padding:15px!important}.sub-card-bottom{grid-template-columns:repeat(2,minmax(0,1fr))!important}.sub-card-bottom .btn{min-height:43px!important;font-size:10px!important}.cfg-actions{grid-template-columns:repeat(2,minmax(0,1fr))!important}.modal-bg{padding:9px!important}.modal,.modal-v2{max-height:calc(100dvh - 18px)!important}.qr-box{padding:17px!important}}
@media(max-width:380px){.main{padding-inline:9px!important}.btn{font-size:9.5px!important;padding:7px 7px!important}.btn-icon{width:38px!important;min-width:38px!important}.sub-card-bottom{gap:7px!important}.sub-card-bottom .btn{font-size:9px!important}}
@media(prefers-reduced-motion:reduce){.btn,button,.nav-it{transition:none!important}.qr-status.is-loading:before{animation:none!important}}


/* FineVPN v1.0 — unified midnight glass design system */
:root{--bg:#050b18!important;--bg2:#08172c!important;--bg3:#102541!important;--card:rgba(12,29,53,.88)!important;--card-b:rgba(112,190,241,.20)!important;--card-bh:rgba(103,211,255,.48)!important;--accent:#63d4fa!important;--accent2:#a2eaff!important;--accent-d:rgba(70,176,235,.13)!important;--t1:#f2f8ff!important;--t2:#b7cce3!important;--t3:#7896b8!important;--shadow:0 18px 48px rgba(0,0,0,.34)!important;--radius:18px!important}
html,body{min-width:320px!important;background:#050b18!important;color:#f2f8ff!important}
body{position:relative;background-image:radial-gradient(ellipse 65% 42% at 8% 0%,rgba(48,158,235,.16),transparent 68%),radial-gradient(ellipse 48% 40% at 98% 96%,rgba(130,91,240,.13),transparent 72%),linear-gradient(145deg,#050b18,#07162b 58%,#090e20)!important;background-attachment:fixed!important}
body:before{content:"";position:fixed;inset:0;pointer-events:none;z-index:-1;opacity:.25;background-image:linear-gradient(rgba(143,197,241,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(143,197,241,.035) 1px,transparent 1px);background-size:42px 42px;mask-image:linear-gradient(to bottom,black,transparent 85%)}
.sidebar{background:linear-gradient(180deg,rgba(7,22,43,.97),rgba(5,13,28,.98))!important;border-left:1px solid rgba(101,187,239,.20)!important;box-shadow:12px 0 46px rgba(0,0,0,.25)!important;backdrop-filter:blur(24px)!important;-webkit-backdrop-filter:blur(24px)!important}
.logo{padding:21px 17px 18px!important;border-bottom-color:rgba(113,190,240,.15)!important}
.logo-img,.mob-logo{display:grid!important;place-items:center!important;background:linear-gradient(145deg,rgba(56,174,235,.19),rgba(134,105,247,.18))!important;border:1px solid rgba(119,215,255,.45)!important;box-shadow:0 0 0 5px rgba(67,166,232,.06),0 9px 27px rgba(33,131,211,.20)!important}
.logo-img{width:48px!important;height:48px!important;border-radius:15px!important}
.mob-logo{width:39px!important;height:39px!important;border-radius:13px!important;overflow:hidden}
.fine-logo-mark{display:block;width:100%;height:100%;filter:drop-shadow(0 4px 9px rgba(67,184,242,.18))}
.logo-name{font-size:15px!important;font-weight:900!important;letter-spacing:.01em}
.logo-sub{font-size:9px!important;letter-spacing:.08em!important;color:#8eb6d7!important}
.nav-wrap{padding:12px 0!important}
.nav-sec{color:#7190b2!important;font-size:9px!important;letter-spacing:.12em!important;padding-top:17px!important}
.nav-it{min-height:43px!important;margin:3px 9px!important;padding:10px 13px!important;border:1px solid transparent!important;border-radius:12px!important;color:#91aeca!important;font-weight:650!important;transition:background .18s,border-color .18s,color .18s,transform .18s!important}
.nav-it:hover{background:rgba(65,162,222,.09)!important;color:#e4f7ff!important;transform:translateX(-2px)}
.nav-it.on{background:linear-gradient(105deg,rgba(57,181,235,.17),rgba(128,101,243,.13))!important;color:#f3fbff!important;border:1px solid rgba(100,190,243,.19)!important;border-right:3px solid #66ddff!important;box-shadow:inset 0 1px rgba(255,255,255,.07),0 8px 22px rgba(0,0,0,.14)!important}
.nav-it.on i{color:#7fe2ff!important}
.nav-badge{background:rgba(65,174,231,.15)!important;color:#a6eaff!important;border:1px solid rgba(98,197,243,.16)!important}
.main{padding-top:28px!important}
.topbar{border:1px solid rgba(104,181,235,.16)!important;border-radius:17px!important;padding:15px 17px!important;background:linear-gradient(130deg,rgba(12,34,61,.75),rgba(8,20,41,.79))!important;box-shadow:0 12px 34px rgba(0,0,0,.16)!important;backdrop-filter:blur(18px)!important;-webkit-backdrop-filter:blur(18px)!important}
.tb-title{color:#eff8ff!important;font-size:18px!important;font-weight:900!important}
.tb-title i,.card-title i{color:#75dcff!important}
.tb-sub{color:#89a8c7!important}
.card,.metric,.v-metric,.sec-panel,.sub-card,.conn-card-v2,.create-panel,.srv-panel,.pw-panel,.traf-chart-card,.traf-mini,.traf-main-stat,.modal,.modal-v2,.qr-box,.table-wrap,.chart-card,.cfg-card,.conn-card{background:linear-gradient(145deg,rgba(15,38,67,.90),rgba(7,18,37,.96))!important;border:1px solid rgba(102,183,237,.19)!important;border-radius:19px!important;box-shadow:0 16px 42px rgba(0,0,0,.24),inset 0 1px rgba(255,255,255,.055)!important;backdrop-filter:blur(16px)!important;-webkit-backdrop-filter:blur(16px)!important}
.card:hover,.sec-panel:hover,.create-panel:hover,.cfg-card:hover{border-color:rgba(108,207,250,.30)!important}
.card-title,.sec-panel-title,.cp-head-title{color:#eef8ff!important;font-weight:900!important}
.metric,.v-metric{transition:transform .2s,border-color .2s,box-shadow .2s!important}
.metric:hover,.v-metric:hover{transform:translateY(-3px)!important;border-color:rgba(111,208,249,.35)!important;box-shadow:0 20px 46px rgba(0,0,0,.28)!important}
.m-ring{background:rgba(62,177,231,.12)!important;border-color:rgba(98,207,249,.32)!important;color:#86e5ff!important;box-shadow:0 0 22px rgba(59,174,232,.12)!important}
.btn,button,.theme-btn,.logout-btn{font-family:'Vazirmatn',system-ui,sans-serif!important;font-weight:800!important;touch-action:manipulation!important;-webkit-tap-highlight-color:transparent!important}
.btn{min-height:40px!important;border-radius:12px!important;box-shadow:inset 0 1px rgba(255,255,255,.10),0 6px 16px rgba(0,0,0,.14)!important;transition:transform .16s,filter .16s,box-shadow .16s!important}
.btn-p,.btn-primary{background:linear-gradient(115deg,#7ce6ff,#55adf4 55%,#9583ff)!important;color:#06172a!important;border:1px solid rgba(190,240,255,.54)!important;box-shadow:0 9px 24px rgba(49,153,224,.22),inset 0 1px rgba(255,255,255,.52)!important}
.btn-g{background:rgba(50,176,223,.12)!important;color:#b9edff!important;border:1px solid rgba(88,194,238,.27)!important}
.btn-o{background:rgba(124,156,191,.10)!important;color:#d8e8f7!important;border:1px solid rgba(132,177,215,.20)!important}
.btn-pur{background:rgba(143,119,245,.14)!important;color:#ddd5ff!important;border:1px solid rgba(165,144,255,.28)!important}
.btn-d{background:rgba(245,91,123,.12)!important;color:#ffb1bf!important;border:1px solid rgba(255,118,145,.27)!important}
.btn:hover:not(:disabled),button:hover:not(:disabled){filter:brightness(1.07)!important;transform:translateY(-1px)!important}
.btn:active:not(:disabled),button:active:not(:disabled){transform:translateY(0)!important}
input,select,textarea,.fi,.fs,.cp-input-full,.subs-search input,.modal-v2-input{background:rgba(3,13,29,.70)!important;border-color:rgba(109,179,226,.23)!important;color:#eff8ff!important;border-radius:12px!important}
input:focus,select:focus,textarea:focus,.fi:focus,.fs:focus,.cp-input-full:focus,.modal-v2-input:focus{border-color:rgba(105,216,255,.75)!important;box-shadow:0 0 0 3px rgba(69,174,231,.13)!important;outline:none!important}
input::placeholder,textarea::placeholder{color:#7795b5!important}
.mob-top{height:auto!important;min-height:62px!important;padding:calc(9px + env(safe-area-inset-top)) 14px 9px!important;background:rgba(5,16,34,.92)!important;border-bottom:1px solid rgba(103,183,237,.19)!important;backdrop-filter:blur(22px)!important;-webkit-backdrop-filter:blur(22px)!important}
.mob-title{font-weight:900!important;color:#eff9ff!important}
.mob-version{font-size:9px!important;line-height:1!important;color:#a8eaff!important;background:rgba(57,174,229,.12)!important;border:1px solid rgba(100,204,249,.20)!important;border-radius:20px!important;padding:4px 7px!important;margin-right:7px!important;letter-spacing:.04em}
.menu-btn{background:linear-gradient(130deg,#69dbff,#4e9cf4 60%,#8e7df5)!important;color:#071a2e!important;border:1px solid rgba(193,240,255,.4)!important;box-shadow:0 7px 19px rgba(48,148,222,.22)!important}
.sb-foot{border-top-color:rgba(101,181,232,.15)!important}
.theme-btn{background:rgba(56,157,215,.10)!important;border-color:rgba(86,176,229,.22)!important;color:#bae9ff!important}
.logout-btn{background:rgba(238,91,119,.10)!important;border-color:rgba(238,111,137,.23)!important}
.brand-contact{border-color:rgba(103,184,238,.19)!important;background:linear-gradient(145deg,rgba(15,38,67,.84),rgba(7,18,38,.88))!important;border-radius:20px!important}
.brand-contact-logo{display:grid!important;place-items:center!important;background:linear-gradient(145deg,rgba(56,174,235,.18),rgba(134,105,247,.16))!important;border:1px solid rgba(119,215,255,.38)!important;overflow:hidden!important}
.fine-tg-link{border-color:rgba(90,189,239,.24)!important;background:rgba(36,131,214,.10)!important;color:#c7ecff!important;border-radius:12px!important}
.badge{border:1px solid rgba(116,189,234,.16)!important}
.modal-bg{background:rgba(1,7,19,.76)!important;backdrop-filter:blur(9px)!important}
.modal-v2-head,.lmodal-head{background:linear-gradient(120deg,rgba(48,163,220,.12),rgba(134,108,246,.10))!important}
.overlay{background:rgba(1,7,19,.66)!important;backdrop-filter:blur(4px)!important}
button:focus-visible,a:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible,.nav-it:focus-visible{outline:2px solid #82e3ff!important;outline-offset:3px!important}
.toast{border-radius:14px!important;box-shadow:0 14px 38px rgba(0,0,0,.34)!important}
.dash-footer{border-top-color:rgba(104,181,235,.15)!important}
.df-text{color:#7f9fbe!important}
@media(max-width:1050px){.main{padding-top:80px!important}.mob-top{display:flex!important}.sidebar{z-index:240!important}.overlay{z-index:230!important}}
@media(max-width:640px){.main{padding:77px 12px calc(32px + env(safe-area-inset-bottom))!important}.topbar{padding:13px!important;gap:9px!important;border-radius:15px!important}.tb-title{font-size:16px!important}.tb-right{width:100%!important;display:flex!important;flex-wrap:wrap!important;gap:7px!important}.card,.sec-panel,.create-panel,.srv-panel,.pw-panel{padding:14px!important;border-radius:16px!important}.btn{min-height:42px!important}.modal-bg{padding:max(8px,env(safe-area-inset-top)) 8px max(8px,env(safe-area-inset-bottom))!important}.modal,.modal-v2{max-height:calc(100dvh - 16px - env(safe-area-inset-top) - env(safe-area-inset-bottom))!important}.mob-top{padding-inline:12px!important}}
@media(max-width:380px){.main{padding-inline:9px!important}.tb-right .btn{flex:1 1 95px}.mob-title{font-size:12px!important}.mob-version{font-size:8px!important}.v-metric{padding:12px 8px!important}}
@media(hover:none){.metric:hover,.v-metric:hover,.nav-it:hover,.btn:hover{transform:none!important}}
@media(prefers-reduced-motion:reduce){*,*:before,*:after{animation:none!important;transition:none!important;scroll-behavior:auto!important}}


/* FineVPN 𝒗₂.₀ — premium blue glass dashboard */
:root{--bg:#030917!important;--bg2:rgba(5,17,39,.93)!important;--bg3:rgba(11,34,67,.82)!important;--card:rgba(9,29,57,.72)!important;--card-b:rgba(93,183,255,.20)!important;--card-bh:rgba(100,213,255,.50)!important;--accent:#48baff!important;--accent2:#9ae9ff!important;--accent-d:rgba(64,168,245,.14)!important;--green:#12d6a0!important;--green-bg:rgba(18,214,160,.12)!important;--green-t:#65f0c4!important;--red:#ff668a!important;--red-bg:rgba(255,102,138,.12)!important;--red-t:#ff9db4!important;--amber:#ffcb72!important;--amber-bg:rgba(255,203,114,.12)!important;--amber-t:#ffdda0!important;--purple:#9ba7ff!important;--purple-bg:rgba(132,145,255,.13)!important;--t1:#f3f9ff!important;--t2:#b5cde7!important;--t3:#7b9cbe!important;--shadow:0 18px 55px rgba(0,0,0,.34)!important;--radius:20px!important;--sidebar-w:264px}
html,body{background:#030917!important;color:#eff8ff!important}
body{position:relative;isolation:isolate;background:radial-gradient(ellipse 55% 38% at 52% -7%,rgba(27,113,226,.25),transparent 70%),radial-gradient(ellipse 38% 38% at 95% 92%,rgba(71,85,216,.16),transparent 72%),linear-gradient(145deg,#030817,#07172f 55%,#050b20)!important}
body:before,body:after{content:"";position:fixed;z-index:-1;pointer-events:none;border-radius:50%;border:1px solid rgba(92,191,255,.105);box-shadow:0 0 0 25px rgba(76,164,237,.02),0 0 0 58px rgba(76,164,237,.014),0 0 0 95px rgba(76,164,237,.01)}
body:before{width:min(68vw,700px);height:min(68vw,700px);right:-22vw;top:-37vw}
body:after{width:min(49vw,510px);height:min(49vw,510px);left:-18vw;bottom:-31vw;border-color:rgba(144,154,255,.12)}
.sidebar{background:linear-gradient(180deg,rgba(5,20,45,.96),rgba(3,11,28,.97))!important;border-left:1px solid rgba(83,177,249,.23)!important;box-shadow:18px 0 60px rgba(0,0,0,.28),inset -1px 0 rgba(255,255,255,.03)!important;backdrop-filter:blur(28px)!important;-webkit-backdrop-filter:blur(28px)!important}
.logo{border-bottom-color:rgba(93,184,255,.17)!important;padding:22px 17px 19px!important}
.logo-img,.mob-logo{border:1px solid rgba(110,216,255,.42)!important;background:rgba(36,126,210,.12)!important;box-shadow:0 0 0 5px rgba(67,163,238,.06),0 0 30px rgba(48,159,246,.2)!important}
.logo-img img,.mob-logo img{object-fit:contain!important}
.logo-name,.mob-title{font-size:15px!important;font-weight:950!important;color:#f4fbff!important;text-shadow:0 0 22px rgba(95,191,255,.18)}
.logo-sub{font-size:10px!important;color:#91b8dc!important;letter-spacing:0!important}
.nav-sec{color:#6f9bc5!important;font-size:10px!important;letter-spacing:0!important;padding:18px 17px 7px!important}
.nav-it{margin:3px 9px!important;padding:11px 13px!important;border:1px solid transparent!important;border-right:2px solid transparent!important;border-radius:13px!important;color:#9db9d8!important;font-size:12.5px!important;transition:all .2s ease!important}
.nav-it i{font-size:18px!important;color:#75cfff!important}
.nav-it:hover{background:rgba(46,143,225,.10)!important;border-color:rgba(83,182,245,.12)!important;color:#e8f8ff!important}
.nav-it.on{background:linear-gradient(105deg,rgba(42,142,242,.26),rgba(70,110,240,.12))!important;border:1px solid rgba(98,202,255,.33)!important;border-right:3px solid #58d7ff!important;color:#fff!important;box-shadow:0 8px 26px rgba(21,114,208,.15),inset 0 1px rgba(255,255,255,.08)!important}
.nav-it.on i{color:#8deaff!important;filter:drop-shadow(0 0 8px rgba(91,211,255,.55))}
.nav-badge{background:rgba(56,162,236,.15)!important;color:#a8e7ff!important}
.sb-foot{border-top-color:rgba(93,184,255,.16)!important}
.logout-btn{border-radius:12px!important}
.mob-top{background:rgba(4,15,35,.9)!important;border-bottom-color:rgba(95,184,246,.19)!important;backdrop-filter:blur(22px)!important}
.menu-btn{background:linear-gradient(130deg,#5cdbff,#347fe9 65%,#7d80ff)!important;color:#04162d!important;box-shadow:0 7px 22px rgba(45,142,230,.3)!important}
.main{position:relative;z-index:1}
.topbar{align-items:center!important;margin-bottom:20px!important;padding:14px 17px!important;border-radius:18px!important;border:1px solid rgba(95,184,246,.15)!important;background:linear-gradient(115deg,rgba(10,31,60,.60),rgba(6,18,40,.44))!important;box-shadow:0 10px 32px rgba(0,0,0,.14)!important;backdrop-filter:blur(14px)!important}
.tb-title{color:#f4faff!important;font-weight:900!important}.tb-title i{color:#75dbff!important;text-shadow:0 0 16px rgba(74,188,255,.35)}.tb-sub{color:#8eb1d2!important}
.card,.metric,.traf-main-stat,.traf-mini,.vless-box,.sec-panel,.create-panel,.srv-panel,.pw-panel,.section-card,.chart-card,.sub-card,.sub-exp-card,.sub-info,.modal,.modal-v2,.cfg-card,.lmodal-head,.lmodal-list,.ip-stat-card{background:linear-gradient(145deg,rgba(13,39,72,.82),rgba(5,17,39,.88))!important;border:1px solid rgba(92,181,244,.22)!important;border-radius:20px!important;box-shadow:0 16px 46px rgba(0,0,0,.25),inset 0 1px rgba(255,255,255,.055)!important;backdrop-filter:blur(20px)!important;-webkit-backdrop-filter:blur(20px)!important}
.metric,.v-metric{position:relative;overflow:hidden!important;transition:transform .22s,border-color .22s,box-shadow .22s!important}
.metric:before,.card:before,.sec-panel:before,.create-panel:before,.vless-box:before{content:"";position:absolute;top:0;left:12%;right:12%;height:1px;background:linear-gradient(90deg,transparent,rgba(104,220,255,.55),rgba(132,154,255,.38),transparent);pointer-events:none}
.metric:hover,.card:hover,.sec-panel:hover{border-color:rgba(103,206,255,.37)!important;box-shadow:0 20px 56px rgba(0,0,0,.28),0 0 28px rgba(38,148,228,.08)!important}
.m-ring{background:linear-gradient(145deg,rgba(52,178,248,.22),rgba(80,105,237,.13))!important;border:1px solid rgba(117,212,255,.25)!important;color:#91e8ff!important;box-shadow:0 0 25px rgba(53,161,237,.16)!important}
.m-ring.r2{color:#7de8ff!important}.m-ring.r3{color:#65e5c4!important}.m-ring.r4{color:#aaaaff!important}
.m-val{color:#f5fbff!important;text-shadow:0 0 20px rgba(95,182,255,.12)}
.vless-box{position:relative;overflow:hidden;background:linear-gradient(120deg,rgba(10,39,78,.82),rgba(6,18,44,.91))!important;border-color:rgba(82,182,255,.32)!important}
.vl-header,.vl-title{color:#dbf6ff!important}.vl-code{background:rgba(1,10,25,.55)!important;border:1px solid rgba(100,187,246,.19)!important;border-radius:13px!important}
.btn,.btn-p,.btn-g,.btn-o,.btn-pur,.cp-submit-btn{border-radius:12px!important;transition:transform .18s,filter .18s,box-shadow .18s!important}
.btn-p,.cp-submit-btn{background:linear-gradient(115deg,#6edfff,#398bef 62%,#8581ff)!important;border:1px solid rgba(186,239,255,.5)!important;color:#03162d!important;box-shadow:0 9px 26px rgba(37,135,221,.24),inset 0 1px rgba(255,255,255,.58)!important;font-weight:900!important}
.btn-pur{background:linear-gradient(115deg,#5d9eff,#6a71f4)!important;color:#fff!important;border:1px solid rgba(153,195,255,.35)!important}
.btn-g{background:rgba(35,177,147,.14)!important;border:1px solid rgba(67,226,188,.25)!important;color:#84f2d0!important}
.btn-o{background:rgba(48,142,221,.11)!important;border:1px solid rgba(106,186,241,.23)!important;color:#c6edff!important}
.btn:hover,.cp-submit-btn:hover{transform:translateY(-2px);filter:brightness(1.07)}
.fi,.fs,.cp-input-full,.modal-v2-input,textarea{background:rgba(2,13,31,.58)!important;border:1px solid rgba(113,182,233,.22)!important;color:#f2f9ff!important;border-radius:13px!important}
.fi:focus,.fs:focus,.cp-input-full:focus,.modal-v2-input:focus,textarea:focus{border-color:rgba(106,216,255,.72)!important;box-shadow:0 0 0 4px rgba(62,165,238,.12)!important}
select option{background:#0c1e39;color:#f2f9ff}
.cp-head-icon,.sec-panel-ico,.sec-hero-ico,.cp-block-label i{color:#7ee4ff!important}
.proto-card{background:rgba(5,20,43,.68)!important;border-color:rgba(98,181,241,.18)!important;border-radius:15px!important}.proto-card.active{background:linear-gradient(145deg,rgba(47,151,229,.22),rgba(75,102,229,.16))!important;border-color:rgba(102,212,255,.48)!important;box-shadow:0 0 25px rgba(47,151,229,.11)!important}
.table-wrap,.table-responsive{border-radius:15px!important;overflow:auto!important}.table-wrap table,.table-responsive table{background:rgba(4,15,34,.35)!important}
th{color:#9ac9ec!important}td{border-bottom-color:rgba(101,170,224,.12)!important}
.badge.bg-blue,.nav-badge{background:rgba(52,153,228,.15)!important;color:#b5eaff!important}.badge.bg-purple{background:rgba(129,132,255,.14)!important;color:#c4c7ff!important}
.sb-close{background:rgba(53,160,235,.16)!important;color:#c7f2ff!important}
.ip-scan-layout{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(230px,.75fr);gap:16px;margin-bottom:16px}.ip-scan-textarea{width:100%;min-height:205px;resize:vertical;padding:14px!important;direction:ltr;text-align:left;line-height:1.9;font-family:ui-monospace,monospace;font-size:13px}.ip-scan-meta{display:flex;justify-content:space-between;gap:8px;flex-wrap:wrap;font-size:10px;color:var(--t3);margin-top:8px}.ip-scan-actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px}.ip-scan-note{display:flex;gap:8px;align-items:flex-start;margin-top:14px;padding:11px 12px;border:1px solid rgba(255,203,114,.20);background:rgba(255,203,114,.07);border-radius:12px;color:#e8cc9a;font-size:10.5px;line-height:1.9}.ip-scan-note i{color:#ffcf7b;margin-top:3px}.ip-scan-stats{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}.ip-stat-card{display:flex;align-items:center;gap:12px;padding:15px!important}.ip-stat-icon{display:grid;place-items:center;width:40px;height:40px;border-radius:13px;background:rgba(23,214,160,.13);color:#69f0c6;font-size:19px}.ip-stat-icon.bad{background:rgba(255,103,139,.13);color:#ff91ac}.ip-stat-icon.wait{background:rgba(255,203,114,.12);color:#ffdb91}.ip-stat-icon.total{background:rgba(74,174,248,.13);color:#8ce4ff}.ip-stat-label{font-size:10px;color:var(--t3)}.ip-stat-value{font-size:24px;font-weight:950;color:#f4faff}.ip-results-panel{margin-top:16px}.ip-result-copy{display:flex;gap:6px;flex-wrap:wrap;margin-right:auto}.ip-results-filters{display:flex;gap:7px;flex-wrap:wrap;margin-bottom:12px}.ip-filter{border:1px solid rgba(96,174,233,.2);background:rgba(44,126,201,.10);color:#b9dff7;border-radius:999px;padding:8px 13px;font:inherit;font-size:10.5px;font-weight:800;cursor:pointer}.ip-filter.active{background:linear-gradient(110deg,rgba(47,151,229,.28),rgba(105,137,255,.2));border-color:rgba(106,210,255,.48);color:#effaff;box-shadow:0 0 18px rgba(47,151,229,.12)}.ip-results-list{display:flex;flex-direction:column;gap:7px}.ip-result-row{display:grid;grid-template-columns:minmax(0,1fr) 110px 100px 40px;align-items:center;gap:10px;padding:10px 12px;border:1px solid rgba(96,174,233,.13);border-radius:12px;background:rgba(3,15,34,.42)}.ip-result-address{direction:ltr;text-align:left;font-family:ui-monospace,monospace;font-size:12px;color:#dcf5ff;overflow-wrap:anywhere}.ip-result-status{font-size:11px;font-weight:800}.ip-result-status.good{color:#68efc2}.ip-result-status.bad{color:#ff91a9}.ip-result-status.unknown{color:#ffda90}.ip-result-latency{direction:ltr;text-align:center;font-size:11px;color:#a8c9e6}.ip-result-copy-one{border:1px solid rgba(101,188,248,.2);background:rgba(45,139,220,.12);color:#c4edff;border-radius:9px;min-height:33px;cursor:pointer}
@media(max-width:900px){.ip-scan-layout{grid-template-columns:1fr}.ip-scan-stats{grid-template-columns:repeat(4,minmax(0,1fr))}}
@media(max-width:640px){.main{padding:77px 12px calc(35px + env(safe-area-inset-bottom))!important}.sidebar{width:min(var(--sidebar-w),86vw)!important}.topbar{padding:12px!important}.ip-scan-stats{grid-template-columns:repeat(2,minmax(0,1fr))}.ip-result-row{grid-template-columns:minmax(0,1fr) 82px 72px 34px;gap:6px;padding:9px 8px}.ip-result-copy{width:100%;margin:8px 0 0}.ip-result-copy .btn{flex:1 1 90px}.ip-result-address{font-size:11px}}
@media(max-width:360px){.ip-result-row{grid-template-columns:minmax(0,1fr) 72px 56px 32px}.ip-result-status,.ip-result-latency{font-size:9px}}
@media(prefers-reduced-motion:reduce){*,*:before,*:after{animation:none!important;transition:none!important}}
.fine-logo-mark{object-fit:contain!important;display:block!important;width:100%!important;height:100%!important}


/* FineVPN 𝒗₂.₀ — complete neon-blue glass dashboard */
:root{--bg:#030a18!important;--bg2:rgba(4,17,39,.96)!important;--bg3:#102b4e!important;--card:rgba(9,29,57,.76)!important;--card-b:rgba(100,190,255,.22)!important;--card-bh:rgba(111,220,255,.55)!important;--accent:#52caff!important;--accent2:#9cecff!important;--accent-d:rgba(67,171,243,.15)!important;--green:#12d7a2!important;--green-bg:rgba(18,215,162,.13)!important;--green-t:#72f3cf!important;--red:#ff698d!important;--red-bg:rgba(255,105,141,.13)!important;--red-t:#ff9ab1!important;--amber:#ffd077!important;--amber-bg:rgba(255,208,119,.13)!important;--amber-t:#ffdda0!important;--purple:#9c9cff!important;--purple-bg:rgba(156,156,255,.14)!important;--t1:#f3f9ff!important;--t2:#b7d1eb!important;--t3:#7f9fbe!important;--shadow:0 18px 55px rgba(0,0,0,.34)!important;--radius:20px!important;--sidebar-w:258px}
html,body{background:#030a18!important;color:#f2f8ff!important}body{position:relative;isolation:isolate;background:radial-gradient(ellipse 60% 42% at 52% -5%,rgba(26,107,218,.25),transparent 70%),radial-gradient(ellipse 43% 36% at 95% 92%,rgba(62,75,205,.15),transparent 72%),linear-gradient(145deg,#020714,#071a35 56%,#030a1b)!important}
body:before,body:after{content:"";position:fixed;z-index:-2;pointer-events:none;border-radius:50%;border:1px solid rgba(105,203,255,.11);box-shadow:0 0 0 24px rgba(75,165,236,.023),0 0 0 58px rgba(75,165,236,.016),0 0 0 96px rgba(75,165,236,.01)}body:before{width:min(66vw,720px);height:min(66vw,720px);top:-34vw;right:-18vw}body:after{width:min(48vw,520px);height:min(48vw,520px);bottom:-30vw;left:-16vw;border-color:rgba(136,152,255,.13)}
.sidebar{background:linear-gradient(180deg,rgba(5,20,46,.96),rgba(3,11,28,.98))!important;border-left:1px solid rgba(93,184,249,.23)!important;box-shadow:16px 0 58px rgba(0,0,0,.29),inset -1px 0 rgba(255,255,255,.035)!important;backdrop-filter:blur(26px)!important;-webkit-backdrop-filter:blur(26px)!important}
.logo{display:flex!important;flex-direction:column!important;justify-content:center!important;align-items:center!important;gap:10px!important;padding:22px 16px 20px!important;border-bottom:1px solid rgba(98,190,255,.16)!important;text-align:center}.logo-img{width:82px!important;height:82px!important;border-radius:24px!important;border:1px solid rgba(110,216,255,.46)!important;background:rgba(35,125,211,.12)!important;box-shadow:0 0 0 7px rgba(61,162,237,.06),0 0 34px rgba(46,160,247,.22)!important;padding:5px}.logo-img img{object-fit:contain!important;filter:drop-shadow(0 0 10px rgba(85,193,255,.35))}.logo-name{font-size:18px!important;font-weight:950!important;color:#f3faff!important}.logo-sub{font-size:10px!important;color:#91bce0!important}
.nav-sec{padding:17px 16px 6px!important;color:#6f9dc8!important;font-size:10px!important;letter-spacing:0!important;text-transform:none!important}.nav-it{margin:3px 9px!important;padding:11px 13px!important;min-height:44px;border:1px solid transparent!important;border-right:2px solid transparent!important;border-radius:13px!important;color:#a2bddb!important;font-size:12.5px!important;transition:background .18s,border-color .18s,transform .18s,color .18s!important}.nav-it i{font-size:18px!important;color:#79d4ff!important}.nav-it:hover{background:rgba(48,148,229,.11)!important;border-color:rgba(83,182,245,.14)!important;color:#f0faff!important}.nav-it.on{background:linear-gradient(105deg,rgba(44,148,248,.27),rgba(75,107,240,.13))!important;border:1px solid rgba(103,207,255,.34)!important;border-right:3px solid #5cddff!important;color:#fff!important;box-shadow:0 8px 25px rgba(25,126,218,.16),inset 0 1px rgba(255,255,255,.09)!important}.nav-it.on i{color:#a0edff!important;filter:drop-shadow(0 0 8px rgba(91,211,255,.58))}.nav-badge{background:rgba(56,162,236,.16)!important;color:#b4edff!important}.sb-foot{border-top:1px solid rgba(93,184,255,.16)!important;padding:13px!important}.logout-btn{background:rgba(255,98,134,.1)!important;border:1px solid rgba(255,112,145,.22)!important;color:#ffabc0!important;border-radius:13px!important;min-height:42px}
.mob-top{background:rgba(4,15,35,.91)!important;border-bottom:1px solid rgba(94,184,248,.2)!important;backdrop-filter:blur(22px)!important}.mob-logo{width:34px!important;height:34px!important;border:1px solid rgba(113,213,255,.42)!important;background:rgba(39,136,219,.15)!important;box-shadow:0 0 16px rgba(44,158,245,.2)!important}.menu-btn{background:linear-gradient(130deg,#68dcff,#398be9 65%,#8785ff)!important;color:#03172c!important;box-shadow:0 7px 22px rgba(45,142,230,.3)!important}.main{position:relative;z-index:1;padding:22px 25px 42px!important;max-width:none!important}.pg{position:relative;max-width:1660px;margin-inline:auto}.pg.on{animation:dash-enter .35s ease both}@keyframes dash-enter{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
.dashboard-scene{position:absolute;z-index:-1;top:-26px;left:2%;right:2%;height:315px;overflow:hidden;pointer-events:none;opacity:.92}.scene-planet{position:absolute;width:clamp(190px,24vw,320px);height:clamp(190px,24vw,320px);top:-45px;left:48%;border-radius:50%;background:radial-gradient(circle at 34% 27%,rgba(211,249,255,.98) 0 1%,rgba(104,203,255,.91) 4%,rgba(34,116,219,.82) 23%,rgba(9,46,111,.94) 54%,rgba(4,14,43,.95) 70%);border:1px solid rgba(126,220,255,.65);box-shadow:0 0 22px rgba(82,186,255,.42),0 0 70px rgba(26,114,231,.28),inset -22px -18px 42px rgba(0,0,0,.7),inset 9px 8px 28px rgba(197,247,255,.32)}.scene-planet:before{content:"";position:absolute;inset:10%;border-radius:50%;background:repeating-radial-gradient(ellipse at 44% 40%,transparent 0 17px,rgba(130,217,255,.08) 18px 20px,transparent 21px 31px);opacity:.8;transform:rotate(-20deg)}.scene-planet:after{content:"";position:absolute;inset:-12%;border:1px solid rgba(110,206,255,.35);border-radius:50%;transform:rotate(-18deg) scaleY(.28);box-shadow:0 0 14px rgba(87,188,255,.25)}.scene-stars{position:absolute;inset:0;background-image:radial-gradient(1px 1px at 12% 22%,#c7efff 60%,transparent 70%),radial-gradient(1px 1px at 26% 12%,#8adfff 60%,transparent 70%),radial-gradient(2px 2px at 70% 26%,#e2f8ff 60%,transparent 70%),radial-gradient(1px 1px at 83% 11%,#9beaff 60%,transparent 70%),radial-gradient(1px 1px at 57% 62%,#8bdcff 60%,transparent 70%);background-size:170px 130px,230px 170px,190px 180px,240px 160px,150px 130px;opacity:.78}.scene-mountain{position:absolute;left:-3%;right:-3%;bottom:0;height:190px;background:linear-gradient(180deg,rgba(35,129,229,.4),rgba(4,23,58,.86));filter:drop-shadow(0 -4px 16px rgba(56,160,255,.18));clip-path:polygon(0 70%,8% 55%,15% 67%,22% 25%,28% 55%,35% 34%,42% 62%,49% 13%,56% 57%,64% 35%,71% 66%,79% 26%,87% 62%,94% 43%,100% 58%,100% 100%,0 100%)}.scene-mountain-back{opacity:.34;transform:scaleY(.75);transform-origin:bottom}.scene-mountain-front{height:135px;opacity:.38;background:linear-gradient(180deg,rgba(18,94,188,.4),rgba(1,12,34,.9));clip-path:polygon(0 65%,10% 44%,19% 73%,28% 35%,38% 69%,47% 28%,55% 74%,63% 45%,72% 72%,81% 31%,90% 69%,100% 43%,100% 100%,0 100%)}.scene-logo-watermark{position:absolute;left:8%;top:24px;width:220px;height:220px;border-radius:50%;border:1px solid rgba(112,201,255,.1);box-shadow:0 0 0 22px rgba(95,177,240,.025),0 0 0 48px rgba(95,177,240,.015);display:grid;place-items:center}.scene-logo-watermark img{width:72%;height:72%;object-fit:contain;opacity:.045;filter:grayscale(1)}
.glass-surface{position:relative;overflow:hidden;border:1px solid rgba(97,185,246,.23)!important;border-radius:20px!important;background:linear-gradient(145deg,rgba(13,39,75,.82),rgba(4,17,40,.88))!important;box-shadow:0 16px 44px rgba(0,0,0,.25),inset 0 1px rgba(255,255,255,.07),inset 0 -1px rgba(66,150,228,.06)!important;backdrop-filter:blur(21px)!important;-webkit-backdrop-filter:blur(21px)!important}.glass-surface:before{content:"";position:absolute;top:0;left:12%;right:12%;height:1px;background:linear-gradient(90deg,transparent,rgba(121,224,255,.54),rgba(141,159,255,.35),transparent);pointer-events:none}
.dash-head{display:grid;grid-template-columns:minmax(175px,.65fr) minmax(260px,1fr) auto;align-items:center;gap:16px;padding:16px 18px!important;margin:3px 0 18px;min-height:112px}.dash-server-pill{display:flex;align-items:center;gap:9px;width:max-content;max-width:100%;padding:10px 12px;border:1px solid rgba(99,190,248,.2);border-radius:15px;background:rgba(18,72,121,.2);color:#d4f2ff}.dash-pill-icon{width:35px;height:35px;border-radius:11px;background:linear-gradient(145deg,rgba(65,175,244,.3),rgba(70,120,232,.13));display:grid;place-items:center;color:#91e7ff;font-size:18px}.dash-server-pill b,.dash-server-pill small{display:block}.dash-server-pill b{font-size:10px;color:#8fb9dc}.dash-server-pill small{font-size:11px;color:#6ef0c8;font-weight:800;margin-top:3px}.dash-server-pill>i:last-child{font-size:20px;color:#64d5ff;margin-right:6px}.dash-welcome{position:relative;z-index:1}.dash-eyebrow,.dash-section-kicker{font-size:10px;color:#76c8f5;font-weight:850;letter-spacing:.02em}.dash-welcome h1{font-size:clamp(18px,2vw,24px);font-weight:950;color:#f5fbff;margin:4px 0;text-shadow:0 0 24px rgba(83,188,255,.16)}.dash-welcome p{font-size:11px;color:#a9c8e5}.dash-head-actions{display:flex;align-items:center;justify-content:flex-end;gap:9px;flex-wrap:wrap}.dash-time-card,.dash-admin-chip{display:flex;align-items:center;gap:8px;padding:9px 11px;border:1px solid rgba(103,190,245,.17);background:rgba(8,30,59,.45);border-radius:13px;color:#ccecff;font-size:10px}.dash-time-card>i{font-size:17px;color:#84dfff}.dash-time-card b{font-family:ui-monospace,monospace;font-size:11px;color:#fff}.dash-theme-toggle{display:flex;align-items:center;gap:7px;border:1px solid rgba(103,190,245,.28);background:rgba(52,135,215,.14);color:#d6f4ff;border-radius:999px;padding:9px 13px;cursor:pointer;font:inherit;font-size:10px;font-weight:850;white-space:nowrap}.dash-theme-toggle i{font-size:17px;color:#ffe6a5}.dash-admin-chip b,.dash-admin-chip small{display:block}.dash-admin-chip b{font-size:11px}.dash-admin-chip small{font-size:9px;color:#7de9c8;margin-top:2px}.dash-admin-avatar{width:33px;height:33px;border-radius:50%;display:grid;place-items:center;color:#a5eaff;background:linear-gradient(145deg,rgba(56,165,237,.31),rgba(80,96,214,.18));border:1px solid rgba(112,204,255,.25)}.dash-admin-chip>i{color:#7aebc9}
.dash-metrics{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:13px;margin-bottom:18px}.dash-metric{min-width:0;min-height:138px;position:relative;overflow:hidden;display:flex;align-items:flex-start;gap:13px;padding:20px 18px;border:1px solid rgba(92,186,250,.24);border-radius:19px;background:linear-gradient(145deg,rgba(12,42,77,.88),rgba(4,19,42,.94));box-shadow:0 14px 36px rgba(0,0,0,.23),inset 0 1px rgba(255,255,255,.07);transition:transform .2s,border-color .2s}.dash-metric:hover{transform:translateY(-3px);border-color:rgba(112,218,255,.5)}.dash-metric-icon{width:50px;height:50px;flex:0 0 50px;border-radius:16px;display:grid;place-items:center;font-size:24px;color:#a4ecff;background:linear-gradient(145deg,rgba(53,162,242,.25),rgba(77,108,231,.14));border:1px solid rgba(117,215,255,.25);box-shadow:0 0 23px rgba(38,147,233,.14)}.metric-cyan .dash-metric-icon{color:#7deeff}.metric-teal .dash-metric-icon{color:#62f0d1}.metric-violet .dash-metric-icon{color:#c3b7ff}.dash-metric-copy{min-width:0;display:flex;flex-direction:column;gap:4px}.dash-metric-copy>span{font-size:10px;color:#a5c8e5;font-weight:750}.dash-metric-copy>strong{font-size:clamp(22px,2.2vw,29px);line-height:1.2;color:#f6fbff;font-weight:950;direction:ltr;text-align:right;white-space:nowrap;text-shadow:0 0 22px rgba(86,187,255,.15)}.dash-metric-copy>strong small{font-size:11px;color:#9bc5e4}.dash-metric-copy>small{font-size:9px;color:#81a8cc}.dash-metric-wave{position:absolute;left:0;right:0;bottom:-1px;height:30px;opacity:.42;background:linear-gradient(180deg,transparent,rgba(53,155,239,.1));border-top:1.5px solid rgba(76,192,255,.55);clip-path:polygon(0 67%,9% 48%,18% 78%,28% 28%,39% 72%,50% 42%,59% 69%,69% 23%,80% 68%,91% 37%,100% 58%,100% 100%,0 100%)}.metric-cyan .dash-metric-wave{border-color:rgba(42,208,255,.65)}.metric-teal .dash-metric-wave{border-color:rgba(42,230,184,.65)}.metric-violet .dash-metric-wave{border-color:rgba(167,132,255,.65)}
.dash-feature-grid{display:grid;grid-template-columns:minmax(0,1.08fr) minmax(0,.92fr);gap:17px;margin-bottom:18px}.dash-feature-card{padding:19px!important;min-width:0}.dash-feature-heading,.dash-lower-heading{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:16px}.dash-feature-heading h2,.dash-lower-heading h2{font-size:17px;color:#f2f9ff;font-weight:950;margin:4px 0;display:flex;align-items:center;gap:9px}.dash-feature-heading h2 i,.dash-lower-heading h2 i{font-size:20px;color:#83e3ff;filter:drop-shadow(0 0 9px rgba(69,183,247,.28))}.dash-feature-heading p{font-size:10px;color:#91b5d7}.dash-view-all{display:inline-flex;align-items:center;gap:6px;white-space:nowrap;border:1px solid rgba(109,193,247,.22);background:rgba(43,139,219,.1);color:#c8edff;border-radius:999px;padding:7px 12px;font:inherit;font-size:10px;font-weight:850;cursor:pointer}.dash-view-all:hover{background:rgba(55,159,236,.2)}.dash-sub-content{display:grid;grid-template-columns:minmax(170px,.8fr) minmax(0,1.2fr);gap:15px;align-items:center}.dash-sub-illustration{min-height:210px;position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;overflow:hidden;border-radius:17px;background:radial-gradient(ellipse at 50% 65%,rgba(24,126,234,.31),transparent 63%),linear-gradient(155deg,rgba(13,52,98,.3),rgba(3,16,39,.14));border:1px solid rgba(88,181,247,.14)}.dash-orbit{position:absolute;width:190px;height:65px;border:2px solid rgba(72,192,255,.72);border-radius:50%;transform:rotate(-8deg);box-shadow:0 0 14px rgba(38,163,243,.45),inset 0 0 14px rgba(38,163,243,.2)}.orbit-two{width:150px;height:48px;transform:rotate(9deg);border-color:rgba(133,147,255,.6)}.dash-sub-platform{position:absolute;bottom:48px;width:190px;height:28px;border-radius:50%;border:2px solid rgba(76,202,255,.8);box-shadow:0 0 18px rgba(43,151,245,.48),inset 0 0 12px rgba(91,182,255,.24)}.dash-user-bubble{position:absolute;z-index:1;display:grid;place-items:center;border-radius:50%;width:57px;height:57px;color:#bbf2ff;font-size:30px;background:radial-gradient(circle at 35% 25%,rgba(176,240,255,.55),rgba(28,127,232,.76) 60%,rgba(7,34,92,.95));border:1px solid rgba(149,225,255,.68);box-shadow:0 0 22px rgba(40,162,255,.54),inset 0 2px 8px rgba(255,255,255,.25)}.bubble-main{top:49px;width:67px;height:67px;font-size:35px}.bubble-left{top:77px;left:calc(50% - 75px);width:43px;height:43px;font-size:23px}.bubble-right{top:77px;right:calc(50% - 75px);width:43px;height:43px;font-size:23px}.dash-sub-caption{position:absolute;bottom:7px;display:flex;flex-direction:column;align-items:center;gap:1px}.dash-sub-caption b{font-size:22px;color:#f4fbff}.dash-sub-caption span{font-size:9px;color:#a3c9e8}.dash-sub-controls,.dash-portal-actions{display:flex;flex-direction:column;gap:8px;min-width:0}.dash-action-row{width:100%;display:flex;align-items:center;gap:10px;padding:10px 11px;border:1px solid rgba(109,192,248,.25);border-radius:14px;background:linear-gradient(110deg,rgba(10,38,73,.78),rgba(7,24,50,.7));color:#e8f7ff;text-align:right;font:inherit;cursor:pointer;transition:border-color .18s,background .18s,transform .18s}.dash-action-row:hover{border-color:rgba(112,216,255,.58);background:rgba(34,112,191,.24);transform:translateX(-2px)}.dash-action-icon{width:36px;height:36px;flex:0 0 36px;border-radius:11px;display:grid;place-items:center;background:linear-gradient(145deg,rgba(63,172,244,.24),rgba(73,107,226,.15));border:1px solid rgba(115,205,255,.2);color:#9ceaff;font-size:18px}.dash-action-row>span:nth-child(2){min-width:0;flex:1}.dash-action-row b,.dash-action-row small{display:block}.dash-action-row b{font-size:11px;font-weight:850}.dash-action-row small{font-size:9px;color:#89acca;margin-top:3px}.dash-action-row>i:last-child{color:#7edbff;font-size:17px}.dash-quick-create{border-top:1px solid rgba(99,184,244,.16);margin-top:15px;padding-top:13px}.dash-quick-title{display:flex;align-items:center;gap:9px;margin-bottom:10px;color:#b9eeff}.dash-quick-title>i{font-size:20px;color:#9f9bff}.dash-quick-title b,.dash-quick-title small{display:block}.dash-quick-title b{font-size:11px}.dash-quick-title small{font-size:9px;color:#8eafd0;margin-top:2px}.dash-quick-fields{display:grid;grid-template-columns:1.15fr .62fr .62fr .7fr 1.05fr .5fr auto;gap:7px}.dash-quick-fields .fi{min-width:0;width:100%;height:40px;padding:8px 10px!important;font-size:10px!important;border-radius:11px!important}.dash-quick-fields .btn{min-height:40px!important;white-space:nowrap;font-size:10px!important}.dash-quick-summary{margin-top:8px;color:#88acd0;font-size:9px}.dash-quick-result{margin-top:9px;padding:10px;border:1px solid rgba(36,213,166,.25);background:rgba(15,170,132,.1);border-radius:12px}.dash-quick-result>b{display:block;color:#68edc5;font-size:10px;margin-bottom:7px}.dash-quick-result>div{display:flex;gap:7px}.dash-quick-result input{flex:1;min-width:0;font-size:10px!important;direction:ltr}.dash-quick-result .btn{font-size:10px!important;white-space:nowrap}
.dash-online-badge,.dash-live-dot{display:inline-flex;align-items:center;gap:6px;border-radius:999px;padding:7px 10px;background:rgba(9,185,143,.13);border:1px solid rgba(52,228,185,.2);color:#68edc7;font-size:9px;font-weight:900;white-space:nowrap}.dash-online-badge i,.dash-live-dot i{font-size:8px}.dash-portal-visual{height:177px;position:relative;display:grid;place-items:center;margin:1px 0 12px;overflow:hidden;border-radius:17px;background:radial-gradient(ellipse at 50% 58%,rgba(26,130,232,.26),transparent 62%),linear-gradient(150deg,rgba(8,35,72,.34),rgba(3,15,35,.16));border:1px solid rgba(95,185,249,.13)}.dash-portal-core{position:relative;z-index:2;width:100px;height:100px;border-radius:50%;display:grid;place-items:center;color:#d0f6ff;font-size:48px;background:radial-gradient(circle at 33% 25%,rgba(173,240,255,.52),rgba(42,128,231,.82) 58%,rgba(8,30,79,.98));border:2px solid rgba(134,222,255,.8);box-shadow:0 0 0 7px rgba(48,153,237,.1),0 0 44px rgba(42,156,255,.48),inset 0 2px 12px rgba(255,255,255,.27)}.dash-portal-halo{position:absolute;width:185px;height:68px;border-radius:50%;border:2px solid rgba(70,202,255,.7);transform:translateY(43px) rotate(-7deg);box-shadow:0 0 20px rgba(53,167,249,.35)}.dash-portal-ring{position:absolute;width:210px;height:210px;border:1px solid rgba(96,181,248,.25);border-radius:50%;box-shadow:inset 0 0 35px rgba(52,142,238,.08)}.ring-b{width:255px;height:255px;border-color:rgba(118,147,255,.16)}.dash-portal-label{position:absolute;bottom:9px;display:flex;gap:6px;align-items:center;color:#9ec9eb;font-size:9px}.dash-portal-label b{color:#f2f9ff;font-size:15px}.dash-portal-footer{display:flex;justify-content:space-between;gap:9px;align-items:center;margin-top:12px;padding-top:10px;border-top:1px solid rgba(96,181,244,.14);font-size:9px;color:#8fbbd9}.dash-portal-footer>span:first-child{display:flex;align-items:center;gap:6px}.dash-portal-footer>span:first-child i{color:#62e9c5}.dash-portal-footer .badge{max-width:65%;overflow:hidden;text-overflow:ellipsis}
.dash-lower-grid{display:grid;grid-template-columns:minmax(0,1.45fr) minmax(260px,.75fr);gap:17px;margin-bottom:18px}.dash-table-card,.dash-status-card,.dash-chart-card{padding:18px!important;min-width:0}.dash-lower-heading{margin-bottom:13px}.dash-lower-heading h2{font-size:15px}.dash-table-wrap{width:100%;overflow:auto;border-radius:13px;border:1px solid rgba(101,179,235,.14)}.dash-recent-table{width:100%;min-width:590px;border-collapse:separate;border-spacing:0;font-size:10px}.dash-recent-table th{padding:11px 10px;background:rgba(31,91,145,.22);color:#a9c8e4;text-align:right;font-weight:850;white-space:nowrap}.dash-recent-table td{padding:10px;border-top:1px solid rgba(103,169,219,.11);color:#d9eafa;white-space:nowrap}.dash-recent-table tbody tr:hover{background:rgba(59,142,211,.08)}.dash-recent-table td:first-child{color:#84dfff}.dash-table-empty{text-align:center!important;color:#8eabc8!important;padding:24px!important}.dash-row-name{font-weight:850;color:#f1f9ff}.dash-row-sub{font-size:8px;color:#7f9fbd;margin-top:2px}.dash-proto{display:inline-flex;padding:4px 8px;border-radius:999px;background:rgba(50,150,224,.13);border:1px solid rgba(92,185,242,.2);color:#bcecff;font-size:9px;font-weight:850}.dash-state-pill{display:inline-flex;align-items:center;gap:5px;border-radius:999px;padding:4px 8px;font-size:9px;font-weight:850}.dash-state-pill:before{content:"";width:6px;height:6px;border-radius:50%;background:currentColor}.dash-state-pill.is-on{background:rgba(12,192,144,.12);color:#62edc4}.dash-state-pill.is-off{background:rgba(255,106,140,.12);color:#ff9bb3}.dash-table-action{width:29px;height:29px;border-radius:9px;border:1px solid rgba(108,193,246,.2);background:rgba(39,129,211,.12);color:#aeeaff;cursor:pointer;margin-left:4px}.dash-table-action:hover{background:rgba(52,153,231,.24)}
.dash-health-ring{width:142px;height:142px;border-radius:50%;margin:8px auto 13px;display:grid;place-items:center;background:conic-gradient(#11d9a5 0 78%,rgba(59,119,171,.2) 78% 100%);position:relative;box-shadow:0 0 25px rgba(13,208,159,.15)}.dash-health-ring:before{content:"";position:absolute;inset:8px;border-radius:50%;background:#081d38;border:1px solid rgba(91,198,240,.22)}.dash-health-core{position:relative;z-index:1;display:flex;flex-direction:column;align-items:center;gap:3px}.dash-health-core i{font-size:27px;color:#73f0ce}.dash-health-logo{width:35px;height:35px;object-fit:contain;border-radius:50%;border:1px solid rgba(125,219,255,.44);background:rgba(50,150,223,.13);padding:3px;box-shadow:0 0 0 4px rgba(70,163,235,.055),0 0 22px rgba(64,169,242,.3);filter:drop-shadow(0 0 6px rgba(94,209,255,.42))}.dash-health-core b{font-size:16px;color:#f3fbff}.dash-health-core small{font-size:9px;color:#8db2d3}.dash-status-lines{display:flex;flex-direction:column;gap:8px}.dash-status-lines>div{display:flex;justify-content:space-between;align-items:center;gap:8px;padding:9px 10px;border:1px solid rgba(96,175,232,.13);border-radius:11px;background:rgba(5,22,46,.44);font-size:9px}.dash-status-lines span{color:#9cbada;display:flex;align-items:center;gap:7px}.dash-status-lines span i{font-size:14px;color:#79d9ff}.dash-status-lines b{color:#e5f5ff;font-size:9px}.dash-progress{height:6px;border-radius:99px;overflow:hidden;background:rgba(81,147,198,.14);margin-top:10px}.dash-progress span{display:block;height:100%;width:0;border-radius:99px;background:linear-gradient(90deg,#25e2bb,#4dbdff,#8787ff);box-shadow:0 0 14px rgba(53,191,241,.42)}.dash-status-footer{display:flex;align-items:center;gap:7px;margin-top:11px;padding-top:10px;border-top:1px solid rgba(99,176,233,.13);font-size:9px;color:#8caccb}.dash-status-footer b{color:#a7eaff}.dash-status-footer span:last-child{margin-right:auto}
.dash-analytics-grid{display:grid;grid-template-columns:1.25fr .75fr;gap:17px;margin-bottom:15px}.dash-chart-card{min-height:260px}.dash-chart-unit{color:#7fa8cc;font-size:9px}.dash-chart-body{height:190px;position:relative;min-width:0}.dash-chart-donut{max-width:310px;margin-inline:auto}.dash-footer-note{display:flex;align-items:center;gap:9px;padding:10px 3px;color:#7f9fbe;font-size:9px}.dash-footer-note img{width:25px;height:25px;object-fit:contain;opacity:.8}.dash-footer-note b{color:#c8eaff}.dash-footer-note a{margin-right:auto;display:flex;align-items:center;gap:5px;color:#a9eaff}.dash-hidden-compat{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%);white-space:nowrap}
.btn,.btn-p,.btn-g,.btn-o,.btn-pur,.cp-submit-btn,.dash-theme-toggle,.dash-view-all{font-family:'Vazirmatn',system-ui,sans-serif!important}.fi,.fs,textarea{font-family:'Vazirmatn',system-ui,sans-serif!important}.nav-it,.dash-action-row,.dash-view-all{touch-action:manipulation;-webkit-tap-highlight-color:transparent}
/* Light mode is a complete palette, not a fake toggle. */
[data-theme="light"]{color-scheme:light;--bg:#edf5fd!important;--bg2:#f7fbff!important;--bg3:#e3effb!important;--card:rgba(255,255,255,.9)!important;--card-b:rgba(37,126,204,.17)!important;--card-bh:rgba(29,147,226,.4)!important;--t1:#10243c!important;--t2:#365674!important;--t3:#6d87a2!important;--shadow:0 14px 36px rgba(18,64,107,.1)!important}
[data-theme="light"] html,[data-theme="light"] body,html[data-theme="light"],html[data-theme="light"] body{background:#edf5fd!important;color:#10243c!important}
html[data-theme="light"] body{background:radial-gradient(ellipse at 52% -5%,rgba(61,159,238,.17),transparent 66%),radial-gradient(ellipse at 95% 92%,rgba(120,123,236,.09),transparent 70%),linear-gradient(145deg,#eef6ff,#e9f3ff 58%,#f5faff)!important}
html[data-theme="light"] body:before,html[data-theme="light"] body:after{border-color:rgba(44,132,202,.12);box-shadow:0 0 0 24px rgba(51,141,205,.025),0 0 0 58px rgba(51,141,205,.018)}
html[data-theme="light"] .sidebar{background:linear-gradient(180deg,rgba(250,253,255,.97),rgba(235,245,255,.98))!important;border-left-color:rgba(50,126,194,.19)!important;box-shadow:10px 0 36px rgba(35,88,132,.11)!important}
html[data-theme="light"] .logo-name,html[data-theme="light"] .dash-welcome h1,html[data-theme="light"] .dash-feature-heading h2,html[data-theme="light"] .dash-lower-heading h2{color:#102b49!important;text-shadow:none}
html[data-theme="light"] .logo-sub,html[data-theme="light"] .nav-it,html[data-theme="light"] .dash-feature-heading p,html[data-theme="light"] .dash-section-kicker{color:#527492!important}
html[data-theme="light"] .nav-it.on{background:linear-gradient(105deg,rgba(45,148,235,.15),rgba(85,126,235,.08))!important;color:#163d66!important;border-color:rgba(46,148,224,.25)!important}
html[data-theme="light"] .glass-surface,html[data-theme="light"] .dash-metric{background:linear-gradient(145deg,rgba(255,255,255,.94),rgba(237,247,255,.94))!important;border-color:rgba(43,131,201,.2)!important;box-shadow:0 14px 36px rgba(22,75,120,.1),inset 0 1px rgba(255,255,255,.8)!important}
html[data-theme="light"] .dash-metric-copy>span,html[data-theme="light"] .dash-metric-copy>small,html[data-theme="light"] .dash-quick-summary,html[data-theme="light"] .dash-table-action{color:#527492!important}
html[data-theme="light"] .dash-metric-copy>strong,html[data-theme="light"] .dash-table-card .dash-recent-table td,html[data-theme="light"] .dash-row-name{color:#163452!important;text-shadow:none}
html[data-theme="light"] .dash-action-row,html[data-theme="light"] .dash-time-card,html[data-theme="light"] .dash-admin-chip,html[data-theme="light"] .dash-status-lines>div{background:rgba(225,240,253,.78)!important;border-color:rgba(45,127,193,.18)!important;color:#173e61!important}
html[data-theme="light"] .dash-action-row b,html[data-theme="light"] .dash-status-lines b{color:#173c60!important}html[data-theme="light"] .dash-action-row small,html[data-theme="light"] .dash-status-lines span,html[data-theme="light"] .dash-table-empty{color:#64829e!important}
html[data-theme="light"] .dash-sub-illustration,html[data-theme="light"] .dash-portal-visual{background:radial-gradient(ellipse at 50% 58%,rgba(53,157,237,.19),transparent 64%),linear-gradient(155deg,rgba(224,241,255,.86),rgba(239,247,255,.6))!important}
html[data-theme="light"] .dash-quick-fields .fi,html[data-theme="light"] .dash-quick-result .fi,html[data-theme="light"] .fi,html[data-theme="light"] .fs,html[data-theme="light"] textarea{background:rgba(255,255,255,.92)!important;color:#183a5b!important;border-color:rgba(57,135,195,.22)!important}
html[data-theme="light"] .dash-recent-table th{background:#e2effb!important;color:#426785!important}html[data-theme="light"] .dash-recent-table td{border-color:rgba(44,119,183,.12)!important}html[data-theme="light"] .dash-table-wrap{border-color:rgba(50,124,186,.17)!important}
html[data-theme="light"] .dash-health-ring:before{background:#f4faff!important;border-color:rgba(58,141,202,.22)!important}html[data-theme="light"] .dash-health-core b{color:#183e62!important}html[data-theme="light"] .dash-health-core small{color:#6787a4!important}
html[data-theme="light"] .dash-theme-toggle{background:rgba(42,131,207,.1)!important;color:#1f5d90!important;border-color:rgba(55,136,200,.24)!important}html[data-theme="light"] .dash-theme-toggle i{color:#d38a13!important}html[data-theme="light"] .dash-portal-footer,html[data-theme="light"] .dash-footer-note{color:#6484a1!important}
@media(max-width:1240px){.dash-head{grid-template-columns:1fr 1.2fr;}.dash-head-actions{grid-column:1/-1;justify-content:space-between}.dash-feature-grid{grid-template-columns:1fr 1fr}.dash-quick-fields{grid-template-columns:repeat(2,minmax(0,1fr))}.dash-quick-fields .btn{grid-column:1/-1}}
@media(max-width:980px){.main{margin-right:0!important;padding:74px 17px 38px!important}.dash-head{grid-template-columns:1fr 1fr}.dash-welcome{grid-column:1/-1;grid-row:1}.dash-server-pill{grid-row:2}.dash-head-actions{grid-column:1/-1;grid-row:3}.dash-feature-grid{grid-template-columns:1fr}.dash-lower-grid{grid-template-columns:1fr}.dash-analytics-grid{grid-template-columns:1fr 1fr}.dashboard-scene{top:10px}}
@media(max-width:640px){.main{padding:70px 10px 30px!important}.dash-head{display:flex;flex-direction:column;align-items:stretch;gap:12px;padding:14px!important;margin-bottom:12px}.dash-welcome{order:0}.dash-server-pill{order:1;width:100%}.dash-head-actions{order:2;justify-content:space-between;width:100%}.dash-time-card{flex:1;justify-content:center}.dash-theme-toggle{padding:9px 10px}.dash-admin-chip{display:none}.dash-metrics{grid-template-columns:repeat(2,minmax(0,1fr));gap:8px;margin-bottom:12px}.dash-metric{min-height:118px;padding:14px 11px;gap:8px;border-radius:16px}.dash-metric-icon{width:40px;height:40px;flex-basis:40px;font-size:19px;border-radius:13px}.dash-metric-copy>span{font-size:9px}.dash-metric-copy>strong{font-size:22px}.dash-metric-copy>small{font-size:8px}.dash-feature-grid,.dash-lower-grid,.dash-analytics-grid{grid-template-columns:1fr;gap:12px;margin-bottom:12px}.dash-feature-card,.dash-table-card,.dash-status-card,.dash-chart-card{padding:14px!important;border-radius:17px!important}.dash-feature-heading h2,.dash-lower-heading h2{font-size:14px}.dash-feature-heading p{font-size:9px}.dash-sub-content{grid-template-columns:1fr;gap:11px}.dash-sub-illustration{min-height:160px}.dash-sub-controls{display:grid;grid-template-columns:1fr 1fr}.dash-action-row{padding:9px 8px;gap:7px}.dash-action-row b{font-size:9px}.dash-action-row small{font-size:8px}.dash-action-icon{width:30px;height:30px;flex-basis:30px;font-size:15px}.dash-quick-fields{grid-template-columns:1fr 1fr}.dash-quick-fields input:first-child{grid-column:1/-1}.dash-quick-fields .btn{grid-column:1/-1}.dash-portal-visual{height:148px}.dash-portal-actions{display:grid;grid-template-columns:1fr 1fr}.dash-online-badge{font-size:8px;padding:6px 8px}.dash-view-all{font-size:9px;padding:6px 9px}.dash-table-wrap{margin-inline:-1px}.dash-chart-body{height:180px}.dash-footer-note{flex-wrap:wrap}.dash-footer-note a{margin-right:0}.dashboard-scene{height:245px;left:-8%;right:-8%;opacity:.55}.scene-planet{left:40%;top:-20px}.scene-logo-watermark{left:0;width:140px;height:140px}}
@media(max-width:380px){.dash-sub-controls,.dash-portal-actions{grid-template-columns:1fr}.dash-head-actions{gap:5px}.dash-time-card{padding:8px 7px;font-size:9px}.dash-theme-toggle{font-size:9px}.dash-metric{padding:12px 9px}.dash-metric-icon{width:34px;height:34px;flex-basis:34px;font-size:17px}.dash-metric-copy>strong{font-size:19px}}
@media(prefers-reduced-motion:reduce){.pg.on,.dash-metric,.dash-action-row{animation:none!important;transition:none!important}}


/* Light-mode compatibility for every management section */
html[data-theme="light"] .topbar,html[data-theme="light"] .card,html[data-theme="light"] .metric,html[data-theme="light"] .sec-panel,html[data-theme="light"] .create-panel,html[data-theme="light"] .srv-panel,html[data-theme="light"] .pw-panel,html[data-theme="light"] .sub-card,html[data-theme="light"] .sub-exp-card,html[data-theme="light"] .cfg-card,html[data-theme="light"] .traf-main-stat,html[data-theme="light"] .traf-mini,html[data-theme="light"] .traf-chart-card,html[data-theme="light"] .conn-card-v2,html[data-theme="light"] .vless-box,html[data-theme="light"] .modal-v2,html[data-theme="light"] .modal,html[data-theme="light"] .ip-stat-card{background:linear-gradient(145deg,rgba(255,255,255,.97),rgba(235,246,255,.95))!important;border-color:rgba(46,128,194,.18)!important;box-shadow:0 12px 32px rgba(26,77,120,.09)!important;color:#163452!important}
html[data-theme="light"] .tb-title,html[data-theme="light"] .card-title,html[data-theme="light"] .sec-panel-title,html[data-theme="light"] .sub-card-name-v2,html[data-theme="light"] .cfg-label,html[data-theme="light"] .m-val,html[data-theme="light"] .traf-main-val{color:#183a5a!important;text-shadow:none!important}
html[data-theme="light"] .tb-sub,html[data-theme="light"] .nav-sec,html[data-theme="light"] .m-label,html[data-theme="light"] .m-sub,html[data-theme="light"] .sec-panel-sub,html[data-theme="light"] .cfg-sub-meta{color:#607f9b!important}
html[data-theme="light"] .nav-it{color:#476a89!important}html[data-theme="light"] .nav-it i{color:#2487ca!important}
html[data-theme="light"] .fi,html[data-theme="light"] .fs,html[data-theme="light"] .cp-input-full,html[data-theme="light"] .modal-v2-input,html[data-theme="light"] textarea{background:rgba(255,255,255,.94)!important;color:#173957!important;border-color:rgba(51,130,194,.22)!important}
html[data-theme="light"] .table-wrap,html[data-theme="light"] .tbl-wrap,html[data-theme="light"] .logs-table-wrap{background:rgba(255,255,255,.8)!important}html[data-theme="light"] td{color:#244968!important}html[data-theme="light"] th{color:#4b6c89!important}
html[data-theme="light"] .dash-hidden-compat{color:#183a5a!important}


/* FineVPN v2.0 refinement: sub-panel, 3D controls and progressive IP scan */
.logo-img{border-radius:50%!important;overflow:hidden!important}
.subpage-theme-toggle{min-height:42px;padding:8px 13px!important}
body:after{background-image:url("https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png");background-position:center;background-size:66% 66%;background-repeat:no-repeat;opacity:.045;filter:grayscale(1) drop-shadow(0 0 22px rgba(75,183,255,.25))}
#pg-subgroups{position:relative;isolation:isolate}
#pg-subgroups:before{content:"";position:absolute;z-index:-1;pointer-events:none;width:min(65vw,620px);height:min(65vw,620px);right:-15%;top:7%;border-radius:50%;border:1px solid rgba(92,193,255,.055);box-shadow:0 0 0 28px rgba(70,160,239,.018),0 0 0 72px rgba(70,160,239,.012),inset 0 0 80px rgba(50,146,235,.025)}
#pg-subgroups:after{content:"";position:absolute;z-index:-1;pointer-events:none;width:min(34vw,330px);height:min(34vw,330px);left:1%;top:16%;border-radius:50%;background:url("https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png") center/contain no-repeat;opacity:.035;filter:grayscale(1) drop-shadow(0 0 24px rgba(73,178,255,.3)}
#pg-subgroups .topbar{gap:12px;background:linear-gradient(120deg,rgba(8,30,61,.78),rgba(10,30,58,.42))!important;border-color:rgba(93,190,251,.22)!important;box-shadow:0 15px 38px rgba(0,0,0,.2),inset 0 1px rgba(255,255,255,.06)!important}
#pg-subgroups .tb-right{display:flex;align-items:center;justify-content:flex-end;gap:9px;flex-wrap:wrap}
#pg-subgroups .subs-toolbar{padding:13px;border-radius:18px;border:1px solid rgba(92,182,244,.16);background:rgba(8,26,52,.48);box-shadow:inset 0 1px rgba(255,255,255,.04);margin-bottom:15px}
#pg-subgroups .subs-search{max-width:520px;border-radius:13px!important;background:rgba(2,14,33,.64)!important;border:1px solid rgba(97,188,245,.22)!important}
#pg-subgroups .topbar .btn-pur{min-height:43px!important;padding:9px 16px!important;border-radius:14px!important;background:linear-gradient(125deg,#168ddc,#526ff0 58%,#8865ec)!important;border:1px solid rgba(173,225,255,.42)!important;box-shadow:0 9px 24px rgba(37,127,222,.26),inset 0 1px rgba(255,255,255,.32)!important}
.dash-status-card{position:relative;overflow:hidden!important;background:linear-gradient(145deg,rgba(10,42,77,.86),rgba(5,17,39,.93))!important;border:1px solid rgba(96,184,245,.24)!important;box-shadow:0 18px 46px rgba(0,0,0,.25),inset 0 1px rgba(255,255,255,.07)!important}.dash-status-card:after{content:"";position:absolute;left:-74px;top:-115px;width:210px;height:210px;border-radius:50%;border:1px solid rgba(91,193,255,.12);box-shadow:0 0 0 20px rgba(70,165,237,.025),0 0 0 45px rgba(70,165,237,.014);pointer-events:none}.dash-health-ring{filter:drop-shadow(0 0 15px rgba(38,191,222,.22));border:1px solid rgba(132,225,255,.25)}.dash-status-lines>div{background:linear-gradient(100deg,rgba(5,24,47,.8),rgba(35,30,80,.34))!important;border-color:rgba(95,180,240,.19)!important;box-shadow:inset 0 1px rgba(255,255,255,.045)!important}
#pg-subgroups .badge{border:1px solid rgba(151,166,255,.28)!important;background:rgba(103,92,212,.16)!important;color:#d5d7ff!important;box-shadow:inset 0 1px rgba(255,255,255,.1)!important}
.sub-grid{display:grid!important;grid-template-columns:repeat(auto-fill,minmax(min(100%,340px),1fr))!important;gap:17px!important;align-items:stretch!important}
.sub-card{position:relative!important;isolation:isolate!important;overflow:hidden!important;border-radius:23px!important;border:1px solid rgba(99,192,250,.28)!important;background:linear-gradient(145deg,rgba(14,52,90,.78),rgba(5,17,39,.91))!important;box-shadow:0 20px 48px rgba(0,0,0,.29),0 0 28px rgba(42,153,232,.075),inset 0 1px rgba(255,255,255,.11),inset 0 -1px rgba(93,186,245,.08)!important;backdrop-filter:blur(22px)!important;-webkit-backdrop-filter:blur(22px)!important;transition:transform .22s,border-color .22s,box-shadow .22s!important}
.sub-card:before{content:"";position:absolute;z-index:-1;inset:0 9% auto;height:1px;background:linear-gradient(90deg,transparent,rgba(148,231,255,.8),rgba(137,155,255,.55),transparent)}
.sub-card:after{content:"";position:absolute;z-index:-1;width:180px;height:180px;left:-70px;top:-100px;border:1px solid rgba(96,199,255,.13);border-radius:50%;box-shadow:0 0 0 18px rgba(66,167,239,.025),0 0 0 42px rgba(66,167,239,.014)}
.sub-card:hover{transform:translateY(-4px)!important;border-color:rgba(111,219,255,.48)!important;box-shadow:0 26px 58px rgba(0,0,0,.34),0 0 35px rgba(39,157,242,.15),inset 0 1px rgba(255,255,255,.14)!important}
.sub-card-top{position:relative;overflow:hidden!important}.sub-card-top:after{content:"";position:absolute;right:-65px;bottom:-115px;width:210px;height:210px;border-radius:50%;border:1px solid rgba(111,203,255,.12);box-shadow:0 0 0 18px rgba(71,160,236,.025),0 0 0 40px rgba(71,160,236,.014);pointer-events:none}
.sub-card-url-copy{transition:transform .16s,filter .16s,box-shadow .16s!important}.sub-card-url-copy:hover{transform:translateY(-2px)!important;filter:brightness(1.2)!important;box-shadow:0 8px 18px rgba(24,132,219,.24),inset 0 1px rgba(255,255,255,.2)!important}
.sub-card-top{padding:19px!important;background:linear-gradient(135deg,rgba(44,157,230,.18),rgba(115,100,238,.10))!important}
.sub-card-head-v2{gap:12px!important;align-items:center!important}
.sub-card-icon{width:48px!important;height:48px!important;border-radius:16px!important;background:linear-gradient(145deg,#64e3ff,#298ce9 55%,#7775ed)!important;border:1px solid rgba(194,242,255,.63)!important;box-shadow:0 10px 25px rgba(30,150,237,.33),inset 0 1px rgba(255,255,255,.62)!important;color:#06284b!important;font-size:22px!important}
.sub-card-name-v2{font-size:16px!important;font-weight:950!important;color:#f4fbff!important;text-shadow:0 0 18px rgba(88,194,255,.18)}
.sub-card-desc-v2{font-size:10px!important;color:#9abbd9!important;line-height:1.8!important}
.sub-card-lock-badge{width:34px;height:34px;display:grid;place-items:center;border-radius:12px;border:1px solid rgba(117,197,247,.23);background:rgba(47,145,218,.14);color:#a8eaff}
.sub-card-stats{margin-top:15px!important;padding:10px 7px!important;display:grid!important;grid-template-columns:repeat(3,minmax(0,1fr))!important;border-radius:15px!important;background:rgba(1,12,29,.5)!important;border:1px solid rgba(100,183,239,.16)!important;box-shadow:inset 0 1px rgba(255,255,255,.04)!important}
.sub-card-stat{min-width:0!important;padding:7px 4px!important}.sub-card-stat-val{font-size:19px!important;color:#f1f9ff!important;font-weight:950!important}.sub-card-stat-label{font-size:9px!important;color:#8baecc!important}
.sub-card-url-row{display:flex!important;align-items:center!important;gap:7px!important;margin:12px 15px 0!important;padding:8px!important;border-radius:13px!important;background:linear-gradient(105deg,rgba(30,122,192,.17),rgba(36,69,140,.13))!important;border:1px solid rgba(94,188,243,.21)!important;box-shadow:inset 0 1px rgba(255,255,255,.055)!important}
.sub-card-url-text{flex:1!important;min-width:0!important;color:#94e8ff!important;font-size:10px!important;direction:ltr!important;text-align:left!important;overflow:hidden!important;text-overflow:ellipsis!important;white-space:nowrap!important}
.sub-card-url-copy{width:36px!important;height:36px!important;flex:0 0 36px!important;display:grid!important;place-items:center!important;border-radius:11px!important;background:linear-gradient(145deg,rgba(79,177,237,.22),rgba(70,91,190,.17))!important;border:1px solid rgba(126,209,255,.3)!important;color:#c9f1ff!important;box-shadow:0 5px 13px rgba(0,0,0,.18),inset 0 1px rgba(255,255,255,.14)!important}
.sub-card-bottom{display:grid!important;grid-template-columns:1.4fr 1fr!important;gap:9px!important;padding:15px!important}
.sub-card-bottom .btn{width:100%!important;min-width:0!important;min-height:44px!important;border-radius:13px!important;font-size:10px!important;font-weight:900!important;box-shadow:0 8px 20px rgba(0,0,0,.2),inset 0 1px rgba(255,255,255,.13)!important}
.ns-destination-grid{display:grid!important;grid-template-columns:minmax(0,1.45fr) minmax(110px,.55fr)!important;gap:10px!important;align-items:end!important}
.ns-destination-grid>div{min-width:0}.ns-destination-grid label{display:block;margin-bottom:6px;color:var(--t2);font-size:10.5px;font-weight:800}
.modal-v2{border:1px solid rgba(101,196,255,.35)!important;background:linear-gradient(145deg,rgba(11,38,73,.97),rgba(4,14,34,.98))!important;box-shadow:0 28px 90px rgba(0,0,0,.55),0 0 42px rgba(38,144,224,.13),inset 0 1px rgba(255,255,255,.11)!important;backdrop-filter:blur(28px)!important}
.modal-v2-head{background:linear-gradient(135deg,rgba(46,156,230,.18),rgba(113,99,231,.12))!important;border-bottom-color:rgba(102,194,246,.15)!important}
.modal-v2-icon{border-radius:16px!important;background:linear-gradient(145deg,#6ce3ff,#398fe9 58%,#8078ef)!important;color:#062649!important;border:1px solid rgba(191,240,255,.65)!important;box-shadow:0 10px 26px rgba(43,145,226,.28),inset 0 1px rgba(255,255,255,.58)!important}
#modal-create-sub .modal-v2-head{position:relative;overflow:hidden}#modal-create-sub .modal-v2-head:after{content:"";position:absolute;left:-35px;top:-85px;width:180px;height:180px;border-radius:50%;border:1px solid rgba(135,212,255,.14);box-shadow:0 0 0 20px rgba(70,161,236,.035),0 0 0 44px rgba(70,161,236,.02);pointer-events:none}
#modal-create-sub .modal-v2-footer .btn-pur{background:linear-gradient(120deg,#167fd1,#536feb 58%,#9459e8)!important;border:1px solid rgba(169,220,255,.42)!important;box-shadow:0 9px 25px rgba(46,117,223,.3),inset 0 1px rgba(255,255,255,.34)!important}
.modal-v2-footer{display:grid!important;grid-template-columns:.7fr 1.5fr!important;gap:9px!important}.modal-v2-footer .btn{min-height:46px!important;border-radius:14px!important}
.ip-progress-wrap{margin-top:14px;padding:12px 13px;border:1px solid rgba(95,190,250,.21);border-radius:14px;background:linear-gradient(120deg,rgba(23,91,151,.19),rgba(60,67,158,.13));box-shadow:inset 0 1px rgba(255,255,255,.055)}
.ip-progress-head{display:flex;justify-content:space-between;align-items:center;gap:8px;margin-bottom:9px;color:#bfeaff;font-size:10px}.ip-progress-head span{font-family:ui-monospace,monospace;color:#88ebff;font-weight:900}
.ip-progress-track{height:9px;border-radius:999px;overflow:hidden;background:rgba(1,12,28,.72);border:1px solid rgba(100,182,234,.14);box-shadow:inset 0 2px 4px rgba(0,0,0,.28)}.ip-progress-track i{display:block;width:0;height:100%;border-radius:inherit;background:linear-gradient(90deg,#32d5e8,#488cf4 58%,#9a76fa);box-shadow:0 0 15px rgba(67,177,255,.55);transition:width .2s ease}
.ip-progress-wrap.is-running .ip-progress-track i{background:linear-gradient(90deg,#38d7ee,#559dff 55%,#b17bff);filter:saturate(1.15)}
.ip-stat-card{position:relative;overflow:hidden!important;border-radius:17px!important;background:linear-gradient(145deg,rgba(11,43,78,.88),rgba(4,17,39,.94))!important;border:1px solid rgba(103,190,247,.23)!important;box-shadow:0 15px 35px rgba(0,0,0,.22),inset 0 1px rgba(255,255,255,.08)!important}.ip-stat-card:after{content:"";position:absolute;inset:auto -25px -45px auto;width:110px;height:110px;border:1px solid rgba(105,194,251,.14);border-radius:50%;box-shadow:0 0 0 15px rgba(83,161,230,.02);pointer-events:none}
.ip-result-row{background:linear-gradient(115deg,rgba(9,33,63,.74),rgba(5,17,40,.78))!important;border-color:rgba(98,178,238,.18)!important;box-shadow:inset 0 1px rgba(255,255,255,.035)!important}.ip-result-copy-one{box-shadow:0 5px 13px rgba(23,114,198,.16),inset 0 1px rgba(255,255,255,.12)!important}
.ip-result-address{display:flex!important;flex-direction:column;gap:3px}.ip-result-scope{align-self:flex-start;font-size:8px;padding:2px 7px;border-radius:999px;border:1px solid rgba(101,190,245,.16);color:#98dfff;background:rgba(42,145,216,.11)}.ip-result-scope.private{color:#d2bdff;border-color:rgba(171,131,248,.22);background:rgba(133,93,223,.13)}
html[data-theme="light"] .sub-card{background:linear-gradient(145deg,rgba(255,255,255,.97),rgba(232,246,255,.96))!important;border-color:rgba(52,137,203,.23)!important;box-shadow:0 16px 36px rgba(25,83,127,.11),inset 0 1px white!important}html[data-theme="light"] .sub-card-name-v2,html[data-theme="light"] .sub-card-stat-val{color:#173b5c!important}html[data-theme="light"] .sub-card-desc-v2,html[data-theme="light"] .sub-card-stat-label{color:#6685a0!important}html[data-theme="light"] .sub-card-stats{background:rgba(224,241,253,.8)!important}html[data-theme="light"] .sub-card-url-row{background:rgba(51,151,214,.08)!important}html[data-theme="light"] .sub-card-url-text{color:#176590!important}html[data-theme="light"] .subpage-theme-toggle{color:#1b5a8d!important}
@media(max-width:640px){#pg-subgroups .tb-right{width:100%;justify-content:stretch}#pg-subgroups .tb-right>*{flex:1 1 auto}.sub-grid{grid-template-columns:minmax(0,1fr)!important;gap:13px!important}.sub-card-top{padding:16px!important}.sub-card-bottom{grid-template-columns:1fr 1fr!important;padding:12px!important}.ns-destination-grid{grid-template-columns:minmax(0,1fr)!important}.modal-v2-footer{grid-template-columns:1fr 1.5fr!important}.ip-progress-wrap{padding:10px}}
@media(max-width:380px){.sub-card-bottom{grid-template-columns:1fr!important}.sub-card-bottom .btn{min-height:42px!important}.sub-card-url-row{margin-inline:10px!important}.sub-card-stats{margin-top:12px!important}}
</style>
</head>
<body>
<div class="toast" id="toast"></div>
<div class="qr-modal" id="qr-modal" onclick="closeQrModal()">
  <div class="qr-box" onclick="event.stopPropagation()">
    <div class="qr-title" id="qr-label">کد QR</div>
    <div class="qr-img"><div class="qr-status" id="qr-status" aria-live="polite">در حال آماده‌سازی QR…</div><img id="qr-img" src="" alt="کد QR فاین وی‌پی‌ان" hidden></div>
    <button class="btn btn-g" style="width:100%;justify-content:center" onclick="closeQrModal()"><i class="ti ti-x"></i> بستن</button>
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
      <div class="modal-v2-field ns-destination-grid">
        <div><label><i class="ti ti-world"></i> آی‌پی مقصد (اختیاری)</label><input class="modal-v2-input" id="ns-address" dir="ltr" inputmode="text" placeholder="خالی = نشانی پیش‌فرض پنل"></div>
        <div><label><i class="ti ti-plug-connected"></i> پورت مقصد</label><input class="modal-v2-input" id="ns-port" type="number" min="1" max="65535" step="1" value="443" dir="ltr" inputmode="numeric"></div>
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
      <div class="fg" style="flex:1"><label>اثر انگشت مرورگر (uTLS)</label>
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
    <div class="fg" style="margin-bottom:13px"><label>آی‌پی مقصد دلخواه (خالی = دامنه پنل)</label><input class="fi" id="el-address" placeholder="مثلاً 203.0.113.10" style="width:100%"></div>
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
    <div class="mob-logo"><img class="fine-logo-mark" src="https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png" alt="لوگوی اصلی FineVPN" loading="eager" decoding="async" style="width:100%;height:100%;object-fit:contain;display:block"></div>
    <span class="mob-title">𝑭𝒊𝒏𝒆𝑽𝑷𝑵</span><span class="mob-version">𝒗₂.₀</span>
  </div>
  <div class="mob-right">
    <button class="menu-btn" id="open-sb"><i class="ti ti-menu-2"></i></button>
  </div>
</div>
<div class="overlay" id="overlay"></div>
<aside class="sidebar" id="sb">
  <button class="sb-close" id="close-sb"><i class="ti ti-x"></i></button>
  <div class="logo">
    <div class="logo-img"><img class="fine-logo-mark" src="https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png" alt="لوگوی اصلی FineVPN" loading="eager" decoding="async" style="width:100%;height:100%;object-fit:contain;display:block"></div>
    <div><div class="logo-name">𝑭𝒊𝒏𝒆𝑽𝑷𝑵</div><div class="logo-sub">مرکز مدیریت · 𝒗₂.₀</div></div>
  </div>
  <div class="nav-wrap">
    <div class="nav-sec">مدیریت سرویس‌ها</div>
    <div class="nav-it on" data-pg="overview"><i class="ti ti-layout-dashboard"></i> نمای کلی</div>
    <div class="nav-it" data-pg="links"><i class="ti ti-key"></i> کانفیگ‌ها <span class="nav-badge" id="links-nb">0</span></div>
    <div class="nav-it" data-pg="subgroups"><i class="ti ti-users-group"></i> پنل ساب <span class="nav-badge" id="subs-nb">0</span></div>
    <div class="nav-it" data-pg="subscriptions"><i class="ti ti-world-share"></i> درگاه اشتراک</div>
    <div class="nav-sec">پایش و گزارش</div>
    <div class="nav-it" data-pg="traffic"><i class="ti ti-chart-area-line"></i> ترافیک و مصرف</div>
    <div class="nav-it" data-pg="connections"><i class="ti ti-network"></i> اتصال‌های فعال <span class="nav-badge" id="conns-nb">0</span></div>
    <div class="nav-it" data-pg="logs"><i class="ti ti-history"></i> رویدادها</div>
    <div class="nav-it" data-pg="errors"><i class="ti ti-alert-triangle"></i> گزارش خطا</div>
    <div class="nav-sec">ابزارها و سیستم</div>
    <div class="nav-it" data-pg="categories"><i class="ti ti-category-2"></i> دسته‌بندی‌ها</div>
    <div class="nav-it" data-pg="ipcheck"><i class="ti ti-radar"></i> آزمایش آی‌پی‌ها</div>
    <div class="nav-it" data-pg="testws"><i class="ti ti-plug-connected"></i> آزمایش WebSocket</div>
    <div class="nav-it" data-pg="settings"><i class="ti ti-adjustments-cog"></i> تنظیمات و امنیت</div>
  </div>
  <div class="sb-foot">
    <button class="logout-btn" id="logout-btn"><i class="ti ti-logout"></i> خروج امن</button>
  </div>
</aside>
<main class="main">
<section class="pg on" id="pg-overview">
  <div class="dashboard-scene" aria-hidden="true">
    <div class="scene-stars"></div><div class="scene-planet"></div>
    <div class="scene-mountain scene-mountain-back"></div><div class="scene-mountain scene-mountain-front"></div>
    <div class="scene-logo-watermark"><img src="https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png" alt=""></div>
  </div>

  <header class="dash-head glass-surface">
    <div class="dash-server-pill"><span class="dash-pill-icon"><i class="ti ti-server-2"></i></span><span><b>وضعیت سرور</b><small id="server-status-badge"><span class="dot db"></span> در حال بررسی</small></span><i class="ti ti-world"></i></div>
    <div class="dash-welcome"><span class="dash-eyebrow">مرکز مدیریت فاین وی‌پی‌ان</span><h1>به پنل مدیریت خوش آمدید!</h1><p>مدیریت حرفه‌ای، سریع و یکپارچهٔ سرویس‌ها</p></div>
    <div class="dash-head-actions">
      <div class="dash-time-card"><i class="ti ti-calendar-time"></i><span id="dash-date">—</span><b id="dash-clock">—</b></div>
      <button class="dash-theme-toggle" id="theme-toggle-top" onclick="toggleTheme()" type="button" aria-label="تغییر حالت روشن و تاریک" title="تغییر حالت روشن و تاریک"><i class="ti ti-sun-moon" id="theme-toggle-icon"></i><span id="theme-toggle-label">حالت روشن</span></button>
      <div class="dash-admin-chip"><span class="dash-admin-avatar"><i class="ti ti-user-shield"></i></span><span><b>مدیر پنل</b><small>دسترسی امن</small></span><i class="ti ti-chevron-down"></i></div>
    </div>
  </header>

  <div class="dash-metrics">
    <article class="dash-metric metric-blue"><div class="dash-metric-icon"><i class="ti ti-users"></i></div><div class="dash-metric-copy"><span>کاربران متصل</span><strong id="m-conns">—</strong><small><b id="m-sessions">—</b> نشست زنده</small></div><div class="dash-metric-wave"></div></article>
    <article class="dash-metric metric-cyan"><div class="dash-metric-icon"><i class="ti ti-server-2"></i></div><div class="dash-metric-copy"><span>کل ترافیک مصرف‌شده</span><strong id="m-traffic">—<small class="m-unit"> MB</small></strong><small>از زمان راه‌اندازی</small></div><div class="dash-metric-wave"></div></article>
    <article class="dash-metric metric-teal"><div class="dash-metric-icon"><i class="ti ti-arrows-left-right"></i></div><div class="dash-metric-copy"><span>کانفیگ‌های فعال</span><strong id="m-alinks">—</strong><small id="m-lsub">از کل کانفیگ‌ها</small></div><div class="dash-metric-wave"></div></article>
    <article class="dash-metric metric-violet"><div class="dash-metric-icon"><i class="ti ti-bolt"></i></div><div class="dash-metric-copy"><span>گروه‌های ساب</span><strong id="m-subs">—</strong><small>گروه‌های ثبت‌شده</small></div><div class="dash-metric-wave"></div></article>
  </div>

  <div class="dash-feature-grid">
    <section class="dash-feature-card dash-sub-feature glass-surface">
      <div class="dash-feature-heading"><div><span class="dash-section-kicker">مدیریت زیرمجموعه‌ها</span><h2><i class="ti ti-users-group"></i> پنل ساب</h2><p>ساخت گروه، مدیریت اعضا و اشتراک‌های اختصاصی</p></div><button class="dash-view-all" type="button" onclick="navTo('subgroups')">مشاهده همه <i class="ti ti-arrow-left"></i></button></div>
      <div class="dash-sub-content">
        <div class="dash-sub-illustration"><div class="dash-orbit orbit-one"></div><div class="dash-orbit orbit-two"></div><div class="dash-user-bubble bubble-main"><i class="ti ti-user-filled"></i></div><div class="dash-user-bubble bubble-left"><i class="ti ti-user-filled"></i></div><div class="dash-user-bubble bubble-right"><i class="ti ti-user-filled"></i></div><div class="dash-sub-platform"></div><div class="dash-sub-caption"><b id="dash-sub-count">—</b><span>گروه اشتراک ثبت‌شده</span></div></div>
        <div class="dash-sub-controls">
          <button class="dash-action-row" onclick="openModal('modal-create-sub')"><span class="dash-action-icon"><i class="ti ti-folder-plus"></i></span><span><b>افزودن گروه ساب جدید</b><small>ایجاد گروه و لینک اشتراک</small></span><i class="ti ti-plus"></i></button>
          <button class="dash-action-row" onclick="navTo('subgroups')"><span class="dash-action-icon"><i class="ti ti-list-details"></i></span><span><b>مدیریت گروه‌های ساب</b><small>اعضا، لینک‌ها و وضعیت گروه‌ها</small></span><i class="ti ti-chevron-left"></i></button>
          <button class="dash-action-row" onclick="navTo('subscriptions')"><span class="dash-action-icon"><i class="ti ti-rss"></i></span><span><b>تنظیمات اشتراک</b><small>پیوندها و درگاه‌های اشتراک</small></span><i class="ti ti-chevron-left"></i></button>
          <button class="dash-action-row" onclick="navTo('traffic')"><span class="dash-action-icon"><i class="ti ti-chart-line"></i></span><span><b>گزارش و مصرف گروه‌ها</b><small>بررسی سهمیه و ترافیک</small></span><i class="ti ti-chevron-left"></i></button>
        </div>
      </div>
      <div class="dash-quick-create">
        <div class="dash-quick-title"><i class="ti ti-wand"></i><span><b>ساخت سریع گروه + ۲۴ کانفیگ</b><small>با سهمیه و مدت مشترک</small></span></div>
        <div class="dash-quick-fields">
          <input class="fi" id="qs-name" type="text" placeholder="نام گروه جدید">
          <input class="fi" id="qs-vol" type="number" min="0" step="0.5" value="20" aria-label="حجم مشترک به گیگابایت" placeholder="حجم (GB)">
          <input class="fi" id="qs-days" type="number" min="0" step="1" value="30" aria-label="مدت اعتبار به روز" placeholder="مدت (روز)">
          <input class="fi" id="qs-ip" type="number" min="0" step="1" value="2" aria-label="سقف کاربر هم‌زمان" placeholder="سقف کاربر">
          <input class="fi" id="qs-address" type="text" inputmode="url" autocomplete="off" spellcheck="false" aria-label="آی‌پی مقصد گروه" placeholder="آی‌پی دلخواه (اختیاری)">
          <input class="fi" id="qs-port" type="number" min="1" max="65535" value="443" aria-label="پورت اتصال گروه" placeholder="پورت">
          <button class="btn btn-p" id="qs-submit-btn" onclick="quickSubCreate()"><i class="ti ti-rocket"></i> ساخت گروه</button>
        </div>
        <div id="qs-summary" class="dash-quick-summary">حجم، اعتبار، سقف کاربر و مقصد اتصال را تعیین کنید. IP و پورت واردشده روی هر ۲۴ کانفیگ گروه اعمال می‌شود.</div>
        <div id="qs-result" class="dash-quick-result" style="display:none"><b><i class="ti ti-circle-check"></i> گروه ساخته شد</b><div><input id="qs-pub-link" class="fi" readonly><button class="btn btn-o" onclick="navigator.clipboard.writeText(document.getElementById('qs-pub-link').value).then(()=>toast('پیوند کپی شد','ok'))"><i class="ti ti-copy"></i> کپی پیوند</button></div></div>
      </div>
    </section>

    <section class="dash-feature-card dash-portal-feature glass-surface">
      <div class="dash-feature-heading"><div><span class="dash-section-kicker">مدیریت ورود و اشتراک</span><h2><i class="ti ti-layout-dashboard"></i> درگاه و پنل ورود</h2><p>دسترسی سریع به پنل ورود، کانفیگ‌ها و صفحهٔ کاربران</p></div><span class="dash-online-badge"><i class="ti ti-circle-filled"></i> آمادهٔ استفاده</span></div>
      <div class="dash-portal-visual"><div class="dash-portal-halo"></div><div class="dash-portal-core"><i class="ti ti-shield-lock"></i></div><div class="dash-portal-ring ring-a"></div><div class="dash-portal-ring ring-b"></div><div class="dash-portal-label"><b id="dash-portal-count">—</b><span>گروه دارای اشتراک</span></div></div>
      <div class="dash-portal-actions">
        <button class="dash-action-row" onclick="navTo('links')"><span class="dash-action-icon"><i class="ti ti-key"></i></span><span><b>مدیریت کانفیگ‌ها</b><small>ساخت، ویرایش و کپی لینک‌ها</small></span><i class="ti ti-chevron-left"></i></button>
        <button class="dash-action-row" onclick="navTo('subscriptions')"><span class="dash-action-icon"><i class="ti ti-world-share"></i></span><span><b>صفحهٔ درگاه اشتراک</b><small>پیوندهای عمومی و اختصاصی</small></span><i class="ti ti-chevron-left"></i></button>
        <button class="dash-action-row" onclick="navTo('connections')"><span class="dash-action-icon"><i class="ti ti-network"></i></span><span><b>اتصال‌های کاربران</b><small>نشست‌ها و آی‌پی‌های فعال</small></span><i class="ti ti-chevron-left"></i></button>
        <button class="dash-action-row" onclick="navTo('settings')"><span class="dash-action-icon"><i class="ti ti-settings"></i></span><span><b>تنظیمات پنل ورود</b><small>امنیت، حساب و پشتیبان‌گیری</small></span><i class="ti ti-chevron-left"></i></button>
      </div>
      <div class="dash-portal-footer"><span><i class="ti ti-lock-check"></i> ورود محافظت‌شده</span><span id="vol-badge" class="badge">در حال بررسی ذخیره‌سازی</span></div>
    </section>
  </div>

  <div class="dash-lower-grid">
    <section class="dash-table-card glass-surface">
      <div class="dash-lower-heading"><div><span class="dash-section-kicker">آخرین تغییرات</span><h2><i class="ti ti-list-details"></i> آخرین کانفیگ‌ها</h2></div><button class="dash-view-all" onclick="navTo('links')">مشاهده همه <i class="ti ti-arrow-left"></i></button></div>
      <div class="dash-table-wrap"><table class="dash-recent-table"><thead><tr><th>ردیف</th><th>نام کانفیگ</th><th>پروتکل</th><th>تاریخ ساخت</th><th>وضعیت</th><th>عملیات</th></tr></thead><tbody id="dash-recent-links"><tr><td colspan="6" class="dash-table-empty">در حال دریافت اطلاعات واقعی کانفیگ‌ها...</td></tr></tbody></table></div>
    </section>
    <section class="dash-status-card glass-surface">
      <div class="dash-lower-heading"><div><span class="dash-section-kicker">پایش لحظه‌ای</span><h2><i class="ti ti-activity-heartbeat"></i> وضعیت سرویس</h2></div><span class="dash-live-dot"><i class="ti ti-circle-filled"></i> زنده</span></div>
      <div class="dash-health-ring"><div class="dash-health-core"><img class="dash-health-logo" src="https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png" alt="" loading="lazy"><b id="dash-health-label">فعال</b><small>وضعیت سرویس</small></div></div>
      <div class="dash-status-lines"><div><span><i class="ti ti-clock"></i> زمان فعالیت</span><b id="uptime-inline">—</b></div><div><span><i class="ti ti-database"></i> ذخیره‌سازی</span><b id="dash-volume-state">در حال بررسی</b></div><div><span><i class="ti ti-gauge"></i> بار ترافیک</span><b id="bw-pct">—%</b></div></div>
      <div class="dash-progress"><span id="bw-bar"></span></div>
      <div class="dash-status-footer"><span>نسخهٔ پنل</span><b>𝒗₂.₀</b><span id="uptime-badge">—</span></div>
    </section>
  </div>

  <div class="dash-analytics-grid">
    <section class="dash-chart-card glass-surface"><div class="dash-lower-heading"><div><span class="dash-section-kicker">تحلیل داده</span><h2><i class="ti ti-chart-area-line"></i> ترافیک ساعتی</h2></div><span class="dash-chart-unit">مگابایت</span></div><div class="dash-chart-body"><canvas id="ch1"></canvas></div></section>
    <section class="dash-chart-card glass-surface"><div class="dash-lower-heading"><div><span class="dash-section-kicker">پروتکل‌های فعال</span><h2><i class="ti ti-chart-donut-3"></i> توزیع پروتکل‌ها</h2></div><span class="dash-chart-unit">واقعی</span></div><div class="dash-chart-body dash-chart-donut"><canvas id="ch2"></canvas></div></section>
  </div>

  <div class="dash-footer-note"><img src="https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png" alt="" loading="lazy"><span><b>FineVPN</b> · مرکز مدیریت سرویس‌های امن</span><a href="https://t.me/sadiq_AFG1" target="_blank" rel="noopener noreferrer"><i class="ti ti-brand-telegram"></i> پشتیبانی</a></div>

  <div class="dash-hidden-compat" aria-hidden="true"><div id="vless-main">در حال دریافت پیوند پیش‌فرض...</div></div>
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
          <div class="cp-block-label"><i class="ti ti-fingerprint"></i> اثر انگشت مرورگر (uTLS)</div>
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
        <div class="cp-block" style="flex:1">
          <div class="cp-block-label"><i class="ti ti-world-pin"></i> آی‌پی مقصد دلخواه (اختیاری)</div>
          <input class="cp-input-full" id="nl-address" type="text" inputmode="url" autocomplete="off" spellcheck="false" placeholder="خالی = استفاده از دامنه پنل">
          <div style="font-size:10px;color:var(--t3);margin-top:5px">در صورت واردکردن IP، نام دامنه برای SNI و Host حفظ می‌شود.</div>
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
      <button class="dash-theme-toggle subpage-theme-toggle" id="subgroup-theme-toggle" onclick="toggleTheme()" type="button" aria-label="تغییر حالت روشن و تاریک"><i class="ti ti-sun" id="subgroup-theme-icon"></i><span id="subgroup-theme-label">حالت روشن</span></button>
      <button class="btn btn-pur" onclick="openModal('modal-create-sub')"><i class="ti ti-folder-plus"></i> ساخت گروه جدید</button>
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
  <div class="topbar"><div><div class="tb-title"><i class="ti ti-rss"></i> اشتراک‌ها</div><div class="tb-sub">پیوندهای اشتراک برای برنامه‌های سازگار با V2Ray</div></div></div>
  <div class="sec-hero">
    <div class="sec-hero-tile"><div class="sec-hero-ico"><i class="ti ti-rss"></i></div><div class="sec-hero-label">سابسکریپشن‌های فعال</div><div class="sec-hero-val" id="sb-count">—</div><div class="sec-hero-sub">گروه‌های دارای لینک ساب</div></div>
    <div class="sec-hero-tile"><div class="sec-hero-ico pur"><i class="ti ti-link"></i></div><div class="sec-hero-label">کل کانفیگ‌ها</div><div class="sec-hero-val" id="sb-links">—</div><div class="sec-hero-sub">قابل اشتراک‌گذاری</div></div>
    <div class="sec-hero-tile"><div class="sec-hero-ico amb"><i class="ti ti-devices"></i></div><div class="sec-hero-label">اپ‌های پشتیبانی‌شده</div><div class="sec-hero-val" style="font-size:15px">کلاینت‌های سازگار</div><div class="sec-hero-sub">و سایر کلاینت‌های VLESS</div></div>
  </div>
  <div class="g2">
    <div class="sec-panel">
      <div class="sec-panel-head"><div class="sec-panel-ico"><i class="ti ti-rss"></i></div><div><div class="sec-panel-title">اشتراک تکی</div><div class="sec-panel-sub">هر کانفیگ پیوند اشتراک مخصوص خود را دارد</div></div></div>
      <div class="sec-panel-body"><p style="font-size:11.5px;color:var(--t3);line-height:1.9">از کارت کانفیگ روی آیکون <i class="ti ti-rss" style="color:var(--accent)"></i> کلیک کنید تا پیوند اشتراک همان کانفیگ کپی شود.</p></div>
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
    <div class="sec-hero-tile"><div class="sec-hero-ico"><i class="ti ti-server"></i></div><div class="sec-hero-label">نسخه پنل</div><div class="sec-hero-val" style="font-size:16px">𝑭𝒊𝒏𝒆𝑽𝑷𝑵 𝒗₂.₀</div><div class="sec-hero-sub">ساختار ۲۴ کانفیگ پرفورمنت</div></div>
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


<section class="pg" id="pg-ipcheck">
  <div class="topbar">
    <div><div class="tb-title"><i class="ti ti-radar"></i> آزمایش و بررسی آی‌پی‌ها</div><div class="tb-sub">اندازه‌گیری پاسخ‌گویی واقعی ICMP برای حداکثر ۵۰۰ نشانی عمومی و خصوصی</div></div>
    <div class="tb-right"><span class="badge bg-blue" id="ip-scan-state">آماده آزمایش</span></div>
  </div>
  <div class="ip-scan-layout">
    <div class="sec-panel ip-scan-input-panel">
      <div class="sec-panel-head"><div class="sec-panel-ico"><i class="ti ti-list-numbers"></i></div><div><div class="sec-panel-title">فهرست آی‌پی‌ها</div><div class="sec-panel-sub">هر آی‌پی را در یک خط وارد کنید؛ حداکثر ۵۰۰ مورد</div></div></div>
      <div class="sec-panel-body">
        <textarea id="ip-scan-input" class="fi ip-scan-textarea" rows="9" placeholder="1.1.1.1&#10;8.8.8.8&#10;9.9.9.9" spellcheck="false" autocapitalize="off"></textarea>
        <div class="ip-scan-meta"><span id="ip-scan-count">۰ آی‌پی وارد شده</span><span>عمومی و خصوصی · IPv4 / IPv6</span></div>
        <div class="ip-progress-wrap" id="ip-progress-wrap" aria-live="polite"><div class="ip-progress-head"><b id="ip-progress-text">آمادهٔ شروع آزمایش</b><span id="ip-progress-pct">۰٪</span></div><div class="ip-progress-track"><i id="ip-progress-fill"></i></div></div>
        <div class="ip-scan-actions">
          <button class="btn btn-p" id="ip-scan-run" onclick="runIpScan()"><i class="ti ti-player-play"></i> شروع آزمایش</button>
          <button class="btn btn-o" onclick="clearIpScan()"><i class="ti ti-eraser"></i> پاک‌کردن</button>
          <button class="btn btn-g" onclick="copyIpInput()"><i class="ti ti-copy"></i> کپی فهرست</button>
        </div>
        <div class="ip-scan-note"><i class="ti ti-info-circle"></i><span>این ابزار فقط پینگ ICMP انجام می‌دهد. پاسخ‌گرفتن، پاک‌بودن IP یا کارکرد قطعی VLESS را ثابت نمی‌کند. بعضی میزبان‌ها یا شبکه‌ها پاسخ ICMP را مسدود می‌کنند.</span></div>
      </div>
    </div>
    <div class="ip-scan-stats">
      <div class="ip-stat-card"><div class="ip-stat-icon"><i class="ti ti-checks"></i></div><div><div class="ip-stat-label">پاسخ‌داده</div><div class="ip-stat-value" id="ip-stat-good">۰</div></div></div>
      <div class="ip-stat-card"><div class="ip-stat-icon bad"><i class="ti ti-x"></i></div><div><div class="ip-stat-label">بدون پاسخ</div><div class="ip-stat-value" id="ip-stat-bad">۰</div></div></div>
      <div class="ip-stat-card"><div class="ip-stat-icon wait"><i class="ti ti-help"></i></div><div><div class="ip-stat-label">نامشخص</div><div class="ip-stat-value" id="ip-stat-unknown">۰</div></div></div>
      <div class="ip-stat-card"><div class="ip-stat-icon total"><i class="ti ti-list-check"></i></div><div><div class="ip-stat-label">بررسی‌شده</div><div class="ip-stat-value" id="ip-stat-total">۰</div></div></div>
      <div class="ip-stat-card"><div class="ip-stat-icon total"><i class="ti ti-world"></i></div><div><div class="ip-stat-label">نشانی عمومی</div><div class="ip-stat-value" id="ip-stat-public">۰</div></div></div>
      <div class="ip-stat-card"><div class="ip-stat-icon wait"><i class="ti ti-home-network"></i></div><div><div class="ip-stat-label">نشانی خصوصی</div><div class="ip-stat-value" id="ip-stat-private">۰</div></div></div>
    </div>
  </div>
  <div class="sec-panel ip-results-panel">
    <div class="sec-panel-head"><div class="sec-panel-ico"><i class="ti ti-table"></i></div><div><div class="sec-panel-title">نتیجه آزمایش</div><div class="sec-panel-sub" id="ip-results-caption">هنوز آزمایشی انجام نشده است</div></div>
      <div class="ip-result-copy"><button class="btn btn-sm btn-g" onclick="copyIpResults('public')"><i class="ti ti-world"></i> کپی عمومی</button><button class="btn btn-sm btn-o" onclick="copyIpResults('private')"><i class="ti ti-home-network"></i> کپی خصوصی</button><button class="btn btn-sm btn-p" onclick="copyIpResults('all')"><i class="ti ti-copy"></i> کپی همه</button></div>
    </div>
    <div class="sec-panel-body">
      <div class="ip-results-filters" role="group" aria-label="فیلتر نتیجه آزمایش">
        <button type="button" class="ip-filter active" data-ip-filter="all" onclick="setIpFilter('all')">همه</button>
        <button type="button" class="ip-filter" data-ip-filter="public" onclick="setIpFilter('public')">عمومی</button>
        <button type="button" class="ip-filter" data-ip-filter="private" onclick="setIpFilter('private')">خصوصی</button>
        <button type="button" class="ip-filter" data-ip-filter="reachable" onclick="setIpFilter('reachable')">پاسخ‌دار</button>
        <button type="button" class="ip-filter" data-ip-filter="unreachable" onclick="setIpFilter('unreachable')">بدون پاسخ</button>
      </div>
      <div class="ip-results-list" id="ip-results-list"><div class="empty"><i class="ti ti-radar"></i><p>فهرست آی‌پی‌ها را وارد و آزمایش را شروع کنید.</p></div></div>
    </div>
  </div>
</section>
</main>
<script>
let currentLang='fa';
let fineTheme='dark';
try{fineTheme=localStorage.getItem('finevpn-theme')==='light'?'light':'dark';}catch(e){}
function applyTheme(theme){
  if(theme==='light'||theme==='dark')fineTheme=theme;
  document.documentElement.setAttribute('data-theme',fineTheme);
  try{localStorage.setItem('finevpn-theme',fineTheme);}catch(e){}
  const icon=document.getElementById('theme-toggle-icon');
  const label=document.getElementById('theme-toggle-label');
  const button=document.getElementById('theme-toggle-top');
  if(icon)icon.className='ti '+(fineTheme==='dark'?'ti-sun':'ti-moon');
  if(label)label.textContent=fineTheme==='dark'?'حالت روشن':'حالت تاریک';
  if(button)button.setAttribute('aria-pressed',String(fineTheme==='light'));
  const subIcon=document.getElementById('subgroup-theme-icon');
  const subLabel=document.getElementById('subgroup-theme-label');
  const subButton=document.getElementById('subgroup-theme-toggle');
  if(subIcon)subIcon.className='ti '+(fineTheme==='dark'?'ti-sun':'ti-moon');
  if(subLabel)subLabel.textContent=fineTheme==='dark'?'حالت روشن':'حالت تاریک';
  if(subButton)subButton.setAttribute('aria-pressed',String(fineTheme==='light'));
}

function toggleTheme(){applyTheme(fineTheme==='dark'?'light':'dark');}
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
'داشبورد':'Dashboard','کانفیگ‌ها':'Configurations','گروه‌های ساب':'Subscription Groups','سابسکریپشن':'Subscriptions','ترافیک':'Traffic','اتصالات':'Connections','امنیت':'Security','لاگ فعالیت‌ها':'Activity Logs','خطاها':'Errors','تست WebSocket':'WebSocket Test','تنظیمات':'Settings','پشتیبانی':'Support','ورود به داشبورد':'Sign in to dashboard','ورود به پنل':'Panel Sign In','ساخت کانفیگ جدید':'Create New Configuration','گروه‌های ساب':'Subscription Groups','پشتیبانی':'Support','تنظیمات سیستم':'System Settings','تغییر رمز عبور':'Change Password','ذخیره تغییرات':'Save Changes','ذخیره رمز جدید':'Save New Password','انصراف':'Cancel','ذخیره':'Save','بستن':'Close','رفرش':'Refresh','کپی':'Copy','دانلود Backup':'Download Backup','Export لینک‌ها':'Export Links','پشتیبانی مستقیم':'Direct Support','وب‌سایت رسمی':'Official Website','تلگرام':'Telegram','اینستاگرام':'Instagram','یوتیوب':'YouTube','توییتر / X':'Twitter / X','سازنده':'Creator','فعال':'Active','نامحدود':'Unlimited','در حال بارگذاری...':'Loading...','پیش‌فرض اولیه · Initial defaults':'Initial defaults','نام کاربری':'Username','رمز عبور · Password':'Password','کد امنیتی · Security code':'Security code','کد / code':'Code','در حال ورود...':'Signing in...','خروج':'Logout','پنل':'Panel','سیستم':'System','کانفیگ‌ها':'Configurations','گروه جدید':'New Group','ساخت کانفیگ':'Create Configuration','ساخت سریع گروه ساب (۲۴ کانفیگ)':'Quick Subscription Group (24 Configs)','ساخت خودکار گروه ساب، تنظیم حجم مشترک و تولید ۲۴ کانفیگ با یک کلیک':'Create a subscription group with shared quota and 24 configs in one click','گروه دسترسی':'Access Group','کپی همه‌ی کانفیگ‌ها':'Copy All Configurations','کپی همه':'Copy All','اتصالات زنده':'Live Connections','کل مصرف':'Total Usage','سهمیه و اعتبار گروه':'Group Quota and Validity','کانفیگ‌های فعال':'Active Configurations','ذخیره‌سازی و ماندگاری داده':'Storage and Data Persistence','پشتیبان‌گیری و بازیابی':'Backup and Restore','امنیت و نشست‌ها':'Security and Sessions','تغییر نام کاربری و رمز عبور':'Change Username and Password','دانلود بکاپ':'Download Backup','بارگذاری بکاپ':'Upload Backup','حذف':'Delete','فعال':'Active','غیرفعال':'Inactive','ساخت':'Create','هر گروه یک صفحه پابلیک مجزا با کانفیگ‌های خودش دارد':'Each group has its own public page and configurations','نام کانفیگ':'Configuration name','عنوان':'Title','نام گروه ساب':'Subscription group name','گروه‌های اشتراک':'Subscription groups','گروه اشتراک':'Subscription group','توضیحات':'Description','حجم':'Traffic quota','حجم مشترک':'Shared quota','مدت اعتبار':'Validity period','روز':'days','بدون محدودیت':'Unlimited','مصرف‌شده':'Used','باقی‌مانده':'Remaining','آمار':'Statistics','عملیات':'Actions','ذخیره':'Save','بازگشت':'Back','بستن':'Close','لغو':'Cancel','حذف گروه':'Delete group','حذف کانفیگ':'Delete configuration','تأیید':'Confirm','بله':'Yes','خیر':'No','در حال ذخیره...':'Saving...','خطا':'Error','موفقیت':'Success','اطلاعات ذخیره شد':'Information saved','کشور خروجی':'Exit-country label','پرچم کشور':'Country flag','انتخاب همه':'Select all','انتخاب‌شده':'Selected','حذف انتخاب‌شده‌ها':'Delete selected','فعال‌سازی':'Activate','غیرفعال‌سازی':'Deactivate','ریست مصرف':'Reset usage','تازه‌سازی':'Refresh','پشتیبانی':'Support'

,'مدیریت کانفیگ‌های':'Manage configurations','کانفیگ‌هایی که می‌خواهید در این گروه باشند را انتخاب کنید':'Choose the configurations to include in this group','انتخاب همه':'Select all','لغو همه':'Clear all','۰ انتخاب شده':'0 selected','تغییرات بلافاصله اعمال می‌شود':'Changes take effect immediately','ساخت گروه ساب':'Create subscription group','یک صفحه پابلیک مجزا با ۲۴ کانفیگ خودکار بسازید':'Create a separate public page with 24 automatically generated configurations','نام گروه':'Group name','توضیحات (اختیاری)':'Description (optional)','رمز صفحه پابلیک (اختیاری)':'Public page password (optional)','ساخت سریع ۲۴ کانفیگ':'Quick-create 24 configurations','۳ پروتکل × ۲ فینگرپرینت × ۴ ALPN = ۲۴ کانفیگ (VWS/XPU/XHS)':'3 protocols × 2 fingerprints × 4 ALPN options = 24 configurations','حجم مشترک کل (GB)':'Total shared quota (GB)','روزهای اعتبار':'Validity days','حداکثر کاربر هم‌زمان (IP Limit)':'Maximum simultaneous users (IP limit)','حجم مشترک بین تمام ۲۴ کانفیگ تقسیم می‌شود. هر کاربر از هر کانفیگی مصرف کند، از همین حجم کم می‌شود.':'The shared quota is used by all 24 configurations. Traffic from any configuration reduces this same quota.','ساخت گروه + ۲۴ کانفیگ':'Create group + 24 configurations','ویرایش کانفیگ':'Edit configuration','سهمیه (0 = نامحدود)':'Quota (0 = unlimited)','واحد':'Unit','انقضا (روز از الان، 0 = بدون تغییر/نامحدود)':'Expiry (days from now; 0 = unchanged/unlimited)','یادداشت':'Note','ALPN (خالی = پیش‌فرض)':'ALPN (blank = default)','پورت اتصال':'Connection port','محدودیت آی‌پی (0 = نامحدود)':'IP limit (0 = unlimited)','محدودیت سرعت (0 = نامحدود)':'Speed limit (0 = unlimited)','برای حفظ انقضای فعلی، فیلد انقضا را صفر بگذارید.':'Set expiry to 0 to keep the current expiry.','ساخت خودکار گروه ساب، تنظیم حجم مشترک و تولید ۲۴ کانفیگ با یک کلیک':'Create a subscription group, set a shared quota, and generate 24 configurations in one click','نام گروه ساب':'Subscription group name','حجم مشترک (GB) —':'Shared quota (GB) —','۰ = نامحدود':'0 = unlimited','مدت اعتبار (روز) —':'Validity period (days) —','سقف کاربر (IP) —':'User limit (IP) —','ساخت گروه ساب + ۲۴ کانفیگ با حجم مشترک':'Create subscription group + 24 configurations with shared quota','گروه ساب و ۲۴ کانفیگ با موفقیت ساخته شد!':'Subscription group and 24 configurations created successfully!','رفرش':'Refresh','اتصالات فعال':'Active connections','زنده':'Live','کل ترافیک':'Total traffic','از راه‌اندازی':'Since startup','کانفیگ فعال':'Active configuration','از کل':'of total','لینک پیش‌فرض (بدون محدودیت)':'Default link (unlimited)','در حال دریافت...':'Loading...','کانفیگ محدود':'Limited configuration','ترافیک ساعتی (MB)':'Hourly traffic (MB)','توزیع پروتکل‌ها':'Protocol distribution','وضعیت سرویس':'Service status','فعال · سخت‌گیرانه':'Active · strict','فعال · 3 mode':'Active · 3 modes','فعال v9':'Active v9','آپتایم':'Uptime','بار نسبی':'Relative load','ارائه‌دهنده: مـحـمـدصـادق افـغـان':'Provider: Muhammad Sadiq Afghan','ساخت و مدیریت کانفیگ با سهمیه، انقضا و گروه‌بندی':'Create and manage configurations with quotas, expiry, and groups','همه دسته‌ها':'All categories','ساخت کانفیگ جدید':'Create new configuration','UUID تصادفی · سهمیه، انقضا و پروتکل رو انتخاب کن':'Random UUID · choose quota, expiry, and protocol','شناسه کانفیگ':'Configuration ID','— بدون دسته —':'— No category —','گروه ساب و انقضا':'Subscription group and expiry','— بدون گروه —':'— No group —','۷ روز':'7 days','۳۰ روز':'30 days','۹۰ روز':'90 days','سهمیه ترافیک':'Traffic quota','۵۰۰ MB':'500 MB','۱ GB':'1 GB','۵ GB':'5 GB','۱۰ GB':'10 GB','۵۰ GB':'50 GB','پروتکل انتقال':'Transport protocol','پایدار و همه‌منظوره':'Stable and general-purpose','سازگار با CDN':'CDN compatible','تاخیر پایین‌تر':'Lower latency','پیش‌فرض پروتکل':'Protocol default','دستی...':'Manual...','محدودیت آی‌پی / کاربر هم‌زمان':'IP limit / simultaneous users','۱ کاربر':'1 user','۲ کاربر':'2 users','۵ کاربر':'5 users','۱ Mbps':'1 Mbps','۵ Mbps':'5 Mbps','۱۰ Mbps':'10 Mbps','۲۵ Mbps':'25 Mbps','UUID کاملاً رندوم تولید می‌شود · فقط UUID‌های ثبت‌شده اجازه اتصال دارند · پروتکل پس از ساخت قابل تغییر نیست.':'UUIDs are random · only registered UUIDs can connect · protocol cannot be changed after creation.','هنوز کانفیگی وجود ندارد':'No configurations yet','هر گروه یک صفحه پابلیک مجزا با کانفیگ‌های خودش دارد':'Each group has its own public page and configurations','۰ گروه':'0 groups','گروه جدید':'New group','هنوز گروهی وجود ندارد':'No groups yet','یک گروه جدید بسازید تا کانفیگ‌ها را دسته‌بندی کنید':'Create a group to organize configurations','لینک‌های اشتراک برای اپ‌های v2ray':'Subscription links for V2Ray apps','سابسکریپشن‌های فعال':'Active subscriptions','گروه‌های دارای لینک ساب':'Groups with subscription links','کل کانفیگ‌ها':'Total configurations','قابل اشتراک‌گذاری':'Shareable','اپ‌های پشتیبانی‌شده':'Supported apps','و سایر کلاینت‌های VLESS':'and other VLESS clients','سابسکریپشن تکی':'Individual subscription','هر کانفیگ پیوند اشتراک مخصوص خود را دارد':'Each configuration has its own subscription URL','از کارت کانفیگ روی آیکون':'On a configuration card, click the icon','کلیک کنید تا پیوند اشتراک همان کانفیگ کپی شود.':'to copy that configuration’s subscription URL.','سابسکریپشن کامل (ادمین)':'Full subscription (admin)','شامل تمام کانفیگ‌های فعال':'Includes all active configurations','این آدرس فقط در مرورگری که به پنل وارد شده کار می‌کند (نیاز به کوکی سشن).':'This URL works only in a browser signed in to the panel (session cookie required).','لینک سابسکریپشن گروه‌ها':'Group subscription links','هر گروه یک صفحه پابلیک مجزا':'Each group has a separate public page','تحلیل و مانیتورینگ مصرف پهنای باند':'Bandwidth usage analytics and monitoring','کل ترافیک مصرفی':'Total traffic used','میانگین ساعتی':'Hourly average','MB در ساعت':'MB per hour','پیک مصرف':'Peak usage','بالاترین ساعت':'Highest hour','کمترین مصرف':'Lowest usage','روند مصرف ترافیک':'Traffic usage trend','بر اساس مگابایت در هر ساعت':'Megabytes per hour','مصرف':'Usage','میانگین':'Average','مانیتورینگ زنده‌ی آی‌پی و ترافیک هر اتصال':'Live IP and traffic monitoring for each connection','مجموع ترافیک لحظه‌ای':'Current total traffic','میانگین مدت اتصال':'Average connection duration','آی‌پی‌های یکتا':'Unique IPs','لیست اتصالات':'Connection list','بروزرسانی خودکار هر ۵ ثانیه':'Auto-refresh every 5 seconds','هیچ اتصال فعالی نیست':'No active connections','به محض اتصال کلاینت‌ها، اینجا نمایش داده می‌شوند':'Clients appear here when they connect','فعالیت ساب‌ها':'Subscription activity','کارتی ساب‌ها + اتصال زنده IP → کانفیگ + لاگ کامل':'Subscription cards + live IP-to-config connections + full logs','اتصال‌های زنده':'Live connections','الان اتصال فعالی وجود ندارد':'There are no active connections right now','لاگ کامل فعالیت':'Full activity log','همه نوعها':'All types','کانفیگ':'Configuration','گروه':'Group','ورود':'Login','اتصال':'Connection','هنوز لاگی ثبت نشده':'No logs recorded yet','خطاهای ثبت‌شده‌ی سیستم':'System errors recorded','تعداد خطاها':'Error count','از زمان راه‌اندازی':'Since startup','آخرین خطا':'Latest error','وضعیت سیستم':'System status','سالم':'Healthy','همه سرویس‌ها فعال':'All services are active','لاگ خطاها':'Error log','خطاهای ثبت‌شده‌ی سیستم از زمان آخرین ریست':'System errors since the last reset','تست اتصال VLESS/WS روی UUID فعال':'Test VLESS/WS connection using an active UUID','فقط UUID‌های ثبت‌شده و فعال اتصال برقرار می‌کنند (این فقط تست VLESS/WS است؛ تست XHTTP از خود کلاینت انجام می‌شود).':'Only registered, active UUIDs can connect (this tests VLESS/WS; test XHTTP from the client app).','UUID (باید در کانفیگ‌ها وجود داشته باشد)':'UUID (must exist in configurations)','قطع':'Disconnect','ارسال':'Send','منتظر اتصال...':'Waiting for connection...','دسته‌بندی کانفیگ‌ها':'Configuration categories','کانفیگ‌ها را به دسته‌های منطقی تقسیم کنید':'Organize configurations into logical categories','۰ دسته':'0 categories','ساخت دسته جدید':'Create category','نام و رنگ دسته را انتخاب کنید':'Choose a category name and color','دسته‌های ساخته‌شده':'Created categories','هر دسته تعداد کانفیگ‌های متعلق به خود را نشان می‌دهد':'Each category shows how many configurations belong to it','پیکربندی پنل و اطلاعات سرور':'Panel configuration and server information','نسخه پنل':'Panel version','ساختار ۲۴ کانفیگ پرفورمنت':'24-configuration performance setup','آپتایم سرور':'Server uptime','از آخرین ریست':'Since last reset','هاست پابلیک':'Public host','لینک‌های ساب از اینجا':'Subscription links from here','اطلاعات سرور':'Server information','مشخصات زیرساخت فعال':'Active infrastructure details','کانفیگ‌ها، ساب‌ها و مصرف حجم بعد از دیپلوی حفظ می‌شوند؟':'Do configurations, subscriptions, and traffic usage persist after deployment?','مدیریت دسترسی پنل':'Panel access management','نام کاربری جدید':'New username','رمز فعلی':'Current password','رمز جدید':'New password','بکاپ کامل کانفیگ‌ها و ساب‌ها':'Full backup of configurations and subscriptions','فایل بکاپ شامل کانفیگ‌ها، گروه‌ها، حجم مصرفی و تنظیمات است. برای حفظ اطلاعات پس از استقرار مجدد، ذخیره‌سازی پایدار را فعال کنید و پشتیبان را جداگانه نگه دارید.':'The backup contains configurations, groups, traffic usage, and settings. Enable persistent storage and keep a separate backup to retain data after redeployments.','بارگذاری بکاپ':'Upload backup','مدیریت دستگاه‌های واردشده به پنل':'Manage devices signed in to the panel','خروج از سایر دستگاه‌ها':'Sign out of other devices','منابع سرور':'Server resources','CPU، RAM و شبکه‌ی همین سرویس':'CPU, RAM, and network usage for this service'
};
Object.assign(I18N, {"دسته‌بندی‌ها":"Categories","۰ کانفیگ":"0 configurations","محدودیت سرعت":"Speed limit","۰ انتخاب":"0 selected","۰":"0","جستجوی کانفیگ...":"Search configurations...","مثلاً: کانال اختصاصی":"e.g. VIP group","توضیح کوتاه درباره این گروه":"Short description of this group","خالی بگذارید = بدون رمز":"Leave blank = no password","مثلا 1 (خالی = نامحدود)":"e.g. 1 (blank = unlimited)","مثلا 30 (۰ = بدون انقضا)":"e.g. 30 (0 = no expiry)","مثلا 2 (۰ = نامحدود)":"e.g. 2 (0 = unlimited)","مثلاً: h2,http/1.1":"e.g. h2,http/1.1","مثلاً: سرویس VIP":"e.g. VIP service","مثلاً: کاربر علی":"e.g. User Ali","یادداشت (اختیاری)":"Note (optional)","انقضا (روز) · 0 = نامحدود":"Expiry (days) · 0 = unlimited","0 = نامحدود":"0 = unlimited","مقدار دستی ALPN":"Manual ALPN value","جستجو در گروه‌ها...":"Search groups...","🔍 جستجو در لاگ...":"🔍 Search logs...","UUID یک کانفیگ فعال":"UUID of an active configuration","پیام تست...":"Test message...","نام دسته جدید (مثلاً: VIP)":"New category name (e.g. VIP)","نام کاربری فعلی را نگه دارید":"Keep current username","خالی = بدون تغییر":"Blank = no change","وضعیت ذخیره‌سازی":"Storage status","دسته":"Category","هنوز دسته‌ای ساخته نشده":"No categories have been created yet","نام دسته الزامی است":"Category name is required","دسته ساخته شد ✓":"Category created ✓","خطا در ساخت دسته":"Failed to create category","حذف این دسته؟ کانفیگ‌ها به «عمومی» برمی‌گردند.":"Delete this category? Configurations will be moved to General.","دسته حذف شد":"Category deleted","خطا در حذف":"Delete failed","نشست فعلی شما است":"This is your current session","نامشخص":"Unknown","آی‌پی":"IP address","زمان ورود":"Login time","از همه‌ی دستگاه‌های دیگر خارج می‌شوید. ادامه؟":"You will be signed out from all other devices. Continue?","نشست لغو شد":"Session revoked","پردازنده":"CPU","روی":"on","هسته · لود":"cores · load","حافظه (این سرویس)":"Memory (this service)","MB کل سرور":"MB total server memory","دیسک":"Disk","% آزاد":"% free","شبکه":"Network","منقضی":"Expired","نامحدود":"Unlimited","حالت فارسی فعال شد":"Persian mode enabled","رمز فعلی را وارد کنید":"Enter the current password","چیزی برای تغییر وارد نشده":"Nothing to change was entered","رمز جدید حداقل ۶ کاراکتر":"New password must be at least 6 characters","در حال ذخیره...":"Saving...","خطا در به‌روزرسانی":"Update failed","✓ ذخیره شد":"✓ Saved","اعلان ورود به‌روزرسانی شد ✓":"Login notice updated ✓","در حال ساخت بکاپ...":"Creating backup...","خطا در ساخت بکاپ":"Backup creation failed","✓ بکاپ دانلود شد":"✓ Backup downloaded","بازگردانی بکاپ، تمام کانفیگ‌ها و ساب‌های فعلی را جایگزین می‌کند. ادامه می‌دهید؟":"Restoring this backup will replace all current configurations and subscriptions. Continue?","در حال بازگردانی...":"Restoring...","خطا در بازگردانی":"Restore failed","کانفیگ و":"Configuration and","ساب بازگردانی شد":"subscription restored","بکاپ بازگردانی شد ✓":"Backup restored ✓","فایل پشتیبان دانلود شد":"Backup file downloaded","دانلود پشتیبان ناموفق بود":"Backup download failed","Export لینک‌ها ناموفق بود":"Failed to export links","ولوم دائمی":"Persistent volume","ذخیره موقت":"Temporary storage","دیسک دائمی:":"Persistent storage:","مگابایت آزاد":"MB free","هیچ Volume پایداری شناسایی نشد؛ یک Volume به سرویس متصل کنید و Mount Path را /data قرار دهید.":"No persistent Volume detected. Attach a Volume to the service and set its mount path to /data.","آخرین بروزرسانی:":"Last updated:","همین الان":"just now","دقیقه پیش":"minutes ago","ساعت پیش":"hours ago","روز پیش":"days ago","روشن/خاموش":"Enable/disable","هنوز سابی وجود ندارد":"No subscriptions yet","در حال بارگذاری...":"Loading...","الان اتصال فعالی برای این ساب وجود ندارد":"There is no active connection for this subscription right now","مصرف به تفکیک کانفیگ":"Usage by configuration","هنوز رویدادی ثبت نشده":"No events recorded yet","ساب روشن شد ✓":"Subscription enabled ✓","ساب خاموش شد":"Subscription disabled","خطا در تغییر وضعیت":"Failed to change status","انتخاب کانفیگ":"Select configuration","UUID کپی شد":"UUID copied","آی‌پی‌های متصل / محدودیت":"Connected IPs / limit","فعال/غیرفعال":"Enable/disable","لینک کپی شد":"Link copied","اشتراک کپی شد":"Sub copied","ویرایش":"Edit","انتخاب":"Select","ابتدا کانفیگ‌ها را انتخاب کنید":"Select configurations first","فعال‌کردن":"Activate","غیرفعال‌کردن":"Deactivate","صفرکردن مصرف":"Reset usage","این کانفیگ‌ها برای همیشه حذف می‌شوند. ادامه می‌دهید؟":"These configurations will be permanently deleted. Continue?","برای کانفیگ اجرا شود؟":"Apply to the selected configurations?","مورد انجام شد ✓":"items processed ✓","عملیات گروهی ناموفق بود:":"Bulk operation failed:","کانفیگ جدید":"New configuration","کانفیگ ساخته شد ✓":"Configuration created ✓","خطا در ساخت":"Creation failed","کانفیگ ویرایش شد ✓":"Configuration updated ✓","خطا در ویرایش":"Update failed","فعال شد ✓":"Enabled ✓","غیرفعال شد":"Disabled","مصرف ریست شد ✓":"Usage reset ✓","حذف این کانفیگ؟":"Delete this configuration?","حذف شد ✓":"Deleted ✓","بدون توضیحات":"No description","رمزدار":"Password-protected","پابلیک":"Public","صفحه پابلیک":"Public page","لینک پابلیک کپی شد":"Public link copied","کپی پابلیک":"Copy public link","باز کردن":"Open","لینک ساب (base64)":"Subscription link (base64)","لینک ساب کپی شد":"Subscription link copied","کپی ساب":"Copy subscription","QR ساب":"Subscription QR","گروه ساخته شد ✓":"Group created ✓","خطا در ساخت گروه":"Failed to create group","گروه سریع":"Quick group","نام گروه را وارد کنید":"Enter a group name","مقادیر نمی‌توانند منفی باشند":"Values cannot be negative","حجم مشترک حداقل ۱ مگابایت باید باشد":"Shared quota must be at least 1 MB","در حال ساخت...":"Creating...","ساخت گروه شکست خورد":"Group creation failed","هشدار: تنظیم حجم مشترک ناموفق بود":"Warning: failed to set shared quota","هشدار: حجم مشترک درست ثبت نشد":"Warning: shared quota was not saved correctly","کانفیگ ساخته شد":"Configuration created","گروه ساخته شد. لینک سابسکریپشن کپی شود؟":"Group created. Copy the subscription link?","خطا در ساخت سریع":"Quick creation failed","این گروه و فقط کانفیگ‌های وابسته به همین گروه حذف می‌شوند. کانفیگ‌های گروه‌های دیگر باقی می‌مانند. ادامه می‌دهید؟":"This group and only its associated configurations will be deleted. Configurations in other groups will remain. Continue?","گروه حذف شد ✓":"Group deleted ✓","خطا در بارگذاری":"Loading failed","کپی لینک VLESS":"Copy VLESS link","ساب کپی شد":"Subscription copied","کپی پیوند اشتراک":"Copy Sub URL","QR کد":"QR code","انتخاب شده":"selected","کانفیگ‌های گروه ذخیره شدند ✓":"Group configurations saved ✓","خطا در ذخیره":"Save failed","کپی شد":"Copied","کپی شد ✓":"Copied ✓","ثانیه":"seconds","دقیقه":"minutes","ساعت":"hours","IP کپی شد":"IP copied","کپی IP":"Copy IP","بدون خطا":"No errors","سیستم پایدار":"System stable","رفرش شد":"Refreshed","UUID را وارد کنید":"Enter a UUID","اتصال:":"Connection:","✓ متصل - UUID معتبر":"✓ Connected - valid UUID","✗ خطا - UUID نامعتبر یا غیرفعال":"✗ Error - invalid or inactive UUID","دریافت":"Receive","- دسترسی رد شد":"- Access denied","ارسال:":"Send:","ساب گروه جدید":"New subscription group","در حال ساخت ۲۴ کانفیگ...":"Creating 24 configurations...","ساخت کانفیگ‌ها ناقص بود (":"Configuration creation was incomplete (","گروه ساب با ۲۴ کانفیگ ساخته شد":"Subscription group created with 24 configurations","خطا در ساخت ساب:":"Failed to create subscription:"});
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
function applyLanguage(lang){currentLang='fa';try{localStorage.setItem('finevpn-lang','fa');document.documentElement.lang='fa';document.documentElement.dir='rtl';}catch(e){}translatePage('fa');}
function toggleLanguage(){applyLanguage('fa');}
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

function updateDashboardClock(){
  const now=new Date();
  const date=document.getElementById('dash-date'),clock=document.getElementById('dash-clock');
  if(date)date.textContent=now.toLocaleDateString('fa-IR',{weekday:'short',day:'numeric',month:'long'});
  if(clock)clock.textContent=now.toLocaleTimeString('fa-IR',{hour:'2-digit',minute:'2-digit',second:'2-digit',hour12:true});
}
updateDashboardClock();setInterval(updateDashboardClock,1000);

function qsPreviewUpdate(){
  const el=document.getElementById('qs-summary');if(!el)return;
  const volume=Number(document.getElementById('qs-vol')?.value||0),days=Number(document.getElementById('qs-days')?.value||0),users=Number(document.getElementById('qs-ip')?.value||0),address=(document.getElementById('qs-address')?.value||'').trim(),port=Number(document.getElementById('qs-port')?.value||443);
  const parts=[];
  parts.push(volume>0?'حجم مشترک: '+toFa(volume)+' گیگابایت':'حجم نامحدود');
  parts.push(days>0?'اعتبار: '+toFa(days)+' روز':'اعتبار نامحدود');
  parts.push(users>0?'سقف اتصال: '+toFa(users)+' کاربر':'اتصال نامحدود');
  parts.push('مقصد: '+(address||'دامنهٔ پنل')+':'+toFa(port||443));
  el.textContent=parts.join('  •  ');
}
['qs-vol','qs-days','qs-ip','qs-address','qs-port'].forEach(id=>document.getElementById(id)?.addEventListener('input',qsPreviewUpdate));
qsPreviewUpdate();

function renderDashboardRecentLinks(links){
  const body=document.getElementById('dash-recent-links');if(!body)return;
  const rows=(Array.isArray(links)?links:[]).slice(0,5);
  if(!rows.length){body.innerHTML='<tr><td colspan="6" class="dash-table-empty">هنوز کانفیگی ساخته نشده است.</td></tr>';return;}
  const names={'vless-ws':'VLESS / WS','xhttp-packet-up':'VLESS / XHTTP','xhttp-stream-up':'VLESS / XHTTP'};
  body.innerHTML=rows.map((link,index)=>{
    const isActive=!!link.active&&!link.expired;
    const date=link.created_at?new Date(link.created_at).toLocaleDateString('fa-IR'):'—';
    const uuid=String(link.uuid||'');
    const safeLink=String(link.vless_link||'').replace(/\\/g,'\\\\').replace(/'/g,"\\'");
    return `<tr><td>${toFa(index+1)}</td><td><div class="dash-row-name">${esc(link.label||'کانفیگ بدون نام')}</div><div class="dash-row-sub">${esc(uuid.slice(0,12))}${uuid.length>12?'…':''}</div></td><td><span class="dash-proto">${esc(names[link.protocol]||link.protocol||'VLESS')}</span></td><td>${date}</td><td><span class="dash-state-pill ${isActive?'is-on':'is-off'}">${isActive?'فعال':'غیرفعال'}</span></td><td><button class="dash-table-action" title="کپی لینک" onclick="navigator.clipboard.writeText('${safeLink}').then(()=>toast('لینک کانفیگ کپی شد','ok'))"><i class="ti ti-copy"></i></button><button class="dash-table-action" title="نمایش QR" onclick="showQR('${safeLink}')"><i class="ti ti-qrcode"></i></button></td></tr>`;
  }).join('');
}

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
    const dashSubCount=document.getElementById('dash-sub-count');if(dashSubCount)dashSubCount.textContent=toFa(d.subs_count??0);
    const dashPortalCount=document.getElementById('dash-portal-count');if(dashPortalCount)dashPortalCount.textContent=toFa(d.subs_count??0);
    const dashHealth=document.getElementById('dash-health-label');if(dashHealth)dashHealth.textContent='فعال';
    const dashVol=document.getElementById('dash-volume-state');if(dashVol)dashVol.textContent=d.volume?.mounted&&d.volume?.writable?'پایدار':'موقت';
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
    renderDashboardRecentLinks(links);
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
    if(!links.length){renderDashboardRecentLinks([]);const grid0=document.getElementById('links-grid');
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
        <button class="btn btn-sm btn-g btn-icon" onclick="navigator.clipboard.writeText('${esc(l.sub_url)}').then(()=>toast('اشتراک کپی شد','ok'))" title="Sub URL"><i class="ti ti-rss"></i></button>
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
  const server_address=(document.getElementById('nl-address')?.value||'').trim();
  const ip_limit=Number(document.getElementById('nl-iplimit').value)||0;
  const speed_limit_value=Number(document.getElementById('nl-speed').value)||0;
  const speed_limit_unit=document.getElementById('nl-speed-unit').value;
  try{
    const category_id=document.getElementById('nl-cat')?document.getElementById('nl-cat').value||null:null;
    const r=await authF('/api/links',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({label,limit_value:val||0,limit_unit:unit,expires_days:exp||0,note,sub_id,category_id,protocol,fingerprint,alpn,port,server_address,ip_limit,speed_limit_value,speed_limit_unit})});
    if(!r.ok)throw new Error('failed');
    ['nl-label','nl-val','nl-exp','nl-note','nl-alpn','nl-address'].forEach(id=>document.getElementById(id).value='');
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
  document.getElementById('el-address').value=l.server_address||'';
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
  const server_address=(document.getElementById('el-address')?.value||'').trim();
  const ip_limit=Number(document.getElementById('el-iplimit').value)||0;
  const speed_limit_value=Number(document.getElementById('el-speed').value)||0;
  const speed_limit_unit=document.getElementById('el-speed-unit').value;
  const body={label,note,limit_value:val||0,limit_unit:unit,fingerprint,alpn,port,server_address,ip_limit,speed_limit_value,speed_limit_unit};
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
let fineQrObjectUrl = '';
let fineQrRequestId = 0;
async function showQR(link){
  const requestId=++fineQrRequestId;
  const modal=document.getElementById('qr-modal');
  const img=document.getElementById('qr-img');
  const status=document.getElementById('qr-status');
  if(!modal||!img||!status)return;
  if(fineQrObjectUrl){URL.revokeObjectURL(fineQrObjectUrl);fineQrObjectUrl='';}
  img.hidden=true;img.removeAttribute('src');
  status.hidden=false;status.className='qr-status is-loading';status.textContent='در حال ساخت کد QR…';
  modal.classList.add('open');
  try{
    const response=await fetch('/api/qr/render',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({data:String(link||'')})});
    if(!response.ok){let detail='ساخت QR ناموفق بود';try{const body=await response.json();detail=body.detail||detail;}catch(e){}throw new Error(detail);}
    const blob=await response.blob();
    if(requestId!==fineQrRequestId)return;
    if(!blob.type.includes('image/svg+xml'))throw new Error('پاسخ QR معتبر نیست');
    const objectUrl=URL.createObjectURL(blob);fineQrObjectUrl=objectUrl;
    img.onload=()=>{if(requestId!==fineQrRequestId)return;img.hidden=false;status.hidden=true;};
    img.onerror=()=>{if(requestId!==fineQrRequestId)return;status.hidden=false;status.className='qr-status is-error';status.textContent='تصویر QR بارگذاری نشد؛ دوباره تلاش کنید';img.hidden=true;};
    img.src=objectUrl;
  }catch(error){
    if(requestId!==fineQrRequestId)return;
    status.hidden=false;status.className='qr-status is-error';status.textContent=String(error?.message||'ساخت QR ناموفق بود');
  }
}
function closeQrModal(){
  const modal=document.getElementById('qr-modal');if(modal)modal.classList.remove('open');
  fineQrRequestId++;
  const img=document.getElementById('qr-img');if(img){img.onload=null;img.onerror=null;img.hidden=true;img.removeAttribute('src');}
  if(fineQrObjectUrl){URL.revokeObjectURL(fineQrObjectUrl);fineQrObjectUrl='';}
}
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
        <button class="btn btn-sm btn-g" onclick="openSubLinks('${esc(s.sub_id)}','${esc(s.name)}')"><i class="ti ti-settings-2"></i> مدیریت کانفیگ‌ها</button>
        <button class="btn btn-sm btn-d" onclick="deleteSub('${esc(s.sub_id)}')"><i class="ti ti-trash"></i> حذف گروه</button>
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
  const addr=(document.getElementById('ns-address')?.value||'').trim();const port=(document.getElementById('ns-port')?.value||'443').trim();
  parts.push('🌐 مقصد: <b>'+esc(addr||'نشانی پیش‌فرض پنل')+':'+esc(port)+'</b>');
  el.innerHTML=parts.join(' &nbsp;•&nbsp; ');
}
['ns-vol','ns-days','ns-iplimit','ns-address','ns-port'].forEach(id=>{
  const e=document.getElementById(id);if(e)e.addEventListener('input',qsUpdatePreview);
});

async function createSubQuick(){
  const name=document.getElementById('ns-name').value.trim()||'گروه سریع';
  const desc=document.getElementById('ns-desc').value.trim();
  const pw=document.getElementById('ns-pw').value;
  const volRaw=document.getElementById('ns-vol').value.trim();
  const daysRaw=document.getElementById('ns-days').value.trim();
  const ipRaw=document.getElementById('ns-iplimit').value.trim();
  const server_address=(document.getElementById('ns-address')?.value||'').trim();
  const portRaw=(document.getElementById('ns-port')?.value||'443').trim();
  const vol=volRaw===''?0:Number(volRaw);
  const days=daysRaw===''?0:Number(daysRaw);
  const ipLimit=ipRaw===''?0:Number(ipRaw);
  const port=portRaw===''?443:Number(portRaw);
  const totalLimitBytes=vol>0?Math.round(vol*1024*1024*1024):0;
  if(!Number.isFinite(vol)||!Number.isFinite(days)||!Number.isFinite(ipLimit)||
     vol<0||days<0||ipLimit<0||!Number.isFinite(totalLimitBytes)||
     !Number.isInteger(days)||!Number.isInteger(ipLimit)||!Number.isInteger(port)||port<1||port>65535){
    toast('مقادیر واردشده معتبر نیستند','err');return;
  }
  if(days>3650||ipLimit>100){toast('روزها حداکثر ۳۶۵۰ و IP حداکثر ۱۰۰ است','err');return;}
  if(totalLimitBytes>0&&totalLimitBytes<1024*1024){toast('حجم مشترک حداقل ۱ مگابایت باید باشد','err');return;}

  const btn=document.querySelector('#modal-create-sub .modal-v2-footer .btn-pur');
  if(btn?.dataset.busy==='1')return;
  const original=btn?btn.innerHTML:'';
  if(btn){btn.dataset.busy='1';btn.disabled=true;btn.innerHTML='<i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i> در حال ساخت گروه...';}
  try{
    const r=await authF('/api/subs/quick',{
      method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({name,desc,password:pw,total_limit_bytes:totalLimitBytes,days,ip_limit:ipLimit,speed_limit_bytes:0,server_address,port})
    });
    const data=await r.json().catch(()=>({}));
    if(!r.ok||!data.ok||Number(data.count)!==24)throw new Error(data.detail||data.message||'ساخت گروه کامل نشد');
    closeModal('modal-create-sub');
    ['ns-name','ns-desc','ns-pw','ns-address'].forEach(id=>{const el=document.getElementById(id);if(el)el.value='';});
    const portEl=document.getElementById('ns-port');if(portEl)portEl.value='443';
    toast('گروه و ۲۴ کانفیگ ساخته شد ✓','ok');
    // UI refresh is deliberately detached from the successful create response.
    void Promise.all([loadSubs(),loadLinks()]).catch(console.error);
    if(data.sub_url&&confirm('گروه ساخته شد. لینک اشتراک کپی شود؟')){
      try{await navigator.clipboard.writeText(data.sub_url);toast('لینک اشتراک کپی شد ✓','ok');}
      catch(e){prompt('لینک اشتراک',data.sub_url);}
    }
  }catch(e){toast(e.message||'خطا در ساخت گروه','err');}
  finally{if(btn){btn.dataset.busy='0';btn.disabled=false;btn.innerHTML=original||'<i class="ti ti-magic-wand"></i> ساخت گروه + ۲۴ کانفیگ';}}
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
          <button class="lrow-link-btn" onclick="event.stopPropagation();navigator.clipboard.writeText('${esc(surl)}').then(()=>toast('ساب کپی شد','ok'))" title="کپی پیوند اشتراک"><i class="ti ti-rss"></i><span>ساب</span></button>
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
    const rows=[['نسخه پنل','𝑭𝒊𝒏𝒆𝑽𝑷𝑵 𝒗₂.₀'],['آپتایم',String(d.uptime||'—')],['اتصالات فعال',toFa(d.active_connections||0)],['کل کانفیگ‌ها',toFa(d.links_count||0)],['گروه‌های ساب',toFa(d.subs_count||0)],['کل ترافیک',(d.total_traffic_mb||0).toFixed(2)+' MB']];
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
  const inp=document.getElementById(id);if(!inp||!btn)return;
  const icon=btn.querySelector('i');const reveal=inp.type==='password';
  inp.type=reveal?'text':'password';
  if(icon)icon.className='ti '+(reveal?'ti-eye-off':'ti-eye');
  btn.setAttribute('aria-pressed',String(reveal));
  btn.setAttribute('aria-label',reveal?'پنهان کردن رمز':'نمایش رمز');
}
function installFinePasswordToggles(root=document){
  root.querySelectorAll('input[type="password"]:not([data-fine-pw-ready])').forEach(inp=>{
    if(inp.closest('.login-password-wrap')||inp.classList.contains('lock-inp'))return;
    let wrap=inp.parentElement;
    if(!wrap||(!wrap.classList.contains('modal-v2-input-wrap')&&!wrap.classList.contains('fine-password-control'))){
      wrap=document.createElement('div');wrap.className='fine-password-control';
      inp.parentNode.insertBefore(wrap,inp);wrap.appendChild(inp);
    }else{wrap.classList.add('fine-password-control');}
    inp.dataset.finePwReady='1';inp.classList.add('fine-password-input');
    const btn=document.createElement('button');btn.type='button';btn.className='fine-pw-toggle';
    btn.setAttribute('aria-label','نمایش رمز');btn.setAttribute('aria-pressed','false');btn.title='نمایش / پنهان کردن رمز';
    btn.innerHTML='<i class="ti ti-eye" aria-hidden="true"></i>';
    btn.addEventListener('click',()=>{const reveal=inp.type==='password';inp.type=reveal?'text':'password';const icon=btn.querySelector('i');if(icon)icon.className='ti '+(reveal?'ti-eye-off':'ti-eye');btn.setAttribute('aria-pressed',String(reveal));btn.setAttribute('aria-label',reveal?'پنهان کردن رمز':'نمایش رمز');btn.title=reveal?'پنهان کردن رمز':'نمایش رمز';});
    wrap.appendChild(btn);
  });
}
installFinePasswordToggles();
const finePwObserver=new MutationObserver(records=>records.forEach(record=>record.addedNodes.forEach(node=>{if(node.nodeType===1){if(node.matches?.('input[type="password"]'))installFinePasswordToggles(node.parentNode||document);installFinePasswordToggles(node);}})));
finePwObserver.observe(document.body,{childList:true,subtree:true});

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
  const server_address=(document.getElementById('qs-address')?.value||'').trim();
  const port=Number(document.getElementById('qs-port')?.value||443);
  const totalLimitBytes=volGb>0?Math.round(volGb*1024*1024*1024):0;
  if(!Number.isFinite(volGb)||!Number.isFinite(days)||!Number.isFinite(ipLimit)||
     volGb<0||days<0||ipLimit<0||!Number.isInteger(days)||!Number.isInteger(ipLimit)||
     days>3650||ipLimit>100||!Number.isSafeInteger(totalLimitBytes)||!Number.isInteger(port)||port<1||port>65535){
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
      body:JSON.stringify({name,desc:'',password:'',total_limit_bytes:totalLimitBytes,days,ip_limit:ipLimit,speed_limit_bytes:0,server_address,port})
    });
    const data=await response.json().catch(()=>({}));
    if(!response.ok||!data.ok||Number(data.count)!==24){
      throw new Error(data.detail||data.message||'ساخت گروه کامل نشد؛ تغییری ناقص ثبت نشد');
    }
    linkInp.value=data.public_url||data.sub_url||'';
    resBox.style.display='block';
    toast('گروه ساب و ۲۴ کانفیگ '+(server_address?'با مقصد '+server_address+':'+port:'')+' ساخته شد ✓','ok');
    void Promise.all([loadLinks(),loadSubs()]).catch(console.error);
  }catch(err){
    toast('خطا در ساخت ساب: '+(err?.message||'خطای نامشخص'),'err');
  }finally{
    if(btn){btn.dataset.busy='';btn.disabled=false;btn.innerHTML=original||'<i class="ti ti-plus"></i> ساخت گروه ساب + ۲۴ کانفیگ با حجم مشترک';}
  }
}


// آزمایش مرحله‌ای نشانی‌های عمومی و خصوصی با پینگ واقعی ICMP
const ipScanState = {busy:false, results:[], filter:"all", total:0, completed:0};
function ipInputList(){return [...new Set((document.getElementById('ip-scan-input')?.value||'').split(/[\s,;]+/).map(x=>x.trim()).filter(Boolean))]}
function updateIpInputCount(){const list=ipInputList();const el=document.getElementById('ip-scan-count');if(el)el.textContent=toFa(list.length)+' آی‌پی وارد شده';const run=document.getElementById('ip-scan-run');if(run)run.disabled=ipScanState.busy||!list.length||list.length>500}
document.addEventListener('input',e=>{if(e.target?.id==='ip-scan-input')updateIpInputCount()});
function setIpProgress(done,total,label){const wrap=document.getElementById('ip-progress-wrap'),fill=document.getElementById('ip-progress-fill'),txt=document.getElementById('ip-progress-text'),pct=document.getElementById('ip-progress-pct');const percent=total?Math.min(100,Math.round(done/total*100)):0;if(wrap)wrap.classList.toggle('is-running',ipScanState.busy);if(fill)fill.style.width=percent+'%';if(txt)txt.textContent=label||('آزمایش '+toFa(done)+' از '+toFa(total));if(pct)pct.textContent=toFa(percent)+'٪';}
function setIpStats(){const rows=ipScanState.results,good=rows.filter(r=>r.status==='reachable').length,bad=rows.filter(r=>r.status==='unreachable').length,unknown=rows.length-good-bad;const vals={good,bad,unknown,total:rows.length,public:rows.filter(r=>r.scope==='public').length,private:rows.filter(r=>r.scope==='private').length};Object.entries(vals).forEach(([key,value])=>{const el=document.getElementById('ip-stat-'+key);if(el)el.textContent=toFa(value);});}
function clearIpScan(){ipScanState.filter='all';ipScanState.results=[];ipScanState.total=0;ipScanState.completed=0;document.querySelectorAll('[data-ip-filter]').forEach(b=>b.classList.toggle('active',b.dataset.ipFilter==='all'));const input=document.getElementById('ip-scan-input');if(input)input.value='';setIpStats();renderIpScanResults();const cap=document.getElementById('ip-results-caption');if(cap)cap.textContent='هنوز آزمایشی انجام نشده است';const state=document.getElementById('ip-scan-state');if(state)state.textContent='آماده آزمایش';setIpProgress(0,0,'آمادهٔ شروع آزمایش');updateIpInputCount();}
async function copyIpText(value){try{await navigator.clipboard.writeText(value);toast('کپی شد','ok')}catch(e){const t=document.createElement('textarea');t.value=value;document.body.appendChild(t);t.select();try{document.execCommand('copy');toast('کپی شد','ok')}catch(_){toast('کپی در این مرورگر ممکن نیست','err')}t.remove()}}
async function copyIpInput(){await copyIpText(ipInputList().join('\n'))}
function copyIpResults(kind){const rows=ipScanState.results.filter(r=>kind==='all'||(kind==='public'||kind==='private'?r.scope===kind:kind==='reachable'?r.status==='reachable':r.status!=='reachable'));if(!rows.length){toast('موردی برای کپی وجود ندارد','err');return}copyIpText(rows.map(r=>r.ip).join('\n'))}
function setIpFilter(filter){ipScanState.filter=['all','public','private','reachable','unreachable'].includes(filter)?filter:'all';document.querySelectorAll('[data-ip-filter]').forEach(b=>b.classList.toggle('active',b.dataset.ipFilter===ipScanState.filter));renderIpScanResults()}
function renderIpScanResults(){
  const host=document.getElementById('ip-results-list');if(!host)return;
  const statusText={reachable:'پاسخ دریافت شد',unreachable:'بدون پاسخ',timeout:'پایان مهلت',blocked:'اجرا نشد',unavailable:'ابزار پینگ موجود نیست'};
  const shown=ipScanState.results.filter(r=>ipScanState.filter==='all'||(ipScanState.filter==='public'||ipScanState.filter==='private'?r.scope===ipScanState.filter:ipScanState.filter==='reachable'?r.status==='reachable':r.status!=='reachable'));
  host.innerHTML=shown.map(r=>{const good=r.status==='reachable',bad=r.status==='unreachable',cls=good?'good':bad?'bad':'unknown',latency=Number.isFinite(Number(r.latency_ms))?toFa(r.latency_ms)+' میلی‌ثانیه':'—',scope=r.scope==='private'?'خصوصی':'عمومی';return `<div class="ip-result-row"><span class="ip-result-address">${esc(r.ip)}<small class="ip-result-scope ${r.scope==='private'?'private':'public'}">${scope}</small></span><span class="ip-result-status ${cls}">${statusText[r.status]||'نامشخص'}</span><span class="ip-result-latency">${latency}</span><button class="ip-result-copy-one" title="کپی آی‌پی" onclick="copyIpText('${esc(r.ip)}')"><i class="ti ti-copy"></i></button></div>`;}).join('')||'<div class="empty"><p>در این دسته نتیجه‌ای وجود ندارد.</p></div>';
}
async function runIpScan(){
  const ips=ipInputList();if(!ips.length){toast('ابتدا آی‌پی وارد کنید','err');return}if(ips.length>500){toast('حداکثر ۵۰۰ آی‌پی مجاز است','err');return}if(ipScanState.busy)return;
  ipScanState.busy=true;ipScanState.results=[];ipScanState.total=ips.length;ipScanState.completed=0;setIpStats();renderIpScanResults();
  const btn=document.getElementById('ip-scan-run'),state=document.getElementById('ip-scan-state'),cap=document.getElementById('ip-results-caption');
  if(btn){btn.disabled=true;btn.innerHTML='<i class="ti ti-loader-2 animate-spin"></i> در حال آزمایش...'}if(state)state.textContent='آزمایش در حال اجرا';if(cap)cap.textContent='در حال پینگ '+toFa(ips.length)+' نشانی';setIpProgress(0,ips.length,'اتصال و شروع آزمایش...');
  try{
    const response=await authF('/api/tools/ip-check/stream',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({ips})});
    if(!response.ok){const err=await response.json().catch(()=>({}));throw new Error(err.detail||'شروع آزمایش ممکن نشد')}
    if(!response.body)throw new Error('مرورگر از دریافت مرحله‌ای نتیجه پشتیبانی نمی‌کند');
    const reader=response.body.getReader(),decoder=new TextDecoder();let buffer='',finished=false;
    const handleLine=(line)=>{if(!line.trim())return;let event;try{event=JSON.parse(line)}catch(_){return}
      if(event.type==='start'){ipScanState.total=Number(event.total)||ips.length;setIpProgress(0,ipScanState.total,'آزمایش '+toFa(ipScanState.total)+' نشانی آغاز شد');}
      else if(event.type==='result'&&event.result){ipScanState.results.push(event.result);ipScanState.completed=ipScanState.results.length;setIpStats();setIpProgress(ipScanState.completed,ipScanState.total,'بررسی '+toFa(ipScanState.completed)+' از '+toFa(ipScanState.total));renderIpScanResults();}
      else if(event.type==='done'){finished=true;ipScanState.completed=Number(event.tested)||ipScanState.completed;setIpStats();setIpProgress(ipScanState.completed,ipScanState.total,'آزمایش کامل شد');if(cap)cap.textContent='بررسی '+toFa(event.tested||0)+' نشانی · پینگ واقعی ICMP';if(state)state.textContent='آزمایش پایان یافت';if(event.note)toast(event.note,'ok');}
    };
    while(true){const {value,done}=await reader.read();if(done)break;buffer+=decoder.decode(value,{stream:true});const lines=buffer.split('\n');buffer=lines.pop()||'';for(const line of lines)handleLine(line);}
    buffer+=decoder.decode();if(buffer.trim())handleLine(buffer);
    if(!finished)throw new Error('جریان نتیجه پیش از پایان قطع شد');
  }catch(e){toast(e.message||'آزمایش انجام نشد','err');if(state)state.textContent='آزمایش ناموفق';setIpProgress(ipScanState.completed,ipScanState.total,'آزمایش متوقف شد');}
  finally{ipScanState.busy=false;const wrap=document.getElementById('ip-progress-wrap');if(wrap)wrap.classList.remove('is-running');if(btn){btn.disabled=false;btn.innerHTML='<i class="ti ti-player-play"></i> شروع آزمایش'}updateIpInputCount();}
}
updateIpInputCount();

</script>
</body></html>"""


def _get_public_page_html_v1(uuid_key: str) -> str:
    """قالب اصلی درگاه اشتراک؛ لایه گرافیکی نسخه دوم پس از تولید افزوده می‌شود."""
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="UTF-8"><link rel="icon" type="image/png" href="https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png"><link rel="apple-touch-icon" href="https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png"><meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
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
body::after{{content:"F";position:fixed;inset:0;z-index:1;pointer-events:none;display:grid;place-items:center;color:rgba(104,195,255,.025);font-size:min(48vw,520px);font-weight:950;mix-blend-mode:screen}}
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

/* FineVPN visual refresh 1.0.0 */
:root{{--bg:#070b18;--bg2:#0b1426;--bg3:#14243b;--card:rgba(16,29,50,.9);--card-b:rgba(100,185,255,.17);--card-bh:rgba(50,202,245,.4);--accent:#27c7f5;--accent2:#67dcff;--accent-d:rgba(39,199,245,.11);--green:#25d6a2;--purple:#a78bfa;--t1:#edf6ff;--t2:#a5bad3;--t3:#7189a8;--shadow:0 16px 44px rgba(0,0,0,.3)}}
html,body{{background:#070b18!important}}
.bg-fx{{background:radial-gradient(ellipse 70% 45% at 50% -8%,rgba(39,199,245,.16),transparent 62%),radial-gradient(ellipse at 0% 95%,rgba(130,93,245,.09),transparent 35%),#070b18!important}}
.grid-fx{{background-image:linear-gradient(rgba(67,183,242,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(67,183,242,.035) 1px,transparent 1px)!important}}
.sub-info,.stat-card,.config-card,.app-card,.card,.section-card,.diagnostic-card{{background:linear-gradient(145deg,rgba(17,32,55,.92),rgba(10,20,37,.94))!important;border:1px solid rgba(105,181,239,.17)!important;border-radius:20px!important;box-shadow:0 14px 38px rgba(0,0,0,.23),inset 0 1px rgba(255,255,255,.03)!important;backdrop-filter:blur(16px)}}
.brand-img{{border-radius:14px!important;box-shadow:0 0 22px rgba(39,199,245,.25)!important}}
.brand-name{{letter-spacing:.02em}}
.icon-btn,button,.btn,.btn-primary,.btn-p,.action-btn{{border-radius:12px!important;transition:transform .16s ease,box-shadow .16s ease,filter .16s ease}}
button:hover:not(:disabled),.btn:hover:not(:disabled),.btn-primary:hover:not(:disabled),.btn-p:hover:not(:disabled),.action-btn:hover:not(:disabled){{filter:brightness(1.08);transform:translateY(-1px)}}
input,select,textarea{{border-radius:12px!important;border-color:rgba(120,175,225,.2)!important;background:rgba(4,12,25,.58)!important;color:var(--t1)!important;max-width:100%}}
input:focus,select:focus,textarea:focus{{border-color:#27c7f5!important;box-shadow:0 0 0 3px rgba(39,199,245,.12)!important;outline:none}}
.sub-sub-box{{background:rgba(39,199,245,.09)!important;border-color:rgba(105,181,239,.2)!important;border-radius:14px!important}}
a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible{{outline:2px solid #57d8ff;outline-offset:3px}}
@media(max-width:600px){{.wrap{{padding:17px 12px 42px}}.sub-info{{padding:19px 16px!important;border-radius:17px!important}}.sub-name{{font-size:20px}}.stats-bar{{gap:7px}}.icon-btn{{width:38px;height:38px}}}}
@media(max-width:380px){{.top{{align-items:flex-start;flex-wrap:wrap}}.top-actions{{margin-right:auto}}.stats-bar{{grid-template-columns:1fr 1fr}}}}
@media(prefers-reduced-motion:reduce){{*,*::before,*::after{{scroll-behavior:auto!important;animation-duration:.01ms!important;transition-duration:.01ms!important}}}}

/* FineVPN 1.0.0 — public portal visual system v2 */
:root{{--bg:#060b18!important;--bg2:#0a1428!important;--bg3:#10213b!important;--card:rgba(13,27,49,.90)!important;--card-b:rgba(94,177,239,.20)!important;--card-bh:rgba(51,207,255,.48)!important;--accent:#32c9f4!important;--accent2:#86e7ff!important;--accent-d:rgba(50,201,244,.13)!important;--green:#35ddb2!important;--green-bg:rgba(53,221,178,.12)!important;--green-t:#76f0d0!important;--purple:#9c8aff!important;--purple-bg:rgba(156,138,255,.13)!important;--purple-t:#c5baff!important;--red:#ff718c!important;--red-bg:rgba(255,113,140,.12)!important;--red-t:#ff9caf!important;--amber:#ffc76b!important;--amber-bg:rgba(255,199,107,.12)!important;--amber-t:#ffda9a!important;--t1:#f2f8ff!important;--t2:#adc3de!important;--t3:#718aa9!important;--shadow:0 18px 48px rgba(0,0,0,.30)!important}}
html,body{{--min-width:320px!important;max-width:100%!important;overflow-x:hidden!important;background:#060b18!important;color:#f2f8ff!important;font-family:'Vazirmatn',system-ui,sans-serif!important}}
body{{background:radial-gradient(ellipse 62% 38% at 8% 0%,rgba(34,159,235,.14),transparent 70%),radial-gradient(ellipse 48% 36% at 94% 94%,rgba(119,87,255,.10),transparent 72%),#060b18!important;padding-bottom:env(safe-area-inset-bottom)}}
.bg-fx{{background:radial-gradient(ellipse 70% 45% at 50% -8%,rgba(39,177,240,.12),transparent 62%),#060b18!important}}
.grid-fx{{background-image:linear-gradient(rgba(67,183,242,.025) 1px,transparent 1px),linear-gradient(90deg,rgba(67,183,242,.025) 1px,transparent 1px)!important;background-size:52px 52px!important}}
.wrap{{width:min(100% - 36px,1120px)!important;max-width:1120px!important;padding:28px 0 60px!important;margin-inline:auto!important}}
.top{{display:flex!important;align-items:center!important;justify-content:space-between!important;gap:18px!important;padding:16px 18px!important;margin:0 0 18px!important;border:1px solid rgba(95,181,240,.20)!important;border-radius:22px!important;background:linear-gradient(145deg,rgba(15,34,60,.92),rgba(7,18,36,.96))!important;box-shadow:0 16px 38px rgba(0,0,0,.25),inset 0 1px rgba(255,255,255,.06)!important;backdrop-filter:blur(18px)!important;-webkit-backdrop-filter:blur(18px)!important}}
.brand{{display:flex!important;align-items:center!important;gap:13px!important;min-width:0!important}}
.brand-img{{width:54px!important;height:54px!important;border-radius:17px!important;border:1px solid rgba(100,213,255,.44)!important;box-shadow:0 0 0 4px rgba(45,177,236,.07),0 0 26px rgba(47,185,245,.20)!important;background:linear-gradient(145deg,rgba(40,174,235,.17),rgba(121,94,245,.18))!important;overflow:hidden!important}}
.brand-img img{{width:100%!important;height:100%!important;object-fit:cover!important}}
.brand-name{{font-size:19px!important;font-weight:950!important;color:#f4f9ff!important;letter-spacing:.025em!important}}
.brand-sub{{font-size:10px!important;color:#85a7c9!important;letter-spacing:.035em!important;margin-top:3px!important}}
.top-actions{{display:flex!important;align-items:center!important;justify-content:flex-end!important;gap:8px!important;flex-wrap:wrap!important;min-width:0!important}}
.public-action,.diag-open{{min-height:42px!important;padding:9px 13px!important;border-radius:12px!important;border:1px solid rgba(98,190,242,.28)!important;background:rgba(36,139,205,.11)!important;color:#c8eeff!important;font-family:inherit!important;font-size:11px!important;font-weight:850!important;text-decoration:none!important;display:inline-flex!important;align-items:center!important;justify-content:center!important;gap:7px!important;white-space:nowrap!important;box-shadow:inset 0 1px rgba(255,255,255,.12),0 7px 18px rgba(0,0,0,.17)!important}}
.public-action:hover,.diag-open:hover{{background:rgba(46,166,225,.18)!important;border-color:rgba(105,205,255,.46)!important}}
.diag-open{{width:42px!important;height:42px!important;padding:0!important;font-size:17px!important}}
.sub-info,.stat-card,.portal-metric,.speed-panel,.download-section,.brand-contact,.cfg-card{{background:linear-gradient(145deg,rgba(15,34,60,.94),rgba(7,18,36,.97))!important;border:1px solid rgba(97,181,239,.20)!important;border-radius:22px!important;box-shadow:0 16px 40px rgba(0,0,0,.25),inset 0 1px rgba(255,255,255,.055)!important;backdrop-filter:blur(16px)!important;-webkit-backdrop-filter:blur(16px)!important}}
.sub-info{{padding:24px!important;margin-bottom:16px!important}}
.sub-eyebrow{{color:#72ddff!important;font-size:10px!important;font-weight:900!important;letter-spacing:.10em!important}}
.sub-name{{font-size:clamp(21px,3vw,28px)!important;font-weight:950!important;line-height:1.35!important;color:#f5f9ff!important;margin-bottom:6px!important}}
.sub-desc{{color:#a5bdd7!important;font-size:12px!important;line-height:1.9!important}}
.sub-meta-row{{color:#7997b8!important;font-size:10px!important}}
.sub-sub-box{{display:grid!important;grid-template-columns:minmax(0,1fr) auto auto!important;align-items:center!important;gap:9px!important;padding:10px!important;background:rgba(37,166,221,.08)!important;border:1px solid rgba(90,184,235,.22)!important;border-radius:15px!important;min-width:0!important}}
.sub-sub-url{{display:block!important;min-width:0!important;width:100%!important;direction:ltr!important;text-align:left!important;white-space:nowrap!important;overflow:hidden!important;text-overflow:ellipsis!important;word-break:normal!important;overflow-wrap:normal!important;font-family:ui-monospace,Consolas,monospace!important;font-size:11px!important;color:#88e4ff!important;line-height:1.7!important}}
.btn{{font-family:inherit!important;font-size:11px!important;font-weight:850!important;min-height:40px!important;padding:9px 13px!important;border-radius:12px!important;display:inline-flex!important;align-items:center!important;justify-content:center!important;gap:7px!important;white-space:normal!important;line-height:1.45!important;touch-action:manipulation!important}}
.btn-p{{background:linear-gradient(120deg,#31c9f3,#397de9 58%,#6d69ef)!important;color:#041629!important;border:1px solid rgba(154,229,255,.48)!important;box-shadow:0 8px 22px rgba(35,153,235,.20),inset 0 1px rgba(255,255,255,.38)!important}}
.btn-g{{background:rgba(44,190,238,.12)!important;color:#b4ecff!important;border:1px solid rgba(81,193,244,.28)!important}}
.btn-pur{{background:rgba(144,121,255,.13)!important;color:#cec5ff!important;border:1px solid rgba(158,137,255,.30)!important}}
.copy-all-bar{{display:flex!important;align-items:center!important;gap:14px!important;flex-wrap:nowrap!important;padding:17px 19px!important;border-radius:18px!important;background:linear-gradient(110deg,rgba(32,149,218,.95),rgba(75,101,224,.96) 58%,rgba(121,91,231,.95))!important;border:1px solid rgba(158,224,255,.34)!important;box-shadow:0 12px 28px rgba(40,117,224,.20)!important}}
.copy-all-text{{flex:1!important;min-width:0!important}}
.copy-all-title{{font-size:14px!important;font-weight:950!important;color:#fff!important}}
.copy-all-sub{{font-size:10px!important;color:rgba(255,255,255,.82)!important;line-height:1.7!important}}
.copy-all-btn{{min-height:44px!important;padding:10px 17px!important;border-radius:13px!important;background:#f1f8ff!important;color:#174d83!important;font-size:11.5px!important;font-weight:950!important;white-space:nowrap!important}}
.stats-bar{{gap:10px!important;margin-bottom:16px!important}}
.stat-card{{padding:15px 16px!important;border-radius:16px!important}}
.stat-label{{color:#80a0c1!important;font-size:9px!important}}
.stat-val{{color:#f2f8ff!important;font-size:22px!important;font-weight:950!important}}
.portal-metrics{{display:grid!important;grid-template-columns:1.15fr 1fr 1fr!important;gap:12px!important;margin:0 0 16px!important}}
.portal-metric{{padding:17px!important;min-width:0!important;border-radius:19px!important}}
.portal-metric-head{{font-size:10px!important;color:#cce3f9!important;font-weight:900!important}}
.metric-tag{{border-radius:999px!important;background:rgba(65,166,221,.12)!important;border:1px solid rgba(85,176,232,.20)!important;color:#8adfff!important;padding:4px 8px!important;font-size:8px!important}}
.ring-gauge{{filter:drop-shadow(0 5px 14px rgba(46,175,238,.13))!important}}
.ring-core strong{{font-size:21px!important;color:#f4f9ff!important}}
.metric-main-value{{color:#f4f9ff!important;font-size:19px!important;font-weight:950!important}}
.metric-hint{{color:#8faaca!important;line-height:1.7!important}}
.metric-remaining{{color:#7eebcb!important;font-weight:900!important}}
.metric-split{{gap:7px!important}}
.metric-split span{{background:rgba(52,171,219,.09)!important;border-color:rgba(93,185,234,.16)!important;color:#addbf2!important;border-radius:9px!important}}
.metric-live-number{{color:#75efce!important;text-shadow:0 0 20px rgba(53,221,178,.16)!important}}
.speed-panel{{padding:18px!important;margin:16px 0!important}}
.speed-chip{{border-radius:13px!important;background:rgba(4,15,31,.65)!important;border:1px solid rgba(94,180,237,.20)!important;padding:12px!important;min-width:0!important}}
.speed-chip label{{color:#86a6c8!important}}
.speed-chip strong{{color:#e9f7ff!important;overflow-wrap:anywhere!important}}
#traffic-chart{{display:block!important;width:100%!important;max-width:100%!important;height:140px!important;margin-top:10px!important}}
.cfg-title{{margin:18px 0 12px!important;color:#c3d8ee!important;font-size:12px!important;font-weight:950!important}}
.cfg-title i{{color:#5cd7ff!important}}
.cfg-grid{{display:grid!important;grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:13px!important}}
.cfg-card{{min-width:0!important;border-radius:18px!important;overflow:hidden!important}}
.cfg-top{{padding:16px 17px 13px!important}}
.cfg-head{{align-items:flex-start!important;gap:10px!important}}
.cfg-label{{font-size:14px!important;font-weight:900!important;line-height:1.6!important;overflow-wrap:anywhere!important}}
.cfg-status-stack{{gap:6px!important;display:flex!important;flex-wrap:wrap!important;justify-content:flex-end!important}}
.cfg-status{{font-size:9px!important;font-weight:850!important;padding:5px 9px!important;border-radius:999px!important;white-space:nowrap!important}}
.cfg-status.live.online{{background:rgba(53,221,178,.12)!important;color:#80f2d1!important;border:1px solid rgba(53,221,178,.24)!important}}
.cfg-status.live.offline{{background:rgba(131,151,177,.12)!important;color:#aabbd0!important;border:1px solid rgba(131,151,177,.18)!important}}
.cfg-usage{{margin-top:12px!important}}
.ubar{{height:6px!important;background:rgba(107,151,190,.14)!important;border-radius:999px!important}}
.cfg-tear{{border-color:rgba(98,180,234,.16)!important}}
.cfg-tear:before,.cfg-tear:after{{border-color:rgba(98,180,234,.18)!important}}
.cfg-bottom{{padding:14px 17px 16px!important}}
.cfg-link-toggle{{min-height:42px!important;border:1px solid rgba(95,180,237,.23)!important;background:rgba(42,142,198,.08)!important;color:#b8e6fa!important;border-radius:12px!important}}
.cfg-vless{{direction:ltr!important;text-align:left!important;overflow-wrap:anywhere!important;word-break:break-word!important;max-height:112px!important;font-size:10px!important;line-height:1.8!important;border-radius:11px!important;background:rgba(3,12,26,.70)!important;border-color:rgba(97,180,236,.17)!important;color:#83e4ff!important}}
.cfg-vless.is-sub{{color:#c7baff!important}}
.cfg-actions{{display:grid!important;grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:8px!important;margin-top:12px!important}}
.cfg-actions .btn{{width:100%!important;min-width:0!important;min-height:42px!important;padding:8px!important;justify-content:center!important;font-size:10px!important}}
.expired-banner{{border-radius:13px!important}}
.brand-contact{{margin-top:18px!important;padding:20px!important;display:flex!important;align-items:center!important;justify-content:space-between!important;gap:16px!important}}
.brand-contact-logo{{border:1px solid rgba(91,214,255,.45)!important;box-shadow:0 0 18px rgba(44,188,245,.18)!important;border-radius:15px!important}}
.brand-contact-title{{color:#f2f8ff!important;font-weight:950!important}}
.brand-contact-provider,.brand-contact-signature{{color:#8faaca!important}}
.fine-tg-link{{min-height:42px!important;padding:10px 14px!important;border-radius:12px!important;background:rgba(36,149,215,.12)!important;border:1px solid rgba(94,188,239,.25)!important;color:#b7e9ff!important;font-weight:850!important}}
.download-section{{margin-top:16px!important;padding:19px!important}}
.download-title{{font-size:14px!important;font-weight:950!important;color:#eff7ff!important}}
.download-subtitle{{font-size:10px!important;color:#8faaca!important}}
.download-grid{{grid-template-columns:repeat(auto-fit,minmax(min(100%,210px),1fr))!important;gap:9px!important}}
.download-card{{min-width:0!important;padding:11px 12px!important;border-radius:13px!important;background:rgba(5,18,35,.64)!important;border:1px solid rgba(95,181,239,.17)!important}}
.download-app-name{{font-size:11px!important;color:#f2f8ff!important}}
.download-app-platform{{font-size:9px!important;color:#8faaca!important;overflow-wrap:anywhere!important}}
.toast{{max-width:calc(100vw - 24px)!important;white-space:normal!important;line-height:1.6!important;text-align:center!important}}
@media(min-width:1200px){{.cfg-grid{{grid-template-columns:repeat(2,minmax(0,1fr))!important}}.portal-metrics{{grid-template-columns:1.2fr 1fr 1fr!important}}}}
@media(max-width:820px){{.wrap{{width:calc(100% - 28px)!important;padding:17px 0 calc(34px + env(safe-area-inset-bottom))!important}}.top{{padding:14px!important;border-radius:18px!important}}.portal-metrics{{grid-template-columns:repeat(2,minmax(0,1fr))!important}}.portal-metric:first-child{{grid-column:1/-1}}.cfg-grid{{grid-template-columns:1fr!important}}}}
@media(max-width:600px){{
  .wrap{{width:calc(100% - 22px)!important;padding-top:12px!important}}
  .top{{display:grid!important;grid-template-columns:minmax(0,1fr)!important;gap:12px!important;padding:13px!important;margin-bottom:13px!important}}
  .brand{{gap:11px!important}}
  .brand-img{{width:48px!important;height:48px!important;border-radius:15px!important}}
  .brand-name{{font-size:17px!important}}
  .top-actions{{display:grid!important;grid-template-columns:42px repeat(3,minmax(0,1fr))!important;gap:7px!important;width:100%!important}}
  .public-action,.diag-open{{min-width:0!important;width:100%!important;min-height:40px!important;padding:7px 5px!important;font-size:9px!important;gap:4px!important}}
  .diag-open{{width:42px!important;padding:0!important}}
  .sub-info{{padding:16px!important;border-radius:18px!important;margin-bottom:12px!important}}
  .sub-name{{font-size:21px!important}}
  .sub-sub-box{{grid-template-columns:minmax(0,1fr) minmax(0,1fr)!important;gap:7px!important;padding:9px!important}}
  .sub-sub-url{{grid-column:1/-1!important;padding:6px 4px!important;font-size:10px!important}}
  .sub-sub-box .btn{{width:100%!important;min-width:0!important;min-height:40px!important;padding:8px 6px!important;font-size:9.5px!important}}
  .copy-all-bar{{display:grid!important;grid-template-columns:minmax(0,1fr)!important;gap:10px!important;padding:15px!important;border-radius:16px!important}}
  .copy-all-title{{font-size:13px!important}}
  .copy-all-btn{{width:100%!important;justify-content:center!important;min-height:43px!important}}
  .portal-metrics{{grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:8px!important}}
  .portal-metric:first-child{{grid-column:1/-1!important}}
  .portal-metric{{padding:13px!important;border-radius:16px!important}}
  .portal-metric-head{{font-size:9px!important;flex-wrap:wrap!important}}
  .metric-flex{{gap:10px!important}}
  .ring-gauge{{width:88px!important;height:88px!important;flex:0 0 88px!important}}
  .ring-core strong{{font-size:18px!important}}
  .metric-main-value{{font-size:17px!important}}
  .metric-hint,.metric-remaining{{font-size:9px!important}}
  .metric-split span{{font-size:8.5px!important}}
  .speed-panel{{padding:14px!important;border-radius:17px!important}}
  .speed-grid{{grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:7px!important}}
  .speed-chip{{padding:10px!important}}
  .speed-chip strong{{font-size:12px!important}}
  .cfg-title{{margin-top:16px!important}}
  .cfg-grid{{grid-template-columns:minmax(0,1fr)!important;gap:11px!important}}
  .cfg-card{{border-radius:16px!important}}
  .cfg-head{{display:flex!important;flex-direction:column!important;align-items:stretch!important}}
  .cfg-status-stack{{justify-content:flex-start!important}}
  .cfg-actions{{grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:7px!important}}
  .cfg-actions .btn{{font-size:9.5px!important;min-height:42px!important}}
  .brand-contact{{display:grid!important;grid-template-columns:minmax(0,1fr)!important;padding:15px!important;border-radius:17px!important}}
  .brand-contact-links{{width:100%!important}}
  .fine-tg-link{{width:100%!important;justify-content:center!important}}
  .download-section{{padding:15px!important;border-radius:17px!important}}
  .download-grid{{grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:7px!important}}
  .download-card{{padding:9px!important;gap:7px!important}}
  .download-app-icon{{width:30px!important;height:30px!important;flex-basis:30px!important}}
  .download-app-platform{{font-size:8px!important}}
  .diag-overlay{{padding:10px!important}}
}}
@media(max-width:380px){{.wrap{{width:calc(100% - 16px)!important}}.top-actions{{grid-template-columns:38px repeat(3,minmax(0,1fr))!important;gap:5px!important}}.public-action{{font-size:8.5px!important}}.portal-metrics{{grid-template-columns:1fr!important}}.portal-metric:first-child{{grid-column:auto!important}}.metric-flex{{align-items:center!important}}.ring-gauge{{width:78px!important;height:78px!important;flex-basis:78px!important}}.download-grid{{grid-template-columns:1fr!important}}.cfg-actions .btn{{font-size:9px!important;padding:7px 5px!important}}}}
@media(prefers-reduced-motion:reduce){{*,*::before,*::after{{animation:none!important;transition:none!important;scroll-behavior:auto!important}}}}


/* FineVPN v1.0.0 — final public portal neon glass layer */
:root{{--bg:#050b18!important;--bg2:#09162b!important;--bg3:#102541!important;--card:rgba(13,31,56,.9)!important;--card-b:rgba(85,185,245,.24)!important;--card-bh:rgba(67,214,255,.48)!important;--accent:#31c9f4!important;--accent2:#83e7ff!important;--accent-d:rgba(49,201,244,.13)!important;--green:#2dd4a5!important;--green-bg:rgba(45,212,165,.13)!important;--green-t:#7af0ce!important;--purple:#a78bfa!important;--purple-bg:rgba(167,139,250,.14)!important;--red:#fb7185!important;--red-bg:rgba(251,113,133,.13)!important;--red-t:#ffabb9!important;--amber:#f5bd68!important;--amber-bg:rgba(245,189,104,.13)!important;--amber-t:#ffdda5!important;--t1:#f2f8ff!important;--t2:#b8cde3!important;--t3:#7897b8!important;--shadow:0 18px 48px rgba(0,0,0,.32)!important}}
html,body{{background:#050b18!important;color:#f2f8ff!important;font-family:'Vazirmatn',system-ui,sans-serif!important;min-width:320px!important}}
body{{background-image:radial-gradient(ellipse 65% 38% at 12% 0%,rgba(36,168,239,.16),transparent 70%),radial-gradient(ellipse 46% 40% at 96% 95%,rgba(124,91,255,.12),transparent 72%),linear-gradient(145deg,#050b18,#07152b 56%,#080d20)!important;background-attachment:fixed!important}}
.bg-fx{{background:radial-gradient(ellipse 68% 45% at 48% -10%,rgba(39,169,239,.13),transparent 65%)!important}}
.grid-fx{{background-image:linear-gradient(rgba(82,177,235,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(82,177,235,.035) 1px,transparent 1px)!important;background-size:42px 42px!important}}
.wrap{{width:min(100% - 32px,880px)!important;padding:24px 0 calc(48px + env(safe-area-inset-bottom))!important}}
.top,.sub-info,.stat-card,.portal-metric,.cfg-card,.speed-panel,.download-section,.brand-contact,.copy-all-bar,.qr-box,.lock-card{{background:linear-gradient(145deg,rgba(17,42,72,.92),rgba(7,18,38,.97))!important;border:1px solid rgba(94,184,241,.23)!important;border-radius:21px!important;box-shadow:0 18px 46px rgba(0,0,0,.28),inset 0 1px rgba(255,255,255,.065)!important;backdrop-filter:blur(18px)!important;-webkit-backdrop-filter:blur(18px)!important;color:#f2f8ff!important}}
.top{{padding:18px 20px!important;gap:14px!important;align-items:center!important}}
.brand-name{{font-size:clamp(17px,2.2vw,22px)!important;font-weight:950!important;color:#f4faff!important;letter-spacing:.025em!important;text-shadow:0 0 22px rgba(57,194,245,.17)}}
.brand-sub{{color:#91b0d0!important;font-size:10px!important}}
.brand-img{{width:54px!important;height:54px!important;border-radius:16px!important;border:1px solid rgba(97,205,255,.48)!important;box-shadow:0 0 0 4px rgba(50,182,239,.07),0 0 24px rgba(43,184,246,.2)!important}}
.top-actions{{gap:8px!important;flex-wrap:wrap!important}}
.public-action,.diag-open{{min-height:43px!important;padding:9px 14px!important;border-radius:13px!important;background:linear-gradient(145deg,rgba(35,147,208,.17),rgba(108,91,220,.14))!important;border:1px solid rgba(89,189,240,.29)!important;color:#bceeff!important;font-family:inherit!important;font-weight:850!important;box-shadow:inset 0 1px rgba(255,255,255,.13),0 7px 20px rgba(0,0,0,.18)!important}}
.public-action:hover,.diag-open:hover{{filter:brightness(1.12)!important;border-color:rgba(98,215,255,.55)!important}}
.sub-info{{padding:clamp(18px,3vw,27px)!important}}
.sub-eyebrow{{color:#67dcff!important;font-weight:900!important;letter-spacing:.07em!important}}
.sub-name{{font-size:clamp(22px,4vw,29px)!important;font-weight:950!important;color:#f4f9ff!important;line-height:1.4!important}}
.sub-desc,.sub-meta-row{{color:#9cb5d1!important;line-height:1.8!important}}
.sub-sub-box{{display:grid!important;grid-template-columns:minmax(0,1fr) auto auto!important;align-items:center!important;gap:9px!important;background:rgba(24,114,166,.12)!important;border:1px solid rgba(84,184,236,.25)!important;border-radius:15px!important;padding:11px!important;min-width:0!important}}
.sub-sub-url{{min-width:0!important;max-width:100%!important;overflow:hidden!important;text-overflow:ellipsis!important;white-space:nowrap!important;direction:ltr!important;text-align:left!important;color:#91e7ff!important;font-size:11px!important}}
.btn,.icon-btn,.copy-all-btn,.lock-btn,.diag-btn,.fine-tg-link{{font-family:inherit!important;font-weight:850!important;border-radius:12px!important;min-height:40px!important;touch-action:manipulation!important;-webkit-tap-highlight-color:transparent!important}}
.btn{{padding:8px 13px!important;font-size:11px!important;line-height:1.45!important;display:inline-flex!important;align-items:center!important;justify-content:center!important;gap:7px!important;white-space:normal!important;min-width:0!important;max-width:100%!important;box-shadow:inset 0 1px rgba(255,255,255,.13),0 7px 18px rgba(0,0,0,.2)!important}}
.btn-p,.copy-all-btn,.lock-btn{{background:linear-gradient(120deg,#34cef5,#347fe9 58%,#7167ed)!important;color:#05182b!important;border:1px solid rgba(164,235,255,.56)!important;box-shadow:0 9px 24px rgba(36,142,234,.25),inset 0 1px rgba(255,255,255,.5)!important}}
.btn-g,.btn-o{{background:rgba(38,187,232,.12)!important;color:#b9efff!important;border:1px solid rgba(84,197,241,.29)!important}}
.stat-card,.portal-metric{{padding:17px!important;border-radius:17px!important}}
.stat-label,.portal-metric-head{{color:#92b2d0!important;font-weight:800!important}}
.stat-val,.metric-main-value{{color:#f2f9ff!important;font-weight:950!important}}
.cfg-card{{overflow:hidden!important;border-radius:19px!important}}
.cfg-top{{padding:17px 18px!important}}
.cfg-label{{font-size:14px!important;font-weight:950!important;color:#eff8ff!important}}
.cfg-status-stack{{gap:7px!important}}
.cfg-status{{font-weight:900!important;padding:5px 9px!important;border-radius:999px!important}}
.cfg-vless{{direction:ltr!important;text-align:left!important;overflow-wrap:anywhere!important;word-break:break-word!important;max-height:130px!important;background:rgba(2,11,25,.8)!important;border:1px solid rgba(85,178,232,.2)!important;color:#91e6ff!important;border-radius:12px!important}}
.cfg-actions{{display:grid!important;grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:8px!important}}
.cfg-actions .btn{{width:100%!important;min-width:0!important;min-height:43px!important;padding:8px 7px!important;font-size:10.5px!important}}
.copy-all-bar{{background:linear-gradient(120deg,rgba(34,157,225,.9),rgba(75,96,221,.92))!important;border:1px solid rgba(151,221,255,.4)!important}}
.copy-all-title{{font-size:14px!important;font-weight:950!important}}
.copy-all-btn{{border-radius:12px!important;min-height:46px!important;padding:10px 16px!important}}
.speed-panel,.download-section,.brand-contact{{padding:20px!important}}
.download-card{{background:rgba(4,17,36,.62)!important;border:1px solid rgba(94,184,241,.2)!important;border-radius:14px!important}}
.lock-card{{max-width:440px!important;overflow:hidden!important}}
.lock-banner{{background:linear-gradient(145deg,rgba(42,172,230,.16),rgba(127,93,239,.10))!important}}
.lock-inp{{direction:ltr!important;text-align:center!important;padding-left:54px!important;padding-right:44px!important;background:rgba(3,13,29,.78)!important;color:#f4f9ff!important;border:1px solid rgba(99,181,233,.25)!important}}
.lock-eye{{width:38px!important;height:38px!important;left:7px!important;display:grid!important;place-items:center!important;border-radius:10px!important;background:rgba(42,166,219,.13)!important;color:#a7eaff!important}}
.qr-modal{{z-index:1300!important;padding:16px!important;background:rgba(1,7,18,.86)!important;backdrop-filter:blur(13px)!important;-webkit-backdrop-filter:blur(13px)!important}}
.qr-box{{width:min(100%,390px)!important;padding:22px!important;border-radius:24px!important;border-color:rgba(77,204,255,.32)!important;box-shadow:0 28px 90px rgba(0,0,0,.58),0 0 38px rgba(39,177,242,.1)!important}}
.qr-title{{font-size:15px!important;font-weight:950!important;color:#f2f8ff!important}}
.qr-img{{display:grid!important;place-items:center!important;min-height:220px!important;padding:10px!important;border-radius:16px!important;background:rgba(255,255,255,.035)!important;border:1px solid rgba(98,184,236,.18)!important}}
.qr-img img{{width:min(100%,310px)!important;aspect-ratio:1/1!important;height:auto!important;object-fit:contain!important;display:block!important;padding:10px!important;background:#fff!important;border-radius:12px!important;image-rendering:pixelated!important}}
.qr-img img[hidden]{{display:none!important}}
.qr-status{{width:100%;min-height:180px;display:grid;place-items:center;padding:20px;text-align:center;color:#9bcbe5;font-size:12px;line-height:1.8}}
.qr-status.is-loading:before{{content:'';width:30px;height:30px;border:3px solid rgba(82,192,241,.2);border-top-color:#51d8ff;border-radius:50%;animation:fineQrSpin .8s linear infinite;margin-bottom:8px}}
.qr-status.is-error{{color:#ffb1bf;background:rgba(245,91,123,.08);border-radius:12px}}
.qr-status[hidden]{{display:none!important}}
@keyframes fineQrSpin{{to{{transform:rotate(360deg)}}}}
.toast{{max-width:calc(100vw - 24px)!important;white-space:normal!important;text-align:center!important;line-height:1.6!important}}
@media(max-width:720px){{.wrap{{width:calc(100% - 24px)!important;padding:13px 0 calc(36px + env(safe-area-inset-bottom))!important}}.top{{display:grid!important;grid-template-columns:minmax(0,1fr)!important;gap:12px!important;padding:14px!important}}.top-actions{{display:grid!important;grid-template-columns:repeat(3,minmax(0,1fr))!important;gap:7px!important;width:100%!important}}.public-action,.diag-open{{width:100%!important;min-width:0!important;min-height:42px!important;padding:7px 5px!important;font-size:9.5px!important}}.sub-info{{padding:17px!important}}.portal-metrics{{grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:9px!important}}.cfg-grid{{grid-template-columns:minmax(0,1fr)!important}}.cfg-head{{gap:10px!important}}.cfg-status-stack{{justify-content:flex-start!important}}.cfg-actions{{grid-template-columns:repeat(2,minmax(0,1fr))!important}}.sub-sub-box{{grid-template-columns:minmax(0,1fr) auto auto!important}}.copy-all-bar{{display:grid!important;grid-template-columns:minmax(0,1fr)!important;gap:10px!important}}.copy-all-btn{{width:100%!important;justify-content:center!important}}}}
@media(max-width:420px){{.wrap{{width:calc(100% - 18px)!important}}.top-actions{{grid-template-columns:repeat(2,minmax(0,1fr))!important}}.sub-sub-box{{grid-template-columns:minmax(0,1fr) minmax(0,1fr)!important}}.sub-sub-url{{grid-column:1/-1!important}}.sub-sub-box .btn{{width:100%!important}}.portal-metrics{{grid-template-columns:1fr!important}}.portal-metric:first-child{{grid-column:auto!important}}.cfg-actions .btn{{font-size:9.5px!important;padding:7px 5px!important}}.qr-box{{padding:16px!important}}}}
@media(prefers-reduced-motion:reduce){{.qr-status.is-loading:before{{animation:none!important}}}}


/* FineVPN v1.0 — public portal glass identity */
:root{{--accent:#64d7fb;--accent2:#a3eaff;--card-b:rgba(108,190,240,.20);--card-bh:rgba(106,212,255,.44)}}
body{{background:radial-gradient(ellipse 65% 38% at 10% 0%,rgba(50,160,234,.18),transparent 70%),radial-gradient(ellipse 50% 42% at 94% 95%,rgba(127,91,242,.14),transparent 70%),linear-gradient(145deg,#050b18,#07172d 58%,#0a1021)!important}}
.bg-fx{{background:radial-gradient(ellipse 70% 45% at 50% -8%,rgba(74,177,238,.13),transparent 62%),transparent!important}}
.wrap{{width:min(100% - 32px,1160px)!important}}
.top{{border:1px solid rgba(104,184,237,.18)!important;border-radius:20px!important;background:linear-gradient(135deg,rgba(14,37,66,.88),rgba(7,18,38,.91))!important;box-shadow:0 16px 44px rgba(0,0,0,.25),inset 0 1px rgba(255,255,255,.06)!important;backdrop-filter:blur(20px)!important;-webkit-backdrop-filter:blur(20px)!important}}
.brand-img{{width:54px!important;height:54px!important;border-radius:16px!important;border:1px solid rgba(119,215,255,.4)!important;box-shadow:0 0 0 5px rgba(67,166,232,.06),0 9px 26px rgba(33,131,211,.18)!important;overflow:hidden!important}}
.fine-logo-mark{{width:100%;height:100%;display:block;filter:drop-shadow(0 4px 9px rgba(67,184,242,.18))}}
.brand-name{{font-weight:950!important;color:#eff9ff!important;text-shadow:0 4px 24px rgba(91,198,255,.16)}}
.brand-sub{{color:#8fb6d7!important;letter-spacing:.055em!important}}
.public-action,.diag-open{{border:1px solid rgba(105,187,237,.23)!important;background:rgba(52,151,210,.11)!important;color:#c7efff!important;border-radius:12px!important;min-height:39px!important;transition:transform .16s,filter .16s!important}}
.public-action:hover,.diag-open:hover{{filter:brightness(1.12);transform:translateY(-1px)}}
.portal-metric,.stat-card,.cfg-card,.speed-panel,.download-section,.sub-info,.diag-window,.lock-card{{border-color:rgba(106,186,238,.2)!important;box-shadow:0 16px 42px rgba(0,0,0,.23),inset 0 1px rgba(255,255,255,.05)!important;backdrop-filter:blur(16px)!important;-webkit-backdrop-filter:blur(16px)!important}}
.portal-metric,.stat-card,.cfg-card,.speed-panel,.download-section,.sub-info{{background:linear-gradient(145deg,rgba(15,38,67,.90),rgba(7,18,37,.96))!important;border-radius:19px!important}}
.portal-metric{{transition:transform .2s,border-color .2s!important}}
.portal-metric:hover{{transform:translateY(-2px);border-color:rgba(107,206,250,.38)!important}}
.brand-contact{{border-color:rgba(104,184,237,.19)!important;background:linear-gradient(145deg,rgba(15,38,67,.84),rgba(7,18,38,.88))!important;border-radius:20px!important}}
.brand-contact-logo{{display:grid!important;place-items:center!important;overflow:hidden!important;background:linear-gradient(145deg,rgba(56,174,235,.18),rgba(134,105,247,.16))!important;border:1px solid rgba(119,215,255,.38)!important}}
.brand-contact-title{{color:#eff8ff!important}}
.fine-tg-link{{border-color:rgba(90,189,239,.24)!important;background:rgba(36,131,214,.10)!important;color:#c7ecff!important;border-radius:12px!important}}
button:focus-visible,a:focus-visible,input:focus-visible{{outline:2px solid #82e3ff!important;outline-offset:3px!important}}
@media(max-width:720px){{.wrap{{width:calc(100% - 22px)!important;padding-top:10px!important}}.top{{padding:13px!important;border-radius:16px!important}}.top-actions{{width:100%;flex-wrap:wrap}}.public-action{{flex:1 1 auto;justify-content:center}}.portal-metric{{padding:12px!important}}}}
@media(prefers-reduced-motion:reduce){{*,*:before,*:after{{animation:none!important;transition:none!important}}}}

</style>
</head>
<body>
<div class="bg-fx"></div><div class="grid-fx"></div>
<div class="toast" id="toast"></div>
<div class="diag-overlay" id="diag-overlay" onclick="if(event.target===this)closePortalDiagnostics()">
  <div class="diag-window" role="dialog" aria-modal="true" aria-label="عیب‌یابی FineVPN">
    <div class="diag-head"><span class="diag-title">فاین‌وی‌پی‌ان // پایش فنی</span><button type="button" onclick="closePortalDiagnostics()" aria-label="بستن">×</button></div>
    <div class="diag-body" id="diag-results"><div class="diag-line"><span>آماده‌سازی تست‌ها</span><span class="diag-state na">اجرا نشده</span></div></div>
    <div class="diag-foot"><button class="diag-btn" onclick="runPortalDiagnostics()">↻ اجرای دوباره</button><button class="diag-btn" onclick="copyPortalDiagnosticReport()">کپی گزارش</button></div>
  </div>
</div>
<div class="qr-modal" id="qr-modal" onclick="closeQrModal()">
  <div class="qr-box" onclick="event.stopPropagation()">
    <div class="qr-title" id="qr-label">کد QR</div>
    <div class="qr-img"><div class="qr-status" id="qr-status" aria-live="polite">در حال آماده‌سازی QR…</div><img id="qr-img" src="" alt="کد QR فاین وی‌پی‌ان" hidden></div>
    <button class="btn btn-g" style="width:100%;justify-content:center" onclick="closeQrModal()"><i class="ti ti-x"></i> بستن</button>
  </div>
</div>
<div class="wrap">
  <div class="top">
    <div class="brand">
      <div class="brand-img"><img class="fine-logo-mark" src="https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png" alt="لوگوی اصلی FineVPN" loading="eager" decoding="async" style="width:100%;height:100%;object-fit:contain;display:block"></div>
      <div><div class="brand-name">𝑭𝒊𝒏𝒆𝑽𝑷𝑵</div><div class="brand-sub">درگاه اشتراک امن · 𝒗₂.₀</div></div>
    </div>
    <div class="top-actions">
      <button class="diag-open" type="button" onclick="openPortalDiagnostics()" title="پایش فنی"><i class="ti ti-terminal-2"></i><span>پایش فنی</span></button>
      <button class="public-action public-theme-toggle" type="button" id="public-theme-toggle" onclick="toggleTheme()" aria-label="تغییر حالت روشن و تاریک"><i class="ti ti-sun" id="public-theme-icon"></i><span id="public-theme-label">حالت روشن</span></button>
      <button class="public-action" onclick="refreshSubscription()" id="refresh-sub-btn"><i class="ti ti-refresh"></i><span data-public-i18n="تازه‌سازی">تازه‌سازی</span></button>
      <a class="public-action public-download-jump" href="#download-clients"><i class="ti ti-download"></i><span>دانلود برنامه</span></a>
    </div>
  </div>
  <div id="root">
    <div class="empty-state"><i class="ti ti-loader-2" style="animation:spin 1s linear infinite"></i>در حال بارگذاری...</div>
  </div>
  <div class="brand-contact public-brand-contact"><div class="brand-contact-links"><a class="fine-tg-link" href="https://t.me/sadiq_AFG1" target="_blank" rel="noopener noreferrer" aria-label="پشتیبانی تلگرام"><i class="ti ti-brand-telegram"></i><span>پشتیبانی</span></a></div></div>
  <section class="download-section" id="download-clients" aria-label="دانلود برنامه‌های سازگار">
    <div class="download-head">
      <div><div class="download-title">دانلود کلاینت‌های سازگار</div><div class="download-subtitle">نسخهٔ رسمی متناسب با دستگاهت را انتخاب کن</div></div>
      <span class="download-head-icon"><i class="ti ti-device-mobile-down"></i></span>
    </div>
    <div class="download-grid">
      <a class="download-card" href="https://github.com/2dust/v2rayNG/releases/latest" target="_blank" rel="noopener noreferrer"><span class="download-app-icon"><i class="ti ti-brand-android"></i></span><span class="download-app-copy"><span class="download-app-name">v2rayNG</span><span class="download-app-platform">اندروید · گیت‌هاب</span></span><i class="ti ti-external-link download-open"></i></a>
      <a class="download-card" href="https://play.google.com/store/apps/details?id=app.hiddify.com" target="_blank" rel="noopener noreferrer"><span class="download-app-icon"><i class="ti ti-brand-android"></i></span><span class="download-app-copy"><span class="download-app-name">Hiddify</span><span class="download-app-platform">اندروید · گوگل‌پلی</span></span><i class="ti ti-external-link download-open"></i></a>
      <a class="download-card" href="https://play.google.com/store/apps/details?id=dev.hexasoftware.v2box" target="_blank" rel="noopener noreferrer"><span class="download-app-icon"><i class="ti ti-brand-android"></i></span><span class="download-app-copy"><span class="download-app-name">V2Box</span><span class="download-app-platform">اندروید · گوگل‌پلی</span></span><i class="ti ti-external-link download-open"></i></a>
      <a class="download-card" href="https://apps.apple.com/us/app/v2box-v2ray-client/id6446814690" target="_blank" rel="noopener noreferrer"><span class="download-app-icon"><i class="ti ti-brand-apple"></i></span><span class="download-app-copy"><span class="download-app-name">V2Box</span><span class="download-app-platform">آیفون · اپ‌استور</span></span><i class="ti ti-external-link download-open"></i></a>
      <a class="download-card" href="https://github.com/hiddify/hiddify-app/releases/latest" target="_blank" rel="noopener noreferrer"><span class="download-app-icon"><i class="ti ti-brand-windows"></i></span><span class="download-app-copy"><span class="download-app-name">Hiddify</span><span class="download-app-platform">ویندوز و رایانه · گیت‌هاب</span></span><i class="ti ti-external-link download-open"></i></a>
    </div>
  </section>
</div>
<script>
const UUID_KEY='{uuid_key}';
let savedPw='';

let publicLang='fa';
let publicTheme='dark';
try{{publicTheme=localStorage.getItem('finevpn-theme')==='light'?'light':'dark';}}catch(e){{}}
function applyTheme(theme){{if(theme==='light'||theme==='dark')publicTheme=theme;document.documentElement.setAttribute('data-theme',publicTheme);try{{localStorage.setItem('finevpn-theme',publicTheme)}}catch(e){{}}const icon=document.getElementById('public-theme-icon'),label=document.getElementById('public-theme-label'),button=document.getElementById('public-theme-toggle');if(icon)icon.className='ti '+(publicTheme==='dark'?'ti-sun':'ti-moon');if(label)label.textContent=publicTheme==='dark'?'حالت روشن':'حالت تاریک';if(button)button.setAttribute('aria-pressed',String(publicTheme==='light'));}}
function toggleTheme(){{applyTheme(publicTheme==='dark'?'light':'dark');}}
applyTheme();
const PUBLIC_I18N={{'تازه‌سازی':'Refresh','در حال بارگذاری...':'Loading...','گروه دسترسی':'Access Group','آخرین بروزرسانی:':'Last updated:','کپی لینک ساب':'Copy subscription link','QR کل':'Group QR','کپی همه‌ی کانفیگ‌ها':'Copy all configurations','تمام لینک‌های فعال این گروه را یک‌جا کپی کن':'Copy all active links at once','کپی همه':'Copy all','کانفیگ‌های فعال':'Active configs','اتصالات زنده':'Live connections','آنلاین':'Online','آفلاین':'Offline','کانفیگ آنلاین':'Online configs','کانفیگ آفلاین':'Offline configs','کانفیگ‌های مجاز':'Allowed configs','دارای اتصال واقعی در همین لحظه':'Connected right now','بدون نشست فعال':'No live session','مجموع آپلود و دانلود':'Upload + download total','سهم از حجم مشترک گروه':'Share of group quota','بدون محدودیت حجمی':'No traffic limit','کل مصرف':'Total usage','سهمیه و اعتبار گروه':'Group quota and validity','دانلود برنامه‌های سازگار':'Download compatible apps','برای واردکردن لینک اشتراک، برنامهٔ متناسب با دستگاه خود را از منبع رسمی دریافت کنید.':'Download a compatible client from its official store to import your subscription.','لینک کانفیگ':'Config link','لینک ساب کلاینت':'Client subscription link','کپی لینک':'Copy link','کپی ساب کلاینت':'Copy client subscription','نمایش لینک کانفیگ':'Show config link','پنهان کردن لینک':'Hide config link','ترافیک دانلود':'Download traffic','ترافیک آپلود':'Upload traffic','سرعت دانلود':'Download speed','سرعت آپلود':'Upload speed','آمار زندهٔ انتقال داده':'Live traffic statistics','حجم دانلود':'Download volume','حجم آپلود':'Upload volume','کانفیگ‌ها':'Configurations','عدد':'items','اتصال':'connection','مصرف شده':'used','سهمیه:':'Quota:','سهمیه: <b>نامحدود</b>':'Quota: <b>Unlimited</b>','اعتبار:':'Validity:','نامحدود':'Unlimited','روز مانده':'days left','اعتبار نامحدود':'Unlimited validity','محدودیت حجمی فعال نیست':'No traffic limit is active','مصرف‌شده:':'Used:','از':'of','QR کانفیگ':'Configuration QR','QR ساب':'Subscription QR','لینک کپی شد ✓':'Link copied ✓','لینک ساب کلاینت کپی شد ✓':'Client subscription copied ✓','همه‌ی':'all','کانفیگی برای کپی نیست':'No configurations to copy','داده تازه شد':'Data refreshed','تازه‌سازی ناموفق بود':'Refresh failed','خطا در بارگذاری':'Loading failed','آنلاین':'Online','فعال':'Active','غیرفعال':'Inactive','مصرف‌شده:':'Used:','نرخ انتقال از اختلاف شمارنده‌های واقعی در دو نمونهٔ پیاپی محاسبه می‌شود؛ نمونهٔ نخست فقط نقطهٔ مبناست.':'Speed is calculated from real counter deltas between requests; it may be zero on first load.'}};
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
function togglePublicLanguage(){{publicLang='fa';translatePublic('fa');applyTheme()}}
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

let fineQrObjectUrl = '';
let fineQrRequestId = 0;
async function showQR(label,link){{
  const requestId=++fineQrRequestId;
  const modal=document.getElementById('qr-modal');
  const img=document.getElementById('qr-img');
  const status=document.getElementById('qr-status');
  if(!modal||!img||!status)return;
  document.getElementById('qr-label').textContent=label||'QR Code';
  if(fineQrObjectUrl){{URL.revokeObjectURL(fineQrObjectUrl);fineQrObjectUrl='';}}
  img.hidden=true;img.removeAttribute('src');
  status.hidden=false;status.className='qr-status is-loading';status.textContent='در حال ساخت کد QR…';
  modal.classList.add('open');
  try{{
    const response=await fetch('/api/qr/render',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{data:String(link||'')}})}});
    if(!response.ok){{let detail='ساخت QR ناموفق بود';try{{const body=await response.json();detail=body.detail||detail;}}catch(e){{}}throw new Error(detail);}}
    const blob=await response.blob();
    if(requestId!==fineQrRequestId)return;
    if(!blob.type.includes('image/svg+xml'))throw new Error('پاسخ QR معتبر نیست');
    const objectUrl=URL.createObjectURL(blob);fineQrObjectUrl=objectUrl;
    img.onload=()=>{{if(requestId!==fineQrRequestId)return;img.hidden=false;status.hidden=true;}};
    img.onerror=()=>{{if(requestId!==fineQrRequestId)return;status.hidden=false;status.className='qr-status is-error';status.textContent='تصویر QR بارگذاری نشد؛ دوباره تلاش کنید';img.hidden=true;}};
    img.src=objectUrl;
  }}catch(error){{
    if(requestId!==fineQrRequestId)return;
    status.hidden=false;status.className='qr-status is-error';status.textContent=String(error?.message||'ساخت QR ناموفق بود');
  }}
}}
function closeQrModal(){{
  const modal=document.getElementById('qr-modal');if(modal)modal.classList.remove('open');
  fineQrRequestId++;
  const img=document.getElementById('qr-img');if(img){{img.onload=null;img.onerror=null;img.hidden=true;img.removeAttribute('src');}}
  if(fineQrObjectUrl){{URL.revokeObjectURL(fineQrObjectUrl);fineQrObjectUrl='';}}
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
        <div class="portal-metric-head"><span><i class="ti ti-chart-donut-3"></i> مصرف سهمیهٔ مشترک</span><span class="metric-tag">مصرف زنده</span></div>
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
        <div class="portal-metric-head"><span><i class="ti ti-clock-hour-4"></i> اعتبار باقی‌مانده</span><span class="metric-tag">اعتبار زمانی</span></div>
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
        <div class="portal-metric-head"><span><i class="ti ti-radar"></i> اتصال‌های زنده</span><span class="metric-tag">اتصال‌های زنده</span></div>
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
      <div class="stat-sub">نرخ انتقال از اختلاف شمارنده‌های واقعی در دو نمونهٔ پیاپی محاسبه می‌شود؛ نمونهٔ نخست فقط نقطهٔ مبناست.</div>
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
  box.innerHTML=setDiagLine('دسترسی اشتراک','busy','در حال بررسی')+setDiagLine('سلامت سرویس پنل','busy','در حال بررسی')+setDiagLine('اعتبار زمانی','busy','در حال بررسی')+setDiagLine('سهمیهٔ حجمی','busy','در حال بررسی')+setDiagLine('دی‌ان‌اس مقصد / تونل','na','قابل سنجش از مرورگر نیست');
  const report=[];let subOk=false,healthOk=false,freshData=null,subMs=null,healthMs=null;
  try{{
    const query=savedPw?'?pw='+encodeURIComponent(savedPw):'';
    const t=performance.now(),r=await fetch('/api/public/sub/'+UUID_KEY+query,{{cache:'no-store'}});subMs=Math.round(performance.now()-t);const d=await r.json();
    subOk=r.ok&&!d.locked;report.push('دسترسی اشتراک: '+(subOk?'موفق':'ناموفق')+' · '+subMs+' میلی‌ثانیه');
    if(subOk){{freshData=d;window.latestPortalData=d;}}
  }}catch(e){{report.push('دسترسی اشتراک: ناموفق · '+String(e));}}
  try{{const t=performance.now(),r=await fetch('/health',{{cache:'no-store'}}),j=await r.json();healthMs=Math.round(performance.now()-t);healthOk=r.ok&&j.status==='ok';report.push('سلامت سرویس پنل: '+(healthOk?'پایدار':'ناموفق')+' · '+healthMs+' میلی‌ثانیه');}}
  catch(e){{report.push('سلامت سرویس پنل: ناموفق · '+String(e));}}
  const d=freshData;
  const expiryOk=d?(!d.expires_at||(!d.expired&&Number(d.remaining_seconds)>0)):null;
  const quotaOk=d?(d.remaining_bytes===null||Number(d.remaining_bytes)>0):null;
  const expiryText=expiryOk===null?'بررسی نشد':d.expires_at?(expiryOk?'معتبر':'پایان‌یافته'):'بدون محدودیت زمانی';
  const quotaText=quotaOk===null?'بررسی نشد':d.remaining_bytes===null?'بدون محدودیت حجمی':(quotaOk?'دارای سهمیه':'سهمیه تمام شده');
  report.push('اعتبار زمانی: '+expiryText);report.push('سهمیهٔ حجمی: '+quotaText);
  box.innerHTML=setDiagLine('دسترسی اشتراک',subOk?'ok':'err',subOk?('موفق · '+toFa(subMs)+' میلی‌ثانیه'):'ناموفق')+
    setDiagLine('سلامت سرویس پنل',healthOk?'ok':'err',healthOk?('پایدار · '+toFa(healthMs)+' میلی‌ثانیه'):'ناموفق')+
    setDiagLine('اعتبار زمانی',expiryOk===null?'na':expiryOk?'ok':'err',expiryText)+
    setDiagLine('سهمیهٔ حجمی',quotaOk===null?'na':quotaOk?'ok':'err',quotaText)+
    setDiagLine('دی‌ان‌اس مقصد / تونل','na','از مرورگر قابل سنجش نیست')+
    setDiagLine('زمان پاسخ پنل',healthMs===null?'na':healthOk?'ok':'err',healthMs===null?'اندازه‌گیری نشد':toFa(healthMs)+' میلی‌ثانیه');
  report.push('دی‌ان‌اس و سلامت تونل: از داخل مرورگر این صفحه قابل اندازه‌گیری نیست.');
  portalDiagnosticReport='گزارش پایش فنی فاین‌وی‌پی‌ان\\n'+report.join('\\n');
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


def get_public_page_html(uuid_key: str) -> str:
    html = _get_public_page_html_v1(uuid_key)
    html = html.replace("𝒗1.0", "𝒗₂.₀")
    html = html.replace("SECURE SUBSCRIPTION PORTAL · 𝒗₂.₀", "درگاه اشتراک امن · 𝒗₂.₀")
    html = html.replace('      <button class="public-action" onclick="togglePublicLanguage()"><i class="ti ti-language"></i><span id="public-lang-label">English</span></button>\n', "")
    html = html.replace("let publicLang='fa';try{{publicLang=localStorage.getItem('finevpn-lang')||'fa'}}catch(e){{}}", "let publicLang='fa';")
    html = html.replace("function togglePublicLanguage(){{publicLang=publicLang==='fa'?'en':'fa';try{{localStorage.setItem('finevpn-lang',publicLang)}}catch(e){{}}translatePublic(publicLang);applyTheme()}}", "function togglePublicLanguage(){{publicLang='fa';translatePublic('fa');applyTheme()}}")
    html = html.replace("</style>", '\n/* FineVPN 𝒗₂.₀ — public subscription blue glass portal */\n:root{--bg:#030917!important;--bg2:#06152d!important;--bg3:#0d2b4e!important;--card:rgba(9,30,58,.78)!important;--card-b:rgba(94,183,247,.23)!important;--accent:#59c9ff!important;--accent2:#a0eaff!important;--t1:#f2f9ff!important;--t2:#b7d1e9!important;--t3:#7e9fbe!important;--green:#16d5a0!important;--green-t:#6af1ca!important;--red:#ff6c92!important;--purple:#9ea8ff!important}\nhtml,body{background:#030917!important;color:#f2f9ff!important}\nbody{position:relative;isolation:isolate;background:radial-gradient(ellipse 72% 46% at 50% -7%,rgba(28,113,219,.24),transparent 68%),linear-gradient(145deg,#030817,#071832 60%,#050b20)!important}\nbody:before,body:after{content:"";position:fixed;z-index:0;pointer-events:none;border-radius:50%;border:1px solid rgba(100,194,255,.10);box-shadow:0 0 0 26px rgba(74,160,235,.018),0 0 0 60px rgba(74,160,235,.012)}\nbody:before{width:min(70vw,680px);height:min(70vw,680px);top:-34vw;right:-19vw}body:after{width:min(50vw,500px);height:min(50vw,500px);bottom:-28vw;left:-16vw;border-color:rgba(142,151,255,.12);background-image:url("https://i.ibb.co/23qKBjNv/copilot-image-1793563203439.png");background-position:center;background-size:72% 72%;background-repeat:no-repeat;opacity:.07;filter:grayscale(1)}\n.bg-fx{background:radial-gradient(ellipse 70% 45% at 50% -8%,rgba(27,110,223,.20),transparent 62%),transparent!important}.grid-fx{background-image:linear-gradient(rgba(97,177,248,.025) 1px,transparent 1px),linear-gradient(90deg,rgba(97,177,248,.025) 1px,transparent 1px)!important}\n.wrap{z-index:2!important}.top{padding:13px 15px!important;border:1px solid rgba(102,189,248,.18)!important;border-radius:18px!important;background:rgba(6,22,48,.58)!important;backdrop-filter:blur(20px)!important;box-shadow:0 14px 40px rgba(0,0,0,.18)!important}\n.brand-img{border:1px solid rgba(111,213,255,.42)!important;background:rgba(52,147,225,.12)!important;box-shadow:0 0 0 5px rgba(65,155,226,.06),0 0 26px rgba(54,154,233,.20)!important}.brand-img img{object-fit:contain!important}.brand-name{color:#f4faff!important}.brand-sub{color:#9dc6e7!important;letter-spacing:0!important}\n.portal-metric,.stat-card,.cfg-card,.speed-panel,.download-section,.sub-info,.diag-window,.lock-card,.brand-contact{background:linear-gradient(145deg,rgba(13,39,72,.84),rgba(5,17,39,.91))!important;border:1px solid rgba(96,186,249,.22)!important;border-radius:20px!important;box-shadow:0 16px 46px rgba(0,0,0,.25),inset 0 1px rgba(255,255,255,.05)!important;backdrop-filter:blur(20px)!important;-webkit-backdrop-filter:blur(20px)!important}\n.public-action,.diag-open,.diag-btn{border:1px solid rgba(105,194,249,.27)!important;background:rgba(50,144,219,.13)!important;color:#d4f1ff!important;border-radius:12px!important}.public-action:hover,.diag-open:hover{filter:brightness(1.12);transform:translateY(-1px)}\n.cfg-card{transition:transform .2s,border-color .2s!important}.cfg-card:hover{transform:translateY(-2px);border-color:rgba(106,210,255,.42)!important}\n.fine-tg-link{border-color:rgba(95,187,247,.25)!important;background:rgba(42,137,217,.13)!important;color:#d1efff!important}\n' + "\n</style>", 1)
    html = html.replace('</style>', '\n/* Public portal: matching persisted light mode */\nhtml[data-theme="light"] body{background:radial-gradient(ellipse 72% 46% at 50% -7%,rgba(69,157,230,.16),transparent 68%),linear-gradient(145deg,#edf6ff,#e6f2ff 60%,#f7fbff)!important;color:#152e49!important}\nhtml[data-theme="light"] .top,html[data-theme="light"] .portal-metric,html[data-theme="light"] .stat-card,html[data-theme="light"] .cfg-card,html[data-theme="light"] .speed-panel,html[data-theme="light"] .download-section,html[data-theme="light"] .sub-info,html[data-theme="light"] .diag-window,html[data-theme="light"] .lock-card,html[data-theme="light"] .brand-contact{background:linear-gradient(145deg,rgba(255,255,255,.96),rgba(235,246,255,.94))!important;border-color:rgba(45,126,193,.18)!important;color:#173a5d!important;box-shadow:0 14px 38px rgba(26,80,127,.1)!important}\nhtml[data-theme="light"] .brand-name,html[data-theme="light"] .metric-main-value,html[data-theme="light"] .dash-welcome,html[data-theme="light"] .cfg-name{color:#183a5b!important}\nhtml[data-theme="light"] .public-action,html[data-theme="light"] .diag-open,html[data-theme="light"] .diag-btn{background:rgba(46,139,213,.1)!important;color:#1d5c8c!important;border-color:rgba(46,139,213,.22)!important}\n' + '</style>', 1)
    portal_refine_css = r"""
/* Public portal 3D glass refinement */
.brand-img,.brand-contact-logo{border-radius:50%!important;overflow:hidden!important}
.brand-img{width:58px!important;height:58px!important;padding:5px!important;background:linear-gradient(145deg,rgba(69,185,244,.2),rgba(100,104,229,.14))!important;box-shadow:0 0 0 6px rgba(61,160,232,.055),0 0 35px rgba(49,167,245,.25),inset 0 1px rgba(255,255,255,.2)!important}
.brand-img img{object-fit:contain!important;filter:drop-shadow(0 0 10px rgba(96,210,255,.42))}
.top-actions{gap:8px!important;align-items:stretch!important}
.public-action,.diag-open{min-width:44px!important;min-height:43px!important;display:inline-flex!important;align-items:center!important;justify-content:center!important;gap:7px!important;padding:9px 12px!important;border-radius:14px!important;box-shadow:0 8px 20px rgba(0,0,0,.17),inset 0 1px rgba(255,255,255,.14)!important}
.public-theme-toggle{background:linear-gradient(145deg,rgba(63,154,225,.18),rgba(112,101,230,.17))!important}
.public-brand-contact{justify-content:center!important;padding:10px!important;margin-top:18px!important;background:transparent!important;border:0!important;box-shadow:none!important}
.public-brand-contact .brand-contact-links{width:100%!important;justify-content:center!important}
.public-brand-contact .fine-tg-link{min-width:170px!important;justify-content:center!important;padding:12px 20px!important;border-radius:15px!important;font-size:12px!important;box-shadow:0 9px 24px rgba(18,105,184,.14),inset 0 1px rgba(255,255,255,.13)!important}
.diag-window{border:1px solid rgba(96,194,255,.38)!important;background:linear-gradient(145deg,rgba(7,28,57,.97),rgba(3,12,31,.985))!important;box-shadow:0 30px 100px rgba(0,0,0,.58),0 0 42px rgba(36,157,240,.15),inset 0 1px rgba(255,255,255,.1)!important;border-radius:23px!important;overflow:hidden!important;position:relative!important}
.diag-window:before{content:"";position:absolute;inset:0;pointer-events:none;background:repeating-linear-gradient(180deg,rgba(93,190,255,.025) 0 1px,transparent 1px 5px);opacity:.45;mix-blend-mode:screen}
.diag-head{background:linear-gradient(110deg,rgba(33,140,218,.18),rgba(121,94,226,.14))!important;border-bottom:1px solid rgba(96,188,245,.18)!important}
.diag-title{font-family:ui-monospace,monospace!important;color:#9deaff!important;font-size:12px!important;letter-spacing:0!important;text-shadow:0 0 12px rgba(80,193,255,.35)}
.diag-line{border:1px solid rgba(92,179,238,.14)!important;background:linear-gradient(100deg,rgba(8,32,62,.72),rgba(35,30,80,.34))!important;border-radius:11px!important;padding:11px 12px!important;margin:7px 0!important;box-shadow:inset 0 1px rgba(255,255,255,.035)!important}
.diag-line:nth-child(2n){border-right:2px solid rgba(116,105,246,.65)!important}.diag-line:nth-child(2n+1){border-right:2px solid rgba(66,192,255,.65)!important}
.diag-state{font-family:'Vazirmatn',sans-serif!important;font-size:10px!important;font-weight:900!important}
.diag-state.ok{color:#69f2c4!important;text-shadow:0 0 12px rgba(40,221,171,.32)}.diag-state.err{color:#ff91a9!important;text-shadow:0 0 12px rgba(255,83,125,.25)}.diag-state.busy{color:#81dbff!important}.diag-state.na{color:#c5b1ff!important}
.diag-btn{min-height:42px!important;border-radius:12px!important;background:linear-gradient(120deg,rgba(47,144,220,.22),rgba(108,97,222,.2))!important;box-shadow:0 8px 20px rgba(0,0,0,.18),inset 0 1px rgba(255,255,255,.12)!important}.diag-foot{gap:9px!important}.diag-foot .diag-btn:first-child{background:linear-gradient(110deg,rgba(32,153,218,.27),rgba(83,92,224,.2))!important}.diag-foot .diag-btn:last-child{background:linear-gradient(110deg,rgba(145,76,217,.23),rgba(51,114,204,.2))!important}
.portal-metric,.stat-card,.speed-panel,.sub-info,.cfg-card{position:relative;overflow:hidden}
.portal-metric:nth-child(1){background:linear-gradient(145deg,rgba(6,65,102,.78),rgba(5,17,42,.94))!important;border-color:rgba(62,203,255,.3)!important}.portal-metric:nth-child(1) .ring-gauge{filter:drop-shadow(0 0 12px rgba(49,194,255,.22))}.portal-metric:nth-child(2){background:linear-gradient(145deg,rgba(55,39,104,.7),rgba(7,18,45,.95))!important;border-color:rgba(157,126,255,.31)!important}.portal-metric:nth-child(2) .ring-gauge{filter:drop-shadow(0 0 13px rgba(157,126,255,.22))}.portal-metric:nth-child(3){background:linear-gradient(145deg,rgba(12,67,81,.72),rgba(5,18,42,.95))!important;border-color:rgba(43,221,191,.25)!important}
.speed-panel{background:linear-gradient(135deg,rgba(11,36,79,.93),rgba(42,26,84,.86) 58%,rgba(68,18,54,.7))!important;border-color:rgba(122,151,255,.29)!important;box-shadow:0 22px 56px rgba(0,0,0,.3),0 0 30px rgba(108,91,237,.10),inset 0 1px rgba(255,255,255,.08)!important}.speed-chip{position:relative;overflow:hidden;background:linear-gradient(145deg,rgba(7,24,50,.82),rgba(15,18,52,.78))!important;border-radius:14px!important;box-shadow:inset 0 1px rgba(255,255,255,.07),0 8px 19px rgba(0,0,0,.14)!important}.speed-chip:nth-child(1){border-color:rgba(59,191,255,.3)!important}.speed-chip:nth-child(2){border-color:rgba(166,119,255,.32)!important}.speed-chip:nth-child(3){border-color:rgba(255,104,145,.29)!important}.speed-chip:nth-child(4){border-color:rgba(37,221,190,.29)!important}.speed-chip strong{text-shadow:0 0 13px rgba(84,173,255,.28)}.speed-chip:nth-child(2) strong{color:#d3b4ff!important;text-shadow:0 0 15px rgba(168,117,255,.3)}.speed-chip:nth-child(3) strong{color:#ffb3c4!important;text-shadow:0 0 15px rgba(255,93,143,.24)}.speed-chip:nth-child(4) strong{color:#9df5de!important;text-shadow:0 0 15px rgba(41,222,182,.22)}
.metric-remaining{color:#7af1d1!important;text-shadow:0 0 12px rgba(50,226,183,.18)!important}.metric-main-value{text-shadow:0 0 18px rgba(90,184,255,.16)}.metric-tag{box-shadow:inset 0 1px rgba(255,255,255,.12),0 5px 15px rgba(25,120,206,.12)!important}
.portal-metric:before,.stat-card:before,.speed-panel:before,.sub-info:before,.cfg-card:before{content:"";position:absolute;inset:0 12% auto;height:1px;background:linear-gradient(90deg,transparent,rgba(143,225,255,.7),transparent);pointer-events:none}
.metric-tag{border:1px solid rgba(105,192,246,.21)!important;background:rgba(54,143,216,.12)!important;color:#a5e8ff!important;border-radius:999px!important;padding:4px 9px!important;font-size:9px!important}
html[data-theme="light"] .diag-window{background:linear-gradient(145deg,rgba(249,253,255,.98),rgba(231,244,255,.97))!important;color:#153b5c!important}html[data-theme="light"] .diag-line{background:rgba(220,239,253,.72)!important;color:#1c486b!important}html[data-theme="light"] .diag-title{color:#176395!important}html[data-theme="light"] .brand-name{color:#173b5b!important}
html[data-theme="light"] .portal-metric:nth-child(1),html[data-theme="light"] .portal-metric:nth-child(2),html[data-theme="light"] .portal-metric:nth-child(3),html[data-theme="light"] .speed-panel{background:linear-gradient(145deg,rgba(245,251,255,.98),rgba(232,243,255,.96))!important;border-color:rgba(57,139,201,.22)!important}html[data-theme="light"] .speed-chip{background:rgba(255,255,255,.86)!important}html[data-theme="light"] .speed-chip strong,html[data-theme="light"] .speed-chip:nth-child(2) strong,html[data-theme="light"] .speed-chip:nth-child(3) strong,html[data-theme="light"] .speed-chip:nth-child(4) strong{color:#1c5681!important;text-shadow:none!important}
@media(max-width:720px){.top-actions{display:grid!important;grid-template-columns:repeat(2,minmax(0,1fr))!important}.public-action,.diag-open{width:100%!important;min-width:0!important}.brand-img{width:52px!important;height:52px!important}}
"""
    html = html.replace('</style>', portal_refine_css + '\n</style>', 1)
    return html
