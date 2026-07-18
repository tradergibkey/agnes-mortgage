# -*- coding: utf-8 -*-
"""Agnes Mortgage — page builder. Run: python3 _gen_pages.py"""
from _gen_common import *

def check(en, de, es, hu):
    return f'<li>{ICON["check"]}{t("span", en, de, es, hu)}</li>'

def faq_item(q, a):
    return f"""<div class="faq-item">
  <button class="faq-q" type="button">{t("span", *q)}{ICON['plus']}</button>
  <div class="faq-a">{t("p", *a)}</div>
</div>"""

def faq_jsonld(pairs):
    import json
    items = [{"@type": "Question", "name": q[0],
              "acceptedAnswer": {"@type": "Answer", "text": a[0]}} for q, a in pairs]
    return '<script type="application/ld+json">' + json.dumps(
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": items},
        ensure_ascii=False) + "</script>"

def service_jsonld(name, desc, slug):
    return f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Service","name":"{name}","description":"{desc}",
"url":"{BASE}/{slug}","areaServed":{{"@type":"Country","name":"United Kingdom"}},
"provider":{{"@type":"FinancialService","name":"Agnes Mortgage","url":"{BASE}"}}}}
</script>"""

# =====================================================================
# INDEX
# =====================================================================
def build_index():
    jsonld = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FinancialService","name":"Agnes Mortgage",
"description":"Private mortgage broker for business owners, portfolio landlords, high-net-worth clients and expats across the United Kingdom.",
"url":"{BASE}","image":"{BASE}/img/og-cover.jpg","telephone":"{PHONE_DISP}",
"areaServed":{{"@type":"Country","name":"United Kingdom"}},
"knowsAbout":["Buy-to-let mortgages","Limited company buy-to-let","HMO finance","Expat mortgages","Self-employed mortgages","High-net-worth mortgages","Remortgaging"],
"priceRange":"££"}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"WebSite","name":"Agnes Mortgage","url":"{BASE}"}}
</script>"""

    cards = [
        ("residential", "svc-residential.jpg",
         ("Residential Mortgages", "Wohnimmobilien-Hypotheken", "Hipotecas residenciales", "Lakóingatlan-jelzáloghitelek"),
         ("Your home is not a standard transaction. Complex income, unusual properties and tight timelines need a broker who knows which lender fits — not a comparison website.",
          "Ihr Zuhause ist keine Standardtransaktion. Komplexes Einkommen, ungewöhnliche Immobilien und enge Fristen brauchen einen Makler, der den richtigen Kreditgeber kennt.",
          "Su hogar no es una transacción estándar. Ingresos complejos, propiedades inusuales y plazos ajustados necesitan un bróker que sepa qué banco encaja.",
          "Az otthona nem egy szokványos ügylet. Összetett jövedelem, szokatlan ingatlanok és szoros határidők — ehhez kell egy bróker, aki tudja, melyik bank illik Önhöz.")),
        ("remortgage", "svc-remortgage.jpg",
         ("Remortgage & Refinance", "Umschuldung & Refinanzierung", "Rehipoteca y refinanciación", "Hitelkiváltás és refinanszírozás"),
         ("Fixed rate ending? Capital to raise? We track your deals and move you at the right moment — never a day on the standard variable rate.",
          "Zinsbindung läuft aus? Kapitalbedarf? Wir überwachen Ihre Konditionen und handeln zum richtigen Zeitpunkt — kein Tag im teuren Standardzins.",
          "¿Termina su tipo fijo? ¿Necesita capital? Seguimos sus condiciones y actuamos en el momento justo — ni un día en el tipo variable estándar.",
          "Lejár a fix kamat? Tőkét vonna ki? Figyeljük a konstrukcióit és a megfelelő pillanatban lépünk — egy napot sem tölt a drága változó kamaton.")),
        ("buy-to-let", "svc-buy-to-let.jpg",
         ("Buy to Let", "Buy-to-Let", "Buy-to-Let", "Buy-to-let"),
         ("From your first investment property to a structured limited-company portfolio — lending built around your growth plan, not a single transaction.",
          "Von der ersten Anlageimmobilie bis zum strukturierten GmbH-Portfolio — Finanzierung nach Ihrem Wachstumsplan, nicht nur für eine Transaktion.",
          "Desde su primera propiedad de inversión hasta una cartera estructurada en sociedad — financiación diseñada para su plan de crecimiento.",
          "Az első befektetési ingatlantól a strukturált céges portfólióig — a növekedési tervéhez igazított finanszírozás.")),
        ("hmo-finance", "svc-hmo.jpg",
         ("HMO & Multi-Unit Block Finance", "HMO & Mehrfamilienblock-Finanzierung", "HMO y financiación de bloques", "HMO és többlakásos tömb finanszírozás"),
         ("Specialist lending for houses in multiple occupation, multi-unit freehold blocks and mixed-use assets — where the high street won't go.",
          "Spezialfinanzierung für HMOs, Mehrfamilienblöcke und Mischobjekte — dort, wo klassische Banken nicht hingehen.",
          "Financiación especializada para HMO, bloques de varias unidades y activos de uso mixto — donde la banca tradicional no llega.",
          "Speciális hitelezés HMO-kra, többlakásos épületekre és vegyes hasznosítású ingatlanokra — ahová a nagybankok nem mennek.")),
        ("self-employed", "svc-self-employed.jpg",
         ("Directors & Self-Employed", "Unternehmer & Selbständige", "Directores y autónomos", "Cégvezetők és vállalkozók"),
         ("Retained profits, dividends, day rates, one year of accounts — we present your income the way specialist underwriters need to see it.",
          "Einbehaltene Gewinne, Dividenden, Tagessätze, ein Jahresabschluss — wir präsentieren Ihr Einkommen so, wie Underwriter es sehen müssen.",
          "Beneficios retenidos, dividendos, tarifas diarias, un año de cuentas — presentamos sus ingresos como los analistas necesitan verlos.",
          "Visszatartott nyereség, osztalék, napidíj, egyéves beszámoló — úgy mutatjuk be a jövedelmét, ahogy a hitelbírálók látni akarják.")),
        ("contractors", "svc-self-employed.jpg",
         ("Contractor Mortgages", "Auftragnehmer-Hypotheken", "Hipotecas para contratistas", "Szerződéses jelzáloghitelek"),
         ("Day rate, umbrella company or limited company — lenders assess contractor income differently, and the right route can double what you qualify for.",
          "Tagessatz, Umbrella oder eigene GmbH — Banken bewerten Auftragnehmer-Einkommen unterschiedlich, und der richtige Weg kann die Darlehenssumme verdoppeln.",
          "Tarifa diaria, umbrella o sociedad limitada — los bancos evalúan los ingresos de contratistas de forma diferente, y la vía correcta puede duplicar su capacidad.",
          "Napidíj, ernyőcégen vagy saját Kft.-n keresztül — a bankok eltérően értékelik a szerződéses jövedelmet, és a helyes út megduplázhatja a hitelkeretét.")),
        ("expat-mortgages", "svc-expat.jpg",
         ("Expat & Foreign National Mortgages", "Expat- & Ausländerfinanzierung", "Hipotecas para expatriados y extranjeros", "Jelzáloghitel külföldieknek és expatoknak"),
         ("UK property finance for British expats and foreign nationals — foreign income, foreign address, no UK credit footprint? We arrange it anyway.",
          "UK-Immobilienfinanzierung für britische Expats und ausländische Staatsbürger — ausländisches Einkommen und Adresse? Wir arrangieren es trotzdem.",
          "Financiación de propiedades en el Reino Unido para expatriados y extranjeros — ¿ingresos y domicilio en el extranjero? Lo gestionamos igualmente.",
          "Brit ingatlanfinanszírozás külföldön élő briteknek és külföldi állampolgároknak — külföldi jövedelemmel és címmel is megoldjuk.")),
        ("high-net-worth", "svc-hnw.jpg",
         ("High-Net-Worth & Large Loans", "Vermögende Kunden & Großdarlehen", "Grandes patrimonios", "Nagy vagyon és nagy hitelek"),
         ("Discreet, bespoke finance for complex wealth — private banks, interest-only structures, multi-currency income and lending well beyond £1m.",
          "Diskrete, maßgeschneiderte Finanzierung für komplexe Vermögen — Privatbanken, endfällige Strukturen und Darlehen weit über £1 Mio.",
          "Financiación discreta y a medida para patrimonios complejos — banca privada, estructuras de solo interés y préstamos muy por encima de £1M.",
          "Diszkrét, egyedi finanszírozás összetett vagyonokra — privátbankok, csak-kamat konstrukciók és £1M feletti hitelek.")),
    ]
    cards_html = "\n".join(f"""      <article class="card reveal-item">
        <a href="/{slug}" class="card-img"><img src="/img/{img}" alt="{names[0]} — Agnes Mortgage" loading="lazy"></a>
        <div class="card-body">
          {t("h3", *names)}
          {t("p", *descs)}
          <a href="/{slug}" class="card-link">{t("span", "Explore this service", "Mehr erfahren", "Ver este servicio", "Részletek")} {ICON['arrow']}</a>
        </div>
      </article>""" for slug, img, names, descs in cards)

    html = head(
        "Private Mortgage Broker UK — Landlords & Expats | Agnes Mortgage",
        "Whole-of-market UK mortgage broker for portfolio landlords, HMO investors, company directors and expats. Advice in English, German, Spanish and Hungarian.",
        "", jsonld=jsonld)
    html += lang_gate() + header("home")

    html += f"""<main>
<section class="hero">
  <div class="hero-media">
    <video autoplay muted loop playsinline poster="/img/hero-fallback.jpg">
      <source src="/img/hero-video.mp4" type="video/mp4">
    </video>
    <img src="/img/hero-fallback.jpg" alt="" aria-hidden="true" style="position:absolute;inset:0;z-index:-1">
  </div>
  <div class="hero-veil"></div>
  <div class="hero-inner">
    <div class="hero-content">
      {t("span", "Private mortgage broker · United Kingdom", "Privater Hypothekenmakler · Vereinigtes Königreich", "Bróker hipotecario privado · Reino Unido", "Privát jelzálogbróker · Egyesült Királyság", cls="eyebrow")}
      <h1><span data-en="Mortgage advice for those" data-de="Hypothekenberatung für alle," data-es="Asesoría hipotecaria para quienes" data-hu="Jelzálog-tanácsadás azoknak,">Mortgage advice for those</span> <span class="accent-text" data-en="the high street wasn't built for" data-de="für die Standardbanken nicht gemacht sind" data-es="no encajan en la banca tradicional" data-hu="akikre a nagybankok nem készültek">the high street wasn't built for</span></h1>
      {t("p", "Portfolio landlords. Company directors. High-net-worth families. Expats buying from abroad. Complex income is our everyday — we structure it, present it and place it with the right lender across the whole UK market.",
         "Portfolio-Vermieter. Geschäftsführer. Vermögende Familien. Expats, die aus dem Ausland kaufen. Komplexes Einkommen ist unser Alltag — wir strukturieren, präsentieren und platzieren es beim richtigen Kreditgeber im gesamten britischen Markt.",
         "Propietarios de carteras. Directores de empresa. Familias con grandes patrimonios. Expatriados que compran desde el extranjero. Los ingresos complejos son nuestro día a día — los estructuramos y colocamos con el prestamista adecuado en todo el mercado británico.",
         "Portfólióval rendelkező bérbeadók. Cégvezetők. Nagy vagyonú családok. Külföldről vásárló expatok. Az összetett jövedelem a mindennapjaink — strukturáljuk, bemutatjuk és a megfelelő hitelezőnél helyezzük el a teljes brit piacon.")}
      <div class="hero-actions">
        <a href="/#contact" class="btn btn-gold">{t("span", "Request a consultation", "Beratung anfragen", "Solicitar consulta", "Konzultáció kérése")} {ICON['arrow']}</a>
        <a href="/about" class="btn btn-ghost">{t("span", "Meet your broker", "Ihren Makler", "Conozca a su bróker", "Ismerje meg brókerét")}</a>
      </div>
      <div class="hero-stats">
        <div class="hero-stat"><b>100+</b>{t("span", "lenders across the market", "Kreditgeber am Markt", "prestamistas en el mercado", "hitelező a piacon")}</div>
        <div class="hero-stat"><b>4</b>{t("span", "languages of advice", "Beratungssprachen", "idiomas de asesoría", "nyelven elérhető tanácsadás")}</div>
        <div class="hero-stat"><b>UK</b>{t("span", "nationwide coverage", "landesweite Abdeckung", "cobertura nacional", "országos lefedettség")}</div>
      </div>
    </div>
  </div>
</section>

<div class="trustbar">
  <div class="container">
    <span>{ICON['shield']}{t("b", "Whole-of-market access", "Zugang zum Gesamtmarkt", "Acceso a todo el mercado", "Teljes piaci hozzáférés")}</span>
    <span>{ICON['shield']}{t("b", "FCA-regulated advice", "FCA-regulierte Beratung", "Asesoría regulada por la FCA", "FCA által felügyelt tanácsadás")}</span>
    <span>{ICON['shield']}{t("b", "Discreet & confidential", "Diskret & vertraulich", "Discreto y confidencial", "Diszkrét és bizalmas")}</span>
  </div>
</div>

<section class="section" id="services">
  <div class="container">
    <div class="section-head reveal-item">
      {t("span", "What we arrange", "Unsere Leistungen", "Qué gestionamos", "Amivel foglalkozunk", cls="eyebrow")}
      {t("h2", "Eight specialisms. One standard: bespoke.", "Acht Spezialgebiete. Ein Standard: maßgeschneidert.", "Ocho especialidades. Un estándar: a medida.", "Nyolc szakterület. Egy mérce: az egyedi megoldás.")}
      {t("p", "We deliberately serve a narrow clientele so the depth of expertise stays exceptional in every case we take on.",
         "Wir betreuen bewusst eine ausgewählte Klientel, damit die Expertise in jedem Fall außergewöhnlich bleibt.",
         "Atendemos deliberadamente a una clientela selecta para que la profundidad de la experiencia sea excepcional en cada caso.",
         "Tudatosan szűk ügyfélkört szolgálunk ki, hogy a szakértelem minden egyes ügyben kivételes maradjon.")}
    </div>
    <div class="grid-3">
{cards_html}
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="container">
    <div class="split">
      <div class="split-img reveal-item"><img src="/img/about-placeholder.jpg" alt="Agnes — private mortgage broker (portrait coming soon)" loading="lazy"></div>
      <div class="split-body reveal-item">
        {t("span", "Your broker", "Ihren Makler", "Su bróker", "Az Ön brókere", cls="eyebrow")}
        {t("h2", "Advice with a name, not a call centre", "Beratung mit Namen — kein Callcenter", "Asesoría con nombre propio, no un call center", "Tanácsadás névvel — nem call center")}
        {t("p", "Agnes Mortgage is built on one principle: clients with complex finances deserve one senior broker who knows their whole picture — every company, every property, every plan — and stays with them for years, not one transaction.",
           "Agnes Mortgage basiert auf einem Prinzip: Kunden mit komplexen Finanzen verdienen einen erfahrenen Makler, der ihr gesamtes Bild kennt — jede Firma, jede Immobilie, jeden Plan — und über Jahre an ihrer Seite bleibt.",
           "Agnes Mortgage se basa en un principio: los clientes con finanzas complejas merecen un bróker sénior que conozca su panorama completo — cada empresa, cada propiedad, cada plan — y les acompañe durante años.",
           "Az Agnes Mortgage egyetlen elvre épül: az összetett pénzügyekkel rendelkező ügyfelek megérdemelnek egy vezető brókert, aki a teljes képet ismeri — minden céget, ingatlant és tervet —, és évekig mellettük marad.")}
        <ul class="check-list">
          {check("Fully qualified, FCA-regulated mortgage broker", "Voll qualifizierte, FCA-regulierter Hypothekenmakler", "Bróker hipotecario cualificado y regulado por la FCA", "Képzett, FCA által felügyelt jelzálogbróker")}
          {check("Advice in English, German, Spanish and Hungarian", "Beratung auf Englisch, Deutsch, Spanisch und Ungarisch", "Asesoría en inglés, alemán, español y húngaro", "Tanácsadás angolul, németül, spanyolul és magyarul")}
          {check("Direct line to your broker — including WhatsApp", "Direkter Draht zu Ihrem Makler — auch per WhatsApp", "Línea directa con su bróker — incluido WhatsApp", "Közvetlen kapcsolat a brókerrel — WhatsAppon is")}
        </ul>
        <div style="margin-top:22px"><a href="/about" class="btn btn-primary">{t("span", "Meet Agnes", "Über Agnes", "Conozca a Agnes", "Ismerje meg Agnest")} {ICON['arrow']}</a></div>
      </div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="container">
    <div class="section-head reveal-item">
      {t("span", "How it works", "So läuft es ab", "Cómo funciona", "Hogyan működik", cls="eyebrow")}
      {t("h2", "From first call to keys — in three moves", "Vom ersten Gespräch bis zum Schlüssel — in drei Schritten", "De la primera llamada a las llaves — en tres pasos", "Az első hívástól a kulcsokig — három lépésben")}
    </div>
    <div class="grid-3">
      <div class="step reveal-item"><div class="step-num">1</div>
        {t("h3", "Private consultation", "Vertrauliches Erstgespräch", "Consulta privada", "Privát konzultáció")}
        {t("p", "A confidential conversation about your income structure, assets and objectives — by phone, video or in person.",
           "Ein vertrauliches Gespräch über Ihre Einkommensstruktur, Vermögenswerte und Ziele — telefonisch, per Video oder persönlich.",
           "Una conversación confidencial sobre su estructura de ingresos, activos y objetivos — por teléfono, vídeo o en persona.",
           "Bizalmas beszélgetés a jövedelmi szerkezetéről, vagyonáról és céljairól — telefonon, videón vagy személyesen.")}</div>
      <div class="step reveal-item"><div class="step-num">2</div>
        {t("h3", "Strategy & sourcing", "Strategie & Auswahl", "Estrategia y búsqueda", "Stratégia és forrásválasztás")}
        {t("p", "We model the options across the whole market, structure the case for underwriting and recommend the strongest route.",
           "Wir modellieren die Optionen im Gesamtmarkt, strukturieren den Fall für das Underwriting und empfehlen den stärksten Weg.",
           "Modelamos las opciones en todo el mercado, estructuramos el caso para el análisis y recomendamos la mejor vía.",
           "A teljes piacon modellezzük a lehetőségeket, felépítjük az ügyet a hitelbírálathoz, és a legerősebb utat ajánljuk.")}</div>
      <div class="step reveal-item"><div class="step-num">3</div>
        {t("h3", "Managed to completion", "Begleitung bis zum Abschluss", "Gestión hasta el cierre", "Végigkísérjük a folyamatot")}
        {t("p", "We run the application and chase lender, valuer and solicitors — you get milestone updates, not paperwork.",
           "Wir führen den Antrag und koordinieren Bank, Gutachter und Anwälte — Sie erhalten Status-Updates statt Papierkram.",
           "Gestionamos la solicitud y coordinamos con el banco, el tasador y los abogados — usted recibe avances, no papeleo.",
           "Mi visszük az igénylést, és mi egyeztetünk a bankkal, értékbecslővel, ügyvédekkel — Ön csak a mérföldkövekről kap értesítést.")}</div>
    </div>
  </div>
</section>

{marquee()}

{cta_band("Serious about your next move?", "Bereit für Ihren nächsten Schritt?", "¿Va en serio con su próximo paso?", "Komolyan gondolja a következő lépést?",
          "Whether it's a twelfth buy-to-let or a first UK purchase from abroad, one conversation will tell you exactly what is possible.",
          "Ob zwölftes Buy-to-Let oder erster UK-Kauf aus dem Ausland — ein Gespräch zeigt Ihnen genau, was möglich ist.",
          "Ya sea su duodécima propiedad de alquiler o su primera compra en el Reino Unido desde el extranjero, una conversación le dirá exactamente qué es posible.",
          "Legyen szó a tizenkettedik bérbeadott ingatlanról vagy az első brit vásárlásról külföldről — egyetlen beszélgetés megmutatja, mi lehetséges.")}

{contact_section()}
</main>
"""
    html += footer()
    open("index.html", "w").write(html)

