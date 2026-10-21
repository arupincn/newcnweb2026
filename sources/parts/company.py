# Company pages replicated from currynation.in: About, Work, Resources, Contact.
# Images are served from currynation.in (the site sends no referrer, so hotlinking is allowed).
from urllib.parse import quote

UP = "https://currynation.in/wp-content/uploads/"
def u(path): return UP + quote(path)

EMAIL = "nagesshp@currynation.in"
PHONE = "+91 9223502716"
TEL = "+919223502716"
ADDRESS = "2nd Floor, Pinnacle Business Park, Mahakali Caves Road, Andheri (E), Mumbai-400093."
SOCIAL = [
 ("Facebook", "https://www.facebook.com/currynation", "f"),
 ("Instagram", "https://www.instagram.com/currynationbrandconversations/", "ig"),
 ("LinkedIn", "https://www.linkedin.com/company/curry-nation/", "in"),
 ("X", "https://x.com/curry_nation", "x"),
 ("YouTube", "https://www.youtube.com/user/CurryNationChannel", "yt"),
]
SOCIAL_SVG = {
 "f": '<path d="M13.5 21v-7.5h2.5l.4-3h-2.9V8.6c0-.9.3-1.5 1.5-1.5h1.5V4.4c-.3 0-1.2-.1-2.2-.1-2.2 0-3.7 1.3-3.7 3.8v2.4H8v3h2.6V21h2.9z"/>',
 "ig": '<path d="M12 7.3A4.7 4.7 0 1 0 12 16.7 4.7 4.7 0 0 0 12 7.3zm0 7.7a3 3 0 1 1 0-6 3 3 0 0 1 0 6zm6-7.9a1.1 1.1 0 1 1-2.2 0 1.1 1.1 0 0 1 2.2 0zM21 8.1c-.1-1.6-.4-3-1.6-4.1C18.3 2.9 16.9 2.5 15.3 2.5 13.6 2.4 10.4 2.4 8.7 2.5 7.1 2.6 5.7 2.9 4.6 4 3.4 5.1 3.1 6.5 3 8.1c-.1 1.7-.1 6.1 0 7.8.1 1.6.4 3 1.6 4.1 1.1 1.1 2.5 1.5 4.1 1.6 1.7.1 4.9.1 6.6 0 1.6-.1 3-.4 4.1-1.6 1.1-1.1 1.5-2.5 1.6-4.1.1-1.7.1-6.1 0-7.8zm-2.1 9.6c-.3.9-1 1.6-1.9 1.9-1.3.5-4.5.4-6 .4s-4.7.1-6-.4c-.9-.3-1.6-1-1.9-1.9-.5-1.3-.4-4.5-.4-6s-.1-4.7.4-6c.3-.9 1-1.6 1.9-1.9 1.3-.5 4.5-.4 6-.4s4.7-.1 6 .4c.9.3 1.6 1 1.9 1.9.5 1.3.4 4.5.4 6s.1 4.7-.4 6z"/>',
 "in": '<path d="M6.9 8.8H3.6V20h3.3V8.8zM5.2 3.5a1.9 1.9 0 1 0 0 3.8 1.9 1.9 0 0 0 0-3.8zM20.4 13.6c0-3-.6-5.1-4.1-5.1-1.7 0-2.8.9-3.2 1.8h-.1V8.8H9.8V20h3.3v-5.5c0-1.5.3-2.9 2.1-2.9 1.8 0 1.8 1.7 1.8 3V20h3.3l.1-6.4z"/>',
 "x": '<path d="M17.8 3h3l-6.6 7.6L22 21h-6.1l-4.8-6.2L5.6 21h-3l7.1-8.1L2.2 3h6.2l4.3 5.7L17.8 3zm-1 16.2h1.7L7.3 4.7H5.5l11.3 14.5z"/>',
 "yt": '<path d="M21.6 7.2a2.5 2.5 0 0 0-1.8-1.8C18.2 5 12 5 12 5s-6.2 0-7.8.4A2.5 2.5 0 0 0 2.4 7.2C2 8.8 2 12 2 12s0 3.2.4 4.8a2.5 2.5 0 0 0 1.8 1.8C5.8 19 12 19 12 19s6.2 0 7.8-.4a2.5 2.5 0 0 0 1.8-1.8c.4-1.6.4-4.8.4-4.8s0-3.2-.4-4.8zM10 15V9l5.2 3L10 15z"/>',
}
def social_row(cls="social"):
    return f'<div class="{cls}">' + "".join(
        f'<a href="{h}" target="_blank" rel="noopener" aria-label="Curry Nation on {n}"><svg viewBox="0 0 24 24" aria-hidden="true">{SOCIAL_SVG[k]}</svg></a>' for n, h, k in SOCIAL) + "</div>"

PRESS = [("eco-times.svg", "The Economic Times"), ("best-media-info.svg", "Best Media Info"), ("business-today.svg", "Business Today"), ("campaign.svg", "Campaign")]
def press_band():
    logos = "".join(f'<div><img src="{u("2025/05/" + f)}" alt="{n}" loading="lazy"></div>' for f, n in PRESS)
    return f'''<section class="press-band"><div class="wrap press-grid">
<div><h2 class="press-h">As featured in</h2><div class="press">{logos}</div></div>
<img class="press-art" src="{u("2025/05/footer-svg-new.svg")}" alt="" loading="lazy"></div></section>'''

