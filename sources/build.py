"""Curry Nation programme pages v2 — styled after currynation.in (yellow ground, folk frame, colour-block tiles)."""
import os, html, shutil, re
HERE = os.path.dirname(os.path.abspath(__file__)); PARTS = os.path.join(HERE, 'parts')

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")
shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)
CONTACT = "contact.html"
UP = "https://currynation.in/wp-content/uploads/2025/05/"
LOGO = "assets/logo-badge.png"
ART = {k: UP + v for k, v in {"chai": "cutting-Chai.png", "bell": "bell.png", "elephant": "Elephant.png",
       "pigeon": "kabootar.png", "drum": "Davandi.png", "diya": "Pledge.png"}.items()}

CSS = r"""
/* Layout: currynation.in system — mustard ground inside a blue folk-print frame; colour-block tiles carry the content */
:root{
  --yellow:#ffcb21; --frame:#2a62ad; --flame:#f15922; --orange:#ff8a01; --maroon:#761817; --red:#800000;
  --green:#008400; --purple:#a100ee; --teal:#0096b4; --deep:#008173; --lime:#a1e93b; --aqua:#39fde2;
  --slate:#7092be; --pink:#cc3366; --ink:#232323; --white:#fff; --cream:#fff8e1;
  --f-display:"Big Shoulders Display","Arial Narrow",Impact,sans-serif;
  --f-body:"Be Vietnam Pro",system-ui,-apple-system,"Segoe UI",sans-serif;
  --frame-w:clamp(8px,1.3vw,18px);
  color-scheme:light;
}
*{box-sizing:border-box}
body{background-color:var(--frame);
  background-image:radial-gradient(circle at 50% 50%,#ffb347 0 2.2px,#fff 2.3px 3.4px,transparent 3.5px),radial-gradient(circle at 50% 50%,#e8403a 0 1.6px,transparent 1.7px);
  background-size:18px 18px,18px 18px;background-position:0 0,9px 9px}
body{margin:0;font:400 16px/1.65 var(--f-body);color:var(--ink);-webkit-font-smoothing:antialiased}
.page{margin:var(--frame-w) var(--frame-w) 0;background:var(--yellow);min-height:100vh;overflow:hidden}
a{color:inherit}
a:focus-visible,button:focus-visible{outline:3px solid var(--ink);outline-offset:3px}
img{max-width:100%}
.wrap{max-width:1140px;margin:0 auto;padding-inline:clamp(16px,4vw,40px)}
h1,h2,h3,p{margin:0}
h1{font:600 clamp(2.1rem,4.6vw,3.4rem)/1.12 var(--f-body);color:var(--maroon);text-wrap:balance;letter-spacing:-.01em}
.display{font:900 clamp(3rem,9vw,6.5rem)/.9 var(--f-display);text-transform:none;letter-spacing:-.01em;text-wrap:balance}
h2{font:900 clamp(2.4rem,5.6vw,4.2rem)/.95 var(--f-display);text-wrap:balance}
h3{font:800 clamp(1.6rem,3vw,2.2rem)/1 var(--f-display)}
.eyebrow{font:500 .95rem/1.2 var(--f-body);color:var(--ink)}
.eyebrow::before{content:"/ ";color:var(--flame);font-weight:700}
.hl{color:var(--flame)}
.hlp{color:var(--pink)}
/* header */
.top{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--yellow);box-shadow:0 6px 18px -12px rgba(0,0,0,.35)}
.top .wrap{display:flex;align-items:center;gap:18px;padding-block:12px;flex-wrap:wrap}
.logo{width:56px;height:56px;border-radius:50%;background:var(--flame) url(%LOGO%) center/cover no-repeat;flex:none;display:grid;place-items:center;font:900 1rem/1 var(--f-display);color:var(--yellow);text-decoration:none;box-shadow:0 0 0 3px var(--slate)}
.nav{display:flex;flex-wrap:wrap;gap:6px 18px;align-items:center;font-size:.9rem;margin-right:auto}
.nav .grp{font:800 .95rem/1 var(--f-display);text-transform:uppercase;letter-spacing:.06em;color:var(--maroon)}
.nav a{text-decoration:none;padding:4px 0;border-bottom:2px solid transparent}
.nav a:hover,.nav a[aria-current]{border-color:var(--flame)}
.nav .sep{width:1px;height:18px;background:rgba(0,0,0,.25)}
/* buttons */
.btn{display:inline-flex;align-items:center;gap:8px;padding:12px 20px;border-radius:60px;font:500 .9rem/1 var(--f-body);text-decoration:none;background:var(--flame);color:#fff;border:0;transition:transform .15s,box-shadow .15s}
.btn::after{content:"↗"}
.btn:hover{transform:translateY(-2px);box-shadow:0 6px 0 -2px var(--ink)}
.btn.dark{background:#000}
.btn.light{background:#fff;color:var(--ink)}
.ctas{display:flex;flex-wrap:wrap;gap:12px;justify-content:center}
/* hero */
.hero{padding-block:clamp(48px,8vw,96px) clamp(40px,6vw,72px);text-align:center;position:relative}
.hero .wrap{display:grid;gap:22px;justify-items:center}
.hero .lede{max-width:60ch;font-size:clamp(1rem,1.6vw,1.12rem)}
.hero .lede b{font-weight:700}
.hero .kicker{font:900 clamp(1.1rem,2vw,1.4rem)/1 var(--f-display);letter-spacing:.08em;text-transform:uppercase;color:var(--flame)}
.chips{display:flex;flex-wrap:wrap;gap:8px;justify-content:center}
.chips span{background:#fff;border-radius:60px;padding:6px 14px;font-size:.85rem}
.chips b{color:var(--maroon)}
.hero-art{position:absolute;width:clamp(90px,13vw,170px);aspect-ratio:1;background:center/contain no-repeat;opacity:.95;pointer-events:none}
.hero-art.l{left:2%;bottom:8%;transform:rotate(-8deg)}
.hero-art.r{right:2%;top:12%;transform:rotate(8deg)}
@media (max-width:900px){.hero-art{display:none}}
/* sections */
section{padding-block:clamp(48px,7vw,88px)}
.white{background:#fff}
.cream{background:var(--cream)}
.sec-head{display:grid;gap:12px;margin-bottom:34px;justify-items:start}
.sec-head.center{justify-items:center;text-align:center}
.sec-head p.sub{max-width:62ch;font-size:1.03rem}
/* stat tiles (site's YEARS / PROJECTS tiles) */
.stats{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px}
.stat{border-radius:10px;padding:18px 16px 20px;text-align:center;display:grid;gap:6px;color:#fff}
.stat .k{font:800 .95rem/1 var(--f-display);text-transform:uppercase;letter-spacing:.06em}
.stat .v{font:900 clamp(2.6rem,6vw,4rem)/.9 var(--f-display)}
.stat .s{font-size:.82rem;opacity:.9}
/* colour fills */
.c-orange{background:var(--orange);color:var(--ink)} .c-orange .k{color:var(--maroon)}
.c-teal{background:var(--teal);color:#fff} .c-teal .k{color:var(--lime)}
.c-deep{background:var(--deep);color:#fff} .c-deep .k{color:var(--aqua)}
.c-red{background:var(--red);color:#fff} .c-red .k{color:var(--orange)}
.c-green{background:var(--green);color:#fff} .c-green .k{color:var(--lime)}
.c-purple{background:var(--purple);color:#fff} .c-purple .k{color:var(--yellow)}
.c-lime{background:var(--lime);color:var(--ink)} .c-lime .k{color:var(--green)}
.c-slate{background:var(--slate);color:#fff} .c-slate .k{color:var(--cream)}
.c-flame{background:var(--flame);color:#fff} .c-flame .k{color:var(--yellow)}
.c-aqua{background:var(--aqua);color:var(--ink)} .c-aqua .k{color:var(--deep)}
/* glance table */
.card{background:#fff;border-radius:12px;padding:clamp(16px,3vw,28px)}
.tablewrap{overflow-x:auto}
table{width:100%;border-collapse:collapse;min-width:620px;font-size:.95rem}
th,td{text-align:left;vertical-align:top;padding:14px 14px 14px 0;border-bottom:1px solid #f0e2b8}
th{font:800 .95rem/1 var(--f-display);text-transform:uppercase;letter-spacing:.06em;color:var(--flame)}
td.k{font:900 1.5rem/1 var(--f-display);color:var(--maroon);white-space:nowrap}
td.t{font-weight:600;white-space:nowrap;font-variant-numeric:tabular-nums}
tr.total td{border-bottom:0;background:var(--cream)}
tr.total td.k{color:var(--flame);padding-left:10px}
.note{font-size:.85rem;margin-top:12px}
/* phases: colour tile + white panel */
.phases{display:grid;gap:18px}
.phase{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,8fr);border-radius:14px;overflow:hidden;background:#fff}
.ptile{padding:clamp(22px,3vw,34px);display:grid;gap:10px;align-content:start;position:relative;min-height:260px}
.ptile .n{font:900 clamp(4rem,9vw,6.5rem)/.8 var(--f-display)}
.ptile .k{font:800 1rem/1 var(--f-display);text-transform:uppercase;letter-spacing:.08em}
.ptile h3{font-size:clamp(2rem,3.6vw,2.8rem)}
.ptile .q{font-size:1.02rem;line-height:1.45;font-weight:500;max-width:34ch}
.ptile .art{position:absolute;right:14px;bottom:10px;width:96px;height:96px;background:center/contain no-repeat;opacity:.9}
.ppanel{padding:clamp(22px,3vw,34px);display:grid;gap:20px;align-content:start;min-width:0}
ul.acts{margin:0;padding:0;list-style:none;display:grid;gap:10px}
ul.acts li{padding-left:26px;position:relative}
ul.acts li::before{content:"↗";position:absolute;left:0;top:0;color:var(--flame);font-weight:700}
ul.acts b{font-weight:700}
.out{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.out div{background:var(--cream);border-radius:10px;padding:14px;display:grid;gap:4px;align-content:start}
.out dt{font:800 .85rem/1 var(--f-display);text-transform:uppercase;letter-spacing:.07em;color:var(--flame)}
.out dd{margin:0;font-size:.9rem;line-height:1.45}
.out div:nth-child(2) dd{font-weight:600;color:var(--maroon)}
.lens{display:flex;flex-wrap:wrap;gap:8px;align-items:center;font-size:.85rem}
.lens>span:first-child{font:800 .85rem/1 var(--f-display);text-transform:uppercase;letter-spacing:.07em;margin-right:4px}
.pill{border:1.5px solid var(--ink);border-radius:60px;padding:4px 12px}
.pill b{font-weight:700}
/* pillars (hub) */
.pillar{display:grid;gap:18px}
.pillar-head{display:flex;flex-wrap:wrap;align-items:end;justify-content:space-between;gap:16px}
.bento{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:0;border-radius:14px;overflow:hidden}
.bento a{display:grid;gap:10px;align-content:start;padding:clamp(20px,3vw,30px);min-height:300px;text-decoration:none;position:relative;transition:filter .2s}
.bento a:hover{filter:saturate(1.15) brightness(1.04)}
.bento .k{font:800 .95rem/1 var(--f-display);text-transform:uppercase;letter-spacing:.08em}
.bento h3{font-size:clamp(2.1rem,3.6vw,3rem)}
.bento p{font-size:.95rem;line-height:1.5;max-width:32ch}
.bento .go{margin-top:auto;font-weight:600;font-size:.9rem}
.bento .go::after{content:" ↗"}
.bento .art{position:absolute;right:12px;bottom:12px;width:110px;height:110px;background:center/contain no-repeat}
.badge{display:inline-block;background:#fff;color:var(--flame);border-radius:60px;padding:3px 10px;font:800 .8rem/1.2 var(--f-display);letter-spacing:.06em;width:max-content}
/* tier scale */
.scale{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.tier{border-radius:12px;padding:20px 16px;display:grid;gap:8px;align-content:start}
.tier .k{font:800 1rem/1 var(--f-display);letter-spacing:.06em;font-variant-numeric:tabular-nums}
.tier .nm{font:900 2.2rem/.9 var(--f-display)}
.tier p{font-size:.9rem;line-height:1.4}
.tier .to{font-size:.85rem;font-weight:600;border-top:1px solid currentColor;padding-top:8px;margin-top:4px}
/* areas */
.areas{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px}
.area{border-radius:12px;padding:20px;display:grid;gap:8px;align-content:start}
.area .v{font:900 3.4rem/.85 var(--f-display)}
.area .v small{font:800 .9rem var(--f-display);letter-spacing:.06em;margin-left:4px}
.area h3{font-size:1.8rem}
.area p{font-size:.9rem}
/* numbered list */
ol.reveal{margin:0;padding:0;list-style:none;display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px;counter-reset:r}
ol.reveal li{counter-increment:r;background:#fff;border-radius:12px;padding:16px 18px;display:grid;grid-template-columns:auto minmax(0,1fr);gap:12px;align-items:start;font-size:.95rem}
ol.reveal li::before{content:counter(r);font:900 2.2rem/.85 var(--f-display);color:var(--flame)}
/* steps */
ol.steps{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;counter-reset:s}
ol.steps li{counter-increment:s;background:#fff;border-radius:12px;padding:18px;display:grid;gap:6px;align-content:start}
ol.steps li::before{content:counter(s,decimal-leading-zero);font:900 2.6rem/.85 var(--f-display);color:var(--flame)}
ol.steps b{font-weight:700}
/* day timeline */
.day{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.slot{border-radius:12px;padding:18px;display:grid;gap:6px;align-content:start}
.slot time{font:900 2.2rem/.9 var(--f-display);font-variant-numeric:tabular-nums}
.slot h3{font-size:1.5rem}
.slot p{font-size:.9rem;line-height:1.45}
/* terms */
.terms{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.terms div{background:#fff;border-radius:12px;padding:16px 18px;display:grid;gap:4px;min-width:0}
.terms h4{margin:0;font:800 1.05rem/1 var(--f-display);text-transform:uppercase;letter-spacing:.06em;color:var(--flame)}
.terms p{font-size:.92rem}
/* promise */
.promise{border-radius:16px;padding:clamp(26px,5vw,52px);display:grid;gap:14px;text-align:center;justify-items:center}
.promise p{max-width:62ch}
/* founder ladder */
.ladder{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;align-items:end}
.rung{border-radius:14px;padding:clamp(20px,3vw,28px);display:grid;gap:10px;align-content:start}
.rung:nth-child(1){min-height:300px}.rung:nth-child(2){min-height:360px}.rung:nth-child(3){min-height:420px}
.rung .k{font:800 .95rem/1 var(--f-display);letter-spacing:.08em;text-transform:uppercase}
.rung h3{font-size:clamp(2.6rem,5vw,3.8rem)}
.rhythm{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.rhythm div{background:#fff;border-radius:12px;padding:18px;display:grid;gap:4px}
.rhythm .v{font:900 3rem/.85 var(--f-display);color:var(--purple)}
/* related + close */
.related{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px}
.related a{border-radius:12px;padding:18px;text-decoration:none;display:grid;gap:6px;transition:transform .15s}
.related a:hover{transform:translateY(-3px)}
.related b{font:900 1.7rem/1 var(--f-display)}
.related span{font-size:.88rem}
.close{text-align:center}
.close .wrap{display:grid;gap:18px;justify-items:center}
.close .display{color:var(--maroon)}
.close p{max-width:56ch}
.foot{background:#000;color:#ddd;font-size:.85rem}
.foot .wrap{display:flex;flex-wrap:wrap;justify-content:space-between;gap:12px;padding-block:24px}
.foot a{text-decoration:none;color:var(--yellow)}
@media (max-width:860px){
  .phase{grid-template-columns:1fr}.ptile{min-height:0}
  .out,.terms,.day,.ladder,.rhythm,.bento{grid-template-columns:1fr}
  .stats,.scale,.areas{grid-template-columns:repeat(2,minmax(0,1fr))}
  .rung{min-height:0!important}.bento a{min-height:230px}
}
@media (max-width:440px){.stats,.scale,.areas{grid-template-columns:1fr}}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
"""
CSS += open(PARTS + "/extra.css").read()
CSS += open(PARTS + "/v4.css").read()
CSS += open(PARTS + "/v5.css").read()
CSS += open(PARTS + "/v6.css").read()
CSS += open(PARTS + "/v7.css").read()
CSS += open(PARTS + "/v8.css").read()
CSS += open(PARTS + "/v10.css").read()
CSS += open(PARTS + "/v11.css").read()
CSS += open(PARTS + "/v13.css").read()
CSS += open(PARTS + "/v14.css").read()
CSS += open(PARTS + "/v15.css").read()
import sys; sys.path.insert(0, PARTS)
import company as co
from pkgs import pkg_section, cmp_section, FOUNDER, C2B, PERF as PERF_PK, DESIGN as DESIGN_PK, LEAD, BRAND, LEAD_PAGE
from faqs import FAQ, faq_section, faq_schema
import json as _json
CSS = CSS.replace("%LOGO%", LOGO)

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@500;600;700&family=Be+Vietnam+Pro:wght@400;500;600;700&display=swap">'

