# -*- coding: utf-8 -*-
"""galerija.html — nuotraukų galerija iš tikrų pasirodymų."""
from lt_common import (SITE, head, body_open, nav, crumbs, breadcrumb_ld, contact_section,
                       footer, organization_ld, write)
from lt_gallery import shots, image_ld, PHOTOS

SLUG = "galerija.html"


def build():
    url = f"{SITE}/{SLUG}"
    ld = [organization_ld(), image_ld(),
          breadcrumb_ld([("Pradžia", f"{SITE}/"), ("Galerija", url)])]

    html = head(
        title="Roboto nuotraukos iš renginių — 33bots galerija",
        description="Nuotraukos iš tikrų 33bots realizacijų: Women in Tech Summit, gala vakarai, "
                    "LEX AI, verslo renginiai ir naktiniai pasirodymai.",
        slug=SLUG,
        keywords="roboto nuotraukos, humanoidinis robotas nuotraukos, Unitree G1 nuotraukos, "
                 "robotas renginyje",
        og_image=f"{SITE}/og/galerija.jpg", extra_ld=ld)
    html += body_open()
    html += nav(active=SLUG)
    html += crumbs([("Pradžia", "index.html"), ("Galerija", None)])
    html += f"""
  <section class="hero hero--sub">
    <div class="hero__content">
      <p class="hero__eyebrow">Galerija · Kadrai iš pasirodymų</p>
      <h1 class="hero__title">Taip robotas atrodo<br />tikruose renginiuose.</h1>
      <p class="hero__sub">Kadrai iš realių 33bots projektų: Women in Tech Summit, gala vakarai rūmuose, LEX AI akcijos senamiestyje, verslo susitikimai ir naktiniai pasirodymai. Ta pati įranga ir ta pati komanda dirba Lietuvoje.</p>
      <div class="hero__ctas">
        <a href="#kontaktai" class="btn-primary">Gauti pasiūlymą</a>
        <a href="video-realizacijos.html" class="btn-ghost">Vaizdo įrašai →</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="shots-wrap">
      <div class="shots">
{shots(eager_first=True)}
      </div>
    </div>
    <p style="max-width:760px; margin:var(--s8) auto 0; text-align:center; color:var(--text-2); line-height:1.8;">
      Visose nuotraukose matyti <strong style="color:var(--text);">kliento ženklinimas</strong> — marškinėliai, logotipas ar QR kodas. Tai įskaičiuota į kiekvieną nuomos paketą, todėl jūsų renginyje toje vietoje bus jūsų prekės ženklas.
    </p>
  </section>

"""
    html += contact_section()
    html += footer()
    write(SLUG, html)


if __name__ == "__main__":
    build()
