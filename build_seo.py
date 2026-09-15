# -*- coding: utf-8 -*-
"""33bots.lt: sitemap.xml, robots.txt, llms.txt, feed.xml, _redirects, .htaccess."""
from datetime import date, datetime

from lt_common import (SITE, EMAIL, PHONE_H, HAS_PHONE, write, esc, CITIES, city_url, NAV_OFFER,
                       alternates)
from lt_articles import ARTICLES as _A1
from lt_articles2 import ARTICLES2 as _A2
from build_misc import VIDEOS
from build_offers import PAGES as _P1
from lt_offers2 import PAGES2 as _P2
from lt_offers3 import PAGES3 as _P3

ARTICLES = _A1 + _A2
OFFER_PAGES = _P1 + _P2 + _P3

TODAY = date.today().isoformat()


def rfc822(iso_date):
    """ISO datą (YYYY-MM-DD) paverčia į RSS reikalaujamą RFC-822 formatą."""
    dt = datetime.fromisoformat(f"{iso_date}T09:00:00+02:00")
    return dt.strftime("%a, %d %b %Y %H:%M:%S %z")


# Paslaugų puslapiai imami tiesiai iš generatorių — sitemapa negali atsilikti nuo turinio.
CORE = (
    [("", "1.0", "weekly", TODAY),
     ("robotu-nuoma.html", "0.9", "weekly", TODAY)]
    + [(p["slug"], "0.9", "monthly", TODAY) for p in OFFER_PAGES]
    + [("parduotuve.html", "0.9", "monthly", TODAY),
       ("roboto-diegimas.html", "0.9", "monthly", TODAY),
       ("kainos.html", "0.9", "monthly", TODAY),
       ("video-realizacijos.html", "0.8", "monthly", TODAY),
       ("galerija.html", "0.8", "monthly", TODAY),
       ("apie-mus.html", "0.7", "yearly", TODAY),
       ("kontaktai.html", "0.7", "yearly", TODAY),
       ("blog.html", "0.8", "weekly", TODAY),
       ("privatumo-politika.html", "0.2", "yearly", TODAY)]
)

# hreflang poros imamos iš to paties šaltinio kaip HTML
ALT = alternates("index.html")


def build_sitemap():
    parts = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
             '        xmlns:xhtml="http://www.w3.org/1999/xhtml"',
             '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"',
             '        xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">']

    def url(loc, prio, freq, lastmod, extra=""):
        return (f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{lastmod}</lastmod>\n"
                f"    <changefreq>{freq}</changefreq>\n    <priority>{prio}</priority>\n{extra}  </url>")

    alt_block = "".join(
        f'    <xhtml:link rel="alternate" hreflang="{lang}" href="{href}" />\n' for lang, href in ALT)
    home_video = (
        "    <video:video>\n"
        "      <video:thumbnail_loc>" + SITE + "/video/33bots-robot-event-poster.jpg</video:thumbnail_loc>\n"
        "      <video:title>Humanoidinis robotas Unitree G1 renginyje — nuoma Lietuvoje</video:title>\n"
        "      <video:description>Robotas Unitree G1 gyvai: vaikšto, gestikuliuoja, pasitinka svečius ir šoka.</video:description>\n"
        "      <video:content_loc>" + SITE + "/video/33bots-robot-event.mp4</video:content_loc>\n"
        "      <video:duration>35</video:duration>\n"
        "      <video:family_friendly>yes</video:family_friendly>\n"
        "    </video:video>\n")
    home_image = ("    <image:image>\n      <image:loc>" + SITE + "/robot-g1.jpg</image:loc>\n"
                  "      <image:title>Humanoidinis robotas Unitree G1 — nuoma renginiams Lietuvoje</image:title>\n"
                  "    </image:image>\n")

    for slug, prio, freq, lastmod in CORE:
        loc = f"{SITE}/" if slug == "" else f"{SITE}/{slug}"
        extra = alt_block if slug == "" else ""
        if slug == "":
            extra += home_image + home_video
        parts.append(url(loc, prio, freq, lastmod, extra))

    # vaizdo įrašų puslapis su visais video
    vid_extra = "".join(
        "    <video:video>\n"
        f"      <video:thumbnail_loc>{SITE}/video/{f}-poster.jpg</video:thumbnail_loc>\n"
        f"      <video:title>{esc(t)}</video:title>\n"
        f"      <video:description>{esc(d)}</video:description>\n"
        f"      <video:content_loc>{SITE}/video/{f}.mp4</video:content_loc>\n"
        "      <video:family_friendly>yes</video:family_friendly>\n"
        "    </video:video>\n" for f, t, d, _ in VIDEOS)
    parts = [p for p in parts if f"<loc>{SITE}/video-realizacijos.html</loc>" not in p]
    parts.append(url(f"{SITE}/video-realizacijos.html", "0.8", "monthly", TODAY, vid_extra))

    for a in ARTICLES:
        parts.append(url(f"{SITE}/{a['slug']}", "0.7", "monthly", a["modified"]))

    for slug, *_ in CITIES:
        parts.append(url(f"{SITE}/{city_url(slug)}", "0.7", "monthly", TODAY))

    parts.append("</urlset>")
    write("sitemap.xml", "\n".join(parts) + "\n")


