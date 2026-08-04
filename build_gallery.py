# -*- coding: utf-8 -*-
"""galerija.html — nuotraukų galerija iš tikrų pasirodymų."""
from lt_common import (SITE, head, body_open, nav, crumbs, breadcrumb_ld, contact_section,
                       footer, organization_ld, write)
from lt_gallery import gallery_grid, image_ld, PHOTOS

SLUG = "galerija.html"


def build():
    url = f"{SITE}/{SLUG}"
    ld = [organization_ld(), image_ld(),
          breadcrumb_ld([("Pradžia", f"{SITE}/"), ("Galerija", url)])]

    html = head(
        title="Roboto nuotraukos iš renginių — 33bots galerija",
        description="Nuotraukos iš tikrų humanoidinio roboto Unitree G1 pasirodymų: svečių "
                    "pasitikimas, šokis, gestai ir ženklinimas prekės ženklu.",
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
      <h1 class="hero__title">Taip robotas atrodo<br />ne renderyje, o gyvai.</h1>
      <p class="hero__sub">Nuotraukos iš tikrų 33bots pasirodymų — su kliento ženklinimu ant krūtinės, lauke ir iš arti. Tas pats robotas ir ta pati komanda dirba ir Lietuvoje.</p>
      <div class="hero__ctas">
        <a href="#kontaktai" class="btn-primary">Gauti pasiūlymą</a>
        <a href="video-realizacijos.html" class="btn-ghost">Vaizdo įrašai →</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div style="max-width:1100px; margin:0 auto; display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:var(--s4);">
{gallery_grid(loading_first_eager=True)}
    </div>
    <p style="max-width:760px; margin:var(--s8) auto 0; text-align:center; color:var(--text-2); line-height:1.8;">
      Ant roboto krūtinės matomas logotipas ir QR kodas — tai <strong style="color:var(--text);">nemokamas ženklinimas</strong>, įskaičiuotas į kiekvieną nuomos paketą. Jūsų renginyje toje vietoje bus jūsų prekės ženklas.
    </p>
  </section>

"""
    html += contact_section()
    html += footer()
    write(SLUG, html)


if __name__ == "__main__":
    build()
