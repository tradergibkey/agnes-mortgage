# -*- coding: utf-8 -*-
"""Agnes Mortgage — about, legal, 404, blog + runner. Run: python3 _gen_extra.py"""
from _gen_common import *
import _gen_pages as P

# =====================================================================
# ABOUT
# =====================================================================
def build_about():
    bc_json, crumb = breadcrumb("Meet Agnes", "Über Agnes", "Conozca a Agnes", "Ismerje meg Agnest", "about")
    jsonld = bc_json + f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Person","name":"[ADVISER FULL NAME]","jobTitle":"Mortgage Adviser",
"worksFor":{{"@type":"FinancialService","name":"Agnes Mortgage","url":"{BASE}"}},"url":"{BASE}/about"}}
</script>"""
    html = head(
        "Meet Agnes — Your Private Mortgage Adviser | Agnes Mortgage",
        "Meet the adviser behind Agnes Mortgage: FCA-regulated, whole-of-market, advising business owners, landlords and expats in English, German, Spanish and Hungarian.",
        "about", jsonld=jsonld)
    html += lang_gate() + header("about")
    html += f"""<main>
<section class="page-hero">
  <div class="container">
    {crumb}
    {t("h1", "Advice with a name: Agnes", "Beratung mit Namen: Agnes", "Asesoría con nombre propio: Agnes", "Tanácsadás névvel: Agnes")}
    {t("p", "One senior adviser. Your whole financial picture. A relationship measured in years, not transactions.",
       "Eine erfahrene Beraterin. Ihr gesamtes Finanzbild. Eine Beziehung, die in Jahren gemessen wird, nicht in Transaktionen.",
       "Una asesora sénior. Su panorama financiero completo. Una relación medida en años, no en transacciones.",
       "Egy vezető tanácsadó. Az Ön teljes pénzügyi képe. Egy kapcsolat, amit években mérünk, nem ügyletekben.")}
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="adviser-card reveal-item">
      <div class="adviser-photo"><img src="/img/about-placeholder.jpg" alt="Agnes — private mortgage adviser (professional portrait coming soon)"></div>
      <div>
        {t("span", "Your adviser", "Ihre Beraterin", "Su asesora", "Az Ön tanácsadója", cls="eyebrow")}
        {t("h2", "[ADVISER FULL NAME]", "[ADVISER FULL NAME]", "[ADVISER FULL NAME]", "[ADVISER FULL NAME]")}
        {t("p", "[BIO PARAGRAPH 1 — professional background, years in mortgage advice, previous roles, qualifications such as CeMAP. To be written after the intake interview.]",
           "[BIO ABSATZ 1 — beruflicher Werdegang, Jahre in der Hypothekenberatung, frühere Positionen, Qualifikationen. Wird nach dem Interview verfasst.]",
           "[PÁRRAFO BIO 1 — trayectoria profesional, años en asesoría hipotecaria, puestos anteriores, cualificaciones. Se redactará tras la entrevista.]",
           "[BIO 1. BEKEZDÉS — szakmai háttér, jelzálog-tanácsadói évek, korábbi pozíciók, képesítések. Az interjú után kerül megírásra.]")}
        {t("p", "[BIO PARAGRAPH 2 — personal angle: languages, international background, why business owners / landlords / expats, approach to clients.]",
           "[BIO ABSATZ 2 — persönlicher Blickwinkel: Sprachen, internationaler Hintergrund, Kundenphilosophie.]",
           "[PÁRRAFO BIO 2 — enfoque personal: idiomas, trayectoria internacional, filosofía con los clientes.]",
           "[BIO 2. BEKEZDÉS — személyes szál: nyelvek, nemzetközi háttér, ügyfélfilozófia.]")}
        <div class="badge-row">
          <span class="badge">{ICON['shield']} CeMAP [QUALIFICATION]</span>
          <span class="badge">{ICON['shield']} FCA [FCA NUMBER]</span>
          <span class="badge">🌍 EN · DE · ES · HU</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="container">
    <div class="section-head reveal-item">
      {t("span", "How we work", "So arbeiten wir", "Cómo trabajamos", "Így dolgozunk", cls="eyebrow")}
      {t("h2", "The principles behind the practice", "Die Prinzipien hinter der Praxis", "Los principios detrás de la práctica", "Az elvek a gyakorlat mögött")}
    </div>
    <div class="grid-3">
      <div class="step reveal-item"><div class="step-num">I</div>
        {t("h3", "Whole of market, no shortcuts", "Gesamtmarkt, keine Abkürzungen", "Todo el mercado, sin atajos", "Teljes piac, rövidítések nélkül")}
        {t("p", "Over 200 lenders, from global banks to private banks and specialist funds. The recommendation is driven by your case — never by a panel.",
           "Über 200 Kreditgeber — von Großbanken über Privatbanken bis zu Spezialfonds. Die Empfehlung folgt Ihrem Fall, nie einer Vorauswahl.",
           "Más de 200 prestamistas, desde grandes bancos hasta banca privada y fondos especializados. La recomendación la dicta su caso, nunca un panel.",
           "Több mint 200 hitelező — a nagybankoktól a privátbankokon át a speciális alapokig. Az ajánlást az Ön ügye vezérli, sosem egy előre szűkített lista.")}</div>
      <div class="step reveal-item"><div class="step-num">II</div>
        {t("h3", "Discretion as default", "Diskretion als Standard", "Discreción por defecto", "Diszkréció alapból")}
        {t("p", "Financial details stay between us and the lender that needs them. No data selling, no marketing lists, no exceptions.",
           "Finanzdaten bleiben zwischen uns und der Bank, die sie braucht. Kein Datenverkauf, keine Marketinglisten, keine Ausnahmen.",
           "Los detalles financieros quedan entre nosotros y el banco que los necesita. Sin venta de datos, sin listas de marketing, sin excepciones.",
           "A pénzügyi adatok köztünk és az azokat igénylő bank között maradnak. Nincs adateladás, nincs marketinglista, nincs kivétel.")}</div>
      <div class="step reveal-item"><div class="step-num">III</div>
        {t("h3", "In your language", "In Ihrer Sprache", "En su idioma", "Az Ön nyelvén")}
        {t("p", "Mortgage terms are complex enough in your mother tongue. Advice is available in English, German, Spanish and Hungarian — documents explained, not just translated.",
           "Hypothekenbedingungen sind schon in der Muttersprache komplex genug. Beratung auf Englisch, Deutsch, Spanisch und Ungarisch — Dokumente werden erklärt, nicht nur übersetzt.",
           "Los términos hipotecarios ya son complejos en su lengua materna. Asesoría en inglés, alemán, español y húngaro — documentos explicados, no solo traducidos.",
           "A jelzálogfeltételek anyanyelven is elég bonyolultak. A tanácsadás elérhető angolul, németül, spanyolul és magyarul — a dokumentumokat elmagyarázzuk, nem csak lefordítjuk.")}</div>
    </div>
  </div>
