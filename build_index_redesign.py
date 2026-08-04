# -*- coding: utf-8 -*-
"""Pagrindinis puslapis — perkeltas 33bots.pl perdarytas dizainas.

Šaltinis: templates/pl-index.html (lenkiškos versijos kopija). Šis skriptas išverčia tekstus,
pakeičia nuorodas į lietuviškus adresus ir perrašo meta bei struktūrizuotus duomenis.
Taip išdėstymas lieka identiškas lenkiškam, o turinys — lietuviškas.
"""
import html
import re

from lt_common import SITE, EMAIL, PHONE_1, PHONE_1_H, alternates, esc, CITIES, city_url
from lt_index_strings import (TEXTS, ATTRS, JS_TEXTS, PRICE_FROM, PRICE_FROM_PLAIN,
                              PRICE_DOG, DISCOUNT)

SRC = "templates/pl-index.html"
OUT = "index.html"

# Lenkiškas adresas -> lietuviškas atitikmuo
LINKS = {
    "wypozyczenie-robota.html": "humanoidinio-roboto-nuoma.html",
    "oferta-targi.html": "robotas-parodoms.html",
    "oferta-konferencje.html": "robotas-konferencijai.html",
    "oferta-dni-otwarte.html": "robotas-atidarymui.html",
    "atrakcje-na-event.html": "atrakcijos-renginiams.html",
    "realizacje-wideo.html": "video-realizacijos.html",
    "oferta.html": "robotu-nuoma.html",
    "blog.html": "blog.html",
    "case-study-lexai.html": "galerija.html",
    "case-study-wallstreet.html": "galerija.html",
    "case-study-women-in-tech.html": "galerija.html",
}

TITLE = "Humanoidinių robotų nuoma renginiams Lietuvoje | 33bots"
DESC = ("Humanoidinio roboto Unitree G1 nuoma renginiams visoje Lietuvoje. Transportas, "
        "operatorius ir ženklinimas kainoje. Kaina per 24 val.")