# ================================================================ V4 NAV (cascading)
PLANNER = "https://currynation-performance.arup-5d2.workers.dev/#planner"
MENU = [
 ("Brand-led", "brand", "When buyers can’t tell you from the next supplier", [
   ("brand-led.html", "All Commodity to Brand packages", "Audit · Positioning · Workshops"),
   ("brand-audit.html", "Brand Audit", "Free · about 10 minutes"),
   ("brand-positioning.html", "Brand Positioning", "3 phases · 6 weeks"),
   ("leadership-workshop.html", "Challenger Workshop for Leadership", "One problem · 2-day offsite"),
      ("challenger-workshop.html#business", "Challenger Workshop for Business", "5 weeks of evidence + workshop + plan")]),
 ("Founder-led", "founder", "When the business is ahead of the founder’s authority", [
   ("founder-visibility.html#audit", "Founder Authority Audit", "₹5,000 · 10 working days"),
   ("founder-visibility.html#plan", "Action Plan", "What to build, and in what order"),
   ("founder-visibility.html#build", "System Build", "4 weeks to a position and content system"),
   ("founder-visibility.html#implement", "Implement", "DIY, guided or managed")]),
 ("Performance-led", "performance", "When sales grow but profit doesn’t", [
   ("performance.html#growth-audit", "Growth Audit", "3–4 weeks · fixed scope"),
   ("performance.html#market-launch", "Market Launch", "90-day managed pilot"),
   ("performance.html#scale", "Scale Partnership", "Ongoing · tailored scope"),
   (PLANNER, "Growth Planner ↗", "Model reach, visits and orders")]),
 ("Design-led", "design", "When you look like a commodity on shelf and screen", [
   ("design.html#identity", "Brand Identity System", "Logo, visual system, guidelines"),
   ("design.html#packaging", "Packaging & Shelf", "Packs, labels, point of sale")]),
]
HUB = {"brand": "brand-led.html", "founder": "founder-visibility.html", "performance": "performance.html", "design": "design.html"}

CO_PAGES = [("work.html", "Work"), ("about.html", "About"), ("resources.html", "Free Resources")]
def CO_LINKS(cur):
    return "".join(f'<li class="m solo lnk"><a class="mt" href="{h}"{" aria-current=\"page\"" if cur==h else ""}>{t}</a></li>' for h, t in CO_PAGES)

def header(cur):
    items = ""
    for name, key, line, subs in MENU:
        hub = HUB[key]
        here = cur == hub or any(h.split("#")[0] == cur for h, _, _ in subs)
        links = "".join(
            f'<a href="{h}"{" target=\"_blank\" rel=\"noopener\"" if h.startswith("http") else ""}><b>{t}</b><small>{s}</small></a>'
            for h, t, s in subs)
        items += f"""<li class="m{" here" if here else ""}"><a class="mt" href="{hub}">{name}</a><button class="mx" type="button" aria-expanded="false" aria-label="Show {name} products"><i aria-hidden="true">▾</i></button>
<div class="sub"><p class="sub-k">{line}</p>{links}<a class="all" href="index.html#{key}">See all {name} products →</a></div></li>"""
    return f"""<header class="top" id="top"><div class="wrap">
<a class="logo" href="index.html" aria-label="Curry Nation home"><img src="logo.png" alt="Curry Nation" width="64" height="64"></a>
<nav class="nav" id="mainnav" aria-label="Products"><ul class="menu"><li class="m solo"><a class="mt" href="index.html"{" aria-current=\"page\"" if cur=="index.html" else ""}>Home</a></li>{items}{CO_LINKS(cur)}</ul></nav>
<a class="btn cta-top" href="{CONTACT}">Let’s Connect</a>
<button class="burger" type="button" aria-controls="mainnav" aria-expanded="false"><span></span>Menu</button>
</div></header>"""

NAVJS = r'''<script>(function(){
var ms=document.querySelectorAll('.m:not(.solo)');
function shut(x){x.classList.remove('open');var b=x.querySelector('.mx');if(b)b.setAttribute('aria-expanded','false')}
ms.forEach(function(li){var b=li.querySelector('.mx');b.addEventListener('click',function(e){e.stopPropagation();var o=!li.classList.contains('open');ms.forEach(shut);if(o){li.classList.add('open');b.setAttribute('aria-expanded','true')}})});
document.addEventListener('click',function(e){if(!e.target.closest('.m'))ms.forEach(shut)});
document.addEventListener('keydown',function(e){if(e.key==='Escape')ms.forEach(shut)});
var bg=document.querySelector('.burger'),hd=document.querySelector('.top');
if(bg)bg.addEventListener('click',function(){var o=hd.classList.toggle('navopen');bg.setAttribute('aria-expanded',o?'true':'false')});
document.querySelectorAll('.sub a').forEach(function(a){a.addEventListener('click',function(){hd.classList.remove('navopen');ms.forEach(shut)})});
var calm=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
var r=document.querySelector('[data-rotate]');
if(r&&!calm){var w=r.getAttribute('data-rotate').split('|'),i=0;setInterval(function(){r.classList.add('out');setTimeout(function(){i=(i+1)%w.length;r.textContent=w[i];r.classList.remove('out')},280)},2300)}
document.querySelectorAll('.vplay').forEach(function(b){b.addEventListener('click',function(){var f=document.createElement('iframe');f.src='https://www.youtube-nocookie.com/embed/'+b.getAttribute('data-yt')+'?autoplay=1&rel=0';f.allow='autoplay; encrypted-media; picture-in-picture';f.allowFullscreen=true;f.title='Client testimonial';b.replaceWith(f)})});
})();</script>'''

FOOT = f'''<footer class="foot"><div class="wrap"><nav class="foot-links" aria-label="Footer"><a href="index.html">Home</a><a href="brand-led.html">Brand-led</a><a href="founder-visibility.html">Founder-led</a><a href="performance.html">Performance-led</a><a href="design.html">Design-led</a><a href="work.html">Work</a><a href="about.html">About</a><a href="resources.html">Free Resources</a><a href="contact.html">Contact</a></nav>{co.social_row()}<span>© 2026 Curry Nation Brand Conversations</span></div></footer>'''

MBAR = {
 "index.html": [("Free Brand Audit", "brand-audit.html"), ("Let’s talk", CONTACT)],
 "brand-led.html": [("Free Brand Audit", "brand-audit.html"), ("Let’s talk", CONTACT)],
 "brand-audit.html": [("Start the audit", CONTACT), ("Let’s talk", CONTACT)],
 "founder-visibility.html": [("Book the ₹5,000 Audit", "mailto:challengeus@currynation.in?subject=Founder%20Authority%20Audit"), ("Packages", "#packages")],
 "performance.html": [("Start a conversation", "mailto:nagesshp@currynation.in?subject=Growth%20enquiry"), ("Planner ↗", PLANNER)],
}
ORG = _json.dumps({"@context":"https://schema.org","@type":"Organization","name":"Curry Nation Brand Conversations","url":"https://currynation.in/","logo":"https://currynation.in/assets/logo-badge.png","address":{"@type":"PostalAddress","addressLocality":"Mumbai","addressCountry":"IN"}}, ensure_ascii=False)

