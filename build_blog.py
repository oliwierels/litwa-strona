# -*- coding: utf-8 -*-
"""33bots.lt blogo indeksas ir straipsniai."""
import re
from lt_common import (SITE, head, body_open, nav, crumbs, breadcrumb_ld, contact_section,
                       footer, faq_section, faq_ld, organization_ld, write, esc)
from lt_articles import ARTICLES as _A1
from lt_articles2 import ARTICLES2 as _A2

ARTICLES = _A1 + _A2


def slugify_anchor(text):
    t = re.sub(r"<[^>]+>", "", text).lower()
    table = str.maketrans("ąčęėįšųūž", "aceeisuuz")
    t = t.translate(table)
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t or "sekcija"


def article_ld(a):
    return f"""{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{esc(a['title'])}",
  "description": "{esc(a['desc'])}",
  "image": "{SITE}/og/{a['slug'].replace('.html', '.jpg')}",
  "datePublished": "{a['published']}",
  "dateModified": "{a['modified']}",
  "inLanguage": "lt-LT",
  "articleSection": "{esc(a['tag'])}",
  "mainEntityOfPage": {{"@type": "WebPage", "@id": "{SITE}/{a['slug']}"}},
  "author": {{"@type": "Organization", "name": "33bots", "url": "{SITE}/"}},
  "publisher": {{"@id": "{SITE}/#organizacija"}}
}}"""


def build_article(a):
    url = f"{SITE}/{a['slug']}"
    ld = [
        organization_ld(),
        article_ld(a),
        breadcrumb_ld([("Pradžia", f"{SITE}/"), ("Blogas", f"{SITE}/blog.html"), (a["crumb"] if "crumb" in a else a["tag"], url)]),
    ]
    if a.get("faq"):
        ld.append(faq_ld(a["faq"]))

    html = head(title=a["title"], description=a["desc"], slug=a["slug"], keywords=a["keywords"],
                og_image=f"{SITE}/og/{a['slug'].replace('.html', '.jpg')}", og_type="article",
                extra_ld=ld,
                article_meta=dict(published=a["published"], modified=a["modified"], section=a["tag"]),
                extra_head="")
    html += body_open()
    html += nav(active="blog.html")
    html += crumbs([("Pradžia", "index.html"), ("Blogas", "blog.html"), (a["tag"], None)])

    toc = "\n".join(
        f'      <li><a href="#{slugify_anchor(h)}">{h}</a></li>' for h, _ in a["sections"]
    )

    body = "\n".join(
        f'      <h2 id="{slugify_anchor(h)}">{h}</h2>\n      {c}'
        for h, c in a["sections"]
    )

    related = "\n".join(f'        <a href="{u}">{t} →</a>' for u, t in a["related"])

    html += f"""
  <section class="hero hero--sub">
    <div class="hero__content">
      <p class="hero__eyebrow">Blogas · {a['tag']}</p>
      <h1 class="hero__title">{a['h1']}</h1>
      <p class="hero__sub">{a['lead']}</p>
      <p style="font-size:0.8rem; color:var(--text-3); margin-top:var(--s3);">
        Publikuota: <time datetime="{a['published']}">{a['published']}</time> ·
        Atnaujinta: <time datetime="{a['modified']}">{a['modified']}</time>
      </p>
    </div>
  </section>

  <section class="section">
    <article class="article-body">
      <nav class="toc" aria-label="Straipsnio turinys">
        <p class="toc__label">Straipsnio turinys</p>
        <ol>
{toc}
        </ol>
      </nav>

{body}

      <p><a href="#kontaktai" class="btn-primary article-cta">Gauti pasiūlymą savo renginiui →</a></p>

      <p style="font-size:0.75rem; color:var(--text-3); text-transform:uppercase; letter-spacing:0.1em; font-weight:700; margin:var(--s8) 0 var(--s3);">Susiję puslapiai</p>
      <div class="related-links">
{related}
      </div>
    </article>
  </section>

"""
    if a.get("faq"):
        html += faq_section(a["faq"], title="Klausimai apie<br />šią temą")

    html += contact_section(heading="Rezervuokite robotą<br />savo renginiui.")
    html += footer()
    write(a["slug"], html)


def build_index():
    cards = "\n".join(f"""      <div class="tile">
        <div class="tile__top"><span class="tile__tag">{a['tag']}</span></div>
        <h2 class="tile__title" style="font-size:1.15rem;">{a['title']}</h2>
        <p class="tile__desc">{a['card']}</p>
        <p style="font-size:0.72rem; color:var(--text-3); margin:0 0 var(--s2);"><time datetime="{a['published']}">{a['published']}</time></p>
        <a href="{a['slug']}" class="tile__link">Skaityti straipsnį →</a>
      </div>""" for a in ARTICLES)

    items = ",\n".join(f"""      {{
        "@type": "ListItem",
        "position": {i + 1},
        "url": "{SITE}/{a['slug']}",
        "name": "{esc(a['title'])}"
      }}""" for i, a in enumerate(ARTICLES))

    ld = [
        organization_ld(),
        f"""{{
  "@context": "https://schema.org",
  "@type": "Blog",
  "name": "33bots blogas — žinios apie renginių robotus",
  "url": "{SITE}/blog.html",
  "inLanguage": "lt-LT",
  "description": "Straipsniai apie humanoidinių robotų nuomą renginiams: kainos, scenarijai, sauga ir technologijos.",
  "publisher": {{"@id": "{SITE}/#organizacija"}}
}}""",
        f"""{{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "itemListElement": [
{items}
  ]
}}""",
        breadcrumb_ld([("Pradžia", f"{SITE}/"), ("Blogas", f"{SITE}/blog.html")]),
    ]

    html = head(title="Blogas apie renginių robotus — kainos ir patarimai | 33bots",
                description="Straipsniai apie humanoidinių robotų nuomą renginiams Lietuvoje: kainos, "
                            "scenarijai, Unitree G1 specifikacija ir sauga renginyje.",
                slug="blog.html",
                keywords="robotų blogas, renginių robotai, roboto nuoma patarimai, Unitree G1",
                og_image=f"{SITE}/og/blog.jpg", extra_ld=ld,
                extra_head="")
    html += body_open()
    html += nav(active="blog.html")
    html += crumbs([("Pradžia", "index.html"), ("Blogas", None)])
    html += f"""
  <section class="hero hero--sub">
    <div class="hero__content">
      <p class="hero__eyebrow">Blogas · Renginių robotika</p>
      <h1 class="hero__title">Žinios apie<br />renginių robotus.</h1>
      <p class="hero__sub">Kainos, scenarijai, sauga ir technologijos — viskas, ką verta žinoti prieš nuomojantis humanoidinį robotą renginiui Lietuvoje.</p>
    </div>
  </section>

  <section class="section">
    <div class="tiles tiles--blog">
{cards}
    </div>
  </section>

"""
    html += contact_section()
    html += footer()
    write("blog.html", html)


def build():
    build_index()
    for a in ARTICLES:
        build_article(a)


if __name__ == "__main__":
    build()