# =====================================================================
# SERVICE PAGE FACTORY
# =====================================================================
def build_service(slug, img, title, desc, names, hero_p, s1, s2, faqs, cta):
    """names=(en,de,es,hu); s1=((h2 4-tuple, p 4-tuple), checks-list); s2=(h2, p1, p2)."""
    s1_checks = s1[1]
    s1 = s1[0]
    bc_json, crumb = breadcrumb(*names, slug)
    jsonld = bc_json + faq_jsonld(faqs) + service_jsonld(names[0], desc, slug)
    html = head(title, desc, slug, og_img=f"/img/{img}", jsonld=jsonld)
    html += lang_gate() + header(slug)
    checks = "\n".join(check(*c) for c in s1_checks)
    faqs_html = "\n".join(faq_item(q, a) for q, a in faqs)
    html += f"""<main>
<section class="page-hero">
  <div class="container">
    {crumb}
    {t("h1", *names)}
    {t("p", *hero_p)}
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split">
      <div class="split-img reveal-item"><img src="/img/{img}" alt="{names[0]} — Agnes Mortgage" loading="lazy"></div>
      <div class="split-body reveal-item">
        {t("h2", *s1[0])}
        {t("p", *s1[1])}
        <ul class="check-list">
{checks}
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="container">
    <div class="split">
      <div class="split-body reveal-item">
        {t("h2", *s2[0])}
        {t("p", *s2[1])}
        {t("p", *s2[2])}
        <div style="margin-top:20px"><a href="/#contact" class="btn btn-primary">{t("span", "Discuss your case", "Ihren Fall besprechen", "Consultar su caso", "Beszéljük meg az esetét")} {ICON['arrow']}</a></div>
      </div>
      <div class="split-img reveal-item"><img src="/img/hero-fallback.jpg" alt="Agnes Mortgage — UK private mortgage broker" loading="lazy"></div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="container" style="max-width:860px">
    <div class="section-head reveal-item">
      {t("span", "Common questions", "Häufige Fragen", "Preguntas frecuentes", "Gyakori kérdések", cls="eyebrow")}
      {t("h2", "Answered before you ask", "Beantwortet, bevor Sie fragen", "Respondidas antes de preguntar", "Válaszok, mielőtt kérdezné")}
    </div>
    <div class="reveal-item">
{faqs_html}
    </div>
  </div>
</section>

{cta_band(*cta)}
</main>
"""
    html += footer()
    open(f"{slug}.html", "w").write(html)