CNMAP = _json.load(open(os.path.join(HERE, "cnmap.json")))
def _local(m):
    from urllib.parse import unquote
    p = unquote(m.group(1))
    if p in CNMAP: return "assets/cn/" + CNMAP[p]
    if p.lower().endswith(".pdf"): return ""
    print("WARN unmapped upload:", p); return m.group(0)
def localise(h): return re.sub(r'https://currynation\.in/wp-content/uploads/([^"\'()\s]+)', _local, h)

def doc(fname, title, desc, body, full=True):
    head = f'<meta name="referrer" content="no-referrer">\n<title>{html.escape(title)}</title>\n<meta name="description" content="{html.escape(desc)}">\n{FONTS}\n<style>{CSS}</style>'
    mb = MBAR.get(fname, [("Free Brand Audit", "brand-audit.html"), ("Let’s talk", CONTACT)])
    bar = f'<nav class="mbar" aria-label="Quick actions"><a class="p" href="{mb[0][1]}">{mb[0][0]}</a><a class="s" href="{mb[1][1]}">{mb[1][0]}</a></nav>'
    extra = '<div class="progress" aria-hidden="true"></div><button class="totop" type="button" aria-label="Back to top">↑</button>' + bar
    items = FAQ.get(fname) or (FV_FAQ if fname == "founder-visibility.html" else None)
    head += f'\n<link rel="icon" href="assets/favicon-48.png" sizes="48x48"><link rel="apple-touch-icon" href="assets/apple-touch-icon.png"><meta name="theme-color" content="#ffcb21">'
    head += f'\n<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:type" content="website"><meta property="og:image" content="assets/team.jpg"><meta name="twitter:card" content="summary_large_image">'
    head += f'\n<script type="application/ld+json">{ORG}</script>' + (faq_schema(items) if items else "")
    inner = '<div class="page">' + header(fname) + "<main>" + body + "</main>" + FOOT + "</div>" + FB + NAVJS
    inner = re.sub(r'(<a class="btn[^"]*"[^>]*>[^<]*?)\s*↗</a>', r'\1</a>', inner)
    head, inner = localise(head), localise(inner)
    if not full: return head + "\n" + inner
    return f'<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n{head}\n</head><body>\n{inner}\n</body></html>'

def art(k, cls="art"): return f'<span class="{cls}" style="background-image:url({ART[k]})" aria-hidden="true"></span>'

def hero(kicker, h1, lede, chips, ctas, arts=("chai", "bell")):
    c = "".join(f"<span>{a} <b>{b}</b></span>" for a, b in chips)
    b = "".join(f'<a class="btn{" " + s if s else ""}" href="{h}">{t}</a>' for t, h, s in ctas)
    a = art(arts[0], "hero-art l") + art(arts[1], "hero-art r") if arts else ""
    return f'<section class="hero">{a}<div class="wrap"><p class="kicker">{kicker}</p><h1>{h1}</h1><p class="lede">{lede}</p><div class="chips">{c}</div><div class="ctas">{b}</div></div></section>'

def head(eyebrow, h, sub=None, center=False):
    s = f'<p class="sub">{sub}</p>' if sub else ""
    return f'<div class="sec-head{" center" if center else ""}"><p class="eyebrow">{eyebrow}</p><h2>{h}</h2>{s}</div>'

def glance(cols, rows, total=None, note=None):
    th = "".join(f"<th>{c}</th>" for c in cols); tr = ""
    for r in rows + ([total] if total else []):
        tds = f'<td class="k">{r[0]}</td>' + "".join(f'<td{" class=\"t\"" if i==len(r)-2 else ""}>{x}</td>' for i, x in enumerate(r[1:]))
        tr += f'<tr{" class=\"total\"" if total is r else ""}>{tds}</tr>'
    n = f'<p class="note">{note}</p>' if note else ""
    return f'<div class="card"><div class="tablewrap"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>{n}</div>'

def stats(items):
    return '<div class="stats">' + "".join(f'<div class="stat {c}"><span class="k">{k}</span><span class="v">{v}</span><span class="s">{s}</span></div>' for c, k, v, s in items) + "</div>"

def phase(color, no, name, time, q, acts, deliv, result, signoff, lens=None, lens_label="Lens", a=None):
    li = "".join(f"<li>{x}</li>" for x in acts)
    l = ""
    if lens: l = f'<div class="lens"><span>{lens_label}</span>' + "".join(f'<span class="pill"><b>{k}:</b> {v}</span>' for k, v in lens) + "</div>"
    return f'''<article class="phase"><div class="ptile {color}"><span class="k">{time}</span><span class="n">{no}</span><h3>{name}</h3><p class="q">{q}</p>{art(a) if a else ""}</div>
<div class="ppanel"><ul class="acts">{li}</ul><dl class="out"><div><dt>You get</dt><dd>{deliv}</dd></div><div><dt>Your business can now</dt><dd>{result}</dd></div><div><dt>Sign-off</dt><dd>{signoff}</dd></div></dl>{l}</div></article>'''

def terms(items): return '<div class="terms">' + "".join(f"<div><h4>{k}</h4><p>{v}</p></div>" for k, v in items) + "</div>"
def steps(items): return '<ol class="steps">' + "".join(f"<li><b>{a}</b><span>{b}</span></li>" for a, b in items) + "</ol>"

REL = {
 "brand-led.html": ("c-red", "Commodity to Brand", "Brand-led · four packages, one ladder."),
 "brand-audit.html": ("c-red", "Brand Audit", "Brand-led · free, about ten minutes."),
 "brand-positioning.html": ("c-red", "Brand Positioning", "Brand-led · a position nobody owns, in six weeks."),
 "challenger-workshop.html": ("c-red", "Challenger Workshop for Business", "Brand-led · five weeks of evidence, then the workshop."),
 "founder-visibility.html": ("c-purple", "Founder Authority System", "Founder-led · audit from ₹5,000."),
 "performance.html": ("c-teal", "Growth Lab", "Performance-led · profitable growth, not just sales."),
 "design.html": ("c-orange", "Design-led", "Brand identity and packaging."),
 "leadership-workshop.html": ("c-red", "Challenger Workshop for Leadership", "Brand-led · one problem, two days."),
}
def related(cur):
    cards = "".join(f'<a class="{c}" href="{f}"><b>{t}</b><span>{d}</span></a>' for f, (c, t, d) in REL.items() if f != cur)
    return f'<section class="cream"><div class="wrap">{head("keep exploring", "Other ways in")}<div class="related">{cards}</div></div></section>'

def close(h, p, btn, href=CONTACT):
    return f'<section class="close"><div class="wrap"><p class="eyebrow">let’s talk</p><h2 class="display">{h}</h2><p>{p}</p><div class="ctas"><a class="btn" href="{href}">{btn}</a><a class="btn dark" href="{CONTACT}">Work with us</a></div></div></section>'

FB = '<script>document.querySelectorAll(".marquee img").forEach(function(i){function f(){var s=document.createElement("span");s.className="wm";s.textContent=i.alt;i.replaceWith(s)}if(i.complete&&!i.naturalWidth)f();else i.addEventListener("error",f)});</script>'
TAIL = [("Ownership", "Final deliverables are yours on full payment. We may reuse anonymised learnings and our method."),
        ("Confidentiality", "Both sides keep shared information confidential. Case references stay anonymised unless you agree in writing."),
        ("Timing", "Delays in inputs or approvals shift dates equally. Third-party costs such as travel, research panels and data are billed at actuals, with your approval first.")]

# ================================================================ HOME (v4)
CLIENTS = [("jai-hind-l.jpg","Jai Hind"),("laughing-cow-l.png","The Laughing Cow"),("kisan-l.png","Kissan"),("eva-l.png","Eva"),
 ("good-home-l.png","Good Home"),("one-run-l.png","One Run"),("pitara-l.png","Pitaara"),("png-l.png","PNG Jewellers"),
 ("rasna-l.png","Rasna"),("acc-l.png","ACC"),("mahindra-l.png","Mahindra"),("abbott-l.png","Abbott"),("nirlep-l.png","Nirlep"),
 ("weikfield-l.png","Weikfield"),("sollatek-l.png","Sollatek"),("bindwell-l.png","Bindwel"),("selsun-l.png","Selsun"),
 ("boro-plus-l.png","BoroPlus"),("chipseez-l.png","Chipseez"),("toi-l.png","The Times of India")]
logos = "".join(f'<li><img src="{UP}{f}" alt="{n}" loading="lazy"></li>' for f, n in CLIENTS)

ROT = "brands|founders|profitable sales|recall|leaders"
hm = f'''<section class="hero home-hero"><div class="wrap hero-split"><div class="hero-copy">
<p class="kicker">From Invisible to Irresistible™</p>
<h1 class="giant">We grow <span class="rot" data-rotate="{ROT}">brands</span></h1>
<p class="for">for <b>ambitious owner-managed businesses</b></p>
<div class="ctas"><a class="btn" href="#products">See the products</a><a class="btn dark" href="brand-audit.html">Take the free Brand Audit</a></div></div>
<figure class="hero-team"><img src="assets/team.jpg" alt="The Curry Nation team at an offsite, in matching white T-shirts" width="1049" height="587"><figcaption><b>The Curry Nation team</b> · strategy, creative, media and growth under one roof</figcaption>{art("drum","sticker")}</figure>
</div></section>'''
hm += f'''<section class="white logos-sec"><div class="wrap"><p class="eyebrow" style="text-align:center">Trusted clients worldwide</p></div>
<div class="marquee" aria-label="Clients"><ul>{logos}</ul><ul aria-hidden="true">{logos}</ul></div></section>'''

