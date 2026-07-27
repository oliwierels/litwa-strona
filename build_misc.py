# -*- coding: utf-8 -*-
"""33bots.lt: kainos, apie mus, kontaktai, vaizdo įrašai, privatumo politika, 404."""
from lt_common import (SITE, EMAIL, PHONE_1, PHONE_1_H, PHONE_2, PHONE_2_H, head, body_open, nav,
                       crumbs, breadcrumb_ld, contact_section, footer, faq_section, faq_ld,
                       organization_ld, video_ld, write, esc, CITIES, city_url, SOCIALS)

VIDEOS = [
    ("33bots-robot-event", "Robotas renginyje — pilnas pasirodymas",
     "Humanoidinis robotas Unitree G1 renginyje: vaikšto tarp svečių, gestikuliuoja, pozuoja "
     "nuotraukoms ir atlieka choreografiją. Ant krūtinės — kliento logotipas ir QR kodas.", "PT35S"),
    ("robot-powitanie", "Svečių pasitikimas",
     "Robotas pasitinka atvykstančius svečius prie įėjimo — mostas, nusilenkimas ir pozavimas "
     "nuotraukoms. Populiariausias renginio pradžios scenarijus.", "PT15S"),
    ("robot-taniec", "Šokio choreografija",
     "Unitree G1 atlieka šokio choreografiją. Toks pasirodymas dažniausiai tampa gala vakaro ar "
     "įmonės šventės kulminacija.", "PT20S"),
    ("robot-gesty", "Gestai ir bendravimas",
     "Roboto gestai iš arti: rankos paspaudimas, mostai ir judesiai, kuriais robotas bendrauja su "
     "svečiais. 43 laisvės laipsniai judesio sklandumui.", "PT12S"),
    ("robot-spacer", "Judėjimas erdvėje",
     "Robotas juda po renginio erdvę tarp žmonių, apeidamas kliūtis. LiDAR jutikliai ir operatoriaus "
     "priežiūra užtikrina saugų darbą minioje.", "PT14S"),
    ("robot-branding", "Ženklinimas prekės ženklu",
     "Roboto ženklinimas kliento logotipu ir QR kodu ant krūtinės. Įskaičiuota į nuomos kainą — "
     "kiekvienas svečio įrašas dirba jūsų prekės ženklui.", "PT10S"),
]


def build_video_page():
    cards = "\n".join(f"""      <figure style="background:var(--surface-2); border:1px solid var(--border-mid); border-radius:16px; overflow:hidden; margin:0;">
        <video controls muted playsinline preload="none"
               poster="video/{f}-poster.jpg"
               width="360" height="640"
               style="width:100%; display:block; background:#000;"
               aria-label="{esc(t)} — humanoidinis robotas Unitree G1">
          <source src="video/{f}.mp4" type="video/mp4" />
          Jūsų naršyklė nepalaiko HTML5 vaizdo įrašų.
        </video>
        <figcaption style="padding:var(--s4);">
          <h2 style="font-size:1.05rem; font-weight:700; color:var(--text); margin:0 0 6px;">{t}</h2>
          <p style="font-size:0.9rem; color:var(--text-2); line-height:1.7; margin:0;">{d}</p>
        </figcaption>
      </figure>""" for f, t, d, _ in VIDEOS)

    ld = [organization_ld()] + [f"""{{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "{esc(t)} — humanoidinis robotas Unitree G1 | 33bots",
  "description": "{esc(d)}",
  "thumbnailUrl": "{SITE}/video/{f}-poster.jpg",
  "contentUrl": "{SITE}/video/{f}.mp4",
  "uploadDate": "2026-07-02",
  "duration": "{dur}",
  "inLanguage": "lt",
  "publisher": {{"@id": "{SITE}/#organizacija"}}
}}""" for f, t, d, dur in VIDEOS] + [
        breadcrumb_ld([("Pradžia", f"{SITE}/"), ("Vaizdo įrašai", f"{SITE}/video-realizacijos.html")])]

    html = head(title="Robotas renginyje — vaizdo įrašai iš pasirodymų | 33bots",
                description="Vaizdo įrašai su humanoidiniu robotu Unitree G1: svečių pasitikimas, šokio "
                            "choreografija, gestai ir ženklinimas. Pamatykite robotą gyvai.",
                slug="video-realizacijos.html",
                keywords="robotas video, humanoidinis robotas įrašai, Unitree G1 video, robotas renginyje video",
                og_image=f"{SITE}/og/video-realizacijos.jpg", extra_ld=ld,
                extra_head="")
    html += body_open()
    html += nav(active="video-realizacijos.html")
    html += crumbs([("Pradžia", "index.html"), ("Vaizdo įrašai", None)])
    html += f"""
  <section class="hero hero--sub">
    <div class="hero__content">
      <p class="hero__eyebrow">Vaizdo įrašai · Robotas gyvai</p>
      <h1 class="hero__title">Pamatykite robotą<br />prieš užsakydami.</h1>
      <p class="hero__sub">Šeši trumpi įrašai, kurie parodo, ką Unitree G1 realiai daro renginyje — nuo svečių pasitikimo iki choreografijos ir ženklinimo prekės ženklu.</p>
    </div>
  </section>

  <section class="section">
    <div style="max-width:1100px; margin:0 auto; display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:var(--s5);">
{cards}
    </div>
    <p style="max-width:760px; margin:var(--s8) auto 0; text-align:center; color:var(--text-2); line-height:1.8;">
      Norite pamatyti robotą gyvai prieš pasirašydami sutartį? Didesniems projektams organizuojame demonstraciją arba vaizdo skambutį su robotu — <a href="#kontaktai" style="color:var(--text); text-decoration:underline; text-underline-offset:3px;">parašykite mums</a>.
    </p>
  </section>

"""
    html += contact_section()
    html += footer()
    write("video-realizacijos.html", html)


