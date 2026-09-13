# -*- coding: utf-8 -*-
"""Pagrindinis puslapis — perkeltas 33bots.pl perdarytas dizainas.

Šaltinis: templates/pl-index.html (lenkiškos versijos kopija). Šis skriptas išverčia tekstus,
pakeičia nuorodas į lietuviškus adresus ir perrašo meta bei struktūrizuotus duomenis.
Taip išdėstymas lieka identiškas lenkiškam, o turinys — lietuviškas.
"""
import html
import re

from lt_common import SITE, esc, CITIES, city_url
from lt_port import (translate_texts, translate_attrs, translate_js, swap_links, rewrite_head,
                     replace_jsonld, strip_comments, apply_contacts, check_gtm)
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


def add_nav_links(doc):
    """Į viršutinę juostą įrašo parduotuvę ir diegimus.

    Lenkiškame šablone jų nėra — jis senesnis už tuos puslapius. Be šių dviejų nuorodų
    pagrindinis puslapis vienintelis svetainėje jų nerodytų.
    """
    nuorodos = ('<a href="parduotuve.html" class="transition hover:text-white">Parduotuvė</a>\n'
                '          <a href="roboto-diegimas.html" class="transition hover:text-white">Diegimai</a>\n'
                '          ')
    zyme = '<a href="robotu-nuoma.html" class="transition hover:text-white">Paslaugos</a>'
    if zyme in doc and "parduotuve.html" not in doc.split("</header>")[0]:
        doc = doc.replace(zyme, nuorodos + zyme, 1)
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


def add_internal_links(doc):
    """Poraštėje prideda paslaugų, straipsnių ir puslapių nuorodas.

    Perdarytame lenkiškame puslapyje jų nėra — jis nukreipia tik į kelis pagrindinius
    skyrius. Be šio bloko pagrindinis puslapis neperduotų svorio 35 vidiniams puslapiams.
    Stilius toks pat kaip miestų sąrašo (<details> juosta poraštėje).
    """
    from build_offers import PAGES as P1
    from lt_offers2 import PAGES2
    from lt_offers3 import PAGES3
    from lt_articles import ARTICLES as A1
    from lt_articles2 import ARTICLES2

    def block(label, items):
        links = "\n".join(
            f'        <a href="{u}" class="transition hover:text-accent">{t}</a>'
            for u, t in items)
        return f"""
    <details class="mt-6 border-t border-line pt-6">
      <summary class="cursor-pointer list-none text-[11px] font-600 uppercase tracking-widest text-neutral-600 transition hover:text-neutral-400">{label} ▾</summary>
      <div class="mt-4 flex flex-wrap gap-x-4 gap-y-2 text-[12px] text-neutral-500">
{links}
      </div>
    </details>"""

    services = [(p["slug"], p["crumb"]) for p in P1 + PAGES2 + PAGES3]
    # Nuorodos tekstas — straipsnio pavadinimas iki brūkšnio, kad būtų aprašomasis,
    # o ne kartotųsi kategorijos pavadinimas.
    articles = [(a["slug"], a["title"].split("—")[0].split("|")[0].strip())
                for a in A1 + ARTICLES2]
    pages = [("robotu-nuoma.html", "Robotų nuoma Lietuvoje"),
             ("parduotuve.html", "Parduotuvė — roboto pirkimas"),
             ("roboto-diegimas.html", "Diegimai įmonėms"),
             ("kainos.html", "Kainos ir paketai"),
             ("galerija.html", "Nuotraukų galerija"),
             ("video-realizacijos.html", "Vaizdo įrašai"),
             ("blog.html", "Blogas"),
             ("apie-mus.html", "Apie mus"),
             ("kontaktai.html", "Kontaktai"),
             ("privatumo-politika.html", "Privatumo politika")]

    extra = (block("Visos nuomos paslaugos", services)
             + block("Straipsniai apie renginių robotus", articles)
             + block("Svetainės puslapiai", pages))

    # įterpiame iškart po miestų sąrašo bloko
    m = re.search(r'</details>', doc)
    if not m:
        return doc
    return doc[:m.end()] + extra + doc[m.end():]


def rewrite_jsonld(doc):
    """Struktūrizuotus duomenis keičia lietuviškais iš lt_common."""
    from lt_common import (organization_ld, website_ld, video_ld, service_ld, faq_ld,
                           product_reviews_ld)
    from build_index import FAQ

    blocks = [organization_ld(), website_ld(), video_ld(),
              service_ld("Humanoidinio roboto Unitree G1 nuoma renginiams",
                         "Humanoidinio roboto nuoma renginiams, parodoms ir konferencijoms "
                         "visoje Lietuvoje.", f"{SITE}/", price=PRICE_FROM_PLAIN),
              product_reviews_ld(PRICE_FROM_PLAIN),
              faq_ld(FAQ)]
    return replace_jsonld(doc, blocks)


