#!/usr/bin/env node
/* build-sitemap.js — Agnes Mortgage
 *
 * Runs on every Vercel deploy (via package.json "build" script,
 * wired in vercel.json "buildCommand").
 *
 * What it does:
 *   1) Regenerates sitemap.xml with language-aware URLs and hreflang alternates
 *      for the blog indexes and translated blog posts.
 *   2) Injects Vercel Analytics into every HTML file that doesn't already have it
 *      (idempotent — a repeat run is a no-op).
 *
 * What it deliberately does NOT do:
 *   - Touch blog/index.html or any /blog/{lang}/index.html.
 *     ABB owns the blog indexes; having a second writer here causes
 *     the exact card-wipe race we fixed in _gen_extra.py in Aug 2026.
 *
 * Translated posts live at /blog/posts/{lang}/{slug}.html; hreflang
 * alternates are only emitted for translations that actually exist
 * on disk (Google penalises 404 alternates).
 */

const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");

const BASE = "https://agnesmortgage.co.uk";
const LANGS = ["de", "es", "hu"];
const today = new Date().toISOString().slice(0, 10);

const STATIC_PAGES = [
  { loc: "/", priority: "1.0", changefreq: "weekly" },
  { loc: "/buy-to-let", priority: "0.9", changefreq: "monthly" },
  { loc: "/hmo-finance", priority: "0.9", changefreq: "monthly" },
  { loc: "/expat-mortgages", priority: "0.9", changefreq: "monthly" },
  { loc: "/self-employed", priority: "0.9", changefreq: "monthly" },
  { loc: "/high-net-worth", priority: "0.9", changefreq: "monthly" },
  { loc: "/contractors", priority: "0.9", changefreq: "monthly" },
  { loc: "/residential", priority: "0.9", changefreq: "monthly" },
  { loc: "/remortgage", priority: "0.9", changefreq: "monthly" },
  { loc: "/calculators", priority: "0.8", changefreq: "monthly" },
  { loc: "/about", priority: "0.8", changefreq: "monthly" },
  { loc: "/privacy-policy", priority: "0.3", changefreq: "yearly" },
  { loc: "/terms", priority: "0.3", changefreq: "yearly" },
];

/* ---------- lastmod resolution ---------- */
/* Vercel does a fresh clone every build, so fs.statSync().mtime is worthless
 * (all files share the clone time). Use git commit date instead — the repo
 * is right there, git is installed on Vercel builds. Fall back to today if
 * anything fails, so a missing repo or a rename never breaks the build. */
function gitDate(relPath) {
  try {
    const out = execSync(`git log -1 --format=%cI -- "${relPath}"`, {
      cwd: __dirname, encoding: "utf8", stdio: ["ignore", "pipe", "ignore"],
    }).trim();
    return out ? out.slice(0, 10) : today;
  } catch (_) {
    return today;
  }
}
function fileFor(loc) {
  if (loc === "/") return "index.html";
  return loc.replace(/^\//, "") + ".html";
}

/* ---------- collect blog posts (all languages) ---------- */
/* Structure:
 *   blog/posts/{slug}.html          — English (canonical)
 *   blog/posts/{lang}/{slug}.html   — translation, once Phase 2 lands
 *
 * We key on EN slug. A post enters the sitemap iff its EN file exists.
 * Translations are optional; each detected translation adds one hreflang
 * alternate and one localised <url> entry with the same alternate set.
 */
function getPosts() {
  const enDir = path.join(__dirname, "blog", "posts");
  if (!fs.existsSync(enDir)) return [];

  const enFiles = fs.readdirSync(enDir).filter(f => f.endsWith(".html"));
  const posts = enFiles.map(f => {
    const slug = f.replace(/\.html$/, "");
    const enPath = path.join(enDir, f);
    const html = fs.readFileSync(enPath, "utf8");
    const dateMatch = html.match(/"datePublished":"([^"]*)"/);
    const date = (dateMatch ? dateMatch[1] : "").slice(0, 10) || gitDate(`blog/posts/${f}`);

    const langs = {};
    for (const l of LANGS) {
      const tPath = path.join(enDir, l, f);
      if (fs.existsSync(tPath)) {
        langs[l] = { date: gitDate(`blog/posts/${l}/${f}`) };
      }
    }
    return { slug, date, langs };
  });

  return posts.sort((a, b) => (a.date < b.date ? 1 : -1));
}

/* ---------- URL builders ---------- */
function postUrl(slug, lang) {
  return lang === "en"
    ? `${BASE}/blog/posts/${slug}`
    : `${BASE}/blog/posts/${lang}/${slug}`;
}
function indexUrl(lang) {
  return lang === "en" ? `${BASE}/blog` : `${BASE}/blog/${lang}`;
}

