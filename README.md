# Big Digital: work

Big Digital's portfolio: ten build case studies, a strip of nine more live sites, and the agency's growth results, testimonials, services and a free audit form. Static site on GitHub Pages.

**Live:** https://rdodeployme.github.io/big-media-case-studies/

**Pages:** `index.html` (home: work, more sites, results, growth, testimonials, services, contact) · `yarta/` · `truckrentals/` · `recycle-group/` · `trash/` · `echeck/` · `declutter/` · `recycled-metals/` · `no-more-dumping/` · `t-waste/` · `nunjara/`

- `src/content.py`: every word, stat and image choice. Edit it, then run `python3 src/build.py` to rebuild all pages.
  - `STUDIES`: the ten builds, ordered by `ORDER` so brands alternate. Figures come from the builds themselves: page counts and commits from each repo, counts read off the live sites.
  - `AGG_PAGES`, `AGG_EDITS`: the home-page totals. Update them when a build is added.
  - `MORE`: the "More sites" strip, with name, one-liner, live link and thumbnail.
  - `RESULTS`, `GROWTH`, `TESTIMONIALS`, `SERVICES`, `CLIENTS`: as published on big.com.au. Don't add figures or quotes that aren't there.
  - `BRAND`: name, phone, email, address. `BRAND['name']` is the one switch for the brand name shown across the site.
- `assets/site.css`: design, using Big Digital's brand from big.com.au. Phudu headings, Google Sans body, black `#000204`, lime `#C4F112` highlights on dark, orange `#FF5420` on light, the asterisk motif and pill buttons. Each case study's result band keeps the client's own colour.
- `assets/site.js`: motion (reveals, count-ups, hero tilt), filters, gallery, lightbox, live previews and the audit form.
- `img/truck-*`, `img/trash-*`, `img/dec-*`, `img/nmd-*`, `img/more-*`: screens captured from the live builds on 24 Nov 2026. Phone shots (`*-m1/2/3`) have a status bar added so the mockup notch doesn't cover the page.
- `img/bd-*`, `img/grow-*`, `img/t-*`: Big Digital's logo, backgrounds, case photos and client avatars, taken from big.com.au.
- `img/echeck-scene-*`, `img/echeck-p*`: eCheck shown as phone and desktop mockups, composed from screens captured on the live app at echeck.com.au (24 Nov 2026).
- `proto/`: the two Nunjara prototypes, embedded on the Nunjara page. They use fictional company names.

## Needs confirmation
- **Declutter:** its own live site still shows the placeholder `1300 XXX XXX` phone number. It's hidden in the screenshots here, but it shows in the live embed until the real number goes in.
- **Audit form:** there's no backend. Submitting opens the visitor's email app with a pre-filled request to info@big.com.au. Swap it for a Google Sheet or CRM hook if you want submissions captured automatically.
- **Logo:** the official `logo.png` from big.com.au is 156 px wide, so it's slightly soft on retina screens. Replace `img/bd-logo.png` with a high-res or SVG version of the official file when you have it.
