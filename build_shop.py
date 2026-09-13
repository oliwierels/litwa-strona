# -*- coding: utf-8 -*-
"""Parduotuvė — perkeltas 33bots.pl puslapis „Sklep“.

Šaltinis: templates/pl-sklep.html. Lietuviškoje versijoje kainų nerodome lygiai taip pat
kaip lenkiškoje — robotai vežami pagal užsakymą, todėl kaina pateikiama po pokalbio.
"""
from lt_common import SITE, organization_ld, breadcrumb_ld, faq_ld
from lt_port import (translate_texts, translate_attrs, translate_js, swap_links, rewrite_head,
                     replace_jsonld, strip_comments, apply_contacts, check_gtm)
from lt_shop_strings import TEXTS, ATTRS, JS_TEXTS
from lt_links import LINKS, swap_photos

SRC = "templates/pl-sklep.html"
OUT = "parduotuve.html"

TITLE = "Parduotuvė — humanoidinis robotas Unitree G1 ir robotas šuo | 33bots"
DESC = ("Humanoidinio roboto pirkimas: užsakome tiesiai iš gamintojo, pristatymas apie mėnesį, "
        "muitinė ir paleidimas — mūsų rūpestis. Mokymai ir pagalba pakete.")
OG_TITLE = "Parduotuvė — humanoidinio roboto pirkimas | 33bots"
OG_DESC = ("Humanoidinis robotas nuosavybėn. Užsakome pagal poreikį, pristatymas apie mėnesį, "
           "paleidimas ir mokymai pakete.")

# Robotų duomenys struktūrizuotiems duomenims — tie patys skaičiai, kurie matomi puslapyje.
SPECS = [("Ūgis", "132 cm"), ("Svoris", "35 kg"), ("Laisvės laipsniai", "23"),
         ("Greitis", "iki 2 m/s"), ("Pristatymo laikas", "apie 30 dienų nuo užsakymo")]

FAQ = [
    ("Kodėl laukiama apie mėnesį?",
     "Robotus parvežame pagal konkretų užsakymą tiesiai iš gamintojo — sandėlyje jų nelaikome, "
     "nes tai didelės vertės įranga su daug variantų. Į tą laiką įeina gamyba, transportas ir "
     "muitinės procedūros. Terminą patvirtiname užsakant ir informuojame apie eigą."),
    ("Kodėl puslapyje nėra kainų?",
     "Kaina priklauso nuo modelio, komplektacijos, programinės įrangos apimties ir valiutų kurso. "
     "Nurodyti vieną sumą būtų klaidinga, todėl kiekvieną užsakymą vertiname atskirai — paprastai "
     "per parą po pokalbio ir be jokių įsipareigojimų iš jūsų pusės."),
    ("Ar reikia sumokėti visą sumą iš karto?",
     "Mokėjimo sąlygas suderiname užsakant ir įrašome į sutartį. Užsakymą gamintojui pateikiame "
     "apmokėjus išankstinę sąskaitą — kol to nepadarysite, niekas nevyksta ir niekas jūsų nesaisto."),
    ("Ar robotas kalbės lietuviškai?",
     "Gamyklinis robotas nėra paruoštas nei lietuvių kalbai, nei jūsų įmonei. Už tai atsakinga mūsų "
     "programinė įranga, kuri įeina į paketą su diegimu — tada robotas kalba lietuviškai ir žino "
     "jūsų pasiūlymą. Ją galima įsigyti ir vėliau."),
    ("Gal pirma išsinuomoti ir pažiūrėti?",
     "Tai protinga eilės tvarka ir dažnai ją patariame. Išsinuomokite robotą vienam renginiui, savo "
     "akimis pamatykite, kaip reaguoja žmonės, ir tik tada spręskite dėl pirkimo. Nuomos sąlygas "
     "rasite pagrindiniame puslapyje."),
]


def product_ld():
    props = ",\n".join(f'    {{"@type": "PropertyValue", "name": "{n}", "value": "{v}"}}'
                       for n, v in SPECS)
    return f"""{{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Humanoidinis robotas Unitree G1",
  "description": "Humanoidinis robotas Unitree G1 nuosavybėn. Ūgis 132 cm, 23 laisvės laipsniai, greitis iki 2 m/s. Vežamas pagal užsakymą; muitinė, pristatymas ir paleidimas — 33bots rūpestis.",
  "image": "{SITE}/robot-g1.jpg",
  "url": "{SITE}/{OUT}",
  "brand": {{"@type": "Brand", "name": "Unitree"}},
  "seller": {{"@id": "{SITE}/#organizacija"}},
  "additionalProperty": [
{props}
  ]
}}"""


def build():
    doc = open(SRC, encoding="utf-8").read()

    doc = swap_links(doc, LINKS)
    doc = swap_photos(doc)
    doc, missing = translate_texts(doc, TEXTS)
    doc = translate_attrs(doc, ATTRS)
    doc = rewrite_head(doc, slug=OUT, title=TITLE, desc=DESC,
                       og_title=OG_TITLE, og_desc=OG_DESC, og_image=f"{SITE}/og/parduotuve.jpg")
    doc = replace_jsonld(doc, [
        organization_ld(),
        product_ld(),
        breadcrumb_ld([("Pradžia", f"{SITE}/"), ("Parduotuvė", f"{SITE}/{OUT}")]),
        faq_ld(FAQ),
    ])
    doc = strip_comments(doc)
    doc = translate_js(doc, JS_TEXTS)
    doc = apply_contacts(doc)

    missing = [t for t in missing if t in doc]

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"  ✓ {OUT} (perkelta lenkiška parduotuvė)")
    if not check_gtm(doc):
        print("  ! dingo Google Tag Manager")
    if missing:
        print(f"  ! neišversta: {len(set(missing))}")
        for t in sorted(set(missing))[:40]:
            print("     ", t[:110])
    return missing


if __name__ == "__main__":
    build()
