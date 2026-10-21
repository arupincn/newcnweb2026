# Stacked, single-column package cards (v10). One card per package, one below the other.
# Each package: dict(id, n, col, name, q, lh, ll, rh, rl, meta=[(k,v)], note, cta=(label, href) or None)

def _ul(items): return '<ul class="acts">' + "".join(f"<li>{x}</li>" for x in items) + "</ul>"

def pkg_card(p):
    meta = "".join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in p["meta"])
    note = f'<p class="note">{p["note"]}</p>' if p.get("note") else ""
    cta = ""
    if p.get("cta"):
        t, h = p["cta"]
        ext = ' target="_blank" rel="noopener"' if h.startswith("http") else ""
        cta = f'<div class="pkg-cta"><a class="btn" href="{h}"{ext}>{t}</a></div>'
    return f'''<article class="pkg" id="{p["id"]}">
<div class="tp-head {p["col"]}"><span class="pn">Package {p["n"]}</span><h3>{p["name"]}</h3><p>{p["q"]}</p></div>
<div class="pkg-block"><h4>{p["lh"]}</h4>{_ul(p["ll"])}</div>
<div class="pkg-block tp-get"><h4>{p["rh"]}</h4>{_ul(p["rl"])}</div>
<dl class="pkg-meta">{meta}</dl>{note}{cta}</article>'''

def pkg_jump(pkgs):
    return '<nav class="pkg-jump" aria-label="Packages">' + "".join(
        f'<a href="#{p["id"]}"><span>{p["n"]}</span>{p["name"]}</a>' for p in pkgs) + "</nav>"

def pkg_section(eyebrow, h, sub, pkgs, head, sid="packages", cls=""):
    cards = "".join(pkg_card(p) for p in pkgs)
    return f'''<section class="{cls}" id="{sid}"><div class="wrap">{head(eyebrow, h, sub)}
{pkg_jump(pkgs)}<div class="pkgs">{cards}</div></div></section>'''

CONTACT = "contact.html"
FV_EMAIL = "challengeus@currynation.in"
PERF_EMAIL = "nagesshp@currynation.in"

# ---------------------------------------------------------------- FOUNDER-LED
FOUNDER = [
 dict(id="audit", n="1", col="c-purple", name="Founder Authority Audit", q="Where does the founder’s authority stand today?",
  lh="We review", ll=["LinkedIn, search presence and existing content", "Founder story, proof assets and category point of view", "How peer and competitor founders show up", "Gaps between attention and a useful next conversation"],
  rh="You receive", rl=["Founder Authority Scorecard", "A clear diagnosis of what’s working and what’s missing", "A 90-day opportunity map", "A recommended next step in a 45-minute readout"],
  meta=[("Fee", "₹5,000"), ("Delivery", "10 working days"), ("Next", "Credit applies if you proceed within 14 days")],
  note="A founder with no meaningful existing presence may start with the Action Plan instead.",
  cta=("Book the Audit", f"mailto:{FV_EMAIL}?subject=Founder%20Authority%20Audit")),
 dict(id="plan", n="2", col="c-slate", name="Action Plan", q="What should we build, and in what order?",
  lh="We work out", ll=["Category lens: which kind of authority matters in your market (expertise, trust, access, proof or category voice)", "Founder intent: which audience and business outcome to prioritise", "Channel choices: where to show up, and which channels to ignore", "Investment path: what deserves money now, and what doesn’t"],
  rh="You receive", rl=["An industry-specific roadmap", "A 90-day sequence", "A 12-month direction", "A recommended investment path"],
  meta=[("Fee", "Scoped on call"), ("Time", "About 2 weeks"), ("Next", "Leads into the System Build")],
  note="This package answers what to build. The System Build answers what the founder should stand for and say.",
  cta=("Talk to us", f"mailto:{FV_EMAIL}?subject=Founder%20Action%20Plan")),
 dict(id="build", n="3", col="c-deep", name="System Build", q="What should the founder stand for and say?",
  lh="We build", ll=["Position: the founder’s point of view and audience intent", "Narrative: origin, proof, battle and category stories", "Content: pillars, formats, starter scripts and launch content", "Profile: headline, about copy, bios and banner direction", "AI system: a prompt library and a live GPT or Claude workspace"],
  rh="You receive", rl=["A complete authority system you own: strategy, copy, prompts and files", "Launch-ready content and profile copy", "One training session for the founder and team", "30 days of implementation support"],
  meta=[("Fee", "Scoped on call"), ("Time", "4 weeks"), ("Next", "Run it yourself, or with us")],
  note="Everything created during the build belongs to you.",
  cta=("Talk to us", f"mailto:{FV_EMAIL}?subject=Founder%20System%20Build")),
 dict(id="implement", n="4", col="c-teal", name="Implement", q="Who runs it, week to week?",
  lh="Three ways to run it", ll=["DIY: your team runs the system with the prompts, templates and roadmap. No ongoing commitment.", "Guided: we stay close for 30 days of reviews, questions and corrections. Included in the System Build.", "Managed: we run a monthly rhythm, starting with a three-month pilot. Scoped on call."],
  rh="Managed monthly base", rl=["Eight LinkedIn posts in the founder’s voice", "Two carousel adaptations", "One long-form article or newsletter", "Engagement and response prompts", "A monthly content review and authority dashboard"],
  meta=[("Founder input", "One 90-minute interview and timely approvals each month"), ("Pilot", "3 months, then scope can grow"), ("Note", "Reach, leads and revenue are not guaranteed")],
  note="Managed starts only after the System Build has set the positioning, voice and approvals.",
  cta=("Talk to us", f"mailto:{FV_EMAIL}?subject=Founder%20Implement")),
]

