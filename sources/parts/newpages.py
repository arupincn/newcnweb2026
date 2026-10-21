# ================================================================ PERFORMANCE-LED
PERF_EMAIL = "nagesshp@currynation.in"
PERF_PHONE = "+91 92235 02716"
pf = hero("Performance-led · Curry Nation Growth Lab",
  "Turn product demand into <span class=\"hl\">profitable growth.</span>",
  "Performance marketing for <b>₹100–300 Cr product businesses</b> that want to grow beyond discounts. We connect media, marketplaces and customer demand, and judge every rupee by what it adds to contribution.",
  [("Approach", "Strategy × Media × Commerce"), ("Measured on", "contribution, not applause")],
  [("Try the growth planner ↗", PLANNER, ""), ("See the packages", "#packages", "dark")], ("diya", "chai"))
plats = "".join(f"<span>{p}</span>" for p in ["Meta", "Google", "Amazon", "Flipkart", "Meesho", "Blinkit", "Zepto", "Zomato", "Myntra", "LinkedIn"])
pf += f'''<section class="white"><div class="wrap"><p class="eyebrow" style="text-align:center">Platforms we connect</p><div class="platforms">{plats}</div></div></section>'''
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
pf += f'''<section class="white" id="packages"><div class="wrap">{head("packages", "The right support for your next growth stage", "Fees are tailored after a discovery call. Media spend, production and platform fees are scoped separately.")}
<div class="phases">
{phase("c-teal","1","Growth Audit","3–4 weeks · fixed scope","Where is profitable growth hiding, and what is stopping it?",[
 "Review margins, ad accounts, tracking, listings and stock","Map cities, audiences and channels worth backing","Find the measurement gaps that make today’s numbers unreliable"],
 "Opportunity map, measurement fixes and a 90-day action plan","Know where to put the next rupee, and where to stop","Approved 90-day plan", a="bell")}
{phase("c-deep","2","Market Launch","90 days · managed pilot","Does the plan work in the market, and where should we scale?",[
 "Everything in the Growth Audit","Campaigns and creative tests, improved product pages, remarketing and enquiry routing","Weekly reviews with clear scale or stop rules"],
 "A market-by-market view of sales, cost and next steps","Scale what works with evidence, not hope","Scale or stop decision per market", a="diya")}
{phase("c-flame","3","Scale Partnership","Ongoing · tailored scope","How do we keep growing without giving the margin back?",[
 "Everything in Market Launch","Meta, Google, LinkedIn and marketplaces managed together","Ongoing tests by city and SKU, with decisions linked to inventory","Contribution reporting and leadership reviews"],
 "A managed growth engine with contribution reporting","Grow sales and profit together","Quarterly leadership review", a="drum")}
</div></div></section>'''
pf.replace("", "")
pf = pf.replace('<article class="phase">', '<article class="phase">', 1)
pf = pf.replace('<span class="n">1</span><h3>Growth Audit', '<span class="n" id="growth-audit">1</span><h3>Growth Audit').replace('<span class="n">2</span><h3>Market Launch', '<span class="n" id="market-launch">2</span><h3>Market Launch').replace('<span class="n">3</span><h3>Scale Partnership', '<span class="n" id="scale">3</span><h3>Scale Partnership')
pf += related("performance.html")
pf += f'''<section class="close" id="enquire"><div class="wrap"><p class="eyebrow">let’s talk</p><h2 class="display">Tell us where growth gets stuck.</h2>
<p>Share your category, current monthly media spend and the growth problem you want solved. We’ll suggest a Growth Audit, Market Launch or Scale Partnership, or tell you it’s too early.</p>
<div class="chips"><span>Email <b class="sel">{PERF_EMAIL}</b></span><span>Phone <b class="sel">{PERF_PHONE}</b></span></div>
<div class="ctas"><a class="btn" href="mailto:{PERF_EMAIL}?subject=Growth%20enquiry">Start a conversation</a><a class="btn dark" href="{PLANNER}" target="_blank" rel="noopener">Try the planner ↗</a></div>
<p class="note">Strategy before spend. Contribution before applause.</p></div></section>'''

