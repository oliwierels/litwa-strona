# -*- coding: utf-8 -*-
"""Sugeneruoja visą 33bots.lt svetainę.

Paleidimas:  python3 build_all.py
"""
import build_index, build_offers, build_blog, build_cities, build_misc, build_hub, build_og, build_seo

STEPS = [
    ("Pagrindinis puslapis", build_index.build),
    ("Paslaugų puslapiai", build_offers.build),
    ("Blogas", build_blog.build),
    ("Miestų puslapiai", build_cities.build),
    ("Kiti puslapiai", build_misc.build),
    ("Robotų nuomos mazgas", build_hub.build),
    ("Open Graph paveikslėliai", build_og.build),
    ("SEO failai", build_seo.build),
]

if __name__ == "__main__":
    for name, fn in STEPS:
        print(f"\n▸ {name}")
        fn()
    print("\n✓ Svetainė sugeneruota.")
