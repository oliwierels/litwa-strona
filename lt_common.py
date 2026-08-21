# -*- coding: utf-8 -*-
"""Bendri 33bots.lt puslapių komponentai: <head>, navigacija, poraštė, forma, schema.org."""

SITE = "https://33bots.lt"
BRAND = "33bots"
EMAIL = "kontakt@33bots.pl"
PHONE_1 = "+48531408004"
PHONE_1_H = "+48 531 408 004"
PHONE_2 = "+48601499947"
PHONE_2_H = "+48 601 499 947"
GTM = "GTM-MR7R7CJ3"
CSS_V = "1"

SOCIALS = [
    ("Instagram", "https://www.instagram.com/33bots_/"),
    ("TikTok", "https://www.tiktok.com/@aimforum"),
    ("Facebook", "https://www.facebook.com/33bots"),
    ("LinkedIn", "https://www.linkedin.com/company/33bots"),
]

# Kalbų versijos — hreflang.
# Nurodomos tik tos versijos, kurios turi tikrą atitikmenį ir gali nurodyti atgal
# (hreflang veikia tik tada, kai nuorodos abipusės). Puslapiams be atitikmens
# paliekama tik savoji „lt“ nuoroda.
EQUIVALENTS = {
    "index.html": {
        "pl": "https://33bots.pl/",
        "de-AT": "https://33bots.at/",
        "de": "https://robotollern.de/",
        "x-default": "https://33bots.pl/",
    },
    "humanoidinio-roboto-nuoma.html": {
        "pl": "https://33bots.pl/wypozyczenie-robota.html",
        "x-default": "https://33bots.pl/wypozyczenie-robota.html",
    },
    "robotas-renginiui.html": {
        "pl": "https://33bots.pl/robot-na-event.html",
        "x-default": "https://33bots.pl/robot-na-event.html",
    },
    "robotas-parodoms.html": {
        "pl": "https://33bots.pl/oferta-targi.html",
        "x-default": "https://33bots.pl/oferta-targi.html",
    },
    "robotas-konferencijai.html": {
        "pl": "https://33bots.pl/oferta-konferencje.html",
        "x-default": "https://33bots.pl/oferta-konferencje.html",
    },
    "robotas-vestuvems.html": {
        "pl": "https://33bots.pl/robot-na-wesele.html",
        "x-default": "https://33bots.pl/robot-na-wesele.html",
    },
    "video-realizacijos.html": {
        "pl": "https://33bots.pl/realizacje-wideo.html",
        "x-default": "https://33bots.pl/realizacje-wideo.html",
    },
    "blog.html": {
        "pl": "https://33bots.pl/blog.html",
        "x-default": "https://33bots.pl/blog.html",
    },
}


def alternates(slug):
    """Grąžina (hreflang, url) porų sąrašą konkrečiam puslapiui."""
    page = slug or "index.html"
    self_url = f"{SITE}/" if page == "index.html" else f"{SITE}/{page}"
    pairs = [("lt", self_url)]
    for lang, url in EQUIVALENTS.get(page, {}).items():
        pairs.append((lang, url))
    if not any(lang == "x-default" for lang, _ in pairs):
        pairs.append(("x-default", self_url))
    return pairs


