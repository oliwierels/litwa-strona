# 33bots.lt — lietuviška 33bots svetainė

Statinė svetainė (HTML + CSS + vanilla JS), generuojama Python skriptais. Lietuviška
33bots.pl / 33bots.at versija, pritaikyta Lietuvos rinkai: savas turinys, miestų puslapiai
ir lokalus SEO.

## Kaip sugeneruoti svetainę

```bash
pip install Pillow          # reikalinga tik Open Graph paveikslėliams
python3 build_all.py
```

Visi `.html` failai, `sitemap.xml`, `robots.txt`, `llms.txt`, `feed.xml` ir `og/` katalogas
yra **generuojami** — jų nereikia redaguoti ranka. Keiskite turinį skriptuose ir paleiskite
`build_all.py` iš naujo.

## Struktūra

| Failas | Ką daro |
| --- | --- |
| `lt_common.py` | Bendri komponentai: `<head>`, navigacija, poraštė, kontaktų forma, schema.org blokai, miestų sąrašas |
| `lt_articles.py` | Blogo straipsnių turinys (tekstai, DUK, metaduomenys) |
| `lt_articles2.py` | Antroji straipsnių banga |
| `lt_offers2.py` | Antroji paslaugų puslapių banga |
| `lt_offers3.py` | Kategoriniai puslapiai (atrakcijos, pramogos, idėjos) — platesnės paieškos frazės |
| `lt_gallery.py` | Galerijos nuotraukų sąrašas ir atvaizdavimas |
| `build_gallery_assets.py` | Paruošia `galerija/` nuotraukas iš tikrų renginių kadrų |
| `build_gallery.py` | `galerija.html` |
| `build_index.py` | Pagrindinis puslapis |
| `build_offers.py` | 16 paslaugų puslapių (renderina `PAGES` + `PAGES2`) |
| `build_hub.py` | `robotu-nuoma.html` — paslaugų ir miestų mazgas (silo struktūra) |
| `build_blog.py` | Blogo indeksas ir 14 straipsnių |
| `build_cities.py` | 28 miestų puslapiai su unikaliu vietos turiniu |
| `build_fonts.py` | Parsisiunčia Inter (latin + latin-ext) į `fonts/`; paleidžiama tik atnaujinant šriftą |
| `build_misc.py` | Kainos, apie mus, kontaktai, vaizdo įrašai, privatumo politika, 404 |
| `build_og.py` | Open Graph paveikslėliai (1200×630) į `og/` |
| `build_seo.py` | `sitemap.xml`, `robots.txt`, `llms.txt`, `feed.xml`, `_redirects`, `.htaccess` |
| `build_all.py` | Paleidžia visus žingsnius iš eilės |

Rankiniu būdu tvarkomi failai: `style.css`, `main.js`, paveikslėliai, `video/`.

## SEO sprendimai

- **hreflang** tarp visų kalbų versijų: `lt` → 33bots.lt, `pl` → 33bots.pl, `de-AT` → 33bots.at,
  `de` → robotollern.de, `x-default` → 33bots.pl. Nustatoma `lt_common.ALTERNATES`.
- **Schema.org**: `ProfessionalService` (bendras `@id`, į kurį nurodo kiti blokai), `WebSite`,
  `Service`, `BreadcrumbList`, `FAQPage`, `BlogPosting`, `VideoObject`, `HowTo`, `OfferCatalog`.
- **Sitemap** su `image:` ir `video:` plėtiniais bei hreflang alternatyvomis pagrindiniam puslapiui.
- **llms.txt** — svetainės santrauka kalbos modeliams (ChatGPT, Perplexity, Claude).
- Unikalūs `title`, `description` ir `canonical` kiekvienam puslapiui; ilgiai neviršija
  65 / 160 simbolių.
- Miestų puslapiai turi savą turinį (vietos renginių scena, tipinės erdvės, regionas), o ne
  pakeistą miesto pavadinimą tame pačiame tekste.
- Sitemapa ir `llms.txt` puslapių sąrašus ima tiesiai iš generatorių, todėl negali atsilikti nuo
  turinio.
- Silo struktūra: `robotu-nuoma.html` sujungia visas paslaugas ir visus miestus, sugrupuotus pagal
  apskritis.
- Kategoriniai puslapiai (`atrakcijos-renginiams`, `atrakcijos-parodoms`, `modernios-pramogos`,
  `renginio-idejos`) taikosi į bendresnes užklausas, kuriose žodžio „robotas“ dar nėra.
- `AggregateRating` ir `Review` naudoja tikrus 33bots klientų atsiliepimus iš Lenkijos projektų —
  puslapyje aiškiai nurodyta, iš kur jie.

## UX sprendimai

- Kalbos perjungiklis navigacijoje (LT / PL / AT / DE).
- „Pereiti prie turinio“ nuoroda ir matomi `:focus-visible` rėmeliai klaviatūros naudotojams.
- Naršymo kelias (breadcrumbs) su struktūrizuotais duomenimis visuose vidiniuose puslapiuose.
- Straipsniuose — turinio lentelė su nuorodomis į skyrius.
- Vaizdo įrašai su `preload="none"` ir plakatais, paveikslėliai su `width`/`height` (be CLS).
- Dviejų žingsnių kontaktinė forma su validacija lietuvių kalba.

## Greitis (Core Web Vitals)

- Inter šriftas talpinamas **lokaliai** (`fonts/`, ~133 KB kintamasis šriftas) — jokių blokuojančių
  užklausų į Google Fonts. Atnaujinama su `python3 build_fonts.py`.
- Kritinis pirmo ekrano CSS įterptas tiesiai į `<head>`; `style.css` kraunamas neblokuojančiai.
- LCP paveikslėlis su `preload`, `fetchpriority="high"` ir WebP variantais.

## Diegimas

Svetainė statinė — tinka bet kuriam hostingui. `_redirects` skirtas Netlify,
`.htaccess` — Apache (HTTPS, non-www, 404, talpykla, gzip).

Po diegimo verta pranešti IndexNow:

```bash
INDEXNOW_KEY=<jūsų raktas> ./scripts/indexnow-submit.sh
```

Prieš tai sugeneruokite raktą ir įkelkite jį kaip `https://33bots.lt/<RAKTAS>.txt`.

## Nuotraukos

`galerija/` turinys generuojamas iš tikrų renginių kadrų (`build_gallery_assets.py`). Šaltiniai —
vaizdo įrašų plakatai ir roboto nuotraukos; viename kadre nukerpama viršutinė juosta su lenkišku
tekstu.

**Naujų nuotraukų pridėjimas:** įkelkite failus į repozitoriją, įrašykite juos į
`build_gallery_assets.SOURCES` ir aprašykite `lt_gallery.PHOTOS` (antraštė + alt tekstas), tada
paleiskite `python3 build_all.py`. Nuotraukos automatiškai atsiras galerijoje, pagrindiniame
puslapyje ir `ImageGallery` struktūrizuotuose duomenyse.

## Ką dar verta padaryti

- Pakeisti Formspree galinį tašką `main.js` savu (dabar naudojamas tas pats kaip 33bots.pl).
- Pridėti tikrus Lietuvos projektų atsiliepimus ir case study, kai jų atsiras.
- Pridėti hreflang nuorodas į 33bots.lt taip pat 33bots.at ir robotollern.de puslapiuose
  (33bots.pl jau nurodo atgal).
- Įkelti daugiau nuotraukų iš renginių — dabar galerijoje yra 8 tikri kadrai, o repozitorijoje
  daugiau nuotraukų nėra.
