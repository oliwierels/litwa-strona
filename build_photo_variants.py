# -*- coding: utf-8 -*-
"""Sukuria 400 px pločio WebP variantus galerijos nuotraukoms.

Perdarytas pagrindinis puslapis naudoja srcset su 400w ir 760w variantais,
todėl mobiliuose įrenginiuose atsisiunčiama mažesnė nuotrauka.
"""
import glob
import os

from PIL import Image

DIR = "nuotraukos"
WIDTHS = [400, 760]


def build():
    made = 0
    for src in sorted(glob.glob(f"{DIR}/*.jpg")):
        name = os.path.splitext(os.path.basename(src))[0]
        if name.endswith(("-400", "-760")):
            continue
        im = Image.open(src).convert("RGB")
        for w in WIDTHS:
            if im.width < w:
                continue
            out = f"{DIR}/{name}-{w}.webp" if w != 760 else f"{DIR}/{name}.webp"
            r = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
            r.save(out, "WEBP", quality=80, method=6)
            made += 1
    print(f"  \u2713 {DIR}/ — {made} WebP variantų")


if __name__ == "__main__":
    build()
