# -*- coding: utf-8 -*-
"""Lenkiškų adresų ir nuotraukų kelių atitikmenys perkeliamuose puslapiuose."""
import re

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
    "sklep.html": "parduotuve.html",
    "wdrozenia.html": "roboto-diegimas.html",
    "case-study-lexai.html": "galerija.html",
    "case-study-wallstreet.html": "galerija.html",
    "case-study-women-in-tech.html": "galerija.html",
}


def swap_photos(doc):
    """Nuotraukų keliai — iš šaknies į nuotraukos/ katalogą.

    Lenkiškoje svetainėje nuotraukos guli šaknyje, lietuviškoje — atskirame kataloge.
    """
    doc = re.sub(r'\b((?:realizacja|robot-pies|robot-g1-studio)[a-z0-9-]*\.(?:jpg|webp))\b',
                 r'nuotraukos/\1', doc)
    return doc.replace("nuotraukos/nuotraukos/", "nuotraukos/")
