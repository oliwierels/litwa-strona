# -*- coding: utf-8 -*-
"""Lenkiško puslapio perkėlimo į lietuvišką versiją įrankiai.

Perdarytas 33bots.pl dizainas į 33bots.lt perkeliamas ne kopijuojant ranka, o verčiant
lenkišką šabloną: tekstiniai mazgai keičiami pagal žodyną, nuorodos — pagal adresų žemėlapį,
meta ir struktūrizuoti duomenys perrašomi iš naujo. Taip visos trys perkeltos svetainės dalys
(pagrindinis puslapis, parduotuvė, diegimai) atrodo taip pat kaip lenkiškos, o atnaujinus
lenkišką šabloną pakanka perpaleisti generatorių.

Čia laikoma tai, kas bendra visiems trims; kiekvieno puslapio savitumai lieka jo generatoriuje.
"""
import re

from lt_common import (SITE, EMAIL, PHONE, PHONE_H, HAS_PHONE, FORM_ENDPOINT, GTM,
                       alternates, esc)


def translate_texts(doc, texts):
    """Pakeičia tekstinius mazgus pagal vertimo žemėlapį.

    Skriptų ir stilių turinys praleidžiamas — ten tekstai keičiami atskirai (`translate_js`).
    Grąžina (dokumentas, neišverstų tekstų sąrašas).
    """
    missing = []
    skip = [(m.start(), m.end()) for m in
            re.finditer(r"<(script|style)[^>]*>.*?</\1>", doc, re.S)]

    def in_skip(pos):
        return any(a <= pos < b for a, b in skip)

    def repl(m):
        if in_skip(m.start()):
            return m.group(0)
        raw = m.group(1)
        key = " ".join(raw.split())
        if not key or not re.search(r"[a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ]", key):
            return m.group(0)
        if key in texts:
            lead = raw[:len(raw) - len(raw.lstrip())]
            tail = raw[len(raw.rstrip()):]
            return ">" + lead + texts[key] + tail + "<"
        missing.append(key)
        return m.group(0)

    return re.sub(r">([^<>]+)<", repl, doc), missing


def translate_attrs(doc, attrs):
    """Atributų reikšmės (alt, aria-label, placeholder, og:image:alt) pagal žodyną."""
    for pl, lt in attrs.items():
        doc = doc.replace(f'"{pl}"', f'"{lt}"')
    return doc


def translate_js(doc, js_texts):
    """Skriptų tekstai — formos pranešimai ir klaidos."""
    for pl, lt in js_texts.items():
        doc = doc.replace(pl, lt)
    return doc


def swap_links(doc, links):
    """Lenkiški adresai -> lietuviški atitikmenys."""
    for pl, lt in links.items():
        doc = doc.replace(f'href="{pl}"', f'href="{lt}"')
    return doc


def rewrite_head(doc, slug, title, desc, og_title=None, og_desc=None, og_image=None):
    """Perrašo <head>: antraštes, OG, kalbą, kanoninį adresą, hreflang ir šriftus.

    SVARBU: bendras domeno pakeitimas (33bots.pl -> 33bots.lt) daromas PRIEŠ įrašant
    kanoninį adresą ir hreflang. Kitaip jis sugadintų ką tik įrašytas kitų kalbų nuorodas —
    „pl" ir „x-default" imtų rodyti į 33bots.lt, o tai savaiminis konfliktas, dėl kurio
    Google gali atmesti visą hreflang klasterį.
    """
    og_title = og_title or title
    og_desc = og_desc or desc
    url = f"{SITE}/" if slug == "index.html" else f"{SITE}/{slug}"

    hreflang = "\n  ".join(
        f'<link rel="alternate" hreflang="{lang}" href="{href}" />'
        for lang, href in alternates(slug))

    doc = re.sub(r"<title>.*?</title>", f"<title>{esc(title)}</title>", doc, flags=re.S)
    doc = re.sub(r'<meta name="description" content="[^"]*"',
                 f'<meta name="description" content="{esc(desc)}"', doc)
    doc = re.sub(r'<meta property="og:title" content="[^"]*"',
                 f'<meta property="og:title" content="{esc(og_title)}"', doc)
    doc = re.sub(r'<meta property="og:description" content="[^"]*"',
                 f'<meta property="og:description" content="{esc(og_desc)}"', doc)
    doc = re.sub(r'<meta name="twitter:title" content="[^"]*"',
                 f'<meta name="twitter:title" content="{esc(og_title)}"', doc)
    doc = re.sub(r'<meta name="twitter:description" content="[^"]*"',
                 f'<meta name="twitter:description" content="{esc(og_desc)}"', doc)
    doc = doc.replace('<html lang="pl">', '<html lang="lt">')
    doc = doc.replace('content="pl_PL"', 'content="lt_LT"')

    doc = doc.replace("https://33bots.pl/feed.xml", f"{SITE}/feed.xml")
    doc = re.sub(r'https://33bots\.pl/og/[a-z0-9-]+\.jpg', og_image or f"{SITE}/og-image.jpg", doc)
    doc = doc.replace("https://33bots.pl", SITE)

    doc = re.sub(r'<link rel="canonical" href="[^"]*" />',
                 f'<link rel="canonical" href="{url}" />', doc)
    doc = re.sub(r'<meta property="og:url" content="[^"]*"',
                 f'<meta property="og:url" content="{url}"', doc)
    if og_image:
        doc = re.sub(r'<meta property="og:image" content="[^"]*"',
                     f'<meta property="og:image" content="{og_image}"', doc)
    doc = re.sub(r'(<link rel="alternate" hreflang="[^"]*" href="[^"]*" />\s*)+',
                 hreflang + "\n  ", doc, count=1)

    # šriftai iš Google -> lokalūs
    doc = re.sub(r'<link rel="preconnect" href="https://fonts\.g[^"]*"[^>]*/>\s*', "", doc)
    doc = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^"]*"\s*/?>',
                 '<link rel="preload" href="fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin />\n'
                 '  <link rel="preload" href="fonts/space-grotesk-latin.woff2" as="font" type="font/woff2" crossorigin />\n'
                 '  <link rel="stylesheet" href="fonts.css?v=1" />', doc)
    return doc


