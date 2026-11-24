# Big Digital: work

Big Digital's portfolio: six build case studies plus the agency's growth results, testimonials, services and a free audit form. Static site on GitHub Pages.

**Live:** https://rdodeployme.github.io/big-media-case-studies/

**Pages:** `index.html` (home: work, results, growth, testimonials, services, contact) · `yarta/` · `recycle-group/` · `echeck/` · `recycled-metals/` · `t-waste/` · `nunjara/`

- `src/content.py`: every word, stat and image choice. Edit it, then run `python3 src/build.py` to rebuild all pages.
  - `STUDIES`: the six builds. Figures come from the builds themselves.
  - `RESULTS`, `GROWTH`, `TESTIMONIALS`, `SERVICES`, `CLIENTS`: as published on big.com.au. Don't add figures or quotes that aren't there.
  - `BRAND`: name, phone, email, address. `BRAND['name']` is the one switch for the brand name shown across the site.
- `assets/site.css`: design, using Big Digital's brand from big.com.au. Phudu headings, Google Sans body, black `#000204`, lime `#C4F112` highlights on dark, orange `#FF5420` on light, the asterisk motif and pill buttons. Each case study's result band keeps the client's own colour.
- `assets/site.js`: motion (reveals, count-ups, hero tilt), filters, gallery, lightbox, live previews and the audit form.
- `img/bd-*`, `img/grow-*`, `img/t-*`: Big Digital's logo, backgrounds, case photos and client avatars, taken from big.com.au.
- `proto/`: the two Nunjara prototypes, embedded on the Nunjara page. They use fictional company names.

## Needs confirmation
- **Audit form:** there's no backend. Submitting opens the visitor's email app with a pre-filled request to info@big.com.au. Swap it for a Google Sheet or CRM hook if you want submissions captured automatically.
- **Logo:** the official `logo.png` from big.com.au is 156 px wide, so it's slightly soft on retina screens. Replace `img/bd-logo.png` with a high-res or SVG version of the official file when you have it.
- **eCheck:** the page shows a partner rollout screen with the Afresh Metals logo. Confirm they're OK being shown.