CRITICAL_CSS = (
    ":root{--bg:#000;--surface-2:#111;--text:#fff;--text-2:#a8a8a8;--text-3:#444;"
    "--border-mid:#2c2c2c;--s4:20px;--s5:28px;--s8:64px}"
    "*{box-sizing:border-box}"
    "body{margin:0;background:#000;color:#fff;"
    "font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;"
    "-webkit-font-smoothing:antialiased}"
    ".nav{position:fixed;top:0;left:0;right:0;z-index:100}"
    ".nav__inner{max-width:1200px;margin:0 auto;padding:0 var(--s4);height:var(--s8);"
    "display:flex;align-items:center;justify-content:space-between;gap:var(--s4)}"
    ".logo{font-size:1.15rem;font-weight:800;letter-spacing:-.02em;color:#fff;text-decoration:none}"
    ".hero{display:grid;grid-template-columns:1fr 1fr;align-items:center;"
    "max-width:1200px;margin:0 auto;padding:0 var(--s4);min-height:100svh}"
    ".hero__content{padding:var(--s8) 0}"
    ".hero__eyebrow{font-size:.7rem;font-weight:700;letter-spacing:.14em;"
    "text-transform:uppercase;color:var(--text-3);margin:0 0 var(--s4)}"
    ".hero__title{font-size:clamp(2.2rem,8vw,6.5rem);font-weight:800;line-height:.96;"
    "letter-spacing:-.03em;margin:0 0 var(--s4)}"
    ".hero__title em{font-style:normal;color:var(--text-2)}"
    ".hero__sub{font-size:.975rem;line-height:1.7;color:var(--text-2);margin:0 0 var(--s5)}"
    ".hero__robot-img{width:100%;height:auto;display:block}"
    "@media(max-width:900px){.nav__links,.lang-switch{display:none}}"
    "@media(max-width:768px){.hero{grid-template-columns:1fr;min-height:auto}}"
)

NAV_OFFER = [
    ("humanoidinio-roboto-nuoma.html", "Humanoidinio roboto nuoma"),
    ("robotas-renginiui.html", "Robotas renginiui"),
    ("robotas-parodoms.html", "Robotas parodoms"),
    ("robotas-konferencijai.html", "Konferencijos ir gala vakarai"),
    ("robotas-imones-sventei.html", "Įmonės šventės"),
    ("robotas-atidarymui.html", "Atidarymai ir pristatymai"),
    ("robotas-vestuvems.html", "Robotas vestuvėms"),
    ("robotas-gimtadieniui.html", "Robotas gimtadieniui"),
    ("robotas-komandos-formavimui.html", "Komandos formavimas"),
    ("robotas-prekybos-centrui.html", "Prekybos centrai"),
    ("robotas-mokyklai.html", "Mokykloms ir universitetams"),
    ("robotas-sporto-renginiui.html", "Sporto renginiai"),
    ("robotas-kaledinei-sventei.html", "Kalėdinės šventės"),
    ("robotas-fotosesijai.html", "Fotosesijos ir filmavimai"),
    ("unitree-g1-nuoma.html", "Unitree G1 nuoma"),
    ("pramogos-renginiams.html", "Pramogos renginiams"),
]

# Viršutinėje juostoje laikome tik 5 punktus — daugiau nebetelpa vienoje eilutėje.
# „Vaizdo įrašai" ir „Apie mus" pasiekiami iš poraštės ir vidinių nuorodų.
NAV_MAIN = [
    ("robotu-nuoma.html", "Miestai"),
    ("galerija.html", "Galerija"),
    ("kainos.html", "Kainos"),
    ("blog.html", "Blogas"),
    ("kontaktai.html", "Kontaktai"),
]

# Mobiliajame meniu ir poraštėje rodome visus punktus
NAV_SECONDARY = [
    ("video-realizacijos.html", "Vaizdo įrašai"),
    ("apie-mus.html", "Apie mus"),
]

