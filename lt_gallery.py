# -*- coding: utf-8 -*-
"""Nuotraukos iš tikrų 33bots realizacijų ir jų atvaizdavimas.

Nuotraukos perimtos iš vokiškos 33bots versijos — tai tie patys kadrai iš realių renginių
(Women in Tech Summit, gala vakarai, LEX AI, verslo susitikimai).
"""
from lt_common import SITE, esc

DIR = "nuotraukos"

# (failas, klasė, antraštė, alt tekstas)
# Klasės atitinka vokiškos versijos išdėstymą: plati / siaura / standartinė plytelė.
PHOTOS = [
    ("realizacja-women-in-tech-tlum", "shot shot--wide",
     "Visi traukia telefonus",
     "Women in Tech Summit dalyvės filmuoja humanoidinį robotą telefonais"),
    ("realizacja-gala-czerwony-dywan", "shot",
     "Raudonas kilimas",
     "Humanoidinis robotas blizgančiu smokingu ant gala vakaro raudonojo kilimo"),
    ("realizacja-women-in-tech-wybieg", "shot",
     "Women in Tech Summit",
     "Humanoidinis robotas ant rožinio podiumo Women in Tech Summit renginyje prieš publiką"),
    ("realizacja-lexai-starowka", "shot shot--wide",
     "Gatvė sustoja",
     "Humanoidinis robotas su LEX AI marškinėliais senamiestyje — praeiviai jį fotografuoja"),
    ("realizacja-gala-detal", "shot shot--narrow",
     "Iki smulkmenų",
     "Humanoidinio roboto stambus planas su karūna ir blizgančiu smokingu"),
    ("realizacja-gala-zdjecia-gosci", "shot shot--wide",
     "Eilė prie nuotraukų zonos",
     "Gala vakaro svečiai fotografuoja humanoidinį robotą prie rėmėjų sienos"),
    ("realizacja-robot-gala-dresden", "shot",
     "Gala vakaras Dresdene",
     "Humanoidinis robotas Unitree G1 gala vakare Dresdene tarp svečių"),
    ("realizacja-gala-palac", "shot",
     "Rūmų pokylių salė",
     "Humanoidinis robotas smokingu rūmų pokylių salėje"),
    ("realizacja-gala-wsrod-gosci", "shot shot--wide",
     "Tarp svečių",
     "Humanoidinis robotas tarp gerai nusiteikusių gala vakaro svečių su taurėmis"),
    ("realizacja-event-nad-woda", "shot",
     "Renginys prie vandens",
     "Humanoidinis robotas mojuoja terasoje virš jachtų prieplaukos"),
    ("realizacja-nocny-pokaz", "shot shot--narrow",
     "Naktiniai pasirodymai",
     "Humanoidinis robotas raudonu apsiaustu naktiniame pasirodyme prie istorinio pastato"),
    ("realizacja-lexai-ulica", "shot",
     "Užduotyje dėl LEX AI",
     "Humanoidinis robotas su LEX AI ženklinimu ir portfeliu senamiesčio gatvelėje"),
    ("realizacja-spotkanie-biznesowe", "shot",
     "Verslo susitikimas",
     "Humanoidinis robotas su įmonės marškinėliais terasoje verslo susitikime"),
    ("robot-pies-branding-klienta", "shot",
     "Robotas šuo su kliento ženklinimu",
     "Robotas šuo su kliento įmonės marškinėliais akcijoje automobilių salone"),
    ("realizacja-robot-w-deszczu", "shot shot--narrow",
     "Ir per lietų",
     "Humanoidinis robotas raudonais marškinėliais per lietų laiko skėtį"),
    ("realizacja-robot-gala-portret", "shot",
     "Portretas",
     "Humanoidinio roboto Unitree G1 portretas gala vakaro apranga"),
]


