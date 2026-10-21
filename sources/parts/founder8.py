# ================================================================ FOUNDER VISIBILITY (v8: package-first)
EMAIL = "challengeus@currynation.in"
fv = hero("Founder-led · The Visible Founder Authority System",
  "Founder authority creates <span class=\"hlp\">context before contact.</span>",
  "Four packages that turn what the founder knows into visible proof, so buyers, partners and hires arrive already knowing why the founder matters. <b>Start with the Audit. Continue only if it makes business sense.</b>",
  [("Start with", "the Audit"), ("Audit fee", "₹10,000"), ("Delivery", "10 working days")],
  [("Compare the packages", "#packages", ""), ("Book the Audit", f"mailto:{EMAIL}?subject=Founder%20Authority%20Audit", "dark")], ("pigeon", "diya"))

fv += '''<nav class="pagenav" aria-label="On this page"><div class="wrap">
<a href="#packages">Packages</a><a href="#covered">What’s covered</a><a href="#fit">Is it for you?</a><a href="#how">How it works</a><a href="#addons">Add-ons</a><a href="#faq">FAQ</a></div></nav>'''

PK = [
 ("audit", "1", "c-purple", "Founder Authority Audit", "₹10,000", "10 working days",
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
rows = [("Price", 4), ("Time", 5), ("Answers", 6), ("You get", 7), ("Best if", 8)]
head_cells = "".join(f'<th scope="col" class="{p[2]}"><span class="pn">Package {p[1]}</span><b>{p[3]}</b><a href="#tab-{p[0]}" data-tab="{p[0]}">What’s covered ↓</a></th>' for p in PK)
body_rows = "".join(f'<tr><th scope="row">{lab}</th>' + "".join(f'<td{" class=\"price\"" if i==4 else ""}>{p[i]}</td>' for p in PK) + "</tr>" for lab, i in rows)
fv += f'''<section class="white" id="packages"><div class="wrap">{head("the packages", "Four packages. Each one stands alone.", "Only the Audit is priced up front. Every later package is scoped on a call once the Audit shows what the founder needs. Proceed within 14 days and the ₹10,000 is credited to the next package.")}
<div class="cmp-wrap"><table class="cmp"><thead><tr><th scope="col" class="cmp-corner">Compare</th>{head_cells}</tr></thead><tbody>{body_rows}</tbody></table></div>
<div class="pk-cards">{"".join(f'<a class="pk {p[2]}" href="#tab-{p[0]}" data-tab="{p[0]}"><span class="pn">Package {p[1]} · {p[5]}</span><b>{p[3]}</b><span class="pp">{p[4]}</span><span>{p[6]}</span><span class="go">What’s covered ↓</span></a>' for p in PK)}</div>
</div></section>'''

COVER = {
 "audit": ("We review", ["LinkedIn, search presence and existing content", "Founder story, proof assets and category point of view", "How peer and competitor founders show up", "Gaps between attention and a useful next conversation"],
           "You receive", ["Founder Authority Scorecard", "A clear diagnosis of what’s working and what’s missing", "A 90-day opportunity map", "A recommended next step in a 45-minute readout"],
           [("Fee", "₹10,000"), ("Delivery", "10 working days"), ("Next", "Credit applies if you proceed within 14 days")],
           "A founder with no meaningful existing presence may start with the Action Plan instead."),
 "plan": ("We work out", ["Category lens: which kind of authority matters in your market (expertise, trust, access, proof or category voice)", "Founder intent: which audience and business outcome to prioritise", "Channel choices: where to show up, and which channels to ignore", "Investment path: what deserves money now, and what doesn’t"],
          "You receive", ["An industry-specific roadmap", "A 90-day sequence", "A 12-month direction", "A recommended investment path"],
          [("Fee", "Scoped on call"), ("Time", "About 2 weeks"), ("Next", "Leads into the System Build")],
          "This package answers what to build. The System Build answers what the founder should stand for and say."),
 "build": ("We build", ["Position: the founder’s point of view and audience intent", "Narrative: origin, proof, battle and category stories", "Content: pillars, formats, starter scripts and launch content", "Profile: headline, about copy, bios and banner direction", "AI system: a prompt library and a live GPT or Claude workspace"],
           "You receive", ["A complete authority system you own: strategy, copy, prompts and files", "Launch-ready content and profile copy", "One training session for the founder and team", "30 days of implementation support"],
           [("Fee", "Scoped on call"), ("Time", "4 weeks"), ("Next", "Run it yourself, or with us")],
           "Everything created during the build belongs to you."),
 "implement": ("Three ways to run it", ["DIY: your team runs the system with the prompts, templates and roadmap. No ongoing commitment.", "Guided: we stay close for 30 days of reviews, questions and corrections. Included in the System Build.", "Managed: we run a monthly rhythm, starting with a three-month pilot. Scoped on call."],
               "Managed monthly base", ["Eight LinkedIn posts in the founder’s voice", "Two carousel adaptations", "One long-form article or newsletter", "Engagement and response prompts", "A monthly content review and authority dashboard"],
               [("Founder input", "One 90-minute interview and timely approvals each month"), ("Pilot", "3 months, then scope can grow"), ("Note", "Reach, leads and revenue are not guaranteed")],
               "Managed starts only after the System Build has set the positioning, voice and approvals."),
}
tabs = "".join(f'<button type="button" role="tab" id="t-{p[0]}" aria-controls="tab-{p[0]}" aria-selected="{"true" if i==0 else "false"}" class="{p[2]}"><span class="pn">{p[1]}</span>{p[3]}</button>' for i, p in enumerate(PK))
panels = ""
for i, p in enumerate(PK):
    lh, ll, rh, rl, meta, note = COVER[p[0]]
    m = "".join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in meta)
    panels += f'''<div class="tabpanel" role="tabpanel" id="tab-{p[0]}" aria-labelledby="t-{p[0]}"{"" if i==0 else " hidden"}>
<span class="anchor" id="{p[0]}"></span>
<div class="tp-head {p[2]}"><span class="pn">Package {p[1]}</span><h3>{p[3]}</h3><p>{p[6]}</p></div>
<div class="tp-body"><div><h4>{lh}</h4><ul class="acts">{"".join(f"<li>{x}</li>" for x in ll)}</ul></div>
<div class="tp-get"><h4>{rh}</h4><ul class="acts">{"".join(f"<li>{x}</li>" for x in rl)}</ul></div></div>
<dl class="tp-meta">{m}</dl><p class="note">{note}</p></div>'''
fv += f'''<section id="covered"><div class="wrap">{head("what’s covered", "Pick a package to see exactly what’s included")}
<div class="tabs" role="tablist" aria-label="Packages">{tabs}</div>{panels}</div></section>'''

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

FAQ = [
 ("Why does founder visibility matter for the business?", "Visibility works when the founder makes expertise, values and category beliefs easier for the market to recognise. Nithin Kamath (Zerodha) made the thinking behind his company accessible through education and transparency. Aman Gupta gave boAt a recognisable human voice. Ghazal Alagh’s personal problem became Mamaearth’s brand story. These examples show the mechanism; they don’t guarantee growth."),
 ("How is pricing decided?", "Only the Audit is priced before the first call, at ₹10,000. Every later package is scoped and priced once the Audit shows what the founder actually needs. Proceed within 14 days and the Audit fee is credited against the next agreed package."),
 ("Do I have to buy all four packages?", "No. Each package stands alone and gives you something useful. Most founders start with the Audit; a founder with no real presence yet may start with the Action Plan."),
 ("What does the founder need to give?", "Honest access to their experience and proof, and approval of a clear point of view. For the managed rhythm, one structured 90-minute interview and timely approvals each month."),
 ("Who owns the work?", "You do. The strategy, copy, prompts and working files created during the engagement are yours, whether your team runs the system or we continue with you."),
 ("What isn’t guaranteed?", "Reach, leads, meetings, media coverage and revenue. The system turns substance into visibility. It cannot manufacture substance that isn’t there."),
 ("Why Curry Nation?", "Positioning comes before posting. We are built for owner-managed companies where trust sits with the promoter, we start from what the market must understand rather than a calendar of random topics, and we keep essential work separate from optional projects and third-party costs."),
]
fv += f'''<section id="faq"><div class="wrap">{head("faq", "Questions founders ask")}
<div class="faq">{"".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)}</div>
<div class="card" style="margin-top:14px"><p>Already visible, but the business still sells on price? <a class="hl" href="brand-audit.html"><b>Take the free Brand Audit</b></a> to see where the company stands.</p></div></div></section>'''
fv += related("founder-visibility.html")
fv += f'''<section class="close" id="enquire"><div class="wrap"><p class="eyebrow">next step</p><h2 class="display">Start with evidence.</h2>
<p>The Audit shows where the founder stands, what’s missing and whether the next investment makes business sense. No retainer required.</p>
<div class="chips"><span>Fee <b>₹10,000</b></span><span>Delivery <b>10 working days</b></span><span>Email <b class="sel">{EMAIL}</b></span></div>
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
fv += FV_JS
