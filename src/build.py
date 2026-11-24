"""Builds the Big Digital work site from content.py.
   python3 src/build.py  ->  index.html and <slug>/index.html"""
import html, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import STUDIES, BRAND, RESULTS, GROWTH, FEATURED_GROWTH, TESTIMONIALS, SERVICES, CLIENTS
e = html.escape
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME = BRAND['name']                 # one switch for the brand name shown across the site
SITE_URL = 'https://rdodeployme.github.io/big-media-case-studies/'
CONTACT = '#contact'                 # the audit form lives on the home page
DARK = {'yarta':'#b5631a','recycle-group':'#c45a22','echeck':'#0f9a49','recycled-metals':'#4f5f6c','t-waste':'#10a845','nunjara':'#a87510'}
FILT = {'yarta':'web app','recycle-group':'web','echeck':'app','recycled-metals':'web','t-waste':'web brand','nunjara':'app'}

NE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17 17 7M8 7h9v9"/></svg>'
AR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
AL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M11 6l-6 6 6 6"/></svg>'
X = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>'
STAR = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.5l2.9 6.1 6.6.8-4.9 4.6 1.3 6.6L12 17.3l-5.9 3.3 1.3-6.6-4.9-4.6 6.6-.8z"/></svg>'
CHAT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/><path d="M8.5 11h7M8.5 14.5h4.5"/></svg>'
LI = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.75h4V21H3zM9.5 9.75h3.83v1.54h.06c.53-1 1.84-2.06 3.79-2.06 4.05 0 4.8 2.67 4.8 6.14V21h-4v-5.02c0-1.2-.02-2.74-1.67-2.74-1.67 0-1.93 1.3-1.93 2.65V21h-4z"/></svg>'
FB = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M13.5 21v-7.5h2.5l.4-3h-2.9V8.6c0-.87.25-1.46 1.5-1.46H16.6V4.45A20 20 0 0 0 14.3 4.3c-2.3 0-3.8 1.4-3.8 3.95v2.25H8v3h2.5V21z"/></svg>'


def btn(label, href, cls='', ext=False):
    t = ' target="_blank" rel="noopener"' if ext else ''
    return f'<a class="btn {cls}" href="{e(href)}"{t}>{label}<span class="ic">{NE}</span></a>'


def head(title, desc, pre, accent='#C4F112', ink='#000204', dark='#212529', body_cls=''):
    return f'''<!doctype html>
<html lang="en-AU"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:type" content="website">
<meta property="og:image" content="{SITE_URL}img/bd-results.webp"><meta name="theme-color" content="#000204">
<link rel="icon" href="{pre}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;600;700&family=Phudu:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}assets/site.css">
<style>:root{{--a:{accent};--a-ink:{ink};--a-dark:{dark}}}</style>
</head><body class="{body_cls}">
<div class="prog" aria-hidden="true"></div>
<header class="top"><div class="wrap"><div class="bar">
  <a class="logo" href="{pre or './'}" aria-label="{NAME}: our work"><img src="{pre}img/bd-logo.png" alt="{NAME}" width="156" height="56"></a>
  <nav class="nav" aria-label="Main"><a class="on" href="{pre}#work">Work</a><a href="{pre}#services">Services</a><a href="{BRAND['site']}about/" target="_blank" rel="noopener">About</a><a href="{pre}{CONTACT}">Contact</a></nav>
  {btn('Talk To Us', pre + CONTACT)}
</div></div></header>'''


