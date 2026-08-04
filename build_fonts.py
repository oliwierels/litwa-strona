# -*- coding: utf-8 -*-
"""Parsisiunčia Inter šriftą (latin + latin-ext, su lietuviškomis raidėmis) ir talpina jį
lokaliai, kad nereikėtų blokuojančio užklausos į Google Fonts.

Paleidžiama rankiniu būdu, kai reikia atnaujinti šriftus:  python3 build_fonts.py
Rezultatas: fonts/*.woff2 ir fonts.css (abu commitinami į repozitoriją).
"""
import os
import re
import urllib.request

CSS_URLS = [
    ("inter", "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"),
    ("space-grotesk", "https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&display=swap"),
]
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/120.0.0.0 Safari/537.36")
KEEP = ("latin", "latin-ext")   # lietuviškos raidės (ąčęėįšųūž) yra latin-ext rinkinyje
OUT_DIR = "fonts"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def build():
    os.makedirs(OUT_DIR, exist_ok=True)
    out = []
    for family, url in CSS_URLS:
        out.extend(_family(family, fetch(url).decode("utf-8")))

    with open("fonts.css", "w", encoding="utf-8") as f:
        f.write("/* Inter ir Space Grotesk — lokaliai talpinami šriftai (latin + latin-ext).\n"
                "   Generuojama build_fonts.py — nekeiskite ranka. */\n" + "\n".join(out) + "\n")
    print(f"  \u2713 fonts.css ({len(out)} @font-face)")


def _family(family, css):
    blocks = re.findall(r"/\* (\S+) \*/\s*(@font-face \{.*?\})", css, re.S)
    out, seen = [], set()
    name_map = {"inter": "Inter", "space-grotesk": "Space Grotesk"}

    for subset, block in blocks:
        if subset not in KEEP or subset in seen:
            continue
        # Inter tiekiamas kaip kintamasis šriftas — visiems svoriams tas pats failas,
        # todėl vienam poaibiui užtenka vieno atsisiuntimo ir vieno @font-face su svorių ruožu.
        seen.add(subset)
        src = re.search(r"url\((https://[^)]+\.woff2)\)", block).group(1)
        name = f"{family}-{subset}.woff2"
        with open(os.path.join(OUT_DIR, name), "wb") as f:
            f.write(fetch(src))
        unicode_range = re.search(r"unicode-range: ([^;]+);", block).group(1)
        out.append(f"""@font-face {{
  font-family: \'Inter\';
  font-style: normal;
  font-weight: 100 900;
  font-display: swap;
  src: url(\'{OUT_DIR}/{name}\') format(\'woff2\');
  unicode-range: {unicode_range};
}}""")

    return out


if __name__ == "__main__":
    build()
