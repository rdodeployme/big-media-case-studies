"""Builds the Big Media case studies from content.py.
   python3 src/build.py  ->  index.html and <slug>/index.html"""
import html, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import STUDIES
e = html.escape
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUDIT = '#audit'          # header button scrolls to the audit band
AUDIT_LINK = '#contact'   # placeholder: point at the real audit / contact form
DARK = {'yarta':'#b5631a','recycle-group':'#c45a22','echeck':'#0f9a49','recycled-metals':'#4f5f6c','t-waste':'#10a845','nunjara':'#a87510'}
FILT = {'yarta':'web app','recycle-group':'web','echeck':'app','recycled-metals':'web','t-waste':'web brand','nunjara':'app'}
AR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
AL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M11 6l-6 6 6 6"/></svg>'
X = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>'

def head(title, desc, pre, accent='#f3f1ea', ink='#0a0a0a', dark='#0c0c0c', on='work'):
    return f'''<!doctype html>
<html lang="en-AU"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta name="theme-color" content="#0a0a0a">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}assets/site.css">
<style>:root{{--a:{accent};--a-ink:{ink};--a-dark:{dark}}}</style>
</head><body>
<div class="prog" aria-hidden="true"></div>
<header class="top"><div class="wrap">
  <a class="logo" href="{pre}">Big Media<i></i></a>
  <nav class="nav"><a class="{'on' if on=='work' else ''}" href="{pre}">Work</a><a href="{pre}#services">Services</a><a class="btn" href="{AUDIT}">Free website audit</a></nav>
</div></header>'''

def foot(pre):
    return f'''<section class="cta" id="audit"><div class="wrap">
  <div class="k rv">Your turn</div>
  <h2 class="rv d1">Got a job<br>like <em>this?</em></h2>
  <div class="row3 rv d2"><p>Tell us what’s slowing your business down. We’ll audit your website and ads for free and show you what we’d build instead of another subscription.</p>
  <a class="btn acc" href="{AUDIT_LINK}">Get a free audit {AR}</a></div>
</div></section>
<footer class="foot"><div class="wrap"><span>© 2026 Big Media</span><span>Websites, ads and custom apps for business</span></div></footer>
<div class="lb" role="dialog" aria-modal="true" aria-label="Screenshot"><img alt=""><div class="cap"></div><button class="x" aria-label="Close">{X}</button><button class="pv" aria-label="Previous">{AL}</button><button class="nx" aria-label="Next">{AR}</button></div>
<script src="{pre}assets/site.js" defer></script>
</body></html>'''

def frame(img, alt, pre, url='', lazy=True, zoom=True):
    bar = f'<div class="bar"><i></i><i></i><i></i>{f"<em>{e(url)}</em>" if url else ""}</div>'
    z = f' data-zoom="{pre}img/{img}.webp" data-cap="{e(alt)}" role="button" tabindex="0"' if zoom else ''
    return f'<div class="frame"{z}>{bar}<img src="{pre}img/{img}.webp" alt="{e(alt)}" width="1600" height="1000"{" loading=lazy decoding=async" if lazy else ""}></div>'

def short(u): return u.split('://')[-1].rstrip('/')

def stat(n, l, first=False):
    num = n if not n.isdigit() else f'<span data-n="{n}">{n}</span>'
    return f'<div class="rv"><b class="{"ac" if first else ""}">{num}</b><span>{e(l)}</span></div>'

