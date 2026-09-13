# -*- coding: utf-8 -*-
"""Diegimai įmonėms — perkeltas 33bots.pl puslapis „Wdrożenia“.

Šaltinis: templates/pl-wdrozenia.html. Puslapis apie tai, kas vyksta nusipirkus robotą:
pristatymas, kalbos programinė įranga su žiniomis apie įmonę, komandos mokymai ir pagalba.
"""
from lt_common import SITE, organization_ld, breadcrumb_ld, faq_ld
from lt_port import (translate_texts, translate_attrs, translate_js, swap_links, rewrite_head,
                     replace_jsonld, strip_comments, apply_contacts, check_gtm)
from lt_deploy_strings import TEXTS, ATTRS, JS_TEXTS
from lt_links import LINKS, swap_photos

SRC = "templates/pl-wdrozenia.html"
OUT = "roboto-diegimas.html"

TITLE = "Humanoidinio roboto diegimas įmonėje — pardavimas ir mokymai | 33bots"
DESC = ("Įsigyjate humanoidinį robotą, o mes sukonfigūruojame kalbą ir žinias apie jūsų įmonę "
        "bei apmokome komandą. Pristatymas, paleidimas vietoje ir pagalba po starto.")
OG_TITLE = "Humanoidinio roboto diegimas įmonėje | 33bots"
OG_DESC = ("Robotas nuolat jūsų įmonėje: įranga, kalbos programinė įranga su žiniomis apie jūsų "
           "pasiūlymą ir komandos mokymai.")

FAQ = [
    ("Kuo diegimas skiriasi nuo nuomos?",
     "Nuomos atveju atvežame robotą į renginį ir pasiimame jį po pabaigos — valdo mūsų operatorius. "
     "Diegimo atveju robotas tampa jūsų nuosavybe, dirba pas jus kasdien, o valdo jį apmokyta jūsų "
     "komanda. Nuoma tinka pavieniams renginiams, diegimas — kai robotas turi tapti nuolatine "
     "įmonės dalimi."),
    ("Kiek tai kainuoja?",
     "Kaina priklauso nuo roboto modelio bei programinės įrangos ir pagalbos apimties, todėl "
     "kiekvieną diegimą vertiname atskirai. Pasiūlymą parengiame po trumpo pokalbio apie tai, kam "
     "robotas skirtas — be jokių įsipareigojimų iš jūsų pusės."),
    ("Kiek trunka visas diegimas?",
     "Ilgiausias etapas — roboto parvežimas, paprastai apie mėnesį nuo užsakymo. Programinės "
     "įrangos konfigūraciją ir žinių bazę ruošiame lygiagrečiai, todėl po pristatymo lieka "
     "paleidimas ir mokymai — paprastai viena diena pas jus."),
    ("Iš kur robotas žino, ką atsakyti?",
     "Prieš paleidimą įkeliame jam žinias apie jūsų įmonę: pasiūlymą, produktų pavadinimus ir "
     "aprašymus, dažniausius klientų klausimus, darbo laiką, kontaktus. Taip pat suderiname, kaip "
     "jis turi elgtis ir ko neturėtų sakyti. Pasikeitus pasiūlymui, žinių bazę atnaujiname."),
    ("Kas gali valdyti robotą po mokymų?",
     "Bet kuris jūsų komandos žmogus — techninio išsilavinimo nereikia. Mokymai apima paleidimą, "
     "pasirodymo vedimą, krovimą, scenarijų keitimą ir saugos taisykles. Paliekame paprasta kalba "
     "parašytą instrukciją, prie kurios visada galima grįžti."),
    ("O kaip su garantija ir servisu?",
     "Robotui taikoma gamintojo garantija, o mes tarpininkaujame ją administruojant — jums nereikia "
     "susisiekti su Kinija. Techninės pagalbos apimtį po paleidimo suderiname rengdami pasiūlymą, "
     "atsižvelgdami į tai, kaip intensyviai robotas dirbs."),
]


def service_ld():
    return f"""{{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Humanoidinio roboto diegimas įmonėje",
  "description": "Roboto pristatymas ir paleidimas, kalbos programinė įranga su žiniomis apie įmonę, komandos mokymai ir pagalba po starto.",
  "url": "{SITE}/{OUT}",
  "serviceType": "Humanoidinio roboto diegimas",
  "provider": {{"@id": "{SITE}/#organizacija"}},
  "areaServed": {{"@type": "Country", "name": "Lithuania"}},
  "offers": {{
    "@type": "Offer",
    "priceCurrency": "EUR",
    "availability": "https://schema.org/InStock",
    "url": "{SITE}/{OUT}"
  }}
}}"""


def build():
    doc = open(SRC, encoding="utf-8").read()

    doc = swap_links(doc, LINKS)
    doc = swap_photos(doc)
    doc, missing = translate_texts(doc, TEXTS)
    doc = translate_attrs(doc, ATTRS)
    doc = rewrite_head(doc, slug=OUT, title=TITLE, desc=DESC,
                       og_title=OG_TITLE, og_desc=OG_DESC,
                       og_image=f"{SITE}/og/roboto-diegimas.jpg")
    doc = replace_jsonld(doc, [
        organization_ld(),
        service_ld(),
        breadcrumb_ld([("Pradžia", f"{SITE}/"), ("Diegimai", f"{SITE}/{OUT}")]),
        faq_ld(FAQ),
    ])
    doc = strip_comments(doc)
    doc = translate_js(doc, JS_TEXTS)
    doc = apply_contacts(doc)

    missing = [t for t in missing if t in doc]

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"  ✓ {OUT} (perkelti lenkiški diegimai)")
    if not check_gtm(doc):
        print("  ! dingo Google Tag Manager")
    if missing:
        print(f"  ! neišversta: {len(set(missing))}")
        for t in sorted(set(missing))[:40]:
            print("     ", t[:110])
    return missing


if __name__ == "__main__":
    build()