</section>

{marquee()}

{cta_band("Put a name to your mortgage strategy", "Geben Sie Ihrer Hypothekenstrategie einen Namen", "Ponga nombre a su estrategia hipotecaria", "Adjon nevet a jelzálogstratégiájának",
          "The first consultation is private, free and without obligation — and it usually changes what people think is possible.",
          "Das Erstgespräch ist vertraulich, kostenlos und unverbindlich — und ändert meist, was Menschen für möglich halten.",
          "La primera consulta es privada, gratuita y sin compromiso — y suele cambiar lo que la gente cree posible.",
          "Az első konzultáció privát, ingyenes és kötelezettségmentes — és általában megváltoztatja, mit gondol az ember lehetségesnek.")}
</main>
"""
    html += footer()
    open("about.html", "w").write(html)

# =====================================================================
# LEGAL (EN-only body — UK regulatory targeting; shared chrome still translates)
# =====================================================================
LEGAL_NOTE = '<p style="font-size:.85rem;color:var(--muted);border:1px solid var(--line);border-radius:10px;padding:12px 16px">This legal document is provided in English only, as our services are subject to the UK regulatory regime and targeted at consumers based in the United Kingdom.</p>'

def legal_page(slug, title, desc, h1, body):
    bc_json, crumb = breadcrumb(h1, h1, h1, h1, slug)
    html = head(title, desc, slug, jsonld=bc_json)
    html += lang_gate() + header("")
    html += f"""<main>
