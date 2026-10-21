# FAQs per page (v12). Answers use only facts already stated on the site's pages and terms.
import json, re, html as _h

FAQ = {}

FAQ["index.html"] = [
 ("Who does Curry Nation work with?", "Ambitious owner-managed and promoter-led businesses, often in categories where buyers compare suppliers on price: FMCG, pharma, real estate, kitchenware, jewellery, manufacturing and B2B."),
 ("Where should I start?", "With the free Brand Audit. It takes about ten minutes, shows your score before we ask for your email, and ends in one agreed next step. If the founder’s own visibility is the gap, start with the Founder Authority Audit."),
 ("Do I have to sign a retainer?", "No. Every product is built around one outcome and can be bought on its own. Most end in a sign-off, and you decide whether to go further."),
 ("How are your products priced?", "The Brand Audit is free and the Founder Authority Audit is ₹5,000. Everything else is scoped on a short call, once we know your business, so you only pay for what the problem needs."),
 ("What makes Curry Nation different?", "Strategy, creative, media and growth under one roof, led by founders with decades of brand building. We start from what makes a business worth choosing, and judge the work by what it does for the business."),
]

FAQ["brand-led.html"] = [
 ("Which package should I start with?", "Most businesses start with the free Brand Audit. It shows where your brand stands and what it costs you, and the call that follows agrees one next step, whether or not it is with us."),
 ("Do I have to buy all four?", "No. Each package stands alone. Start where your business is today and move up only when the evidence makes the case."),
 ("What’s the difference between the two Challenger Workshops?", "The Workshop for Leadership starts with one problem the founder gives us: a two-day offsite where senior operators challenge each decision-maker on it, then the team agrees a plan. The Workshop for Business starts with five weeks of evidence from customers, the trade and rivals, then the workshop day and the plan."),
 ("How is it priced?", "The Brand Audit is free. Positioning and both workshops are scoped on a call, plus GST, once we know your business."),
 ("Is this only for consumer brands?", "No. The method is built for commodity, B2B and consumer categories, wherever buyers compare you with the next supplier on price."),
]

FAQ["brand-audit.html"] = [
 ("Is the Brand Audit really free?", "Yes, with no obligation. It shows where you stand. It doesn’t include a plan, prices or a recommendation to buy anything."),
 ("How long does it take?", "About ten minutes for 20 yes/no questions and three short written answers. If you want the written report, eight deeper questions take about ten minutes more."),
 ("Do I have to give my email?", "Only after you have seen your score, so we can send the written report."),
 ("Who should answer the questions?", "Ideally the person who knows your margins and dealer terms."),
 ("What happens to my answers?", "They stay private. We use them only to build your report and prepare for the call, and never share them. Sector comparisons come only from combined results, and only when there are enough of them."),
 ("What happens on the call?", "A 30–45 minute conversation with a Curry Nation founder. We test the diagnosis against what you see in your business and agree one next step. No pitch unless you ask for one."),
 ("How accurate can twenty questions be?", "Twenty questions give a read of your business, not a full study of it. That is why the call exists: to test the read against reality."),
]

FAQ["brand-positioning.html"] = [
 ("What is brand positioning, in plain words?", "The one reason a buyer should choose you over the next supplier, that no rival already owns, with the proof that makes it believable."),
 ("Can I buy just one phase?", "Yes. Each phase ends in its own sign-off. Define needs a Demand Atlas or your own buyer research (or a three-day Rapid Demand Scan first), and Express needs a documented positioning."),
 ("How much does it cost?", "Fees are quoted per business, plus GST. The full programme costs 15% less than buying the phases separately, and if you add the next phase within 45 days, part of the previous fee is credited."),
 ("How much of our time does it take?", "One decision-maker as the contact, access to sales data and past research, two or three people for interviews, a weekly call, and feedback within three working days."),
 ("Does it include a logo or packaging?", "No. Logo, identity, packaging, production, media and website build are quoted separately. Our Design-led products build them on the positioning."),
 ("Will it work for a B2B or commodity business?", "Yes. Each phase has a lens for commodity, B2B and consumer businesses, from value-chain and margin maps to buyer interviews and lost-deal reviews."),
]

