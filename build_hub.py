# -*- coding: utf-8 -*-
"""Centrinis „robotų nuoma“ puslapis — paslaugų ir miestų mazgas (silo struktūra)."""
from collections import OrderedDict

from lt_gallery import gallery_section
from build_cities import CITY_DATA
from lt_offers2 import PAGES2
from lt_offers3 import PAGES3
from build_offers import PAGES
from lt_common import (SITE, head, body_open, nav, crumbs, breadcrumb_ld, contact_section,
                       footer, faq_section, faq_ld, organization_ld, service_ld, video_section,
                       write, esc, CITIES, city_url)

SLUG = "robotu-nuoma.html"

FAQ = [
    ("Kas yra robotų nuoma ir kuo ji skiriasi nuo pirkimo?",
     "Nuomos atveju vienam renginiui gaunate ne tik įrangą, bet ir komandą: robotą, operatorių, "
     "paruošimą ir ženklinimą. Perkant robotą prie kainos prisideda mokymai, servisas, "
     "atsarginės dalys, sandėliavimas ir draudimas — todėl iki maždaug 10–15 renginių per metus nuoma "
     "beveik visada pigesnė."),
    ("Kokiuose Lietuvos miestuose nuomojate robotus?",
     "Visoje Lietuvoje. Turime atskirus puslapius 28 miestams — nuo Vilniaus ir Kauno iki Mažeikių, "
     "Anykščių ar Birštono — bet atvažiuojame ir į bet kurią kitą vietą, įskaitant sodybas bei "
     "gamyklų teritorijas."),
    ("Kiek kainuoja atvykimas?",
     "Atvykimą vertiname pagal renginio vietą ir sumą nurodome pasiūlyme kartu su nuomos kaina. "
     "Dirbame visoje Lietuvoje."),
    ("Kokiems renginiams tinka robotų nuoma?",
     "Dažniausiai — parodoms, konferencijoms, gala vakarams, įmonių šventėms, atidarymams ir produktų "
     "pristatymams. Taip pat vestuvėms, gimtadieniams, mokyklų renginiams, sporto varžyboms ir "
     "reklamos filmavimams."),
    ("Kiek iš anksto reikia rezervuoti?",
     "Sezono metu (rugsėjis–gruodis, gegužė–birželis) rekomenduojame 3–4 savaites, gruodžiui — dar "
     "anksčiau. Ne sezono metu dažnai pavyksta suderinti per kelias dienas."),
    ("Ar robotą reikia mokėti valdyti?",
     "Ne. Robotą valdo mūsų operatorius, kuris lieka visą renginio laiką. Jums lieka tik renginio "
     "turinys — techninė pusė yra mūsų atsakomybė."),
]


def regions():
    """Miestus sugrupuoja pagal apskritis — natūralus vidinių nuorodų grupavimas."""
    grouped = OrderedDict()
    for slug, name, loc, _ in CITIES:
        region = CITY_DATA[slug]["region"]
        grouped.setdefault(region, []).append((slug, name))
    return grouped


