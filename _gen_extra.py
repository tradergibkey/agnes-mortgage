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
{{"@context":"https://schema.org","@type":"Person","name":"Agnes Siry","image":"{BASE}/img/agnes-siry.webp","jobTitle":"Mortgage Broker",
"worksFor":{{"@type":"FinancialService","name":"Agnes Mortgage","url":"{BASE}"}},"hasCredential":{{"@type":"EducationalOccupationalCredential","credentialCategory":"certification","name":"CeMAP 3"}},"url":"{BASE}/about"}}
</script>"""
    html = head(
        "Meet Agnes — Your Private Mortgage Broker | Agnes Mortgage",
        "Meet the broker behind Agnes Mortgage: FCA-regulated, whole-of-market, advising business owners, landlords and expats in English, German, Spanish and Hungarian.",
        "about", jsonld=jsonld)
    html += lang_gate() + header("about")
    html += f"""<main>
<section class="page-hero">
  <div class="container">
    {crumb}
    {t("h1", "Advice with a name: Agnes", "Beratung mit Namen: Agnes", "Asesoría con nombre propio: Agnes", "Tanácsadás névvel: Agnes")}
    {t("p", "One senior broker. Your whole financial picture. A relationship measured in years, not transactions.",
       "Ein erfahrener Makler. Ihr gesamtes Finanzbild. Eine Beziehung, die in Jahren gemessen wird, nicht in Transaktionen.",
       "Un bróker sénior. Su panorama financiero completo. Una relación medida en años, no en transacciones.",
       "Egy vezető bróker. Az Ön teljes pénzügyi képe. Egy kapcsolat, amit években mérünk, nem ügyletekben.")}
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="adviser-card reveal-item">
      <div class="adviser-photo"><img src="/img/agnes-siry.webp" alt="Agnes Siry, mortgage broker at Agnes Mortgage" width="1200" height="1405"></div>
      <div>
        {t("span", "Your broker", "Ihr Makler", "Su bróker", "Az Ön brókere", cls="eyebrow")}
        {t("h2", "Agnes Siry", "Agnes Siry", "Agnes Siry", "Agnes Siry")}
        {t("p", "Hi, I'm Agnes. Over the last 17+ years I've worked across financial services — mortgages, pensions, investments, accounting, protection — and along the way I found where I actually belong: helping people get the right mortgage, with the right cover behind it.",
           "Hallo, ich bin Agnes. In den letzten 17+ Jahren habe ich in verschiedenen Bereichen der Finanzdienstleistungen gearbeitet — Hypotheken, Renten, Investments, Buchhaltung, Absicherung — und dabei habe ich gefunden, wo ich wirklich hingehöre: Menschen zur richtigen Hypothek zu verhelfen, mit der richtigen Absicherung dahinter.",
           "Hola, soy Agnes. En los últimos 17+ años he trabajado en varias áreas de los servicios financieros — hipotecas, pensiones, inversiones, contabilidad, protección — y en el camino encontré dónde realmente pertenezco: ayudando a las personas a conseguir la hipoteca adecuada, con la cobertura adecuada detrás.",
           "Szia, Agnes vagyok. Az elmúlt 17+ évben a pénzügyi szolgáltatások szinte minden területén dolgoztam — jelzáloghitelek, nyugdíjak, befektetések, könyvelés, biztosítások — és útközben megtaláltam, hogy valójában hol a helyem: segíteni az embereknek a megfelelő jelzáloghitelt megtalálni, mögötte a megfelelő biztosítással.")}
        {t("p", "Mortgages are one of the biggest financial decisions most of us ever make, and I don't think anyone should walk into that decision half-informed. So my approach leans heavily on education. When we work together, you'll understand your options, the trade-offs, and <em>why</em> we're recommending what we're recommending — not because I'll bury you in jargon, but because I'll explain the parts that matter and skip the parts that don't.",
           "Eine Hypothek ist eine der größten finanziellen Entscheidungen, die die meisten von uns je treffen, und ich finde, niemand sollte diese Entscheidung halbinformiert treffen. Deshalb setzt mein Ansatz stark auf Aufklärung. Wenn wir zusammenarbeiten, werden Sie Ihre Optionen verstehen, die Abwägungen und <em>warum</em> wir empfehlen, was wir empfehlen — nicht weil ich Sie mit Fachjargon überschütte, sondern weil ich Ihnen das Wesentliche erkläre und den Rest weglasse.",
           "La hipoteca es una de las decisiones financieras más importantes que la mayoría tomamos en la vida, y no creo que nadie deba entrar en esa decisión con información a medias. Por eso mi enfoque se apoya mucho en la educación. Cuando trabajamos juntos, entenderá sus opciones, los compromisos, y <em>por qué</em> recomendamos lo que recomendamos — no porque le abrume con jerga, sino porque le explicaré lo que importa y omitiré lo que no.",
           "A jelzáloghitel egyike a legnagyobb pénzügyi döntéseknek, amelyeket életünk során hozunk, és úgy gondolom, senkinek sem szabadna félig informáltan belevágnia. Ezért a megközelítésem nagyrészt az oktatásra épít. Amikor együtt dolgozunk, meg fogja érteni a lehetőségeit, a kompromisszumokat, és azt is, hogy <em>miért</em> pont azt ajánljuk, amit ajánlunk — nem azért, mert szakzsargonnal árasztom el, hanem mert elmagyarázom, ami valóban számít, és kihagyom, ami nem.")}
        {t("p", "As a whole-of-market broker, I'm not tied to any single lender. I have access to over 100 lenders — high street banks, specialist providers, and private options — which means I can match a mortgage to your circumstances rather than squeeze you into someone else's box. Whether you're buying your first home, remortgaging, expanding a portfolio, or arranging something more complex, we start with your situation and work outwards from there.",
           "Als Whole-of-Market-Maklerin bin ich an keinen einzelnen Kreditgeber gebunden. Ich habe Zugang zu über 100 Kreditgebern — Großbanken, Spezialanbietern und Privatbanken — was bedeutet, dass ich eine Hypothek an Ihre Situation anpassen kann, statt Sie in eine fremde Schablone zu zwingen. Ob Sie Ihr erstes Zuhause kaufen, umschulden, ein Portfolio ausbauen oder etwas Komplexeres arrangieren — wir beginnen bei Ihrer Situation und arbeiten von dort aus weiter.",
           "Como bróker de mercado completo, no estoy ligada a un único prestamista. Tengo acceso a más de 100 prestamistas — grandes bancos, proveedores especializados y opciones privadas — lo que significa que puedo ajustar la hipoteca a sus circunstancias, en lugar de encajarle en el molde de otro. Ya sea que esté comprando su primera vivienda, refinanciando, ampliando una cartera o gestionando algo más complejo, empezamos por su situación y construimos desde ahí.",
           "Teljes piaci brókerként nem vagyok egyetlen hitelezőhöz kötve. Több mint 100 hitelezőhöz van hozzáférésem — nagybankokhoz, speciális szolgáltatókhoz és privát megoldásokhoz — ami azt jelenti, hogy a jelzáloghitelt az Ön körülményeihez igazítom, nem pedig Önt egy előre gyártott dobozba szorítom. Legyen szó első otthon vásárlásáról, refinanszírozásról, portfólió bővítéséről vagy valami összetettebbről, mindig az Ön helyzetéből indulunk ki, és onnan építkezünk.")}
        {t("p", "I also feel strongly about protection. A mortgage keeps a roof over your head; protection keeps that roof there if life takes an unexpected turn — critical illness, long-term illness, loss of income, or worse. It's not the glamorous part of the conversation, but it's often the most important one.",
           "Auch beim Thema Absicherung habe ich klare Überzeugungen. Eine Hypothek gibt Ihnen ein Dach über dem Kopf; eine Absicherung sorgt dafür, dass es dort bleibt, falls das Leben eine unerwartete Wendung nimmt — schwere Krankheit, langfristige Erkrankung, Einkommensverlust oder Schlimmeres. Es ist nicht der glamouröse Teil des Gesprächs, aber oft der wichtigste.",
           "También creo firmemente en la protección. Una hipoteca le pone un techo sobre la cabeza; la protección se asegura de que ese techo siga ahí si la vida da un giro inesperado — enfermedad grave, enfermedad prolongada, pérdida de ingresos o algo peor. No es la parte glamurosa de la conversación, pero suele ser la más importante.",
           "A biztosítás kérdése is fontos számomra. A jelzáloghitel tetőt biztosít a feje fölé; a biztosítás pedig azt biztosítja, hogy az a tető ott is maradjon, ha az élet váratlan fordulatot vesz — súlyos betegség, hosszú távú megbetegedés, jövedelemkiesés vagy még rosszabb esetén. Nem ez a beszélgetés csillogó része, de gyakran ez a legfontosabb.")}
        {t("p", "My goal is simple: keep the process smooth, keep you informed at every step, and make sure you walk away with the right mortgage <em>and</em> the right cover for real peace of mind.",
           "Mein Ziel ist einfach: den Prozess reibungslos halten, Sie in jedem Schritt informieren und dafür sorgen, dass Sie am Ende mit der richtigen Hypothek <em>und</em> der richtigen Absicherung nach Hause gehen — für echte Sicherheit.",
           "Mi objetivo es sencillo: mantener el proceso fluido, mantenerle informado en cada paso, y asegurarme de que se marche con la hipoteca adecuada <em>y</em> la cobertura adecuada, para una verdadera tranquilidad.",
           "A célom egyszerű: a folyamat legyen zökkenőmentes, Ön minden lépésnél tájékozott, és a végén valóban a megfelelő jelzáloghitellel <em>és</em> a megfelelő biztosítással távozzon — valódi lelki nyugalommal.")}
        <div class="badge-row">
          <span class="badge">{ICON['shield']} CeMAP 3</span>
          <span class="badge">{ICON['shield']} FCA 750470</span>
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
        {t("p", "Over 100 lenders, from global banks to private banks and specialist funds. The recommendation is driven by your case — never by a panel.",
           "Über 100 Kreditgeber — von Großbanken über Privatbanken bis zu Spezialfonds. Die Empfehlung folgt Ihrem Fall, nie einer Vorauswahl.",
           "Más de 100 prestamistas, desde grandes bancos hasta banca privada y fondos especializados. La recomendación la dicta su caso, nunca un panel.",
           "Több mint 100 hitelező — a nagybankoktól a privátbankokon át a speciális alapokig. Az ajánlást az Ön ügye vezérli, sosem egy előre szűkített lista.")}</div>
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
<p>Agnes Mortgage is a trading name of Milla Mortgages Ltd, registered in England and Wales (company number 08461134), registered office 420a Streatham High Road, London, SW16 3SN. We are the data controller for personal data collected through this website. Contact: [DATA CONTACT EMAIL / POSTAL ADDRESS].</p>
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
<p>Agnes Mortgage is a trading name of Milla Mortgages Ltd, authorised and regulated by the Financial Conduct Authority (FCA number 750470). You can verify our status on the Financial Services Register at register.fca.org.uk. The FCA does not regulate most buy-to-let mortgages, commercial lending or tax advice.</p>
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
                "Plain-spoken guides on buy-to-let structuring, expat lending, HMO finance and remortgage timing — from a whole-of-market UK broker.",
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
        <h2>Talk this through with a broker</h2>
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
# CALCULATORS
# =====================================================================
def build_calculators():
    bc_json, crumb = breadcrumb("Calculators", "Rechner", "Calculadoras", "Kalkulátorok", "calculators")
    html = head(
        "UK Mortgage Calculators — Repayment, Borrowing, Stamp Duty, Buy-to-Let | Agnes Mortgage",
        "Free UK mortgage tools: monthly repayment calculator, how much can I borrow, stamp duty (SDLT) calculator and buy-to-let rental cover — instant results.",
        "calculators", jsonld=bc_json)
    html += lang_gate() + header("calculators")

    def seg(id_, options):
        btns = "".join(
            f'<button type="button" data-val="{v}"{" class=\"active\"" if i==0 else ""} data-en="{esc(en)}" data-de="{esc(de)}" data-es="{esc(es)}" data-hu="{esc(hu)}">{en}</button>'
            for i,(v,en,de,es,hu) in enumerate(options))
        return f'<div class="calc-seg" id="{id_}">{btns}</div>'

    html += f"""<main>
<section class="page-hero">
  <div class="container">
    {crumb}
    {t("h1", "Mortgage calculators", "Hypothekenrechner", "Calculadoras hipotecarias", "Jelzálog-kalkulátorok")}
    {t("p", "Instant estimates as you type — repayments, borrowing power, stamp duty and buy-to-let cover. Figures are illustrations, not offers; your exact numbers depend on lender criteria.",
       "Sofortige Schätzungen während der Eingabe — Raten, Kreditrahmen, Grunderwerbsteuer und Buy-to-Let-Deckung. Die Zahlen sind Beispiele, keine Angebote.",
       "Estimaciones instantáneas mientras escribe — cuotas, capacidad de préstamo, impuesto de transmisiones y cobertura buy-to-let. Las cifras son ilustrativas, no ofertas.",
       "Azonnali becslések gépelés közben — törlesztő, hitelkeret, illeték és buy-to-let fedezettség. A számok tájékoztató jellegűek, nem ajánlatok.")}
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="calc-tabs reveal-item">
      <button class="calc-tab active" data-panel="repay" data-en="Monthly repayment" data-de="Monatliche Rate" data-es="Cuota mensual" data-hu="Havi törlesztő">Monthly repayment</button>
      <button class="calc-tab" data-panel="borrow" data-en="How much can I borrow?" data-de="Wie viel kann ich leihen?" data-es="¿Cuánto puedo pedir?" data-hu="Mennyit kaphatok?">How much can I borrow?</button>
      <button class="calc-tab" data-panel="sdlt" data-en="Stamp duty (SDLT)" data-de="Grunderwerbsteuer (SDLT)" data-es="Impuesto SDLT" data-hu="Illeték (SDLT)">Stamp duty (SDLT)</button>
      <button class="calc-tab" data-panel="btl" data-en="Buy-to-let cover" data-de="Buy-to-Let-Deckung" data-es="Cobertura buy-to-let" data-hu="Buy-to-let fedezet">Buy-to-let cover</button>
    </div>

    <!-- ============ REPAYMENT ============ -->
    <div class="calc-panel active" id="panel-repay">
      <div class="calc-grid">
        <div class="calc-inputs reveal-item">
          <div class="calc-field">
            <label>{t("span", "Loan amount", "Darlehensbetrag", "Importe del préstamo", "Hitelösszeg")}<output id="repay-amount-out">£250,000</output></label>
            <input type="range" id="repay-amount" min="25000" max="3000000" step="5000" value="250000">
          </div>
          <div class="calc-field">
            <label>{t("span", "Interest rate (% per year)", "Zinssatz (% pro Jahr)", "Tipo de interés (% anual)", "Kamatláb (% évente)")}<output id="repay-rate-out">4.5%</output></label>
            <input type="range" id="repay-rate" min="0.5" max="12" step="0.05" value="4.5">
          </div>
          <div class="calc-field">
            <label>{t("span", "Term (years)", "Laufzeit (Jahre)", "Plazo (años)", "Futamidő (év)")}<output id="repay-term-out">25</output></label>
            <input type="range" id="repay-term" min="5" max="40" step="1" value="25">
          </div>
          <div class="calc-field">
            <label>{t("span", "Repayment type", "Tilgungsart", "Tipo de amortización", "Törlesztés típusa")}</label>
            {seg("repay-type", [("repayment","Capital repayment","Annuität","Amortización","Tőke + kamat"),("io","Interest-only","Tilgungsfrei","Solo interés","Csak kamat")])}
          </div>
        </div>
        <div class="calc-result reveal-item">
          {t("h3", "Estimated monthly payment", "Geschätzte Monatsrate", "Cuota mensual estimada", "Becsült havi törlesztő")}
          <div class="calc-big" id="repay-big">£1,390</div>
          <div class="calc-rows">
            <div class="calc-row">{t("span", "Total repaid over term", "Gesamtrückzahlung", "Total devuelto", "Teljes visszafizetés")}<b id="repay-total">—</b></div>
            <div class="calc-row">{t("span", "Total interest", "Gesamtzinsen", "Interés total", "Teljes kamat")}<b id="repay-interest">—</b></div>
          </div>
          <p class="calc-note" data-en="Illustration only. Assumes a constant rate for the whole term." data-de="Nur zur Veranschaulichung. Konstanter Zinssatz über die gesamte Laufzeit angenommen." data-es="Solo ilustrativo. Supone un tipo constante durante todo el plazo." data-hu="Csak illusztráció. A teljes futamidőre változatlan kamatot feltételez.">Illustration only. Assumes a constant rate for the whole term.</p>
          <div class="calc-cta"><a href="/#contact" class="btn btn-gold btn-sm">{t("span", "Get exact figures", "Genaue Zahlen anfragen", "Obtener cifras exactas", "Pontos számokat kérek")} {ICON['arrow']}</a></div>
        </div>
      </div>
    </div>

    <!-- ============ BORROWING ============ -->
    <div class="calc-panel" id="panel-borrow">
      <div class="calc-grid">
        <div class="calc-inputs reveal-item">
          <div class="calc-field">
            <label>{t("span", "Your annual income (before tax)", "Ihr Jahreseinkommen (brutto)", "Sus ingresos anuales (brutos)", "Éves jövedelme (bruttó)")}<output id="borrow-inc1-out">£60,000</output></label>
            <input type="range" id="borrow-inc1" min="10000" max="500000" step="1000" value="60000">
          </div>
          <div class="calc-field">
            <label>{t("span", "Second applicant income (optional)", "Einkommen zweite Person (optional)", "Ingresos del segundo titular (opcional)", "Második igénylő jövedelme (opcionális)")}<output id="borrow-inc2-out">£0</output></label>
            <input type="range" id="borrow-inc2" min="0" max="500000" step="1000" value="0">
          </div>
        </div>
        <div class="calc-result reveal-item">
          {t("h3", "Estimated borrowing range", "Geschätzter Kreditrahmen", "Rango de préstamo estimado", "Becsült hitelkeret")}
          <div class="calc-big" id="borrow-big">£240,000 – £330,000</div>
          <div class="calc-rows">
            <div class="calc-row">{t("span", "Typical (4.5× income)", "Typisch (4,5× Einkommen)", "Típico (4,5× ingresos)", "Jellemző (4,5× jövedelem)")}<b id="borrow-typ">—</b></div>
            <div class="calc-row">{t("span", "Some lenders (up to 5.5×)", "Einige Banken (bis 5,5×)", "Algunos bancos (hasta 5,5×)", "Egyes bankok (akár 5,5×)")}<b id="borrow-max">—</b></div>
          </div>
          <p class="calc-note" data-en="Actual figures depend on outgoings, credit profile and lender criteria — complex income often supports more than the standard multiple." data-de="Tatsächliche Werte hängen von Ausgaben, Bonität und Bankkriterien ab — komplexes Einkommen ermöglicht oft mehr als das Standardvielfache." data-es="Las cifras reales dependen de gastos, perfil crediticio y criterios del banco — los ingresos complejos a menudo permiten más que el múltiplo estándar." data-hu="A tényleges összeg a kiadásoktól, hitelprofiltól és banki feltételektől függ — összetett jövedelem gyakran többet tesz lehetővé a szokásos szorzónál.">Actual figures depend on outgoings, credit profile and lender criteria — complex income often supports more than the standard multiple.</p>
          <div class="calc-cta"><a href="/#contact" class="btn btn-gold btn-sm">{t("span", "Check my real maximum", "Mein echtes Maximum prüfen", "Comprobar mi máximo real", "Valós maximumom ellenőrzése")} {ICON['arrow']}</a></div>
        </div>
      </div>
    </div>

    <!-- ============ SDLT ============ -->
    <div class="calc-panel" id="panel-sdlt">
      <div class="calc-grid">
        <div class="calc-inputs reveal-item">
          <div class="calc-field">
            <label>{t("span", "Purchase price", "Kaufpreis", "Precio de compra", "Vételár")}<output id="sdlt-price-out">£350,000</output></label>
            <input type="range" id="sdlt-price" min="50000" max="3000000" step="5000" value="350000">
          </div>
          <div class="calc-field">
            <label>{t("span", "Buyer type", "Käufertyp", "Tipo de comprador", "Vásárló típusa")}</label>
            {seg("sdlt-type", [("mover","Home mover","Umzügler","Comprador estándar","Költöző"),("ftb","First-time buyer","Erstkäufer","Primer comprador","Első vásárló"),("additional","Additional property","Zusatzimmobilie","Propiedad adicional","További ingatlan")])}
          </div>
        </div>
        <div class="calc-result reveal-item">
          {t("h3", "Stamp duty payable", "Zu zahlende Steuer", "Impuesto a pagar", "Fizetendő illeték")}
          <div class="calc-big" id="sdlt-big">£7,500</div>
          <div class="calc-rows" id="sdlt-bands"></div>
          <p class="calc-note" data-en="England &amp; Northern Ireland rates from April 2025. Additional-property surcharge +5%. Scotland (LBTT) and Wales (LTT) differ." data-de="Sätze für England &amp; Nordirland ab April 2025. Zuschlag für Zusatzimmobilien +5%. Schottland (LBTT) und Wales (LTT) weichen ab." data-es="Tarifas de Inglaterra e Irlanda del Norte desde abril de 2025. Recargo por propiedad adicional +5%. Escocia (LBTT) y Gales (LTT) difieren." data-hu="Anglia és Észak-Írország 2025. áprilisi kulcsai. További ingatlan felára +5%. Skócia (LBTT) és Wales (LTT) eltér.">England &amp; Northern Ireland rates from April 2025. Additional-property surcharge +5%. Scotland (LBTT) and Wales (LTT) differ.</p>
          <div class="calc-cta"><a href="/#contact" class="btn btn-gold btn-sm">{t("span", "Plan the full purchase cost", "Gesamtkosten planen", "Planificar el coste total", "Teljes költség tervezése")} {ICON['arrow']}</a></div>
        </div>
      </div>
    </div>

    <!-- ============ BTL ============ -->
    <div class="calc-panel" id="panel-btl">
      <div class="calc-grid">
        <div class="calc-inputs reveal-item">
          <div class="calc-field">
            <label>{t("span", "Property value", "Immobilienwert", "Valor de la propiedad", "Ingatlan értéke")}<output id="btl-value-out">£250,000</output></label>
            <input type="range" id="btl-value" min="50000" max="3000000" step="5000" value="250000">
          </div>
          <div class="calc-field">
            <label>{t("span", "Expected monthly rent", "Erwartete Monatsmiete", "Alquiler mensual previsto", "Várható havi bérleti díj")}<output id="btl-rent-out">£1,200</output></label>
            <input type="range" id="btl-rent" min="300" max="10000" step="50" value="1200">
          </div>
          <div class="calc-field">
            <label>{t("span", "Taxpayer type", "Steuerstatus", "Tipo de contribuyente", "Adózási státusz")}</label>
            {seg("btl-tax", [("basic","Basic rate","Basissteuersatz","Tipo básico","Alapkulcs"),("higher","Higher rate","Spitzensteuersatz","Tipo alto","Magasabb kulcs"),("ltd","Ltd / SPV","GmbH / SPV","Ltd / SPV","Kft. / SPV")])}
          </div>
        </div>
        <div class="calc-result reveal-item">
          {t("h3", "Buy-to-let assessment", "Buy-to-Let-Bewertung", "Evaluación buy-to-let", "Buy-to-let értékelés")}
          <div class="calc-big" id="btl-big">—</div>
          <div class="calc-rows">
            <div class="calc-row">{t("span", "Mortgage at 75% LTV", "Hypothek bei 75% LTV", "Hipoteca al 75% LTV", "Jelzáloghitel 75% LTV-nél")}<b id="btl-loan">—</b></div>
            <div class="calc-row">{t("span", "Deposit required (25%)", "Eigenkapital (25%)", "Entrada necesaria (25%)", "Szükséges önerő (25%)")}<b id="btl-deposit">—</b></div>
            <div class="calc-row">{t("span", "Monthly mortgage at stress rate", "Monatsrate bei Stresstest", "Cuota mensual al tipo de estrés", "Havi törlesztő stresszkamat mellett")}<b id="btl-monthly">—</b></div>
            <div class="calc-row">{t("span", "Rent needed to pass ICR", "Erforderliche Miete für ICR", "Alquiler necesario para ICR", "Szükséges bérleti díj az ICR-hez")}<b id="btl-needed">—</b></div>
          </div>
          <p class="calc-note" data-en="Based on 75% LTV, 5.5% stress rate. ICR: 125% for basic-rate and Ltd/SPV, 145% for higher-rate taxpayers. Actual criteria vary by lender." data-de="Basierend auf 75% LTV, 5,5% Stresszins. ICR: 125% für Basissteuersatz und GmbH/SPV, 145% für Spitzensteuersatz. Kriterien variieren je nach Bank." data-es="Basado en 75% LTV, 5,5% tipo de estrés. ICR: 125% para tipo básico y Ltd/SPV, 145% para tipo alto. Los criterios varían según el banco." data-hu="75% LTV, 5,5% stresszkamat alapján. ICR: 125% alapkulcs és Kft./SPV esetén, 145% magasabb kulcsnál. A tényleges feltételek bankonként eltérnek.">Based on 75% LTV, 5.5% stress rate. ICR: 125% for basic-rate and Ltd/SPV, 145% for higher-rate taxpayers. Actual criteria vary by lender.</p>
          <div class="calc-cta"><a href="/#contact" class="btn btn-gold btn-sm">{t("span", "Model my portfolio", "Mein Portfolio modellieren", "Modelar mi cartera", "Portfólióm modellezése")} {ICON['arrow']}</a></div>
        </div>
      </div>
    </div>

  </div>
</section>

{cta_band("Numbers are the start, not the answer", "Zahlen sind der Anfang, nicht die Antwort", "Los números son el inicio, no la respuesta", "A számok a kezdet, nem a válasz",
          "A calculator cannot see lender criteria, your income structure or next year's plans. A twenty-minute conversation can.",
          "Ein Rechner kennt weder Bankkriterien noch Ihre Einkommensstruktur oder Ihre Pläne. Ein zwanzigminütiges Gespräch schon.",
          "Una calculadora no ve los criterios del banco, su estructura de ingresos ni sus planes. Una conversación de veinte minutos, sí.",
          "Egy kalkulátor nem látja a banki feltételeket, a jövedelmi szerkezetét és a jövő évi terveit. Egy húszperces beszélgetés igen.")}
</main>
<script src="/js/calculators.js" defer></script>
"""
    html += footer()
    open("calculators.html", "w").write(html)

# =====================================================================
# RUN
# =====================================================================
if __name__ == "__main__":
    import os
    os.makedirs("blog/posts/images", exist_ok=True)
    P.build_index()
    P.build_all_services()
    P.build_contractors()
    P.build_residential()
    P.build_remaining_services()
    build_about()
    legal_page("privacy-policy", "Privacy Policy | Agnes Mortgage",
               "How Agnes Mortgage collects, uses and protects personal data under UK GDPR.",
               "Privacy Policy", PRIVACY_BODY)
    legal_page("terms", "Terms of Business | Agnes Mortgage",
               "Terms of business for Agnes Mortgage: regulation, fees, complaints and FSCS coverage.",
               "Terms of Business", TERMS_BODY)
    build_calculators()
    build_404()
    build_blog_index()
    for p in POSTS:
        build_post(p)
    build_post(POSTS[0], template=True)
    print("ALL PAGES BUILT")
