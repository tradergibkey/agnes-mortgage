# -*- coding: utf-8 -*-
"""Agnes Mortgage site generator — shared chrome. Build tool only, not shipped."""
import html as _html

BASE = "https://agnes-mortgage.vercel.app"
PHONE_DISP = "+44 7700 900123"          # Ofcom-reserved fictional number — SWAP AT GO-LIVE
PHONE_TEL = "+447700900123"
WA = "https://wa.me/447700900123"

def esc(s):
    return _html.escape(s, quote=True)

def t(tag, en, de, es, hu, cls="", attrs=""):
    """Element carrying all 4 translations as data attributes; EN inline."""
    c = f' class="{cls}"' if cls else ""
    a = f" {attrs}" if attrs else ""
    return (f'<{tag}{c}{a} data-en="{esc(en)}" data-de="{esc(de)}" '
            f'data-es="{esc(es)}" data-hu="{esc(hu)}">{en}</{tag}>')

def tp(en, de, es, hu):
    """Placeholder attribute set for form inputs."""
    return (f'data-en-ph="{esc(en)}" data-de-ph="{esc(de)}" '
            f'data-es-ph="{esc(es)}" data-hu-ph="{esc(hu)}" placeholder="{esc(en)}"')

FLAGS = {
    "en": '<svg class="flag" viewBox="0 0 60 42"><rect width="60" height="42" fill="#012169"/><path d="M0,0 60,42 M60,0 0,42" stroke="#fff" stroke-width="8"/><path d="M0,0 60,42 M60,0 0,42" stroke="#C8102E" stroke-width="4"/><path d="M30,0 V42 M0,21 H60" stroke="#fff" stroke-width="12"/><path d="M30,0 V42 M0,21 H60" stroke="#C8102E" stroke-width="7"/></svg>',
    "de": '<svg class="flag" viewBox="0 0 60 42"><rect width="60" height="14" fill="#000"/><rect y="14" width="60" height="14" fill="#DD0000"/><rect y="28" width="60" height="14" fill="#FFCE00"/></svg>',
    "es": '<svg class="flag" viewBox="0 0 60 42"><rect width="60" height="42" fill="#AA151B"/><rect y="10.5" width="60" height="21" fill="#F1BF00"/></svg>',
    "hu": '<svg class="flag" viewBox="0 0 60 42"><rect width="60" height="14" fill="#CE2939"/><rect y="14" width="60" height="14" fill="#fff"/><rect y="28" width="60" height="14" fill="#477050"/></svg>',
}

ICON = {
    "chev": '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>',
    "check": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>',
    "plus": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M12 5v14M5 12h14"/></svg>',
    "arrow": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>',
    "shield": '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
    "phone": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
    "wa": '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/></svg>',
    "pin": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "clock": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
}

def head(title, desc, slug, og_img="/img/og-cover.jpg", jsonld=""):
    canonical = BASE + (("/" + slug) if slug else "")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{BASE}{og_img}">
<meta property="og:site_name" content="Agnes Mortgage">
<meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="GB">
<meta name="geo.placename" content="United Kingdom">
<link rel="icon" type="image/png" sizes="32x32" href="/img/favicon-32.png">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" onload="this.onload=null;this.rel='stylesheet'">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" media="print" onload="this.media='all'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap"></noscript>
<link rel="stylesheet" href="/css/styles.css">
{jsonld}
</head>
<body>
"""

def lang_gate():
    return f"""<div class="lang-gate hidden" id="langGate">
  <div class="lang-gate-card">
    <div class="brand" style="justify-content:center"><span class="brand-mark">AM</span><span>Agnes Mortgage</span></div>
    <h2>Welcome · Willkommen · Bienvenido · Üdvözöljük</h2>
    <p>Please choose your language / Bitte wählen Sie Ihre Sprache / Elija su idioma / Kérjük, válasszon nyelvet</p>
    <div class="lang-gate-grid">
      <button data-lang="en">{FLAGS['en']} English</button>
      <button data-lang="de">{FLAGS['de']} Deutsch</button>
      <button data-lang="es">{FLAGS['es']} Español</button>
      <button data-lang="hu">{FLAGS['hu']} Magyar</button>
    </div>
  </div>
