# ================================================================ HOME (v4)
CLIENTS = [("jai-hind-l.jpg","Jai Hind"),("laughing-cow-l.png","The Laughing Cow"),("kisan-l.png","Kissan"),("eva-l.png","Eva"),
 ("good-home-l.png","Good Home"),("one-run-l.png","One Run"),("pitara-l.png","Pitaara"),("png-l.png","PNG Jewellers"),
 ("rasna-l.png","Rasna"),("acc-l.png","ACC"),("mahindra-l.png","Mahindra"),("abbott-l.png","Abbott"),("nirlep-l.png","Nirlep"),
 ("weikfield-l.png","Weikfield"),("sollatek-l.png","Sollatek"),("bindwell-l.png","Bindwel"),("selsun-l.png","Selsun"),
 ("boro-plus-l.png","BoroPlus"),("chipseez-l.png","Chipseez"),("toi-l.png","The Times of India")]
logos = "".join(f'<li><img src="{UP}{f}" alt="{n}" loading="lazy"></li>' for f, n in CLIENTS)

ROT = "brands|founders|profitable sales|recall|leaders"
hm = f'''<section class="hero home-hero">{art("chai","hero-art l")}{art("drum","hero-art r")}<div class="wrap">
<p class="kicker">From Invisible to Irresistible™</p>
<h1 class="giant">We grow <span class="rot" data-rotate="{ROT}">brands</span></h1>
<p class="for">for <b>ambitious owner-managed businesses</b></p>
<p class="lede">Discounts, dealer dependence, a founder nobody outside the industry knows, media that buys sales but not margin. We fix the one that’s holding you back, with products built around a business outcome, not hours billed.</p>
<div class="ctas"><a class="btn" href="#products">See the products</a><a class="btn dark" href="brand-audit.html">Take the free Brand Audit</a></div></div></section>'''
hm += f'''<section class="white logos-sec"><div class="wrap"><p class="eyebrow" style="text-align:center">Trusted clients worldwide</p></div>
<div class="marquee" aria-label="Clients"><ul>{logos}</ul><ul aria-hidden="true">{logos}</ul></div></section>'''