# ---------------------------------------------------------------- BRAND-LED · COMMODITY TO BRAND
C2B = [
 dict(id="audit", n="1", col="c-red", name="Brand Audit", q="Where does your brand stand, and what is it costing you?",
  lh="You answer", ll=["20 yes/no questions across four areas: Dependence, Conditioning, Signal and Pull", "Three short answers in your own words, including how you would finish “Customers choose us because…”", "Eight deeper questions, if you want the written report"],
  rh="You receive", rl=["Your score out of 40 and your tier, from Replaceable to Requested", "Your two weakest areas, named, with what they cost you in margin, dealer power and pricing", "A written report by email within two working days", "A 30–45 minute call with a Curry Nation founder, and one agreed next step"],
  meta=[("Fee", "Free"), ("Time", "About 10 minutes · report in 2 working days"), ("Next", "Your email is asked for only after you see your score")],
  note="The Audit shows where you stand. It doesn’t include a plan, prices or a recommendation to buy anything.",
  cta=("See how the Audit works", "brand-audit.html")),
 dict(id="positioning", n="2", col="c-orange", name="Brand Positioning", q="What is the one reason to choose you that no rival owns?",
  lh="We work through", ll=["Discover (2 weeks): your team, your sales and pricing, your category, and the buyers who choose in it", "Define (2 weeks): the target buyer, the proof only you can show, and the Brand Key", "Express (2 weeks): two creative routes and the plan to launch them"],
  rh="You receive", rl=["A Demand Atlas with 3–5 unclaimed reasons to choose you, and one recommended", "A one-page Brand Platform: target, positioning, proof and Brand Key", "Two creative routes with a recommended line", "A 90-day launch roadmap with owners and sequence"],
  meta=[("Fee", "Scoped on call, plus GST"), ("Time", "6 weeks, or one 2-week phase at a time"), ("Next", "The full programme costs 15% less than buying phases separately")],
  note="Logo, packaging, production, media and website build are quoted separately.",
  cta=("See the three phases", "brand-positioning.html")),
 dict(id="workshop", n="3", col="c-deep", name="Challenger Workshop", q="Is your leadership team behind the one problem that matters most?",
  lh="Two ways to run it", ll=["For Leadership: one workshop day for the founder and 8–10 functional heads, then the plan a week later. For teams with research from the last six months.", "For Business: five weeks of evidence first (25 customer interviews, a store and channel safari, a rival tear-down), then the day and the plan."],
  rh="You receive", rl=["One priority problem, agreed in the room", "A Challenger Positioning Snapshot on one page", "Three campaign directions", "A 90-day roadmap with named owners and measures"],
  meta=[("Fee", "Scoped on call · venue and travel at actuals"), ("Time", "For Leadership: 1 day + 1 week · For Business: about 7 weeks"), ("Promise", "No breakthrough idea on the day, no fee")],
  note="The Curry Nation founders lead the workshop day.",
  cta=("See the workshop day", "challenger-workshop.html")),
]