def build():
    url = f"{SITE}/{SLUG}"
    all_pages = PAGES + PAGES2 + PAGES3

    region_blocks = "\n".join(f"""      <div class="use-item">
        <span class="use-num">{i + 1:02d}</span>
        <h3>{region}</h3>
        <div class="related-links" style="margin-top:var(--s2);">
{chr(10).join(f'          <a href="{city_url(s)}">{n}</a>' for s, n in cities)}
        </div>
      </div>""" for i, (region, cities) in enumerate(regions().items()))

    service_cards = "\n".join(f"""      <div class="tile">
        <div class="tile__top"><span class="tile__tag">{p['tag']}</span></div>
        <h3 class="tile__title" style="font-size:1.1rem;">{p['crumb']}</h3>
        <p class="tile__desc">{p['desc']}</p>
        <a href="{p['slug']}" class="tile__link">Sužinoti daugiau →</a>
      </div>""" for p in all_pages)

    city_items = ",\n".join(f"""      {{
        "@type": "ListItem",
        "position": {i + 1},
        "url": "{SITE}/{city_url(s)}",
        "name": "Humanoidinio roboto nuoma {esc(loc)}"
      }}""" for i, (s, n, loc, _) in enumerate(CITIES))

    ld = [
        organization_ld(),
        service_ld("Robotų nuoma Lietuvoje",
                   "Humanoidinių robotų Unitree G1 nuoma renginiams visoje Lietuvoje su operatoriumi "
                   "ir ženklinimu.", url),
        f"""{{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "Robotų nuoma Lietuvoje — visi miestai ir paslaugos",
  "url": "{url}",
  "inLanguage": "lt-LT",
  "isPartOf": {{"@id": "{SITE}/#svetaine"}},
  "about": {{"@id": "{SITE}/#organizacija"}}
}}""",
        f"""{{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Miestai, kuriuose nuomojame humanoidinius robotus",
  "numberOfItems": {len(CITIES)},
  "itemListElement": [
{city_items}
  ]
}}""",
        breadcrumb_ld([("Pradžia", f"{SITE}/"), ("Robotų nuoma", url)]),
        faq_ld(FAQ),
    ]

    html = head(
        title="Robotų nuoma Lietuvoje — visi miestai ir paslaugos | 33bots",
        description="Robotų nuoma visoje Lietuvoje: humanoidinis Unitree G1 su operatoriumi "
                    "ir ženklinimu. Visi miestai ir paslaugų formatai.",
        slug=SLUG,
        keywords="robotų nuoma, robotų nuoma Lietuvoje, roboto nuoma, humanoidinių robotų nuoma, "
                 "robotas renginiui",
        og_image=f"{SITE}/og/robotu-nuoma.jpg", extra_ld=ld)
    html += body_open()
    html += nav(active=SLUG)
    html += crumbs([("Pradžia", "index.html"), ("Robotų nuoma", None)])

    html += f"""
  <section class="hero hero--sub">
    <div class="hero__content">
      <p class="hero__eyebrow">Robotų nuoma · Visa Lietuva · {len(CITIES)} miestai</p>
      <h1 class="hero__title">Robotų nuoma<br />Lietuvoje.</h1>
      <p class="hero__sub">Vienas puslapis, nuo kurio galite pradėti: visos paslaugos, visi miestai ir visos sąlygos. Humanoidinis robotas Unitree G1 su operatoriumi, transportu ir ženklinimu — nuo trijų valandų pasirodymo iki kelių dienų parodos.</p>
      <div class="hero__ctas">
        <a href="#kontaktai" class="btn-primary">Gauti pasiūlymą</a>
        <a href="#miestai" class="btn-ghost">Rasti savo miestą ↓</a>
      </div>
      <div class="hero__trust">
        <span class="hero__trust-item">✓ Atvykimas visoje Lietuvoje</span>
        <span class="hero__trust-item">✓ Operatorius kainoje</span>
        <span class="hero__trust-item">✓ Ženklinimas be priemokų</span>
        <span class="hero__trust-item">✓ Atsakymas per 24 val.</span>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="article-body">
      <h2>Kaip veikia robotų nuoma</h2>
      <p>Robotų nuoma 33bots visada reiškia <strong>pilną paslaugą</strong>, o ne įrangos perdavimą. Į kiekvieną užsakymą įeina robotas Unitree G1, sertifikuotas operatorius visam renginio laikui, transportas į bet kurią Lietuvos vietą, paruošimas vietoje, ženklinimas jūsų logotipu bei QR kodu ir scenarijaus derinimas prieš renginį.</p>
      <p>Praktiškai tai atrodo taip: parašote datą, miestą ir renginio tipą — per 24 valandas gaunate konkrečią kainą ir laisvas datas. Po sutarties pasirašymo jums nebereikia daryti nieko, išskyrus užtikrinti elektros lizdą ir maždaug 2×2 m laisvos erdvės. Detalią kainodarą aprašėme <a href="kainos.html">kainų puslapyje</a>, o visą procesą — <a href="blog-kaip-issinuomoti-robota.html">nuomos vadove</a>.</p>
    </div>
  </section>

  <!-- PASLAUGOS -->
  <section class="section tiles-section" id="paslaugos">
    <div class="section-header">
      <span class="tag">Paslaugos</span>
      <h2 class="section-title">Visi nuomos<br />formatai</h2>
    </div>
    <div class="tiles tiles--blog">
{service_cards}
    </div>
  </section>

  <!-- MIESTAI -->
  <section class="section" id="miestai">
    <div class="section-header">
      <span class="tag">Miestai</span>
      <h2 class="section-title">Robotų nuoma<br />pagal regionus</h2>
    </div>
    <p style="max-width:760px; margin:0 auto var(--s7); text-align:center; color:var(--text-2); line-height:1.8;">Aptarnaujame visą Lietuvą, o {len(CITIES)} miestams turime atskirus puslapius su vietos renginių scenos aprašymu ir tipinėmis erdvėmis. Jūsų miesto sąraše nėra? Tai nieko nekeičia — atvažiuojame visur, ir transportas visada įskaičiuotas.</p>
    <div class="use-grid">
{region_blocks}
    </div>
  </section>

"""
    html += gallery_section(lead="Kadrai iš tikrų 33bots projektų — ta pati įranga ir komanda dirba visoje Lietuvoje.")
    html += video_section()
    html += faq_section(FAQ, title="Klausimai apie<br />robotų nuomą")
    html += contact_section(heading="Gaukite pasiūlymą<br />savo renginiui.")
    html += footer()
    write(SLUG, html)


if __name__ == "__main__":
    build()