def replace_jsonld(doc, blocks):
    """Lenkiškus struktūrizuotus duomenis keičia lietuviškais."""
    new = "\n".join(f'  <script type="application/ld+json">\n{b}\n  </script>' for b in blocks)
    doc = re.sub(r'(\s*<script type="application/ld\+json">.*?</script>)+',
                 "\n" + new, doc, count=1, flags=re.S)
    doc = re.sub(r'\s*<script type="application/ld\+json">.*?</script>', "", doc, flags=re.S)
    if "application/ld+json" not in doc:
        doc = doc.replace("</head>", new + "\n</head>")
    return doc


def strip_comments(doc):
    """Pašalina lenkiškus kūrimo komentarus iš galutinio HTML.

    Tai kūrėjų pastabos lenkų kalba — lietuviškame puslapyje jos neturi prasmės,
    o kartu sutaupoma apie 4 KB. Šalinami trys tipai:

    1. HTML komentarai `<!-- … -->` (išskyrus sąlyginius `<!--[if …]>`),
    2. `/* … */` blokai `<style>` ir `<script>` viduje,
    3. eilutės, prasidedančios `//` (tik visa eilutė, kad nenukentėtų adresai
       su `https://`).
    """
    doc = re.sub(r"<!--(?!\[if).*?-->\n?", "", doc, flags=re.S)

    def valyk(m):
        turinys = m.group(2)
        turinys = re.sub(r"/\*.*?\*/\s*", "", turinys, flags=re.S)
        turinys = re.sub(r"(?m)^[ \t]*//.*\n?", "", turinys)
        return m.group(1) + turinys + m.group(3)

    return re.sub(r"(<(?:style|script)[^>]*>)(.*?)(</(?:style|script)>)",
                  valyk, doc, flags=re.S)


def apply_contacts(doc, klaidos_tekstas=None):
    """Kontaktai: el. paštas, formos adresas ir telefonas.

    Kol lietuviško numerio nėra (`lt_common.HAS_PHONE`), telefono nuorodos iš puslapio
    išimamos visai — lenkiškas numeris lietuviškoje svetainėje klaidina. Įrašius numerį
    į `lt_common.PHONE_LT` jos savaime grįžta į tas pačias vietas.
    """
    doc = doc.replace("kontakt@33bots.pl", EMAIL)
    doc = re.sub(r"https://formspree\.io/f/\w+", FORM_ENDPOINT, doc)

    # Telefono lauko užuomina — lietuviško formato, kad nieko neklaidintų
    doc = doc.replace('placeholder="+48 531 408 004"', 'placeholder="+370 600 00000"')

    if HAS_PHONE:
        doc = doc.replace("+48 531 408 004", PHONE_H).replace("+48531408004", PHONE)
    else:
        doc = re.sub(r'<a href="tel:[^"]*"[^>]*>.*?</a>\s*', "", doc, flags=re.S)
        klaidos = klaidos_tekstas or (
            f'Nepavyko išsiųsti — parašykite mums: '
            f'<a class="text-accent underline" href="mailto:{EMAIL}">{EMAIL}</a>')
        doc = re.sub(r"msg\.innerHTML = '[^']*'", f"msg.innerHTML = '{klaidos}'", doc)
    return doc


def check_gtm(doc):
    """Patikrina, ar perkeliant nedingo analitika — be jos puslapis nematomas ataskaitose."""
    return GTM in doc
