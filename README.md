# Big Media: case studies

Six case studies and a work index, built as a static site.

**Pages:** `index.html` (work index) · `yarta/` · `recycle-group/` · `echeck/` · `recycled-metals/` · `t-waste/` · `nunjara/`

- `src/content.py`: every word, stat and image choice. Edit it, then run `python3 src/build.py` to rebuild all pages.
- `assets/site.css`: design. Brand tokens are at the top. Each case study takes its accent colour from the client's own brand.
- `assets/site.js`: motion (reveals, count-ups, hero tilt), the index hover previews and filters, the gallery, the lightbox and the live previews.
- `proto/`: the two Nunjara prototypes, embedded on the Nunjara page. They use fictional company names.
- `img/`: screenshots, captured from the live builds.

## Before it goes live
- Point `AUDIT_LINK` in `src/build.py` at the real audit or contact form. It's currently `#contact`.
- The eCheck page shows a partner rollout screen with the Afresh Metals logo. Confirm they're OK being shown.
- The Services nav link goes to `/#services` on the main Big Media site.