def figure(photo, loading="lazy", strip=False):
    name, cls, cap, alt = photo
    if strip:
        # juostoje visos plytelės vienodo aukščio — plačiąsias paliekame, siaurąsias sulyginame
        cls = cls.replace(" shot--narrow", "")
    return f"""      <figure class="{cls}">
        <picture>
          <source srcset="{DIR}/{name}.webp" type="image/webp" />
          <img src="{DIR}/{name}.jpg" alt="{esc(alt)}" loading="{loading}" decoding="async" class="shot__img" />
        </picture>
        <figcaption class="shot__cap">{cap}</figcaption>
      </figure>"""


def shots(photos=None, strip=False, eager_first=False):
    photos = photos or PHOTOS
    out = []
    for i, p in enumerate(photos):
        loading = "eager" if (eager_first and i == 0) else "lazy"
        out.append(figure(p, loading, strip))
    return "\n".join(out)


def rotate_for(slug, count=6):
    """Kiekvienam puslapiui parenka kitą nuotraukų rinkinį, kad svetainė neatrodytų monotoniškai.

    Poslinkis skaičiuojamas iš puslapio adreso, todėl jis stabilus tarp generavimų.
    """
    n = len(PHOTOS)
    offset = sum(ord(c) for c in slug) % n
    # Vien poslinkio neužtenka: 28 miestų puslapiams iš 16 nuotraukų gaunasi tik 16
    # galimų gretimų langų, tad rinkiniai kartojasi. Todėl imame ne iš eilės, o žingsniu,
    # kuris yra nelyginis (taigi tarpusavyje pirminis su 16) ir taip pat priklauso nuo
    # adreso — variantų gaunasi 16 × 8, o nuotraukos viename puslapyje nesikartoja.
    step = 1 + 2 * (sum(ord(c) * (i + 1) for i, c in enumerate(slug)) % (n // 2))
    return [PHOTOS[(offset + i * step) % n] for i in range(count)]


def gallery_section(title="Kadrai iš tikrų<br />renginių", tag="Realizacijos", photos=None,
                    lead=None, cta=True):
    photos = photos or PHOTOS
    lead_html = f'    <p class="shots__lead">{lead}</p>\n' if lead else ""
    cta_html = ('\n      <div class="shots__more"><a href="galerija.html" class="btn-ghost">'
                'Visa galerija →</a></div>') if cta else ""
    return f"""  <!-- REALIZACIJOS -->
  <section class="section" id="galerija">
    <div class="section-header">
      <span class="tag">{tag}</span>
      <h2 class="section-title">{title}</h2>
    </div>
    <div class="shots-wrap">
{lead_html}      <div class="shots">
{shots(photos)}
      </div>{cta_html}
    </div>
  </section>

"""


def strip_section(slug, title="Iš mūsų renginių", count=6):
    """Kompaktiška nuotraukų juosta paslaugų ir miestų puslapiams."""
    photos = rotate_for(slug, count)
    return f"""  <!-- NUOTRAUKŲ JUOSTA -->
  <section class="section" style="padding-top:0;">
    <div class="shots-wrap">
      <p style="font-size:0.75rem; color:var(--text-3); text-transform:uppercase; letter-spacing:0.1em; font-weight:700; margin-bottom:var(--s3);">{title}</p>
      <div class="shots shots--strip">
{shots(photos, strip=True)}
      </div>
      <div class="shots__more"><a href="galerija.html" class="btn-ghost">Visos nuotraukos →</a></div>
    </div>
  </section>

"""


def image_ld():
    items = ",\n".join(f"""      {{
        "@type": "ImageObject",
        "contentUrl": "{SITE}/{DIR}/{name}.jpg",
        "name": "{esc(cap)}",
        "description": "{esc(alt)}"
      }}""" for name, cls, cap, alt in PHOTOS)
    return f"""{{
  "@context": "https://schema.org",
  "@type": "ImageGallery",
  "name": "33bots — nuotraukos iš humanoidinio roboto realizacijų",
  "url": "{SITE}/galerija.html",
  "inLanguage": "lt-LT",
  "publisher": {{"@id": "{SITE}/#organizacija"}},
  "associatedMedia": [
{items}
  ]
}}"""
