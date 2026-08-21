# -*- coding: utf-8 -*-
"""Sugeneruoja visą 33bots.lt svetainę.

Paleidimas:  python3 build_all.py
"""
import build_index_redesign, build_offers, build_blog, build_cities, build_misc, build_hub
import build_gallery, build_photo_variants, build_og, build_seo

STEPS = [
    ("Pagrindinis puslapis (perkeltas PL dizainas)", build_index_redesign.build),
    ("Paslaugų puslapiai", build_offers.build),
    ("Blogas", build_blog.build),
    ("Miestų puslapiai", build_cities.build),
    ("Kiti puslapiai", build_misc.build),
    ("Robotų nuomos mazgas", build_hub.build),
    ("Nuotraukų variantai", build_photo_variants.build),
    ("Galerijos puslapis", build_gallery.build),
    ("Open Graph paveikslėliai", build_og.build),
    ("SEO failai", build_seo.build),
]

if __name__ == "__main__":
    for name, fn in STEPS:
        print(f"\n▸ {name}")
        fn()
    print("\n✓ Svetainė sugeneruota.")