def build_all_services():
    build_service(
        "buy-to-let", "svc-buy-to-let.jpg",
        "Buy to Let Mortgages UK | Agnes Mortgage",
        "Buy-to-let and portfolio landlord mortgage advice across the UK — limited company BTL, portfolio restructuring, top-slicing and specialist lenders.",
        ("Buy to Let Mortgages", "Buy-to-Let-Hypotheken", "Hipotecas Buy-to-Let", "Buy-to-let jelzáloghitelek"),
        ("Four properties or forty — we finance portfolios as a strategy, not one mortgage at a time. Personal name or limited company, purchase or refinance, vanilla or complex.",
         "Vier Immobilien oder vierzig — wir finanzieren Portfolios als Strategie, nicht Hypothek für Hypothek. Privat oder über eine Gesellschaft, Kauf oder Refinanzierung.",
         "Cuatro propiedades o cuarenta — financiamos carteras como estrategia, no hipoteca a hipoteca. A título personal o en sociedad, compra o refinanciación.",
         "Négy ingatlan vagy negyven — a portfóliót stratégiaként finanszírozzuk, nem hitelenkénti alapon. Magánszemélyként vagy cégen keresztül, vásárlásra vagy kiváltásra."),
        ((("Built for the professional landlord", "Für den professionellen Vermieter", "Pensado para el arrendador profesional", "A profi bérbeadóra szabva"),
          ("Lenders now assess portfolio landlords on the whole book: aggregate LTV, rental cover across every property, and business plans. We prepare that picture professionally, so underwriters say yes faster and on better terms.",
           "Kreditgeber bewerten Portfolio-Vermieter heute im Gesamtbild: Gesamt-LTV, Mietdeckung über alle Objekte, Businessplan. Wir bereiten dieses Bild professionell auf — für schnellere und bessere Zusagen.",
           "Los prestamistas evalúan hoy al arrendador por su cartera completa: LTV agregado, cobertura de alquiler y plan de negocio. Preparamos ese expediente profesionalmente para lograr aprobaciones más rápidas y mejores condiciones.",
           "A hitelezők ma a teljes portfóliót nézik: összesített hitelfedezet, bérleti fedezettség minden ingatlanon, üzleti terv. Ezt a képet mi készítjük elő profin — gyorsabb és jobb feltételű jóváhagyásért.")),
         [("Limited company (SPV) buy-to-let, including transfers from personal name", "GmbH-/SPV-Strukturen, auch Übertragung aus Privatbesitz", "Buy-to-let en sociedad (SPV), incluidas transferencias desde nombre propio", "Céges (SPV) buy-to-let, magánnévről történő átvezetéssel is"),
          ("Portfolio remortgages coordinated across multiple properties and lenders", "Portfolio-Umschuldungen über mehrere Objekte und Banken koordiniert", "Rehipotecas de cartera coordinadas entre varias propiedades y bancos", "Portfóliószintű hitelkiváltás több ingatlan és bank között összehangolva"),
          ("Top-slicing where rental income alone doesn't stack", "Top-Slicing, wenn die Miete allein nicht ausreicht", "Top-slicing cuando el alquiler por sí solo no es suficiente", "Top-slicing, ha a bérleti díj önmagában nem elég"),
          ("Holiday lets, student lets and short-term letting models", "Ferienvermietung, Studentenwohnungen und Kurzzeitmodelle", "Alquiler vacacional, de estudiantes y de corta estancia", "Nyaralók, diáklakások és rövid távú kiadási modellek"),
          ("Capital raising against the existing portfolio for the next purchase", "Kapitalfreisetzung aus dem Bestand für den nächsten Kauf", "Liberación de capital de la cartera para la próxima compra", "Tőkekivonás a meglévő portfólióból a következő vásárláshoz")]),
        ((("Personal name or limited company?", "Privat oder über eine Gesellschaft?", "¿A nombre propio o en sociedad?", "Magánszemélyként vagy céggel?"),
          ("It's the first question every serious landlord asks, and the honest answer is: it depends on your tax position, growth plans and exit horizon. We model both routes with real lender pricing — then you decide with your accountant on facts, not folklore.",
           "Das ist die erste Frage jedes ernsthaften Vermieters — und die ehrliche Antwort lautet: Es hängt von Steuerposition, Wachstumsplänen und Exit-Horizont ab. Wir modellieren beide Wege mit echten Konditionen, damit Sie mit Ihrem Steuerberater faktenbasiert entscheiden.",
           "Es la primera pregunta de todo arrendador serio, y la respuesta honesta es: depende de su situación fiscal, planes de crecimiento y horizonte de salida. Modelamos ambas vías con precios reales de los bancos para que decida con su asesor fiscal sobre hechos.",
           "Ez minden komoly bérbeadó első kérdése — és az őszinte válasz: az adóhelyzettől, a növekedési tervektől és a kiszállási horizonttól függ. Mindkét utat valós banki árazással modellezzük, hogy a könyvelőjével tények alapján dönthessen."),
          ("Rates for limited-company lending have narrowed dramatically against personal BTL, and the specialist market now competes hard for professional landlords. The gap that made incorporation 'not worth it' five years ago has largely closed.",
           "Die Konditionen für Gesellschaftsdarlehen haben sich gegenüber privaten BTL-Krediten stark angenähert, und der Spezialmarkt konkurriert intensiv um professionelle Vermieter. Die Lücke, die eine Firmengründung früher unattraktiv machte, ist weitgehend geschlossen.",
           "Los tipos para sociedades se han acercado mucho a los de BTL personal, y el mercado especializado compite con fuerza por el arrendador profesional. La brecha que hacía que constituir sociedad 'no valiera la pena' hace cinco años prácticamente ha desaparecido.",
           "A céges hitelek kamatai jelentősen közeledtek a magánszemélyes buy-to-let árazáshoz, és a speciális piac ma erősen versenyez a profi bérbeadókért. Az az árkülönbség, ami öt éve még a cégalapítás ellen szólt, mára nagyrészt eltűnt."))),
        [((("Can I move properties I own personally into a limited company?", "Kann ich private Immobilien in eine Gesellschaft übertragen?", "¿Puedo traspasar propiedades personales a una sociedad?", "Átvihetem a magánnéven lévő ingatlanjaimat cégbe?")),
          (("Yes — it's treated as a sale to the company, so stamp duty and potentially capital gains tax apply, and the company needs its own mortgage. For larger portfolios, incorporation relief may be available. We coordinate the finance side while your accountant confirms the tax treatment.",
            "Ja — es gilt als Verkauf an die Gesellschaft, daher fallen Grunderwerbsteuer und ggf. Kapitalertragsteuer an, und die Gesellschaft braucht eine eigene Hypothek. Wir koordinieren die Finanzierung, Ihr Steuerberater die steuerliche Seite.",
            "Sí — se trata como una venta a la sociedad, por lo que aplican el impuesto de transmisiones y potencialmente plusvalías, y la sociedad necesita su propia hipoteca. Coordinamos la financiación mientras su asesor fiscal confirma el tratamiento tributario.",
            "Igen — ez a cég felé történő eladásnak minősül, így illetéket és adott esetben árfolyamnyereség-adót kell fizetni, a cégnek pedig saját jelzáloghitel kell. A finanszírozási oldalt mi koordináljuk, az adózásit a könyvelője."))),
         ((("How many properties count as a 'portfolio landlord'?", "Ab wann gilt man als Portfolio-Vermieter?", "¿Cuántas propiedades definen a un 'arrendador de cartera'?", "Hány ingatlantól számít valaki portfóliós bérbeadónak?")),
          (("Four or more mortgaged buy-to-lets under UK rules. From that point lenders must review your entire portfolio on every application — which is exactly where professional preparation starts paying for itself.",
            "Ab vier finanzierten Buy-to-Let-Objekten nach britischen Regeln. Ab dann muss die Bank bei jedem Antrag das gesamte Portfolio prüfen — genau hier zahlt sich professionelle Vorbereitung aus.",
            "Cuatro o más propiedades hipotecadas según las normas británicas. A partir de ahí, el banco debe revisar toda su cartera en cada solicitud — justo donde la preparación profesional empieza a rentar.",
            "A brit szabályok szerint négy vagy több jelzáloggal terhelt kiadó ingatlantól. Ettől kezdve a bank minden igénylésnél a teljes portfóliót vizsgálja — pontosan itt térül meg a profi előkészítés."))),
         ((("What deposit do I need for a buy-to-let?", "Wie viel Eigenkapital brauche ich?", "¿Qué entrada necesito para un buy-to-let?", "Mekkora önerő kell egy buy-to-let hitelhez?")),
          (("Typically 25% of the purchase price, with the strongest pricing from 40% equity. The rental income must also cover the mortgage by a set margin — we calculate the exact figures for your property before you offer.",
            "In der Regel 25% des Kaufpreises; die besten Konditionen ab 40% Eigenkapital. Die Miete muss die Rate mit einer festen Marge decken — wir rechnen die genauen Zahlen vor Ihrem Angebot durch.",
            "Normalmente el 25% del precio de compra, con los mejores precios a partir del 40% de capital. El alquiler debe cubrir la cuota con un margen fijado — calculamos las cifras exactas antes de que haga su oferta.",
            "Jellemzően a vételár 25%-a, a legjobb árazás 40% önerőtől érhető el. A bérleti díjnak meghatározott ráhagyással fedeznie kell a törlesztőt — a pontos számokat még az ajánlattétel előtt kiszámoljuk.")))],
        ("Ready to scale the portfolio?", "Bereit, das Portfolio auszubauen?", "¿Listo para ampliar la cartera?", "Készen áll a portfólió bővítésére?",
         "Bring us the spreadsheet. We'll bring the lending strategy that makes the next three purchases possible.",
         "Bringen Sie die Zahlen mit. Wir bringen die Finanzierungsstrategie für die nächsten drei Käufe.",
         "Traiga su hoja de cálculo. Nosotros traemos la estrategia de financiación para sus próximas tres compras.",
         "Hozza a táblázatot. Mi hozzuk a finanszírozási stratégiát, amely lehetővé teszi a következő három vásárlást."))

    build_service(
        "hmo-finance", "svc-hmo.jpg",
        "HMO & Multi-Unit Block Finance UK | Agnes Mortgage",
        "Specialist HMO mortgage and multi-unit freehold block finance across the UK — licensed HMOs, large HMOs, MUFBs, valuations and refinancing.",
        ("HMO & Multi-Unit Block Finance", "HMO & Mehrfamilienblock-Finanzierung", "Financiación HMO y bloques multiunidad", "HMO és többlakásos tömb finanszírozás"),
        ("Houses in multiple occupation and multi-unit blocks yield more — and demand lenders who actually understand them. We work with the specialists daily.",
         "HMOs und Mehrfamilienblöcke bringen höhere Renditen — und verlangen Banken, die sie wirklich verstehen. Mit diesen Spezialisten arbeiten wir täglich.",
         "Los HMO y bloques multiunidad rinden más — y exigen bancos que realmente los entiendan. Trabajamos con esos especialistas a diario.",
         "A több bérlős házak és többlakásos épületek magasabb hozamot hoznak — de olyan bankot igényelnek, amely valóban érti őket. Mi napi szinten dolgozunk ezekkel a specialistákkal."),
        ((("Finance that matches the asset", "Finanzierung, die zum Objekt passt", "Financiación a la altura del activo", "Az ingatlanhoz illő finanszírozás"),
          ("HMO lending turns on details the high street never asks about: licensing, Article 4 areas, room counts, commercial versus bricks-and-mortar valuation. Getting these right before application is the difference between a strong offer and a down-valuation.",
           "Bei HMO-Finanzierungen entscheiden Details, nach denen klassische Banken nie fragen: Lizenzen, Article-4-Gebiete, Zimmeranzahl, Ertragswert- vs. Substanzwertbewertung. Diese vorab richtig zu setzen, entscheidet zwischen starkem Angebot und Abwertung.",
           "La financiación HMO depende de detalles que la banca tradicional nunca pregunta: licencias, zonas Article 4, número de habitaciones, valoración comercial frente a residencial. Acertarlos antes de solicitar marca la diferencia entre una buena oferta y una tasación a la baja.",
           "A HMO-hitelezés olyan részleteken múlik, amelyekről a nagybankok sosem kérdeznek: engedélyek, Article 4 övezetek, szobaszám, hozamalapú vagy hagyományos értékelés. Ha ezeket előre jól állítjuk be, az a különbség egy erős ajánlat és egy leértékelés között.")),
         [("Licensed and large HMOs (7+ rooms) with specialist lenders", "Lizenzierte und große HMOs (7+ Zimmer) bei Spezialbanken", "HMO con licencia y grandes (7+ habitaciones) con bancos especializados", "Engedélyes és nagy HMO-k (7+ szoba) speciális hitelezőkkel"),
          ("Multi-unit freehold blocks (MUFB) on a single title", "Mehrfamilienblöcke (MUFB) auf einem Grundbuchtitel", "Bloques multiunidad (MUFB) bajo un único título", "Többlakásos épületek (MUFB) egy helyrajzi számon"),
          ("Commercial (investment) valuations where the yield justifies it", "Ertragswert-Bewertungen, wo die Rendite es rechtfertigt", "Valoraciones comerciales por rendimiento cuando el yield lo justifica", "Hozamalapú értékelés, ahol a bérleti hozam indokolja"),
          ("Refurbishment-to-let and bridge-to-term structures", "Sanierungs- und Bridge-to-Term-Strukturen", "Estructuras de reforma-para-alquilar y puente a largo plazo", "Felújítás-majd-kiadás és áthidaló-hosszútávú struktúrák"),
          ("First-time HMO investors with a landlord track record", "HMO-Einsteiger mit Vermietererfahrung", "Primeros inversores en HMO con historial de arrendador", "Első HMO-vásárlók meglévő bérbeadói múlttal")]),
        ((("The valuation is the battle", "Die Bewertung ist die Schlacht", "La tasación es la batalla", "Az értékbecslés a döntő csata"),
          ("Two valuers can put six figures of difference on the same HMO depending on the method instructed. We select lenders whose valuation approach fits your asset — and prepare the pack the valuer sees on the day.",
           "Zwei Gutachter können dasselbe HMO je nach Methode sechsstellig unterschiedlich bewerten. Wir wählen Banken, deren Bewertungsansatz zu Ihrem Objekt passt — und bereiten die Unterlagen vor, die der Gutachter am Termin sieht.",
           "Dos tasadores pueden diferir en seis cifras sobre el mismo HMO según el método aplicado. Elegimos bancos cuyo enfoque de tasación encaje con su activo — y preparamos el dossier que el tasador verá ese día.",
           "Két értékbecslő akár hat számjegyű különbséggel értékelheti ugyanazt a HMO-t a módszertől függően. Olyan bankot választunk, amelynek értékelési megközelítése illik az ingatlanához — és mi állítjuk össze az anyagot, amit az értékbecslő a helyszínen lát."),
          ("On refinance, a well-argued commercial valuation can release the capital for your next project without selling anything. That's the multiplier professional HMO investors build on.",
           "Bei einer Refinanzierung kann eine gut begründete Ertragswert-Bewertung das Kapital für Ihr nächstes Projekt freisetzen — ohne Verkauf. Das ist der Hebel professioneller HMO-Investoren.",
           "En una refinanciación, una tasación comercial bien argumentada puede liberar el capital para su próximo proyecto sin vender nada. Ese es el multiplicador de los inversores profesionales en HMO.",
           "Hitelkiváltáskor egy jól alátámasztott hozamalapú értékelés eladás nélkül szabadíthatja fel a tőkét a következő projekthez. Ez az a többszöröző, amire a profi HMO-befektetők építenek."))),
        [((("Do I need experience to get an HMO mortgage?", "Brauche ich Erfahrung für eine HMO-Finanzierung?", "¿Necesito experiencia para una hipoteca HMO?", "Kell tapasztalat HMO-hitelhez?")),
          (("Most lenders want at least 12 months as a landlord of any kind; some want previous HMO ownership specifically. A handful accept first-timers with strong wider profiles. We match you to the right tier honestly, before anyone runs your credit.",
            "Die meisten Banken verlangen mindestens 12 Monate Vermietererfahrung; einige speziell HMO-Erfahrung. Wenige akzeptieren Einsteiger mit starkem Profil. Wir ordnen Sie ehrlich der richtigen Kategorie zu — bevor jemand Ihre Bonität abfragt.",
            "La mayoría de bancos exigen al menos 12 meses como arrendador; algunos requieren experiencia previa en HMO. Unos pocos aceptan principiantes con perfiles sólidos. Le situamos honestamente en el nivel correcto antes de cualquier consulta de crédito.",
            "A legtöbb bank legalább 12 hónap bérbeadói múltat kér; néhány kifejezetten HMO-tapasztalatot. Kevés fogad el kezdőt, erős profillal. Őszintén a megfelelő kategóriába soroljuk, mielőtt bárki lekérdezné a hitelmúltját."))),
         ((("Bricks-and-mortar or commercial valuation — which will I get?", "Substanzwert oder Ertragswert — was bekomme ich?", "¿Tasación residencial o comercial — cuál tendré?", "Hagyományos vagy hozamalapú értékelést kapok?")),
          (("Smaller HMOs in residential areas usually value as standard houses; large, licensed or Article 4 HMOs can justify investment-based valuations. Since this can swing the loan size enormously, we assess it before choosing the lender, not after.",
            "Kleinere HMOs in Wohngebieten werden meist als normale Häuser bewertet; große, lizenzierte oder Article-4-Objekte können Ertragswert rechtfertigen. Da dies die Darlehenshöhe enorm beeinflusst, prüfen wir es vor der Bankauswahl.",
            "Los HMO pequeños en zonas residenciales suelen tasarse como viviendas estándar; los grandes, con licencia o en zonas Article 4 pueden justificar tasación por rendimiento. Como esto cambia enormemente el importe del préstamo, lo evaluamos antes de elegir banco.",
            "A kisebb, lakóövezeti HMO-kat általában normál házként értékelik; a nagy, engedélyes vagy Article 4 övezetben lévők hozamalapú értékelést indokolhatnak. Mivel ez óriási mértékben befolyásolja a hitelösszeget, még a bank kiválasztása előtt felmérjük."))),
         ((("Can I convert a house into an HMO with mortgage finance?", "Kann ich ein Haus mit Finanzierung in ein HMO umwandeln?", "¿Puedo convertir una casa en HMO con financiación?", "Átalakíthatok egy házat HMO-vá hitelből?")),
          (("Yes — typically with a refurbishment bridge that funds the works, exiting onto a term HMO mortgage at the higher post-conversion value. We arrange both legs together so the exit is guaranteed before the bridge starts.",
            "Ja — üblicherweise über einen Sanierungskredit für die Arbeiten, der nach Umbau in eine HMO-Hypothek zum höheren Wert übergeht. Wir arrangieren beide Schritte gemeinsam, damit der Exit vor Start gesichert ist.",
            "Sí — normalmente con un préstamo puente de reforma que financia las obras, saliendo a una hipoteca HMO al valor superior tras la conversión. Gestionamos ambos tramos juntos para que la salida esté garantizada antes de empezar.",
            "Igen — jellemzően felújítási áthidaló hitellel, amely a munkálatokat fedezi, majd az átalakítás utáni magasabb értéken HMO-jelzáloghitelbe vált. A két lépést együtt intézzük, hogy a kiszállás már az áthidaló indulása előtt biztosított legyen.")))],
        ("Higher yield needs sharper finance", "Höhere Rendite braucht schärfere Finanzierung", "Mayor rendimiento exige mejor financiación", "A magasabb hozamhoz élesebb finanszírozás kell",
         "Send us the property details and current tenancy schedule — we'll tell you what a specialist lender would really advance.",
         "Senden Sie uns Objektdaten und Mietaufstellung — wir sagen Ihnen, was eine Spezialbank wirklich finanzieren würde.",
         "Envíenos los datos de la propiedad y el cuadro de alquileres — le diremos qué financiaría realmente un banco especializado.",
         "Küldje el az ingatlan adatait és a bérleti kimutatást — megmondjuk, mennyit finanszírozna valójában egy specialista bank."))

