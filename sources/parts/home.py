# ================================================================ HOME
CLIENTS = [("jai-hind-l.jpg","Jai Hind"),("laughing-cow-l.png","The Laughing Cow"),("kisan-l.png","Kissan"),("eva-l.png","Eva"),
 ("good-home-l.png","Good Home"),("one-run-l.png","One Run"),("pitara-l.png","Pitaara"),("png-l.png","PNG Jewellers"),
 ("rasna-l.png","Rasna"),("acc-l.png","ACC"),("mahindra-l.png","Mahindra"),("abbott-l.png","Abbott"),("nirlep-l.png","Nirlep"),
 ("weikfield-l.png","Weikfield"),("sollatek-l.png","Sollatek"),("bindwell-l.png","Bindwel"),("selsun-l.png","Selsun"),
 ("boro-plus-l.png","BoroPlus"),("chipseez-l.png","Chipseez"),("toi-l.png","The Times of India")]
logos = "".join(f'<li><img src="{UP}{f}" alt="{n}" loading="lazy"></li>' for f, n in CLIENTS)

hm = f'''<section class="hero home-hero">{art("chai","hero-art l")}{art("drum","hero-art r")}<div class="wrap">
<p class="kicker">Brand transformation for owner-managed businesses</p>
<h1 class="giant">From Invisible to Irresistible™</h1>
<p class="lede">If you’re tired of discounts, dealer dependence, and customers <b>not knowing your name</b>, it’s time to <b>build a brand</b> that commands respect, premium pricing and customer preference. We do it for the business, and for the founder behind it.</p>
<div class="ctas"><a class="btn" href="instant-audit.html">Take the free C2B Audit</a><a class="btn dark" href="founder-visibility.html">Founder Authority Audit</a></div></div></section>'''
hm += f'''<section class="white logos-sec"><div class="wrap"><p class="eyebrow" style="text-align:center">Trusted clients worldwide</p></div>
<div class="marquee" aria-label="Clients"><ul>{logos}</ul><ul aria-hidden="true">{logos}</ul></div></section>'''
hm += f'''<section><div class="wrap">{head("two kinds of invisible", "Which one is costing you?", "Most owner-led businesses have one of two problems, and many have both. We built a product line for each.", True)}
<div class="split">
<a class="half c-red" href="#c2b"><span class="k">C2B · Commodity to Brand</span><h3>Your business is invisible</h3>
<p>Buyers can’t tell you from the next supplier. Dealers decide what sells. Every slow quarter ends in a scheme.</p><span class="go">See C2B programmes</span>{art("elephant")}</a>
<a class="half c-purple" href="#founder"><span class="k">Founder Visibility</span><h3>The founder is invisible</h3>
<p>The business is ahead of the founder’s public authority, so every new buyer, partner or hire starts cold.</p><span class="go">See Founder Visibility</span>{art("pigeon")}</a>
</div></div></section>'''
hm += f'''<section class="white" id="c2b"><div class="wrap pillar">
{head("c2b · commodity to brand", "Turn the business into a brand", "Three programmes for owner-managed commodity businesses. Use them in order or on their own. Every phase ends in one deliverable and one sign-off.")}
<div class="bento flow">
<a class="c-flame" href="instant-audit.html"><span class="k">Step 1 · Diagnose</span><span class="badge">FREE</span><h3>Audit</h3><p>Twenty questions, about ten minutes. Your score out of 40, your tier, and what your two weakest areas cost you.</p><span class="go">Take the audit</span>{art("bell")}</a>
<a class="c-green" href="brand-positioning.html"><span class="k">Step 2 · Position · 6 weeks</span><h3>Brand Positioning</h3><p>Discover, Define, Express. Find the reason to choose you that no rival owns, prove it, and launch it in 90 days.</p><span class="go">See the programme</span>{art("chai")}</a>
<a class="c-red" href="c2b-workshop.html"><span class="k">Step 3 · Align · 1 day</span><h3>UNLIMIT Workshop</h3><p>Five weeks of evidence, one day in the room with your leadership team, a 90-day plan with named owners.</p><span class="go">See the workshop</span>{art("drum")}</a>
</div>
<div class="scale mini">
<div class="tier c-red"><span class="k">AUDIT SCORE 0–12</span><span class="nm">Replaceable</span><span class="to">Start with Brand Positioning</span></div>
<div class="tier c-orange"><span class="k">14–22</span><span class="nm">Compared</span><span class="to">Start with Brand Positioning</span></div>
<div class="tier c-teal"><span class="k">24–30</span><span class="nm">Preferred</span><span class="to">Start with the Workshop</span></div>
<div class="tier c-green"><span class="k">32–40</span><span class="nm">Requested</span><span class="to">Start with the Workshop</span></div>
</div></div></section>'''
hm += f'''<section id="founder"><div class="wrap pillar">
{head("founder visibility · the visible founder", "Give the founder the authority the business has earned", "Founder authority creates context before contact. A staged system that turns private expertise into visible signals, so commercial conversations don’t start cold.")}
<div class="stages">
<a class="stage c-purple" href="founder-visibility.html#audit"><span class="k">Stage 1</span><h3>Authority Audit</h3><span class="price">₹10,000</span><p>Where the founder’s authority stands today. Delivered in 10 working days.</p></a>
<a class="stage c-slate" href="founder-visibility.html#plan"><span class="k">Stage 2</span><h3>Action Plan</h3><span class="price">Scoped on call</span><p>What to build, where to show up, and in what order.</p></a>
<a class="stage c-deep" href="founder-visibility.html#build"><span class="k">Stage 3</span><h3>System Build</h3><span class="price">Scoped on call</span><p>Four weeks: position, narrative, content, profile and an AI workspace.</p></a>
<a class="stage c-teal" href="founder-visibility.html#implement"><span class="k">Stage 4</span><h3>Implement</h3><span class="price">Scoped on call</span><p>Your team runs it, we guide it, or we manage the monthly rhythm.</p></a>
</div>
<div class="ctas" style="justify-content:flex-start"><a class="btn" href="founder-visibility.html">See the Founder Authority System</a></div></div></section>'''
hm += f'''<section class="white"><div class="wrap">{head("about us", "Hi, we’re Curry Nation!")}
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
hm += close("Let’s talk. Work with us.", "Start free with the C2B Audit, or book the Founder Authority Audit. Either way you leave with a clear diagnosis and one next step.", "Take the free C2B Audit", "instant-audit.html")