PILLARS = [
 ("1", "Brand-led", "brand", "c-red", "elephant",
  "When buyers can’t tell you from the next supplier, they choose on price. We make you the brand they ask for by name.",
  "Premium pricing and preference that doesn’t depend on a scheme.",
  [("brand-audit.html", "Brand Audit", "Free", "Twenty questions, about ten minutes. Your score out of 40, your tier, and what your two weakest areas cost you."),
   ("brand-positioning.html", "Brand Positioning", "6 weeks", "Discover, Define, Express. Find the reason to choose you that no rival owns, prove it, and launch it in 90 days."),
   ("leadership-workshop.html", "Challenger Workshop for Leadership", "2-day offsite", "The founder names one problem. Senior operators challenge each decision-maker on it, then the team agrees a 90-day plan in the room."),
   ("challenger-workshop.html", "Challenger Workshop for Business", "~7 weeks", "Five weeks of customer, trade and rival evidence first, then the workshop, so the plan is built on facts.")]),
 ("2", "Founder-led", "founder", "c-purple", "pigeon",
  "When the business is ahead of the founder’s public authority, every new buyer, partner and hire starts cold.",
  "Context before contact: conversations that start warm.",
  [("founder-visibility.html#audit", "Founder Authority Audit", "₹5,000", "Where the founder’s authority stands today. Scorecard, gaps and a 90-day opportunity map in 10 working days."),
   ("founder-visibility.html#plan", "Action Plan", "On call", "Which kind of authority matters in your market, where to show up, and in what order."),
   ("founder-visibility.html#build", "System Build", "4 weeks", "Position, narrative, content, profile and a working AI workspace that you own."),
   ("founder-visibility.html#implement", "Implement", "On call", "Your team runs it, we guide it, or we manage the monthly rhythm.")]),
 ("3", "Performance-led", "performance", "c-teal", "diya",
  "When sales grow but profit doesn’t, the media is buying orders, not contribution.",
  "Growth judged by contribution after fees, returns and discounts, not by in-platform ROAS.",
  [("performance.html#growth-audit", "Growth Audit", "3–4 weeks", "Margins, accounts, tracking, listings and stock reviewed. An opportunity map and a 90-day action plan."),
   ("performance.html#market-launch", "Market Launch", "90 days", "A managed pilot: campaigns, creative tests, better product pages, weekly reviews and scale or stop rules."),
   ("performance.html#scale", "Scale Partnership", "Ongoing", "Meta, Google, LinkedIn and marketplaces managed together, with decisions tied to inventory and contribution."),
   (PLANNER, "Growth Planner", "Free tool", "Model reach, visits and potential orders by platform, market and budget before you spend.")]),
 ("4", "Design-led", "design", "c-orange", "bell",
  "When you look like a commodity on the shelf and the screen, you get priced like one.",
  "A brand identity and pack people recognise before they read a word.",
  [("design.html#identity", "Brand Identity System", "On call", "Logo, visual system, typography, colour and guidelines your team and vendors can follow."),
   ("design.html#packaging", "Packaging & Shelf", "On call", "Packs, labels, back-of-pack claims and point-of-sale that justify the price.")]),

]
cards = ""
for n, name, key, col, a, problem, outcome, prods in PILLARS:
    plist = "".join(
        f'<a class="prod" href="{h}"{" target=\"_blank\" rel=\"noopener\"" if h.startswith("http") else ""}><span class="pt">{t}</span><span class="pm">{m}</span><span class="pd">{d}</span></a>'
        for h, t, m, d in prods)
    cards += f'''<article class="pillar-row" id="{key}"><div class="ptag {col}"><span class="n">{n}</span><h3>{name}</h3><p>{problem}</p><p class="oc"><b>Outcome:</b> {outcome}</p>{art(a)}</div>
<div class="prods{" one" if len(prods)==1 else ""}">{plist}</div></article>'''
hm += f'''<section id="products"><div class="wrap">{head("what we do", "Growth and outcome-based products", "Four ways we grow an owner-managed business. Each product is built around one outcome, priced up front or scoped after a short call, and can be bought on its own.")}
<div class="pillars">{cards}</div></div></section>'''

hm += f'''<section class="cxo-band" id="cxo"><div class="wrap cxo-grid">
<div><p class="eyebrow light">brand-led · for leadership teams</p><h2 class="display">One problem. Two days. Every decision-maker in the room.</h2>
<p class="sub">The Challenger Workshop for Leadership starts with one problem the founder gives us. At an offsite, senior operators matched to each function challenge your decision-makers on it, then the team works the problem through and agrees a 90-day plan, with the founder in the room.</p>
<div class="ctas" style="justify-content:flex-start"><a class="btn" href="leadership-workshop.html">See how it works</a><a class="btn light" href="{CONTACT}">Talk to us</a></div></div>
<div class="cxo-facts">
<div><span class="v">1</span><span>problem statement from the founder</span></div>
<div><span class="v">2</span><span>days at an offsite, never your premises</span></div>
<div><span class="v">5</span><span>senior operators, one per function</span></div>
<div><span class="v">90</span><span>day plan with named owners</span></div>
</div></div></section>'''

CASES = [
 ("case-laughingcow.jpg", "The Laughing Cow · Bel", "Cheese", "Owning the tiffin box",
  "A European cheese brand entering India with cheese in a sachet, against established players like Amul and Britannia.",
  "Instead of being everything for everybody, we owned the tiffin box. Mascot, influencer and 360° in-store activations.",
  [("+30%", "brand awareness and usage"), ("#2", "cheese brand in the country"), ("50%+", "retention after first purchase"), ("10%", "share in key retail accounts")]),
 ("case-kinderjoy.jpg", "Kinder Joy · Ferrero", "Confectionery", "“Imagination ko Jodo”",
  "Build a distinct preference among children and mothers in a market dominated by established confectionery giants.",
  "Positioned the toy as an investment in a child’s imagination, with TV films, a Diwali 360° campaign and social storytelling.",
  [("The result", "A pioneer of play with indulgence, and a community of parent advocates creating their own content")]),
 ("case-eva.jpg", "Eva", "Women’s deodorant", "The confidence enabler for teens",
  "A market leader losing share in a cluttered deo market full of new entrants and price challenges.",
  "Targeted teens, an unaddressed segment, stepping into a new world. TV commercials with Rashmika Mandanna.",
  [("The shift", "From one more deo on the shelf to the brand teens choose for confidence")]),
 ("case-oicia.jpg", "Oicia", "Premium kitchenware", "From kitchen utility to modern dining",
  "Strong products and premium design, but buyers still saw a good utility brand.",
  "Rebuilt the brand lens around premium modern living, with campaigns built on dining, gifting and hosting.",
  [("The shift", "Utility products → a modern dining aesthetics brand")]),
 ("case-selsun.jpg", "Selsun · Abbott", "Anti-dandruff shampoo", "“Bade problem ka simple solution”",
  "Win metro millennials with acute dandruff, who reach for home remedies first.",
  "Social campaigns with celebrity influencer Rohan Mehra, taking on the traditional remedies.",
  [("2M", "views"), ("36,000", "Amazon store visits"), ("+15%", "unit volumes"), ("+20%", "sales, month on month")]),
 ("case-bkt.jpg", "BKT Tires", "Off-highway tyres", "Becoming “Bharat Ka Tire”",
  "A global off-highway tyre leader, one of the last to enter India, and seen as foreign.",
  "Rebranded BKT as Bharat Ka Tire, with video-led product stories rooted in Indian identity.",
  [("6.2M", "impressions"), ("4.3M", "reach"), ("96.7K", "engagements"), ("1.75M", "video views")]),
]
def _case(img, client, cat, title, chal, did, stats):
    st = "".join(f'<div><b>{v}</b><span>{k}</span></div>' for v, k in stats)
    return f'''<article class="case-card"><img src="assets/{img}" alt="{client} campaign creative" loading="lazy">
<div class="cc-body"><p class="cc-k"><b>{client}</b> · {cat}</p><h3>{title}</h3>
<dl><dt>The challenge</dt><dd>{chal}</dd><dt>What we did</dt><dd>{did}</dd></dl>
<div class="cc-stats{" one" if len(stats)==1 else ""}">{st}</div></div></article>'''
hm += f'''<section class="white" id="case-studies"><div class="wrap">{head("case studies", "Work that moved the business", "Six brands, six different problems, from category creation to repositioning. Results are from past campaigns and do not imply guaranteed outcomes.")}
<div class="cases">{"".join(_case(*c) for c in CASES)}</div></div></section>'''
hm += f'''<section class="white"><div class="wrap">{head("about curry nation", "Hi, we’re Curry Nation!")}
<div class="about">
<div class="ab c-orange big"><p>We’re not just an ad agency. We’re India’s only <b class="hlp">brand transformation partner</b> focused exclusively on <b class="hlp">owner-managed commodity businesses.</b></p></div>
<div class="ab c-green">{art("chai","ab-art")}</div>
<div class="ab c-red">{art("drum","ab-art")}</div>
<div class="ab c-purple">{art("bell","ab-art")}</div>
<div class="ab c-teal">{art("diya","ab-art")}</div>
<div class="ab c-lime wide"><p>From PNG Jewellers to BKT, Sollatek, RL Steel and Bindwel, we’ve helped businesses like yours become the brand everyone’s talking about.</p></div>
<div class="ab c-deep">{art("elephant","ab-art")}</div>
<div class="ab c-aqua wide"><p>Our founders built Havells, Halonix, Greenply, Camlin and Ambuja Cements, turning trade-led products into customer-demanded brands.</p></div>
<div class="ab c-slate">{art("pigeon","ab-art")}</div>
</div>
<div class="stats" style="margin-top:14px">
<div class="stat c-orange"><span class="k">Large campaigns</span><span class="v">250+</span><span class="s">advertising campaigns executed</span></div>
<div class="stat c-teal"><span class="k">Ad films</span><span class="v">400+</span><span class="s">across TV and digital</span></div>
<div class="stat c-deep"><span class="k">Projects</span><span class="v">75+</span><span class="s">MNCs, Indian firms, SMEs, start-ups</span></div>
<div class="stat c-red"><span class="k">Awards</span><span class="v">30+</span><span class="s">for creative and marketing work</span></div></div>
<div class="leaders">
<figure class="leader"><img src="assets/nagessh.jpg" alt="Nagessh Pannaswami" loading="lazy"><figcaption><b>Nagessh Pannaswami</b><span>Founder · Brand growth strategist</span><p>30+ years transforming FMCG, durables and industrial brands. Built Bindwel, Mosil, ACC, RL Steel, BKT, Halonix and Camlin. Author of the Amazon bestseller <i>From Commodity to Brand</i>.</p></figcaption></figure>
<figure class="leader"><img src="assets/priti.jpg" alt="Priti Nair" loading="lazy"><figcaption><b>Priti Nair</b><span>Co-founder · Creative leader</span><p>36+ years. Launched BBH in India, ECD at Lowe, creative head at Lintas. Behind “What an Idea Sirji”, “Shock Laga” and “Red Bindi”.</p></figcaption></figure>
<figure class="leader"><img src="assets/navin.jpg" alt="Navin B" loading="lazy"><figcaption><b>Navin B</b><span>Head of Growth</span><p>10+ years turning marketing into measurable growth across e-commerce, social, paid media and conversion funnels.</p></figcaption></figure>
</div>
<div class="ctas" style="margin-top:22px"><a class="btn dark" href="about.html">Know more</a><a class="btn light" href="work.html">Explore our work</a></div></div></section>'''
AW = [("award-lacp-ambuja.jpg","LACP Vision Awards · Silver","Ambuja Cements · Annual report · 2020"),
 ("award-power-print-croma.jpg","Times Power of Print · First runner-up","Croma · Print · 2019"),
 ("award-power-print-nestle.jpg","Times Power of Print · Winner","Nestlé · Print · 2018"),
 ("award-ncea-laadli.jpg","National Creative Excellence · Silver","Laadli, “Ashamed” · Design · 2020"),
 ("award-abby-nirlep.jpg","Goafest Creative Abby","Nirlep · Radio · 2014"),
 ("award-abby-masoom.jpg","Goafest Creative Abby","Masoom Night School · Print · 2014"),
 ("award-abby-taste.jpg","Goafest Creative Abby","Taste for Life · Print · 2014"),
 ("award-kyoorius-taste.jpg","Kyoorius Design Awards","Taste for Life · Graphic design · 2014"),
 ("award-psff.jpg","12th Pune Short Film Festival · Best Advertisement","“The Confidant” · 2022")]
