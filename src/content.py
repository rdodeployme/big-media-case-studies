# Big Media case studies: all copy, stats and image choices.
# Figures come from the builds themselves: page counts and edit history from the repos,
# counts read off the live apps. Nothing here is a client result we haven't seen.

STUDIES = [
 dict(
  slug='yarta', name='Yarta', client='Yarta (Recycle Group)', service='Product site + live demo', year='2026',
  accent='#e8892c', ink='#140b02',
  kicker='Environmental reporting platform',
  title='Selling a technical product before the first meeting.',
  line='A 37-page product site, a clickable dashboard demo and a sample report for a sustainability score built for councils and businesses.',
  url='https://rdodeployme.github.io/yes-site/', urltext='Live preview',
  embed='https://rdodeployme.github.io/yes-site/demo/?sector=council', embed_label='The Yarta demo portal, live',
  hero='yarta-hero',
  stats=[('37','pages built'),('8','sector demos'),('126','edits shipped'),('1','score, ten categories')],
  problem='Yarta turns scattered environmental data into one score, a report a council can hand over, and a roadmap to improve. It’s a technical product sold to council officers and business owners, who don’t have time to decode a method.',
  goal='A site that explains the method in plain English, and a demo good enough that buyers have already tried the product before a sales call.',
  features=[
   ('A demo you can click','A live portal with sample data for eight sectors: council, business, construction, education, health, logistics, manufacturing and retail. Buyers see their own kind of organisation, not a generic chart.','yarta-demo','Demo Shire Council: score, benchmarks and the year’s trend'),
   ('The report, before they buy','A full sample Yarta Report shows exactly what a council receives: the score, the benchmarks behind it, and the ranked roadmap.','yarta-report','The sample report: what lands on a council’s desk'),
   ('Lead qualification built in','A five-minute Readiness Check gives prospects a first read on where they stand and tells the sales team who is ready to talk.','yarta-readiness','Readiness Check: five minutes, one clear answer'),
   ('Pricing without the phone call','Simple, published pricing by organisation size, with the first-year offer up front, so councils can budget before they ever enquire.','yarta-pricing','Published pricing, by organisation size'),
  ],
  gallery=[('yarta-how','How it works'),('yarta-councils','Councils'),('yarta-demo-health','Demo: health sector'),('yarta-hero','Home')],
  phones=['yarta-m1','yarta-m2','yarta-m3'],
  timeline=[('28 Sep','First build: site, pricing and the sample report'),('29 Sep','Yarta brand, sector demos and the sample report engine'),('13 Oct','Client portal back end and the Readiness Check'),('23 Nov','Latest release: 126 edits shipped')],
  outcome='Yarta now has a 37-page site, a working demo and a sample report. The team runs council walkthroughs straight from the demo accounts.',
  scope=['Product positioning','Information design','UX and UI','Interactive demo','Copywriting','Build'],
  stack='Hand-built HTML, CSS and JavaScript. Hosted on GitHub Pages.',
 ),
 dict(
  slug='recycle-group', name='Recycle Group', client='Recycle Group', service='Corporate website', year='2026',
  accent='#e2763a', ink='#160a03',
  kicker='National recycling group',
  title='Every material, every sector, one group, and easy to buy from.',
  line='A 74-page corporate site that makes a complex, multi-brand recycling business clear to councils, government, rail and ports.',
  url='https://recycle.net.au/', urltext='recycle.net.au',
  embed='https://rdodeployme.github.io/recycle-group/', embed_label='The Recycle Group site, live',
  hero='recycle-hero',
  stats=[('74','pages built'),('12','material streams'),('14','sector pages'),('139','edits shipped')],
  problem='Recycle Group recycles everything from steel and polystyrene to mattresses and soil, across several brands, for buyers like councils, state road operators, rail and ports. The story was too big to tell in a brochure site.',
  goal='Show the scale in seconds, then get each buyer to the exact service, sector and proof they need, without a phone call.',
  features=[
   ('A material index','Twelve material streams, each with its own page: what’s taken, how it’s processed and where it goes next.','recycle-materials','Materials: every stream, one index'),
   ('Numbers people can picture','Big figures turned into something you can see, like a year of Victoria’s landfilled mattresses laid across the MCG playing surface.','recycle-mattress','The mattress problem, at the scale of the MCG'),
   ('Proof, not promises','A case-study section that leads with the result for each job, so buyers see what was done for organisations like theirs.','recycle-jobs','Case studies that lead with the number'),
   ('Built for procurement','Fourteen sector pages, plus infrastructure, chain of custody and reporting: what a council or government buyer needs to sign off a supplier.','recycle-councils','Sector pages: councils'),
  ],
  gallery=[('recycle-trace','Trace a load'),('recycle-infra','Infrastructure'),('recycle-reporting','Reporting'),('recycle-cases','Case studies')],
  phones=['recycle-m1','recycle-m2','recycle-m3'],
  timeline=[('23 Sep','First build: sectors, materials, chain of custody'),('27 Sep','Imagery across every sector and role page'),('30 Sep','New positioning: every material, every sector, one group'),('2 Oct','Case studies added'),('19 Oct','139 edits in, live at recycle.net.au')],
  outcome='The site is live at recycle.net.au: 74 pages covering the group’s materials, sectors and brands.',
  scope=['Content strategy','Site architecture','UX and UI','Data storytelling','Copywriting','Build'],
  stack='Hand-built HTML, CSS and JavaScript. Live on its own domain.',
 ),
 dict(
  slug='echeck', name='eCheck', client='Recycle Group', service='Custom app', year='2026',
  accent='#22e06b', ink='#03140a',
  kicker='Safety & compliance app',
  title='The safety system that lives on the yard, not in a binder.',
  line='A daily safety, training and compliance app for a working recycling yard. It runs on any phone, with no per-seat subscription.',
  url='https://echeck.com.au/', urltext='echeck.com.au',
  embed='https://rm-echeck-shear-baler-2611.netlify.app/training/alligator-shear/', embed_label='An eCheck training module, live',
  hero='echeck-shear', heroUrl='eCheck · training',
  stats=[('58','check types'),('62','policies'),('8','check groups'),('0','subscription fees')],
  problem='Recycle Group runs transfer stations, recycling lines, trucks and heavy plant. Safety checks were only worth anything if they happened at the start of a shift, beside the machine, on whatever phone was in someone’s pocket.',
  goal='Rather than pay for off-the-shelf safety software and bend the process to fit, build a system around the group’s own machines, sites and policies.',
  features=[
   ('Daily checks in seconds','About 58 check types across eight groups, from fit-for-work declarations to vehicles, machinery, site checks and high-risk work. Each one is a tap from the home screen.','echeck-form','A machine pre-start: tick, photo, sign'),
   ('Faults that get closed','Report a fault, and it goes straight to a manager follow-up with the action taken, whether more is needed, and a signature. Nothing sits in a drawer.','echeck-fault','Report a fault: straight to a manager'),
   ('Training for each machine','Step-by-step modules for specific plant, like the alligator shear, canister puncturer and scrap metal baler, with hazards, controls and sign-off.','echeck-baler','Training module: scrap metal baler'),
   ('Policies, acknowledged','62 policies across five departments, read and acknowledged on the phone, with the record kept against each worker.','echeck-modules','The training library'),
  ],
  gallery=[('echeck-hero','Partner rollout: the same daily checks under a partner yard’s own brand'),('echeck-training','The full training library')],
  phones=['echeck-m3','echeck-m2','echeck-m1'],
  timeline=[],
  outcome='Live at echeck.com.au and in use at the group’s North Geelong site. The same app has been rolled out to a partner’s yard under their own brand.',
  scope=['Process mapping','UX for the field','Forms and sign-off','Training content','Build'],
  stack='Mobile-first web app with an office back end. No app store, no per-seat licence.',
 ),
 dict(
  slug='recycled-metals', name='Recycled Metals', client='Recycle Group (metals)', service='Service website + client portal', year='2026',
  accent='#cfd8df', ink='#0c1014',
  kicker='Metal collection service',
  title='One fee, quoted upfront. Every tonne weighed and reported.',
  line='A booking-led site and client portal for a metal collection service working with councils, aged care, hospitals, universities and business.',
  url='https://rdodeployme.github.io/global-steel/', urltext='Live preview',
  embed='https://rdodeployme.github.io/global-steel/', embed_label='The Recycled Metals site, live',
  hero='metals-hero',
  stats=[('33','pages built'),('5','sector pages'),('5','step booking'),('66','edits shipped')],
  problem='Old road signs, hospital beds, X-ray machines, racking: if it’s mostly metal, this service collects it. But customers didn’t know what counted, what it would cost, or where it ended up.',
  goal='Make booking as easy as calling a tradie, price it before the truck comes, and prove where the metal went afterwards.',
  features=[
   ('Book, quote, collect, recycle, report','A five-step flow that tells customers exactly what happens and when, from a two-minute online booking to a statement at the end.','steel-process','The five-step service, start to finish'),
   ('What we collect, at a glance','A visual index of everything the service takes, from guardrail and bollards to whitegoods and medical equipment, so nobody has to ask.','metals-collect','What we collect'),
   ('Sector pages that speak the language','Separate pages for councils and state roads, aged care, hospitals, universities, and business and government, each with its own examples.','metals-hospitals','Hospitals and health'),
   ('A portal for the paperwork','Four numbers for every collection, and a client portal where customers see their own statements.','steel-numbers','Four numbers for every collection, plus the client portal'),
  ],
  gallery=[('metals-book','Book a collection'),('metals-sectors','Sectors'),('metals-trace','Traceability'),('metals-connect','Client portal sign-in')],
  phones=['metals-m1','metals-m2','metals-m3'],
  timeline=[('23 Sep','Site and client portal built'),('7 Oct','3D product renders across the site'),('12 Oct','Online booking form'),('14 Oct','Rebrand to Recycled')],
  outcome='A 33-page service site with booking, sector pages and a client portal built in.',
  scope=['Service design','UX and UI','3D product imagery','Client portal','Copywriting','Build'],
  stack='Hand-built HTML, CSS and JavaScript. Hosted on GitHub Pages.',
 ),
 dict(
  slug='t-waste', name='T-Waste', client='Recycle Group', service='Brand + launch website', year='2026',
  accent='#3cff7d', ink='#021407',
  kicker='E-waste brand launch',
  title='A new brand and a nine-page site, live in two days.',
  line='Big technology waste, gone properly: a launch site for a service that takes TVs, monitors, copiers and servers.',
  url='https://rdodeployme.github.io/t-waste/', urltext='Live preview',
  embed='https://rdodeployme.github.io/t-waste/', embed_label='The T-Waste site, live',
  hero='twaste-hero',
  stats=[('2','days to launch'),('9','pages built'),('12','item types shown'),('1','passport per cage')],
  problem='Every office refit leaves a room full of dead screens nobody knows how to get rid of. They can’t go in the skip, they’re heavy, and plenty still hold data.',
  goal='Launch a brand and a site, fast, that makes a dull and risky problem feel completely handled.',
  features=[
   ('Take a TV apart','An interactive teardown: tap a part of the screen to see what it’s made of and where it goes. It turns compliance into something people want to click.','twaste-tv','What’s inside a flat screen'),
   ('The cage passport','Every cage gets its own record, from loaded and sealed to dismantled to certificate issued. One idea that sells traceability.','twaste-how','Every step on record'),
   ('Data security, spelled out','Data-bearing devices are logged and destroyed on record, with the process written out for whoever has to sign it off.','twaste-data','Dead devices still talk'),
   ('A clear way in','Cages for screens, IT and bulk clear-outs, smaller bins for the everyday stuff, and one obvious call to action: book a cage.','twaste-bins','Built for the big stuff'),
  ],
  gallery=[('twaste-what','What goes in'),('twaste-industries','Industries'),('twaste-impact','Impact')],
  phones=['twaste-m1','twaste-m2','twaste-m3'],
  timeline=[('19 Oct','Brief, brand and first build'),('20 Oct','Nine pages live for review')],
  outcome='Brand, copy and a nine-page site went from brief to live preview in two days.',
  scope=['Brand','Launch website','Interactive','Copywriting'],
  stack='Hand-built HTML, CSS and JavaScript. Hosted on GitHub Pages.',
 ),
 dict(
  slug='nunjara', name='Nunjara', client='Nunjara Recycling', service='App design + prototype', year='2026',
  accent='#e0a92e', ink='#1a1203',
  kicker='Soil recycling: load register',
  title='Every truck through the gate, recorded in six taps.',
  line='An iPad app for logging every load tipped at a soil recycling site, and the office dashboard that reports on it, designed in two directions.',
  url='', urltext='',
  embed='../proto/nunjara-yard.html', embed_label='The Yard prototype: tap through it',
  hero='nun-a-field',
  stats=[('6','tap capture'),('2','design directions'),('5','office views'),('0','re-keying')],
  problem='Nunjara recycles soil, fill and rubble. Every load through the gate needs a record: which company, which truck, how much, what material, with photos, done between trucks.',
  goal='A gate record that takes seconds, can’t be quietly changed later, and reaches the office ready to report on without re-typing.',
  features=[
   ('Six steps, big buttons','Details, truck, volume, material, photos, lock. Regular customers are a quick-pick, and every choice is a large tap target.','nun-a-truck','Truck configuration: one tap, then on'),
   ('Works without signal','The record locks on the iPad and uploads the same minute, or as soon as signal comes back. There is nothing for the operator to remember.','nun-a-lock','Locked: a permanent site record'),
   ('Records that hold up','Photo evidence attaches to each load, every record carries an integrity check, and office corrections are added on top rather than overwriting.','nun-a-companies','Every company, every load'),
   ('The office, sorted','Reports by company, material and truck, an activity feed, and one-click CSV and PDF exports for accounts.','nun-b-office','Direction B, “Ledger”: the office report'),
  ],
  gallery=[('nun-a-office','Yard: office report'),('nun-b-field','Ledger: field app'),('nun-b-materials','Ledger: materials')],
  phones=['nun-m1','nun-m2','nun-m3'],
  timeline=[],
  outcome='Two interactive prototypes, Yard (dark, high contrast for outdoors) and Ledger (light, editorial), for the client to tap through and choose from. Shown with sample data.',
  scope=['Workflow design','App UX','Two design directions','Interactive prototype'],
  stack='Interactive HTML prototypes, ready to build as an offline-first iPad web app.',
 ),
]