CITIES = [
    ("vilnius", "Vilnius", "Vilniuje", "Vilniaus"),
    ("kaunas", "Kaunas", "Kaune", "Kauno"),
    ("klaipeda", "Klaipėda", "Klaipėdoje", "Klaipėdos"),
    ("siauliai", "Šiauliai", "Šiauliuose", "Šiaulių"),
    ("panevezys", "Panevėžys", "Panevėžyje", "Panevėžio"),
    ("alytus", "Alytus", "Alytuje", "Alytaus"),
    ("marijampole", "Marijampolė", "Marijampolėje", "Marijampolės"),
    ("mazeikiai", "Mažeikiai", "Mažeikiuose", "Mažeikių"),
    ("jonava", "Jonava", "Jonavoje", "Jonavos"),
    ("utena", "Utena", "Utenoje", "Utenos"),
    ("kedainiai", "Kėdainiai", "Kėdainiuose", "Kėdainių"),
    ("telsiai", "Telšiai", "Telšiuose", "Telšių"),
    ("taurage", "Tauragė", "Tauragėje", "Tauragės"),
    ("palanga", "Palanga", "Palangoje", "Palangos"),
    ("druskininkai", "Druskininkai", "Druskininkuose", "Druskininkų"),
    ("trakai", "Trakai", "Trakuose", "Trakų"),
    ("visaginas", "Visaginas", "Visagine", "Visagino"),
    ("ukmerge", "Ukmergė", "Ukmergėje", "Ukmergės"),
    ("plunge", "Plungė", "Plungėje", "Plungės"),
    ("kretinga", "Kretinga", "Kretingoje", "Kretingos"),
    ("silute", "Šilutė", "Šilutėje", "Šilutės"),
    ("radviliskis", "Radviliškis", "Radviliškyje", "Radviliškio"),
    ("birstonas", "Birštonas", "Birštone", "Birštono"),
    ("elektrenai", "Elektrėnai", "Elektrėnuose", "Elektrėnų"),
    ("anyksciai", "Anykščiai", "Anykščiuose", "Anykščių"),
    ("birzai", "Biržai", "Biržuose", "Biržų"),
    ("rokiskis", "Rokiškis", "Rokiškyje", "Rokiškio"),
    ("prienai", "Prienai", "Prienuose", "Prienų"),
]


def city_url(slug):
    return f"robotu-nuoma-{slug}.html"


def esc(text):
    return (text.replace("&", "&amp;").replace("<", "&lt;")
                .replace(">", "&gt;").replace('"', "&quot;"))


def head(*, title, description, slug, keywords="", og_image=None, og_type="website",
         extra_ld=(), extra_head="", preload_hero=False, article_meta=None):
    """Sugeneruoja pilną <head> bloką su meta, OG, hreflang ir JSON-LD."""
    canonical = f"{SITE}/" if slug in ("", "index.html") else f"{SITE}/{slug}"
    image = og_image or f"{SITE}/og-image.jpg"

    hreflang = "\n".join(
        f'  <link rel="alternate" hreflang="{lang}" href="{href}" />'
        for lang, href in alternates(slug)
    )

    ld_blocks = "\n".join(
        f'  <script type="application/ld+json">\n{block}\n  </script>' for block in extra_ld
    )

    art = ""
    if article_meta:
        art = f"""
  <meta property="article:published_time" content="{article_meta['published']}" />
  <meta property="article:modified_time" content="{article_meta['modified']}" />
  <meta property="article:section" content="{esc(article_meta['section'])}" />"""

    preload = ""
    if preload_hero:
        preload = ('\n  <link rel="preload" as="image" href="robot-g1-960.webp" '
                   'imagesrcset="robot-g1-960.webp 960w, robot-g1.webp 2390w" imagesizes="45vw" '
                   'fetchpriority="high" type="image/webp" media="(min-width: 769px)" />')

    kw = f'\n  <meta name="keywords" content="{esc(keywords)}" />' if keywords else ""

    return f"""<!DOCTYPE html>
<html lang="lt">
<head>
  <!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
}})(window,document,'script','dataLayer','{GTM}');</script>
<!-- End Google Tag Manager -->
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}" />{kw}
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />
  <link rel="canonical" href="{canonical}" />

  <!-- Open Graph -->
  <meta property="og:type" content="{og_type}" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:title" content="{esc(title)}" />
  <meta property="og:description" content="{esc(description)}" />
  <meta property="og:image" content="{image}" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:alt" content="Humanoidinis robotas Unitree G1 — nuoma renginiams Lietuvoje" />
  <meta property="og:locale" content="lt_LT" />
  <meta property="og:locale:alternate" content="pl_PL" />
  <meta property="og:locale:alternate" content="de_AT" />
  <meta property="og:site_name" content="{BRAND}" />{art}

  <!-- Twitter / X -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{esc(title)}" />
  <meta name="twitter:description" content="{esc(description)}" />
  <meta name="twitter:image" content="{image}" />

  <meta name="theme-color" content="#000000" />
  <meta name="format-detection" content="telephone=no" />

  <!-- Kalbų versijos -->
{hreflang}

{ld_blocks}

  <script>history.scrollRestoration = 'manual';</script>{preload}
  <link rel="alternate" type="application/rss+xml" title="33bots — blogo RSS" href="{SITE}/feed.xml" />
  <link rel="icon" type="image/svg+xml" href="favicon.svg" />

  <!-- Šriftas talpinamas lokaliai — jokių blokuojančių užklausų į trečiųjų šalių serverius -->
  <link rel="preload" href="fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin />
  <link rel="preload" href="fonts/inter-latin-ext.woff2" as="font" type="font/woff2" crossorigin />
  <link rel="stylesheet" href="fonts.css?v={CSS_V}" />

  <!-- Kritinis CSS įterptas — pirmas ekranas piešiamas nelaukiant style.css -->
  <style>{CRITICAL_CSS}</style>
  <link rel="preload" href="style.css?v={CSS_V}" as="style" onload="this.onload=null;this.rel='stylesheet'" />
  <noscript><link rel="stylesheet" href="style.css?v={CSS_V}" /></noscript>

  <link rel="preconnect" href="https://www.googletagmanager.com" />
{extra_head}</head>
"""


