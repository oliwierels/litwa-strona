# -*- coding: utf-8 -*-
"""Pagrindinis 33bots.lt puslapis."""
from lt_articles import ARTICLES as _A1
from lt_articles2 import ARTICLES2 as _A2
from build_offers import PAGES as _P1
from lt_offers2 import PAGES2 as _P2
from lt_offers3 import PAGES3 as _P3
from lt_gallery import gallery_section
from lt_common import (SITE, head, body_open, nav, contact_section, footer, faq_section,
                       faq_ld, organization_ld, website_ld, video_ld, video_section,
                       write, CITIES, city_url, service_ld)

ARTICLES = _A1 + _A2
OFFER_PAGES = _P1 + _P2 + _P3

FAQ = [
    ("Ar galiu išsinuomoti robotą, jei nemoku juo valdyti?",
     "Taip. Su robotu visada atvyksta mūsų operatorius, kuris pasirūpina paruošimu, valdymu ir "
     "programa viso renginio metu. Jums nereikia jokių techninių žinių — tiesiog pasakykite, ko "
     "norite, o mes tai įgyvendinsime."),
    ("Ar robotą galima ženklinti mūsų prekės ženklu?",
     "Taip, ir tai nekainuoja papildomai. Ant roboto krūtinės uždedame jūsų logotipą ir QR kodą, "
     "o programą pritaikome prie renginio komunikacijos. Ženklinimas įskaičiuotas į nuomos kainą."),
    ("Ar robotas saugus svečiams?",
     "Taip. Unitree G1 turi LiDAR jutiklius ir kompiuterinę regą, todėl realiu laiku aptinka kliūtis "
     "ir žmones. Papildomai visą laiką budi mūsų operatorius, o veiklai taikoma civilinės "
     "atsakomybės draudimo apsauga."),
    ("Ar nuomojate robotą visoje Lietuvoje?",
     "Taip — dirbame visoje Lietuvoje ir transportas įskaičiuotas į kainą, nesvarbu, ar renginys "
     "Vilniuje, Klaipėdoje, ar mažesniame mieste. Nėra mokesčio už kilometrus ir nėra minimalaus "
     "atstumo."),
    ("Kokių techninių sąlygų reikia vietoje?",
     "Užtenka standartinio 230 V lizdo ir maždaug 2×2 m laisvos erdvės. Interneto ryšys ar specialus "
     "apšvietimas nebūtinas. Operatorius atvyksta su visa įranga ir viską paruošia per 30–45 minutes "
     "prieš renginio pradžią."),
    ("Ar robotas moka šokti?",
     "Taip. Į atmintį įrašytos kelios choreografijos — nuo trumpo pasirodymo scenoje iki šokio kartu "
     "su svečiais šokių aikštelėje. Jei renginyje yra DJ, robotas mielai perima aikštelę."),
    ("Kaip greitai gausiu pasiūlymą?",
     "Užklausas peržiūrime kiekvieną darbo dieną ir atsakome per 24 valandas su kaina bei laisvomis "
     "datomis. Skubiems renginiams paskambinkite — dažnai pavyksta suderinti net ir per kelias dienas."),
    ("Kiek laiko robotas gali dirbti renginyje?",
     "Nuomos paketai apima nuo trumpo pasirodymo (iki 3 val.) iki visos dienos ar kelių dienų parodos. "
     "Robotas dirba ciklais su trumpomis pertraukomis baterijai pakeisti — svečiams tai nepastebima, "
     "nes operatorius pertraukas suderina su renginio programa."),
    ("Kuo 33bots skiriasi nuo kitų nuomos įmonių?",
     "Į kainą visada įeina visas paketas: nemokamas transportas be kilometrų limito, sertifikuotas "
     "operatorius visą renginį ir nemokamas roboto ženklinimas. Dirbame su savo įranga — be tarpininkų, "
     "o mūsų projektai Lenkijoje buvo rodomi nacionalinėje televizijoje."),
]

BLOG_CARDS = "\n".join(f"""      <div class="tile">
        <div class="tile__top"><span class="tile__tag">{a['tag']}</span></div>
        <h3 class="tile__title" style="font-size:1.1rem;">{a['title']}</h3>
        <p class="tile__desc">{a['card']}</p>
        <a href="{a['slug']}" class="tile__link">Skaityti straipsnį →</a>
      </div>""" for a in ARTICLES[:8])

OFFER_CHIPS = "\n".join(
    f'        <a href="{p["slug"]}">{p["crumb"]}</a>' for p in OFFER_PAGES
)

CITY_CHIPS = "\n".join(
    f'        <a href="{city_url(s)}" class="tile__link" style="padding:8px 16px; background:var(--surface-2); '
    f'border:1px solid var(--border-mid); border-radius:8px;">{n}</a>'
    for s, n, _, _ in CITIES
)

TITLE = "Humanoidinių robotų nuoma renginiams Lietuvoje | 33bots"
DESC = ("Humanoidinio roboto Unitree G1 nuoma renginiams, parodoms ir konferencijoms visoje "
        "Lietuvoje. Transportas, operatorius ir ženklinimas kainoje.")