def footer(pre):
    svc = ''.join(f'<li><a href="{e(u)}" target="_blank" rel="noopener">{e(n)}</a></li>' for n, _, u, _ in SERVICES)
    return f'''<footer class="foot"><div class="wrap">
<div class="f-grid">
  <div><img src="{pre}img/bd-logo.png" alt="{NAME}" width="156" height="56" loading="lazy">
    <p>{NAME} is a senior digital team helping Australian businesses grow through bespoke, results-focused strategy and hand-built websites and apps. No juniors, no guesswork.</p>
    <div class="soc"><a href="{BRAND['linkedin']}" target="_blank" rel="noopener" aria-label="LinkedIn">{LI}</a><a href="{BRAND['facebook']}" target="_blank" rel="noopener" aria-label="Facebook">{FB}</a></div></div>
  <div><h4>Quick links</h4><ul><li><a href="{pre}#work">Work</a></li><li><a href="{pre}#services">Services</a></li><li><a href="{BRAND['site']}about/" target="_blank" rel="noopener">About</a></li><li><a href="{BRAND['site']}blog/" target="_blank" rel="noopener">Blog</a></li><li><a href="{pre}{CONTACT}">Contact</a></li></ul></div>
  <div><h4>Services</h4><ul>{svc}</ul></div>
  <div><h4>Contact us</h4><ul><li>{e(BRAND['address'])}</li><li><a href="tel:{BRAND['tel']}">{BRAND['phone']}</a></li><li><a href="mailto:{BRAND['email']}">{BRAND['email']}</a></li></ul></div>
</div>
<div class="wm" aria-hidden="true">{e(NAME)}</div>
<div class="f-bot"><span>© 2026 {e(BRAND['legal'])}. All rights reserved.</span><nav><a href="{BRAND['site']}privacy-policy/" target="_blank" rel="noopener">Privacy Policy</a><a href="{BRAND['site']}terms-and-conditions/" target="_blank" rel="noopener">Terms &amp; Conditions</a></nav></div>
</div></footer>
<a class="sticky" href="{pre}{CONTACT}">{CHAT}Free Audit</a>
<div class="lb" role="dialog" aria-modal="true" aria-label="Screenshot"><img alt=""><div class="cap"></div><button class="x" aria-label="Close">{X}</button><button class="pv" aria-label="Previous">{AL}</button><button class="nx" aria-label="Next">{AR}</button></div>
<script src="{pre}assets/site.js" defer></script>
</body></html>'''


def frame(img, alt, pre, url='', lazy=True, zoom=True, bare=False):
    # bare: the image is already a composed device scene, so no browser bar
    bar = '' if bare else f'<div class="bar"><i></i><i></i><i></i>{f"<em>{e(url)}</em>" if url else ""}</div>'
    z = f' data-zoom="{pre}img/{img}.webp" data-cap="{e(alt)}" role="button" tabindex="0"' if zoom else ''
    return f'<div class="frame"{z}>{bar}<img src="{pre}img/{img}.webp" alt="{e(alt)}" width="1600" height="1000"{" loading=lazy decoding=async" if lazy else ""}></div>'


def short(u): return u.split('://')[-1].rstrip('/')


def sym(t):
    """Set +, % and minus in Google Sans so they sit right next to Phudu numerals."""
    return re.sub(r'([+%−-])', r'<i class="sy">\1</i>', e(t))


def hl(title, part):
    """Wrap the highlight phrase of a headline in <em> (lime on dark)."""
    t = e(title)
    if part and e(part) in t:
        return t.replace(e(part), f'<em>{e(part)}</em>', 1)
    return t


def stat(n, l, first=False):
    num = n if not n.isdigit() else f'<span data-n="{n}">{n}</span>'
    return f'<div class="rv"><b class="{"ac" if first else ""}">{num}</b><span>{e(l)}</span></div>'