def body_open():
    return f"""<body>
  <!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM}"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

  <a href="#turinys" class="skip-link">Pereiti prie turinio</a>
  <div class="cursor-glow" id="cursorGlow" aria-hidden="true"></div>
  <div class="scroll-progress" id="scrollProgress" aria-hidden="true"></div>
"""


def nav(active=""):
    offer = "\n".join(
        f'            <a href="{u}">{t}</a>' for u, t in NAV_OFFER
    )
    main_links = "\n".join(
        '        <a href="{}"{}>{}</a>'.format(u, ' aria-current="page"' if u == active else "", t)
        for u, t in NAV_MAIN
    )
    mob_offer = "\n".join(
        f'    <a href="{u}" class="mobile-menu__sub">{t}</a>' for u, t in NAV_OFFER
    )
    mob_main = "\n".join(f'    <a href="{u}">{t}</a>' for u, t in NAV_MAIN + NAV_SECONDARY)

    return f"""  <!-- NAVIGACIJA -->
  <header class="nav" id="nav">
    <div class="nav__inner">
      <a href="index.html" class="logo" aria-label="33bots — pradžia">33BOTS</a>
      <nav class="nav__links" aria-label="Pagrindinė navigacija">
        <div class="nav__dropdown">
          <button class="nav__dropdown-toggle" aria-haspopup="true" aria-expanded="false" type="button">Paslaugos <svg viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M1 1l4 4 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
          <div class="nav__dropdown-menu">
{offer}
          </div>
        </div>
{main_links}
      </nav>
      <div class="lang-switch" aria-label="Kalbos pasirinkimas">
        <span class="lang-switch__current" aria-current="true">LT</span>
        <a href="https://33bots.pl/" hreflang="pl" lang="pl" title="Polska wersja strony">PL</a>
        <a href="https://33bots.at/" hreflang="de-AT" lang="de" title="Österreichische Version">AT</a>
        <a href="https://robotollern.de/" hreflang="de" lang="de" title="Deutsche Version">DE</a>
      </div>
      <button class="hamburger" id="hamburger" aria-label="Atidaryti meniu" aria-expanded="false">
        <span></span><span></span>
      </button>
    </div>
  </header>
  <main id="turinys">

  <div class="mobile-menu" id="mobileMenu">
    <span class="mobile-menu__label">Paslaugos</span>
{mob_offer}
{mob_main}
    <span class="mobile-menu__label">Kalba</span>
    <a href="https://33bots.pl/" hreflang="pl" lang="pl">Polski — 33bots.pl</a>
    <a href="https://33bots.at/" hreflang="de-AT" lang="de">Deutsch — 33bots.at</a>
  </div>
"""


