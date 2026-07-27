# -*- coding: utf-8 -*-
"""Generuoja lietuviškus Open Graph paveikslėlius (1200×630) į og/ katalogą."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

from lt_articles import ARTICLES as _A1
from lt_articles2 import ARTICLES2 as _A2
from build_offers import PAGES as _P1
from lt_offers2 import PAGES2 as _P2
from lt_common import CITIES, city_url

ARTICLES = _A1 + _A2
OFFER_PAGES = _P1 + _P2

W, H = 1200, 630
BASE = "robot-g1.jpg"
OUT = "og"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FOOTER = "33bots.lt — humanoidinių robotų nuoma"

TITLES = {
    "index.jpg": "Humanoidinių robotų nuoma renginiams",
    "robotu-nuoma.jpg": "Robotų nuoma Lietuvoje — visi miestai",
    "blog.jpg": "Žinios apie renginių robotus",
    "kainos.jpg": "Roboto nuomos kainos ir paketai",
    "apie-mus.jpg": "Apie 33bots — viena specializacija",
    "kontaktai.jpg": "Kontaktai — atsakome per 24 val.",
    "video-realizacijos.jpg": "Robotas renginyje — vaizdo įrašai",
}

for p in OFFER_PAGES:
    TITLES[p["slug"].replace(".html", ".jpg")] = p["crumb"]

for a in ARTICLES:
    key = a["slug"].replace(".html", ".jpg")
    TITLES[key] = a["h1"].replace("<br />", " ").replace("<em>", "").replace("</em>", "")

for slug, name, loc, _ in CITIES:
    TITLES[city_url(slug).replace(".html", ".jpg")] = f"Humanoidinio roboto nuoma {loc}"


def wrap(draw, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def make(filename, title):
    base = Image.open(BASE).convert("RGB")
    # visas robotas telpa į kadro aukštį ir dedamas dešinėje pusėje
    ratio = H / base.height
    img = base.resize((round(base.width * ratio), H), Image.LANCZOS)

    canvas = Image.new("RGB", (W, H), (0, 0, 0))
    canvas.paste(img, (W - img.width, 0))

    # tamsinantis gradientas kairėje, kad tekstas būtų kontrastingas
    grad = Image.new("L", (W, 1))
    for x in range(W):
        t = x / W
        grad.putpixel((x, 0), int(238 * max(0.0, 1 - (t / 0.72)) + 12))
    mask = grad.resize((W, H)).filter(ImageFilter.GaussianBlur(2))
    canvas = Image.composite(Image.new("RGB", (W, H), (0, 0, 0)), canvas, mask)

    d = ImageDraw.Draw(canvas)

    size = 62
    while size > 34:
        font = ImageFont.truetype(FONT_BOLD, size)
        lines = wrap(d, title, font, 640)
        if len(lines) <= 3:
            break
        size -= 4
    else:
        font = ImageFont.truetype(FONT_BOLD, 34)
        lines = wrap(d, title, font, 640)[:3]

    d.rectangle([72, 150, 152, 158], fill=(60, 130, 246))

    y = 196
    for line in lines:
        d.text((72, y), line, font=font, fill=(255, 255, 255))
        y += int(size * 1.28)

    f_small = ImageFont.truetype(FONT_REG, 26)
    d.text((72, H - 90), FOOTER, font=f_small, fill=(168, 168, 168))

    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, filename)
    canvas.save(path, "JPEG", quality=86, optimize=True, progressive=True)
    return path


def build():
    for filename, title in TITLES.items():
        make(filename, title)
    print(f"  ✓ og/ — {len(TITLES)} paveikslėlių")


if __name__ == "__main__":
    build()