</div>
"""

NAV_ITEMS = [
    ("buy-to-let", ("Buy-to-Let & Portfolio", "Buy-to-Let & Portfolio", "Buy-to-Let y carteras", "Buy-to-let és portfólió")),
    ("hmo-finance", ("HMO & Multi-Unit", "HMO & Mehrfamilienobjekte", "HMO y multiunidad", "HMO és többlakásos")),
    ("expat-mortgages", ("Expat & Overseas", "Expats & Auslandskunden", "Expatriados y no residentes", "Külföldön élők")),
    ("self-employed", ("Directors & Self-Employed", "Unternehmer & Selbständige", "Directores y autónomos", "Cégvezetők és vállalkozók")),
    ("high-net-worth", ("High-Net-Worth & Large Loans", "Vermögende Kunden & Großdarlehen", "Grandes patrimonios y préstamos", "Nagy vagyon és nagy hitelek")),
    ("remortgage", ("Remortgage & Refinance", "Umschuldung & Refinanzierung", "Rehipoteca y refinanciación", "Hitelkiváltás és refinanszírozás")),
]

def header(active=""):
    drop = "\n".join(
        t("a", *names, attrs=f'href="/{slug}"' + (' class="active"' if active == slug else ""))
        for slug, names in NAV_ITEMS
    )
    def nav_a(href, key, en, de, es, hu):
        cls = ' class="active"' if active == key else ""
        return f'<a href="{href}"{cls} data-en="{esc(en)}" data-de="{esc(de)}" data-es="{esc(es)}" data-hu="{esc(hu)}">{en}</a>'
    return f"""<header class="site-header">
  <div class="header-inner">
    <a href="/" class="brand" aria-label="Agnes Mortgage — home">
      <span class="brand-mark">AM</span>
      <span>Agnes Mortgage<small data-en="Private mortgage advisory" data-de="Private Hypothekenberatung" data-es="Asesoría hipotecaria privada" data-hu="Privát jelzálog-tanácsadás">Private mortgage advisory</small></span>
    </a>
    <nav aria-label="Main">
      <ul class="main-nav">
        <li>{nav_a("/", "home", "Home", "Start", "Inicio", "Kezdőlap")}</li>
        <li class="nav-item-drop">
          <button class="drop-toggle" type="button"><span data-en="Services" data-de="Leistungen" data-es="Servicios" data-hu="Szolgáltatások">Services</span>{ICON['chev']}</button>
          <div class="nav-drop">
{drop}
          </div>
        </li>
        <li>{nav_a("/about", "about", "Meet Agnes", "Über Agnes", "Conozca a Agnes", "Ismerje meg Agnest")}</li>
        <li>{nav_a("/blog", "blog", "Insights", "Insights", "Blog", "Blog")}</li>
        <li>{nav_a("/#contact", "contact", "Contact", "Kontakt", "Contacto", "Kapcsolat")}</li>
      </ul>
    </nav>
    <div class="header-cta">
      <div class="lang-switch">
        <button class="lang-btn" type="button">{FLAGS['en'].replace('class="flag"','class="flag lang-flag"')}<span class="lang-label">EN</span>{ICON['chev']}</button>
        <div class="lang-menu">
          <button data-lang="en">{FLAGS['en']} English</button>
          <button data-lang="de">{FLAGS['de']} Deutsch</button>
          <button data-lang="es">{FLAGS['es']} Español</button>
          <button data-lang="hu">{FLAGS['hu']} Magyar</button>
        </div>
      </div>
      <a href="tel:{PHONE_TEL}" class="btn btn-primary btn-sm">{ICON['phone']}<span data-en="Book a call" data-de="Gespräch buchen" data-es="Reservar llamada" data-hu="Hívás foglalása">Book a call</span></a>
      <button class="nav-burger" type="button" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