# ---------------------------------------------------------------- case study
def study(i, s):
    pre = '../'; nxt = STUDIES[(i + 1) % len(STUDIES)]
    live = (f'<a href="{e(s["url"])}" target="_blank" rel="noopener">{e(s["urltext"])} ↗</a>' if s['url'] else 'Prototype')
    meta = ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in [('Client', e(s['client'])), ('Service', e(s['service'])), ('Year', s['year']), ('Live', live)])
    stats = ''.join(stat(n, l, k == 0) for k, (n, l) in enumerate(s['stats']))
    feats = ''.join(f'''<article class="feat"><div class="ft rv"><div class="num">0{k+1}</div><h3>{e(h)}</h3><p>{e(p)}</p></div>
<figure class="rv d1">{frame(im, cap, pre, bare=s.get('bare', False))}<figcaption>{e(cap)}</figcaption></figure></article>''' for k, (h, p, im, cap) in enumerate(s['features']))
    gal = ''.join(f'<figure>{frame(im, cap, pre, bare=s.get('bare', False))}<figcaption>{e(cap)}</figcaption></figure>' for im, cap in s['gallery'])
    phones = ''.join(f'<div class="phone rv d{k}"><img src="{pre}img/{p}.webp" alt="{e(s["name"])} on a phone" loading="lazy" width="390" height="800"></div>' for k, p in enumerate(s['phones']))
    tl = ''
    if s['timeline']:
        tl = f'''<section class="tl" id="timeline"><div class="wrap"><div class="k rv">Timeline</div><h2 class="h2 rv d1">How it <em>came together</em></h2>
<ol>{''.join(f'<li class="rv d{min(k,3)}"><b>{e(d)}</b><span>{e(t)}</span></li>' for k, (d, t) in enumerate(s['timeline']))}</ol></div></section>'''
    embed = s['embed']
    live_sec = f'''<section class="live" id="live"><div class="wrap">
<div class="row2"><div><div class="k rv">Try it</div><h2 class="h2 rv d1">Don’t take <em>our word</em> for it.</h2></div>
<span class="rv">{btn('Open Full Screen', embed, 'ghost', ext=True)}</span></div>
<div class="frame rv d1"><div class="bar"><i></i><i></i><i></i><em>{e(s['embed_label'])}</em></div>
<div class="vp" style="background-image:url({pre}img/{s['hero']}.webp)"><iframe title="{e(s['embed_label'])}" data-src="{e(embed)}" loading="lazy"></iframe>
<div class="cover"><button class="btn" type="button">Load The Live {'Prototype' if 'proto' in embed else 'Site'}<span class="ic">{NE}</span></button></div></div></div>
</div></section>'''
    visit = btn('Visit The Site', s['url'], ext=True) if s['url'] else ''
    sub = ''.join(f'<a href="#{a}">{t}</a>' for a, t in [('brief','The brief'),('build','What we built'),('screens','Screens')] + ([('timeline','Timeline')] if s['timeline'] else []) + [('live','Try it'),('result','Result')])
    body = f'''
<main>
<section class="c-hero pat"><div class="wrap">
  <div class="crumb rv"><a href="../#work">Work</a><span>/</span><span>{e(s['name'])}</span></div>
  <h1 class="rv d1">{hl(s['title'], s.get('hl'))}</h1>
  <p class="c-line rv d2">{e(s['line'])}</p>
  <dl class="c-meta rv d3">{meta}</dl>
  <div class="stagewrap"><div class="tilt">{frame(s['hero'], s['name'], pre, s.get('heroUrl') or (short(s['url']) if s['url'] else 'prototype'), lazy=False, bare=s.get('bare', False))}</div></div>
</div></section>
<section class="stats"><div class="wrap"><div class="g">{stats}</div></div></section>
<nav class="subnav" aria-label="Sections"><div class="wrap"><span class="nm">{e(s['name'])}</span>{sub}</div></nav>
<div class="light">
<section class="sec" id="brief"><div class="wrap">
  <div class="k rv">The brief</div><h2 class="h2 rv d1">What they <em>needed</em></h2>
  <div class="pg"><div class="rv"><h3>The problem</h3><p>{e(s['problem'])}</p></div><div class="rv d1"><h3>The goal</h3><p>{e(s['goal'])}</p></div></div>
</div></section>
<section class="sec" id="build" style="padding-top:0"><div class="wrap">
  <div class="k rv">What we built</div><h2 class="h2 rv d1" style="margin-bottom:56px">The <em>work</em></h2>
  {feats}
</div></section>
</div>
<section class="gal" id="screens"><div class="wrap galhead"><div><div class="k rv">Screens</div><h2 class="h2 rv d1">More <em>of it</em></h2></div>
<div class="arrows rv"><button type="button" data-d="-1" aria-label="Scroll back">{AL}</button><button type="button" data-d="1" aria-label="Scroll forward">{AR}</button></div></div>
<div class="strip">{gal}</div>
<div class="wrap"><div class="phones">{phones}</div></div></section>
{tl}
{live_sec}
<section class="result" id="result"><div class="wrap">
  <div class="k rv">Where it landed</div>
  <p class="big rv d1">{e(s['outcome'])}</p>
  <div class="cols rv d2"><div><h4>What we did</h4><ul>{''.join(f'<li>{e(x)}</li>' for x in s['scope'])}</ul></div>
  <div><h4>How it’s built</h4><p>{e(s['stack'])}</p></div><div><h4>See it</h4>{visit or '<p>Prototype, shown with sample data.</p>'}</div></div>
</div></section>
<a class="next" href="../{nxt['slug']}/"><img src="{pre}img/{nxt['hero']}.webp" alt="" loading="lazy">
<div class="wrap"><div><div class="k">Next case study</div><strong>{e(nxt['name'])}</strong></div><span class="ar">{NE}</span></div></a>
<section class="cta pat"><div class="wrap">
  <div class="k rv">Your turn</div>
  <h2 class="rv d1">Got a job<br><em>like this?</em></h2>
  <div class="row3 rv d2"><p>Tell us what’s slowing your business down. We’ll audit your website and ads for free and show you what we’d build or fix, instead of selling you another subscription.</p>
  <div style="display:flex;gap:12px;flex-wrap:wrap">{btn('Get Your Free Audit', pre + CONTACT, 'big')}<a class="btn ghost big" href="tel:{BRAND['tel']}">Call {BRAND['phone']}<span class="ic">{NE}</span></a></div></div>
</div></section>
</main>'''
    os.makedirs(os.path.join(ROOT, s['slug']), exist_ok=True)
    t = f"{s['name']}: {s['kicker']} | {NAME}"
    open(os.path.join(ROOT, s['slug'], 'index.html'), 'w').write(
        head(t, s['line'], pre, s['accent'], s['ink'], DARK[s['slug']], 'case') + body + footer(pre))