PILLARS = [
 ("1", "Brand-led", "brand", "c-red", "elephant",
  "When buyers can’t tell you from the next supplier, they choose on price. We make you the brand they ask for by name.",
  "Premium pricing and preference that doesn’t depend on a scheme.",
  [("brand-audit.html", "Brand Audit", "Free", "Twenty questions, about ten minutes. Your score out of 40, your tier, and what your two weakest areas cost you."),
   ("brand-positioning.html", "Brand Positioning", "6 weeks", "Discover, Define, Express. Find the reason to choose you that no rival owns, prove it, and launch it in 90 days."),
   ("challenger-workshop.html#leadership", "Challenger Workshop for Leadership", "1 day + plan", "Your leadership team in one room, agreeing the one problem to solve first, with a 90-day plan and named owners."),
   ("challenger-workshop.html#business", "Challenger Workshop for Business", "~7 weeks", "Five weeks of customer, trade and rival evidence first, then the workshop, so the plan is built on facts.")]),
 ("2", "Founder-led", "founder", "c-purple", "pigeon",
  "When the business is ahead of the founder’s public authority, every new buyer, partner and hire starts cold.",
  "Context before contact: conversations that start warm.",
  [("founder-visibility.html#audit", "Founder Authority Audit", "₹10,000", "Where the founder’s authority stands today. Scorecard, gaps and a 90-day opportunity map in 10 working days."),
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
  "An identity, pack and campaign people recognise before they read a word.",
  [("design.html#identity", "Identity System", "On call", "Logo, visual system, typography, colour and guidelines your team and vendors can follow."),
   ("design.html#packaging", "Packaging & Shelf", "On call", "Packs, labels, back-of-pack claims and point-of-sale that justify the price."),
   ("design.html#communication", "Communication Design", "On call", "Print, film and digital assets that say the same thing everywhere.")]),
 ("5", "Leadership-led", "leadership", "c-green", "drum",
  "When the founder hears only what each function head chooses to say, problems surface months too late.",
  "Every function’s blind spot named in one room, in two days.",
  [("cxo-audit.html", "CXO Audit", "2-day offsite", "Senior operators matched to each of your functions challenge your leadership team’s answers, with the founder in the room.")]),
]
cards = ""
for n, name, key, col, a, problem, outcome, prods in PILLARS:
    plist = "".join(
        f'<a class="prod" href="{h}"{" target=\"_blank\" rel=\"noopener\"" if h.startswith("http") else ""}><span class="pt">{t}</span><span class="pm">{m}</span><span class="pd">{d}</span></a>'
        for h, t, m, d in prods)
    cards += f'''<article class="pillar-row" id="{key}"><div class="ptag {col}"><span class="n">{n}</span><h3>{name}</h3><p>{problem}</p><p class="oc"><b>Outcome:</b> {outcome}</p>{art(a)}</div>
<div class="prods{" one" if len(prods)==1 else ""}">{plist}</div></article>'''
hm += f'''<section id="products"><div class="wrap">{head("what we do", "Growth and outcome-based products", "Five ways we grow an owner-managed business. Each product is built around one outcome, priced up front or scoped after a short call, and can be bought on its own.")}
<div class="pillars">{cards}</div></div></section>'''

hm += f'''<section class="cxo-band" id="cxo"><div class="wrap cxo-grid">
<div><p class="eyebrow light">for cxos · leadership-led</p><h2 class="display">Hear what your leadership team won’t say in the office.</h2>
<p class="sub">The CXO Audit is a two-day offsite. Five senior operators, each matched to one of your functions, challenge your heads’ answers with the founder in the room. You leave with every function’s blind spot named, and an agreed list of what to act on.</p>
<div class="ctas" style="justify-content:flex-start"><a class="btn" href="cxo-audit.html">See the CXO Audit</a><a class="btn light" href="{CONTACT}">Talk to us</a></div></div>
<div class="cxo-facts">
<div><span class="v">2</span><span>days at an offsite, never your premises</span></div>
<div><span class="v">5</span><span>senior operators, one per function</span></div>
<div><span class="v">5–8</span><span>function heads audited, live</span></div>
<div><span class="v">1</span><span>findings pack the founder can act on</span></div>
</div></div></section>'''

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
<div class="ctas" style="margin-top:22px"><a class="btn dark" href="https://currynation.in/about-us/">Know more</a><a class="btn light" href="https://currynation.in/work/">Explore our work</a></div></div></section>'''
hm += f'''<section><div class="wrap">{head("case studies", "Real results. Proven impact.")}
<div class="case c-red"><div><span class="k">The Laughing Cow</span><h3>Category creation and new product launch</h3></div>
<div class="awards"><div><b>e4m Indian Marketing Awards</b><span>Category Creation · New Product Launch · 2022</span></div><div><b>Inkspell: Masters of Modern Marketing Awards</b><span>2022</span></div></div></div></div></section>'''
T = [("They don’t just give ads. They give direction.","I’ve had the opportunity to witness their work up close, and what stood out most was Nagessh Pannaswami’s clarity of thought and creative leaps. Nagessh’s ability to distil complex business problems into brand-led solutions is exceptional.","Saket Gore","General Manager, International Business","c-orange"),
 ("A sounding board for all things marketing.","Nagessh is more of a marketing strategist than the stereotypical ad man. His industry know-how, understanding of ground realities by sector and practical outlook made him a good sounding board for marketing, branding and communication strategy.","Deepa Arjunan","Sr. General Manager, Branding","c-teal"),
 ("No silos. Creative problem solving across the business.","They understand not only the brand requirements but also business challenges, and offer many areas of expertise to help us achieve our goals. They are open to engage in all aspects of business and orchestrate a great outcome.","Mustufa Arsiwalla","Marketing Group Manager","c-green")]
tq = "".join(f'<figure class="quote {c}"><h3>{h}</h3><blockquote>{q}</blockquote><figcaption><b>{n}</b><span>/ {r}</span></figcaption></figure>' for h, q, n, r, c in T)
hm += f'''<section class="white"><div class="wrap">{head("testimonials", "Client stories")}<div class="quotes">{tq}</div>
<div class="featured"><span>As featured in</span><b>BestMediaInfo</b><b>The Economic Times</b><b>Business Today</b><b>Campaign</b></div></div></section>'''
hm += close("Let’s talk. Work with us.", "Not sure which product fits? Start with the free Brand Audit, or tell us where growth is stuck and we’ll point you to one next step.", "Take the free Brand Audit", "brand-audit.html")