awg = "".join(f'<figure class="aw"><img src="assets/{f}" alt="{t} trophy" loading="lazy"><figcaption><b>{t}</b><span>{c}</span></figcaption></figure>' for f, t, c in AW)
hm += f'''<section id="awards"><div class="wrap">{head("awards won", "Real results. Proven impact.", "30+ awards for work that moved the business, most recently Product Launch Campaign of the Year at the AdAura Awards 2026, for Good Home.")}
<div class="aw-feat">
<figure class="awf big"><img src="assets/award-adaura-goodhome.jpg" alt="AdAura Awards 2026 trophy for Good Home" loading="lazy"><figcaption><span class="k">AdAura Awards 2026 · Marketing Mind</span><b>Product Launch Campaign of the Year</b><span>Good Home · “Bathroom Nahi. Freshroom.” · Integrated Marketing Excellence</span></figcaption></figure>
<figure class="awf"><img src="assets/award-e4m-ima.jpg" alt="Two e4m Indian Marketing Awards trophies for The Laughing Cow" loading="lazy"><figcaption><span class="k">e4m Indian Marketing Awards · Silver · 2022</span><b>Best Product Launch and Best Category Creation</b><span>The Laughing Cow cheese · “The Lost Hunger” and “Mom, one more please”</span></figcaption></figure>
<figure class="awf"><img src="assets/award-health-marcom.jpg" alt="e4m Health Marcom and Inkspell trophies" loading="lazy"><figcaption><span class="k">e4m Health Marcom · Gold · 2022</span><b>Best Integrated Campaign, Food & Beverages</b><span>The Laughing Cow · plus Gold at Inkspell Masters of Modern Marketing</span></figcaption></figure>
<figure class="awf"><img src="assets/award-inkspell.jpg" alt="Inkspell Masters of Modern Marketing trophy" loading="lazy"><figcaption><span class="k">Inkspell · Masters of Modern Marketing · 2022</span><b>Best 360° Marketing Campaign</b><span>The Laughing Cow cheese sachet</span></figcaption></figure>

</div>
<div class="aw-grid">{awg}</div></div></section>'''
T = [("They don’t just give ads. They give direction.","I’ve had the opportunity to witness their work up close, and what stood out most was Nagessh Pannaswami’s clarity of thought and creative leaps. Nagessh’s ability to distil complex business problems into brand-led solutions is exceptional.","Saket Gore","General Manager, International Business","c-orange"),
 ("A sounding board for all things marketing.","Nagessh is more of a marketing strategist than the stereotypical ad man. His industry know-how, understanding of ground realities by sector and practical outlook made him a good sounding board for marketing, branding and communication strategy.","Deepa Arjunan","Sr. General Manager, Branding","c-teal"),
 ("No silos. Creative problem solving across the business.","They understand not only the brand requirements but also business challenges, and offer many areas of expertise to help us achieve our goals. They are open to engage in all aspects of business and orchestrate a great outcome.","Mustufa Arsiwalla","Marketing Group Manager","c-green")]
VT = [("VRJIscd8mz0","Piruz Khambatta","CMD, Rasna"),("D8j17BeSt2U","Mukund Bhogale","Former MD, Nirlep"),("YskB6GZKqV0","Mustufa Arsiwala","Marketing Group Manager, Bel Groupe (The Laughing Cow)")]
vt = "".join(f'<figure class="vt"><button class="vplay" type="button" data-yt="{i}" aria-label="Play testimonial from {n}"><img src="https://i.ytimg.com/vi/{i}/hqdefault.jpg" alt="" loading="lazy"><span class="pbtn" aria-hidden="true">▶</span></button><figcaption><b>{n}</b><span>{r}</span><a href="https://www.youtube.com/watch?v={i}" target="_blank" rel="noopener">Watch on YouTube ↗</a></figcaption></figure>' for i, n, r in VT)
tq = "".join(f'<figure class="quote {c}"><h3>{h}</h3><blockquote>{q}</blockquote><figcaption><b>{n}</b><span>/ {r}</span></figcaption></figure>' for h, q, n, r, c in T)
hm += f'''<section class="white"><div class="wrap">{head("testimonials", "Client stories", "Hear it from the people who hired us.")}<div class="vts">{vt}</div><div class="quotes" style="margin-top:14px">{tq}</div>
<div class="featured"><span>As featured in</span><b>BestMediaInfo</b><b>The Economic Times</b><b>Business Today</b><b>Campaign</b></div></div></section>'''
hm += faq_section(FAQ["index.html"], head, "Questions owners ask us", "white")
hm += close("Let’s talk. Work with us.", "Not sure which product fits? Start with the free Brand Audit, or tell us where growth is stuck and we’ll point you to one next step.", "Take the free Brand Audit", "brand-audit.html")

# ================================================================ AUDIT
au = hero("Brand-led · Brand Audit · Free",
  "Where your brand stands, and <span class=\"hl\">what it’s costing you.</span>",
  "You can feel it when <b>dealers decide what sells</b>, when every slow quarter ends in a scheme, when buyers can’t tell you from the next supplier. The Audit shows you what that costs, in your own answers and your own numbers.",
  [("Time", "about 10 min"), ("Questions", "20 yes/no + 3 written"), ("Cost", "free"), ("Email", "only after your score")],
  [("Start the audit", CONTACT, ""), ("How it works", "#how", "dark")], ("bell", "diya"))
au += f'''<section class="white" id="how"><div class="wrap">{head("the audit at a glance", "Four steps. Each gives you something to keep.")}
{stats([("c-flame","1 · Answer","10","minutes, 23 questions"),("c-teal","2 · See","0","seconds to your score"),("c-deep","3 · Report","8","deeper questions, then a written report"),("c-red","4 · Talk","1","agreed next step")])}</div></section>'''
au += f'''<section><div class="wrap">{head("what we measure", "Four areas, 40 points", "Conditioning and Signal carry the most points because that is where you have the most control. Pull is mostly an outcome, so you raise it by raising the other three.")}
<div class="areas">
<div class="area c-orange"><span class="v">8<small>PTS</small></span><h3>Dependence</h3><p>Who owns the demand. 4 questions.</p></div>
<div class="area c-green"><span class="v">12<small>PTS</small></span><h3>Conditioning</h3><p>What the market waits for. 6 questions.</p></div>
<div class="area c-purple"><span class="v">12<small>PTS</small></span><h3>Signal</h3><p>Whether your difference is visible. 6 questions, worded for your sector.</p></div>
<div class="area c-teal"><span class="v">8<small>PTS</small></span><h3>Pull</h3><p>How demand arrives. 4 questions.</p></div>
</div>
<div class="card" style="margin-top:16px"><p>You also write three short answers in your own words: one thing you gave up in the last twelve months to keep a customer, how you would finish <b class="hl">“Customers choose us because…”</b>, and what the person who takes over your business actually inherits.</p></div></div></section>'''
au += f'''<section class="white"><div class="wrap">{head("see where you stand", "Four tiers. Which one are you?", "You see your result before we ask for anything.")}
<div class="scale">
<div class="tier c-red"><span class="k">0–12</span><span class="nm">Replaceable</span><p>The market buys your rate. Demand belongs to the channel.</p></div>
<div class="tier c-orange"><span class="k">14–22</span><span class="nm">Compared</span><p>In the set, then judged on price like everyone in it.</p></div>
<div class="tier c-teal"><span class="k">24–30</span><span class="nm">Preferred</span><p>Chosen when you are in the room. Vulnerable when you are not.</p></div>
<div class="tier c-green"><span class="k">32–40</span><span class="nm">Requested</span><p>Asked for by name. Price is a detail, not the decision.</p></div>
</div></div></section>'''
au += f'''<section><div class="wrap">{head("your result page", "What you see, in order")}
<ol class="reveal">
<li><span>Your score and your tier</span></li>
<li><span>Four bars showing where you are strong and where you are not</span></li>
<li><span>Your two weakest areas, named, with what they cost you in margin, dealer power and pricing</span></li>
<li><span>Your own “Customers choose us because…” line, with one test: could your two largest rivals sign it and be telling the truth?</span></li>
<li><span>The concession you named, added up over a year, on the one account you told us about</span></li>
<li><span>How you compare with others in your sector, once enough owners have taken the audit</span></li>
<li><span>One next step</span></li>
</ol></div></section>'''
au += f'''<section class="white"><div class="wrap">{head("after your score", "The written report and the call")}<div class="phases">
{phase("c-purple","3","Deeper read","About 10 min","What is behind your score?",[
 "Share your email so we can send the written report",
 "Answer 8 short questions: how you describe your business, what happens if it shuts tomorrow, what you have tried, who else has to agree before anything changes, why you took the audit today, what three more years of no change looks like, what you would never change about how you make your product, and what competitors do that you privately think is wrong",
 "We read your answers before the call"],
 "A written report by email within two working days: score, tier, four areas, your two weakest areas and their cost, your own words, and what your answers point to",
 "Put one document in front of a partner, a son or a board","Confirm your call time", a="pigeon")}
{phase("c-red","4","Report call","30–45 min","What does this mean for your business, and what is the one thing to do next?",[
 "Go through the report with a Curry Nation founder","Test the diagnosis against what you see in your own business","Agree one next step, and only one"],
 "A short note after the call with the agreed next step","Know exactly what to do next, whether or not it is with us","You decide: go ahead, or not now", a="drum")}
</div></div></section>'''
au += f'''<section><div class="wrap">{head("how this works", "Plain terms")}
{terms([("Cost","Free, with no obligation."),("Your answers","Private. Used only to build your report and prepare for the call, and never shared. Sector figures come only from combined results, and only when there are enough of them."),("Your email","Asked for after you see your score, to send the written report."),("Who should answer","Ideally the person who knows your margins and dealer terms."),("Not included","A plan, prices, or a recommendation to buy anything. The audit shows where you stand. The call decides what to do."),("Limits","Twenty questions give a read of your business, not a full study of it.")])}</div></section>'''
au += faq_section(FAQ["brand-audit.html"], head, cls="white")
au += related("brand-audit.html") + close("Ten minutes to your score.", "No email until you have seen it. No pitch on the call unless you ask for one.", "Start the audit")

# ================================================================ POSITIONING
L3 = ["Commodity", "B2B", "Consumer"]
po = hero("Brand-led · Brand Positioning",
  "Answer “why you?” <span class=\"hl\">in one line.</span>",
  "When buyers can’t tell you from the next supplier, they choose on price. Brand Positioning finds the <b>reason to choose you that nobody in your category owns</b>, builds the proof behind it, and gives you a 90-day plan to launch it.",
  [("Phases", "3"), ("Full programme", "6 weeks"), ("Buy", "one phase or all three")],
  [("Let’s talk", CONTACT, ""), ("Not sure? Take the free Audit", "brand-audit.html", "dark")], ("chai", "elephant"))
po += f'''<section class="white"><div class="wrap">{head("programme overview", "Three phases. Each ends in one sign-off.")}
{glance(["Phase","You get","Your business can now","Time"],[
 ["1. Discover","Demand Atlas","Choose the position to own","2 wks"],["2. Define","Brand Platform","Answer “why you?” in one line","2 wks"],["3. Express","Route and Roadmap","Launch with one voice for 90 days","2 wks"]],
 ["Full programme","All three, one team, one kickoff","Go from strategy to launch, at 15% less than buying phases separately","6 wks"], "Fees are quoted per business, plus GST.")}</div></section>'''
po += f'''<section><div class="wrap"><div class="phases">
{phase("c-orange","1","Discover","2 weeks","Who chooses in this category, why, and which reasons does nobody own?",[
 "Interview your team and review your sales, pricing and past research","Map the category: rivals, channels, and how buyers judge quality today","Study buyers: when they choose, who decides, what they compare, and where trust breaks","Find the gaps: reasons to choose a brand that no competitor claims"],
 "Demand Atlas with 3–5 unclaimed reasons to choose you, and one recommended","Know who pays more and why, and which position is open","Your choice of position to build on",
 list(zip(L3,["value chain and margin map","8–12 buyer interviews and a lost-deal review","occasion and time-of-day map"])), a="bell")}
{phase("c-green","2","Define","2 weeks","Who are we for, what do we stand for, and why should anyone believe us?",[
 "Pick the target buyer and the need we serve","Define your role in the buyer’s world and the gap between you and rivals","Build the proof ladder: what you can show, certify or trace that others cannot","Write the Brand Key: belief, promise, personality","Test the platform against your product, pricing and sales reality"],
 "One-page Brand Platform: target, positioning, proof, Brand Key","Give one clear answer to “why you?” that your team, sales and partners can all repeat","Approved positioning",
 list(zip(L3,["proof and certification claims","benefit ladder from feature to business outcome","emotional benefit ladder"])), a="chai")}
{phase("c-purple","3","Express","2 weeks","How do we say it, and what do we do in the first 90 days?",[
 "Turn the platform into an insight and a reason to believe","Develop 2 creative routes with 3–5 lines each","Map what it means for your range, offer and channels","Build the 90-day launch and activation plan with owners and sequence"],
 "2 routes with a recommended line, plus a 90-day roadmap","Put a message on pack, site or pitch deck next week, with a plan to launch it","Approved route and roadmap",
 list(zip(L3,["name options, trust marks, channel plan","sales narrative, case-study frame, website messaging outline","consumer routes, range stretch"])), a="pigeon")}
</div></div></section>'''
po += f'''<section class="white"><div class="wrap">{head("terms", "How we work together")}
{terms([("Payment","Single phase: 50% at kickoff, 50% at sign-off. Full programme: 40% at kickoff, 30% at Phase 2 sign-off, 30% at final delivery."),("Adding a phase","Add the next phase within 45 days and part of the previous phase fee is credited against it."),("Where you can start","Define needs a Demand Atlas or your own buyer research, or a 3-day Rapid Demand Scan first. Express needs a documented positioning."),("Process","One lead strategist, a weekly call, one revision round per sign-off, feedback within three working days."),("What we need from you","One decision-maker as contact, access to sales data and past research, and 2–3 people for interviews."),("Not included","Logo and identity, packaging design, creative production, media and website build. We quote these separately."),*TAIL])}</div></section>'''
po += f'''<section><div class="wrap">{head("next steps", "Getting started")}{steps([("Pick your option","One phase or the full programme, and the lens that fits your business"),("Sign and pay","The kickoff instalment"),("We kick off","We send the intake form and book the kickoff")])}</div></section>'''
po += faq_section(FAQ["brand-positioning.html"], head)
po += related("brand-positioning.html") + close("Find the position nobody owns.", "Tell us about your business and we’ll recommend where to start.", "Let’s talk")