# ---------------------------------------------------------------- LEADERSHIP-LED · CXO
CXO = [
 dict(id="cxo-audit", n="1", col="c-green", name="CXO Audit", q="Where do your team’s answers stop holding up?",
  lh="How the two days run", ll=["Before: a founder briefing to flag sensitive topics and set ground rules", "Day 1: three functions audited in turn, each by a senior operator matched to that function, with the founder in the room", "Evening: structured downtime with our panel", "Day 2: the remaining functions audited, then a findings session"],
  rh="You receive", rl=["A findings pack: what each function admitted under challenge", "Where answers didn’t hold up, and where functions quietly disagreed", "Every function’s blind spot, named in front of the founder", "An agreed list of findings to act on"],
  meta=[("Fee", "Scoped on call · includes 5 senior auditors, venue and meals"), ("Time", "2-day offsite"), ("Next", "Leads into the Challenger Workshop")],
  note="Always offsite, at a property from our shortlist. Your team’s travel to the venue is at actuals.",
  cta=("See how the two days run", "#days")),
 dict(id="cxo-workshop", n="2", col="c-red", name="Challenger Workshop for Leadership", q="Of everything we found, which problem do we solve first?",
  lh="The workshop day", ll=["The founder sets the challenge and what is at stake", "Small groups test assumptions in challenger drills and scenario boards", "Teams map how they will launch and sell, and score each action", "Teams pitch back. The founder gives a verdict and commits to the plan."],
  rh="You receive", rl=["One priority problem, agreed by the whole leadership team", "A Challenger Positioning Snapshot on one page", "Three campaign directions", "A 90-day roadmap with named owners and measures"],
  meta=[("Fee", "Scoped on call · venue and travel at actuals"), ("Time", "1 day + 1 week"), ("Promise", "No breakthrough idea on the day, no fee")],
  note="Built for founders who have completed the CXO Audit, or who have research from the last six months.",
  cta=("See the workshop day", "challenger-workshop.html#day")),
 dict(id="cxo-implement", n="3", col="c-teal", name="Implementation Support", q="Are the heads acting on what they agreed?",
  lh="We support", ll=["The function heads who own each agreed finding", "The founder, with progress reviewed at agreed check-ins"],
  rh="You receive", rl=["Support from the audit panel while your heads act on the findings", "A clear view, for the founder, of what has moved and what hasn’t"],
  meta=[("Fee", "Scoped on call"), ("Time", "Scoped to the findings"), ("Next", "Agreed after the Audit or the Workshop")],
  note="Scope is set by the findings, function by function.",
  cta=("Talk to us", CONTACT)),
]

# ---------------------------------------------------------------- PERFORMANCE-LED · GROWTH LAB
PERF = [
 dict(id="growth-audit", n="1", col="c-teal", name="Growth Audit", q="Where is profitable growth hiding, and what is stopping it?",
  lh="We review", ll=["Margins and SKU economics", "Ad accounts and tracking", "Listings and stock", "Cities, audiences and channels worth backing", "Measurement gaps that make today’s numbers unreliable"],
  rh="You receive", rl=["An opportunity map", "Measurement fixes", "A 90-day action plan", "A clear view of where to put the next rupee, and where to stop"],
  meta=[("Fee", "Tailored after a discovery call"), ("Delivery", "3–4 weeks · fixed scope"), ("Next", "Leads into Market Launch")],
  note="Media spend, production and platform fees are scoped separately.",
  cta=("Start a conversation", f"mailto:{PERF_EMAIL}?subject=Growth%20Audit")),
 dict(id="market-launch", n="2", col="c-deep", name="Market Launch", q="Does the plan work in the market, and where should we scale?",
  lh="We run", ll=["Everything in the Growth Audit", "Campaigns and creative tests", "Improved product pages", "Remarketing and enquiry routing", "Weekly reviews with clear scale or stop rules"],
  rh="You receive", rl=["A market-by-market view of sales, cost and next steps", "A scale or stop decision for each market"],
  meta=[("Fee", "Tailored after a discovery call"), ("Time", "90 days · managed pilot"), ("Next", "Leads into the Scale Partnership")],
  note="Media spend, production and platform fees are scoped separately.",
  cta=("Start a conversation", f"mailto:{PERF_EMAIL}?subject=Market%20Launch")),
 dict(id="scale", n="3", col="c-flame", name="Scale Partnership", q="How do we keep growing without giving the margin back?",
  lh="We manage", ll=["Everything in Market Launch", "Meta, Google, LinkedIn and marketplaces, together", "Ongoing tests by city and SKU, with decisions linked to inventory"],
  rh="You receive", rl=["A managed growth engine", "Contribution reporting", "Quarterly leadership reviews"],
  meta=[("Fee", "Tailored after a discovery call"), ("Time", "Ongoing · tailored scope"), ("Measured on", "Contribution after fees, returns and discounts")],
  note="Media spend, production and platform fees are scoped separately.",
  cta=("Start a conversation", f"mailto:{PERF_EMAIL}?subject=Scale%20Partnership")),
]