def build_pricing():
    faq = [
        ("Kodėl kainos nėra nurodytos tiesiogiai svetainėje?",
         "Nes vienos teisingos kainos nėra: trijų valandų pasirodymas ir kelių dienų paroda yra "
         "skirtingi produktai. Vietoj bendro kainoraščio pateikiame konkrečią kainą per 24 valandas "
         "po užklausos."),
        ("Ar transportas tikrai kainuoja 0 €?",
         "Taip, visoje Lietuvoje. Nėra kilometrų limito, minimalaus atstumo ar priemokos už tolimesnius "
         "miestus — kaina Vilniuje ir Mažeikiuose vienoda."),
        ("Ar ženklinimas kainuoja papildomai?",
         "Ne. Logotipas ir QR kodas ant roboto krūtinės įeina į standartinį paketą, kad ir kiek kartų "
         "juos keistume prieš renginį."),
        ("Ar kainos nurodomos su PVM?",
         "Pasiūlyme visada aiškiai nurodome sumą be PVM ir su PVM, kad nekiltų neaiškumų derinant "
         "biudžetą."),
        ("Ar galima mokėti po renginio?",
         "Datą rezervuojame avansu — tai standartinė renginių rinkos praktika. Likusios sumos mokėjimo "
         "terminą derinam individualiai, dažnai pagal jūsų vidines apskaitos taisykles."),
        ("Kas nutinka, jei renginys perkeliamas?",
         "Datos perkėlimo sąlygas numatome sutartyje. Stengiamės būti lankstūs — perkelti renginį "
         "beveik visada lengviau nei jį atšaukti."),
    ]
    ld = [organization_ld(), faq_ld(faq),
          breadcrumb_ld([("Pradžia", f"{SITE}/"), ("Kainos", f"{SITE}/kainos.html")]),
          f"""{{
  "@context": "https://schema.org",
  "@type": "OfferCatalog",
  "name": "33bots humanoidinio roboto nuomos paketai",
  "url": "{SITE}/kainos.html",
  "provider": {{"@id": "{SITE}/#organizacija"}},
  "itemListElement": [
    {{"@type": "Offer", "name": "Impulsas — iki 3 val.", "priceCurrency": "EUR",
      "description": "Trumpas pasirodymas: robotas, operatorius, transportas.", "url": "{SITE}/kainos.html"}},
    {{"@type": "Offer", "name": "Standartas — iki 8 val.", "priceCurrency": "EUR",
      "description": "Visa renginio diena su ženklinimu ir bendravimu su svečiais.", "url": "{SITE}/kainos.html"}},
    {{"@type": "Offer", "name": "Multi-Day — 2–7+ dienų", "priceCurrency": "EUR",
      "description": "Parodos ir ilgesnės kampanijos su skirtu operatoriumi.", "url": "{SITE}/kainos.html"}}
  ]
}}"""]

    html = head(title="Roboto nuomos kainos ir paketai — kas įeina | 33bots",
                description="Humanoidinio roboto nuomos paketai Lietuvoje: kas įeina į kainą, nuo ko "
                            "priklauso pasiūlymas ir kodėl transportas kainuoja 0 €. Kaina per 24 val.",
                slug="kainos.html",
                keywords="roboto nuomos kaina, robotų nuomos paketai, kiek kainuoja robotas renginiui",
                og_image=f"{SITE}/og/kainos.jpg", extra_ld=ld,
                extra_head="")
    html += body_open()
    html += nav(active="kainos.html")
    html += crumbs([("Pradžia", "index.html"), ("Kainos", None)])
    html += """
  <section class="hero hero--sub">
    <div class="hero__content">
      <p class="hero__eyebrow">Kainos · Paketai · Kas įeina</p>
      <h1 class="hero__title">Kainos be<br />žvaigždučių.</h1>
      <p class="hero__sub">Nepateikiame vienos kainos už robotą, nes jos nėra — bet pateikiame tikslią kainą per 24 valandas ir aiškiai pasakome, kas į ją įeina. Ir kas neįeina.</p>
      <div class="hero__ctas">
        <a href="#kontaktai" class="btn-primary">Gauti kainą per 24 val.</a>
        <a href="#paketai" class="btn-ghost">Paketai ↓</a>
      </div>
    </div>
  </section>

  <section class="section tiles-section" id="paketai">
    <div class="section-header">
      <span class="tag">Paketai</span>
      <h2 class="section-title">Trys formatai,<br />viena logika</h2>
    </div>
    <div class="tiles tiles--packages">
      <div class="tile tile--pkg">
        <div class="tile__top"><span class="tile__tag">Iki 3 valandų</span></div>
        <h3 class="tile__pkg-name">Impulsas</h3>
        <p class="tile__desc">Trumpas pasirodymas per konferencijos pertrauką, stendo atidarymą arba vakaro akcentą.</p>
        <ul class="tile__list">
          <li>Robotas iki 3 val.</li>
          <li>Operatorius vietoje</li>
          <li>Vienas pasirodymas + nuotraukos</li>
          <li>Transportas — 0 €</li>
        </ul>
        <a href="#kontaktai" class="tile__link">Klausti kainos →</a>
      </div>
      <div class="tile tile--pkg tile--pkg-featured">
        <div class="tile__top"><span class="tile__tag">Populiariausias</span></div>
        <h3 class="tile__pkg-name">Standartas</h3>
        <p class="tile__desc">Visa renginio diena: pasirodymai ciklais, bendravimas su svečiais ir pilnas ženklinimas.</p>
        <ul class="tile__list">
          <li>Iki 8 valandų</li>
          <li>Operatorius + asistentas</li>
          <li>Ženklinimas (logotipas + QR)</li>
          <li>Individualus scenarijus</li>
          <li>Transportas — 0 €</li>
        </ul>
        <a href="#kontaktai" class="tile__link">Klausti kainos →</a>
      </div>
      <div class="tile tile--pkg">
        <div class="tile__top"><span class="tile__tag">2–7+ dienų</span></div>
        <h3 class="tile__pkg-name">Multi-Day</h3>
        <p class="tile__desc">Parodos, festivaliai ir ilgesnės kampanijos su ta pačia komanda visą laiką.</p>
        <ul class="tile__list">
          <li>Kelių dienų nuoma</li>
          <li>Skirtas operatorius</li>
          <li>Pilnas pritaikymas</li>
          <li>Visa logistika — 0 €</li>
        </ul>
        <a href="#kontaktai" class="tile__link">Klausti kainos →</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="article-body">
      <h2>Kas visada įeina į kainą</h2>
      <ul>
        <li><strong>Robotas Unitree G1</strong> su baterijomis, valdymu ir garso sistema.</li>
        <li><strong>Sertifikuotas operatorius</strong> visą renginio laiką — ne tik paleidimui.</li>
        <li><strong>Transportas</strong> į bet kurią Lietuvos vietą ir atgal.</li>
        <li><strong>Paruošimas vietoje</strong> ir bandomasis paleidimas prieš renginį.</li>
        <li><strong>Ženklinimas</strong> jūsų logotipu ir QR kodu.</li>
        <li><strong>Scenarijaus derinimas</strong> prieš renginį.</li>
        <li><strong>Civilinės atsakomybės draudimo apsauga</strong> veiklai.</li>
      </ul>

      <h2>Kas gali kainuoti papildomai</h2>
      <p>Sąžiningumo dėlei — situacijos, kuriose kaina didėja, ir jos visada aptariamos iš anksto:</p>
      <ul>
        <li>Antras robotas arba antras operatorius dideliems renginiams.</li>
        <li>Nakvynė ir logistika, kai renginys prasideda labai anksti kitame šalies gale.</li>
        <li>Specialiai kuriama choreografija pagal jūsų muziką.</li>
        <li>Roboto darbas trumpesniais intervalais keliose vietose tą pačią dieną.</li>
      </ul>
      <div class="callout"><p>Ko <strong>niekada</strong> nepridedame prie sąskaitos: mokesčio už kilometrus, priemokos už savaitgalį, mokesčio už ženklinimą ar „aptarnavimo mokesčio“, kurio nebuvo pasiūlyme.</p></div>

      <h2>Nuo ko priklauso galutinė kaina</h2>
      <p>Keturi kintamieji: <strong>trukmė</strong>, <strong>formatas</strong> (statiška zona ar pasirodymas scenoje), <strong>data</strong> (sezonas ar ne) ir <strong>papildomos paslaugos</strong>. Detalų paaiškinimą su lentelėmis rasite straipsnyje <a href="blog-kiek-kainuoja-roboto-nuoma.html">kiek kainuoja roboto nuoma</a>.</p>
      <p>Jei lyginate kelis pasiūlymus, naudingas bus ir mūsų <a href="blog-kaip-issinuomoti-robota.html">nuomos vadovas</a> — jame surinkti klausimai, kuriuos verta užduoti kiekvienam tiekėjui.</p>
    </div>
  </section>

"""
    html += faq_section(faq, title="Klausimai apie<br />kainas")
    html += contact_section(heading="Gaukite tikslią kainą<br />per 24 valandas.")
    html += footer()
    write("kainos.html", html)