<section class="page-hero"><div class="container">{crumb}<h1>{h1}</h1></div></section>
<section class="section"><div class="container" style="max-width:820px">
{LEGAL_NOTE}
{body}
</div></section>
</main>
"""
    html += footer()
    open(f"{slug}.html", "w").write(html)

PRIVACY_BODY = """
<div class="post-body">
<p><em>Last updated: [DATE]</em></p>
<h2>1. Who we are</h2>
<p>Agnes Mortgage is a trading name of [LEGAL ENTITY NAME LTD], registered in England and Wales (company number [COMPANY NUMBER]), registered office [REGISTERED OFFICE ADDRESS]. We are the data controller for personal data collected through this website. Contact: [DATA CONTACT EMAIL / POSTAL ADDRESS].</p>
<h2>2. What we collect</h2>
<p>Information you submit through our contact form (name, email address, phone number, enquiry topic and message), and basic technical data necessary to deliver the website securely (IP address, browser type) processed by our hosting provider.</p>
<h2>3. Why we process it (lawful bases)</h2>
<p>To respond to your enquiry and provide mortgage advice at your request (steps prior to entering a contract, UK GDPR Art. 6(1)(b)); to meet our regulatory record-keeping obligations as an FCA-authorised firm (legal obligation, Art. 6(1)(c)); and to operate and secure this website (legitimate interests, Art. 6(1)(f)).</p>
<h2>4. Who receives your data</h2>
<p>Form submissions are transmitted via Web3Forms (form processing) and delivered to our business mailbox. If you become a client, relevant information is shared with lenders, insurers and other parties strictly as needed to arrange your mortgage, and only with your knowledge. We never sell personal data.</p>
<h2>5. Retention</h2>
<p>Enquiry data is kept for up to [X] months if you do not become a client. Client files are retained for the periods required by FCA rules and applicable law, typically a minimum of six years after the relationship ends.</p>
<h2>6. Your rights</h2>
<p>Under UK GDPR you may request access, rectification, erasure, restriction, portability, and object to processing based on legitimate interests. To exercise any right, contact [DATA CONTACT EMAIL]. You also have the right to complain to the Information Commissioner's Office (ico.org.uk).</p>
<h2>7. Cookies</h2>
<p>This website stores a single functional preference in your browser (your chosen language, key <code>am-lang</code>). No advertising or cross-site tracking cookies are set.</p>
</div>
"""

TERMS_BODY = """
<div class="post-body">
<p><em>Last updated: [DATE]</em></p>
<h2>1. About us and regulation</h2>
<p>Agnes Mortgage is a trading name of [LEGAL ENTITY NAME LTD], authorised and regulated by the Financial Conduct Authority (FCA number [FCA NUMBER]). You can verify our status on the Financial Services Register at register.fca.org.uk. The FCA does not regulate most buy-to-let mortgages, commercial lending or tax advice.</p>
<h2>2. Our service</h2>
<p>We provide advised mortgage intermediation on a whole-of-market basis: we assess your circumstances, recommend suitable products from across the market, and manage your application through to completion. We are not tied to any lender.</p>
<h2>3. Fees</h2>
<p>A fee of [FEE STRUCTURE — e.g. up to £X or Y% of the loan amount, payable on application/offer] may be charged for our advice. The exact amount depends on your circumstances and will be confirmed in writing before any chargeable work begins. We may also receive commission from the lender; its amount will be disclosed to you.</p>
<h2>4. Your obligations</h2>
<p>You agree to provide complete and accurate information. Providing false or incomplete information for a mortgage application may constitute fraud and will invalidate our advice.</p>
<h2>5. Website content</h2>
<p>Content on this website is for general information only and does not constitute personal advice. Rates and criteria change frequently; nothing here is an offer of lending. The guidance on this website is targeted at consumers based in the United Kingdom.</p>
<h2>6. Complaints</h2>
<p>If you are unhappy with our service, contact [COMPLAINTS CONTACT]. If we cannot resolve your complaint, you may refer it to the Financial Ombudsman Service (financial-ombudsman.org.uk) free of charge.</p>
<h2>7. Compensation</h2>
<p>We are covered by the Financial Services Compensation Scheme (FSCS). Mortgage advising and arranging is covered up to £85,000 per person. Details at fscs.org.uk.</p>
<h2>8. Risk warning</h2>
<p><strong>Your home may be repossessed if you do not keep up repayments on your mortgage.</strong></p>
</div>
"""

# =====================================================================
# 404
# =====================================================================
def build_404():
    html = head("Page Not Found | Agnes Mortgage", "The page you were looking for could not be found on the Agnes Mortgage site.", "404")
    html += f"""<div class="notfound">
  <div>
    <h1>404</h1>
    {t("p", "This page has moved on — like a good fixed rate.", "Diese Seite ist weitergezogen — wie eine gute Zinsbindung.", "Esta página se ha ido — como un buen tipo fijo.", "Ez az oldal továbblépett — mint egy jó fix kamat.", attrs='style="margin:14px 0 26px;color:rgba(255,255,255,.8)"')}
    <a href="/" class="btn btn-gold">{t("span", "Back to the homepage", "Zurück zur Startseite", "Volver al inicio", "Vissza a kezdőlapra")}</a>
  </div>