# ---------------------------------------------------------------- home page
def index():
    cards = ''.join(f'''<a class="card rv{' d1' if k % 2 else ''}" href="{s['slug']}/" data-f="{FILT[s['slug']]}" style="--c:{s['accent']}">
<span class="shot"><img src="img/{s['hero']}.webp" alt="{e(s['name'])}: {e(s['kicker'])}" loading="lazy" width="1600" height="1000"></span>
<span class="row1"><span class="metric"><span class="dot"></span>{e(s['stats'][0][0])} {e(s['stats'][0][1])}</span><span class="n">0{k+1}</span></span>
<h3>{e(s['name'])}</h3><p>{e(s['service'])} · {e(s['kicker'])}</p><span class="go">{NE}</span></a>''' for k, s in enumerate(STUDIES))
    reel = ''.join(f'<img src="img/{im}.webp" alt="" loading="lazy">' for s in STUDIES for im in [s['features'][0][2], s['gallery'][0][0]]) * 2
    marq = ''.join(f'<span>{e(c)}</span>' for c in CLIENTS) * 2
    nums = ''.join(f'<div class="rv d{min(k,3)}"><b><span data-n="{n}" data-d="{d}">{n}</span>{sym(sf)}</b><span class="lbl">{e(l)}</span></div>' for k, (n, d, sf, l) in enumerate(RESULTS))
    grow = ''.join(f'''<article class="gcard rv{' d1' if k % 3 == 1 else ' d2' if k % 3 == 2 else ''}"><div class="ph"><img src="img/{im}.webp" alt="{e(c)}" loading="lazy"></div>
<div class="tx"><div class="m">{sym(m)}</div><span class="ml">{e(l)}</span><h3>{e(c)}</h3></div></article>''' for k, (m, l, c, im) in enumerate(GROWTH))
    fg = FEATURED_GROWTH
    grow += f'''<article class="gcard feat2 rv d2"><img class="ast2" src="img/bd-asterisk.svg" alt="" width="54" height="54">
<div><div class="m">{sym(fg['metric'])}</div><span class="ml">{e(fg['label'])}</span><h3>{e(fg['client'])}</h3>
<blockquote>“{e(fg['quote'])}”<cite>{e(fg['who'])}</cite></blockquote></div></article>'''
    quotes = ''.join(f'''<figure class="q rv{' d1' if k % 2 else ''}"><div><div class="stars" aria-label="5 stars">{STAR * 5}</div><blockquote>“{e(q)}”</blockquote></div>
<figcaption class="who"><img src="img/{av}.webp" alt="" width="52" height="52" loading="lazy"><div><b>{e(n)}</b><span>{e(r)}, {e(c)}</span></div></figcaption></figure>''' for k, (q, n, r, c, av) in enumerate(TESTIMONIALS))
    svc = ''.join(f'''<a class="s rv{' d1' if k % 4 == 1 else ' d2' if k % 4 == 2 else ' d3' if k % 4 == 3 else ''}" href="{e(u)}" target="_blank" rel="noopener" style="--t:{t}">
<span class="num">0{k+1}</span><h3>{e(n)}</h3><p>{e(line)}</p><span class="txt">Read more {AR}</span></a>''' for k, (n, line, u, t) in enumerate(SERVICES))
    svc += f'''<div class="s cta-s rv d3"><span class="num" style="color:var(--lime)">?</span><h3>Not sure where to start?</h3><p>Get a free audit of your website and ads. We’ll show you the biggest wins first.</p>{btn('Get Your Free Audit', CONTACT)}</div>'''
    opts = ''.join(f'<label><input type="checkbox" name="need" value="{e(o)}"><span>{e(o)}</span></label>' for o in ['Website', 'Custom app', 'Google Ads', 'Social ads', 'SEO & AI search', 'Automation'])
    total_pages = sum(int(s['stats'][0][0]) for s in STUDIES if s['stats'][0][1] == 'pages built') + 9  # + T-Waste's nine pages
    body = f'''
<main>
<section class="hero pat">
  <div class="vert"><a href="{BRAND['linkedin']}" target="_blank" rel="noopener">LinkedIn</a><a href="{BRAND['facebook']}" target="_blank" rel="noopener">Facebook</a></div>
  <div class="wrap">
  <div class="tagline rv"><span class="chip">{e(NAME)} · Selected work · 2026</span></div>
  <h1 class="rv d1"><span class="ln">Work that <span class="cap"><img src="img/yarta-hero.webp" alt=""></span></span><span class="ln"><span class="cap team"><img src="img/bd-team.webp" alt="The {e(NAME)} team"></span><em>does a job.</em></span></h1>
  <div class="tags rv d2"><span class="chip">Websites</span><span class="chip">Custom apps</span><span class="chip">Google Ads</span><span class="chip">Social ads</span><span class="chip">SEO &amp; AI search</span><span class="chip">Automation</span></div>
  <div class="hero-sub"><img class="ast spin" src="img/bd-asterisk.svg" alt="" width="150" height="150">
    <div class="rv d3"><p>Websites, apps and systems for Aussie businesses that move real things: trucks, tonnes, safety checks and sales. Hand-built by a senior team, with no templates and no subscriptions. Here’s the work, and why it works.</p>
    <div class="ctas">{btn('Get Your Free Audit', CONTACT)}{btn('See The Work', '#work', 'ghost')}</div></div></div>
  <div class="agg countme rv"><div><b data-n="6">6</b><span>builds in this portfolio</span></div><div><b data-n="{total_pages}">{total_pages}</b><span>pages built</span></div><div><b data-n="335">335</b><span>edits shipped</span></div><div><b data-n="2">2</b><span>days, fastest launch</span></div></div>
  </div>
  <div class="reel" aria-hidden="true"><div class="tr">{reel}</div></div>
  <div class="marq"><div class="lbl">Helping Aussie homegrown businesses thrive</div><div class="tr" aria-hidden="true">{marq}</div></div>
</section>

<section class="sec light" id="work"><div class="wrap">
  <div class="sec-head"><div><div class="k rv">Selected builds</div><h2 class="h2 rv d1">Six builds. <em>Zero templates.</em></h2>
  <p class="lead rv d2">Each one hand-built around how the business actually works. Open any of them for the brief, the build, the screens and a live demo.</p></div>
  <div class="filters rv" role="group" aria-label="Filter the work"><button class="chip" data-f="all" aria-pressed="true">All work</button><button class="chip" data-f="web" aria-pressed="false">Websites</button><button class="chip" data-f="app" aria-pressed="false">Apps</button><button class="chip" data-f="brand" aria-pressed="false">Brand</button></div></div>
  <div class="cards">{cards}</div>
</div></section>

<section class="results" style="background-image:url(img/bd-results.webp)"><div class="wrap">
  <h2 class="rv">Proven results<br>by the numbers</h2>
  <div class="nums countme">{nums}<small>Across {e(NAME)} client accounts, as published on big.com.au.</small></div>
</div></section>

<section class="sec pat" id="growth"><div class="wrap">
  <div class="k rv">Grown by {e(NAME)}</div><h2 class="h2 rv d1" style="max-width:16ch">Ads and SEO that <em>pay their way.</em></h2>
  <p class="lead rv d2">The same senior team runs Google Ads, social, SEO and email for homegrown Aussie brands. A few of the headline results:</p>
  <div class="grow">{grow}</div>
  <div class="grow-foot rv"><p>Senior specialists only, fewer clients, and a strategy built around your numbers. Clients stay because the results do.</p>{btn('Get Your Free Audit', CONTACT)}</div>
</div></section>

<section class="sec light" id="clients"><div class="wrap">
  <div class="k rv">Client stories</div><h2 class="h2 rv d1">Hear it from <em>the clients.</em></h2>
  <div class="quotes">{quotes}</div>
</div></section>

<section class="sec white" id="services"><div class="wrap">
  <div class="sec-head"><div><div class="k rv">What we do</div><h2 class="h2 rv d1">Everything it takes <em>to grow.</em></h2></div>
  <p class="lead rv d2" style="max-width:40ch">Seven services, one senior team. Pick one, or let us audit the lot.</p></div>
  <div class="svc">{svc}</div>
</div></section>

<section class="contact pat" id="contact"><div class="wrap">
  <div class="k rv">Your turn</div>
  <h2 class="rv d1">Got a job<br><em>like this?</em></h2>
  <p class="lead rv d2">Tell us what’s slowing your business down. We’ll audit your website and ads for free and show you what we’d build or fix. No lock-in contracts, no sales pressure.</p>
  <div class="ct-grid">
  <form class="ct-form rv" id="audit-form" novalidate data-to="{BRAND['email']}">
    <h3>Free website &amp; ads audit</h3><p class="sub">Takes about a minute. Tell us where you want to grow.</p>
    <div class="f2"><div class="fld"><label for="f-name">Your name *</label><input id="f-name" name="name" autocomplete="name" required placeholder="Jane Smith"></div>
    <div class="fld"><label for="f-biz">Business</label><input id="f-biz" name="business" autocomplete="organization" placeholder="Business name"></div></div>
    <div class="f2"><div class="fld"><label for="f-email">Email *</label><input id="f-email" name="email" type="email" autocomplete="email" required placeholder="you@business.com.au"></div>
    <div class="fld"><label for="f-phone">Mobile</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" placeholder="04xx xxx xxx"></div></div>
    <div class="fld"><label for="f-site">Website</label><input id="f-site" name="website" type="url" inputmode="url" placeholder="https://"></div>
    <fieldset class="fs"><legend>What do you need help with?</legend><div class="opts">{opts}</div></fieldset>
    <div class="fld"><label for="f-msg">What’s slowing your business down? *</label><textarea id="f-msg" name="message" required placeholder="e.g. Our site doesn’t bring in enough leads and our ads cost too much per job."></textarea></div>
    <button class="btn big" type="submit">Send My Audit Request<span class="ic">{NE}</span></button>
    <p class="err" role="alert" aria-live="polite"></p>
    <p class="note">This opens your email app with everything filled in, addressed to {BRAND['email']}.</p>
  </form>
  <aside class="ct-side">
    <div class="box rv d1"><div class="k">Prefer to talk?</div><a class="big" href="tel:{BRAND['tel']}">{BRAND['phone']}</a></div>
    <div class="box rv d2"><div class="k">Email</div><a class="mid" href="mailto:{BRAND['email']}">{BRAND['email']}</a><div class="k" style="margin-top:22px">Visit</div><p>{e(BRAND['address'])}</p></div>
    <div class="box rv d3"><ul class="ticks"><li>No lock-in contracts</li><li>Senior specialists only, no juniors</li><li>A free audit with no sales pressure</li><li>Strategy built around your numbers</li></ul></div>
  </aside>
  </div>
</div></section>
</main>'''
    open(os.path.join(ROOT, 'index.html'), 'w').write(
        head(f'Our Work | {NAME}', f'Websites, apps and growth results from {NAME}: senior-led digital for Australian businesses. Get a free website and ads audit.', '') + body + footer(''))


for i, s in enumerate(STUDIES): study(i, s)
index()
print('built', len(STUDIES), 'case studies + index')