def study(i, s):
    pre = '../'; nxt = STUDIES[(i + 1) % len(STUDIES)]
    live = (f'<a href="{e(s["url"])}" target="_blank" rel="noopener">{e(s["urltext"])} ↗</a>' if s['url'] else 'Prototype')
    meta = ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in [('Client', e(s['client'])), ('Service', e(s['service'])), ('Year', s['year']), ('Live', live)])
    stats = ''.join(stat(n, l, k == 0) for k, (n, l) in enumerate(s['stats']))
    feats = ''.join(f'''<article class="feat"><div class="ft rv"><div class="num">0{k+1}</div><h3>{e(h)}</h3><p>{e(p)}</p></div>
<figure class="rv d1">{frame(im, cap, pre)}<figcaption>{e(cap)}</figcaption></figure></article>''' for k, (h, p, im, cap) in enumerate(s['features']))
    gal = ''.join(f'<figure>{frame(im, cap, pre)}<figcaption>{e(cap)}</figcaption></figure>' for im, cap in s['gallery'])
    phones = ''.join(f'<div class="phone rv d{k}"><img src="{pre}img/{p}.webp" alt="{e(s["name"])} on a phone" loading="lazy" width="390" height="800"></div>' for k, p in enumerate(s['phones']))
    tl = ''
    if s['timeline']:
        tl = f'''<section class="tl" id="timeline"><div class="wrap"><div class="k rv">Timeline</div><h2 class="h2 rv d1">How it came together</h2>
<ol>{''.join(f'<li class="rv d{min(k,3)}"><b>{e(d)}</b><span>{e(t)}</span></li>' for k, (d, t) in enumerate(s['timeline']))}</ol></div></section>'''
    embed = s['embed']
    live_sec = f'''<section class="live" id="live"><div class="wrap">
<div class="row2"><div><div class="k rv">Try it</div><h2 class="h2 rv d1">Don’t take our word for it.</h2></div>
<a class="btn line rv" href="{e(embed)}" target="_blank" rel="noopener">Open full screen {AR}</a></div>
<div class="frame rv d1"><div class="bar"><i></i><i></i><i></i><em>{e(s['embed_label'])}</em></div>
<div class="vp" style="background-image:url({pre}img/{s['hero']}.webp)"><iframe title="{e(s['embed_label'])}" data-src="{e(embed)}" loading="lazy"></iframe>
<div class="cover"><button class="btn acc" type="button">Load the live {'prototype' if 'proto' in embed else 'site'} {AR}</button></div></div></div>
</div></section>'''
    visit = f'<a class="btn" href="{e(s["url"])}" target="_blank" rel="noopener">Visit the site {AR}</a>' if s['url'] else ''
    sub = ''.join(f'<a href="#{a}">{t}</a>' for a, t in [('brief','The brief'),('build','What we built'),('screens','Screens')] + ([('timeline','Timeline')] if s['timeline'] else []) + [('live','Try it'),('result','Result')])
    body = f'''
<main>
<section class="c-hero"><div class="wrap">
  <div class="crumb rv"><a href="../">Work</a> / {e(s['name'])}</div>
  <h1 class="rv d1">{e(s['title'])}</h1>
  <p class="c-line rv d2">{e(s['line'])}</p>
  <dl class="c-meta rv d3">{meta}</dl>
  <div class="stagewrap"><div class="tilt">{frame(s['hero'], s['name'], pre, s.get('heroUrl') or (short(s['url']) if s['url'] else 'prototype'), lazy=False)}</div></div>
</div></section>
<section class="stats"><div class="wrap"><div class="g">{stats}</div></div></section>
<nav class="subnav" aria-label="Sections"><div class="wrap"><span class="nm">{e(s['name'])}</span>{sub}</div></nav>
<div class="light">
<section class="sec" id="brief"><div class="wrap">
  <div class="k rv">The brief</div><h2 class="h2 rv d1">What they needed</h2>
  <div class="pg"><div class="rv"><h3>The problem</h3><p>{e(s['problem'])}</p></div><div class="rv d1"><h3>The goal</h3><p>{e(s['goal'])}</p></div></div>
</div></section>
<section class="sec tight" id="build"><div class="wrap">
  <div class="k rv">What we built</div><h2 class="h2 rv d1" style="margin-bottom:56px">The work</h2>
  {feats}
</div></section>
</div>
<section class="gal" id="screens"><div class="wrap galhead"><div><div class="k rv">Screens</div><h2 class="h2 rv d1">More of it</h2></div>
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
<a class="next" href="../{nxt['slug']}/" style="--na:{nxt['accent']}"><img src="{pre}img/{nxt['hero']}.webp" alt="" loading="lazy">
<div class="wrap"><div><div class="k">Next case study</div><strong>{e(nxt['name'])}</strong></div><span class="ar">{AR}</span></div></a>
</main>'''
    os.makedirs(os.path.join(ROOT, s['slug']), exist_ok=True)
    t = f"{s['name']}: {s['kicker']} | Big Media"
    open(os.path.join(ROOT, s['slug'], 'index.html'), 'w').write(head(t, s['line'], pre, s['accent'], s['ink'], DARK[s['slug']]) + body + foot(pre))

def index():
    rows = ''.join(f'''<a class="row rv" href="{s['slug']}/" data-img="img/{s['hero']}.webp" data-f="{FILT[s['slug']]}" style="--c:{s['accent']}">
<span class="th"><img src="img/{s['hero']}.webp" alt="" loading="lazy" width="1600" height="1000"></span>
<span class="n">0{k+1}</span><h2>{e(s['name'])}</h2><span class="sv">{e(s['service'])}</span><span class="kk">{e(s['kicker'])}</span><span class="ar">{AR}</span></a>''' for k, s in enumerate(STUDIES))
    reel = ''.join(f'<img src="img/{im}.webp" alt="" loading="lazy">' for s in STUDIES for im in [s['features'][0][2], s['gallery'][0][0]]) * 2
    marq = ''.join(f'<span style="color:{s["accent"]}">{e(s["name"])}</span>' for s in STUDIES) * 2
    body = f'''
<main>
<section class="ix-hero"><div class="wrap">
  <div class="k rv">Big Media · Selected work · 2026</div>
  <h1 class="rv d1"><span>Work that</span><span><em>does</em> a job.</span></h1>
  <div class="ix-sub"><p class="rv d2">Websites, apps and systems for businesses that move real things: trucks, tonnes, safety checks and sales. No templates, no subscriptions. Here’s what we built and why.</p>
  <div class="agg rv d3"><div><b data-n="6">6</b><span>projects</span></div><div><b data-n="153">153</b><span>pages built</span></div><div><b data-n="335">335</b><span>edits shipped</span></div><div><b data-n="2">2</b><span>days, fastest launch</span></div></div></div>
</div>
<div class="marq" aria-hidden="true"><div class="tr">{marq}</div></div>
<div class="reel" aria-hidden="true"><div class="tr">{reel}</div></div></section>
<section id="work"><div class="wrap">
  <div class="filters rv"><span class="k">Filter</span><button class="chip" data-f="all" aria-pressed="true">All work</button><button class="chip" data-f="web" aria-pressed="false">Websites</button><button class="chip" data-f="app" aria-pressed="false">Apps</button><button class="chip" data-f="brand" aria-pressed="false">Brand</button></div>
  <div class="rows">{rows}</div>
</div></section>
<div class="peek" aria-hidden="true"><img alt=""></div>
</main>'''
    # the hero stat numbers count up when they come into view
    body = body.replace('<div class="agg rv d3">', '<div class="agg rv d3 countme">')
    open(os.path.join(ROOT, 'index.html'), 'w').write(head('Work | Big Media', 'Websites, apps and systems built by Big Media.', '') + body + foot(''))

for i, s in enumerate(STUDIES): study(i, s)
index()
print('built', len(STUDIES), 'case studies + index')