# Words to pick out in lime in each case-study headline.
HL = {
 'yarta': 'before the first meeting.',
 'recycle-group': 'easy to buy from.',
 'echeck': 'not in a binder.',
 'recycled-metals': 'weighed and reported.',
 't-waste': 'live in two days.',
 'nunjara': 'in six taps.',
}
for _s in STUDIES:
    _s['hl'] = HL.get(_s['slug'], '')

# ---------------------------------------------------------------------------
# Big Digital agency proof. Everything below is as published on big.com.au
# (read 24 Nov 2026). Don't add figures or quotes that aren't on that site.
# ---------------------------------------------------------------------------
BRAND = dict(
  name='Big Digital', legal='Adspire Group Pty Ltd',
  phone='1300 366 438', tel='1300366438', email='info@big.com.au',
  address='116 Furner Ave, North Geelong VIC 3215',
  site='https://big.com.au/',
  linkedin='https://www.linkedin.com/company/big-digital-aus/',
  facebook='https://www.facebook.com/profile.php?id=61585934444174',
)

RESULTS = [  # (number, decimals, suffix, label)
  ('7.2', 1, '', 'Average ROAS'),
  ('500', 0, 'K+', 'Sales orders'),
  ('650', 0, 'K+', 'Leads generated'),
  ('200', 0, 'M+', 'Revenue driven'),
]