WK_OPTIONS = f'''<section class="white" id="options"><div class="wrap">{head("two ways to run it", "Challenger Workshop for Leadership, or for Business", "Same workshop day. The difference is how much evidence we gather before your team walks into the room.")}
<div class="options">
<div class="option c-red" id="leadership"><span class="k">For Leadership · 1 day + 1 week</span><h3>Challenger Workshop for Leadership</h3>
<p>Your founder and 8–10 functional heads in one room for a full day, agreeing the one problem to solve first, then a 90-day plan with named owners.</p>
<ul><li>Phase 2: Align, the workshop day</li><li>Phase 3: Commit, the Output Pack a week later</li><li>Our promise: no breakthrough, no fee</li></ul>
<p class="best"><b>Best if</b> you already have customer, trade or market research from the last six months that we can review.</p>
<div><a class="btn light" href="#day">See the day</a></div></div>
<div class="option c-deep" id="business"><span class="k">For Business · about 7 weeks</span><h3>Challenger Workshop for Business</h3>
<p>Five weeks of evidence from your customers, the trade and your rivals first, so the workshop settles arguments with facts, then the day and the 90-day plan.</p>
<ul><li>Phase 1: Investigate, 25 customer interviews, store safari, rival tear-down</li><li>Phase 2: Align, the workshop day</li><li>Phase 3: Commit, the Output Pack a week later</li></ul>
<p class="best"><b>Best if</b> growth has stalled and nobody can say for sure why.</p>
<div><a class="btn light" href="#investigate">See the evidence phase</a></div></div>
</div></div></section>'''

# ================================================================ WORKSHOP
slots = [("c-flame","09:00","Founder sets the challenge","The founder frames the problem and what is at stake, tied to sales, market share or product choice."),
 ("c-teal","09:30","Insight playback","We play back the Evidence Pack: customer pain, unmet needs, rival weaknesses, gaps to use."),
 ("c-purple","11:00","Challenger drills","Small groups test your assumptions and rewrite the message around what customers actually need."),
 ("c-green","14:00","Scenario boards","Groups compare positioning, pricing and promotion scenarios and their likely sales outcomes."),
 ("c-orange","15:45","Go-to-market canvas","Map how you will launch and sell, then score each action on impact, confidence and ease."),
 ("c-red","17:15","Pitch-back and verdict","Teams present their plans. The founder gives a verdict and commits to the plan.")]
day = "".join(f'<div class="slot {c}"><time>{t}</time><h3>{h}</h3><p>{p}</p></div>' for c, t, h, p in slots)
wk = hero("Brand-led · Challenger Workshop for Business (UNLIMIT)",
  "One problem. One plan. <span class=\"hl\">One aligned team.</span>",
  "Share has plateaued. Rivals with weaker products are winning trade preference. Your leadership team doesn’t agree on what comes next. <b>UNLIMIT puts facts in the room, gets everyone behind one problem, and leaves you with a 90-day plan</b> with named owners.",
  [("Evidence", "5 weeks"), ("Workshop", "1 day, 09:00–18:00"), ("Plan", "1 week after")],
  [("Let’s talk", CONTACT, ""), ("See the five weeks of evidence", "#investigate", "dark")], ("drum", "elephant"))
wk += f'''<section class="white" id="options"><div class="wrap"><div class="card"><p>Already know the one problem you need solved? The <a class="hl" href="leadership-workshop.html"><b>Challenger Workshop for Leadership</b></a> starts with it: two days at an offsite where senior operators challenge each decision-maker, then the team agrees a plan.</p></div></div></section>'''
wk += f'''<section class="white"><div class="wrap">{head("the programme at a glance", "Three phases. Each ends in one sign-off.", "Five weeks of evidence, one workshop day, and the plan a week later.")}
{glance(["Phase","You get","Your business can now","Time"],[
 ["1. Investigate","Evidence Pack","See your business through your customers’, the trade’s and your rivals’ eyes","5 wks"],["2. Align","One priority problem, agreed in the room","Agree the one problem to solve first, with your whole leadership team","1 day"],["3. Commit","Output Pack","Start a 90-day plan with named owners and measures","1 wk after"]], None,
 "Fees quoted per business, plus GST. Venue, travel and boarding at actuals.")}</div></section>'''
wk += f'''<section id="investigate"><div class="wrap"><div class="phases">{phase("c-deep","1","Investigate","5 weeks","What are customers, the trade and rivals telling us that the leadership team has not heard?",[
 "<b>Customer voice (2 weeks).</b> 25 interviews with current and lapsed customers: why they buy, why they left, what they wish you did.",
 "<b>Store and channel safari (1 week).</b> Mystery-shop your outlets and your key rivals’: how products are shown, priced and pitched.",
 "<b>Rival tear-down (1 week).</b> Decode how rivals communicate, package, price and promote, and find what none of them claims.",
 "<b>Synthesis (1 week).</b> One story of what is holding sales back, with 3–5 candidate problems for the day."],
 "Evidence Pack: findings from all four pieces of work, plus the workshop pre-read","Settle arguments in the room with facts, not opinions","Agree the workshop brief and the challenge for the day", a="bell")}</div></div></section>'''
wk += f'''<section class="white" id="day"><div class="wrap">{head("phase 2 · align", "The workshop day", "Of all the problems we could solve, which one matters most, and is the whole team behind it?")}
<div class="day">{day}</div>
<p class="note">Tools: Miro board, role-play cards, challenger prompt deck, live sketching. Venue: a hotel conference room in your city, booked by you.</p></div></section>'''
wk += f'''<section><div class="wrap">{head("who is in the room", "Your leaders, our team, and fresh eyes")}
{stats([("c-orange","Your side","8–10","founder or MD plus functional heads"),("c-teal","Curry Nation","8–10","strategy, creative, media, customer experience"),("c-purple","Fresh eyes","5–6","outside-category consultant, Gen-Z shoppers"),("c-red","Outcome","1","priority problem, agreed in the room")])}</div></section>'''
wk += f'''<section class="white"><div class="wrap"><div class="phases">{phase("c-green","3","Commit","1 week after","What do we do in the next 90 days, and who owns what?",[
 "Turn the top-voted ideas into 3 campaign directions across advertising, in-store and on-ground, and niche trade channels","Write the Challenger Positioning Snapshot on one page","Build the 90-day quick-win roadmap with owners, sequence and the measures to track","Photograph and compile every canvas from the day"],
 "Output Pack: problem statement, Challenger Positioning Snapshot, 3 campaign directions, 90-day roadmap with owners and measures, photo record of every canvas","Start the next Monday with one plan, named owners and measures","Approved roadmap", a="diya")}</div></div></section>'''
wk += '''<section><div class="wrap"><div class="promise c-red"><p class="eyebrow" style="color:#fff">our promise</p><h2 class="display">No breakthrough, no fee.</h2>
<p>At the end of the day, after every team has presented, you decide. If you don’t see at least one breakthrough idea you’re ready to put in your 90-day plan, tell us within 30 minutes and we refund the fee, except venue and third-party costs. The decision has to be made on the day.</p></div></div></section>'''
wk += f'''<section class="white"><div class="wrap">{head("terms", "How we work together")}
{terms([("Payment","40% at kickoff, 40% at Phase 1 sign-off, 20% after your verdict on the day."),("Where you can start","If you’ve done our Brand Positioning programme recently, Phase 1 becomes a two-week top-up."),("Process","The Curry Nation founders lead the workshop. One lead strategist, a weekly call during Phase 1, one revision round on the Output Pack, feedback within three working days."),("What we need from you","The founder or MD and 8–10 functional heads for the full day, contacts for 25 current and lapsed customers, access to outlets, sales and pricing data, one contact person, and the venue booked."),("Not included","Logo and visual identity, packaging design, content and ad production, media buying, website build, and execution after the 90-day plan. We quote these separately."),*TAIL])}</div></section>'''
wk += faq_section(FAQ["challenger-workshop.html"], head, cls="white")
wk += related("challenger-workshop.html") + close("Get your team behind one problem.", "Tell us where growth has stalled. We’ll tell you which workshop fits.", "Let’s talk")

# ================================================================ FOUNDER VISIBILITY (v8: package-first)
EMAIL = "challengeus@currynation.in"
fv = hero("Founder-led · The Visible Founder Authority System",
  "Founder authority creates <span class=\"hlp\">context before contact.</span>",
  "Four packages that turn what the founder knows into visible proof, so buyers, partners and hires arrive already knowing why the founder matters. <b>Start with the Audit. Continue only if it makes business sense.</b>",
  [("Start with", "the Audit"), ("Audit fee", "₹5,000"), ("Delivery", "10 working days")],
  [("Compare the packages", "#packages", ""), ("Book the Audit", f"mailto:{EMAIL}?subject=Founder%20Authority%20Audit", "dark")], ("pigeon", "diya"))

fv += '''<nav class="pagenav" aria-label="On this page"><div class="wrap">
<a href="#compare">Compare</a><a href="#packages">Packages</a><a href="#fit">Is it for you?</a><a href="#how">How it works</a><a href="#addons">Add-ons</a><a href="#faq">FAQ</a></div></nav>'''

PK = [
 ("audit", "1", "c-purple", "Founder Authority Audit", "₹5,000", "10 working days",
  "Where does the founder’s authority stand today?",
  "Scorecard, diagnosis, 90-day opportunity map and a 45-minute readout",
  "You want evidence before investing"),
 ("plan", "2", "c-slate", "Action Plan", "On call", "About 2 weeks",
  "What should we build, and in what order?",
  "Category lens, audience, channel choices and a 90-day roadmap",
  "The founder has little or no presence yet"),
 ("build", "3", "c-deep", "System Build", "On call", "4 weeks",
  "What should the founder stand for and say?",
  "Positioning, narrative, content system, profile and an AI workspace you own",
  "You’re ready to commit to a clear point of view"),
 ("implement", "4", "c-teal", "Implement", "DIY · Guided · Managed", "From 30 days",
  "Who runs it, week to week?",
  "Your team, your team with our support, or a managed monthly rhythm",
  "The system is built and approved"),
]
fv += cmp_section("compare", "Four packages, side by side", "Only the Audit is priced up front. Every later package is scoped on a call once the Audit shows what the founder needs.", FOUNDER, head, cls="")
fv += pkg_section("the packages", "Four packages. Each one stands alone.", "Only the Audit is priced up front. Every later package is scoped on a call once the Audit shows what the founder needs. Proceed within 14 days and the ₹5,000 is credited to the next package.", FOUNDER, head)