def build():
    ld = [
        organization_ld(),
        website_ld(),
        video_ld(),
        service_ld("Humanoidinio roboto Unitree G1 nuoma renginiams",
                   "Humanoidinio roboto nuoma renginiams, parodoms, konferencijoms ir įmonių šventėms visoje Lietuvoje.",
                   f"{SITE}/"),
        f"""{{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Humanoidinio roboto Unitree G1 nuoma",
  "description": "Humanoidinio roboto Unitree G1 nuoma renginiams, parodoms ir konferencijoms Lietuvoje.",
  "url": "{SITE}/",
  "image": "{SITE}/robot-g1.jpg",
  "brand": {{"@type": "Brand", "name": "Unitree"}},
  "aggregateRating": {{
    "@type": "AggregateRating",
    "ratingValue": "5.0",
    "reviewCount": "3",
    "bestRating": "5",
    "worstRating": "1"
  }},
  "review": [
    {{
      "@type": "Review",
      "author": {{"@type": "Person", "name": "Karolina M."}},
      "datePublished": "2025-10-12",
      "reviewRating": {{"@type": "Rating", "ratingValue": "5", "bestRating": "5"}},
      "reviewBody": "Rezultatas pranoko drąsiausius lūkesčius. Susidomėjimas buvo milžiniškas visą renginio laiką."
    }},
    {{
      "@type": "Review",
      "author": {{"@type": "Person", "name": "Piotr Z."}},
      "datePublished": "2025-11-03",
      "reviewRating": {{"@type": "Rating", "ratingValue": "5", "bestRating": "5"}},
      "reviewBody": "Tai buvo vienas geriausių organizacinių sprendimų. Teigiamos dalyvių reakcijos ir jų įsitraukimas mums yra geriausias įvertinimas."
    }},
    {{
      "@type": "Review",
      "author": {{"@type": "Person", "name": "Magdalena T."}},
      "datePublished": "2025-12-08",
      "reviewRating": {{"@type": "Rating", "ratingValue": "5", "bestRating": "5"}},
      "reviewBody": "Bendradarbiavimas virto neįtikėtinais pasiekiamumo skaičiais socialiniuose tinkluose."
    }}
  ]
}}""",
        faq_ld(FAQ),
        f"""{{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "Kaip išsinuomoti humanoidinį robotą renginiui",
  "description": "Roboto Unitree G1 nuomos procesas penkiais žingsniais: užklausa, kaina, sutartis, roboto atvykimas su operatoriumi ir pasirodymas gyvai.",
  "image": "{SITE}/robot-g1.jpg",
  "totalTime": "P1D",
  "step": [
    {{"@type": "HowToStep", "position": 1, "name": "Parašykite mums", "text": "Užpildykite formą arba parašykite el. laišką. Atsakome per 24 val.", "url": "{SITE}/#kontaktai"}},
    {{"@type": "HowToStep", "position": 2, "name": "Kaina ir data", "text": "Aptariame datą, vietą ir lūkesčius. Paruošiame individualų pasiūlymą."}},
    {{"@type": "HowToStep", "position": 3, "name": "Sutartis ir avansas", "text": "Paprasta sutartis, aiškios sąlygos. Datą rezervuojate avansu."}},
    {{"@type": "HowToStep", "position": 4, "name": "Robotas atvyksta", "text": "Atvežame G1, paruošiame ir išbandome. Operatorius su jumis visą laiką."}},
    {{"@type": "HowToStep", "position": 5, "name": "Pasirodymas", "text": "Svečiai sužavėti, o nuotraukos ir įrašai keliauja į socialinius tinklus."}}
  ]
}}""",
    ]

    html = head(title=TITLE, description=DESC, slug="index.html",
                keywords="humanoidinio roboto nuoma, robotas renginiui, roboto nuoma, Unitree G1, "
                         "robotas parodoms, robotas konferencijai, renginių pramogos, robotas Vilnius",
                og_image=f"{SITE}/og/index.jpg", extra_ld=ld, preload_hero=True)
    html += body_open()
    html += nav()

    html += f"""
  <!-- HERO -->
  <section class="hero">
    <div class="hero__content">
      <p class="hero__eyebrow">Humanoidinių robotų nuoma · Lietuva · Robotas renginiui</p>
      <h1 class="hero__title">Humanoidinių<br />robotų nuoma<br /><em>Unitree G1.</em></h1>
      <p class="hero__sub">Humanoidinio roboto Unitree G1 nuoma renginiui, konferencijai ir parodai visoje Lietuvoje. Vaikšto, gestikuliuoja, sustabdo minią. Nemokamas transportas — Vilnius, Kaunas, Klaipėda, Šiauliai, Panevėžys ir visa šalis.</p>
      <div class="hero__ctas">
        <a href="#kontaktai" class="btn-primary">Rezervuoti datą</a>
        <a href="#paslaugos" class="btn-ghost">Pamatyti pasiūlymą ↓</a>
      </div>
      <div class="hero__trust">
        <span class="hero__trust-item">✓ Skaidri kaina</span>
        <span class="hero__trust-item">✓ Nemokamas transportas</span>
        <span class="hero__trust-item">✓ Operatorius kainoje</span>
        <span class="hero__trust-item">✓ Ženklinimas be priemokų</span>
      </div>
    </div>
    <div class="hero__visual">
      <div class="hero__spotlight" aria-hidden="true"></div>
      <div class="hero__robot-wrap" id="robotWrap">
      <div class="hero__robot">
        <div class="robot-scan" aria-hidden="true"></div>
        <picture>
          <source srcset="robot-g1-960.webp 960w, robot-g1.webp 2390w" sizes="(min-width: 769px) 45vw, 1px" type="image/webp" />
          <img src="robot-g1.jpg"
               alt="Humanoidinis robotas Unitree G1 — pramoga renginiams, parodoms ir konferencijoms Lietuvoje"
               class="hero__robot-img"
               width="600" height="800"
               loading="eager"
               fetchpriority="high" />
        </picture>
      </div>
      </div>
    </div>
  </section>

  <!-- SKAIČIAI -->
  <div class="stats-bar">
    <div class="stats-bar__inner">
      <div class="stat-item">
        <span class="stat-item__val" data-count="16" data-suffix="+">0</span>
        <span class="stat-item__lbl">miestų Lietuvoje</span>
      </div>
      <div class="stat-item__div" aria-hidden="true"></div>
      <div class="stat-item">
        <span class="stat-item__val" data-count="43" data-suffix=" DOF">0</span>
        <span class="stat-item__lbl">roboto laisvės laipsniai</span>
      </div>
      <div class="stat-item__div" aria-hidden="true"></div>
      <div class="stat-item">
        <span class="stat-item__val" data-count="24" data-suffix=" val.">0</span>
        <span class="stat-item__lbl">atsakymo laikas</span>
      </div>
      <div class="stat-item__div" aria-hidden="true"></div>
      <div class="stat-item">
        <span class="stat-item__val" data-count="0" data-suffix=" €">0</span>
        <span class="stat-item__lbl">už transportą</span>
      </div>
    </div>
  </div>

  <!-- MARQUEE -->
  <div class="marquee" aria-hidden="true">
    <div class="marquee__track">
      <span class="marquee__item">UNITREE G1</span><span class="marquee__sep">·</span>
      <span class="marquee__item">HUMANOIDAS</span><span class="marquee__sep">·</span>
      <span class="marquee__item">VISA LIETUVA</span><span class="marquee__sep">·</span>
      <span class="marquee__item">RENGINIAI</span><span class="marquee__sep">·</span>
      <span class="marquee__item">KONFERENCIJOS</span><span class="marquee__sep">·</span>
      <span class="marquee__item">PARODOS</span><span class="marquee__sep">·</span>
      <span class="marquee__item">GALA VAKARAI</span><span class="marquee__sep">·</span>
      <span class="marquee__item">PASIRODYMAI</span><span class="marquee__sep">·</span>
      <span class="marquee__item">RETAIL</span><span class="marquee__sep">·</span>
      <span class="marquee__item">ŽENKLINIMAS</span><span class="marquee__sep">·</span>
      <span class="marquee__item">43 DOF</span><span class="marquee__sep">·</span>
      <span class="marquee__item">132 CM</span><span class="marquee__sep">·</span>
      <span class="marquee__item">UNITREE G1</span><span class="marquee__sep">·</span>
      <span class="marquee__item">HUMANOIDAS</span><span class="marquee__sep">·</span>
      <span class="marquee__item">VISA LIETUVA</span><span class="marquee__sep">·</span>
      <span class="marquee__item">RENGINIAI</span><span class="marquee__sep">·</span>
      <span class="marquee__item">KONFERENCIJOS</span><span class="marquee__sep">·</span>
      <span class="marquee__item">PARODOS</span><span class="marquee__sep">·</span>
      <span class="marquee__item">GALA VAKARAI</span><span class="marquee__sep">·</span>
      <span class="marquee__item">PASIRODYMAI</span><span class="marquee__sep">·</span>
      <span class="marquee__item">RETAIL</span><span class="marquee__sep">·</span>
      <span class="marquee__item">ŽENKLINIMAS</span><span class="marquee__sep">·</span>
      <span class="marquee__item">43 DOF</span><span class="marquee__sep">·</span>
      <span class="marquee__item">132 CM</span><span class="marquee__sep">·</span>
    </div>
  </div>

  <!-- ŽINIASKLAIDA -->
  <section class="section" id="ziniasklaida" style="padding-top:var(--s8); padding-bottom:var(--s8);">
    <div style="max-width:1000px; margin:0 auto; text-align:center;">
      <p style="font-size:0.75rem; font-weight:700; letter-spacing:0.14em; text-transform:uppercase; color:var(--text-3); margin-bottom:var(--s5);">Mus rodė nacionalinė televizija</p>
      <div style="display:flex; flex-wrap:wrap; align-items:stretch; justify-content:center; gap:var(--s4);">
        <a href="https://gdansk.tvp.pl/93950197/pan-mecenas-robot" target="_blank" rel="noopener noreferrer" style="display:flex; flex-direction:column; gap:4px; padding:var(--s4) var(--s6); background:var(--surface-2); border:1px solid var(--border-mid); border-radius:12px; text-decoration:none; min-width:240px; text-align:left;">
          <span style="font-size:0.7rem; font-weight:700; letter-spacing:0.08em; text-transform:uppercase; color:var(--text-3);">TVP Gdańsk · Reportažas</span>
          <span style="font-size:1.05rem; font-weight:700; color:var(--text);">„Pan Mecenas Robot“ →</span>
        </a>
        <a href="https://www.tiktok.com/@teleexpress.tvp/video/7654958168786619680" target="_blank" rel="noopener noreferrer" style="display:flex; flex-direction:column; gap:4px; padding:var(--s4) var(--s6); background:var(--surface-2); border:1px solid var(--border-mid); border-radius:12px; text-decoration:none; min-width:240px; text-align:left;">
          <span style="font-size:0.7rem; font-weight:700; letter-spacing:0.08em; text-transform:uppercase; color:var(--text-3);">Teleexpress TVP · Video</span>
          <span style="font-size:1.05rem; font-weight:700; color:var(--text);">Mūsų robotas per žinias →</span>
        </a>
      </div>
      <p style="margin-top:var(--s5); color:var(--text-2); font-size:0.95rem; max-width:660px; margin-left:auto; margin-right:auto; line-height:1.7;">Mūsų humanoidinis robotas Unitree G1 pateko į Lenkijos nacionalinės televizijos laidas — <strong style="color:var(--text);">Teleexpress</strong> reportažą ir <strong style="color:var(--text);">TVP Gdańsk</strong> reportažą „Pan Mecenas Robot“, filmuotą per mūsų kliento renginį.</p>
      <div style="display:flex; flex-wrap:wrap; justify-content:center; align-items:flex-start; gap:var(--s6); margin-top:var(--s7);">
        <div style="background:var(--surface-2); border:1px solid var(--border-mid); border-radius:16px; overflow:hidden; width:min(340px,90vw);">
          <iframe loading="lazy" src="https://www.tiktok.com/embed/v2/7654958168786619680" title="Teleexpress TVP — 33bots humanoidinis robotas" style="width:100%; height:580px; border:0; display:block;" allow="encrypted-media; picture-in-picture" allowfullscreen></iframe>
          <div style="padding:var(--s3) var(--s4); text-align:left;">
            <span style="font-size:0.7rem; font-weight:700; letter-spacing:0.08em; text-transform:uppercase; color:var(--text-3);">Teleexpress TVP</span>
            <p style="font-size:0.95rem; font-weight:700; color:var(--text); margin:4px 0 0;">Robotas per nacionalines žinias</p>
          </div>
        </div>
        <div style="background:var(--surface-2); border:1px solid var(--border-mid); border-radius:16px; overflow:hidden; width:min(340px,90vw);">
          <iframe loading="lazy" src="https://www.instagram.com/p/DZNfiWNseFm/embed/" title="33bots humanoidinis robotas WallStreet konferencijoje" style="width:100%; height:580px; border:0; display:block;" scrolling="no" allowtransparency="true" allowfullscreen></iframe>
          <div style="padding:var(--s3) var(--s4); text-align:left;">
            <span style="font-size:0.7rem; font-weight:700; letter-spacing:0.08em; text-transform:uppercase; color:var(--text-3);">Projektas · Instagram</span>
            <p style="font-size:0.95rem; font-weight:700; color:var(--text); margin:4px 0 0;">WallStreet 30 konferencija</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- PATIRTIS -->
  <section class="section" id="patirtis" style="padding-top:var(--s8); padding-bottom:var(--s8);">
    <div style="max-width:1000px; margin:0 auto; text-align:center;">
      <h2 style="font-size:0.75rem; font-weight:700; letter-spacing:0.14em; text-transform:uppercase; color:var(--text-3); margin-bottom:var(--s5);">Patirtis, kurią atsivežame į Lietuvą</h2>
      <div style="display:flex; flex-wrap:wrap; align-items:stretch; justify-content:center; gap:var(--s4);">
        <div style="display:flex; flex-direction:column; gap:4px; padding:var(--s4) var(--s6); background:var(--surface-2); border:1px solid var(--border-mid); border-radius:12px; min-width:220px; text-align:left;">
          <span style="font-size:0.7rem; font-weight:700; letter-spacing:0.08em; text-transform:uppercase; color:var(--text-3);">Švietimas · Women in Tech Summit</span>
          <span style="font-size:1.05rem; font-weight:700; color:var(--text);">Perspektywy fondas</span>
        </div>
        <div style="display:flex; flex-direction:column; gap:4px; padding:var(--s4) var(--s6); background:var(--surface-2); border:1px solid var(--border-mid); border-radius:12px; min-width:220px; text-align:left;">
          <span style="font-size:0.7rem; font-weight:700; letter-spacing:0.08em; text-transform:uppercase; color:var(--text-3);">Transportas ir logistika</span>
          <span style="font-size:1.05rem; font-weight:700; color:var(--text);">DSV</span>
        </div>
        <div style="display:flex; flex-direction:column; gap:4px; padding:var(--s4) var(--s6); background:var(--surface-2); border:1px solid var(--border-mid); border-radius:12px; min-width:220px; text-align:left;">
          <span style="font-size:0.7rem; font-weight:700; letter-spacing:0.08em; text-transform:uppercase; color:var(--text-3);">Technologijos · Fintech</span>
          <span style="font-size:1.05rem; font-weight:700; color:var(--text);">Cashify</span>
        </div>
        <div style="display:flex; flex-direction:column; gap:4px; padding:var(--s4) var(--s6); background:var(--surface-2); border:1px solid var(--border-mid); border-radius:12px; min-width:220px; text-align:left;">
          <span style="font-size:0.7rem; font-weight:700; letter-spacing:0.08em; text-transform:uppercase; color:var(--text-3);">Legal tech · Pasirodymas TV</span>
          <span style="font-size:1.05rem; font-weight:700; color:var(--text);">LEX AI</span>
        </div>
      </div>
      <p style="margin-top:var(--s5); color:var(--text-2); font-size:0.95rem; max-width:680px; margin-left:auto; margin-right:auto; line-height:1.7;">33bots humanoidiniai robotai jau dirbo <strong style="color:var(--text);">Perspektywy fondo</strong> organizuojamame Women in Tech Summit — didžiausioje women-in-tech konferencijoje Europoje, taip pat pasaulinio logistikos operatoriaus <strong style="color:var(--text);">DSV</strong>, <strong style="color:var(--text);">Cashify</strong> ir <strong style="color:var(--text);">LEX AI</strong> renginiuose. Pastarojo pasirodymas su mūsų robotu pateko į nacionalinės televizijos laidas. Tą pačią patirtį ir tą pačią įrangą dabar atvežame į Lietuvą.</p>
      <div style="display:flex; gap:var(--s5); justify-content:center; flex-wrap:wrap; margin-top:var(--s5);">
        <a href="video-realizacijos.html" style="display:inline-flex; color:var(--text); font-size:0.9rem; font-weight:600; text-decoration:underline; text-underline-offset:3px;">Pamatyti įrašus iš renginių →</a>
        <a href="apie-mus.html" style="display:inline-flex; color:var(--text); font-size:0.9rem; font-weight:600; text-decoration:underline; text-underline-offset:3px;">Daugiau apie 33bots →</a>
      </div>
    </div>
  </section>

  <!-- PASLAUGOS -->
  <section class="section tiles-section" id="paslaugos">
    <div class="section-header">
      <span class="tag">Paslaugos</span>
      <h2 class="section-title">Ką galime<br />padaryti jums</h2>
    </div>
    <div class="tiles">
      <div class="tile">
        <div class="tile__top">
          <svg class="tile__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
          <span class="tile__tag">Jūsų renginio žvaigždė</span>
        </div>
        <h3 class="tile__title">Robotas<br />renginiui</h3>
        <p class="tile__desc">Norite, kad apie jūsų renginį kalbėtų? G1 atvyks į konferenciją, atidarymą ar gala vakarą ir garantuotai surinks minią. Žmonės traukia telefonus, o įrašai plinta patys. <a href="robotas-renginiui.html" style="color:inherit; text-decoration:underline;">Robotas renginiui →</a></p>
        <a href="#kontaktai" class="tile__link">Sužinoti daugiau →</a>
      </div>
      <div class="tile tile--light">
        <div class="tile__top">
          <svg class="tile__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
          <span class="tile__tag">Ilgalaikiai projektai</span>
        </div>
        <h3 class="tile__title">Robotų<br />nuoma</h3>
        <p class="tile__desc">Turime Unitree G1 robotų parką nuomai — parodoms, prekybos centrams, rinkodaros kampanijoms ir filmavimams. <a href="humanoidinio-roboto-nuoma.html" style="color:inherit; text-decoration:underline;">Nuomos sąlygos →</a></p>
        <a href="#kontaktai" class="tile__link">Sužinoti daugiau →</a>
      </div>
      <div class="tile">
        <div class="tile__top">
          <svg class="tile__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/></svg>
          <span class="tile__tag">Pasiekiamumas, kurio nenupirksi</span>
        </div>
        <h3 class="tile__title">Turinys<br />socialiniams</h3>
        <p class="tile__desc">Humanoidinis robotas sukuria daugiau organinio pasiekiamumo nei dauguma influencerių kampanijų — ir tas turinys lieka jūsų.</p>
        <a href="#kontaktai" class="tile__link">Sužinoti daugiau →</a>
      </div>
    </div>
  </section>

  <!-- APIE MUS -->
  <section class="section onas-section" id="apie-mus">
    <div class="onas-head">
      <span class="tag">Apie mus</span>
      <h2 class="section-title">Renginių robotikos<br />pionieriai Baltijos šalyse</h2>
    </div>

    <div class="onas-body">
      <div class="onas-text">
        <p class="lead-text">33bots — įmonė, kurios vienintelė specializacija yra <a href="humanoidinio-roboto-nuoma.html">humanoidinių robotų Unitree G1 nuoma</a> renginiams, parodoms ir technologijų pristatymams. Nesame reklamos agentūra, kuri daro viską po truputį — darome vieną dalyką ir darome jį gerai.</p>
        <p class="body-text">Roboto nuoma iš 33bots visada reiškia pilną paslaugą: atvežame robotą į vietą, paskiriame operatorių visam renginio laikui ir pasirūpiname viskuo — nuo paruošimo iki finalinio pasirodymo. Dirbame Vilniuje, Kaune, Klaipėdoje, Šiauliuose, Panevėžyje ir bet kuriame kitame Lietuvos mieste. Jūs rūpinatės svečiais, mes — robotu.</p>
        <p class="body-text">Peržiūrėkite specializuotus pasiūlymus: <a href="robotas-parodoms.html">robotas parodoms ir mugėms</a> bei <a href="robotas-konferencijai.html">robotas konferencijoms ir gala vakarams</a>. Taip pat perskaitykite mūsų straipsnį: <a href="blog-kodel-robotas-renginyje.html">5 priežastys, kodėl jūsų renginiui reikia humanoido</a>.</p>
      </div>
      <ul class="onas-usps">
        <li>Sava įranga — jokių tarpininkų ir netikėtumų</li>
        <li>Skirtas operatorius visą renginio laiką</li>
        <li>Civilinės atsakomybės draudimas — ramybė abiem pusėms</li>
        <li>Projektai visuose Lietuvos regionuose</li>
        <li>Skaidri kaina be paslėptų mokesčių</li>
      </ul>
    </div>

    <div class="transport-callout">
      <div class="transport-callout__glow" aria-hidden="true"></div>
      <div class="transport-callout__left">
        <span class="transport-callout__eyebrow">Mūsų standartas</span>
        <p class="transport-callout__claim"><em>Nemokamas transportas</em><br />visoje<br />Lietuvoje.</p>
      </div>
      <div class="transport-callout__right">
        <p class="transport-callout__note">Jokių priemokų už kilometrus, jokio minimalaus atstumo, jokių paslėptų kaštų. Atvežame robotą į kiekvieną renginį — nuo Klaipėdos iki Visagino, nuo Palangos iki Druskininkų — ir už tai nepridedame nė vieno euro.</p>
        <ul class="transport-callout__stats">
          <li><strong>0 €</strong><span>už kilometrą</span></li>
          <li><strong>100%</strong><span>Lietuvos teritorijos</span></li>
          <li><strong>24 val.</strong><span>iki pasiūlymo</span></li>
        </ul>
        <a href="#kontaktai" class="btn-primary">Rezervuoti nemokamą atvykimą →</a>
      </div>
    </div>
  </section>

  <!-- ROBOTO GALERIJA -->
  <section class="section robot-gallery-section">
    <div class="section-header">
      <span class="tag">Robotas</span>
      <h2 class="section-title">Unitree G1 —<br />naujos kartos humanoidas</h2>
    </div>
    <div class="robot-gallery">
      <figure class="robot-gallery__main">
        <picture>
          <source srcset="robot-g1-960.webp 960w, robot-g1.webp 2390w" sizes="(min-width: 769px) 800px, 92vw" type="image/webp" />
          <img src="robot-g1.jpg"
               alt="Humanoidinis robotas Unitree G1 — sidabrinis humanoidas su mėlynu vizoriumi, nuoma renginiams Lietuvoje"
               width="800" height="800"
               loading="lazy" />
        </picture>
        <figcaption>Unitree G1 · 132 cm · 35 kg · 43 laisvės laipsniai</figcaption>
      </figure>
      <div class="robot-gallery__side">
        <figure class="robot-gallery__action">
          <picture>
            <source srcset="robot-g1-action.webp" type="image/webp" />
            <img src="robot-g1-action.jpg"
                 alt="Robotas Unitree G1 šokio choreografijoje — kadras iš tikro 33bots pasirodymo"
                 width="600" height="600"
                 loading="lazy" />
          </picture>
          <figcaption>Dinamiškos choreografijos ir pasirodymai gyvai</figcaption>
        </figure>
        <div class="robot-gallery__specs">
          <div class="robot-spec"><span class="robot-spec__val">132 cm</span><span class="robot-spec__lbl">Ūgis</span></div>
          <div class="robot-spec"><span class="robot-spec__val">35 kg</span><span class="robot-spec__lbl">Svoris</span></div>
          <div class="robot-spec"><span class="robot-spec__val">43</span><span class="robot-spec__lbl">DOF</span></div>
          <div class="robot-spec"><span class="robot-spec__val">2 m/s</span><span class="robot-spec__lbl">Greitis</span></div>
        </div>
      </div>
    </div>
    <p style="max-width:760px; margin:var(--s6) auto 0; text-align:center; color:var(--text-2); line-height:1.8;">Visa techninė specifikacija, palyginimas su kitais humanoidais ir paaiškinimas, kodėl G1 tinka renginiams — <a href="blog-unitree-g1-specifikacija.html" style="color:var(--text); text-decoration:underline; text-underline-offset:3px;">Unitree G1 apžvalgoje</a>.</p>
  </section>

"""

    html += gallery_section(
        lead="Ne renderiai ir ne gamintojo reklama — kadrai iš tikrų 33bots projektų: Women in Tech "
             "Summit, gala vakarai, LEX AI akcijos ir verslo renginiai. Kiekvienoje nuotraukoje "
             "matyti kliento ženklinimas, kuris į nuomos kainą įeina visada.")
    html += video_section()

    html += """  <!-- CITATA -->
  <div class="statement">
    <div class="statement__inner">
      <blockquote class="statement__quote">
        „Kai robotas įžengia į salę —<br />visi traukia telefonus."
      </blockquote>
      <p class="statement__sub">Tai ne metafora. Tai ataskaita iš kiekvieno mūsų aptarnauto renginio.</p>
      <a href="#kontaktai" class="btn-primary">Patikrinti laisvas datas →</a>
    </div>
  </div>

  <!-- PAKETAI -->
  <section class="section tiles-section" id="paketai">
    <div class="section-header">
      <span class="tag">Paketai</span>
      <h2 class="section-title">Pasirinkite savo<br />formatą</h2>
    </div>
    <div class="tiles tiles--packages">
      <div class="tile tile--pkg">
        <div class="tile__top">
          <span class="tile__tag">Iki 3 valandų</span>
        </div>
        <h3 class="tile__pkg-name">Impulsas</h3>
        <p class="tile__desc">Trumpas pasirodymas per konferencijos pertrauką arba stendo atidarymą. Idealu pirmam įspūdžiui.</p>
        <ul class="tile__list">
          <li>Robotas iki 3 val.</li>
          <li>Operatorius vietoje</li>
          <li>Trumpas pasirodymas</li>
          <li>Transportas visoje Lietuvoje</li>
        </ul>
        <a href="#kontaktai" class="tile__link">Klausti kainos →</a>
      </div>
      <div class="tile tile--pkg tile--pkg-featured">
        <div class="tile__top">
          <span class="tile__tag">Visa diena</span>
        </div>
        <h3 class="tile__pkg-name">Standartas</h3>
        <p class="tile__desc">Pilna paslauga, roboto ženklinimas ir pritaikytos choreografijos.</p>
        <ul class="tile__list">
          <li>Iki 8 valandų</li>
          <li>Operatorius + asistentas</li>
          <li>Bendravimas su svečiais</li>
          <li>Ženklinimas (logotipas / QR)</li>
          <li>Transportas visoje Lietuvoje</li>
        </ul>
        <a href="#kontaktai" class="tile__link">Klausti kainos →</a>
      </div>
      <div class="tile tile--pkg">
        <div class="tile__top">
          <span class="tile__tag">2–7+ dienų</span>
        </div>
        <h3 class="tile__pkg-name">Multi-Day</h3>
        <p class="tile__desc">Parodos, technologijų festivaliai, ilgos kampanijos. Robotas lieka su jumis kelias dienas.</p>
        <ul class="tile__list">
          <li>Kelių dienų nuoma</li>
          <li>Skirtas operatorius</li>
          <li>Pilnas pritaikymas</li>
          <li>Nemokamas transportas visoje Lietuvoje</li>
        </ul>
        <a href="#kontaktai" class="tile__link">Klausti kainos →</a>
      </div>
    </div>
    <p style="text-align:center; margin-top:var(--s6);"><a href="kainos.html" class="btn-ghost" style="display:inline-flex;">Kas įeina į kainą →</a></p>
  </section>

  <!-- ATSILIEPIMAI -->
  <section class="section testimonials-section">
    <div class="section-header">
      <span class="tag">Atsiliepimai</span>
      <h2 class="section-title">Ką sako<br />klientai</h2>
    </div>
    <div class="testimonials">
      <div class="testimonial">
        <p class="testimonial__quote">„Rezultatas pranoko drąsiausius lūkesčius. Susidomėjimas buvo milžiniškas visą renginio laiką — nesitikėjau, kad pritrauksime tiek dėmesio."</p>
        <div class="testimonial__meta">
          <span class="testimonial__name">Karolina M.</span>
          <span class="testimonial__role">Rinkodara · IT sektorius</span>
        </div>
      </div>
      <div class="testimonial">
        <p class="testimonial__quote">„Tai buvo vienas geriausių organizacinių sprendimų. Teigiamos dalyvių reakcijos ir jų įsitraukimas mums yra geriausias viso renginio įvertinimas."</p>
        <div class="testimonial__meta">
          <span class="testimonial__name">Piotr Z.</span>
          <span class="testimonial__role">Organizatorius · įmonės gala vakaras</span>
        </div>
      </div>
      <div class="testimonial">
        <p class="testimonial__quote">„Bendradarbiavimas virto neįtikėtinais pasiekiamumo skaičiais socialiniuose tinkluose. Tokio autentiško susidomėjimo tiesiog nenusipirksi."</p>
        <div class="testimonial__meta">
          <span class="testimonial__name">Magdalena T.</span>
          <span class="testimonial__role">PR vadovė · technologijų paroda</span>
        </div>
      </div>
    </div>
    <p style="max-width:700px; margin:var(--s6) auto 0; text-align:center; color:var(--text-3); font-size:0.85rem; line-height:1.7;">Atsiliepimai iš 33bots projektų Lenkijoje — ta pati įranga, ta pati komanda ir tas pats aptarnavimo standartas dirba ir Lietuvoje.</p>
  </section>

  <!-- KUR TINKA -->
  <section class="section" id="pritaikymas">
    <div class="section-header">
      <span class="tag">Pritaikymas</span>
      <h2 class="section-title">Kur G1<br />pasiteisina?</h2>
    </div>
    <div class="use-grid">
      <div class="use-item">
        <span class="use-num">01</span>
        <h3>Konferencijos ir forumai</h3>
        <p>Robotas kaip renginio vedėjas, gidas arba pramoga prie svečių registracijos.</p>
        <a href="robotas-konferencijai.html" class="tile__link" style="margin-top:var(--s2);display:inline-flex;">Konferencijų pasiūlymas →</a>
      </div>
      <div class="use-item">
        <span class="use-num">02</span>
        <h3>Parodos ir mugės</h3>
        <p>Pritraukite prie stendo dešimt kartų daugiau dėmesio nei bet kuris baneris.</p>
        <a href="robotas-parodoms.html" class="tile__link" style="margin-top:var(--s2);display:inline-flex;">Sužinoti daugiau →</a>
      </div>
      <div class="use-item">
        <span class="use-num">03</span>
        <h3>Įmonių šventės ir vestuvės</h3>
        <p>Vasaros šventės, jubiliejai, gala vakarai, vestuvės — pokalbių tema ilgam po renginio.</p>
        <a href="robotas-vestuvems.html" class="tile__link" style="margin-top:var(--s2);display:inline-flex;">Robotas vestuvėms →</a>
      </div>
      <div class="use-item">
        <span class="use-num">04</span>
        <h3>Atviros dienos ir švietimas</h3>
        <p>Mokyklos, universitetai, mokslo centrai — technologija, kurią galima pamatyti gyvai.</p>
      </div>
      <div class="use-item">
        <span class="use-num">05</span>
        <h3>Foto ir video sesijos</h3>
        <p>Reklaminė medžiaga su humanoidu. Kadrai, kurių niekas kitas neturi.</p>
      </div>
      <div class="use-item">
        <span class="use-num">06</span>
        <h3>Produkto pristatymai</h3>
        <p>Parduotuvės atidarymas ar įvaizdžio kampanija — G1 sukuria pasirodymą.</p>
        <a href="robotas-atidarymui.html" class="tile__link" style="margin-top:var(--s2);display:inline-flex;">Atidarymų pasiūlymas →</a>
      </div>
    </div>
  </section>

  <!-- PROCESAS -->
  <section class="section process-section" id="procesas">
    <div class="section-header">
      <span class="tag">Kaip tai veikia</span>
      <h2 class="section-title">Nuo užklausos<br />iki pasirodymo</h2>
    </div>
    <div class="process">
      <div class="process-step">
        <span class="process-step__n">01</span>
        <div>
          <h3>Parašykite mums</h3>
          <p>Forma arba el. paštas. Atsakysime per 24 val. su klausimais apie detales.</p>
        </div>
      </div>
      <div class="process-step">
        <span class="process-step__n">02</span>
        <div>
          <h3>Kaina ir data</h3>
          <p>Aptariame datą, vietą ir lūkesčius. Paruošiame individualų pasiūlymą.</p>
        </div>
      </div>
      <div class="process-step">
        <span class="process-step__n">03</span>
        <div>
          <h3>Sutartis ir avansas</h3>
          <p>Paprasta sutartis, aiškios sąlygos. Datą rezervuojate avansu.</p>
        </div>
      </div>
      <div class="process-step">
        <span class="process-step__n">04</span>
        <div>
          <h3>Robotas atvyksta</h3>
          <p>Atvežame G1, paruošiame, išbandome. Operatorius su jumis visą laiką.</p>
        </div>
      </div>
      <div class="process-step">
        <span class="process-step__n">05</span>
        <div>
          <h3>Pasirodymas</h3>
          <p>Svečiai sužavėti. Nuotraukos keliauja į socialinius tinklus. Jūs spindite.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- DEMO CTA -->
  <div class="video-teaser">
    <div class="video-teaser__content">
      <span class="tag">Gyvai</span>
      <h2 class="video-teaser__title">Norite pamatyti<br />G1 veikiantį?</h2>
      <a href="#kontaktai" class="btn-primary">Užsisakyti nemokamą konsultaciją →</a>
      <p class="video-teaser__note">Nemokama konsultacija · Atsakome per 24 val.</p>
    </div>
  </div>

"""

    html += faq_section(FAQ, title="Dažniausi<br />klausimai")

    html += f"""  <!-- BLOGAS -->
  <section class="section" id="blogas">
    <div class="section-header">
      <span class="tag">Blogas</span>
      <h2 class="section-title">Žinios apie renginių<br />robotus</h2>
    </div>
    <div class="tiles tiles--blog">
{BLOG_CARDS}
    </div>

    <div style="text-align:center; margin:0 0 var(--s10);">
      <a href="blog.html" class="btn-ghost" style="display:inline-flex;">Visi straipsniai →</a>
    </div>

    <!-- VISOS PASLAUGOS -->
    <div style="margin-top:var(--s8); max-width:900px; margin-left:auto; margin-right:auto;">
      <p style="font-size:0.75rem; color:var(--text-3); text-transform:uppercase; letter-spacing:0.1em; font-weight:700; margin-bottom:var(--s3);">Visos nuomos paslaugos</p>
      <div class="related-links">
{OFFER_CHIPS}
      </div>
    </div>

    <!-- MIESTAI -->
    <div style="margin-top:var(--s7); max-width:900px; margin-left:auto; margin-right:auto;">
      <p style="font-size:0.75rem; color:var(--text-3); text-transform:uppercase; letter-spacing:0.1em; font-weight:700; margin-bottom:var(--s3);">Robotų nuoma jūsų mieste — <a href="robotu-nuoma.html" style="color:var(--text-2); text-decoration:underline; text-underline-offset:3px;">visi {len(CITIES)} miestai</a></p>
      <div style="display:flex; flex-wrap:wrap; gap:var(--s2);">
{CITY_CHIPS}
      </div>
    </div>
  </section>

"""

    html += contact_section()
    html += footer()
    write("index.html", html)


if __name__ == "__main__":
    build()
