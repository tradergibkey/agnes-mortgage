#!/usr/bin/env node
/* build-sitemap.js — Agnes Mortgage
 * Regenerates sitemap.xml from static pages + blog/posts scan,
 * injects Vercel Analytics into every HTML file,
 * rebuilds the blog index card grid between BLOG-LIST markers.
 * Run locally or as Vercel build step: node build-sitemap.js
 */
const fs = require("fs");
const path = require("path");

const BASE = "https://agnes-mortgage.vercel.app"; // ← swap when the real domain goes live

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
  { loc: "/blog", priority: "0.8", changefreq: "weekly" },
  { loc: "/privacy-policy", priority: "0.3", changefreq: "yearly" },
  { loc: "/terms", priority: "0.3", changefreq: "yearly" },
];

const POSTS_DIR = path.join(__dirname, "blog", "posts");
const today = new Date().toISOString().slice(0, 10);

/* ---------- collect blog posts ---------- */
function getPosts() {
  if (!fs.existsSync(POSTS_DIR)) return [];
  return fs.readdirSync(POSTS_DIR)
    .filter(f => f.endsWith(".html"))
    .map(f => {
      const html = fs.readFileSync(path.join(POSTS_DIR, f), "utf8");
      const get = re => (html.match(re) || [, ""])[1].trim();
      return {
        slug: f.replace(/\.html$/, ""),
        title: get(/<title>([^|<]+)/),
        desc: get(/<meta name="description" content="([^"]*)"/),
        date: get(/"datePublished":"([^"]*)"/) || today,
        img: get(/<meta property="og:image" content="[^"]*?(\/blog\/posts\/images\/[^"]+)"/) ||
             get(/class="post-hero-img"><img src="([^"]+)"/),
        dateDisplay: get(/class="post-meta"[^>]*>([^·<]+)/),
        tag: get(/<span>([^<]+)<\/span><\/div>\s*<h1>/),
      };
    })
    .sort((a, b) => (a.date < b.date ? 1 : -1));
}

/* ---------- sitemap ---------- */
function buildSitemap(posts) {
  const urls = [
    ...STATIC_PAGES.map(p =>
      `  <url><loc>${BASE}${p.loc === "/" ? "" : p.loc}</loc><lastmod>${today}</lastmod><changefreq>${p.changefreq}</changefreq><priority>${p.priority}</priority></url>`),
    ...posts.map(p =>
      `  <url><loc>${BASE}/blog/posts/${p.slug}</loc><lastmod>${p.date}</lastmod><changefreq>yearly</changefreq><priority>0.6</priority></url>`),
  ].join("\n");
  const xml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls}\n</urlset>\n`;
  fs.writeFileSync(path.join(__dirname, "sitemap.xml"), xml);
  console.log(`sitemap.xml written (${STATIC_PAGES.length + posts.length} URLs)`);
}

/* ---------- Vercel Analytics injection ---------- */
const ANALYTICS = `<script>window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };</script>\n<script defer src="/_vercel/insights/script.js"></script>`;
function walk(dir, out = []) {
  for (const f of fs.readdirSync(dir)) {
    const p = path.join(dir, f);
    if (fs.statSync(p).isDirectory()) walk(p, out);
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

/* ---------- blog index card grid ---------- */
const ARROW = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>';
function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/"/g, "&quot;"); }
function rebuildBlogIndex(posts) {
  const idx = path.join(__dirname, "blog", "index.html");
  if (!fs.existsSync(idx)) return;
  let html = fs.readFileSync(idx, "utf8");
  const cards = posts.map(p => `      <article class="card reveal-item">
        <a href="/blog/posts/${p.slug}.html" class="card-img"><img src="${p.img}" alt="${esc(p.title)}" loading="lazy"></a>
        <div class="card-body">
          <span class="post-meta">${esc(p.dateDisplay)} · ${esc(p.tag)}</span>
          <h2 style="font-size:1.28rem">${esc(p.title)}</h2>
          <p>${esc(p.desc)}</p>
          <a href="/blog/posts/${p.slug}.html" class="card-link">Read the article ${ARROW}</a>
        </div>
      </article>`).join("\n");
  html = html.replace(/<!-- BLOG-LIST-START -->[\s\S]*<!-- BLOG-LIST-END -->/,
    `<!-- BLOG-LIST-START -->\n${cards}\n<!-- BLOG-LIST-END -->`);
  fs.writeFileSync(idx, html);
  console.log(`blog/index.html card grid rebuilt (${posts.length} post(s))`);
}

const posts = getPosts();
buildSitemap(posts);
injectAnalytics();
rebuildBlogIndex(posts);
console.log("build-sitemap.js DONE");