/* ---------- xhtml:link hreflang block ---------- */
/* Google's strict rule: every URL in a language cluster must list the full
 * set of alternates (self included) plus x-default → English canonical. */
function altLinks(urls) {
  const lines = [];
  for (const [lang, url] of Object.entries(urls)) {
    lines.push(`    <xhtml:link rel="alternate" hreflang="${lang}" href="${url}"/>`);
  }
  lines.push(`    <xhtml:link rel="alternate" hreflang="x-default" href="${urls.en}"/>`);
  return lines.join("\n");
}

/* ---------- sitemap ---------- */
function buildSitemap(posts) {
  const entries = [];

  // Static pages — no hreflang (single-language surfaces; the whole page
  // swaps text via data-attrs but the URL never changes).
  for (const p of STATIC_PAGES) {
    const lastmod = gitDate(fileFor(p.loc));
    entries.push(
      `  <url>\n` +
      `    <loc>${BASE}${p.loc === "/" ? "" : p.loc}</loc>\n` +
      `    <lastmod>${lastmod}</lastmod>\n` +
      `    <changefreq>${p.changefreq}</changefreq>\n` +
      `    <priority>${p.priority}</priority>\n` +
      `  </url>`
    );
  }

  // Blog indexes — one URL per language, each carrying the full 4-way cluster.
  const indexCluster = { en: indexUrl("en"), de: indexUrl("de"), es: indexUrl("es"), hu: indexUrl("hu") };
  for (const lang of ["en", ...LANGS]) {
    const lastmod = gitDate(lang === "en" ? "blog/index.html" : `blog/${lang}/index.html`);
    entries.push(
      `  <url>\n` +
      `    <loc>${indexUrl(lang)}</loc>\n` +
      `    <lastmod>${lastmod}</lastmod>\n` +
      `    <changefreq>weekly</changefreq>\n` +
      `    <priority>${lang === "en" ? "0.8" : "0.7"}</priority>\n` +
      altLinks(indexCluster) + "\n" +
      `  </url>`
    );
  }

  // Blog posts — EN plus every translation that actually exists on disk.
  for (const post of posts) {
    const cluster = { en: postUrl(post.slug, "en") };
    for (const lang of LANGS) {
      if (post.langs[lang]) cluster[lang] = postUrl(post.slug, lang);
    }

    // Canonical (EN)
    entries.push(
      `  <url>\n` +
      `    <loc>${postUrl(post.slug, "en")}</loc>\n` +
      `    <lastmod>${post.date}</lastmod>\n` +
      `    <changefreq>monthly</changefreq>\n` +
      `    <priority>0.6</priority>\n` +
      altLinks(cluster) + "\n" +
      `  </url>`
    );
    // Translations
    for (const lang of LANGS) {
      if (!post.langs[lang]) continue;
      entries.push(
        `  <url>\n` +
        `    <loc>${postUrl(post.slug, lang)}</loc>\n` +
        `    <lastmod>${post.langs[lang].date}</lastmod>\n` +
        `    <changefreq>monthly</changefreq>\n` +
        `    <priority>0.6</priority>\n` +
        altLinks(cluster) + "\n" +
        `  </url>`
      );
    }
  }

  const xml =
    `<?xml version="1.0" encoding="UTF-8"?>\n` +
    `<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n` +
    `        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n` +
    entries.join("\n") + "\n" +
    `</urlset>\n`;

  fs.writeFileSync(path.join(__dirname, "sitemap.xml"), xml);
  const totalTranslations = posts.reduce((n, p) => n + Object.keys(p.langs).length, 0);
  console.log(
    `sitemap.xml written: ${STATIC_PAGES.length} static + ${1 + LANGS.length} indexes ` +
    `+ ${posts.length} EN posts + ${totalTranslations} translations = ${entries.length} URLs`
  );
}

/* ---------- Vercel Analytics injection (idempotent) ---------- */
const ANALYTICS = `<script>window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };</script>\n<script defer src="/_vercel/insights/script.js"></script>`;

function walk(dir, out = []) {
  for (const f of fs.readdirSync(dir)) {
    const p = path.join(dir, f);
    const st = fs.statSync(p);
    if (st.isDirectory()) walk(p, out);
    else if (f.endsWith(".html")) out.push(p);
  }
  return out;
}
function injectAnalytics() {
  let n = 0;
  for (const file of walk(__dirname)) {
    let html = fs.readFileSync(file, "utf8");
    if (html.includes("/_vercel/insights/script.js")) continue;
    if (!html.includes("</body>")) continue;
    html = html.replace("</body>", `${ANALYTICS}\n</body>`);
    fs.writeFileSync(file, html);
    n++;
  }
  console.log(`Vercel Analytics injected into ${n} file(s)`);
}

/* ---------- run ---------- */
const posts = getPosts();
buildSitemap(posts);
injectAnalytics();
console.log("build-sitemap.js DONE");