def crumbs(items):
    """items: [(title, url|None)] — paskutinis be nuorodos."""
    parts = []
    for i, (title, url) in enumerate(items):
        if url:
            parts.append(f'<a href="{url}">{title}</a>')
        else:
            parts.append(f'<span aria-current="page">{title}</span>')
    sep = ' <span aria-hidden="true">/</span> '
    return f"""  <nav class="crumbs" aria-label="Naršymo kelias">
    {sep.join(parts)}
  </nav>
"""


def breadcrumb_ld(items):
    """items: [(title, absolute_url)]"""
    els = ",\n".join(
        f"""      {{"@type": "ListItem", "position": {i + 1}, "name": "{esc(t)}", "item": "{u}"}}"""
        for i, (t, u) in enumerate(items)
    )
    return f"""{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
{els}
  ]
}}"""


def faq_ld(pairs):
    items = ",\n".join(
        f"""      {{
        "@type": "Question",
        "name": "{esc(q)}",
        "acceptedAnswer": {{"@type": "Answer", "text": "{esc(a)}"}}
      }}""" for q, a in pairs
    )
    return f"""{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
{items}
  ]
}}"""


def faq_section(pairs, title="Dažniausiai užduodami<br />klausimai"):
    items = "\n".join(f"""      <div class="faq-item">
        <button class="faq-q" aria-expanded="false" type="button">
          <span>{q}</span>
          <span class="faq-q__icon" aria-hidden="true">+</span>
        </button>
        <div class="faq-a" hidden>
          <p>{a}</p>
        </div>
      </div>""" for q, a in pairs)

    return f"""  <!-- DUK -->
  <section class="section faq-section" id="duk">
    <div class="section-header">
      <span class="tag">DUK</span>
      <h2 class="section-title">{title}</h2>
    </div>
    <div class="faq">
{items}
    </div>
  </section>
"""


def video_section(heading="Pamatykite robotą<br />gyvai", lead=None):
    lead = lead or ('Taip <strong style="color:var(--text);">Unitree G1</strong> atrodo gyvai: vaikšto, '
                    'gestikuliuoja, pasitinka svečius ir šoka. Ant roboto matyti mūsų standartas — '
                    '<strong style="color:var(--text);">nemokamas ženklinimas</strong> su jūsų logotipu '
                    'ir QR kodu ant krūtinės.')
    return f"""  <!-- VIDEO -->
  <section class="section" id="video">
    <div class="section-header">
      <span class="tag">Video</span>
      <h2 class="section-title">{heading}</h2>
    </div>
    <div style="display:flex; flex-wrap:wrap; gap:var(--s6); align-items:center; justify-content:center; max-width:1000px; margin:0 auto;">
      <video controls muted playsinline preload="none"
             poster="video/33bots-robot-event-poster.jpg"
             width="360" height="640"
             style="width:min(360px,90vw); border-radius:16px; border:1px solid var(--border-mid); background:var(--surface-2);"
             aria-label="Humanoidinis robotas Unitree G1 renginyje — vaikšto, gestikuliuoja ir šoka">
        <source src="video/33bots-robot-event.mp4" type="video/mp4" />
        Jūsų naršyklė nepalaiko HTML5 vaizdo įrašų.
      </video>
      <div style="max-width:420px; display:flex; flex-direction:column; gap:var(--s4); text-align:left;">
        <p style="color:var(--text-2); font-size:1rem; line-height:1.8; margin:0;">{lead}</p>
        <a href="video-realizacijos.html" style="display:inline-flex; align-items:center; gap:8px; color:var(--text); font-size:0.9rem; font-weight:600; text-decoration:underline; text-underline-offset:3px;">Daugiau įrašų iš renginių →</a>
        <a href="#kontaktai" class="btn-primary" style="display:inline-flex; align-self:flex-start;">Rezervuoti pasirodymą →</a>
      </div>
    </div>
  </section>
"""