# ================================================================ v11
# Comparison table (desktop) + stacked summary cards (mobile), reusing .cmp / .pk styles from v8.
# rows: list of (label, key). Each package needs those keys.
CMP_ROWS = [("Fee", "fee"), ("Time", "time"), ("Answers", "q"), ("You get", "get"), ("Best if", "best")]
def cmp_section(eyebrow, h, sub, pkgs, head, sid="compare", cls="white"):
    th = "".join(f'<th scope="col" class="{p["col"]}"><span class="pn">Package {p["n"]}</span><b>{p["name"]}</b><a href="#{p["id"]}">See what’s covered ↓</a></th>' for p in pkgs)
    body = "".join(f'<tr><th scope="row">{lab}</th>' + "".join(f'<td{" class=\"price\"" if k=="fee" else ""}>{p[k]}</td>' for p in pkgs) + "</tr>" for lab, k in CMP_ROWS)
    cards = "".join(f'<a class="pk {p["col"]}" href="#{p["id"]}"><span class="pn">Package {p["n"]} · {p["time"]}</span><b>{p["name"]}</b><span class="pp">{p["fee"]}</span><span>{p["get"]}</span><span><b style="font:inherit;font-weight:600">Best if:</b> {p["best"]}</span><span class="go">See what’s covered ↓</span></a>' for p in pkgs)
    mw = 260 * len(pkgs) + 120
    return f'''<section class="{cls}" id="{sid}"><div class="wrap">{head(eyebrow, h, sub)}
<div class="cmp-wrap"><table class="cmp" style="min-width:{mw}px"><thead><tr><th scope="col" class="cmp-corner">Compare</th>{th}</tr></thead><tbody>{body}</tbody></table></div>
<div class="pk-cards">{cards}</div></div></section>'''

def _add(pk, rows):
    for p, (fee, time, get, best) in zip(pk, rows):
        p.update(fee=fee, time=time, get=get, best=best)

_add(FOUNDER, [
 ("₹5,000", "10 working days", "Scorecard, diagnosis, 90-day opportunity map and a 45-minute readout", "You want evidence before investing"),
 ("On call", "About 2 weeks", "Category lens, audience, channel choices and a 90-day roadmap", "The founder has little or no presence yet"),
 ("On call", "4 weeks", "Positioning, narrative, content system, profile and an AI workspace you own", "You’re ready to commit to a clear point of view"),
 ("DIY · Guided · Managed", "From 30 days", "Your team, your team with our support, or a managed monthly rhythm", "The system is built and approved")])

# Brand-led: the leadership version of the workshop now lives under Leadership-led, so Package 3 is For Business only.
C2B[2].update(name="Challenger Workshop for Business", id="workshop",
  lh="How it runs", ll=["Five weeks of evidence: 25 interviews with current and lapsed customers, a store and channel safari, and a rival tear-down", "One synthesis of what is holding sales back, with 3–5 candidate problems for the day", "The workshop day: the founder and 8–10 functional heads agree the one problem to solve first", "The plan, a week later"],
  rh="You receive", rl=["An Evidence Pack and the workshop pre-read", "One priority problem, agreed in the room", "A Challenger Positioning Snapshot and three campaign directions", "A 90-day roadmap with named owners and measures"],
  meta=[("Fee", "Scoped on call · venue and travel at actuals"), ("Time", "About 7 weeks"), ("Promise", "No breakthrough idea on the day, no fee")],
  note="Want the leadership team in the room without the five weeks of research? See the <a class=\"hl\" href=\"cxo-audit.html\"><b>Challenger Workshop for Leadership</b></a>.",
  cta=("See the workshop", "challenger-workshop.html#business"))
_add(C2B, [
 ("Free", "About 10 minutes", "Score out of 40, your tier, a written report and a call", "You want to know where you stand before spending"),
 ("Scoped on call", "6 weeks", "Demand Atlas, Brand Platform, two creative routes and a 90-day roadmap", "Buyers compare you with rivals on price"),
 ("Scoped on call", "About 7 weeks", "Evidence Pack, one agreed problem and a 90-day plan with owners", "Growth has stalled and nobody can say for sure why")])