def mark_reviews(doc):
    """Virš atsiliepimų prideda eilutę, iš kur jie.

    Atsiliepimai yra iš 33bots realizacijų Lenkijoje (lenkiški klientų vardai),
    todėl puslapyje tai pasakoma atvirai — o struktūrizuoti duomenys
    (`product_reviews_ld`) remiasi tais pačiais tekstais.
    """
    from lt_common import REVIEWS, REVIEWS_NOTE

    zyme = ('<p class="reveal mt-20 text-center text-[12px] uppercase tracking-widest '
            f'text-neutral-500">{REVIEWS_NOTE}</p>\n    ')
    tinklelis = '<div class="mt-20 grid gap-4 md:grid-cols-3">'
    if tinklelis in doc and REVIEWS_NOTE not in doc:
        # tinklelis jau turi viršutinį tarpą — žymei jį perduodame, o tinkleliui mažiname
        doc = doc.replace(tinklelis, zyme + '<div class="mt-8 grid gap-4 md:grid-cols-3">', 1)
    return doc


def check_reviews(doc):
    """Įspėja, jei struktūrizuotų atsiliepimų nebėra matomame tekste.

    Google reikalauja, kad `Review` atitiktų tai, ką mato lankytojas. Jei kas nors
    pakeis citatą lt_index_strings.TEXTS ir pamirš lt_common.REVIEWS, tai išlįs čia,
    o ne Search Console po mėnesio.
    """
    from lt_common import REVIEWS
    tekstas = re.sub(r"\s+", " ", doc)
    return [body for _, _, body in REVIEWS if body not in tekstas]


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
    # srcset gali turėti kelis variantus (400w, 760w), todėl prefiksą dedame kiekvienam
    # failo vardui atskirai, o ne visam atributui.
    doc = re.sub(r'\b((?:realizacja|robot-pies)[a-z0-9-]*\.(?:jpg|webp))\b',
                 r'nuotraukos/\1', doc)
    doc = doc.replace("nuotraukos/nuotraukos/", "nuotraukos/")
    # Juostos nuotraukos slenka horizontaliai ir niekada nepatenka į matomą sritį,
    # todėl lazy įkėlimas joms nesuveikia — paliekame įprastą įkėlimą.
    doc = re.sub(r'(<img[^>]*class="strip-img"[^>]*)\sloading="lazy"', r'\1', doc)
    doc = re.sub(r'(<img[^>]*)\sloading="lazy"([^>]*class="strip-img")', r'\1\2', doc)
    return doc


def build():
    doc = open(SRC, encoding="utf-8").read()

    doc = swap_links(doc, LINKS)
    doc = swap_photos(doc)
    doc, missing = translate_texts(doc, TEXTS)
    doc = translate_attrs(doc, ATTRS)
    doc = swap_city_list(doc)
    doc = add_nav_links(doc)
    doc = add_internal_links(doc)
    doc = mark_reviews(doc)
    doc = rewrite_head(doc, slug="index.html", title=TITLE, desc=DESC,
                       og_image=f"{SITE}/og/index.jpg")
    doc = rewrite_jsonld(doc)

    doc = swap_prices(doc)
    doc = strip_comments(doc)
    doc = translate_js(doc, JS_TEXTS)
    doc = apply_contacts(doc)

    be_atitikmens = check_reviews(doc)

    # Į „neišversta“ sąrašą patenka ir tekstai, kurie vėlesniuose žingsniuose
    # apskritai iškrenta iš puslapio (lenkiškų miestų sąrašas, senos meta antraštės).
    # Rodome tik tai, kas realiai liko galutiniame HTML — kitaip įspėjimas skęsta
    # tarp keturiasdešimties netikrų pranešimų ir nustoja ką nors reikšti.
    missing = [t for t in missing if t in doc]

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"  ✓ {OUT} (perkeltas lenkiškas dizainas)")
    if not check_gtm(doc):
        print("  ! dingo Google Tag Manager")
    for citata in be_atitikmens:
        print(f"  ! atsiliepimas struktūrizuotuose duomenyse be atitikmens puslapyje: {citata[:70]}…")
    if missing:
        uniq = sorted(set(missing))
        print(f"  ! neišversta: {len(uniq)}")
        for t in uniq[:40]:
            print("     ", t[:110])
    return missing


if __name__ == "__main__":
    build()