def contact_section(heading="Rezervuokite robotą<br />savo renginiui.",
                    lead="Parašykite mums — atsakysime per vieną darbo dieną su kaina ir laisvomis datomis."):
    city_links = "\n".join(
        f'            <li><a href="{city_url(s)}">{n}</a></li>' for s, n, _, _ in CITIES
    )
    return f"""  <!-- KONTAKTAI -->
  <section class="section contact-section" id="kontaktai">
    <div class="contact-layout">
      <div class="contact-left">
        <span class="tag">Kontaktai</span>
        <h2 class="section-title">{heading}</h2>
        <p class="body-text">{lead}</p>
        <div class="contact-details">
          <div class="contact-detail">
            <span class="contact-detail__label">Įmonė</span>
            <span class="contact-detail__val">33bots — humanoidinių robotų nuoma</span>
          </div>
          <a href="mailto:{EMAIL}" class="contact-detail">
            <span class="contact-detail__label">El. paštas</span>
            <span class="contact-detail__val">{EMAIL}</span>
          </a>
          <a href="tel:{PHONE_1}" class="contact-detail">
            <span class="contact-detail__label">Telefonas</span>
            <span class="contact-detail__val">{PHONE_1_H}</span>
          </a>
          <a href="tel:{PHONE_2}" class="contact-detail">
            <span class="contact-detail__label">Telefonas</span>
            <span class="contact-detail__val">{PHONE_2_H}</span>
          </a>
          <div class="contact-detail">
            <span class="contact-detail__label">Aptarnaujame</span>
            <span class="contact-detail__val">Visą Lietuvą</span>
          </div>
        </div>

        <nav class="coverage" aria-label="Miestai, kuriuose nuomojame robotą">
          <p class="coverage__label">Atvažiuojame be papildomo mokesčio į:</p>
          <ul class="coverage__cities">
{city_links}
          </ul>
          <p class="coverage__note">ir bet kurią kitą Lietuvos vietą — atvykimo kainą nurodome pasiūlyme</p>
        </nav>
      </div>
      <div class="contact-right">
        <form id="contactForm" class="form" novalidate>
          <div class="form-steps-header">
            <span class="form-step-ind active" id="stepInd1">01 — Kontaktiniai duomenys</span>
            <span class="form-step-sep">/</span>
            <span class="form-step-ind" id="stepInd2">02 — Jūsų renginys</span>
          </div>

          <div class="form-step" id="formStep1">
            <div class="form-row">
              <div class="form-field">
                <label for="f-name">Vardas ir pavardė *</label>
                <input id="f-name" type="text" name="name" placeholder="Jonas Jonaitis" autocomplete="name" required />
                <span class="form-field__err" aria-live="polite"></span>
              </div>
              <div class="form-field">
                <label for="f-company">Įmonė</label>
                <input id="f-company" type="text" name="company" placeholder="Įmonės pavadinimas" autocomplete="organization" />
              </div>
            </div>
            <div class="form-row">
              <div class="form-field">
                <label for="f-email">El. paštas *</label>
                <input id="f-email" type="email" name="email" placeholder="info@imone.lt" autocomplete="email" required />
                <span class="form-field__err" aria-live="polite"></span>
              </div>
              <div class="form-field">
                <label for="f-phone">Telefonas</label>
                <input id="f-phone" type="tel" name="phone" placeholder="+370 600 00000" autocomplete="tel" />
              </div>
            </div>
            <button type="button" id="btnNext" class="btn-submit">Toliau — papasakokite apie renginį →</button>
          </div>

          <div class="form-step form-step--hidden" id="formStep2" aria-hidden="true">
            <div class="form-row">
              <div class="form-field">
                <label for="f-date">Planuojama renginio data</label>
                <input id="f-date" type="date" name="date" />
              </div>
              <div class="form-field">
                <label for="f-location">Miestas / vieta</label>
                <input id="f-location" type="text" name="location" placeholder="pvz. Vilnius, LITEXPO" autocomplete="address-level2" />
              </div>
            </div>
            <div class="form-field">
              <label for="f-message">Papasakokite apie renginį *</label>
              <textarea id="f-message" name="message" rows="6"
                placeholder="Renginio tipas (paroda, konferencija, gala vakaras...), apytikslis svečių skaičius, kiek laiko norite roboto ir viskas, kas jums atrodo svarbu." required></textarea>
              <div class="form-field__footer">
                <span class="form-field__err" aria-live="polite"></span>
                <span class="char-counter"><span id="charCount">0</span> / 600</span>
              </div>
            </div>
            <div class="form-step__nav">
              <button type="button" id="btnBack" class="btn-back">← Atgal</button>
              <button type="submit" class="btn-submit">Siųsti užklausą →</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </section>
"""