def co_hero(bg, h1, lede, art, ink="#232323"):
    return f'''<section class="co-hero" style="--hbg:{bg};--hink:{ink}"><div class="wrap co-hero-grid">
<div><h1 class="co-h1">{h1}</h1><p class="co-lede">{lede}</p></div>
<img class="co-art" src="{u(art)}" alt="" width="320" height="320"></div></section>'''

# ================================================================ ABOUT
TEAM = [
 ("Team.png", "Priti Nair", "Director", [
  "Priti is a self-confessed lover of food, cooking, working out, watching crime and supernatural serials and carom (not necessarily in that order). She’s also a lover of animals and little children; and gets immense joy helping the underprivileged – especially children. Alternate reality (sorry to disappoint, but not the digital kind) fascinates Priti and she’s a huge believer in things beyond.",
  "Priti likes to be happy (who doesn’t), so doesn’t let most things and people bother her. She likes to be with people who make her laugh; and can’t stand people who are full of themselves. (So stay away, if you’re one.)",
  "Now here’s where the inspiration for Curry-Nation comes from – Priti is very, very proud of India and specially the textured nature of its food and people. She hates when pseudo intellectual sorts have anti India viewpoints.",
  "All in all Priti is happy at the agency called Curry–Nation."]),
 ("Team-1.png", "Nagessh Pannaswami", "Director", [
  "Nagessh’s philosophy is: ‘Live to fill the years with life, not to fill life with years.’",
  "He’s a person, doing person things.",
  "Having seen so much in life Nagessh understands the importance of being a good human being; and of listening and observing – the said and the unsaid.",
  "Nagessh stumbled upon advertising serendipitously and it continues to throw up surprises and new experiences, even to this date after 30 long years. It lets him be an explorer, a creator, a judge and a warrior – all at the same time.",
  "At Curry-Nation there’s never a dearth of fun, food and freedom – the three primary reasons for existence for most human beings, and also for curry-nation as an agency.",
  "All these are available in varied textures. So the spicier the food, the spicier is life for Nagessh."]),
 ("Team-2-1.png", "Cedric D’Souza", "Business Brand Management", [
  "Metalhead by night. Client whisperer by day.",
  "With 16 years of experience in advertising, Cedric brings a high-energy, hands-on approach to everything he touches. From Eva Deodorants and Rasna to Good Home and BKT Tires, he’s helped steer some of the wildest campaigns to the finish line.",
  "Fueled by masala chai and the newest gadgets, Cedric has a knack for turning chaos into structure—and delivering under pressure without missing a beat."]),
 ("Team-3.png", "Kushal Lingayat", "Finance", [
  "A true foodie at heart, he’s always on the lookout for exciting new flavours around town—feeding his never-ending appetite for culinary adventure.",
  "When he’s not indulging his taste buds, you’ll find him chasing sunsets on offbeat trails, soaking in nature, tuning into his favourite tracks, or breaking a sweat on the field."]),
 ("Team-4.png", "Vikrant Dange", "Creative Brand Management", [
  "Thinking and writing is a continuous job. Location or condition hardly counts. Family vacations, wild trips, washroom affairs… your brain is always ticking. Mostly instinctual. Partly conscious. Wordsmiths, won’t you admit? I know. I do.",
  "From banking to gaming, fashion to hospitality, commodity to FMCG, Indian to multinational – each industry has had a stirring impact on my writing skills and my capability to think original.",
  "A work history spanning across 20 monsoons, I am thankful that I got to work on big brands such as Rasna, Loksatta, Colors Marathi, Laughing Cow, SBI, LIC, Camlin, Piaggio, Rich’s, BKT… a portfolio with fair and fitting communication solutions that saw our accounts flourish, and a handful of awards that brought joy to my soul.",
  "*At this point, allow this wordsmith to ask you: did you mark that this straight-forward, dull looking bio is without an ‘e’?"]),
 ("Team-5.png", "Satish Bansode", "Creative Brand Management", [
  "Satish approaches life with a refreshing straightforwardness and level-headed demeanour. He sees the world as rich with opportunities and experiences waiting to be seized.",
  "An adventurous spirit at heart, Satish thrives on new challenges that fuel his drive for excellence. His enthusiasm for tackling unfamiliar territory has become a hallmark of his professional approach.",
  "Satish lives by a core philosophy: one should continuously pursue personal growth and improvement. This belief propels him forward, unafraid to begin where others might conclude their journey.",
  "His combination of pragmatism, adventurous spirit, and commitment to constant improvement makes him a valuable asset to our team at Curry Nation."]),
 ("Team-6.png", "Devendra Singh", "Creative Brand Management", [
  "With over two decades in advertising, Devendra has done it all—print, digital, TV, and even a bit of crime (fictional, of course). From shaping campaigns for Reliance-Zapak and NDTV Imagine to bringing stories alive on Crime Alert for Dangal TV, his journey has been anything but ordinary.",
  "He’s dabbled in film publicity, dived into production design at Marching Ants, and recently added “FTII-trained director” to his list with a course in Film Direction. A short stint in Hyderabad, he has now found his way back to his beloved Mumbai, he will bring bold ideas, sharp storytelling, and relentless curiosity to every creative brief."]),
 ("Team-7.png", "Pooja Sawant", "Digital Content Strategist & Producer", [
  "Pooja Sawant is a storyteller at heart and a strategist by craft. With a background in theatre and a deep love for all things shoot—videos, photos, styling, and set design—she thrives where creativity meets content. From styling the perfect frame to shaping full-fledged digital campaigns, she’s done it all (and done it well). Having worked with 35+ brands, Pooja brings a hands-on, art-meets-strategy approach to everything she touches, always chasing that sweet spot where visual appeal meets real impact."]),
 ("Team-8.png", "Vishal Pawar", "Creative Brand Management", [
  "His career in advertising kick started with Comart and then followed Leo Burnett, Bates and now Curry-Nation. His 20 years stint in advertising has given him a chance to work on brands like Radio City, McDonalds, Tata AIG, Sony entertainment television and many more. Vishal says nature inspires him a lot and that’s why he loves travelling and adventure. His weekends are mostly spent playing Volleyball and Cricket. Along with his work, travelling and sports he never misses to update his Facebook status."]),
 ("Team-9.png", "Mohit Mordani", "Business Brand Manager", [
  "By day, Mohit is the brand world’s Batman—rescuing teams from client chaos with strategy, speed, and just the right punchline. He blends sharp thinking with superhero stamina to build brands that stand out and stay strong.",
  "Outside the boardroom, Mohit is a creative soul who finds joy in writing, reading, and geeking out over all things DC (yes, he is the Batman of the office). A self-declared foodie, he doesn’t shy away from having ice cream for breakfast (Provided its Sunday)—because why not? When he’s not lifting ideas, he’s lifting weights—gym sessions are sacred, and travel plans are always brewing.",
  "Despite all the action, this caped crusader calls it a day like clockwork—lights out at 9:30 PM, baby-snores included."]),
 ("Team-10.png", "Mihir Janwalkar", "Digital Content Strategist", [
  "With a keen eye for impactful ideas and meaningful storytelling. He enjoys crafting thoughtful campaigns, building strong client relationships, and translating brand goals into engaging digital narratives. With a calm and collaborative approach, Mihir focuses on strategies that connect authentically—both with audiences and partners. His work is rooted in creativity, consistency, and a genuine passion for helping brands grow."]),
 ("Team-11.png", "Navin", "Head of Digital Business", [
  "Addicted to Campaign Highs & Strategic Serotonin.",
  "While the world clocks into a 9-to-5, he’s already deep into a 5-to-9 — decoding data, plotting brand coups, and turning briefs into full-blown business blueprints. People usually start their mornings with chai and a run. Navin starts his with black coffee and a campaign rollout.",
  "Offline. Online. On-ground. In-air. If there’s a touchpoint, he’ll turn it into a turning point. Obsessed with impact, allergic to mediocrity, Navin’s the guy who treats every campaign like a blockbuster and every brand like a legacy in the making.",
  "He might skip meals, but never a strategic insight.",
  "His addictions? Branding that sticks. Strategies that scale. And coffee. Lots of it."]),
]
GALLERY = [28, 29, 30, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
AWARDS = [
 (1, "2024", "Silver Award in LACP’S Annual Report Competition, The 2019 Vision Award", "Ambuja Cements Limited"),
 (2, "2022", "The Laughing Cow Cheese", "The Laughing Cow Cheese"),
 (3, "2022", "Inkspell - Masters of Modern Marketing Awards", "The Laughing Cow Cheese"),
 (4, "2022", "Pune Short Film Festival", "Ambuja Cement Limited"),
 (5, "2020", "Silver Awards in National Creative Excellence Awards", "Laadli"),
 (6, "2019", "Times Group Power of Print", "Times Group / Croma"),
 (7, "2018", "Times Group Power of Print", "Times Group / Nestlé"),
 (8, "2014", "Creative Abby Awards at Goafest", "Nirlep"),
 (9, "2014", "Creative Abby Awards at Abby", "Masoom Night School"),
 (10, "2014", "Creative Abby Awards at Abby", "Taste for Life"),
 (11, "2014", "Kyoorius", "Taste for Life"),
 (12, "2014", "Kyoorius", "Taste for Life"),
]
VALUES = [("Clarity Before Creativity", "We believe sharp strategy must lead creative execution."),
 ("Speed Over Perfection", "Done is better than perfect — we prioritize momentum."),
 ("People Over Process", "Human insight beats checklists. We value intuition, empathy, and instinct."),
 ("Relationships Over Revenue", "We choose long-term trust over short-term wins."),
 ("Challenger Thinking Always", "We punch above our weight — and help our clients do the same."),
 ("Results. Not Just Campaigns.", "Every brand move must drive impact — be it recall, margins, or conversion.")]

def about_page():
    p = f'''<section class="ab-video"><img src="{u("2025/05/about-gallery2.png")}" alt="The Curry Nation team at the studio"></section>
<section class="ab-intro"><div class="wrap ab-intro-grid">
<img src="{u("2025/05/about-currynation.jpg")}" alt="The Curry Nation team" loading="lazy">
<div><h1 class="co-h1 sm">About Curry Nation</h1><p>From PNG Jewellers to BKT, Sollatek, RL Steel to Bindwel &amp; many more — we’ve helped businesses like yours become the brand everyone’s talking about.</p>
<div class="ctas left"><a class="btn dark" href="contact.html">Let’s Connect</a></div></div></div></section>
<section class="white"><div class="wrap areare">
<div class="aren"><h2>What We Aren’t</h2><ul>
<li>A generic agency that delivers one-size-fits-all solutions.</li><li>Stuck in outdated methods, unable to adapt to the market.</li><li>Focused on short-term ads with no lasting impact.</li><li>Here to offer quick fixes, not lasting brand value.</li></ul></div>
<div class="are"><h2>What We Are</h2><ul>
<li>Build brands that outsell the competition.</li><li>Drive demand that pulls, not pushes.</li><li>Help you charge a premium without apology.</li><li>Give your next generation a brand worth inheriting.</li></ul></div></div></section>
<section><div class="wrap corner">
<div class="corner-l"><p class="eyebrow">curry corner</p><h2 class="corner-h">We’re not just an ad agency. We’re India’s only brand transformation partner focused exclusively on owner-managed commodity businesses.</h2>
<img src="{u("2025/05/cutting-Chai-about.svg")}" alt="" loading="lazy"></div>
<div class="corner-r">
<h3>Our Mission</h3><p>To create category-defining branding strategies for owner-managed companies in commodity sectors like steel, plywood, cement, salt, cooking oil, and footwear — enabling them to gain visibility, build customer preference, and increase profitability through the power of branding.</p>
<h3>Our Vision</h3><p>To be the go-to agency for owner-managed commodity businesses, transforming them from trade-dependent players into irresistible customer demanded brands.</p><p class="unig">“We WILL make commodity businesses UNIGNORABLE.”</p>
<h3>Our Values</h3><dl class="vals">{"".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in VALUES)}</dl>
<h3>Our Philosophy</h3><p>At Curry Nation, we believe that branding is not a luxury — it is a survival strategy for commodity businesses in today’s hypercompetitive world. While most agencies chase glamour or startups, we’ve chosen to stand with the builders of real India — the owner-managed companies who’ve built their businesses brick by brick. Our work is rooted in the belief that every product, no matter how commoditized, has the potential to become iconic — if it is guided by strategy, storytelling, and courage. We don’t just build brands — we spark movements inside businesses, turning overlooked products into category leaders, and invisible businesses into household names.</p>
</div></div>
<div class="wrap"><div class="counts">
<div class="c-orange"><span class="k">Years</span><span class="v">15+</span></div>
<div class="c-teal"><span class="k">Projects</span><span class="v">300+</span></div>
<div class="c-deep"><span class="k">Awards</span><span class="v">50+</span></div>
<div class="c-red"><span class="k">Clients</span><span class="v">100+</span></div></div></div></section>'''
    cards = ""
    for img, name, role, bio in TEAM:
        paras = "".join(f"<p>{x}</p>" for x in bio)
        cards += f'''<article class="tm"><img src="{u("2025/05/" + img)}" alt="{name}" loading="lazy" width="120" height="120"><h3>{name}</h3><p class="role">{role}</p>
<details><summary>Read more</summary><div class="bio">{paras}</div></details></article>'''
    p += f'''<section class="team-band" id="team"><div class="wrap"><div class="big-head"><p class="eyebrow">team</p><h2><span>Meet</span> <span class="g">Our Team</span></h2></div>
<div class="team">{cards}</div></div></section>'''
    gal = "".join(f'<img src="{u(f"2025/05/about-gallery{n}.png")}" alt="Life at Curry Nation" loading="lazy">' for n in GALLERY)
    p += f'<section class="white gal-sec" aria-label="Life at Curry Nation"><div class="gal">{gal}</div></section>'
    aw = "".join(f'''<figure class="awc"><div class="awc-img"><img src="{u(f"2025/05/award{n}.png")}" alt="{t}" loading="lazy"></div><figcaption><b>{y}</b><span>{t}</span><em>{c}</em></figcaption></figure>''' for n, y, t, c in AWARDS)
    p += f'''<section class="white" id="awards"><div class="wrap"><div class="big-head left"><p class="eyebrow">awards</p><h2><span class="o">Awards &amp;</span> <span>Recognition</span></h2></div>
<div class="awgrid">{aw}</div></div></section>'''
    p += press_band()
    return p

# ================================================================ WORK
WORK = [
 ("mewar-by-jaihind", "Mewar by JAIHIND", "Retail", "2025/07/Untitled-design-8.png"),
 ("jaihind", "JAIHIND", "Retail", "2025/05/jai-hind-1.png"),
 ("the-laughing-cow", "The Laughing Cow", "Food", "2025/05/the-laughing-cow.png"),
 ("kissan-konnect", "Kissan Konnect", "Commodity, Food", "2025/05/kisan-konnect.png"),
 ("eva", "Eva", "FMCG", "2025/05/eva.png"),
 ("good-home", "Good Home", "Commodity, FMCG", "2025/05/good-home.png"),
 ("on-the-run", "On The Run", "Food", "2025/05/on-the-run.png"),
 ("pitaara", "Pitaara", "Commodity, Food", "2025/05/pitaara.png"),
 ("indica-hair-color", "Indica Hair Color", "FMCG", "2025/05/indica-hair-color.png"),
 ("pn-gadgil-jewellers", "PN Gadgil Jewellers", "Retail", "2025/05/pn-gadgil-jewellers.png"),
 ("colors-marathi", "Colors Marathi", "Media & Entertainment", "2025/05/colors-marathi.png"),
 ("acc-2", "ACC", "Commodity", "2025/05/acc.png"),
 ("mittal", "Mittal", "Commodity", "2025/05/mittal.png"),
 ("sollatek", "Sollatek", "Commodity", "2025/05/sollatek.png"),
 ("rl-steel", "RL Steel", "Commodity", "2025/05/rl-steel.png"),
 ("bindwel", "Bindwel", "Commodity", "2025/05/bindwel.png"),
 ("abp-weddings", "ABP Weddings", "Retail", "2025/05/abp-weddings.png"),
 ("hometown", "HomeTown", "Retail", "2025/05/hometown.png"),
 ("asian-heart-institute", "Asian Heart Institute", "Retail", "2025/05/asian-heart-institute.png"),
 ("711-2", "711", "Retail", "2025/05/711.png"),
 ("limcee", "Limcee", "Retail", "2025/05/Limcee-369-x-313-mm.png"),
 ("melaglow", "Melaglow", "Retail", "2025/05/melaglow.png"),
 ("spinz", "Spinz", "FMCG", "2025/05/spinz.png"),
 ("boroplus", "BoroPlus", "FMCG", "2025/05/boroplus.png"),
 ("netsurf", "Netsurf", "FMCG", "2025/05/netsurf.png"),
 ("vasocare", "Emami Vasocare", "FMCG", "2025/05/vasocare.png"),
 ("fairever", "Fairever", "FMCG", "2025/05/fairever.png"),
 ("krishna-thulasi", "Krishna Thulasi", "FMCG", "2025/05/krishna-thulasi.png"),
 ("18-again", "18 Again", "FMCG", "2025/05/18-again.png"),
 ("selsun", "Selsun", "FMCG", "2025/05/selsun-1.png"),
 ("mosil", "Mosil", "FMCG", "2025/05/mosil-1.png"),
 ("rasna", "Rasna", "Food", "2025/05/rasna-2.png"),
 ("dinshaws", "Dinshaws", "Food", "2025/05/dinshaws.png"),
 ("saii-dairy", "Saii Dairy", "Food", "2025/05/saii-dairy.png"),
 ("kinder-joy", "Kinder Joy", "Food", "2025/05/kinder-joy.png"),
 ("chipseez", "Chipseez", "Food", "2025/05/chipseez.png"),
 ("naturals", "Naturals", "Food", "2025/05/naturals.png"),
 ("taste-for-life", "Taste for Life", "Food", "2025/05/taste-for-life.png"),
 ("richs", "Rich’s", "Food", "2025/05/richs.png"),
 ("loksatta", "Loksatta", "Media & Entertainment", "2025/05/loksatta.png"),
 ("the-times-of-india", "The Times of India", "Media & Entertainment", "2025/05/the-times-of-india.png"),
 ("brand-capital", "Brand Capital", "Media & Entertainment", "2025/05/brand-capital.png"),
]
WORK_CATS = ["Commodity", "Retail", "FMCG", "Food", "Media & Entertainment"]
def slug(c): return c.lower().replace(" & ", "-").replace(" ", "-")

def work_page():
    p = co_hero("var(--lime)", "Our Work", "At Curry Nation, our creatives might not sketch rangolis at home, but their designs resonate just as deeply. Trained at top Indian art schools, our team crafts visuals that combine culture and creativity effortlessly. From vibrant campaigns to insightful stories, every piece in our portfolio celebrates India's eclectic spirit—explore some of our best.", "2025/05/Elephant-work.svg")
    tabs = '<button type="button" class="on" data-f="all">All Work</button>' + "".join(f'<button type="button" data-f="{slug(c)}">{c.replace("&", "&amp;")}</button>' for c in WORK_CATS)
    items = ""
    for s, n, cat, img in WORK:
        cs = " ".join(slug(c.strip()) for c in cat.split(","))
        items += f'''<button type="button" class="wk" data-c="{cs}" data-n="{n}" data-k="{cat.replace("&", "&amp;")}"><span class="wk-img"><img src="{u(img)}" alt="{n}" loading="lazy"></span><b>{n}</b><span class="wk-c">/ {cat.replace("&", "&amp;")}</span></button>'''
    p += f'''<section class="white"><div class="wrap"><div class="ftabs" role="group" aria-label="Filter work">{tabs}</div>
<div class="wkgrid">{items}</div><p class="note wk-none" hidden>No work in this category yet.</p></div></section>
<dialog class="wkbox" aria-label="Project"><button type="button" class="wkx" aria-label="Close">×</button><img alt=""><div class="wkt"><b></b><span></span><a class="btn" href="contact.html">Want work like this? Let’s talk</a></div></dialog>'''
    p += press_band()
    return p

WORK_JS = r'''<script>(function(){var b=document.querySelectorAll('.ftabs button'),it=document.querySelectorAll('.wk');b.forEach(function(x){x.addEventListener('click',function(){b.forEach(function(y){y.classList.toggle('on',y===x);y.setAttribute('aria-pressed',y===x)});var f=x.dataset.f,n=0;it.forEach(function(i){var s=f==='all'||(' '+i.dataset.c+' ').indexOf(' '+f+' ')>-1;i.hidden=!s;if(s)n++});document.querySelector('.wk-none').hidden=n>0})});var d=document.querySelector('.wkbox');if(d&&d.showModal){it.forEach(function(i){i.addEventListener('click',function(){var g=i.querySelector('img');d.querySelector('img').src=g.src;d.querySelector('img').alt=i.dataset.n;d.querySelector('.wkt b').textContent=i.dataset.n;d.querySelector('.wkt span').innerHTML='/ '+i.dataset.k;d.showModal()})});d.querySelector('.wkx').onclick=function(){d.close()};d.addEventListener('click',function(e){if(e.target===d)d.close()})}})();</script>'''

# ================================================================ RESOURCES
EBOOKS = [
 ("Customer Insights & Strategy", "2025/05/Resources.png", ""),
 ("B2B Buyer Persona Guide", "2025/05/Resources-2.png", ""),
 ("User Interview Guide", "2025/05/Resources-3.png", "2025/07/User-Interview-Guide.pdf"),
 ("ICP Template for B2B Owner-Managed Commodity Businesses", "2025/05/Resources-4.png", "2025/07/ICP-Template-for-B2B-Owner-Managed-Commodity-Businesses.pdf"),
 ("ICP Template for B2C Marketing of Owner-Managed Commodity Businesses", "2025/05/Resources-5.png", ""),
 ("Ultimate Guide to Finding the Right ICP", "2025/05/Resources-6.png", "2025/07/Ultimate-Guide-to-Finding-the-Right-ICP-.pdf"),
 ("Brand Development & Positioning", "2025/05/Resources-7.png", ""),
 ("A Practical Guide to Understanding Your Commodity Product Before Branding It", "2025/05/Resources-8.png", "2025/07/A-Practical-Guide-to-Understanding-Your-Commodity-Product-Before-Branding-It.pdf"),
 ("Brand Book Template", "2025/05/Resources-9.png", ""),
 ("Branding Brief Template", "2025/05/Resources-10.png", ""),
 ("Core Value Proposition (CVP)", "2025/05/Resources-11.png", "2025/07/Core-Value-Proposition-CVP-Workbook.pdf"),
 ("Inbound Marketing & Tracking for Commodity Businesses", "2025/07/International-case-studies-header.png", "2025/07/Inbound-Marketing-Tracking-for-Commodity-Businesses.pdf"),
]
CASES_IN = [
 ("How Havells electrified a commodity market & became a power brand", "2025/07/WhatsApp-Image-2025-07-23-at-15.43.24_a0e2b8b8.jpg", "2025/07/HOW-HAVELLS-ELECTRIFIED-A-COMMODITY-MARKET-BECAME-A-POWER-BRAND.pdf"),
 ("How Camlin redefined a commodity & became a household name", "2025/07/WhatsApp-Image-2025-07-23-at-15.53.26_45b43a83.jpg", "2025/04/HOW-CAMLIN-REDEFINED-A-COMMODITY-BECAME-A-HOUSEHOLD-NAME.pdf"),
 ("How Fevikwik turned a one-second solution into a lifetime brand", "2025/07/WhatsApp-Image-2025-07-23-at-15.55.59_478e723b.jpg", "2025/07/HOW-FEVIKWIK-TURNED-A-ONE-SECOND-SOLUTION-INTO-A-LIFETIME-BRAND.pdf"),
 ("How Bisleri’s camel TVC made India ask for water by name", "2025/07/WhatsApp-Image-2025-07-23-at-15.59.43_652f8e87.jpg", "2025/07/HOW-BISLERIS-CAMEL-TVC-MADE-INDIA-ASK-FOR-WATER-BY-NAME.pdf"),
 ("How Saint-Gobain became a premium choice", "2025/07/WhatsApp-Image-2025-07-23-at-18.07.04_6134001b.jpg", "2025/07/HOW-SAINT-GOBAINS-BECAME-A-PREMIUM-CHOICE.pdf"),
 ("How Asian Paints made colours meaningful & became a category leader", "2025/07/WhatsApp-Image-2025-07-23-at-18.14.05_523862e9.jpg", "2025/07/HOW-ASIAN-PAINTS-MADE-COLOURS-MEANINGFUL-BECAME-A-CATEGORY-LEADER.pdf"),
 ("How UltraTech Cement built an unbreakable brand", "2025/07/WhatsApp-Image-2025-07-23-at-18.15.36_81fa3800.jpg", "2025/07/HOW-ULTRATECH-CEMENT-BUILT-AN-UNBREAKABLE-BRAND.pdf"),
 ("How Tata Salt turned a commodity into India’s most trusted brand", "2025/07/WhatsApp-Image-2025-07-23-at-18.18.32_2fd292ba.jpg", "2025/07/HOW-TATA-SALT-TURNED-A-COMMODITY-INTO-INDIAS-MOST-TRUSTED-BRAND.pdf"),
 ("How Madhur Sugar turned a basic commodity into a trusted household brand", "2025/07/WhatsApp-Image-2025-07-23-at-18.24.37_4ece6462.jpg", "2025/07/HOW-MADHUR-SUGAR-TURNED-A-BASIC-COMMODITY-INTO-A-TRUSTED-HOUSEHOLD-BRAND.pdf"),
 ("How Annapurna Atta built a powerful brand", "2025/07/WhatsApp-Image-2025-07-23-at-18.26.16_b3323adc.jpg", "2025/07/HOW-ANNAPURNA-ATTA-BUILT-A-POWERFUL-BRAND.pdf"),
 ("How Century Ply built a powerhouse brand in a ‘no-brand’ market", "2025/07/WhatsApp-Image-2025-07-23-at-18.28.08_3f0552ac.jpg", "2025/08/HOW-CENTURY-PLY-BUILT-A-POWERHOUSE-BRAND-IN-A-NO-BRAND-MARKET.pdf"),
 ("How Captain Cook Salt challenged a monopoly and won", "2025/07/WhatsApp-Image-2025-07-23-at-18.31.18_e8a746cf.jpg", "2025/07/HOW-CAPTAIN-COOK-SALT-CHALLENGED-A-MONOPOLY-AND-WON.pdf"),
]
CASES_INTL = [
 ("How ‘Who Gives A Crap’ turned toilet paper into a cult brand", "assets/res-intl-1.jpg", "2025/07/HOW-‘WHO-GIVES-A-CRAP-TURNED-TOILET-PAPER-INTO-A-CULT-BRAND.pdf"),
 ("How ‘Got Milk?’ turned a commodity into a cultural icon", "assets/res-intl-2.jpg", "2025/07/HOW-‘GOT-MILK-TURNED-A-COMMODITY-INTO-A-CULTURAL-ICON.pdf"),
 ("How California Almonds turned a generic nut into a global superfood", "assets/res-intl-3.jpg", "2025/07/HOW-CALIFORNIA-ALMONDS-TURNED-A-GENERIC-NUT-INTO-A-GLOBAL-SUPERFOOD.pdf"),
 ("How Liquid Death turned water into a rebellious lifestyle brand", "assets/res-intl-4.jpg", "2025/07/HOW-LIQUID-DEATH-TURNED-WATER-INTO-A-REBELLIOUS-LIFESTYLE-BRAND.pdf"),
 ("How Zespri turned kiwi from a forgotten fruit into a global power brand", "assets/res-intl-5.jpg", "2025/07/HOW-ZESPRI-TURNED-KIWI-FROM-A-FORGOTTEN-FRUIT-INTO-A-GLOBAL-POWER-BRAND.pdf"),
]
RES_GROUPS = [("ebooks", "e-Books", EBOOKS), ("cases", "Case Studies", CASES_IN), ("intl", "International Case Studies", CASES_INTL)]

def resources_page():
    p = co_hero("#25abe0", "Free Resources", "<b>Marketing Tools for the Real Builders of Bharat.</b> Free brand-building resources for owner-managed commodity businesses. Break free from price wars and low visibility with templates, and strategies designed to help you build a brand customers ask for by name. No fluff. Just practical tools, templates, and frameworks to help you grow from invisible to irresistible.", "2025/05/Dabba.svg")
    tabs = '<button type="button" class="on" data-f="all">All Resources</button>' + "".join(f'<button type="button" data-f="{k}">{n}</button>' for k, n, _ in RES_GROUPS)
    items = ""
    for k, _, lst in RES_GROUPS:
        for t, img, pdf in lst:
            href = u(pdf) if pdf else ""
            items += f'''<button type="button" class="rs" data-c="{k}" data-t="{t.replace('"', "&quot;")}" data-pdf="{href}"><span class="rs-img"><img src="{img if img.startswith('assets/') else u(img)}" alt="" loading="lazy"></span><b>{t}</b><span class="rs-dl">Download free ↓</span></button>'''
    p += f'''<section class="white"><div class="wrap"><div class="ftabs" role="group" aria-label="Filter resources">{tabs}</div>
<div class="rsgrid">{items}</div></div></section>'''
    p += f'''<dialog class="dl" id="dl" aria-labelledby="dl-h"><form name="resource-download" method="POST" data-netlify="true" netlify-honeypot="bot-field" class="dl-form">
<input type="hidden" name="form-name" value="resource-download"><input type="hidden" name="resource" value="">
<p class="hide"><label>Leave this empty <input name="bot-field"></label></p>
<button type="button" class="dl-x" aria-label="Close">×</button>
<p class="eyebrow">free resources</p><h2 id="dl-h"><span class="dim">Sign up</span> to download</h2><p class="dl-t"></p>
<label>Hi! My name is<input name="name" required placeholder="Type your name*" autocomplete="name"></label>
<label>Designation<input name="designation" required placeholder="Type your designation*" autocomplete="organization-title"></label>
<label>Industry<input name="industry" required placeholder="Type your industry*"></label>
<label>Feel free to contact me on<input name="phone" type="tel" required placeholder="Type your contact number*" autocomplete="tel"></label>
<label>You can also reach me at<input name="email" type="email" required placeholder="Type your contact email*" autocomplete="email"></label>
<label class="chk"><input type="checkbox" name="updates" value="yes"> By checking this, you agree to receive updates on email.</label>
<button class="btn dark" type="submit">Download Now</button><p class="dl-msg" role="status"></p></form></dialog>'''
    p += press_band()
    return p

RES_JS = r'''<script>(function(){
var b=document.querySelectorAll('.ftabs button'),it=document.querySelectorAll('.rs');b.forEach(function(x){x.addEventListener('click',function(){b.forEach(function(y){y.classList.toggle('on',y===x);y.setAttribute('aria-pressed',y===x)});var f=x.dataset.f;it.forEach(function(i){i.hidden=!(f==='all'||i.dataset.c===f)})})});
var d=document.getElementById('dl'),f=d.querySelector('form'),msg=d.querySelector('.dl-msg'),cur=null;
it.forEach(function(i){i.addEventListener('click',function(){cur=i;f.reset();msg.textContent='';f.resource.value=i.dataset.t;d.querySelector('.dl-t').textContent=i.dataset.t;d.showModal()})});
d.querySelector('.dl-x').addEventListener('click',function(){d.close()});
d.addEventListener('click',function(e){if(e.target===d)d.close()});
function done(){var pdf=cur&&cur.dataset.pdf;if(pdf){msg.textContent='Thank you! Your download is opening.';window.open(pdf,'_blank','noopener')}else{msg.textContent='Thank you! We’ll email this resource to you shortly.'}}
f.addEventListener('submit',function(e){e.preventDefault();var body=new URLSearchParams(new FormData(f)).toString();fetch('/',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:body}).then(done,done)});
})();</script>'''

# ================================================================ CONTACT
def contact_page():
    p = co_hero("var(--yellow)", "Contact Us", "“GIVE A SHOUT!”—An Indian tradition that's charming but noisy. Thankfully, Curry Nation has evolved beyond yelling from courtyards or beneath balconies. With a clearly mapped office, reliable phone lines, and prompt emails, connecting with us is easy, friendly, and refreshingly quiet.", "2025/05/kabootar.svg")
    p += f'''<section class="ct-red"><div class="wrap ct-center">
<p class="eyebrow">say hello</p><h2 class="ct-h">Let’s build something <span>amazing together!</span></h2>
<div class="ct-card"><h3>Nagessh Pannaswami</h3><p>{ADDRESS}</p><p><a href="mailto:{EMAIL}">{EMAIL}</a></p><p><a href="tel:{TEL}">{PHONE}</a></p></div>
<h3 class="ct-follow">Follow Us</h3>{social_row("social big")}</div>
<img class="ct-mask" src="{u("2025/05/masks-final.svg")}" alt="" loading="lazy"></section>
<section class="ct-lime" id="form"><div class="wrap ct-center">
<p class="eyebrow">connect</p><h2 class="ct-h"><span class="g">Customer</span> area</h2>
<form class="ct-form" name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field" action="contact.html?sent=1#form">
<input type="hidden" name="form-name" value="contact"><p class="hide"><label>Leave this empty <input name="bot-field"></label></p>
<label>Hi! My name is<input name="name" required placeholder="Type your name*" autocomplete="name"></label>
<label>Feel free to contact us on<input name="phone" type="tel" required placeholder="Type your contact number*" autocomplete="tel"></label>
<label>You can also reach us at<input name="email" type="email" required placeholder="Type your contact email*" autocomplete="email"></label>
<label>Want to say something?<textarea name="message" rows="4" placeholder="Type your message"></textarea></label>
<div class="ctas"><button class="btn dark" type="submit">Send a Message</button></div><p class="ct-msg" role="status"></p></form></div></section>'''
    p += press_band()
    return p

CONTACT_JS = r'''<script>(function(){var f=document.querySelector('.ct-form'),m=document.querySelector('.ct-msg');if(/sent=1/.test(location.search))m.textContent='Thank you! We’ll get back to you soon.';
f.addEventListener('submit',function(e){e.preventDefault();var body=new URLSearchParams(new FormData(f)).toString();
fetch('/',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:body}).then(function(r){if(!r.ok)throw 0;f.reset();m.textContent='Thank you! We’ll get back to you soon.'}).catch(function(){var d=new FormData(f);location.href='mailto:nagesshp@currynation.in?subject='+encodeURIComponent('Enquiry from '+(d.get('name')||'the website'))+'&body='+encodeURIComponent((d.get('message')||'')+'\n\n'+(d.get('name')||'')+'\n'+(d.get('phone')||'')+'\n'+(d.get('email')||''))})});})();</script>'''