GROWTH = [  # (metric, label, client, image)
  ('−30%', 'CPA', 'Junk.com.au', 'grow-junk'),
  ('+320%', 'Organic traffic', 'Zeal Refrigeration Group', 'grow-zeal'),
  ('9.6x', 'ROAS', 'Tobe Healthcare', 'grow-tobe'),
  ('−20%', 'CPA', 'Lockcorp Locksmith', 'grow-lockcorp'),
  ('+200%', 'Revenue', 'Bayside Blades', 'grow-bayside'),
]
FEATURED_GROWTH = dict(metric='+300%', label='Leads', client='24H Melbourne Plumbers',
  quote='We hit $50K+ in revenue in our very first month with Big Digital.', who='Dean E., Owner')

TESTIMONIALS = [  # (quote, name, role, company, avatar)
  ('Our website wasn’t converting and we couldn’t generate enough sales through it. Andy and the team rebuilt the site, fixed the technical issues that had been holding us back, and rolled out a proper SEO, Google Ads and Meta Ads strategy. Sales were up 200% within the first three months.',
   'Mathew Y.', 'Director', 'Precision Safes', 't-mathew'),
  ('Since Big Digital took over our Google Ads account, our cost per lead has dropped by 30% consistently, and we’re getting more jobs from the same spend. It’s good to finally have someone who actually cares about our business.',
   'Todd M.', 'Operations Manager QLD', 'Junk.com.au', 't-todd'),
  ('We run a big budget on Google Ads, so we needed someone genuinely skilled with search advertising. After a stressful run with our previous agency, Andy turned things around fast, rebuilding our landing pages and restructuring the account.',
   'Dean E.', 'Owner', '24 Hour Melbourne Plumbers', 't-dean'),
  ('In over 20 years in business, this has probably been the most positive experience I’ve had with an agency. Andy improved our SEO ranking and optimised our Google Ads account, which gave us an immediate 50% lower cost per acquisition within the first three months.',
   'Josh S.', 'Owner', 'Cheap And Best Cleaning', 't-josh'),
]