# ================================================================ DESIGN-LED
dz = hero("Design-led",
  "Look like the brand <span class=\"hl\">you’re becoming.</span>",
  "Once you know what you stand for, it has to show up on the pack, the shelf, the screen and the dealer counter. Design-led work turns your positioning into an <b>identity, packaging and communication</b> people recognise before they read a word.",
  [("Covers", "identity · packaging · communication"), ("Built on", "an approved positioning")],
  [("Let’s talk", CONTACT, ""), ("See our work", "https://currynation.in/work/", "dark")], ("bell", "elephant"))
dz += f'''<section class="white"><div class="wrap">{head("the problem", "When it looks like a commodity, it gets priced like one")}
<div class="gap">
<div class="c-orange"><span class="n">01</span><p>On the shelf, your pack looks like the three next to it, so the cheapest one wins</p></div>
<div class="c-flame"><span class="n">02</span><p>With the trade, your catalogue and counter material don’t justify a better margin</p></div>
<div class="c-red"><span class="n">03</span><p>On screen, every channel looks like it came from a different company</p></div>
</div></div></section>'''
dz += f'''<section><div class="wrap">{head("products", "Three ways to make the brand visible")}<div class="phases">
{phase("c-orange","1","Identity System","Scoped on call","How should the brand look everywhere it appears?",[
 "Logo and wordmark, or a refresh of the one you have","Visual identity system: colour, typography, imagery and layout","Brand guidelines your team, dealers and vendors can follow","Rollout to stationery, signage, vehicles and digital profiles"],
 "Identity system and brand guidelines","Look like one company on every surface","Approved identity", a="elephant")}
{phase("c-flame","2","Packaging & Shelf","Scoped on call","How do we win the three seconds in front of the shelf?",[
 "Product packaging and range architecture","Labels and back-of-pack claims that prove the promise","Point-of-sale displays and trade collateral","Print-ready artwork and vendor handover"],
 "Print-ready packaging, label and POS files","Stand out on the shelf and justify the price","Approved artwork", a="chai")}
{phase("c-red","3","Communication Design","Scoped on call","How do we say it the same way in print, film and digital?",[
 "Print and press advertising","Brand and product films","Digital, social and performance creative","Campaign toolkits for dealers and distributors"],
 "Campaign and content assets, ready to run","Say the same thing, the right way, on every channel","Approved assets", a="drum")}
</div></div></section>'''
dz = dz.replace('<span class="n">1</span><h3>Identity System', '<span class="n" id="identity">1</span><h3>Identity System').replace('<span class="n">2</span><h3>Packaging', '<span class="n" id="packaging">2</span><h3>Packaging').replace('<span class="n">3</span><h3>Communication Design', '<span class="n" id="communication">3</span><h3>Communication Design')
dz += f'''<section class="white"><div class="wrap">{head("how we work", "Strategy first, then design")}
{terms([("Starts from positioning","Design-led work needs an approved positioning, from our Brand Positioning programme or your own. Otherwise we start with a short positioning check."),("Scope and fees","Each product is scoped and priced on a call, once we know your range, channels and rollout."),("Production","Printing, shoots, studios, media and external vendors are billed at actuals, with your approval first."),*TAIL])}
<div class="card" style="margin-top:14px"><p>Want to see the work first? Browse packaging, print, film and digital for Rasna, Nirlep, Chipseez, Emami and more on <a class="hl" href="https://currynation.in/work/"><b>currynation.in/work</b></a>.</p></div></div></section>'''
dz += related("design.html") + close("Make the brand impossible to mistake.", "Tell us what you sell and where it’s sold. We’ll recommend where design will move the price first.", "Let’s talk")

# ================================================================ LEADERSHIP-LED · CXO AUDIT
cx = hero("Leadership-led · CXO Audit",
  "Your leadership team, <span class=\"hl\">audited in one room.</span>",
  "A founder hears what each function head chooses to say. Over two days at an offsite, <b>senior operators matched to each of your functions challenge your team’s own answers</b>, with you in the room. You hear in two days what would take months of one-on-ones.",
  [("Format", "2-day offsite"), ("Auditors", "5 senior operators"), ("Your side", "founder + 5–8 heads")],
  [("Let’s talk", CONTACT, ""), ("How the two days run", "#days", "dark")], ("drum", "pigeon"))