def build_robots():
    write("robots.txt", f"""User-agent: *
Allow: /

# AI naršyklės — sąmoningai leidžiame
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Google-Extended
Allow: /

Sitemap: {SITE}/sitemap.xml

# Svetainės santrauka kalbos modeliams: {SITE}/llms.txt
""")


def build_llms():
    kontaktu_telefonas = f", {PHONE_H}" if HAS_PHONE else ""
    offers = "\n".join(f"- [{p['crumb']}]({SITE}/{p['slug']}) — {p['desc']}"
                        for p in OFFER_PAGES)
    posts = "\n".join(f"- [{a['title']}]({SITE}/{a['slug']}) — {a['desc']}" for a in ARTICLES)
    cities = "\n".join(f"- [{n}]({SITE}/{city_url(s)})" for s, n, _, _ in CITIES)
    write("llms.txt", f"""# 33bots — humanoidinių robotų nuoma renginiams Lietuvoje

> 33bots nuomoja humanoidinius robotus Unitree G1 renginiams, parodoms, konferencijoms ir įmonių
> šventėms visoje Lietuvoje. Į pradinę kainą įeina sertifikuotas operatorius visam renginio laikui ir roboto
> ženklinimas kliento logotipu bei QR kodu; atvykimą vertiname pagal renginio vietą.

## Pagrindiniai faktai

- Paslauga: humanoidinio roboto nuoma su operatoriumi
- Robotas: Unitree G1 (132 cm, 35 kg, iki 43 laisvės laipsnių, iki 2 m/s, LiDAR ir kompiuterinė rega)
- Teritorija: visa Lietuva; atvykimas vertinamas pagal renginio vietą
- Į pradinę kainą įeina: robotas, operatorius, paruošimas, ženklinimas, scenarijaus derinimas,
  civilinės atsakomybės draudimo apsauga
- Paketai: Impulsas (iki 3 val.), Standartas (iki 8 val.), Multi-Day (2–7+ dienų)
- Be nuomos: robotų pardavimas (parduotuve.html) ir diegimas įmonėje su kalbos programine
  įranga bei komandos mokymais (roboto-diegimas.html); kaina pateikiama po pokalbio
- Atsakymo laikas į užklausą: 24 darbo valandos
- Kontaktai: {EMAIL}{kontaktu_telefonas}
- Kalbų versijos: lietuvių ({SITE}), lenkų (https://33bots.pl), vokiečių (https://33bots.de),
  austriška (https://33bots.at)

## Paslaugų puslapiai

- [Robotų nuoma Lietuvoje — visi miestai ir paslaugos]({SITE}/robotu-nuoma.html)
{offers}
- [Kainos ir paketai]({SITE}/kainos.html)
- [Parduotuvė — humanoidinio roboto ir roboto šuns pirkimas]({SITE}/parduotuve.html)
- [Diegimai įmonėms — robotas, kalbos programinė įranga, mokymai]({SITE}/roboto-diegimas.html)
- [Vaizdo įrašai iš renginių]({SITE}/video-realizacijos.html)
- [Nuotraukų galerija]({SITE}/galerija.html)
- [Apie 33bots]({SITE}/apie-mus.html)
- [Kontaktai]({SITE}/kontaktai.html)

## Straipsniai

{posts}

## Miestai

{cities}

## Dažni klausimai

- Ar robotą gali valdyti užsakovas? Ne — robotą valdo 33bots operatorius, kuris lieka visą renginį.
- Ar atvykimas kainuoja papildomai? Atvykimą vertiname pagal renginio vietą ir nurodome pasiūlyme.
- Ar ženklinimas kainuoja papildomai? Ne, logotipas ir QR kodas įeina į standartinį paketą.
- Kokių sąlygų reikia vietoje? 230 V lizdo, ~2×2 m laisvos erdvės, prieigos likus 45 min. iki starto.
- Ar robotas saugus? Taip — LiDAR jutikliai, kompiuterinė rega ir nuolatinė operatoriaus priežiūra.
""")