def build_about():
    ld = [organization_ld(),
          breadcrumb_ld([("Pradžia", f"{SITE}/"), ("Apie mus", f"{SITE}/apie-mus.html")]),
          f"""{{
  "@context": "https://schema.org",
  "@type": "AboutPage",
  "name": "Apie 33bots",
  "url": "{SITE}/apie-mus.html",
  "inLanguage": "lt-LT",
  "mainEntity": {{"@id": "{SITE}/#organizacija"}}
}}"""]

    html = head(title="Apie 33bots — humanoidinių robotų nuoma renginiams Lietuvoje",
                description="Kas yra 33bots: viena specializacija — humanoidinių robotų nuoma "
                            "renginiams. Sava įranga, savi operatoriai, patirtis tarptautiniuose "
                            "renginiuose.",
                slug="apie-mus.html",
                keywords="33bots, apie mus, robotų nuomos įmonė, humanoidiniai robotai Lietuvoje",
                og_image=f"{SITE}/og/apie-mus.jpg", extra_ld=ld,
                extra_head="")
    html += body_open()
    html += nav(active="apie-mus.html")
    html += crumbs([("Pradžia", "index.html"), ("Apie mus", None)])
    html += """
  <section class="hero hero--sub">
    <div class="hero__content">
      <p class="hero__eyebrow">Apie mus · Viena specializacija</p>
      <h1 class="hero__title">Darome vieną dalyką.<br />Ir darome jį gerai.</h1>
      <p class="hero__sub">33bots nėra renginių agentūra, kuri tarp kitko turi robotą. Humanoidinių robotų nuoma yra vienintelė mūsų veikla — nuo pirmos dienos.</p>
    </div>
  </section>

  <section class="section">
    <div class="article-body">
      <h2>Kas mes esame</h2>
      <p>33bots — įmonė, specializuota <a href="humanoidinio-roboto-nuoma.html">humanoidinių robotų Unitree G1 nuomoje</a> renginiams, parodoms ir rinkodaros projektams. Dirbame su sava įranga ir savo operatoriais: kai užsakote robotą, jį atveža ir valdo tie patys žmonės, su kuriais derinote scenarijų.</p>
      <p>Tai svarbu, nes rinkoje veikia ir tarpininkų modelis, kai užsakymas perduodamas trečiajai šaliai. Tokiu atveju niekas negali garantuoti nei įrangos būklės, nei operatoriaus patirties. Mes garantuojame abu.</p>

      <h2>Iš kur mūsų patirtis</h2>
      <p>33bots robotai jau dirbo tarptautiniuose renginiuose Lenkijoje — tarp jų Perspektywy fondo organizuotame <strong>Women in Tech Summit</strong>, didžiausioje women-in-tech konferencijoje Europoje, taip pat pasaulinio logistikos operatoriaus <strong>DSV</strong>, <strong>Cashify</strong> ir <strong>LEX AI</strong> projektuose. Pastarojo pasirodymas su mūsų robotu pateko į nacionalinės televizijos laidas.</p>
      <p>Į Lietuvą atvežame tą pačią įrangą, tuos pačius standartus ir tuos pačius operatorius. Skirtumas tik vienas — čia dirbame lietuvių kalba ir su vietiniu kontekstu.</p>

      <h2>Kuo skiriamės</h2>
      <ul>
        <li><strong>Sava įranga.</strong> Jokių tarpininkų grandinių ir netikėtumų renginio dieną.</li>
        <li><strong>Operatorius visą laiką.</strong> Ne tik atvežimui — visą renginį.</li>
        <li><strong>Transportas 0 €.</strong> Visoje Lietuvoje, be kilometrų limito.</li>
        <li><strong>Ženklinimas įskaičiuotas.</strong> Logotipas ir QR kodas be priemokų.</li>
        <li><strong>Skaidrus pasiūlymas.</strong> Kaina su PVM ir be jo, be paslėptų punktų.</li>
        <li><strong>Atsakymas per 24 val.</strong> Kiekvieną darbo dieną.</li>
      </ul>

      <h2>Kaip dirbame su agentūromis</h2>
      <p>Didelė dalis mūsų projektų ateina per renginių agentūras. Joms svarbu, kad tiekėjas pats pateiktų techninę specifikaciją, saugos informaciją ir suderintų viską su objekto administracija — visa tai darome be atskiro prašymo. Saugos klausimus išsamiai aprašėme <a href="blog-roboto-sauga-renginyje.html">saugos vadove</a>.</p>

      <h2>Kur dirbame</h2>
      <p>Visoje Lietuvoje — nuo Vilniaus ir Kauno iki Mažeikių, Palangos ar Druskininkų. Miestų puslapiuose rasite konkrečią informaciją apie vietos renginių sceną ir tipines erdves.</p>
    </div>
  </section>

"""
    chips = "\n".join(f'        <a href="{city_url(s)}">{n}</a>' for s, n, _, _ in CITIES)
    html += f"""  <section class="section" style="padding-top:0;">
    <div style="max-width:900px; margin:0 auto;">
      <p style="font-size:0.75rem; color:var(--text-3); text-transform:uppercase; letter-spacing:0.1em; font-weight:700; margin-bottom:var(--s3);">Robotų nuoma miestuose</p>
      <div class="related-links">
{chips}
      </div>
    </div>
  </section>

"""
    html += contact_section()
    html += footer()
    write("apie-mus.html", html)