def build_contractors():
    build_service(
        "contractors", "svc-self-employed.jpg",
        "Contractor Mortgages UK — Day Rate, Umbrella & Ltd | Agnes Mortgage",
        "UK contractor mortgage advice: day-rate assessment, umbrella company income, limited company contractors. Whole-of-market, FCA-regulated broker.",
        ("Contractor Mortgages", "Auftragnehmer-Hypotheken", "Hipotecas para contratistas", "Szerződéses jelzáloghitelek"),
        ("Day rate, umbrella or limited company — lenders assess contractor income in three completely different ways. The right route can double what you qualify for.",
         "Tagessatz, Umbrella oder eigene GmbH — Banken bewerten Auftragnehmer-Einkommen auf drei völlig unterschiedliche Arten. Der richtige Weg kann Ihre Darlehenssumme verdoppeln.",
         "Tarifa diaria, umbrella o sociedad limitada — los bancos evalúan los ingresos de contratistas de tres formas completamente distintas. La vía correcta puede duplicar su capacidad.",
         "Napidíj, ernyőcég vagy saját Kft. — a bankok háromféleképpen értékelik a szerződéses jövedelmet. A helyes út megduplázhatja, amire jogosult."),
        ((("Three income routes, one right answer", "Drei Einkommenswege, eine richtige Antwort", "Tres vías de ingresos, una respuesta correcta", "Három jövedelmi út, egy helyes válasz"),
          ("A contractor earning £500 a day can qualify for anything from £180,000 to £450,000 depending on how the lender assesses income. Day-rate annualisation, umbrella payslips, or company accounts — each route has lenders that prefer it, and choosing wrong means borrowing far less than you should.",
           "Ein Auftragnehmer mit £500 Tagessatz kann je nach Bewertungsmethode für £180.000 bis £450.000 qualifiziert werden. Tagessatz-Hochrechnung, Umbrella-Gehaltsabrechnungen oder Firmenabschlüsse — für jede Methode gibt es spezialisierte Banken.",
           "Un contratista que gana £500 al día puede cualificar desde £180.000 hasta £450.000 según cómo evalúe el banco. Anualización de tarifa diaria, nóminas de umbrella o cuentas de sociedad — cada vía tiene bancos que la prefieren.",
           "Egy napi £500-ot kereső szerződéses £180.000-tól £450.000-ig bármennyire jogosult lehet, attól függően, hogyan értékeli a bank a jövedelmét. Napidíj-éves vetítés, ernyőcéges bérjegyzék vagy céges beszámoló — mindegyikhez vannak speciális bankok.")),
         [("Day-rate contractors assessed at annualised contract value (×46 or ×48 weeks)", "Tagessatz-Auftragnehmer bewertet auf Jahresbasis (×46 oder ×48 Wochen)", "Contratistas de tarifa diaria evaluados por valor anualizado (×46 o ×48 semanas)", "Napidíjas szerződésesek éves vetítéssel értékelve (×46 vagy ×48 hét)"),
          ("Umbrella company contractors using PAYE payslips", "Umbrella-Auftragnehmer mit PAYE-Gehaltsabrechnungen", "Contratistas umbrella con nóminas PAYE", "Ernyőcéges szerződésesek PAYE bérjegyzékkel"),
          ("Ltd company contractors assessed on salary plus dividends or retained profit", "GmbH-Auftragnehmer bewertet auf Gehalt plus Dividenden oder einbehaltenen Gewinn", "Contratistas Ltd evaluados por salario más dividendos o beneficio retenido", "Kft.-s szerződésesek fizetés + osztalék vagy visszatartott nyereség alapján"),
          ("CIS subcontractors in construction and trades", "CIS-Subunternehmer im Baugewerbe", "Subcontratistas CIS en construcción", "CIS alvállalkozók az építőiparban"),
          ("Contract gaps, multiple contracts and IR35 — navigated with the right lender", "Vertragslücken, mehrere Verträge und IR35 — beim richtigen Kreditgeber kein Hindernis", "Vacíos entre contratos, múltiples contratos e IR35 — navegados con el banco adecuado", "Szerződés-szünetek, több szerződés és IR35 — a megfelelő bankkal kezelhetők")]),
        ((("Day rate is the fastest path to maximum borrowing", "Tagessatz ist der schnellste Weg zur maximalen Darlehenssumme", "La tarifa diaria es la vía más rápida al máximo préstamo", "A napidíj a leggyorsabb út a maximális hitelösszeghez"),
          ("If you have a current contract and at least 12 months of continuous contracting history, day-rate lenders will annualise your contract value and apply a standard income multiple — typically 4.5× to 5.5×. That usually produces a far higher figure than your company accounts, which show income after expenses and tax planning.",
           "Wenn Sie einen laufenden Vertrag und mindestens 12 Monate kontinuierliche Auftragstätigkeit nachweisen, rechnen Tagessatz-Banken Ihren Vertragswert aufs Jahr hoch und wenden das übliche Vielfache an — typisch 4,5× bis 5,5×. Das ergibt meist deutlich mehr als Ihre Firmenabschlüsse nach Ausgaben und Steueroptimierung.",
           "Si tiene un contrato vigente y al menos 12 meses de historial continuo, los bancos de tarifa diaria anualizarán su valor contractual y aplicarán un múltiplo estándar — normalmente 4,5× a 5,5×. Eso suele producir una cifra muy superior a sus cuentas de empresa, que muestran ingresos tras gastos y planificación fiscal.",
           "Ha van aktuális szerződése és legalább 12 hónapos folyamatos szerződéses múltja, a napidíjas bankok éves szintre vetítik a szerződés értékét és a szokásos szorzót alkalmazzák — jellemzően 4,5×–5,5×. Ez általában jóval magasabb összeget eredményez, mint a céges beszámoló, ami a kiadások és adótervezés utáni jövedelmet mutatja."),
          ("We check which route produces the strongest result for your specific situation before submitting anything. Sometimes it is the day rate, sometimes the company accounts — and occasionally the umbrella payslip route wins for contractors who have recently switched structures.",
           "Wir prüfen, welcher Weg in Ihrer Situation das beste Ergebnis liefert, bevor wir etwas einreichen. Manchmal ist es der Tagessatz, manchmal die Firmenabschlüsse — und gelegentlich gewinnt die Umbrella-Methode bei kürzlich gewechselter Struktur.",
           "Comprobamos qué vía produce el mejor resultado para su situación antes de presentar nada. A veces es la tarifa diaria, a veces las cuentas de empresa — y ocasionalmente la vía umbrella gana para contratistas que han cambiado de estructura recientemente.",
           "Mielőtt bármit beadnánk, ellenőrizzük, melyik út hozza a legerősebb eredményt az Ön helyzetében. Néha a napidíj, néha a céges beszámoló — és alkalmanként az ernyőcéges út nyer azoknál, akik nemrég váltottak struktúrát."))),
        [((("How long do I need to have been contracting?", "Wie lange muss ich als Auftragnehmer tätig sein?", "¿Cuánto tiempo necesito llevar como contratista?", "Mennyi ideje kell szerződésesnek lennem?")),
          (("Most day-rate lenders want at least 12 months of continuous contracting, though not necessarily with the same client. Some accept six months if your CV shows a longer career in the field. We match the requirement to your history before running any credit search.",
            "Die meisten Tagessatz-Banken verlangen mindestens 12 Monate kontinuierliche Auftragstätigkeit, nicht unbedingt beim selben Kunden. Einige akzeptieren sechs Monate bei längerer Branchenerfahrung. Wir gleichen die Anforderung mit Ihrer Historie ab, bevor wir eine Bonitätsprüfung starten.",
            "La mayoría de bancos de tarifa diaria exigen al menos 12 meses de contratación continua, no necesariamente con el mismo cliente. Algunos aceptan seis meses si su CV muestra una carrera más larga. Ajustamos el requisito a su historial antes de cualquier consulta de crédito.",
            "A legtöbb napidíjas bank legalább 12 hónap folyamatos szerződéses múltat kér, bár nem feltétlenül ugyanannál az ügyfélnél. Néhányan hat hónapot is elfogadnak, ha az önéletrajz hosszabb szakmai pályát mutat. A követelményt az Ön múltjához illesztjük, mielőtt bármilyen hitelkeresést futtatnánk."))),
         ((("What if I have a gap between contracts?", "Was, wenn ich eine Vertragspause habe?", "¿Qué pasa si tengo un vacío entre contratos?", "Mi van, ha szünet van a szerződéseim között?")),
          (("Short gaps — up to six weeks — are usually fine with most lenders. Longer breaks or a current gap require careful lender selection; some will assess on the last completed contract if you have a strong track record. We would not submit until we know the lender's stance on your specific gap.",
            "Kurze Pausen — bis zu sechs Wochen — sind bei den meisten Banken kein Problem. Längere Unterbrechungen erfordern sorgfältige Bankauswahl; einige bewerten anhand des letzten abgeschlossenen Vertrags bei guter Historie. Wir reichen erst ein, wenn wir die Position der Bank zu Ihrer Pause kennen.",
            "Vacíos cortos — hasta seis semanas — suelen ser aceptables. Interrupciones más largas requieren selección cuidadosa; algunos bancos evalúan por el último contrato si tiene buen historial. No presentamos hasta conocer la postura del banco sobre su vacío concreto.",
            "Rövid szünetek — hat hétig — általában elfogadhatók a legtöbb banknál. Hosszabb szünet vagy aktuális szünet gondos bankválasztást igényel; néhányan az utolsó befejezett szerződés alapján értékelnek, ha erős a múltja. Nem adunk be semmit, amíg nem ismerjük a bank álláspontját az Ön konkrét szünetéről."))),
         ((("Does IR35 affect my mortgage application?", "Beeinflusst IR35 meinen Hypothekenantrag?", "¿Afecta IR35 a mi solicitud?", "Az IR35 hatással van a jelzáloghitel-igénylésemre?")),
          (("It can change which assessment route is available. Inside IR35, you are typically paid via PAYE through an umbrella or agency, so lenders treat you closer to an employee — sometimes helpful. Outside IR35 with your own Ltd, the day-rate annualisation route usually produces a higher figure. We assess your IR35 status as part of the income routing, not as an afterthought.",
            "Es kann ändern, welcher Bewertungsweg verfügbar ist. Innerhalb von IR35 werden Sie meist über PAYE bezahlt — Banken behandeln Sie dann ähnlich wie einen Angestellten. Außerhalb von IR35 mit eigener GmbH liefert die Tagessatz-Hochrechnung meist eine höhere Summe. Wir bewerten Ihren IR35-Status als Teil der Einkommensroute.",
            "Puede cambiar qué vía de evaluación está disponible. Dentro de IR35, normalmente cobra por PAYE a través de umbrella — los bancos le tratan más como empleado. Fuera de IR35 con su Ltd, la anualización de tarifa diaria suele producir una cifra mayor. Evaluamos su estado IR35 como parte del enrutamiento de ingresos.",
            "Megváltoztathatja, melyik értékelési út érhető el. IR35-ön belül jellemzően PAYE-n keresztül kap fizetést — a bankok alkalmazotthoz hasonlóan kezelik. IR35-ön kívül, saját Kft.-vel a napidíj-éves vetítés általában magasabb összeget eredményez. Az IR35-státuszát a jövedelemútvonal részeként értékeljük.")))],
        ("Contracting should unlock lending, not limit it", "Auftragnehmer sein sollte Kreditchancen eröffnen, nicht begrenzen", "Ser contratista debería abrir puertas, no cerrarlas", "A szerződéses munka lehetőségeket nyisson, ne korlátozzon",
         "Bring us your current contract and we will show you exactly what each assessment route produces — in one conversation.",
         "Bringen Sie Ihren aktuellen Vertrag mit und wir zeigen Ihnen, was jede Bewertungsmethode ergibt — in einem Gespräch.",
         "Traiga su contrato actual y le mostraremos exactamente qué produce cada vía de evaluación — en una conversación.",
         "Hozza el a jelenlegi szerződését, és megmutatjuk, mit eredményez az egyes értékelési utak — egyetlen beszélgetésben."))