fv += f'''<section class="white" id="fit"><div class="wrap">{head("is it for you?", "Built for founders whose business is ahead of their public authority", "The test: if a qualified buyer has to meet the founder before understanding why the founder matters, the authority system is under-built.")}
<div class="fit"><div class="yes"><h3>A strong fit</h3><ul>
<li>Owner-managed and promoter-led businesses</li><li>B2B, manufacturing or commodity categories where trust matters</li><li>Regional businesses entering new markets</li><li>Founders seeking customers, talent, partners or media credibility</li></ul></div>
<div class="no"><h3>Not the right fit</h3><ul>
<li>Anyone looking only for viral content or follower growth</li><li>Founders unwilling to share experience or approve a clear point of view</li><li>Businesses expecting guaranteed leads, sales or media coverage</li><li>Teams looking for a low-cost posting service</li></ul></div></div></div></section>'''

fv += f'''<section id="how"><div class="wrap">{head("how it works", "Extract. Position. Publish. Convert.", "Progress shows up as decisions and usable assets before it shows up as market outcomes. Here is a typical first 90 days.")}
<div class="day four">
<div class="slot c-purple"><time>Days 1–10</time><h3>Extract</h3><p>Audit: capture the founder’s experience, beliefs and proof. Scorecard and gaps.</p></div>
<div class="slot c-slate"><time>Days 11–25</time><h3>Position</h3><p>Action Plan: choose the idea, audience and channels the founder should own.</p></div>
<div class="slot c-deep"><time>Days 26–55</time><h3>Publish</h3><p>System Build: narrative, profile and a repeatable content system.</p></div>
<div class="slot c-teal"><time>Days 56–90</time><h3>Convert</h3><p>Implement: a first publishing rhythm that supports meetings, partnerships and demand.</p></div>
</div></div></section>'''

ADD = [("Book", "Concept, interviews, writing and launch support"), ("Podcast", "Format, identity, guest strategy and production plan"), ("PR + speaking", "Narratives, media angles, award and event support"), ("Webinar", "Topic, script, landing page and follow-up assets"), ("Lead assets", "Landing pages, lead magnets and conversion copy"), ("Appointments", "Founder-led outreach and meeting support")]
fv += f'''<section class="white" id="addons"><div class="wrap">{head("add-ons", "Optional authority assets", "Scoped separately after the Action Plan, only where they matter for this founder. Production, travel, paid media and vendors are billed at actuals.")}
<div class="addons">{"".join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in ADD)}</div></div></section>'''

FV_FAQ = [
 ("Why does founder visibility matter for the business?", "Visibility works when the founder makes expertise, values and category beliefs easier for the market to recognise. Nithin Kamath (Zerodha) made the thinking behind his company accessible through education and transparency. Aman Gupta gave boAt a recognisable human voice. Ghazal Alagh’s personal problem became Mamaearth’s brand story. These examples show the mechanism; they don’t guarantee growth."),
 ("How is pricing decided?", "Only the Audit is priced before the first call, at ₹5,000. Every later package is scoped and priced once the Audit shows what the founder actually needs. Proceed within 14 days and the Audit fee is credited against the next agreed package."),
 ("Do I have to buy all four packages?", "No. Each package stands alone and gives you something useful. Most founders start with the Audit; a founder with no real presence yet may start with the Action Plan."),
 ("What does the founder need to give?", "Honest access to their experience and proof, and approval of a clear point of view. For the managed rhythm, one structured 90-minute interview and timely approvals each month."),
 ("Who owns the work?", "You do. The strategy, copy, prompts and working files created during the engagement are yours, whether your team runs the system or we continue with you."),
 ("What isn’t guaranteed?", "Reach, leads, meetings, media coverage and revenue. The system turns substance into visibility. It cannot manufacture substance that isn’t there."),
 ("Why Curry Nation?", "Positioning comes before posting. We are built for owner-managed companies where trust sits with the promoter, we start from what the market must understand rather than a calendar of random topics, and we keep essential work separate from optional projects and third-party costs."),
]
fv += f'''<section id="faq"><div class="wrap">{head("faq", "Questions founders ask")}
<div class="faq">{"".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in FV_FAQ)}</div>
<div class="card" style="margin-top:14px"><p>Already visible, but the business still sells on price? <a class="hl" href="brand-audit.html"><b>Take the free Brand Audit</b></a> to see where the company stands.</p></div></div></section>'''
fv += related("founder-visibility.html")
fv += f'''<section class="close" id="enquire"><div class="wrap"><p class="eyebrow">next step</p><h2 class="display">Start with evidence.</h2>
<p>The Audit shows where the founder stands, what’s missing and whether the next investment makes business sense. No retainer required.</p>
<div class="chips"><span>Fee <b>₹5,000</b></span><span>Delivery <b>10 working days</b></span><span>Email <b class="sel">{EMAIL}</b></span></div>
<div class="ctas"><a class="btn" href="mailto:{EMAIL}?subject=Founder%20Authority%20Audit">Book the Founder Authority Audit</a><a class="btn dark" href="{CONTACT}">Work with us</a></div></div></section>'''

FV_JS = r'''<script>(function(){
var tabs=[].slice.call(document.querySelectorAll('[role=tab]'));if(!tabs.length)return;
function show(k,scroll){var t=document.getElementById('t-'+k);if(!t)return false;
tabs.forEach(function(b){var on=b===t;b.setAttribute('aria-selected',on?'true':'false');document.getElementById(b.getAttribute('aria-controls')).hidden=!on});
if(scroll){document.getElementById('covered').scrollIntoView({behavior:'smooth',block:'start'})}return true}
tabs.forEach(function(b,i){b.addEventListener('click',function(){show(b.id.slice(2))});b.addEventListener('keydown',function(e){var d=e.key==='ArrowRight'?1:e.key==='ArrowLeft'?-1:0;if(d){var n=tabs[(i+d+tabs.length)%tabs.length];n.focus();n.click()}})});
document.querySelectorAll('[data-tab]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();show(a.getAttribute('data-tab'),true);history.replaceState(null,'','#'+a.getAttribute('data-tab'))})});
function fromHash(){var h=location.hash.replace('#','').replace('tab-','');if(['audit','plan','build','implement'].indexOf(h)>-1){show(h);setTimeout(function(){document.getElementById('covered').scrollIntoView({block:'start'})},50)}}
fromHash();window.addEventListener('hashchange',fromHash);
})();</script>'''

# ================================================================ PERFORMANCE-LED
PERF_EMAIL = "nagesshp@currynation.in"
PERF_PHONE = "+91 92235 02716"
pf = hero("Performance-led · Curry Nation Growth Lab",
  "Turn product demand into <span class=\"hl\">profitable growth.</span>",
  "Performance marketing for <b>₹100–300 Cr product businesses</b> that want to grow beyond discounts. We connect media, marketplaces and customer demand, and judge every rupee by what it adds to contribution.",
  [("Approach", "Strategy × Media × Commerce"), ("Measured on", "contribution, not applause")],
  [("Try the growth planner ↗", PLANNER, ""), ("See the packages", "#packages", "dark")], ("diya", "chai"))
_SI = _json.load(open(PARTS + "/platform_icons.json"))
def _plat(name, dom=None):
    if not dom and name in _SI:
        hx, d = _SI[name]
        ic = f'<svg viewBox="0 0 24 24" role="img" aria-hidden="true"><path fill="#{hx}" d="{d}"/></svg>'
    else:
        ic = f'<img src="https://www.google.com/s2/favicons?domain={dom}&sz=128" alt="" loading="lazy" width="44" height="44">'
    return f'<div class="plat">{ic}<span>{name}</span></div>'
plats = "".join(_plat(n, d) for n, d in [("Meta",None),("Google",None),("Amazon",None),("Flipkart",None),("Meesho","meesho.com"),("Blinkit","blinkit.com"),("Zepto","zeptonow.com"),("Zomato","zomato.com"),("Myntra","myntra.com"),("LinkedIn",None)])
pf += f'''<section class="white"><div class="wrap"><p class="eyebrow" style="text-align:center">Platforms we connect</p><div class="plats">{plats}</div></div></section>'''

pf += f'''<section><div class="wrap">{head("the difference", "Sales are growing. Is your brand growing with them?", "A sale isn’t a win if fees, returns or discounts eat the profit. Advertising has to answer to availability, conversion and margin.")}
<div class="gap">
<div class="c-teal"><span class="n">01</span><p>Demand created, not just captured from people already searching for you</p></div>
<div class="c-deep"><span class="n">02</span><p>SKU and market economics, not blended vanity metrics</p></div>
<div class="c-slate"><span class="n">03</span><p>Media decisions steered by inventory and margin</p></div>
</div></div></section>'''
CH = [("c-flame","Meta Ads","Create demand before search","Prospecting, creative testing, Conversions API, catalogues, remarketing and click-to-WhatsApp.","Qualified conversations · incremental reach · creative fatigue"),
 ("c-teal","Google Ads","Capture demand with context","Search intent, negative keywords, Performance Max governance, Merchant Center feeds, location signals and value rules.","Search share · qualified conversions · marginal acquisition cost"),
 ("c-orange","Marketplace media","Amazon, Flipkart, Meesho","Listing readiness, SKU unit economics, sponsored placements, query harvesting and inventory-aware bidding.","TACoS · contribution after fees · new-to-brand orders"),
 ("c-green","Quick commerce & food","Blinkit, Zepto, Zomato","Assortment, in-app sponsored shelves, city demand pockets and basket attach.","In-stock rate · basket share · city-level contribution"),
 ("c-purple","Category & B2B media","Myntra, LinkedIn","Activated only where product and buyer fit: Myntra for fashion and lifestyle, LinkedIn for considered B2B demand.","Qualified enquiries · product discovery · contribution")]
chs = "".join(f'<div class="chan {c}"><span class="k">{f}</span><h3>{n}</h3><p>{d}</p><p class="sig"><b>Signals we track</b>{s}</p></div>' for c, n, f, d, s in CH)
pf += f'''<section class="white" id="services"><div class="wrap">{head("services", "From discovery to delivery. One connected growth plan.", "No platform is in the plan just to fill a media plan. Each one has a job and the signals that prove it’s doing it.")}
<div class="channels">{chs}</div>
<div class="chain"><span>Creative</span><i>→</i><span>Availability</span><i>→</i><span>Conversion</span><i>→</i><span>Repeat</span><i>→</i><span class="end">Contribution</span></div>
<p class="note" style="text-align:center">What happens after the click is the strategy.</p></div></section>'''
pf += f'''<section id="method"><div class="wrap">{head("method", "Plan. Test. Learn. Then scale what works.")}
<div class="day four">
<div class="slot c-teal"><time>01</time><h3>Map</h3><p>Find profitable pockets using margins, SKU mix, geography, stock, occasions, search demand and channel conflict.</p></div>
<div class="slot c-deep"><time>02</time><h3>Instrument</h3><p>Make the signal trustworthy with events, UTMs, Conversions API, feeds and consent-aware measurement.</p></div>
<div class="slot c-slate"><time>03</time><h3>Test</h3><p>Treat creative as a hypothesis: offers, language, audiences, landing paths and placements, by market cluster.</p></div>
<div class="slot c-flame"><time>04</time><h3>Scale</h3><p>Move money by incremental contribution, not in-platform ROAS, and feed sales and stock data into the next sprint.</p></div>
</div></div></section>'''
pf += f'''<section class="planner-band" id="planner"><div class="wrap planner-grid">
<div><p class="eyebrow light">growth studio</p><h2 class="display">Model the month before you spend it.</h2>
<p class="sub">Pick an industry, objective, platform, market tier, focus cities, budget and order value. The planner estimates reach, visits, potential orders and gross order value.</p>
<div class="ctas" style="justify-content:flex-start"><a class="btn" href="{PLANNER}" target="_blank" rel="noopener">Open the growth planner ↗</a></div>
<p class="fine">A planning estimate, not a guarantee. Revenue shown is gross order value, not profit. Fees, returns and stock-outs are excluded.</p></div>
<div class="scenario"><p class="sk">Sample scenario · Meta Ads · Tier 2 cities · 30 days · ₹3,00,000 media</p>
<div class="sgrid">
<div><span class="v">9.5 L</span><span>people reached · 3.1 frequency</span></div>
<div><span class="v">27.3 L</span><span>impressions</span></div>
<div><span class="v">28,964</span><span>estimated visits · ₹10 per visit</span></div>
<div><span class="v">1,318</span><span>potential orders · ₹228 per action</span></div>
<div><span class="v">₹34.3 L</span><span>illustrative gross order value</span></div>
<div><span class="v">11.4×</span><span>value to media spend</span></div>
</div></div></div></section>'''
pf += cmp_section("compare", "Three packages, side by side", "Fees are tailored after a discovery call. Media spend is always kept separate.", PERF_PK, head, cls="")
pf += pkg_section("packages", "The right support for your next growth stage", "Fees are tailored after a discovery call. Media spend, production and platform fees are scoped separately.", PERF_PK, head, cls="white")
pf += faq_section(FAQ["performance.html"], head)
pf += related("performance.html")
pf += f'''<section class="close" id="enquire"><div class="wrap"><p class="eyebrow">let’s talk</p><h2 class="display">Tell us where growth gets stuck.</h2>
<p>Share your category, current monthly media spend and the growth problem you want solved. We’ll suggest a Growth Audit, Market Launch or Scale Partnership, or tell you it’s too early.</p>
<div class="chips"><span>Email <b class="sel">{PERF_EMAIL}</b></span><span>Phone <b class="sel">{PERF_PHONE}</b></span></div>
<div class="ctas"><a class="btn" href="mailto:{PERF_EMAIL}?subject=Growth%20enquiry">Start a conversation</a><a class="btn dark" href="{PLANNER}" target="_blank" rel="noopener">Try the planner ↗</a></div>
<p class="note">Strategy before spend. Contribution before applause.</p></div></section>'''