SERVICES = [  # (name, line, url, tint)
  ('Google Ads', 'Paid search built to chase conversions, not clicks, run by certified Google Partners.', 'https://big.com.au/services/google-ads/', '#EBE4F7'),
  ('Social Media Marketing', 'Creative-led campaigns across Meta, TikTok and Pinterest that turn scrollers into buyers.', 'https://big.com.au/services/social-media-marketing/', '#D7FFBF'),
  ('SEO & AI Search', 'Technical SEO, answer-first content and authority, so you show up on Google and in AI answers.', 'https://big.com.au/services/seo-aeo-geo/', '#FFD3D3'),
  ('Web & App Development', 'Fast sites built to convert, and custom apps that replace another monthly subscription.', 'https://big.com.au/services/web-app-development/', '#FFE0B3'),
  ('CRM & Automation', 'Email and automation flows that turn the customers you already have into repeat revenue.', 'https://big.com.au/services/crm-automation/', '#CDE6FF'),
  ('AI Automation', 'Practical AI built into your workflows, so routine admin gets done without adding headcount.', 'https://big.com.au/services/ai-automation/', '#BDFCF5'),
  ('Web Hosting & Maintenance', 'Hosting, security and updates handled, so your site stays fast, safe and live.', 'https://big.com.au/services/web-hosting-maintenance/', '#FFF3B0'),
]

# Client names shown in the marquee: all appear on big.com.au's client strip or in the work below.
CLIENTS = ['Junk.com.au', 'Recycle Group', 'Zeal Refrigeration', 'Tobe Healthcare', '24H Melbourne Plumbers',
           'Lockcorp', 'Bayside Blades', 'Precision Safes', 'Cheap And Best Cleaning', 'The Mattress Recycling Company',
           'Nunjara', 'Hektik Automotive']