def footer():
    socials = "\n".join(
        f'          <a href="{u}" target="_blank" rel="noopener noreferrer" class="footer__social">↗ {n}</a>'
        for n, u in SOCIALS
    )
    links = "\n".join(
        f'        <a href="{u}">{t}</a>'
        for u, t in (NAV_OFFER[:4] + NAV_MAIN + NAV_SECONDARY
                     + [("privatumo-politika.html", "Privatumo politika")])
    )
    return f"""  </main>
  <footer class="footer">
    <div class="footer__inner">
      <div class="footer__brand">
        <span class="logo">33BOTS</span>
        <p class="footer__tagline">Humanoidinių robotų nuoma · Lietuva</p>
        <div class="footer__nap">
          <a href="tel:{PHONE_1}" class="footer__nap-item">{PHONE_1_H}</a>
          <a href="mailto:{EMAIL}" class="footer__nap-item">{EMAIL}</a>
        </div>
        <p class="footer__tagline" style="margin-top:12px;">
          <a href="https://33bots.pl/" hreflang="pl" lang="pl" style="color:inherit;">Polski</a> ·
          <a href="https://33bots.at/" hreflang="de-AT" lang="de" style="color:inherit;">Österreich</a> ·
          <a href="https://robotollern.de/" hreflang="de" lang="de" style="color:inherit;">Deutschland</a>
        </p>
      </div>
      <div class="footer__links">
{links}
      </div>
      <div class="footer__right">
        <div class="footer__socials">
{socials}
        </div>
        <span class="footer__copy">© 2026 33bots. Visos teisės saugomos.</span>
      </div>
    </div>
  </footer>

  <div class="cookie-banner" id="cookieBanner" aria-live="polite">
    <p class="cookie-banner__text">
      Ši svetainė naudoja slapukus analizės tikslais.
      <a href="privatumo-politika.html" class="cookie-banner__link">Privatumo politika</a>
    </p>
    <button class="cookie-banner__btn" id="cookieAccept" type="button">Supratau</button>
  </div>

  <div class="sticky-cta">
    <a href="#kontaktai" class="btn-primary">Rezervuoti robotą →</a>
  </div>

  <script src="main.js"></script>
  <script>window._nQc="89159321";</script>
  <script async src="https://serve.albacross.com/track.js"></script>
</body>
</html>
"""


