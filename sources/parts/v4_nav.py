# ================================================================ V4 NAV (cascading)
PLANNER = "https://currynation-performance.arup-5d2.workers.dev/#planner"
MENU = [
 ("Brand-led", "brand", "When buyers can’t tell you from the next supplier", [
   ("brand-audit.html", "Brand Audit", "Free · about 10 minutes"),
   ("brand-positioning.html", "Brand Positioning", "3 phases · 6 weeks"),
   ("challenger-workshop.html#leadership", "Challenger Workshop for Leadership", "1 day in the room + 90-day plan"),
   ("challenger-workshop.html#business", "Challenger Workshop for Business", "5 weeks of evidence + workshop + plan")]),
 ("Founder-led", "founder", "When the business is ahead of the founder’s authority", [
   ("founder-visibility.html#audit", "Founder Authority Audit", "₹10,000 · 10 working days"),
   ("founder-visibility.html#plan", "Action Plan", "What to build, and in what order"),
   ("founder-visibility.html#build", "System Build", "4 weeks to a position and content system"),
   ("founder-visibility.html#implement", "Implement", "DIY, guided or managed")]),
 ("Performance-led", "performance", "When sales grow but profit doesn’t", [
   ("performance.html#growth-audit", "Growth Audit", "3–4 weeks · fixed scope"),
   ("performance.html#market-launch", "Market Launch", "90-day managed pilot"),
   ("performance.html#scale", "Scale Partnership", "Ongoing · tailored scope"),
   (PLANNER, "Growth Planner ↗", "Model reach, visits and orders")]),
 ("Design-led", "design", "When you look like a commodity on shelf and screen", [
   ("design.html#identity", "Identity System", "Logo, visual system, guidelines"),
   ("design.html#packaging", "Packaging & Shelf", "Packs, labels, point of sale"),
   ("design.html#communication", "Communication Design", "Print, film, digital")]),
 ("Leadership-led", "leadership", "When the founder hears only what’s safe to say", [
   ("cxo-audit.html", "CXO Audit", "Two-day offsite · 5 senior operators")]),
]

def header(cur):
    items = ""
    for name, key, line, subs in MENU:
        here = any(h.split("#")[0] == cur for h, _, _ in subs)
        links = "".join(
            f'<a href="{h}"{" target=\"_blank\" rel=\"noopener\"" if h.startswith("http") else ""}><b>{t}</b><small>{s}</small></a>'
            for h, t, s in subs)
        items += f'''<li class="m{" here" if here else ""}"><button class="mt" type="button" aria-expanded="false">{name}<i aria-hidden="true">▾</i></button>
<div class="sub"><p class="sub-k">{line}</p>{links}<a class="all" href="index.html#{key}">See all {name} products →</a></div></li>'''
    return f'''<header class="top" id="top"><div class="wrap">
<a class="logo" href="index.html" aria-label="Curry Nation home"><img src="logo.png" alt="Curry Nation" width="64" height="64"></a>
<nav class="nav" id="mainnav" aria-label="Products"><ul class="menu"><li class="m solo"><a class="mt" href="index.html"{" aria-current=\"page\"" if cur=="index.html" else ""}>Home</a></li>{items}</ul></nav>
<a class="btn cta-top" href="{CONTACT}">Let’s Connect</a>
<button class="burger" type="button" aria-controls="mainnav" aria-expanded="false"><span></span>Menu</button>
</div></header>'''

NAVJS = r'''<script>(function(){
var ms=document.querySelectorAll('.m:not(.solo)');
function shut(x){x.classList.remove('open');var b=x.querySelector('.mt');if(b)b.setAttribute('aria-expanded','false')}
ms.forEach(function(li){var b=li.querySelector('.mt');b.addEventListener('click',function(e){e.stopPropagation();var o=!li.classList.contains('open');ms.forEach(shut);if(o){li.classList.add('open');b.setAttribute('aria-expanded','true')}})});
document.addEventListener('click',function(e){if(!e.target.closest('.m'))ms.forEach(shut)});
document.addEventListener('keydown',function(e){if(e.key==='Escape')ms.forEach(shut)});
var bg=document.querySelector('.burger'),hd=document.querySelector('.top');
if(bg)bg.addEventListener('click',function(){var o=hd.classList.toggle('navopen');bg.setAttribute('aria-expanded',o?'true':'false')});
document.querySelectorAll('.sub a').forEach(function(a){a.addEventListener('click',function(){hd.classList.remove('navopen');ms.forEach(shut)})});
var r=document.querySelector('[data-rotate]');
if(r&&!window.matchMedia('(prefers-reduced-motion: reduce)').matches){var w=r.getAttribute('data-rotate').split('|'),i=0;setInterval(function(){r.classList.add('out');setTimeout(function(){i=(i+1)%w.length;r.textContent=w[i];r.classList.remove('out')},280)},2300)}
})();</script>'''