</div>
<script src="/js/scripts.js" defer></script>
</body>
</html>
"""
    open("404.html", "w").write(html)

# =====================================================================
# BLOG
# =====================================================================
POSTS = [
    {
        "slug": "limited-company-buy-to-let-2026",
        "title": "Limited Company Buy-to-Let in 2026: When Incorporation Actually Pays",
        "desc": "Personal name or limited company for your UK buy-to-let? The 2026 numbers on rates, tax and lender appetite — and the honest break-even test.",
        "img": "ltd-company-btl.jpg",
        "date": "2026-07-01",
        "datefmt": "1 July 2026",
        "tag": "Buy-to-Let",
        "body": """
<p>Five years ago the maths was awkward: limited-company buy-to-let rates carried a hefty premium over personal deals, and for many landlords the tax savings never caught up with the extra interest. In 2026 that premium has narrowed to the point where the old rule of thumb — "incorporation is only for big portfolios" — deserves retirement.</p>
<h2>What changed</h2>
<p>Three things. First, competition: the number of lenders actively courting SPV borrowers has grown every year, and pricing has compressed accordingly. Second, Section 24 has now fully worked through landlords' tax returns for long enough that higher-rate taxpayers can see precisely what mortgage interest relief restriction costs them annually in personal name. Third, lenders' stress tests treat company borrowers more generously in many cases, because corporation tax rates change the interest coverage arithmetic.</p>
<h2>The honest break-even test</h2>
<p>Incorporation still is not free. Moving existing properties into a company is a disposal: stamp duty and possibly capital gains tax apply, and the company remortgages at company pricing. The break-even question is simply whether the annual tax saving multiplied by your holding horizon exceeds those one-off costs plus any residual rate premium.</p>
<ul>
<li>Higher-rate taxpayer, planning to hold 10+ years, reinvesting profits into more property: the company route usually wins, often decisively.</li>
<li>Basic-rate taxpayer with one or two properties and no growth plans: personal name frequently remains the better answer.</li>
<li>Buying the <em>next</em> property? The calculus is different again — no transfer costs apply, so the company wrapper is cheap to choose from day one.</li>
</ul>
<h2>What we do differently</h2>
<p>We model both routes with live lender pricing before you commit, and we coordinate with your accountant so the tax assumptions are real, not folklore. If the personal route wins on your numbers, we will tell you so — the recommendation has to survive contact with your spreadsheet.</p>
<p>Thinking about your structure for the next purchase? A short conversation now can save an expensive restructuring later.</p>
"""
    },
    {
        "slug": "uk-mortgage-living-abroad-expat-guide",
        "title": "Getting a UK Mortgage While Living Abroad: What Lenders Really Check",
        "desc": "The expat mortgage playbook: foreign income, currency haircuts, credit footprint and the documents that make or break a UK application from overseas.",
        "img": "expat-uk-mortgage.jpg",
        "date": "2026-06-15",
        "datefmt": "15 June 2026",
        "tag": "Expat",
        "body": """