def organization_ld():
    same_as = ",\n".join(f'      "{u}"' for _, u in SOCIALS)
    return f"""{{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "@id": "{SITE}/#organizacija",
  "name": "33bots — humanoidinių robotų nuoma renginiams",
  "alternateName": "33bots",
  "url": "{SITE}/",
  "logo": "{SITE}/logo.png",
  "image": "{SITE}/robot-g1.jpg",
  "description": "Humanoidinių robotų Unitree G1 nuoma renginiams, parodoms ir konferencijoms visoje Lietuvoje. Sertifikuotas operatorius ir ženklinimas kainoje; atvykimą vertiname pagal renginio vietą.",
  "telephone": "{PHONE_1}",
  "email": "{EMAIL}",
  "areaServed": {{"@type": "Country", "name": "Lithuania"}},
  "sameAs": [
{same_as}
  ],
  "contactPoint": {{
    "@type": "ContactPoint",
    "telephone": "{PHONE_1}",
    "email": "{EMAIL}",
    "contactType": "sales",
    "areaServed": "LT",
    "availableLanguage": ["Lithuanian", "Polish", "English"]
  }},
  "knowsAbout": [
    "humanoidinio roboto nuoma",
    "robotas renginiui",
    "robotas parodoms",
    "robotas konferencijai",
    "Unitree G1",
    "renginių pramogos"
  ],
  "priceRange": "nuo 2100 EUR už renginio dieną"
}}"""


def website_ld():
    return f"""{{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "{SITE}/#svetaine",
  "name": "33bots",
  "alternateName": "33bots — humanoidinių robotų nuoma",
  "url": "{SITE}/",
  "inLanguage": "lt-LT",
  "description": "Humanoidinių robotų Unitree G1 nuoma renginiams, parodoms ir konferencijoms visoje Lietuvoje.",
  "publisher": {{"@id": "{SITE}/#organizacija"}}
}}"""


def video_ld():
    return f"""{{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "Humanoidinis robotas Unitree G1 renginyje — nuoma Lietuvoje | 33bots",
  "description": "Humanoidinis robotas Unitree G1 gyvai: vaikšto, gestikuliuoja, pasitinka svečius ir šoka. Nemokamas ženklinimas su prekės ženklo logotipu ir QR kodu. Nuoma renginiams, parodoms ir konferencijoms visoje Lietuvoje.",
  "thumbnailUrl": "{SITE}/video/33bots-robot-event-poster.jpg",
  "contentUrl": "{SITE}/video/33bots-robot-event.mp4",
  "uploadDate": "2026-07-02",
  "duration": "PT35S",
  "inLanguage": "lt",
  "publisher": {{"@id": "{SITE}/#organizacija"}}
}}"""


def service_ld(name, description, url, area="Lietuva", price=None):
    """`price` — kaina eurais už realizacijos dieną; nurodžius ji patenka į Offer bloką."""
    if price:
        offers = f"""{{
    "@type": "Offer",
    "priceCurrency": "EUR",
    "price": "{price}",
    "availability": "https://schema.org/InStock",
    "url": "{url}",
    "priceSpecification": {{
      "@type": "UnitPriceSpecification",
      "priceCurrency": "EUR",
      "price": "{price}",
      "unitText": "diena",
      "valueAddedTaxIncluded": false
    }}
  }}"""
    else:
        offers = f"""{{
    "@type": "Offer",
    "priceCurrency": "EUR",
    "availability": "https://schema.org/InStock",
    "url": "{url}",
    "priceSpecification": {{
      "@type": "PriceSpecification",
      "priceCurrency": "EUR",
      "valueAddedTaxIncluded": false
    }}
  }}"""
    return f"""{{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "{esc(name)}",
  "description": "{esc(description)}",
  "url": "{url}",
  "serviceType": "Humanoidinio roboto nuoma",
  "provider": {{"@id": "{SITE}/#organizacija"}},
  "areaServed": {{"@type": "Place", "name": "{esc(area)}"}},
  "offers": {offers}
}}"""


def write(path, html):
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✓ {path}")