def build_residential():
    build_service(
        "residential", "svc-residential.jpg",
        "Residential Mortgages UK | Agnes Mortgage",
        "Residential mortgage advice for complex income, unusual properties and demanding timelines. Whole-of-market, FCA-regulated, four languages.",
        ("Residential Mortgages", "Wohnimmobilien-Hypotheken", "Hipotecas residenciales", "Lakóingatlan-jelzáloghitelek"),
        ("Buying your own home should not mean squeezing your finances into a high-street checkbox. Whether your income is complex, the property is unusual or the timeline is tight, we find the lender that fits.",
         "Der Kauf Ihres Eigenheims sollte nicht bedeuten, Ihre Finanzen in ein Standard-Schema zu pressen. Ob komplexes Einkommen, ungewöhnliche Immobilie oder enge Fristen — wir finden die passende Bank.",
         "Comprar su hogar no debería significar encajar sus finanzas en una casilla estándar. Ya sea por ingresos complejos, una propiedad inusual o plazos ajustados, encontramos el banco adecuado.",
         "A saját otthon vásárlása nem jelentheti azt, hogy a pénzügyeit egy nagybanki sablonba kell préselnie. Legyen szó összetett jövedelemről, szokatlan ingatlanról vagy szoros határidőről — megtaláljuk a megfelelő bankot."),
        ((("Beyond the high-street criteria", "Jenseits der Standardkriterien", "Más allá de los criterios estándar", "A nagybanki feltételeken túl"),
          ("Most residential lenders follow rigid affordability models that penalise anyone whose income does not arrive as a single PAYE salary. We know which lenders flex on complex income, new-build incentives, non-standard construction and properties above commercial premises.",
           "Die meisten Wohnkreditgeber folgen starren Modellen, die jeden bestrafen, dessen Einkommen nicht als einfaches Gehalt kommt. Wir wissen, welche Banken bei komplexem Einkommen, Neubau-Anreizen und Sonderbauweisen flexibel sind.",
           "La mayoría de bancos residenciales siguen modelos rígidos que penalizan a quien no cobra un único salario fijo. Sabemos qué bancos son flexibles con ingresos complejos, incentivos de obra nueva y construcciones no estándar.",
           "A legtöbb lakossági hitelező merev modellt követ, ami hátrányba hozza, akinek jövedelme nem egyetlen PAYE fizetés. Tudjuk, melyik bank rugalmas összetett jövedelemnél, újépítésű ösztönzőknél és nem szabványos építésnél.")),
         [("First-time buyers with complex income or gifted deposits", "Erstkäufer mit komplexem Einkommen oder geschenktem Eigenkapital", "Compradores primerizos con ingresos complejos o depósitos donados", "Első vásárlók összetett jövedelemmel vagy ajándékozott önerővel"),
          ("Home movers needing simultaneous sale and purchase coordination", "Umzügler mit gleichzeitigem Verkaufs- und Kaufprozess", "Compradores que necesitan coordinar venta y compra simultáneas", "Költözők, akiknek az eladás és vásárlás egyidejű koordinálása kell"),
          ("New-build purchases with developer incentives and tight exchange deadlines", "Neubau-Käufe mit Entwickler-Anreizen und engen Fristen", "Compras de obra nueva con incentivos del promotor y plazos ajustados", "Újépítésű vásárlások fejlesztői ösztönzőkkel és szoros határidőkkel"),
          ("Non-standard construction: timber frame, steel frame, flat roof, listed buildings", "Sonderbauweisen: Holzrahmen, Stahlrahmen, Flachdach, denkmalgeschützte Gebäude", "Construcción no estándar: madera, acero, techo plano, edificios protegidos", "Nem szabványos építés: fa váz, acél váz, lapos tető, műemléképületek"),
          ("Interest-only residential on higher incomes with clear repayment strategy", "Tilgungsfreie Wohnkredite bei höherem Einkommen mit klarer Rückzahlungsstrategie", "Solo interés residencial con ingresos altos y estrategia de reembolso clara", "Csak-kamat lakossági hitel magasabb jövedelemnél, világos visszafizetési stratégiával")]),
        ((("The right lender, not just the cheapest rate", "Die richtige Bank, nicht nur der günstigste Zins", "El banco adecuado, no solo el tipo más barato", "A megfelelő bank, nem csak a legolcsóbb kamat"),
          ("A mortgage comparison site ranks by rate. An adviser ranks by likelihood of approval, speed to offer, flexibility on income and property type, and total cost including fees. When your case has any complexity at all, the cheapest headline rate is rarely the cheapest mortgage.",
           "Ein Vergleichsportal sortiert nach Zins. Eine Beraterin sortiert nach Genehmigungschance, Bearbeitungstempo, Flexibilität bei Einkommen und Objektart sowie Gesamtkosten inkl. Gebühren. Bei jeder Komplexität ist der günstigste Schlagzeilenzins selten die günstigste Hypothek.",
           "Un comparador ordena por tipo de interés. Una asesora ordena por probabilidad de aprobación, rapidez de oferta, flexibilidad con ingresos y tipo de propiedad, y coste total con comisiones. Con cualquier complejidad, el tipo más barato del titular rara vez es la hipoteca más barata.",
           "Egy összehasonlító oldal kamat szerint rangsorol. Egy tanácsadó a jóváhagyás valószínűsége, az ajánlat gyorsasága, a jövedelem és ingatlantípus rugalmassága, valamint a díjakkal együtt számított teljes költség alapján rangsorol. Ha bármilyen összetettség van, a legolcsóbb címlapkamat ritkán a legolcsóbb jelzáloghitel."),
          ("We explain the trade-offs plainly, model two or three realistic routes with live pricing, and let you choose with full visibility. No pressure, no clock.",
           "Wir erklären die Abwägungen klar, modellieren zwei oder drei realistische Wege mit aktuellen Konditionen und lassen Sie mit voller Transparenz entscheiden.",
           "Explicamos las alternativas con claridad, modelamos dos o tres vías realistas con precios actuales y le dejamos elegir con total visibilidad.",
           "Világosan elmagyarázzuk a kompromisszumokat, két-három reális utat modellezünk aktuális árazással, és Ön teljes átláthatóság mellett dönt."))),
        [((("How quickly can I get a mortgage offer?", "Wie schnell bekomme ich ein Hypothekenangebot?", "¿En cuánto tiempo puedo obtener una oferta?", "Milyen gyorsan kaphatok hitelígérvényt?")),
          (("Most mainstream lenders issue offers in two to four weeks from full application. If speed is critical — a chain break, an auction, a new-build exchange deadline — we route to lenders with known fast-track underwriting and flag the urgency from day one.",
            "Die meisten Banken erstellen Angebote in zwei bis vier Wochen nach vollständiger Antragstellung. Wenn Tempo entscheidend ist, leiten wir zu Banken mit bekanntem Fast-Track und melden die Dringlichkeit ab Tag eins.",
            "La mayoría de bancos emiten ofertas en dos a cuatro semanas desde la solicitud completa. Si la velocidad es crítica, dirigimos a bancos con tramitación rápida conocida y señalamos la urgencia desde el primer día.",
            "A legtöbb bank két-négy hét alatt ad ajánlatot a teljes igénylés beadásától. Ha a gyorsaság kritikus, ismert gyorsított eljárású bankokhoz irányítjuk, és az első naptól jelezzük a sürgősséget."))),
         ((("Do I need a big deposit?", "Brauche ich viel Eigenkapital?", "¿Necesito una entrada grande?", "Nagy önerő kell?")),
          (("Residential mortgages are available from 5% deposit, though the rate improves significantly at 10%, 15% and 25%. We model the cost difference so you can decide whether stretching the deposit is worth the saving — sometimes it is, sometimes it genuinely is not.",
            "Wohnkredite sind ab 5% Eigenkapital möglich, wobei die Konditionen bei 10%, 15% und 25% deutlich besser werden. Wir berechnen den Kostenunterschied, damit Sie entscheiden können, ob sich mehr Eigenkapital lohnt.",
            "Las hipotecas residenciales están disponibles desde el 5% de entrada, aunque el tipo mejora significativamente al 10%, 15% y 25%. Modelamos la diferencia de coste para que decida si ampliar la entrada merece la pena.",
            "Lakossági jelzáloghitel már 5% önerőtől elérhető, bár a kamat jelentősen javul 10%, 15% és 25%-nál. Kiszámoljuk a költségkülönbséget, hogy eldönthesse, megéri-e magasabb önerőt felmutatni."))),
         ((("Can you help with new-build purchases?", "Können Sie bei Neubau-Käufen helfen?", "¿Pueden ayudar con compras de obra nueva?", "Segítenek újépítésű ingatlan vásárlásánál?")),
          (("Yes — new builds have specific lender requirements around valuations, developer warranties, exchange deadlines and incentive handling. We work with the developer's timeline backwards to make sure funding is confirmed before exchange, not chased after it.",
            "Ja — Neubauten haben spezifische Anforderungen an Bewertungen, Bauträger-Garantien, Fristen und Anreize. Wir planen vom Termin des Bauträgers rückwärts, damit die Finanzierung vor dem Vertragsaustausch steht.",
            "Sí — las obras nuevas tienen requisitos específicos sobre tasaciones, garantías del promotor, plazos de intercambio y gestión de incentivos. Trabajamos hacia atrás desde el plazo del promotor para asegurar la financiación antes del intercambio.",
            "Igen — az újépítésű ingatlanoknál speciális követelmények vannak az értékelésre, fejlesztői garanciákra, szerződéskötési határidőkre és ösztönzők kezelésére. A fejlesztő határidejétől visszafelé tervezünk, hogy a finanszírozás a szerződéskötés előtt álljon.")))],
        ("Your home deserves more than an algorithm", "Ihr Zuhause verdient mehr als einen Algorithmus", "Su hogar merece más que un algoritmo", "Az otthona többet érdemel egy algoritmusnál",
         "Tell us what you are looking for and we will show you exactly what the market offers — with no obligation and no clock running.",
         "Sagen Sie uns, wonach Sie suchen, und wir zeigen Ihnen genau, was der Markt bietet — unverbindlich und ohne Zeitdruck.",
         "Díganos qué busca y le mostraremos exactamente lo que ofrece el mercado — sin compromiso y sin prisa.",
         "Mondja el, mit keres, és pontosan megmutatjuk, mit kínál a piac — kötelezettség és időnyomás nélkül."))

