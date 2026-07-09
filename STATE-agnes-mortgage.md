# STATE — agnes-mortgage
Updated: 2026-07-09 · Status: **v1 built, QA passed, ready for first deploy**

## What this is
UK private mortgage advisory site "Agnes Mortgage" for business owners, portfolio landlords, HNW clients and expats. Vercel-only for now (no domain yet). Navy+gold private-banking skin on the emlektabla design system.

## Locked decisions
- Vercel project name must be `agnes-mortgage` → canonical BASE `https://agnes-mortgage.vercel.app` (one-line swap in build-sitemap.js when real domain arrives)
- UK-only: GB geo tags, areaServed United Kingdom, FCA compliance (risk warning + FCA/legal placeholders in footer, EN-only legal pages, UK GDPR privacy)
- 4 languages EN/DE/ES/HU via data-attribute toggle + first-visit language gate, localStorage `am-lang`; hreflang intentionally skipped (single URL serves all langs)
- Phone/WhatsApp placeholder: +44 7700 900123 (Ofcom fictional range — must swap)
- Palette: navy #0B1830/#122548/#1A335F + gold #C9A24B/#DDBE72/#EBD9A6, Playfair Display + Inter
- 6 service pages: buy-to-let, hmo-finance, expat-mortgages, self-employed, high-net-worth, remortgage
- Adviser bio + photo slots reserved on / and /about ([ADVISER FULL NAME], bio placeholders, img/about-placeholder.jpg)

## Built (v1 complete)
- 15 HTML pages: index, 6 services (each: hero, split+5 checks, split+2¶, 3-FAQ w/ FAQPage JSON-LD, CTA), about, privacy-policy, terms, 404, blog/index (BLOG-LIST markers), post-template (ABB-compatible), 2 seed posts
- css/styles.css (full navy/gold system), js/scripts.js (lang engine, gate, nav, marquee shuffle+50% loop, FAQ, reveal, video fallback, Web3Forms submit)
- 13 Pillow images (navy/gold dark 3D-studio style): hero-fallback, 6 svc images, about-placeholder, og-cover, 2 favicons, 2 blog covers
- 23-review marquee (EN + 2 HU + 2 DE + 2 ES)
- robots.txt (+Llms-txt), llms.txt, sitemap.xml (13 URLs), vercel.json (cleanUrls + CSP/security headers, validated), build-sitemap.js + package.json (sitemap + analytics injection + blog grid rebuild, tested), local-server.py + start-local.bat, README-DEPLOY.md
- QA: 0 findings (tag balance, 1×H1, no heading jumps, JSON-LD parses, title/desc lengths, links resolve, full 4-lang attr coverage, no emails, no /blog/ trailing slash)

## Pending (go-live checklist — full table in README-DEPLOY.md)
1. Web3Forms key (YOUR_WEB3FORMS_KEY in index.html)
2. Real phone number (search 7700 900123 + 447700900123)
3. [LEGAL ENTITY NAME LTD] / [COMPANY NUMBER] / [FCA NUMBER] / registered office — footer + legal pages + about
4. Adviser name, bio, qualification, photo-shoot images
5. Legal page placeholders ([DATE], fee structure, complaints/data contacts)
6. Real testimonials (edit _gen_common.py REVIEWS or HTML directly)
7. Hero video: Pexels SD 640×360 → img/hero-video.mp4 (candidates given in chat 2026-07-09; .mp4.mp4 trap)
8. Deploy: private GitHub repo `agnes-mortgage` → Vercel import → enable Analytics
9. Later: real domain (BASE swap + search-replace + re-run build-sitemap.js), Search Console, ABB tenant onboarding

## Build tools in repo
_gen_common.py (chrome/translations/REVIEWS), _gen_pages.py (index+services), _gen_extra.py (about/legal/404/blog + runner). Regenerate: `python3 _gen_extra.py && node build-sitemap.js`. Note: regeneration wipes manual HTML edits — edit generators instead where possible.