_add(PERF, [
 ("Tailored", "3–4 weeks", "Opportunity map, measurement fixes and a 90-day action plan", "ROAS looks fine but profit doesn’t move"),
 ("Tailored", "90 days", "A market-by-market view of sales and cost, with scale or stop decisions", "You have a plan and want to prove it in the market"),
 ("Tailored", "Ongoing", "A managed growth engine with contribution reporting", "The pilot has shown where to scale")])

DESIGN = [
 dict(id="identity", n="1", col="c-orange", name="Brand Identity System", q="How should the brand look everywhere it appears?",
  lh="We design", ll=["Logo and wordmark, or a refresh of the one you have", "Visual identity system: colour, typography, imagery and layout", "Brand guidelines your team, dealers and vendors can follow", "Rollout to stationery, signage, vehicles and digital profiles"],
  rh="You receive", rl=["An identity system", "Brand guidelines", "Rollout artwork for every surface agreed"],
  meta=[("Fee", "Scoped on call"), ("Time", "Scoped on call"), ("Starts from", "An approved positioning")],
  note="Printing, shoots and external vendors are billed at actuals, with your approval first.", cta=("Talk to us", CONTACT)),
 dict(id="packaging", n="2", col="c-flame", name="Packaging & Shelf", q="How do we win the three seconds in front of the shelf?",
  lh="We design", ll=["Product packaging and range architecture", "Labels and back-of-pack claims that prove the promise", "Point-of-sale displays and trade collateral", "Print-ready artwork and vendor handover"],
  rh="You receive", rl=["Print-ready packaging and label files", "Point-of-sale and trade collateral files", "A vendor handover"],
  meta=[("Fee", "Scoped on call"), ("Time", "Scoped on call"), ("Starts from", "An approved positioning")],
  note="Printing, shoots and external vendors are billed at actuals, with your approval first.", cta=("Talk to us", CONTACT)),
]
_add(DESIGN, [
 ("Scoped on call", "Scoped on call", "Identity system, guidelines and rollout artwork", "You look like a different company on every surface"),
 ("Scoped on call", "Scoped on call", "Print-ready packaging, label and point-of-sale files", "Your pack looks like the three next to it")])

# Leadership-led: ONE product. The founder brings one problem; a 2-day offsite mixes the audit and the workshop.
LEAD = [
 dict(id="leadership", n="1", col="c-green", name="Challenger Workshop for Leadership", q="The founder names one problem. Is the whole leadership team really behind solving it?",
  lh="How it runs", ll=["Before: the founder gives us one problem statement, and flags sensitive topics", "Day 1: senior operators, each matched to one of your functions, challenge every decision-maker on that problem, with the founder in the room", "Evening: structured downtime with our panel", "Day 2: the workshop. Challenger drills and scenario boards on the problem, then each team pitches its plan and the founder gives a verdict", "A week later: the plan, written up"],
  rh="You receive", rl=["The founder’s problem, tested from every function", "Where answers didn’t hold up, and where functions quietly disagreed", "One agreed way forward, decided by the people who have to deliver it", "A 90-day plan with named owners and measures"],
  meta=[("Fee", "Scoped on call · includes the senior operators, venue and meals"), ("Time", "2-day offsite, plan a week later"), ("Who’s in the room", "The founder and the key decision-makers")],
  note="Always offsite, at a property from our shortlist. Your team’s travel to the venue is at actuals.",
  cta=("Talk to us", CONTACT)),
]

# ================================================================ v12
# Leadership workshop now sits inside Brand-led as Package 3; Business becomes Package 4.
import copy as _copy
LEAD_PAGE = "leadership-workshop.html"
_lead = _copy.deepcopy(LEAD[0])
_lead.update(id="leadership", n="3", col="c-green", cta=("See how the two days run", LEAD_PAGE + "#days"),
  fee="Scoped on call", time="2 days + 1 week", get="The founder’s problem tested by every function, and a 90-day plan", best="You know the problem and need every decision-maker behind the answer")
_biz = _copy.deepcopy(C2B[2])
_biz.update(n="4", note="Already know the problem? The <a class=\"hl\" href=\"" + LEAD_PAGE + "\"><b>Challenger Workshop for Leadership</b></a> starts with it and takes two days.")
BRAND = [C2B[0], C2B[1], _lead, _biz]
LEAD[0]["cta"] = ("Talk to us", CONTACT)