"""

def footer():
    svc_links = "\n".join(
        "<li>" + t("a", *names, attrs=f'href="/{slug}"') + "</li>"
        for slug, names in NAV_ITEMS
    )
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-brand"><span class="brand-mark">AM</span> Agnes Mortgage</div>
        {t("p", "Private mortgage advisory for business owners, portfolio landlords, high-net-worth clients and expats — serving the whole United Kingdom.",
           "Private Hypothekenberatung für Unternehmer, Portfolio-Vermieter, vermögende Kunden und Expats — im gesamten Vereinigten Königreich.",
           "Asesoría hipotecaria privada para empresarios, propietarios de carteras, grandes patrimonios y expatriados — en todo el Reino Unido.",
           "Privát jelzálog-tanácsadás cégtulajdonosoknak, portfólióval rendelkező bérbeadóknak, nagy vagyonú ügyfeleknek és külföldön élőknek — az egész Egyesült Királyságban.")}
      </div>
      <div>
        {t("p", "Services", "Leistungen", "Servicios", "Szolgáltatások", cls="footer-title")}
        <ul>
{svc_links}
        </ul>
      </div>
      <div>
        {t("p", "Company", "Unternehmen", "Empresa", "Cégünk", cls="footer-title")}
        <ul>
          <li>{t("a", "Meet Agnes", "Über Agnes", "Conozca a Agnes", "Ismerje meg Agnest", attrs='href="/about"')}</li>
          <li>{t("a", "Insights & guides", "Insights & Ratgeber", "Blog y guías", "Blog és útmutatók", attrs='href="/blog"')}</li>
          <li>{t("a", "Contact", "Kontakt", "Contacto", "Kapcsolat", attrs='href="/#contact"')}</li>
        </ul>
      </div>
      <div>
        {t("p", "Legal", "Rechtliches", "Legal", "Jogi", cls="footer-title")}
        <ul>
          <li>{t("a", "Privacy policy", "Datenschutz", "Política de privacidad", "Adatvédelem", attrs='href="/privacy-policy"')}</li>
          <li>{t("a", "Terms of business", "Geschäftsbedingungen", "Términos del servicio", "Üzleti feltételek", attrs='href="/terms"')}</li>
        </ul>
      </div>
    </div>
    <div class="footer-legal">
      <p>Agnes Mortgage is a trading name of [LEGAL ENTITY NAME LTD], registered in England and Wales, company number [COMPANY NUMBER]. Registered office: [REGISTERED OFFICE ADDRESS]. [LEGAL ENTITY NAME LTD] is authorised and regulated by the Financial Conduct Authority, FCA number [FCA NUMBER]. The FCA does not regulate most buy-to-let mortgages. The guidance on this website is subject to the UK regulatory regime and is therefore targeted at consumers based in the UK. A fee may be charged for mortgage advice; the exact amount depends on your circumstances and will be agreed before any work begins.</p>
      <span class="risk">Your home may be repossessed if you do not keep up repayments on your mortgage.</span>
      <p style="margin-top:14px">© 2026 Agnes Mortgage. All rights reserved.</p>
    </div>
  </div>
</footer>
<script src="/js/scripts.js" defer></script>
</body>
</html>
"""

REVIEWS = [
    ("James W.", "Agnes restructured our five-property portfolio into a limited company arrangement that our accountant had been recommending for years. Executed flawlessly."),
    ("Charlotte H.", "As a company director with retained profits, high-street lenders simply didn't understand my income. Agnes found a lender who did — within a week."),
    ("Dr. Priya N.", "Buying in London while working in Singapore felt impossible until this firm took over. Every document, every time zone, handled."),
    ("Tamás K.", "Külföldön élő magyarként azt hittem, esélyem sincs brit jelzáloghitelre. Agnes bebizonyította az ellenkezőjét."),
    ("Oliver B.", "The HMO refinance saved us a five-figure sum annually. Sharp, discreet, and genuinely whole-of-market."),
    ("Sophie D.", "Our large loan needed private bank treatment. Agnes negotiated terms we couldn't have reached ourselves."),
    ("Markus F.", "Als deutscher Unternehmer in London war die Beratung auf Deutsch ein unbezahlbarer Vorteil. Absolut professionell."),
    ("Eleanor R.", "Remortgaged three buy-to-lets in one coordinated move before our fixed rates expired. Not a single day on the SVR."),
    ("Daniel O.", "Self-employed for two years and still got a competitive rate. The presentation of my accounts made all the difference."),
    ("Isabella M.", "Compramos nuestra primera propiedad en Manchester desde Madrid. Todo el proceso fue claro y sin sorpresas."),
    ("George T.", "Portfolio landlord with 12 units — Agnes is the first adviser who modelled the whole picture instead of one deal at a time."),
    ("Hannah L.", "Responsive at hours no bank would ever be. WhatsApp updates at every milestone of the application."),
    ("Viktor S.", "A cégem osztalékjövedelmét egyetlen nagybank sem fogadta el. Itt két hét alatt volt ajánlatom."),
    ("William P.", "Complex income, multiple currencies, offshore structure — handled with total discretion and zero drama."),
    ("Amara J.", "First HMO purchase. The lender criteria maze was terrifying alone; with Agnes it was a checklist."),
    ("Lucía G.", "Como expatriada, el trato en español me dio una confianza enorme. Recomendable al cien por cien."),
    ("Henry C.", "Our bridging-to-term exit was arranged before the bridge even completed. That's planning."),
    ("Freya A.", "Moved our entire portfolio remortgage forward six months and locked rates before the rise. Foresight you pay brokers for."),
    ("Stefan B.", "Die Finanzierung unserer Ferienimmobilie in Cornwall lief reibungslos — trotz Wohnsitz in München."),
    ("Nathan E.", "Large loan, unusual property, tight deadline. Delivered on all three."),
    ("Zsófia H.", "Vállalkozóként végre valaki, aki érti a beszámolót és a bank nyelvét is. Köszönjük!"),
    ("Grace M.", "The annual review caught a product switch that saved us £340 a month. Proactive, not reactive."),
    ("Arthur D.", "From first call to offer in 11 working days on a £1.4m purchase. Exceptional."),
]