def build_remaining_services():
    build_service(
        "expat-mortgages", "svc-expat.jpg",
        "Expat & Foreign National Mortgages UK | Agnes Mortgage",
        "UK mortgages for British expats and foreign nationals — foreign currency income, no UK credit history, buy-to-let or residential, arranged remotely worldwide.",
        ("Expat & Foreign National Mortgages", "Expat- & Ausländerfinanzierung", "Hipotecas para expatriados y extranjeros", "Jelzáloghitel külföldieknek és expatoknak"),
        ("Living in Dubai, Frankfurt, Madrid or Budapest and buying in the UK? Distance is not the obstacle — the wrong lender is. We arrange everything remotely, in your language.",
         "Sie leben in Dubai, Frankfurt oder Madrid und kaufen in Großbritannien? Die Entfernung ist nicht das Hindernis — die falsche Bank ist es. Wir arrangieren alles remote, in Ihrer Sprache.",
         "¿Vive en Dubái, Fráncfort o Madrid y compra en el Reino Unido? La distancia no es el obstáculo — el banco equivocado sí. Lo gestionamos todo en remoto, en su idioma.",
         "Dubajban, Frankfurtban vagy Budapesten él, és az Egyesült Királyságban vásárolna? Nem a távolság az akadály — hanem a rossz bank. Mindent távolról intézünk, az Ön nyelvén."),
        ((("Built for cross-border lives", "Für ein Leben über Grenzen hinweg", "Pensado para vidas transfronterizas", "Határokon átívelő életekre tervezve"),
          ("Expat lending has its own rulebook: which currencies a lender accepts, how they haircut foreign income, whether a thin UK credit file matters, which countries they will not touch. We navigate that rulebook every week.",
           "Expat-Finanzierung folgt eigenen Regeln: akzeptierte Währungen, Abschläge auf Auslandseinkommen, Umgang mit dünner UK-Kreditakte, ausgeschlossene Länder. Wir navigieren dieses Regelwerk jede Woche.",
           "La financiación para expatriados tiene sus propias reglas: qué divisas acepta cada banco, qué recorte aplican a los ingresos extranjeros, si importa un historial crediticio británico escaso. Navegamos ese reglamento cada semana.",
           "A külföldieknek szóló hitelezésnek saját szabálykönyve van: mely devizákat fogadja el a bank, mekkora levonást alkalmaz a külföldi jövedelemre, számít-e a vékony brit hitelmúlt. Ezt a szabálykönyvet mi hetente forgatjuk.")),
         [("British expats buying residential or buy-to-let from anywhere in the world", "Britische Expats: Eigennutzung oder Vermietung, weltweit", "Expatriados británicos: vivienda o inversión desde cualquier país", "Brit expatok: saját célra vagy kiadásra, a világ bármely pontjáról"),
          ("Foreign nationals with no UK footprint — including first UK purchases", "Ausländische Staatsbürger ohne UK-Historie — auch Erstkäufe", "Extranjeros sin historial en el Reino Unido — incluida la primera compra", "Külföldi állampolgárok brit előzmények nélkül — első vásárlásra is"),
          ("Income in EUR, USD, AED, CHF, HUF and other major currencies", "Einkommen in EUR, USD, AED, CHF, HUF und weiteren Währungen", "Ingresos en EUR, USD, AED, CHF, HUF y otras divisas", "Jövedelem EUR, USD, AED, CHF, HUF és más devizákban"),
          ("Remote identity verification, digital signing and power-of-attorney completions", "Remote-Identifizierung, digitale Signatur, Abschluss per Vollmacht", "Verificación de identidad remota, firma digital y cierres con poder notarial", "Távoli azonosítás, digitális aláírás, meghatalmazással történő zárás"),
          ("Advice in English, German, Spanish and Hungarian throughout", "Beratung durchgehend auf Deutsch, Englisch, Spanisch, Ungarisch", "Asesoría en español, inglés, alemán y húngaro durante todo el proceso", "Tanácsadás végig magyarul, angolul, németül vagy spanyolul")]),
        ((("Foreign income, properly presented", "Auslandseinkommen, richtig präsentiert", "Ingresos extranjeros, bien presentados", "Külföldi jövedelem, jól bemutatva"),
          ("Lenders discount foreign-currency income by up to 25% for exchange-rate risk — but which lender, which currency and which discount varies enormously. Choosing the right combination often changes the maximum loan by six figures.",
           "Banken kürzen Fremdwährungseinkommen wegen Wechselkursrisiko um bis zu 25% — aber Bank, Währung und Abschlag variieren enorm. Die richtige Kombination verändert die maximale Darlehenssumme oft sechsstellig.",
           "Los bancos recortan los ingresos en divisa extranjera hasta un 25% por riesgo cambiario — pero el banco, la divisa y el recorte varían enormemente. La combinación correcta cambia el préstamo máximo a menudo en seis cifras.",
           "A bankok az árfolyamkockázat miatt akár 25%-kal is csökkentik a devizajövedelmet — de hogy melyik bank, melyik deviza és mekkora levonás, az óriási szórást mutat. A jó kombináció gyakran hat számjeggyel változtatja meg a maximális hitelösszeget."),
          ("Documents from foreign employers, tax systems and banks all need translating into a UK underwriter's language — figuratively and sometimes literally. That preparation is precisely what we do before any application is submitted.",
           "Unterlagen ausländischer Arbeitgeber, Steuersysteme und Banken müssen in die Sprache britischer Underwriter übersetzt werden — im übertragenen und manchmal wörtlichen Sinn. Genau diese Vorbereitung leisten wir vor jedem Antrag.",
           "Los documentos de empleadores, sistemas fiscales y bancos extranjeros deben traducirse al lenguaje del analista británico — en sentido figurado y a veces literal. Esa preparación es exactamente lo que hacemos antes de presentar cualquier solicitud.",
           "A külföldi munkáltatók, adórendszerek és bankok dokumentumait le kell fordítani a brit hitelbíráló nyelvére — átvitt és néha szó szerinti értelemben is. Pontosan ezt az előkészítést végezzük el minden igénylés benyújtása előtt."))),
        [((("Can I get a UK mortgage with no UK credit history?", "Bekomme ich eine UK-Hypothek ohne britische Kredithistorie?", "¿Puedo obtener una hipoteca sin historial crediticio británico?", "Kaphatok brit jelzáloghitelt brit hitelmúlt nélkül?")),
          (("Yes. Specialist and international lenders underwrite on your global profile — income, assets and credit conduct in your country of residence — rather than a UK credit score. Rates are slightly higher than domestic deals but entirely workable.",
            "Ja. Spezial- und internationale Banken prüfen Ihr globales Profil — Einkommen, Vermögen und Zahlungsverhalten im Wohnsitzland — statt eines UK-Scores. Die Konditionen liegen leicht über Inlandsniveau, sind aber absolut tragfähig.",
            "Sí. Los bancos especializados e internacionales evalúan su perfil global — ingresos, activos y conducta crediticia en su país de residencia — en lugar de una puntuación británica. Los tipos son algo superiores a los nacionales, pero perfectamente viables.",
            "Igen. A speciális és nemzetközi bankok a globális profilja alapján bírálnak — jövedelem, vagyon és hitelmúlt a lakóhelye szerinti országban — nem brit pontszám alapján. A kamatok kissé magasabbak a belföldinél, de teljesen vállalhatóak."))),
         ((("Do I need to fly to the UK to complete?", "Muss ich zur Abwicklung nach Großbritannien reisen?", "¿Tengo que viajar al Reino Unido para firmar?", "El kell utaznom az Egyesült Királyságba az aláíráshoz?")),
          (("Almost never. Identity checks run digitally, documents are signed electronically or witnessed at a local notary or British embassy, and solicitors complete by post and bank transfer. Many clients first see their property after they own it.",
            "Fast nie. Identitätsprüfungen laufen digital, Dokumente werden elektronisch signiert oder bei Notar bzw. Botschaft beglaubigt, Anwälte wickeln per Post und Überweisung ab. Viele Kunden sehen ihre Immobilie erstmals nach dem Kauf.",
            "Casi nunca. La verificación de identidad es digital, los documentos se firman electrónicamente o ante notario local o embajada británica, y los abogados cierran por correo y transferencia. Muchos clientes ven su propiedad por primera vez ya siendo suya.",
            "Szinte soha. Az azonosítás digitálisan zajlik, a dokumentumokat elektronikusan vagy helyi közjegyző, illetve brit nagykövetség előtt írják alá, az ügyvédek postán és átutalással zárnak. Sok ügyfelünk már tulajdonosként látja először az ingatlanát."))),
         ((("What deposit do overseas buyers need?", "Wie viel Eigenkapital brauchen Auslandskäufer?", "¿Qué entrada necesita un comprador no residente?", "Mekkora önerő kell külföldi vásárlóként?")),
          (("Plan for 25% on buy-to-let and 15–25% on residential, depending on lender and currency. Additional stamp duty surcharges apply to non-resident and second-home purchases — we include every cost in your numbers upfront.",
            "Rechnen Sie mit 25% bei Vermietungsobjekten und 15–25% bei Eigennutzung, je nach Bank und Währung. Für Nicht-Residenten und Zweitimmobilien fallen Stempelsteuer-Zuschläge an — wir kalkulieren alle Kosten von Anfang an ein.",
            "Calcule un 25% para inversión y un 15–25% para vivienda, según banco y divisa. Se aplican recargos del impuesto de transmisiones a no residentes y segundas viviendas — incluimos cada coste en sus números desde el principio.",
            "Számoljon 25%-kal kiadási célnál és 15–25%-kal saját lakhatásnál, banktól és devizától függően. A nem rezidensekre és második ingatlanokra illetékfelár vonatkozik — minden költséget előre beépítünk a kalkulációba.")))],
        ("Buying the UK from abroad?", "Kaufen Sie UK-Immobilien aus dem Ausland?", "¿Comprando en el Reino Unido desde el extranjero?", "Külföldről vásárolna az Egyesült Királyságban?",
         "One call in your own language and you will know your budget, your costs and your timeline — before you view a single property.",
         "Ein Gespräch in Ihrer Sprache und Sie kennen Budget, Kosten und Zeitplan — bevor Sie die erste Immobilie besichtigen.",
         "Una llamada en su idioma y conocerá su presupuesto, costes y plazos — antes de visitar una sola propiedad.",
         "Egyetlen hívás az anyanyelvén, és tudni fogja a keretét, a költségeit és az ütemtervét — mielőtt egyetlen ingatlant megnézne."))

    build_service(
        "self-employed", "svc-self-employed.jpg",
        "Self-Employed & Company Director Mortgages UK | Agnes Mortgage",
        "Mortgages for company directors, contractors and the self-employed — retained profits, dividends, day rates, one year of accounts. Whole-of-market UK advice.",
        ("Directors & Self-Employed Mortgages", "Hypotheken für Unternehmer & Selbständige", "Hipotecas para directores y autónomos", "Jelzáloghitel cégvezetőknek és vállalkozóknak"),
        ("You built a business precisely so a salary wouldn't define you. Your mortgage shouldn't be defined by one either — we lend against how entrepreneurs actually earn.",
         "Sie haben ein Unternehmen aufgebaut, damit ein Gehalt Sie nicht definiert. Ihre Hypothek sollte es auch nicht — wir finanzieren so, wie Unternehmer wirklich verdienen.",
         "Montó un negocio precisamente para que un salario no le definiera. Su hipoteca tampoco debería — financiamos según cómo ganan realmente los empresarios.",
         "Pont azért épített céget, hogy ne egy fizetés határozza meg. A jelzáloghitelét se az határozza meg — mi úgy finanszírozunk, ahogy a vállalkozók valójában keresnek."),
        ((("Income the high street can't read", "Einkommen, das Standardbanken nicht lesen können", "Ingresos que la banca tradicional no sabe leer", "Jövedelem, amit a nagybank nem tud olvasni"),
          ("Salary plus dividends is only the beginning. The right lender will work from salary plus your share of net profit — including profit you deliberately retained in the company. On a healthy business, that difference alone can double your borrowing.",
           "Gehalt plus Dividenden ist nur der Anfang. Die richtige Bank rechnet mit Gehalt plus Ihrem Anteil am Nettogewinn — einschließlich bewusst im Unternehmen belassener Gewinne. Bei einem gesunden Betrieb kann allein das Ihre Kreditsumme verdoppeln.",
           "Salario más dividendos es solo el principio. El banco adecuado calculará con salario más su parte del beneficio neto — incluido el que dejó deliberadamente en la empresa. En un negocio sano, solo esa diferencia puede duplicar su capacidad de préstamo.",
           "A fizetés plusz osztalék csak a kezdet. A megfelelő bank a fizetés plusz a nettó nyereség Önre eső részével számol — beleértve a tudatosan a cégben hagyott nyereséget is. Egy egészséges vállalkozásnál már ez a különbség megduplázhatja a hitelösszeget.")),
         [("Assessment on salary + net profit share, not just dividends drawn", "Bewertung nach Gehalt + Gewinnanteil, nicht nur entnommenen Dividenden", "Evaluación por salario + participación en beneficios, no solo dividendos", "Bírálat fizetés + nyereségrészesedés alapján, nem csak a felvett osztalék szerint"),
          ("One year of accounts accepted by selected lenders", "Ein Jahresabschluss bei ausgewählten Banken ausreichend", "Un solo ejercicio de cuentas aceptado por bancos seleccionados", "Egyetlen lezárt üzleti év is elég egyes bankoknál"),
          ("Contractors assessed on day rate, not accounts", "Contractor-Bewertung nach Tagessatz statt Bilanz", "Contractors evaluados por tarifa diaria, no por cuentas", "Vállalkozói napidíj alapú bírálat, beszámoló helyett"),
          ("Declining or lumpy profits handled with narrative underwriting", "Schwankende Gewinne durch erklärendes Underwriting gelöst", "Beneficios irregulares gestionados con análisis contextual", "Ingadozó nyereség kezelése magyarázó hitelbírálattal"),
          ("Partnerships, LLPs and sole traders equally covered", "Personengesellschaften, LLPs und Einzelunternehmer gleichermaßen abgedeckt", "Sociedades, LLP y autónomos igualmente cubiertos", "Bt-k, kkt-k és egyéni vállalkozók egyaránt lefedve")]),
        ((("The accountant's paradox, solved", "Das Steuerberater-Paradox, gelöst", "La paradoja del contable, resuelta", "A könyvelői paradoxon, megoldva"),
          ("Good accountants minimise your taxable income; mortgage lenders want to see maximum income. Caught between the two, most directors under-borrow for years. Our job is presenting the same legitimate numbers in the framework each underwriter uses.",
           "Gute Steuerberater minimieren Ihr zu versteuerndes Einkommen; Banken wollen maximales Einkommen sehen. Zwischen beiden gefangen, leihen die meisten Geschäftsführer jahrelang zu wenig. Unsere Aufgabe: dieselben legitimen Zahlen im Raster des jeweiligen Underwriters zu präsentieren.",
           "Un buen contable minimiza su base imponible; el banco quiere ver ingresos máximos. Atrapados entre ambos, la mayoría de directores piden menos de lo posible durante años. Nuestro trabajo es presentar las mismas cifras legítimas en el marco que usa cada analista.",
           "A jó könyvelő minimalizálja az adóköteles jövedelmet; a bank maximális jövedelmet akar látni. A kettő közé szorulva a legtöbb cégvezető évekig alulhitelezett. A mi dolgunk ugyanazokat a legitim számokat abban a keretben bemutatni, amit az adott hitelbíráló használ."),
          ("Timing matters too: applying two months before or after your year-end can change which figures count. We plan the application calendar around your accounts, not the other way round.",
           "Auch das Timing zählt: Ein Antrag zwei Monate vor oder nach dem Bilanzstichtag kann ändern, welche Zahlen gelten. Wir planen den Antragskalender um Ihre Abschlüsse herum — nicht umgekehrt.",
           "El momento también importa: solicitar dos meses antes o después del cierre del ejercicio puede cambiar qué cifras cuentan. Planificamos el calendario de la solicitud en torno a sus cuentas, no al revés.",
           "Az időzítés is számít: a fordulónap előtt vagy után két hónappal beadott igénylésnél más-más számok számíthatnak. Az igénylési naptárat a beszámolóihoz igazítjuk — nem fordítva."))),
        [((("How many years of accounts do I really need?", "Wie viele Jahresabschlüsse brauche ich wirklich?", "¿Cuántos años de cuentas necesito realmente?", "Hány év beszámoló kell valójában?")),
          (("The market standard is two; a meaningful group of lenders accepts one full year, and contractors can skip accounts entirely with day-rate assessment. Your trading history determines the lender pool — we tell you honestly which pool you're in.",
            "Der Marktstandard sind zwei; eine relevante Gruppe akzeptiert ein volles Jahr, und Contractors können mit Tagessatz-Bewertung ganz auf Abschlüsse verzichten. Ihre Historie bestimmt den Bankenpool — wir sagen Ihnen ehrlich, in welchem Sie sind.",
            "El estándar del mercado son dos; un grupo relevante de bancos acepta un ejercicio completo, y los contractors pueden prescindir de cuentas con la evaluación por tarifa diaria. Su historial determina el grupo de bancos — le decimos honestamente en cuál está.",
            "A piaci sztenderd kettő; a bankok egy jelentős köre elfogad egy teljes évet, a kontraktorok pedig napidíjas bírálattal beszámoló nélkül is mehetnek. A működési múlt határozza meg a szóba jöhető bankok körét — őszintén megmondjuk, Ön hol áll."))),
         ((("My latest year was lower — am I stuck?", "Mein letztes Jahr war schwächer — bin ich blockiert?", "Mi último año fue peor — ¿estoy bloqueado?", "A legutóbbi évem gyengébb volt — elakadtam?")),
          (("Not necessarily. Some lenders average the years, some take the latest, and some will accept a written explanation of a one-off dip with current management figures. The story matters as much as the spreadsheet — and we know who listens.",
            "Nicht unbedingt. Manche Banken mitteln die Jahre, manche nehmen das letzte, manche akzeptieren eine schriftliche Erklärung eines Einmaleffekts mit aktuellen BWA-Zahlen. Die Story zählt so viel wie die Tabelle — und wir wissen, wer zuhört.",
            "No necesariamente. Algunos bancos promedian los años, otros toman el último, y otros aceptan una explicación escrita de una caída puntual con cifras de gestión actuales. La historia importa tanto como la hoja de cálculo — y sabemos quién escucha.",
            "Nem feltétlenül. Egyes bankok átlagolják az éveket, mások a legutóbbit nézik, megint mások írásos magyarázatot is elfogadnak egy egyszeri visszaesésről, friss vezetői számokkal. A történet ugyanannyit ér, mint a táblázat — és mi tudjuk, ki hallgatja meg."))),
         ((("Does using retained profit for the deposit cause problems?", "Ist einbehaltener Gewinn als Eigenkapital problematisch?", "¿Usar beneficios retenidos como entrada da problemas?", "Gond, ha a cégben hagyott nyereség az önerő?")),
          (("Withdrawing a large sum for a deposit needs care — lenders will check it doesn't destabilise the company, and the tax cost needs weighing. Alternatives exist, including director's loans and lenders comfortable with company-sourced deposits. We map the options with your accountant.",
            "Eine große Entnahme fürs Eigenkapital erfordert Sorgfalt — Banken prüfen, ob sie das Unternehmen destabilisiert, und die Steuerlast ist abzuwägen. Es gibt Alternativen, etwa Gesellschafterdarlehen und Banken, die firmenbasiertes Eigenkapital akzeptieren.",
            "Retirar una suma grande para la entrada requiere cuidado — los bancos comprobarán que no desestabiliza la empresa, y hay que sopesar el coste fiscal. Existen alternativas, incluidos préstamos del director y bancos cómodos con entradas de origen empresarial.",
            "Nagy összeg kivétele önerőnek körültekintést igényel — a bank vizsgálja, hogy nem ingatja-e meg a céget, és az adóvonzatot is mérlegelni kell. Vannak alternatívák: tagi kölcsön, illetve olyan bankok, amelyek elfogadják a céges forrású önerőt. A lehetőségeket a könyvelőjével közösen térképezzük fel.")))],
        ("Your business deserves a better mortgage", "Ihr Unternehmen verdient eine bessere Hypothek", "Su negocio merece una hipoteca mejor", "A vállalkozása jobb jelzáloghitelt érdemel",
         "Send us your last accounts and we'll show you — in numbers — how much more the right presentation unlocks.",
         "Senden Sie uns Ihren letzten Abschluss und wir zeigen Ihnen in Zahlen, wie viel mehr die richtige Präsentation freisetzt.",
         "Envíenos sus últimas cuentas y le mostraremos — en cifras — cuánto más desbloquea la presentación correcta.",
         "Küldje el a legutóbbi beszámolóját, és számokban mutatjuk meg, mennyivel többet hoz a megfelelő bemutatás."))

    build_service(
        "high-net-worth", "svc-hnw.jpg",
        "High-Net-Worth Mortgages & Large Loans UK | Agnes Mortgage",
        "Bespoke high-net-worth mortgage advice — £1m+ lending, private banks, interest-only, multi-currency and complex-asset income across the UK.",
        ("High-Net-Worth & Large Loan Mortgages", "Finanzierung für vermögende Kunden", "Hipotecas para grandes patrimonios", "Jelzáloghitel nagy vagyonú ügyfeleknek"),
        ("Above a certain level, mortgages stop being products and become negotiations. We conduct those negotiations — with private banks and specialist desks that never advertise.",
         "Ab einem gewissen Niveau sind Hypotheken keine Produkte mehr, sondern Verhandlungen. Wir führen diese Verhandlungen — mit Privatbanken und Spezialabteilungen, die nie werben.",
         "A partir de cierto nivel, las hipotecas dejan de ser productos y se convierten en negociaciones. Nosotros llevamos esas negociaciones — con bancas privadas y mesas especializadas que nunca se anuncian.",
         "Egy bizonyos szint felett a jelzáloghitel már nem termék, hanem tárgyalás. Ezeket a tárgyalásokat mi folytatjuk le — privátbankokkal és speciális részlegekkel, amelyek sosem hirdetnek."),
        ((("Lending that reads a balance sheet", "Finanzierung, die eine Bilanz lesen kann", "Financiación que sabe leer un balance", "Finanszírozás, amely érti a mérleget"),
          ("Carried interest, vesting stock, trust distributions, income across three currencies: mainstream affordability calculators simply reject what they cannot categorise. HNW underwriting instead asks one question — does the overall wealth support the debt? We frame your case to answer it decisively.",
           "Carried Interest, Aktienoptionen, Trust-Ausschüttungen, Einkommen in drei Währungen: Standard-Rechner lehnen ab, was sie nicht einordnen können. HNW-Underwriting stellt stattdessen eine Frage — trägt das Gesamtvermögen die Schuld? Wir formulieren Ihren Fall so, dass die Antwort eindeutig ist.",
           "Carried interest, acciones en vesting, distribuciones de trusts, ingresos en tres divisas: las calculadoras convencionales rechazan lo que no saben clasificar. El análisis HNW hace en cambio una sola pregunta — ¿el patrimonio global sostiene la deuda? Enmarcamos su caso para responderla con contundencia.",
           "Carried interest, részvényopciók, vagyonkezelői kifizetések, három devizában érkező jövedelem: a hagyományos kalkulátorok egyszerűen elutasítják, amit nem tudnak besorolni. A HNW-bírálat ehelyett egyetlen kérdést tesz fel — a teljes vagyon elbírja-e az adósságot? Az Ön ügyét úgy építjük fel, hogy a válasz egyértelmű legyen.")),
         [("Large loans from £1m to £25m+, arranged discreetly", "Großdarlehen von £1 Mio. bis über £25 Mio., diskret arrangiert", "Préstamos grandes de £1M a más de £25M, gestionados con discreción", "Nagy hitelek £1M-tól £25M felett, diszkréten intézve"),
          ("Private bank relationships — with and without assets under management", "Privatbank-Zugang — mit und ohne verwaltetes Vermögen", "Relaciones con banca privada — con y sin activos bajo gestión", "Privátbanki kapcsolatok — kezelt vagyonnal és anélkül is"),
          ("Interest-only with sale-of-property or investment-backed repayment", "Endfällige Darlehen mit Verkaufs- oder Investment-Rückzahlung", "Solo interés con amortización por venta o respaldada por inversiones", "Csak-kamat konstrukciók eladásból vagy befektetésből történő törlesztéssel"),
          ("Lombard-style and securities-backed structures alongside property debt", "Lombard- und wertpapierbesicherte Strukturen neben Immobilienkrediten", "Estructuras tipo lombardo respaldadas por valores junto a la deuda inmobiliaria", "Értékpapír-fedezetű, lombard jellegű struktúrák az ingatlanhitel mellett"),
          ("Prime London, country estates, listed buildings and unusual assets", "Prime London, Landsitze, denkmalgeschützte und besondere Objekte", "Prime London, fincas rurales, edificios protegidos y activos singulares", "Prime London, vidéki birtokok, műemlék épületek és különleges ingatlanok")]),
        ((("Discretion as standard", "Diskretion als Standard", "Discreción como estándar", "Diszkréció alapfelszereltségként"),
          ("Our clients rarely want their affairs circulated across a dozen lending desks. We approach a shortlist — typically two or three institutions matched to the case — under strict confidentiality, and negotiate terms in parallel.",
           "Unsere Kunden möchten ihre Verhältnisse selten über ein Dutzend Kreditabteilungen gestreut sehen. Wir kontaktieren eine Shortlist — meist zwei bis drei passende Institute — unter strikter Vertraulichkeit und verhandeln parallel.",
           "Nuestros clientes rara vez quieren que sus asuntos circulen por una docena de mesas de crédito. Contactamos una lista corta — normalmente dos o tres instituciones adecuadas al caso — bajo estricta confidencialidad, y negociamos en paralelo.",
           "Ügyfeleink ritkán szeretnék, ha ügyeik tucatnyi hitelezési osztályon keringenének. Egy rövid listát keresünk meg — jellemzően két-három, az ügyhöz illő intézményt — szigorú titoktartás mellett, és párhuzamosan tárgyalunk."),
          ("Where a private bank expects assets under management as the price of admission, we quantify that trade-off honestly against specialist lenders who ask for nothing but the deal. The cheapest headline rate is not always the cheapest arrangement.",
           "Wo eine Privatbank verwaltetes Vermögen als Eintrittspreis erwartet, quantifizieren wir diesen Trade-off ehrlich gegen Spezialbanken, die nichts außer dem Geschäft verlangen. Der günstigste Zins ist nicht immer die günstigste Struktur.",
           "Cuando una banca privada exige activos bajo gestión como precio de entrada, cuantificamos ese coste honestamente frente a bancos especializados que no piden nada más que la operación. El tipo más barato no siempre es el acuerdo más barato.",
           "Ahol egy privátbank kezelt vagyont vár el a belépő árán, ott ezt az árat őszintén összevetjük a specialista bankokkal, amelyek semmit sem kérnek az ügyleten kívül. A legalacsonyabb kamat nem mindig a legolcsóbb konstrukció."))),
        [((("What counts as a high-net-worth exemption?", "Was gilt als High-Net-Worth-Ausnahme?", "¿Qué es la exención para grandes patrimonios?", "Mi számít HNW-mentességnek?")),
          (("UK rules allow tailored underwriting for clients with £300k+ annual net income or £3m+ in net assets. It gives lenders freedom to structure around wealth rather than payslips — used properly, it unlocks terms unavailable elsewhere.",
            "Britische Regeln erlauben maßgeschneidertes Underwriting ab £300k Jahresnettoeinkommen oder £3 Mio. Nettovermögen. Das gibt Banken Freiheit, um Vermögen statt Gehaltszettel zu strukturieren — richtig genutzt, eröffnet es anderswo unerreichbare Konditionen.",
            "Las normas británicas permiten un análisis a medida para clientes con más de £300k de ingresos netos anuales o £3M en activos netos. Da a los bancos libertad para estructurar en torno al patrimonio y no a las nóminas — bien usada, desbloquea condiciones inalcanzables por otra vía.",
            "A brit szabályok egyedi bírálatot engednek £300k feletti éves nettó jövedelem vagy £3M feletti nettó vagyon esetén. Ez szabadságot ad a bankoknak, hogy a vagyonra és ne a fizetési papírokra építsenek — jól használva máshol elérhetetlen feltételeket nyit meg."))),
         ((("Do private banks require moving my investments?", "Verlangen Privatbanken die Übertragung meiner Anlagen?", "¿La banca privada exige trasladar mis inversiones?", "A privátbankok megkövetelik a befektetéseim áthozását?")),
          (("Some do, some don't, and some negotiate. AUM requirements range from none to 50%+ of the loan. We compare the whole cost of each relationship — rate, fees and tied assets — so the decision is financial, not emotional.",
            "Manche ja, manche nein, manche verhandeln. AUM-Anforderungen reichen von null bis über 50% der Darlehenssumme. Wir vergleichen die Gesamtkosten jeder Beziehung — Zins, Gebühren, gebundene Anlagen — damit die Entscheidung finanziell fällt, nicht emotional.",
            "Algunas sí, otras no, y otras negocian. Los requisitos de activos van desde cero hasta más del 50% del préstamo. Comparamos el coste total de cada relación — tipo, comisiones y activos vinculados — para que la decisión sea financiera, no emocional.",
            "Van, amelyik igen, van, amelyik nem, és van, amelyik tárgyal. Az elvárt kezelt vagyon nullától a hitelösszeg 50%-a fölé is terjedhet. Minden kapcsolat teljes költségét összevetjük — kamat, díjak, lekötött eszközök —, hogy a döntés pénzügyi legyen, ne érzelmi."))),
         ((("Can property income alone support a large loan?", "Können Mieteinnahmen allein ein Großdarlehen tragen?", "¿Los ingresos por alquiler pueden sostener un préstamo grande?", "Elbír-e egy nagy hitelt pusztán az ingatlanjövedelem?")),
          (("Frequently, yes — particularly where a portfolio produces stable six-figure rental profit. Lenders will stress-test the income, but professional landlords with clean books borrow at this level routinely. Presentation, again, decides the outcome.",
            "Häufig ja — besonders wenn ein Portfolio stabile sechsstellige Mietgewinne erzielt. Banken führen Stresstests durch, aber professionelle Vermieter mit sauberen Büchern leihen routinemäßig auf diesem Niveau. Auch hier entscheidet die Präsentation.",
            "Con frecuencia sí — sobre todo cuando una cartera genera beneficios de alquiler estables de seis cifras. Los bancos aplicarán pruebas de estrés, pero los arrendadores profesionales con cuentas limpias piden prestado a este nivel de forma rutinaria. La presentación, otra vez, decide el resultado.",
            "Gyakran igen — különösen ha a portfólió stabil, hat számjegyű bérleti nyereséget termel. A bankok stressztesztelik a jövedelmet, de a rendezett könyvelésű profi bérbeadók rutinszerűen hiteleznek ezen a szinten. A kimenetelt itt is a bemutatás dönti el.")))],
        ("Complex wealth. Uncomplicated process.", "Komplexes Vermögen. Unkomplizierter Prozess.", "Patrimonio complejo. Proceso sencillo.", "Összetett vagyon. Egyszerű folyamat.",
         "One confidential conversation to understand the full picture. Then a shortlist, negotiated terms and a single recommendation.",
         "Ein vertrauliches Gespräch für das Gesamtbild. Danach eine Shortlist, verhandelte Konditionen und eine klare Empfehlung.",
         "Una conversación confidencial para entender el panorama completo. Después, una lista corta, condiciones negociadas y una única recomendación.",
         "Egy bizalmas beszélgetés a teljes kép megértéséhez. Utána rövid lista, kitárgyalt feltételek és egyetlen, egyértelmű ajánlás."))

    build_service(
        "remortgage", "svc-remortgage.jpg",
        "Remortgage & Refinance Advice UK | Agnes Mortgage",
        "Remortgage advice across the UK — rate switches, capital raising, debt consolidation and portfolio refinancing, timed before your fixed rate ends.",
        ("Remortgage & Refinance", "Umschuldung & Refinanzierung", "Rehipoteca y refinanciación", "Hitelkiváltás és refinanszírozás"),
        ("The most expensive mortgage in Britain is the one nobody reviewed. We track your deal, model the market and move you at precisely the right moment.",
         "Die teuerste Hypothek Großbritanniens ist die, die niemand überprüft hat. Wir überwachen Ihre Konditionen, modellieren den Markt und handeln im exakt richtigen Moment.",
         "La hipoteca más cara del Reino Unido es la que nadie revisó. Seguimos su préstamo, modelamos el mercado y actuamos en el momento exacto.",
         "A legdrágább brit jelzáloghitel az, amelyet senki sem vizsgált felül. Figyeljük a konstrukcióját, modellezzük a piacot, és pontosan a megfelelő pillanatban lépünk."),
        ((("Timing is the whole game", "Timing ist das ganze Spiel", "El momento lo es todo", "Az időzítés a lényeg"),
          ("A remortgage can be secured up to six months before your current deal ends — and repriced downwards if rates fall before completion. Starting early costs nothing and removes every risk of drifting onto the standard variable rate.",
           "Eine Umschuldung lässt sich bis zu sechs Monate vor Ablauf sichern — und wird bei fallenden Zinsen vor Abschluss nachgebessert. Ein früher Start kostet nichts und beseitigt jedes Risiko, in den teuren Standardzins zu rutschen.",
           "Una rehipoteca puede asegurarse hasta seis meses antes de que termine su contrato actual — y ajustarse a la baja si los tipos caen antes del cierre. Empezar pronto no cuesta nada y elimina el riesgo de caer en el tipo variable estándar.",
           "A hitelkiváltás akár hat hónappal a jelenlegi konstrukció lejárta előtt rögzíthető — és ha a kamatok a zárás előtt csökkennek, újraárazható. A korai indulás semmibe sem kerül, és megszünteti a drága változó kamatra sodródás minden kockázatát.")),
         [("Rate-switch and full remortgage compared side by side, with all fees", "Produktwechsel und Vollumschuldung im direkten Vergleich, inkl. aller Gebühren", "Cambio de producto y rehipoteca completa comparados con todas las comisiones", "Kamatváltás és teljes kiváltás összevetve, minden díjjal együtt"),
          ("Capital raising for improvements, investments or the next deposit", "Kapitalfreisetzung für Umbauten, Investments oder die nächste Anzahlung", "Liberación de capital para reformas, inversiones o la próxima entrada", "Tőkekivonás felújításra, befektetésre vagy a következő önerőre"),
          ("Debt consolidation modelled honestly — total cost, not just monthly relief", "Umschuldung von Verbindlichkeiten ehrlich gerechnet — Gesamtkosten, nicht nur Monatsrate", "Consolidación de deudas calculada con honestidad — coste total, no solo alivio mensual", "Adósságrendezés őszintén modellezve — teljes költség, nem csak havi könnyebbség"),
          ("Portfolio-wide refinancing sequenced across multiple expiry dates", "Portfolioweite Refinanzierung über mehrere Zinsbindungsenden hinweg", "Refinanciación de cartera secuenciada entre varios vencimientos", "Portfóliószintű refinanszírozás több lejárati dátumra ütemezve"),
          ("Product transfer negotiation with your existing lender when staying wins", "Verhandlung des Produktwechsels bei Ihrer Bank, wenn Bleiben gewinnt", "Negociación del cambio de producto con su banco actual cuando quedarse es mejor", "Termékváltás kitárgyalása a jelenlegi bankjánál, ha a maradás éri meg")]),
        ((("More than a cheaper rate", "Mehr als ein günstigerer Zins", "Más que un tipo más barato", "Több, mint olcsóbb kamat"),
          ("A remortgage is the moment to redesign the debt itself: shorten the term while payments are manageable, split the loan into fixed and flexible parts, add offset features against business cash, or release equity for the next acquisition.",
           "Die Umschuldung ist der Moment, die Schuld selbst neu zu gestalten: Laufzeit verkürzen, das Darlehen in fixe und flexible Teile aufteilen, Offset-Funktionen gegen Firmenliquidität einbauen oder Eigenkapital für den nächsten Kauf freisetzen.",
           "La rehipoteca es el momento de rediseñar la deuda misma: acortar el plazo mientras las cuotas son manejables, dividir el préstamo en partes fijas y flexibles, añadir cuentas offset contra la tesorería del negocio o liberar capital para la próxima adquisición.",
           "A hitelkiváltás a pillanat, amikor magát az adósságot lehet újratervezni: futamidő-rövidítés, a hitel fix és rugalmas részekre bontása, offset funkció a céges készpénz ellenében, vagy tőke felszabadítása a következő vásárláshoz."),
          ("For landlords, we sequence expiry dates deliberately so the whole portfolio never reprices in the same market moment — the refinancing equivalent of not betting everything on one card.",
           "Für Vermieter staffeln wir Zinsbindungsenden bewusst, damit nie das gesamte Portfolio im selben Marktmoment neu bepreist wird — das Refinanzierungs-Äquivalent dazu, nicht alles auf eine Karte zu setzen.",
           "Para los arrendadores, escalonamos los vencimientos deliberadamente para que toda la cartera nunca se reprecie en el mismo momento de mercado — el equivalente en refinanciación a no apostarlo todo a una carta.",
           "Bérbeadóknál a lejáratokat tudatosan lépcsőzzük, hogy a teljes portfólió soha ne ugyanabban a piaci pillanatban árazódjon újra — a refinanszírozás megfelelője annak, hogy nem teszünk fel mindent egy lapra."))),
        [((("When should I start my remortgage?", "Wann sollte ich mit der Umschuldung beginnen?", "¿Cuándo debo iniciar mi rehipoteca?", "Mikor kezdjem a hitelkiváltást?")),
          (("Six months before your current deal ends. Offers last around six months, so you lock protection immediately and still benefit if pricing improves — we re-broker automatically before completion whenever rates move in your favour.",
            "Sechs Monate vor Ablauf Ihrer aktuellen Kondition. Angebote gelten rund sechs Monate — Sie sichern sofort Schutz und profitieren trotzdem, wenn die Preise fallen: Wir vermitteln vor Abschluss automatisch neu, sobald sich Zinsen zu Ihren Gunsten bewegen.",
            "Seis meses antes de que termine su contrato actual. Las ofertas duran unos seis meses, así que asegura protección de inmediato y aún se beneficia si los precios mejoran — renegociamos automáticamente antes del cierre siempre que los tipos se muevan a su favor.",
            "Hat hónappal a jelenlegi konstrukció lejárta előtt. Az ajánlatok kb. hat hónapig érvényesek, így azonnal védelmet rögzít, és mégis nyer, ha az árazás javul — a zárás előtt automatikusan újratárgyalunk, amint a kamatok az Ön javára mozdulnak."))),
         ((("Is a product transfer with my current lender easier?", "Ist ein Produktwechsel bei meiner Bank einfacher?", "¿Es más fácil un cambio de producto con mi banco actual?", "Egyszerűbb a termékváltás a jelenlegi bankomnál?")),
          (("Easier, yes — best, only sometimes. Transfers skip valuation and legals but hide the market comparison. We price both routes every time; when your existing lender genuinely wins, we'll say so and arrange it.",
            "Einfacher ja — am besten nur manchmal. Wechsel sparen Bewertung und Anwälte, verbergen aber den Marktvergleich. Wir rechnen jedes Mal beide Wege; wenn Ihre Bank wirklich gewinnt, sagen wir es und arrangieren den Wechsel.",
            "Más fácil, sí — mejor, solo a veces. Los cambios evitan tasación y trámites legales pero ocultan la comparación de mercado. Calculamos ambas vías siempre; cuando su banco actual gana de verdad, se lo diremos y lo gestionaremos.",
            "Egyszerűbb, igen — a legjobb csak néha. A termékváltás megspórolja az értékbecslést és az ügyvédi részt, de elrejti a piaci összehasonlítást. Mindig mindkét utat beárazzuk; ha a jelenlegi bankja tényleg nyer, megmondjuk, és azt intézzük."))),
         ((("Can I remortgage to buy another property?", "Kann ich umschulden, um eine weitere Immobilie zu kaufen?", "¿Puedo rehipotecar para comprar otra propiedad?", "Kiválthatom a hitelt egy újabb ingatlan vásárlásához?")),
          (("It's one of the most common strategies we arrange: release equity from your home or portfolio at residential-level rates and deploy it as the deposit on the next purchase. Done properly, the numbers on both loans are agreed as one plan.",
            "Eine der häufigsten Strategien, die wir umsetzen: Eigenkapital aus Haus oder Portfolio zu Wohnkredit-Konditionen freisetzen und als Anzahlung für den nächsten Kauf einsetzen. Richtig gemacht, werden beide Darlehen als ein Plan vereinbart.",
            "Es una de las estrategias más comunes que gestionamos: liberar capital de su vivienda o cartera a tipos residenciales y usarlo como entrada de la siguiente compra. Bien hecho, los números de ambos préstamos se acuerdan como un solo plan.",
            "Az egyik leggyakoribb stratégia, amit intézünk: tőke felszabadítása a lakásból vagy portfólióból lakossági szintű kamaton, majd önerőként bevetése a következő vásárlásnál. Jól csinálva a két hitel számai egyetlen tervként dőlnek el.")))],
        ("Your fixed rate has an expiry date. Your plan should too.", "Ihre Zinsbindung hat ein Ablaufdatum. Ihr Plan sollte auch eins haben.", "Su tipo fijo tiene fecha de caducidad. Su plan también debería.", "A fix kamatának lejárati dátuma van. Legyen a tervének is.",
         "Tell us when your current deal ends and we'll build the timeline backwards from that day — starting now.",
         "Sagen Sie uns, wann Ihre Kondition ausläuft, und wir planen die Timeline von diesem Tag rückwärts — ab sofort.",
         "Díganos cuándo termina su contrato actual y construiremos el calendario hacia atrás desde ese día — empezando hoy.",
         "Mondja meg, mikor jár le a jelenlegi konstrukciója, és attól a naptól visszafelé építjük fel az ütemtervet — már ma."))