def translate_texts(doc):
    """Pakeičia tekstinius mazgus pagal vertimo žemėlapį.

    Skriptų ir stilių turinys praleidžiamas — ten tekstai keičiami atskirai.
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
        if key in TEXTS:
            lead = raw[:len(raw) - len(raw.lstrip())]
            tail = raw[len(raw.rstrip()):]
            return ">" + lead + TEXTS[key] + tail + "<"
        missing.append(key)
        return m.group(0)

    doc = re.sub(r">([^<>]+)<", repl, doc)
    return doc, missing


def translate_attrs(doc):
    for pl, lt in ATTRS.items():
        doc = doc.replace(f'"{pl}"', f'"{lt}"')
    return doc


def swap_links(doc):
    for pl, lt in LINKS.items():
        doc = doc.replace(f'href="{pl}"', f'href="{lt}"')
    # miestų nuorodos: robot-wynajem-<miestas>.html -> robotu-nuoma-<miestas>.html
    doc = re.sub(r'href="robot-wynajem-[a-z-]+\.html"', 'href="robotu-nuoma.html"', doc)
    return doc


def swap_city_list(doc):
    """Lenkiškų miestų sąrašą poraštėje keičia lietuvišku (visi 28 miestai)."""
    items = "\n".join(
        f'        <a href="{city_url(slug)}" class="transition hover:text-accent">{name}</a>'
        for slug, name, _, _ in CITIES
    )
    pattern = re.compile(
        r'(<div class="mt-4 flex flex-wrap gap-x-4 gap-y-2 text-\[12px\] text-neutral-500">)'
        r'.*?(</div>)', re.S)
    return pattern.sub(lambda m: m.group(1) + "\n" + items + "\n      " + m.group(2), doc, count=1)


def rewrite_head(doc):
    hreflang = "\n  ".join(
        f'<link rel="alternate" hreflang="{lang}" href="{href}" />'
        for lang, href in alternates("index.html"))

    doc = re.sub(r"<title>.*?</title>", f"<title>{esc(TITLE)}</title>", doc, flags=re.S)
    doc = re.sub(r'<meta name="description" content="[^"]*"',
                 f'<meta name="description" content="{esc(DESC)}"', doc)
    doc = re.sub(r'<meta property="og:title" content="[^"]*"',
                 f'<meta property="og:title" content="{esc(TITLE)}"', doc)
    doc = re.sub(r'<meta property="og:description" content="[^"]*"',
                 f'<meta property="og:description" content="{esc(DESC)}"', doc)
    doc = re.sub(r'<meta name="twitter:title" content="[^"]*"',
                 f'<meta name="twitter:title" content="{esc(TITLE)}"', doc)
    doc = re.sub(r'<meta name="twitter:description" content="[^"]*"',
                 f'<meta name="twitter:description" content="{esc(DESC)}"', doc)
    doc = doc.replace('<html lang="pl">', '<html lang="lt">')
    doc = doc.replace('content="pl_PL"', 'content="lt_LT"')

    # kanoninis adresas ir kalbų versijos
    doc = re.sub(r'<link rel="canonical" href="[^"]*" />',
                 f'<link rel="canonical" href="{SITE}/" />', doc)
    doc = re.sub(r'(<link rel="alternate" hreflang="[^"]*" href="[^"]*" />\s*)+',
                 hreflang + "\n  ", doc, count=1)

    # šriftai iš Google -> lokalūs
    doc = re.sub(r'<link rel="preconnect" href="https://fonts\.g[^"]*"[^>]*/>\s*', "", doc)
    doc = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^"]*"\s*/?>',
                 '<link rel="preload" href="fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin />\n'
                 '  <link rel="preload" href="fonts/space-grotesk-latin.woff2" as="font" type="font/woff2" crossorigin />\n'
                 '  <link rel="stylesheet" href="fonts.css?v=1" />', doc)

    # visi likę absoliutūs adresai į lenkišką domeną
    doc = doc.replace("https://33bots.pl/feed.xml", f"{SITE}/feed.xml")
    doc = re.sub(r'https://33bots\.pl/og/[a-z0-9-]+\.jpg', f"{SITE}/og/index.jpg", doc)
    doc = doc.replace("https://33bots.pl", SITE)
    return doc


def rewrite_jsonld(doc):
    """Struktūrizuotus duomenis keičia lietuviškais iš lt_common."""
    from lt_common import organization_ld, website_ld, video_ld, service_ld, faq_ld
    from build_index import FAQ

    blocks = [organization_ld(), website_ld(), video_ld(),
              service_ld("Humanoidinio roboto Unitree G1 nuoma renginiams",
                         "Humanoidinio roboto nuoma renginiams, parodoms ir konferencijoms "
                         "visoje Lietuvoje.", f"{SITE}/", price=PRICE_FROM_PLAIN),
              faq_ld(FAQ)]
    new = "\n".join(f'  <script type="application/ld+json">\n{b}\n  </script>' for b in blocks)

    doc = re.sub(r'(\s*<script type="application/ld\+json">.*?</script>)+',
                 "\n" + new, doc, count=1, flags=re.S)
    doc = re.sub(r'\s*<script type="application/ld\+json">.*?</script>', "", doc, flags=re.S)
    # grąžinam mūsų bloką (ankstesnis šalinimas nuvalė ir jį)
    if "application/ld+json" not in doc:
        doc = doc.replace("</head>", new + "\n</head>")
    return doc


def swap_prices(doc):
    """Lenkiškas kainas keičia lietuviškomis visur — tekste, meta, JSON-LD ir skripte.

    Daroma po vertimo, kad būtų pagauti ir atskiri skaičių mazgai (pvz. didelis
    skaičius kainų kortelėje), kurių vertimo žemėlapyje nėra.
    """
    doc = doc.replace("5 500", PRICE_FROM).replace("5500", PRICE_FROM_PLAIN)
    doc = doc.replace("1 900", PRICE_DOG).replace("1900", PRICE_DOG)
    doc = re.sub(r"\bzł\b", "€", doc)
    doc = doc.replace("PLN", "EUR")
    return doc


def swap_photos(doc):
    """Nuotraukų keliai — iš šaknies į nuotraukos/ katalogą (įskaitant lightbox data-full)."""
    doc = re.sub(r'(src|srcset|data-full)="(realizacja-[a-z-]+|robot-pies-branding-klienta)\.(jpg|webp)"',
                 r'\1="nuotraukos/\2.\3"', doc)
    # Juostos nuotraukos slenka horizontaliai ir niekada nepatenka į matomą sritį,
    # todėl lazy įkėlimas joms nesuveikia — paliekame įprastą įkėlimą.
    doc = re.sub(r'(<img[^>]*class="strip-img"[^>]*)\sloading="lazy"', r'\1', doc)
    doc = re.sub(r'(<img[^>]*)\sloading="lazy"([^>]*class="strip-img")', r'\1\2', doc)
    return doc


def build():
    doc = open(SRC, encoding="utf-8").read()

    doc = swap_links(doc)
    doc = swap_photos(doc)
    doc, missing = translate_texts(doc)
    doc = translate_attrs(doc)
    doc = swap_city_list(doc)
    doc = rewrite_head(doc)
    doc = rewrite_jsonld(doc)

    doc = swap_prices(doc)

    # skriptų tekstai (formos pranešimai)
    for pl, lt in JS_TEXTS.items():
        doc = doc.replace(pl, lt)

    # kontaktai
    doc = doc.replace("+48 531 408 004", PHONE_1_H).replace("+48531408004", PHONE_1)
    doc = doc.replace("kontakt@33bots.pl", EMAIL)

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"  ✓ {OUT} (perkeltas lenkiškas dizainas)")
    if missing:
        uniq = sorted(set(missing))
        print(f"  ! neišversta: {len(uniq)}")
        for t in uniq[:40]:
            print("     ", t[:110])
    return missing


if __name__ == "__main__":
    build()