def marquee():
    cards = "\n".join(
        f'<div class="review-card"><div class="review-stars">★★★★★</div><p>{esc(txt)}</p><b>{esc(name)}</b></div>'
        for name, txt in REVIEWS
    )
    return f"""<section class="marquee-section" aria-label="Client reviews">
  <div class="marquee-wrap">
    <div class="marquee-track">
{cards}
    </div>
  </div>
</section>
"""

def contact_section():
    return f"""<section class="section" id="contact">
  <div class="container">
    <div class="section-head reveal-item">
      {t("span", "Contact", "Kontakt", "Contacto", "Kapcsolat", cls="eyebrow")}
      {t("h2", "Start the conversation", "Beginnen wir das Gespräch", "Iniciemos la conversación", "Kezdjük el a beszélgetést")}
      {t("p", "Tell us a little about your plans and we will come back to you within one working day — by phone, email or WhatsApp, whichever you prefer.",
         "Erzählen Sie uns kurz von Ihren Plänen und wir melden uns innerhalb eines Werktags — per Telefon, E-Mail oder WhatsApp, ganz wie Sie möchten.",
         "Cuéntenos brevemente sus planes y le responderemos en un día laborable — por teléfono, correo o WhatsApp, como prefiera.",
         "Írja le röviden a terveit, és egy munkanapon belül jelentkezünk — telefonon, e-mailben vagy WhatsAppon, ahogy Önnek kényelmes.")}
    </div>
    <div class="contact-grid">
      <div class="contact-info-card reveal-item">
        {t("h3", "Speak to an adviser", "Sprechen Sie mit uns", "Hable con un asesor", "Beszéljen tanácsadóval")}
        <div class="contact-line">{ICON['phone']}<div>{t("b", "Phone", "Telefon", "Teléfono", "Telefon")}<a href="tel:{PHONE_TEL}">{PHONE_DISP}</a></div></div>
        <div class="contact-line">{ICON['clock']}<div>{t("b", "Hours", "Erreichbarkeit", "Horario", "Elérhetőség")}{t("span", "Mon–Fri 9:00–18:00 · evenings by appointment", "Mo–Fr 9:00–18:00 · abends nach Vereinbarung", "Lun–Vie 9:00–18:00 · tardes con cita", "H–P 9:00–18:00 · este egyeztetéssel")}</div></div>
        <div class="contact-line">{ICON['pin']}<div>{t("b", "Coverage", "Einzugsgebiet", "Cobertura", "Lefedettség")}{t("span", "The whole United Kingdom — in person and remote", "Das gesamte Vereinigte Königreich — persönlich und remote", "Todo el Reino Unido — presencial y en remoto", "Az egész Egyesült Királyság — személyesen és online")}</div></div>
        <a class="wa-btn" href="{WA}" target="_blank" rel="noopener">{ICON['wa']} WhatsApp</a>
      </div>
      <form class="form-card reveal-item" id="contactForm">
        <input type="hidden" name="access_key" value="YOUR_WEB3FORMS_KEY">
        <input type="hidden" name="subject" value="New enquiry — Agnes Mortgage website">
        <input type="hidden" name="from_name" value="Agnes Mortgage Website">
        <div class="hp-field"><input type="checkbox" name="botcheck" tabindex="-1" autocomplete="off"></div>
        <div class="form-grid">
          <div class="form-field">
            {t("label", "Full name *", "Vollständiger Name *", "Nombre completo *", "Teljes név *", attrs='for="cf-name"')}
            <input id="cf-name" type="text" name="name" required {tp("Your name", "Ihr Name", "Su nombre", "Az Ön neve")}>
          </div>
          <div class="form-field">
            {t("label", "Email *", "E-Mail *", "Correo electrónico *", "E-mail *", attrs='for="cf-email"')}
            <input id="cf-email" type="email" name="email" required {tp("name@example.com", "name@beispiel.de", "nombre@ejemplo.com", "nev@pelda.hu")}>
          </div>
          <div class="form-field">
            {t("label", "Phone (optional)", "Telefon (optional)", "Teléfono (opcional)", "Telefon (nem kötelező)", attrs='for="cf-phone"')}
            <input id="cf-phone" type="tel" name="phone" {tp("+44 …", "+49 …", "+34 …", "+36 …")}>
          </div>
          <div class="form-field">
            {t("label", "I am interested in *", "Ich interessiere mich für *", "Estoy interesado en *", "Ez érdekel *", attrs='for="cf-topic"')}
            <select id="cf-topic" name="topic" required>
              {t("option", "Buy-to-let / portfolio", "Buy-to-Let / Portfolio", "Buy-to-let / cartera", "Buy-to-let / portfólió", attrs='value="Buy-to-let / portfolio"')}
              {t("option", "HMO / multi-unit", "HMO / Mehrfamilienobjekt", "HMO / multiunidad", "HMO / többlakásos", attrs='value="HMO / multi-unit"')}
              {t("option", "Expat / overseas buyer", "Expat / Auslandskäufer", "Expatriado / comprador no residente", "Külföldön élő vásárló", attrs='value="Expat / overseas buyer"')}
              {t("option", "Self-employed / director", "Selbständig / Geschäftsführer", "Autónomo / director", "Vállalkozó / cégvezető", attrs='value="Self-employed / director"')}
              {t("option", "High-net-worth / large loan", "Vermögender Kunde / Großdarlehen", "Gran patrimonio / préstamo grande", "Nagy vagyon / nagy hitel", attrs='value="High-net-worth / large loan"')}
              {t("option", "Remortgage / refinance", "Umschuldung / Refinanzierung", "Rehipoteca / refinanciación", "Hitelkiváltás / refinanszírozás", attrs='value="Remortgage / refinance"')}
              {t("option", "Something else", "Etwas anderes", "Otro asunto", "Egyéb", attrs='value="Other"')}
            </select>
          </div>
          <div class="form-field full">
            {t("label", "Your message *", "Ihre Nachricht *", "Su mensaje *", "Üzenete *", attrs='for="cf-msg"')}
            <textarea id="cf-msg" name="message" rows="5" required {tp("Briefly describe your situation and goals…", "Beschreiben Sie kurz Ihre Situation und Ziele…", "Describa brevemente su situación y objetivos…", "Röviden írja le a helyzetét és céljait…")}></textarea>
          </div>
          <label class="form-consent">
            <input type="checkbox" name="gdpr_consent" value="yes" required>
            {t("span", "I consent to my data being processed to respond to this enquiry, as described in the privacy policy. *",
               "Ich willige ein, dass meine Daten zur Beantwortung dieser Anfrage gemäß der Datenschutzerklärung verarbeitet werden. *",
               "Consiento el tratamiento de mis datos para responder a esta consulta, según la política de privacidad. *",
               "Hozzájárulok adataim kezeléséhez a megkeresés megválaszolása céljából, az adatvédelmi tájékoztató szerint. *")}
          </label>
          <p class="form-status" data-ok="Thank you — we will be in touch within one working day." data-err="Something went wrong. Please try again or call us."></p>
          <div class="form-field full">
            <button type="submit" class="btn btn-gold">{t("span", "Send enquiry", "Anfrage senden", "Enviar consulta", "Üzenet küldése")} {ICON['arrow']}</button>
          </div>
        </div>
      </form>
    </div>
  </div>
</section>
"""

def cta_band(h_en, h_de, h_es, h_hu, p_en, p_de, p_es, p_hu):
    return f"""<section class="section">
  <div class="container">
    <div class="band-dark reveal-item">
      {t("h2", h_en, h_de, h_es, h_hu)}
      {t("p", p_en, p_de, p_es, p_hu)}
      <a href="/#contact" class="btn btn-gold">{t("span", "Request a private consultation", "Private Beratung anfragen", "Solicitar una consulta privada", "Privát konzultáció kérése")} {ICON['arrow']}</a>
    </div>
  </div>
</section>
"""

def breadcrumb(name_en, name_de, name_es, name_hu, slug):
    jsonld = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
{{"@type":"ListItem","position":1,"name":"Home","item":"{BASE}"}},
{{"@type":"ListItem","position":2,"name":"{name_en}","item":"{BASE}/{slug}"}}]}}
</script>"""
    crumb = f"""<div class="breadcrumb">{t("a", "Home", "Start", "Inicio", "Kezdőlap", attrs='href="/"')}<span>›</span>{t("span", name_en, name_de, name_es, name_hu)}</div>"""
    return jsonld, crumb