def build_contacts():
    socials = "\n".join(
        f'        <a href="{u}" target="_blank" rel="noopener noreferrer">{n} →</a>' for n, u in SOCIALS)
    chips = "\n".join(f'        <a href="{city_url(s)}">{n}</a>' for s, n, _, _ in CITIES)
    ld = [organization_ld(),
          breadcrumb_ld([("Pradžia", f"{SITE}/"), ("Kontaktai", f"{SITE}/kontaktai.html")]),
          f"""{{
  "@context": "https://schema.org",
  "@type": "ContactPage",
  "name": "33bots kontaktai",
  "url": "{SITE}/kontaktai.html",
  "inLanguage": "lt-LT",
  "mainEntity": {{"@id": "{SITE}/#organizacija"}}
}}"""]

    html = head(title="Kontaktai — humanoidinio roboto nuoma Lietuvoje | 33bots",
                description="Susisiekite dėl humanoidinio roboto nuomos renginiui: el. paštas, telefonas "
                            "ir užklausos forma. Atsakome per 24 darbo valandas. Aptarnaujame visą Lietuvą.",
                slug="kontaktai.html",
                keywords="33bots kontaktai, roboto nuoma kontaktai, susisiekti robotų nuoma",
                og_image=f"{SITE}/og/kontaktai.jpg", extra_ld=ld,
                extra_head="")
    html += body_open()
    html += nav(active="kontaktai.html")
    html += crumbs([("Pradžia", "index.html"), ("Kontaktai", None)])
    html += f"""
  <section class="hero hero--sub">
    <div class="hero__content">
      <p class="hero__eyebrow">Kontaktai · Atsakome per 24 val.</p>
      <h1 class="hero__title">Susisiekime.</h1>
      <p class="hero__sub">Parašykite renginio datą, miestą ir formatą — atsakysime per vieną darbo dieną su konkrečia kaina ir laisvomis datomis. Be įkyrių skambučių.</p>
    </div>
  </section>

  <section class="section" style="padding-top:0;">
    <div style="max-width:1000px; margin:0 auto; display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:var(--s6);">
      <div class="article-body" style="max-width:none;">
        <h2>Tiesioginiai kontaktai</h2>
        <p><strong>El. paštas:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a><br />
        <strong>Telefonas:</strong> <a href="tel:{PHONE_1}">{PHONE_1_H}</a><br />
        <strong>Telefonas:</strong> <a href="tel:{PHONE_2}">{PHONE_2_H}</a></p>
        <p>Dirbame darbo dienomis, o renginių savaitgaliais esame pasiekiami telefonu.</p>
        <h3>Socialiniai tinklai</h3>
        <div class="related-links">
{socials}
        </div>
      </div>
      <div class="article-body" style="max-width:none;">
        <h2>Ką parašyti užklausoje</h2>
        <p>Kad galėtume atsakyti tiksliai jau pirmu laišku, naudinga nurodyti:</p>
        <ul>
          <li>Renginio <strong>datą</strong> ir valandas</li>
          <li><strong>Miestą</strong> ir vietą (salė, stendas, lauko erdvė)</li>
          <li>Apytikslį <strong>svečių skaičių</strong></li>
          <li>Renginio <strong>tipą</strong> — paroda, konferencija, šventė, atidarymas</li>
          <li>Ko tikitės: pramogos svečiams, kontaktų rinkimo ar turinio soc. tinklams</li>
        </ul>
        <p>Jei dar ne visko žinote — tai visiškai normalu. Parašykite, ką turite, ir likusius klausimus užduosime patys.</p>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0;">
    <div style="max-width:900px; margin:0 auto;">
      <p style="font-size:0.75rem; color:var(--text-3); text-transform:uppercase; letter-spacing:0.1em; font-weight:700; margin-bottom:var(--s3);">Aptarnaujami miestai</p>
      <div class="related-links">
{chips}
      </div>
      <p style="color:var(--text-3); font-size:0.85rem; margin-top:var(--s3);">Sąrašas nėra baigtinis — atvykstame į bet kurią Lietuvos vietą, ir transportas visada įskaičiuotas.</p>
    </div>
  </section>

"""
    html += contact_section(heading="Užklausos forma",
                            lead="Užpildykite formą — atsakysime per vieną darbo dieną su kaina ir laisvomis datomis.")
    html += footer()
    write("kontaktai.html", html)