<p>Every week we speak to someone abroad who has been told by a high-street bank that a UK mortgage is "not possible" for them. Almost every time, the honest translation is: <em>not possible here</em>. The specialist expat market exists precisely for this borrower — but it assesses applications differently, and knowing the differences in advance is most of the battle.</p>
<h2>1. Your income will take a currency haircut</h2>
<p>Lenders discount foreign-currency income to protect against exchange-rate swings — commonly by 10–25% depending on the currency. Earning €120,000 does not mean lenders assess €120,000. We calculate the post-haircut figure per lender before anything is submitted, so the loan size never surprises you.</p>
<h2>2. The credit footprint problem is solvable</h2>
<p>Years abroad often mean a thin or dormant UK credit file. Some lenders insist on active UK credit; others accept international credit reports or build the picture from banking history. Keeping a UK bank account and an address history helps enormously — but its absence is a routing problem, not a refusal.</p>
<h2>3. Documents decide timelines</h2>
<p>Expect requests for: passport and visa status, employment contract, payslips and bank statements (sometimes translated and certified), tax returns from your country of residence, and proof of deposit source under anti-money-laundering rules. Applications from abroad fail slowly and painfully when documents trickle in — and fly through when the pack is complete on day one. Assembling that pack is a core part of our job.</p>
<h2>4. Buy-to-let is usually the smoother path</h2>
<p>Investment purchases are assessed primarily on the property's rental income, which sidesteps part of the foreign-income complexity. Many expats build a UK portfolio while abroad and refinance onto residential terms when they return.</p>
<p>Wherever you live, the process runs remotely: video calls, digital signatures, couriered originals where required — in English, German, Spanish or Hungarian.</p>
"""
    },
]

def post_card(p):
    return f"""      <article class="card reveal-item">
        <a href="/blog/posts/{p['slug']}.html" class="card-img"><img src="/blog/posts/images/{p['img']}" alt="{esc(p['title'])}" loading="lazy"></a>
        <div class="card-body">
          <span class="post-meta">{p['datefmt']} · {p['tag']}</span>
          <h2 style="font-size:1.28rem">{esc(p['title'])}</h2>
          <p>{esc(p['desc'])}</p>
          <a href="/blog/posts/{p['slug']}.html" class="card-link">Read the article {ICON['arrow']}</a>
        </div>
      </article>"""

def build_blog_index():
    bc_json, crumb = breadcrumb("Insights", "Insights", "Blog", "Blog", "blog")
    html = head("Insights & Guides — UK Mortgage Intelligence | Agnes Mortgage",
                "Plain-spoken guides on buy-to-let structuring, expat lending, HMO finance and remortgage timing — from a whole-of-market UK adviser.",
                "blog", jsonld=bc_json)
    html += lang_gate() + header("blog")
    cards = "\n".join(post_card(p) for p in POSTS)
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

def build_post(p, template=False):
    slug_path = "blog/posts/TEMPLATE" if template else f"blog/posts/{p['slug']}"
    canonical_slug = "blog/posts/{{SLUG}}.html" if template else f"blog/posts/{p['slug']}.html"
    title = "{{TITLE}}" if template else p["title"]
    desc = "{{DESCRIPTION}}" if template else p["desc"]
    img = "{{COVER_IMAGE}}" if template else f"/blog/posts/images/{p['img']}"
    date = "{{DATE_ISO}}" if template else p["date"]
    datefmt = "{{DATE_DISPLAY}}" if template else p["datefmt"]
    tag = "{{TAG}}" if template else p["tag"]
    body = "{{BODY_HTML}}" if template else p["body"]
    jsonld = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Article","headline":"{esc(title)}",
"description":"{esc(desc)}","image":"{BASE}{img}",
"datePublished":"{date}","dateModified":"{date}",
"author":{{"@type":"Organization","name":"Agnes Mortgage","url":"{BASE}"}},
"publisher":{{"@type":"Organization","name":"Agnes Mortgage","logo":{{"@type":"ImageObject","url":"{BASE}/img/apple-touch-icon.png"}}}},
"mainEntityOfPage":"{BASE}/{canonical_slug.replace('.html','')}"}}
</script>"""
    html = head(title if not template else "{{TITLE}} | Agnes Mortgage",
                desc, canonical_slug.replace(".html", ""), og_img=img if template is False else "/img/og-cover.jpg", jsonld=jsonld)
    html += lang_gate() + header("blog")
    html += f"""<main>
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="/">Home</a><span>›</span><a href="/blog">Insights</a><span>›</span><span>{tag}</span></div>
    <h1>{title}</h1>
    <p class="post-meta" style="color:rgba(255,255,255,.7)">{datefmt} · {tag} · Agnes Mortgage</p>
  </div>
</section>
<section class="section" style="padding-top:56px">
  <div class="container">
    <div class="post-hero-img"><img src="{img}" alt="{esc(title)}"></div>
    <div class="post-body">
{body}
    </div>
    <div style="max-width:780px;margin:40px auto 0">
      <div class="band-dark">
        <h2>Talk this through with an adviser</h2>
        <p>Every article generalises; your case is specific. A private consultation costs nothing and commits you to nothing.</p>
        <a href="/#contact" class="btn btn-gold">Request a consultation {ICON['arrow']}</a>
      </div>
    </div>
  </div>
</section>
</main>
"""
    html += footer()
    fname = "blog/post-template.html" if template else f"blog/posts/{p['slug']}.html"
    open(fname, "w").write(html)

# =====================================================================
# RUN
# =====================================================================
if __name__ == "__main__":
    import os
    os.makedirs("blog/posts/images", exist_ok=True)
    P.build_index()
    P.build_all_services()
    P.build_residential()
    P.build_remaining_services()
    build_about()
    legal_page("privacy-policy", "Privacy Policy | Agnes Mortgage",
               "How Agnes Mortgage collects, uses and protects personal data under UK GDPR.",
               "Privacy Policy", PRIVACY_BODY)
    legal_page("terms", "Terms of Business | Agnes Mortgage",
               "Terms of business for Agnes Mortgage: regulation, fees, complaints and FSCS coverage.",
               "Terms of Business", TERMS_BODY)
    build_404()
    build_blog_index()
    for p in POSTS:
        build_post(p)
    build_post(POSTS[0], template=True)
    print("ALL PAGES BUILT")
