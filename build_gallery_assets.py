# -*- coding: utf-8 -*-
"""Paruošia galerijos nuotraukas iš tikrų renginių kadrų.

Kadrai paimti iš vaizdo įrašų plakatų (tikros nuotraukos iš renginių). Vienam kadrui
nukerpama viršutinė juosta su lenkišku tekstu, kad puslapyje liktų tik nuotrauka.
Rezultatas: galerija/*.jpg + *.webp — commitinami į repozitoriją.
"""
import os
from PIL import Image

OUT = "galerija"
MAX_W = 720

# (šaltinis, rezultato vardas, nukerpama viršaus dalis 0–1)
SOURCES = [
    ("video/robot-powitanie-poster.jpg", "svetainiu-pasitikimas", 0.0),
    ("video/robot-taniec-poster.jpg",    "sokio-pasirodymas",     0.0),
    ("video/robot-gesty-poster.jpg",     "gestai-is-arti",        0.0),
    ("video/robot-spacer-poster.jpg",    "judejimas-lauke",       0.0),
    ("video/robot-branding-poster.jpg",  "zenklinimas-qr",        0.0),
    # šiame kadre viršuje įrašytas lenkiškas tekstas — nukerpame 16 % viršaus
    ("video/33bots-robot-event-poster.jpg", "robotas-renginyje",  0.16),
    ("robot-g1.jpg",        "unitree-g1-studija", 0.0),
    ("robot-g1-action.jpg", "g1-choreografija",   0.0),
]


def build():
    os.makedirs(OUT, exist_ok=True)
    made = []
    for src, name, crop_top in SOURCES:
        im = Image.open(src).convert("RGB")
        if crop_top:
            im = im.crop((0, int(im.height * crop_top), im.width, im.height))
        if im.width > MAX_W:
            im = im.resize((MAX_W, round(im.height * MAX_W / im.width)), Image.LANCZOS)
        jpg = f"{OUT}/{name}.jpg"
        im.save(jpg, "JPEG", quality=84, optimize=True, progressive=True)
        im.save(f"{OUT}/{name}.webp", "WEBP", quality=80, method=6)
        made.append((name, im.width, im.height))
    for n, w, h in made:
        print(f"  ✓ {OUT}/{n} — {w}×{h}")
    return made


if __name__ == "__main__":
    build()