def build_feed():
    items = "\n".join(f"""    <item>
      <title>{esc(a['title'])}</title>
      <link>{SITE}/{a['slug']}</link>
      <guid isPermaLink="true">{SITE}/{a['slug']}</guid>
      <description>{esc(a['desc'])}</description>
      <category>{esc(a['tag'])}</category>
      <pubDate>{rfc822(a['published'])}</pubDate>
    </item>""" for a in ARTICLES)

    write("feed.xml", f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>33bots — blogas apie renginių robotus</title>
    <link>{SITE}/blog.html</link>
    <atom:link href="{SITE}/feed.xml" rel="self" type="application/rss+xml" />
    <description>Straipsniai apie humanoidinių robotų nuomą renginiams Lietuvoje: kainos, scenarijai, sauga ir technologijos.</description>
    <language>lt-lt</language>
    <lastBuildDate>{rfc822(TODAY)}</lastBuildDate>
{items}
  </channel>
</rss>
""")


def build_server_config():
    write("_redirects", """https://www.33bots.lt/* https://33bots.lt/:splat 301!
http://www.33bots.lt/* https://33bots.lt/:splat 301!
http://33bots.lt/* https://33bots.lt/:splat 301!

/index https://33bots.lt/ 301
/kontaktas.html /kontaktai.html 301
/blogas.html /blog.html 301
""")

    write(".htaccess", """RewriteEngine On

# HTTPS ir non-www (kanoninis adresas: https://33bots.lt)
RewriteCond %{HTTP_HOST} ^www\\.33bots\\.lt$ [NC,OR]
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://33bots.lt/$1 [L,R=301]

ErrorDocument 404 /404.html

# Talpyklos politika statiniam turiniui
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType text/css "access plus 1 year"
  ExpiresByType application/javascript "access plus 1 year"
  ExpiresByType image/jpeg "access plus 1 year"
  ExpiresByType image/webp "access plus 1 year"
  ExpiresByType image/png "access plus 1 year"
  ExpiresByType image/svg+xml "access plus 1 year"
  ExpiresByType video/mp4 "access plus 1 year"
  ExpiresByType text/html "access plus 1 hour"
</IfModule>

<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css application/javascript application/json image/svg+xml text/xml
</IfModule>

<IfModule mod_headers.c>
  Header set X-Content-Type-Options "nosniff"
  Header set Referrer-Policy "strict-origin-when-cross-origin"
</IfModule>
""")


# IndexNow raktas. Jis yra viešas pagal sumanymą: tas pats raktas guli svetainėje kaip
# <RAKTAS>.txt ir būtent taip paieškos sistema patikrina, kad adresus siunčia savininkas.
# Todėl jį laikome repozitorijoje, o ne paslaptyse.
INDEXNOW_KEY = "da66134087cc25b2d1bc36011f30f615"


def build_indexnow_key():
    write(f"{INDEXNOW_KEY}.txt", INDEXNOW_KEY)


def build():
    build_indexnow_key()
    build_sitemap()
    build_robots()
    build_llms()
    build_feed()
    build_server_config()


if __name__ == "__main__":
    build()
