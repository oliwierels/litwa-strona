# -*- coding: utf-8 -*-
"""Galerijos nuotraukos (tikri kadrai iš renginių) ir jų atvaizdavimas."""
from lt_common import SITE, esc

# (failo vardas be plėtinio, plotis, aukštis, antraštė, alt tekstas)
PHOTOS = [
    ("robotas-renginyje", 720, 1076,
     "Robotas su kliento ženklinimu",
     "Humanoidinis robotas Unitree G1 renginyje su 33bots logotipu ir QR kodu ant krūtinės"),
    ("svetainiu-pasitikimas", 540, 960,
     "Svečių pasitikimas",
     "Humanoidinis robotas Unitree G1 mojuoja ranka pasitikdamas renginio svečius"),
    ("sokio-pasirodymas", 540, 960,
     "Šokio choreografija",
     "Robotas Unitree G1 atlieka šokio choreografiją lauko renginyje"),
    ("gestai-is-arti", 540, 960,
     "Gestai iš arti",
     "Humanoidinio roboto Unitree G1 rankos ir gestai iš arti — 43 laisvės laipsniai"),
    ("judejimas-lauke", 540, 960,
     "Judėjimas lauke",
     "Robotas Unitree G1 vaikšto žole lauko renginio erdvėje"),
    ("zenklinimas-qr", 540, 960,
     "Ženklinimas ir QR kodas",
     "Roboto krūtinė su prekės ženklo logotipu ir QR kodu — ženklinimas įskaičiuotas į nuomos kainą"),
    ("unitree-g1-studija", 720, 540,
     "Unitree G1 iš arti",
     "Humanoidinis robotas Unitree G1 studijoje — 132 cm, 35 kg, 43 laisvės laipsniai"),
    ("g1-choreografija", 600, 600,
     "Dinamiška poza",
     "Robotas Unitree G1 dinamiškoje pozoje — kadras iš pasirodymo"),
]


def figure(name, w, h, caption, alt, loading="lazy"):
    return f"""      <figure style="margin:0; background:var(--surface-2); border:1px solid var(--border-mid); border-radius:14px; overflow:hidden;">
        <picture>
          <source srcset="galerija/{name}.webp" type="image/webp" />
          <img src="galerija/{name}.jpg" alt="{esc(alt)}" width="{w}" height="{h}"
               loading="{loading}" decoding="async"
               style="width:100%; height:auto; display:block;" />
        </picture>
        <figcaption style="padding:var(--s3) var(--s4); font-size:0.85rem; color:var(--text-2);">{caption}</figcaption>
      </figure>"""


def gallery_grid(photos=None, loading_first_eager=False):
    photos = photos or PHOTOS
    items = []
    for i, (name, w, h, cap, alt) in enumerate(photos):
        loading = "eager" if (loading_first_eager and i == 0) else "lazy"
        items.append(figure(name, w, h, cap, alt, loading))
    return "\n".join(items)


def gallery_section(title="Kadrai iš<br />tikrų pasirodymų", tag="Galerija", photos=None,
                    lead=None, cta=True):
    photos = photos or PHOTOS
    lead_html = ""
    if lead:
        lead_html = (f'    <p style="max-width:760px; margin:0 auto var(--s7); text-align:center; '
                     f'color:var(--text-2); line-height:1.8;">{lead}</p>\n')
    cta_html = ""
    if cta:
        cta_html = ('\n    <p style="text-align:center; margin-top:var(--s7);">'
                    '<a href="galerija.html" class="btn-ghost" style="display:inline-flex;">'
                    'Visa galerija →</a></p>')
    return f"""  <!-- GALERIJA -->
  <section class="section" id="galerija">
    <div class="section-header">
      <span class="tag">{tag}</span>
      <h2 class="section-title">{title}</h2>
    </div>
{lead_html}    <div style="max-width:1100px; margin:0 auto; display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:var(--s4);">
{gallery_grid(photos)}
    </div>{cta_html}
  </section>

"""


def image_ld():
    items = ",\n".join(f"""      {{
        "@type": "ImageObject",
        "contentUrl": "{SITE}/galerija/{name}.jpg",
        "name": "{esc(cap)}",
        "description": "{esc(alt)}",
        "width": {w},
        "height": {h}
      }}""" for name, w, h, cap, alt in PHOTOS)
    return f"""{{
  "@context": "https://schema.org",
  "@type": "ImageGallery",
  "name": "33bots — kadrai iš humanoidinio roboto pasirodymų",
  "url": "{SITE}/galerija.html",
  "inLanguage": "lt-LT",
  "publisher": {{"@id": "{SITE}/#organizacija"}},
  "associatedMedia": [
{items}
  ]
}}"""