cx += f'''<section class="white"><div class="wrap">{head("at a glance", "Two days, two rounds, one findings session")}
{glance(["Session","You get","Your business can now","Time"],[
 ["Day 1 · Round 1","Live audit of 3 functions","Hear how your team’s answers hold up to outside challenge","4 hrs"],
 ["Day 1 · Evening","Structured downtime with our panel","Build trust with our team before the harder questions on Day 2","—"],
 ["Day 2 · Round 2","Audit of the remaining functions, then a findings session","Leave with every function’s blind spot named in one room","4 hrs"]], None,
 "The fee includes 5 senior auditors, the venue and meals from our shortlist of partner properties. Travel to the venue is at actuals.")}</div></section>'''
cx += f'''<section><div class="wrap">{head("who’s in the room", "Your heads. Our operators.")}
{stats([("c-green","Founder or MD","1","present for both days"),("c-orange","Function heads","5–8","sales, operations, HR, trade marketing and more"),("c-teal","Senior operators","5","one matched to each function, briefed on your category"),("c-red","Coordinating lead","1","runs the two days and owns the findings")])}
<div class="terms" style="margin-top:14px"><div><h4>Default · one panel</h4><p>Every function is audited in front of the others, so answers are heard once and agreed in the same room.</p></div>
<div><h4>Option · parallel breakouts</h4><p>Function by function in separate rooms, if you’d rather each head is challenged privately. Agreed with you before the day.</p></div></div></div></section>'''
cx += f'''<section class="white" id="days"><div class="wrap">{head("how the two days run", "Where do your team’s answers stop holding up?")}
<div class="day four">
<div class="slot c-slate"><time>Before</time><h3>Founder briefing</h3><p>Sensitive topics flagged and ground rules set. Our default is open conversation in the room, on your call.</p></div>
<div class="slot c-green"><time>Day 1</time><h3>Round 1 audits</h3><p>Three functions audited in turn, each by a matched operator, with the founder and the rest of the team watching.</p></div>
<div class="slot c-purple"><time>Evening</time><h3>Downtime, by design</h3><p>People open up on Day 2 because they spent Day 1 being challenged together.</p></div>
<div class="slot c-red"><time>Day 2</time><h3>Round 2 and synthesis</h3><p>The remaining functions audited, then every function’s blind spot named in front of the founder.</p></div>
</div>
<dl class="out" style="margin-top:14px"><div><dt>You get</dt><dd>A findings pack: what each function admitted under challenge, where answers didn’t hold up, and where functions quietly disagreed</dd></div><div><dt>Your business can now</dt><dd>Hear in one room what would otherwise take months of one-on-ones to surface</dd></div><div><dt>Sign-off</dt><dd>An agreed list of findings to act on</dd></div></dl></div></section>'''
cx += '''<section><div class="wrap"><div class="promise c-green"><p class="eyebrow light">the venue</p><h2 class="display">Always offsite. Never your boardroom.</h2>
<p>Choose from our shortlist of partner properties. The distance from the office is deliberate: people say things at a resort they would not say in their own boardroom.</p></div></div></section>'''
cx += f'''<section class="white"><div class="wrap">{head("terms", "How we work together")}
{terms([("Payment","50% at kickoff, 50% on the day."),("Included","5 senior auditors, venue and coordination from our shortlist, meals for both days."),("Not included","Your team’s travel to the venue, rooms or guests beyond the agreed list, alcohol, and any follow-up execution."),("Process","One coordinating lead. Panel confirmed at kickoff. Your function list and the founder briefing agreed a week before."),("What we need from you","The founder for both days, 5–8 function heads for both days, one contact person, and sensitive topics flagged in advance."),("Confidentiality","Nothing said in the room leaves it without agreement. Case references stay anonymised unless you agree in writing."),("Ownership","The findings pack is yours on full payment. We may reuse anonymised learnings and our method."),("Timing","Delays in confirming your function list or the founder’s availability shift the date. Venues outside our shortlist are billed at actuals.")])}</div></section>'''
cx += f'''<section><div class="wrap">{head("next steps", "Getting started")}{steps([("Pick functions and venue","Confirm the function list and choose a property from our shortlist"),("Sign and pay","The kickoff instalment"),("We brief","We confirm the panel and send the founder briefing template")])}</div></section>'''
cx += related("cxo-audit.html") + close("Hear what your team won’t say in the office.", "Tell us which functions you want audited and we’ll match the panel.", "Let’s talk")