def build_privacy():
    ld = [organization_ld(),
          breadcrumb_ld([("Pradžia", f"{SITE}/"), ("Privatumo politika", f"{SITE}/privatumo-politika.html")])]
    html = head(title="Privatumo politika ir slapukai | 33bots",
                description="Kaip 33bots tvarko asmens duomenis, gautus per kontaktinę formą, ir kokius "
                            "slapukus naudoja svetainė 33bots.lt.",
                slug="privatumo-politika.html", og_image=f"{SITE}/og-image.jpg", extra_ld=ld,
                extra_head="")
    html += body_open()
    html += nav()
    html += crumbs([("Pradžia", "index.html"), ("Privatumo politika", None)])
    html += f"""
  <section class="hero hero--sub">
    <div class="hero__content">
      <p class="hero__eyebrow">Teisinė informacija</p>
      <h1 class="hero__title">Privatumo politika<br />ir slapukai.</h1>
    </div>
  </section>

  <section class="section">
    <div class="article-body">
      <h2>Duomenų valdytojas</h2>
      <p>Svetainę 33bots.lt administruoja 33bots. Klausimais dėl asmens duomenų rašykite adresu <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

      <h2>Kokius duomenis renkame</h2>
      <p>Per kontaktinę formą renkame duomenis, kuriuos pateikiate patys: vardą ir pavardę, įmonės pavadinimą, el. pašto adresą, telefono numerį bei informaciją apie planuojamą renginį. Šie duomenys naudojami tik tam, kad galėtume atsakyti į jūsų užklausą ir pateikti pasiūlymą.</p>
      <p>Papildomai svetainė renka techninius duomenis apie naršymą (puslapio peržiūros, apytikslė vietovė, įrenginio tipas) analitikos tikslais.</p>

      <h2>Teisinis pagrindas ir saugojimo terminas</h2>
      <p>Užklausos duomenys tvarkomi siekiant imtis veiksmų jūsų prašymu prieš sudarant sutartį, taip pat teisėto intereso pagrindu — atsakyti į verslo užklausas. Duomenis saugome tiek, kiek reikia susirašinėjimui ir galimam bendradarbiavimui, o vėliau juos ištriname.</p>

      <h2>Duomenų gavėjai</h2>
      <p>Kontaktinės formos duomenys perduodami formų apdorojimo paslaugos teikėjui (Formspree), kuris persiunčia juos į mūsų el. paštą. Analitikos duomenys tvarkomi per Google Tag Manager ir susietus analitikos įrankius. Duomenų neparduodame ir neperduodame tretiesiems asmenims rinkodaros tikslais.</p>

      <h2>Jūsų teisės</h2>
      <p>Turite teisę susipažinti su savo duomenimis, prašyti juos ištaisyti ar ištrinti, apriboti tvarkymą, nesutikti su tvarkymu ir perkelti duomenis. Norėdami pasinaudoti šiomis teisėmis, rašykite <a href="mailto:{EMAIL}">{EMAIL}</a>. Taip pat turite teisę pateikti skundą Valstybinei duomenų apsaugos inspekcijai.</p>

      <h2>Slapukai</h2>
      <p>Svetainėje naudojami:</p>
      <ul>
        <li><strong>Būtinieji</strong> — reikalingi svetainės veikimui ir jūsų pasirinkimo dėl slapukų juostos įsiminimui (saugoma jūsų naršyklėje).</li>
        <li><strong>Analitiniai</strong> — padeda suprasti, kaip lankytojai naudojasi svetaine, kad galėtume ją tobulinti.</li>
        <li><strong>Rinkodaros</strong> — naudojami lankytojų srauto analizei verslo klientų kontekste.</li>
      </ul>
      <p>Slapukus galite bet kada ištrinti ar blokuoti savo naršyklės nustatymuose. Išjungus dalį slapukų kai kurios svetainės funkcijos gali veikti ribotai.</p>

      <h2>Pakeitimai</h2>
      <p>Šią politiką galime atnaujinti — aktuali versija visada skelbiama šiame puslapyje.</p>
    </div>
  </section>

"""
    html += footer()
    write("privatumo-politika.html", html)