FAQ["challenger-workshop.html"] = [
 ("Why five weeks of evidence before the workshop?", "So the room settles arguments with facts, not opinions. Customer interviews, a store and channel safari and a rival tear-down show what customers, the trade and rivals are telling you that the leadership team hasn’t heard."),
 ("Who is in the room?", "The founder or MD and 8–10 functional heads, 8–10 people from Curry Nation across strategy, creative, media and customer experience, and 5–6 fresh eyes such as an outside-category consultant and Gen-Z shoppers."),
 ("What does ‘no breakthrough, no fee’ mean?", "At the end of the day, if you don’t see at least one breakthrough idea you’re ready to put in your 90-day plan, tell us within 30 minutes and we refund the fee, except venue and third-party costs."),
 ("Where is it held?", "A hotel conference room in your city, booked by you. Venue, travel and boarding are at actuals."),
 ("What do we leave with?", "An Output Pack a week later: the problem statement, a Challenger Positioning Snapshot, three campaign directions, a 90-day roadmap with owners and measures, and a photo record of every canvas."),
 ("How is it different from the Workshop for Leadership?", "The Workshop for Leadership starts with one problem the founder already knows, and spends two days at an offsite challenging every decision-maker on it. This one starts with five weeks of research for when nobody can say for sure what is holding growth back."),
 ("How do payments work?", "40% at kickoff, 40% at Phase 1 sign-off, and 20% after your verdict on the day."),
]

FAQ["leadership-workshop.html"] = [
 ("What kind of problem should the founder bring?", "One problem statement that matters to the business and needs more than one function to solve. We agree it with the founder before the offsite."),
 ("Who are the senior operators?", "People who have run the functions they challenge, one matched to each of your functions and briefed on your category."),
 ("Will my team speak openly with the founder in the room?", "That is what the format is built for. We meet away from the office, the evening of Day 1 is structured downtime, sensitive topics are flagged in advance, and nothing said in the room leaves it without agreement."),
 ("Who should attend from our side?", "The founder for both days and 5–8 decision-makers: the heads who will have to deliver the answer."),
 ("Where is it held?", "Always offsite, at a property from our shortlist. The venue and meals for both days are included. Your team’s travel to the venue is at actuals."),
 ("What do we leave with?", "The founder’s problem tested from every function, where answers didn’t hold up, one agreed way forward, and a 90-day plan with named owners and measures, written up a week later."),
 ("How is it priced?", "Scoped on a call. Payment is 50% at kickoff and 50% on the day."),
]

FAQ["founder-visibility.html"] = None  # page keeps its own FAQ list (updated in build)

FAQ["performance.html"] = [
 ("Who is the Growth Lab for?", "Product businesses of roughly ₹100–300 Cr that want to grow beyond discounts, across D2C, marketplaces and quick commerce."),
 ("How are fees set?", "Fees are tailored after a discovery call. Media spend, production and platform fees are always scoped separately."),
 ("Do you guarantee a ROAS?", "No. We judge every rupee by what it adds to contribution after fees, returns and discounts, not by in-platform ROAS, and we tell you where to stop spending as well as where to scale."),
 ("Which platforms do you work across?", "Meta, Google, Amazon, Flipkart, Meesho, Blinkit, Zepto, Zomato, Myntra and LinkedIn. Each platform is in the plan only if it has a job to do."),
 ("What data do you need from us?", "Margins, SKU mix, stock and sales, alongside access to ad accounts and tracking. Without margin and stock data we can’t judge growth by contribution."),
 ("Can we start with just the Growth Audit?", "Yes. Each package stands alone. The Growth Audit is a fixed-scope 3–4 weeks and ends in a 90-day action plan."),
 ("What does the growth planner tell me?", "It estimates reach, visits, potential orders and gross order value for a platform, market and budget. It is a planning estimate, not a guarantee, and gross order value is not profit."),
]

FAQ["design.html"] = [
 ("Do we need a positioning first?", "Yes. Design-led work starts from an approved positioning, from our Brand Positioning programme or your own. If there isn’t one, we start with a short positioning check."),
 ("Can you refresh our existing logo instead of replacing it?", "Yes. The Brand Identity System covers a new logo and wordmark, or a refresh of the one you have."),
 ("Will our dealers and vendors be able to use it?", "Yes. You get brand guidelines written for your team, dealers and vendors, and rollout artwork for each surface agreed."),
 ("Do you handle printing?", "We deliver print-ready artwork and a vendor handover. Printing, shoots, studios and external vendors are billed at actuals, with your approval first."),
 ("How is it priced?", "Each product is scoped and priced on a call, once we know your range, channels and rollout."),
 ("Who owns the files?", "You do. Final deliverables are yours on full payment."),
]

def faq_section(items, head, title="Questions owners ask", cls=""):
    det = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items)
    return f'''<section class="{cls}" id="faq"><div class="wrap">{head("faq", title)}<div class="faq">{det}</div></div></section>'''

def faq_schema(items):
    strip = lambda s: _h.unescape(re.sub(r"<[^>]+>", "", s))
    d = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in items]}
    return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False) + "</script>"