# ================================================================ DESIGN-LED
dz = hero("Design-led",
  "Look like the brand <span class=\"hl\">you’re becoming.</span>",
  "Once you know what you stand for, it has to show up on the pack, the shelf, the screen and the dealer counter. Design-led work turns your positioning into a <b>brand identity and packaging</b> people recognise before they read a word.",
  [("Covers", "brand identity · packaging"), ("Built on", "an approved positioning")],
  [("Let’s talk", CONTACT, ""), ("See our work", "work.html", "dark")], ("bell", "elephant"))
dz += f'''<section class="white"><div class="wrap">{head("the problem", "When it looks like a commodity, it gets priced like one")}
<div class="gap">
<div class="c-orange"><span class="n">01</span><p>On the shelf, your pack looks like the three next to it, so the cheapest one wins</p></div>
<div class="c-flame"><span class="n">02</span><p>With the trade, your catalogue and counter material don’t justify a better margin</p></div>
<div class="c-red"><span class="n">03</span><p>On screen, every channel looks like it came from a different company</p></div>
</div></div></section>'''
dz += cmp_section("compare", "Two products, side by side", "Both start from an approved positioning, and both are scoped on a call.", DESIGN_PK, head, cls="")
dz += pkg_section("products", "What each one covers", None, DESIGN_PK, head, cls="white")
dz = dz.replace('<span class="n">1</span><h3>Brand Identity System', '<span class="n" id="identity">1</span><h3>Brand Identity System').replace('<span class="n">2</span><h3>Packaging', '<span class="n" id="packaging">2</span><h3>Packaging').replace('<span class="n">3</span><h3>Communication Design', '<span class="n" id="communication">3</span><h3>Communication Design')
dz += f'''<section class="white"><div class="wrap">{head("how we work", "Strategy first, then design")}
{terms([("Starts from positioning","Design-led work needs an approved positioning, from our Brand Positioning programme or your own. Otherwise we start with a short positioning check."),("Scope and fees","Each product is scoped and priced on a call, once we know your range, channels and rollout."),("Production","Printing, shoots, studios, media and external vendors are billed at actuals, with your approval first."),*TAIL])}
<div class="card" style="margin-top:14px"><p>Want to see the work first? Browse packaging, print, film and digital for Rasna, Nirlep, Chipseez, Emami and more on <a class="hl" href="work.html"><b>our work page</b></a>.</p></div></div></section>'''
dz += faq_section(FAQ["design.html"], head, cls="white")
dz += related("design.html") + close("Make the brand impossible to mistake.", "Tell us what you sell and where it’s sold. We’ll recommend where design will move the price first.", "Let’s talk")

# ================================================================ LEADERSHIP-LED · CHALLENGER WORKSHOP FOR LEADERSHIP
cx = hero("Brand-led · Challenger Workshop for Leadership",
  "One problem. <span class=\"hl\">Every decision-maker in the room.</span>",
  "The founder gives us one problem. Over two days at an offsite, <b>senior operators matched to each of your functions challenge your decision-makers on it</b>, then the team works it through and agrees one way forward, with the founder in the room.",
  [("Format", "2-day offsite"), ("Starts with", "one problem from the founder"), ("Leaves with", "a 90-day plan")],
  [("How it works", "#days", ""), ("Let’s talk", CONTACT, "dark")], ("drum", "pigeon"))
cx += f'''<section class="white" id="days"><div class="wrap">{head("how it works", "Audit the problem on Day 1. Solve it on Day 2.", "Two days, one problem: first every function is challenged on it by someone who has run that function, then the team works it through and decides.")}
<div class="day four">
<div class="slot c-slate"><time>Before</time><h3>One problem</h3><p>The founder gives us one problem statement. Sensitive topics are flagged and ground rules set.</p></div>
<div class="slot c-green"><time>Day 1</time><h3>Challenge</h3><p>Each decision-maker is challenged on the problem by a senior operator matched to their function, with the founder and the rest of the team in the room.</p></div>
<div class="slot c-purple"><time>Evening</time><h3>Downtime, by design</h3><p>People open up on Day 2 because they spent Day 1 being challenged together.</p></div>
<div class="slot c-red"><time>Day 2</time><h3>Solve</h3><p>Challenger drills and scenario boards on the problem. Teams pitch their plans, and the founder gives a verdict.</p></div>
</div></div></section>'''
cx += f'''<section><div class="wrap">{head("who’s in the room", "Your decision-makers. Our operators.")}
{stats([("c-green","Founder or MD","1","sets the problem, gives the verdict"),("c-orange","Decision-makers","5–8","the heads who will have to deliver the answer"),("c-teal","Senior operators","5","one matched to each function, briefed on your category"),("c-red","Coordinating lead","1","runs the two days and owns the plan")])}</div></section>'''
cx += pkg_section("the package", "What’s included", None, LEAD, head, cls="white")
cx += '''<section><div class="wrap"><div class="promise c-green"><p class="eyebrow light">the venue</p><h2 class="display">Always offsite. Never your boardroom.</h2>
<p>Choose from our shortlist of partner properties. The distance from the office is deliberate: people say things at a resort they would not say in their own boardroom.</p></div></div></section>'''
cx += f'''<section class="white"><div class="wrap">{head("terms", "How we work together")}
{terms([("Payment","50% at kickoff, 50% on the day."),("Included","The senior operators, venue and coordination from our shortlist, and meals for both days."),("Not included","Your team’s travel to the venue, rooms or guests beyond the agreed list, alcohol, and execution after the 90-day plan."),("What we need from you","The founder for both days, one problem statement, 5–8 decision-makers for both days, one contact person, and sensitive topics flagged in advance."),("Confidentiality","Nothing said in the room leaves it without agreement. Case references stay anonymised unless you agree in writing."),("Ownership","The plan and findings are yours on full payment. We may reuse anonymised learnings and our method.")])}</div></section>'''
cx += faq_section(FAQ["leadership-workshop.html"], head)
cx += related("leadership-workshop.html") + close("Bring us one problem.", "Tell us the problem and who has to solve it. We’ll match the panel.", "Let’s talk")

c2 = hero("Brand-led · Commodity to Brand",
  "From bought on rate to <span class=\"hl\">asked for by name.</span>",
  "Four packages for owner-managed businesses that buyers compare on price. <b>Start with the free Audit</b>, then find the position nobody owns, then get your leadership team behind it.",
  [("Start with", "the free Audit"), ("Packages", "4"), ("Each one", "stands alone")],
  [("See the packages", "#packages", ""), ("Take the free Audit", "brand-audit.html", "dark")], ("elephant", "bell"))
c2 += cmp_section("compare", "Four packages, side by side", "Each package stands alone. Start where your business is today.", BRAND, head)
c2 += pkg_section("the packages", "Four packages. Diagnose, position, align.", "Each package stands alone. Start where your business is today and move up only when the evidence makes the case.", BRAND, head)
c2 += faq_section(FAQ["brand-led.html"], head, cls="white")
c2 += related("brand-led.html") + close("Find out where your brand stands.", "Ten minutes, twenty questions, and your score before we ask for anything.", "Take the free Brand Audit", "brand-audit.html")

SPEC = [
 ("about.html","About Us · Curry Nation","India’s only brand transformation partner focused exclusively on owner-managed commodity businesses: mission, values, team and awards.",co.about_page()),
 ("work.html","Our Work · Curry Nation","Campaigns and brands built by Curry Nation across commodity, retail, FMCG, food and media.",co.work_page() + co.WORK_JS),
 ("resources.html","Free Resources · Curry Nation","Free e-books, templates and case studies for owner-managed commodity businesses.",co.resources_page() + co.RES_JS),
 ("contact.html","Contact Us · Curry Nation","Talk to Curry Nation: Pinnacle Business Park, Andheri (E), Mumbai.",co.contact_page() + co.CONTACT_JS),
 ("brand-led.html","Commodity to Brand · Curry Nation","Brand-led packages: Brand Audit, Brand Positioning, and the Challenger Workshops for Leadership and for Business.",c2),
 ("index.html","Curry Nation · We grow ambitious owner-managed businesses","Growth and outcome-based products: brand-led, founder-led, performance-led and design-led.",hm),
 ("brand-audit.html","Brand Audit · Curry Nation","A free ten-minute audit that shows where your brand stands and what it is costing you.",au),
 ("brand-positioning.html","Brand Positioning · Curry Nation","A three-phase, six-week programme to find and launch a position nobody in your category owns.",po),
 ("challenger-workshop.html","Challenger Workshop for Business · Curry Nation","UNLIMIT: five weeks of customer, trade and rival evidence, a workshop day, and a 90-day plan.",wk),
 ("founder-visibility.html","Founder Authority System · Curry Nation","The Visible Founder Authority System: Audit, Action Plan, System Build, Implement.",fv),
 ("performance.html","Growth Lab · Curry Nation","Performance marketing that turns product demand into profitable growth.",pf),
 ("design.html","Design-led · Curry Nation","Brand identity and packaging design built on your positioning.",dz),
 ("leadership-workshop.html","Challenger Workshop for Leadership · Curry Nation","The founder brings one problem. A two-day offsite where senior operators challenge your decision-makers on it, and the team agrees a 90-day plan.",cx),
]
for f, t, d, b in SPEC: open(os.path.join(OUT, f), "w").write(doc(f, t, d, b))
shutil.copytree(os.path.join(HERE, "assets"), os.path.join(OUT, "assets"))
open(os.path.join(OUT, "cxo-audit.html"), "w").write('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Challenger Workshop for Leadership · Curry Nation</title><meta http-equiv="refresh" content="0; url=leadership-workshop.html"><link rel="canonical" href="leadership-workshop.html"></head><body><a href="leadership-workshop.html">Challenger Workshop for Leadership</a></body></html>')
for x in ("logo.png", "vercel.json"): shutil.copy(os.path.join(HERE, x), OUT)
print("ok")