def build_404():
    links = "\n".join(f'        <a href="{u}">{t} →</a>' for u, t in [
        ("index.html", "Pradžia"),
        ("humanoidinio-roboto-nuoma.html", "Humanoidinio roboto nuoma"),
        ("robotas-renginiui.html", "Robotas renginiui"),
        ("robotas-parodoms.html", "Robotas parodoms"),
        ("kainos.html", "Kainos"),
        ("blog.html", "Blogas"),
        ("kontaktai.html", "Kontaktai"),
    ])
    html = head(title="Puslapis nerastas (404) | 33bots",
                description="Tokio puslapio nėra. Grįžkite į pradžią arba pasirinkite vieną iš pagrindinių skyrių.",
                slug="404.html", og_image=f"{SITE}/og-image.jpg",
                extra_head="").replace('<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />',
             '<meta name="robots" content="noindex, follow" />')
    html += body_open()
    html += nav()
    html += f"""
  <section class="hero hero--sub">
    <div class="hero__content">
      <p class="hero__eyebrow">Klaida 404</p>
      <h1 class="hero__title">Šio puslapio<br />nėra.</h1>
      <p class="hero__sub">Nuoroda gali būti pasenusi arba adrese įsivėlė klaida. Robotas vis dar veikia — tik ne šiuo adresu.</p>
      <div class="hero__ctas">
        <a href="index.html" class="btn-primary">Grįžti į pradžią</a>
        <a href="kontaktai.html" class="btn-ghost">Susisiekti</a>
      </div>
      <div class="related-links" style="margin-top:var(--s6);">
{links}
      </div>
    </div>
  </section>

"""
    html += footer()
    write("404.html", html)


def build():
    build_video_page()
    build_pricing()
    build_about()
    build_contacts()
    build_privacy()
    build_404()


if __name__ == "__main__":
    build()
