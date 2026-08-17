# Patch for `_gen_extra.py` — stop the blog index wipe

## What this fixes

`_gen_extra.py`'s `build_blog_index()` overwrites `blog/index.html` from a
hardcoded 2-post list every time it runs. ABB adds cards to that same file
between the `<!-- BLOG-LIST-START -->` / `<!-- BLOG-LIST-END -->` markers.
Whichever writes last wins — which is why the seed posts and ABB posts kept
disappearing from the grid.

The patched function reads the existing file first and preserves whatever
sits between the markers. Chrome (head, nav, hero, footer) is still
regenerated on every run, so any change to shared components still propagates.
The hardcoded `POSTS` list is only used as a bootstrap fallback when
`blog/index.html` doesn't exist yet.

## How to apply

In `_gen_extra.py`, find the current `build_blog_index()` function and
REPLACE it entirely with the version below. Nothing else in the file needs
to change. Add `import os, re` at the top of the file if they aren't already
imported (they're only needed here, so importing inside the function is fine
too — the version below does that so you can drop it in with no other edits).

## Replacement function

```python
def build_blog_index():
    """Rebuild the blog index chrome while PRESERVING existing cards between
    the BLOG-LIST markers. ABB adds cards to those markers on every publish;
    this function must never clobber them. Falls back to the hardcoded POSTS
    list only when blog/index.html does not exist yet (first bootstrap)."""
    import os, re
    bc_json, crumb = breadcrumb("Insights", "Insights", "Blog", "Blog", "blog")

    # ---- Preserve existing card list if the file is already there ----
    existing_cards = None
    if os.path.exists("blog/index.html"):
        try:
            with open("blog/index.html", "r", encoding="utf-8") as f:
                current = f.read()
            m = re.search(
                r"<!-- BLOG-LIST-START -->(.*?)<!-- BLOG-LIST-END -->",
                current, re.DOTALL)
            if m:
                existing_cards = m.group(1).strip("\n")
        except Exception as e:
            print(f"[build_blog_index] Could not read existing index, "
                  f"falling back to POSTS bootstrap: {e}")

    if existing_cards is not None:
        cards = existing_cards
    else:
        # Bootstrap: no existing file, use the hardcoded seed POSTS
        cards = "\n".join(post_card(p) for p in POSTS)

    html = head("Insights & Guides — UK Mortgage Intelligence | Agnes Mortgage",
                "Plain-spoken guides on buy-to-let structuring, expat lending, HMO finance and remortgage timing — from a whole-of-market UK broker.",
                "blog", jsonld=bc_json)
    html += lang_gate() + header("blog")
    html += f"""<main>
<section class="page-hero">
  <div class="container">
    {crumb}
    {t("h1", "Insights & guides", "Insights & Ratgeber", "Blog y guías", "Blog és útmutatók")}
    {t("p", "Plain-spoken intelligence on specialist UK lending. Articles are published in English.",
       "Klartext zu spezialisierten UK-Finanzierungen. Artikel erscheinen auf Englisch.",
       "Análisis claro sobre financiación especializada en el Reino Unido. Los artículos se publican en inglés.",
       "Közérthető elemzések a speciális brit hitelezésről. A cikkek angol nyelven jelennek meg.")}
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="blog-grid">
<!-- BLOG-LIST-START -->
{cards}
<!-- BLOG-LIST-END -->
    </div>
  </div>
</section>
</main>
"""
    html += footer()
    open("blog/index.html", "w").write(html)
```

## Behavioural check

- **First run on a repo with no `blog/index.html`** → seeds get written from
  POSTS. Same as before.
- **Re-run on existing site** → chrome refreshes, current cards stay put. ABB
  additions survive.
- **File is present but markers are missing** → falls back to POSTS bootstrap.
  Safe.
- **File exists but markers are empty** → keeps them empty. Correct: means
  the site owner has deliberately cleared it. Add cards back through ABB or a
  bootstrap re-run with the file deleted.

## Optional cleanup

The `POSTS` list at the top of the file becomes bootstrap-only after this
patch. The runner still calls `build_post(p)` for each POST to generate the
seed post HTML files — leave that alone unless you want to stop regenerating
the two seed post pages on every run (they haven't changed in weeks, so
it's harmless either way).
