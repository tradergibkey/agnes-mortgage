# Agnes Mortgage — Deploy Guide

Static site: HTML + CSS + JS, no build framework. Deploys to Vercel by GitHub drag-and-drop, exactly like the other sites.

## First deploy

1. Create a **private** GitHub repo named `agnes-mortgage`.
2. Drag-and-drop the entire contents of this folder into the repo (keep the folder structure: `css/`, `js/`, `img/`, `blog/`, root files).
3. In Vercel: **Add New Project** → import `agnes-mortgage` → Framework preset: **Other** → deploy.
4. Vercel will serve it at `https://agnes-mortgage.vercel.app` (the name must match — canonicals, sitemap and og:urls all point there).
5. Vercel → Project → **Analytics** → Enable. The pages already load `/_vercel/insights/script.js`.

## Local preview

- Windows: double-click `start-local.bat`
- Any OS: `python3 local-server.py` → http://localhost:8000
- The local server mimics Vercel's cleanUrls (`/buy-to-let` → `buy-to-let.html`).

## Adding a blog post (until ABB takes over)

1. Copy `blog/post-template.html` → `blog/posts/your-slug.html`, replace the `{{PLACEHOLDERS}}`.
2. Put the cover image in `blog/posts/images/`.
3. Run `node build-sitemap.js` — it updates `sitemap.xml` and rebuilds the card grid on `/blog` automatically.
4. Upload the changed files.

The blog structure (post-template, BLOG-LIST markers, images folder, URL pattern `/blog/posts/<slug>`) is AI Blog Builder-compatible — the site can be onboarded as an ABB tenant later without restructuring.

## Language system

- 4 languages: EN (default), DE, ES, HU — every string carries `data-en/de/es/hu` attributes; `js/scripts.js` swaps them.
- First visit shows a language gate; the choice is stored in `localStorage` under `am-lang`.
- One URL serves all languages, so no hreflang tags are used (hreflang requires separate URLs per language). If per-language URLs are ever wanted, that's a separate build.
- Legal pages (privacy, terms) are English-only by design — UK regulatory targeting.

## GO-LIVE CHECKLIST (placeholders to replace)

| # | Item | Where |
|---|------|-------|
| 1 | `YOUR_WEB3FORMS_KEY` → real Web3Forms access key | `index.html` (contact form) |
| 2 | Phone `+44 7700 900123` → real number (it's an Ofcom fictional number) | all pages: `tel:`, `wa.me/`, displayed text — search for `7700 900123` and `447700900123` |
| 3 | `[LEGAL ENTITY NAME LTD]`, `[COMPANY NUMBER]`, `[REGISTERED OFFICE ADDRESS]`, `[FCA NUMBER]` | footer (all pages), `privacy-policy.html`, `terms.html`, `about.html` |
| 4 | `[ADVISER FULL NAME]`, bio paragraphs, `[QUALIFICATION]` | `about.html` (+ Person JSON-LD in its head) |
| 5 | `[DATE]`, `[X]` months, `[FEE STRUCTURE]`, `[COMPLAINTS CONTACT]`, `[DATA CONTACT EMAIL / POSTAL ADDRESS]` | `privacy-policy.html`, `terms.html` |
| 6 | Adviser photos from the photo shoot → replace `img/about-placeholder.jpg` | homepage split + about page |
| 7 | Real client testimonials → replace the 23 marquee reviews | `_gen_common.py` REVIEWS + regenerate, or edit the HTML directly |
| 8 | Hero video: download chosen Pexels clip in **SD 640×360**, rename to exactly `hero-video.mp4` (watch out for the hidden `.mp4.mp4` trap), upload to `img/` | homepage hero |
| 9 | Real domain: one-line swap of `BASE` in `build-sitemap.js`, then search-replace `https://agnes-mortgage.vercel.app` across HTML, re-run `node build-sitemap.js` | canonicals, og:url, JSON-LD, sitemap |
| 10 | After domain: add to Google Search Console (DNS verify), submit sitemap | — |

Until #1 is done the contact form will not deliver — Web3Forms rejects the placeholder key.
