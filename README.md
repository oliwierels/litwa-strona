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
| `lt_gallery.py` | Nuotraukų sąrašas, galerijos ir juostų atvaizdavimas |
| `build_gallery.py` | `galerija.html` |
| `build_index_redesign.py` | **Pagrindinis puslapis** — perkeltas 33bots.pl perdarytas dizainas |
| `lt_index_strings.py` | Pagrindinio puslapio vertimo žemėlapis (PL → LT) ir kainos |
| `templates/pl-index.html` | Lenkiškos versijos kopija — porto šaltinis |
| `build_index.py` | Senasis pagrindinio puslapio variantas (nebenaudojamas; iš jo imamas DUK sąrašas) |
| `build_offers.py` | 16 paslaugų puslapių (renderina `PAGES` + `PAGES2`) |
| `build_hub.py` | `robotu-nuoma.html` — paslaugų ir miestų mazgas (silo struktūra) |
| `build_blog.py` | Blogo indeksas ir 14 straipsnių |
| `build_cities.py` | 28 miestų puslapiai su unikaliu vietos turiniu |
| `build_fonts.py` | Parsisiunčia Inter (latin + latin-ext) į `fonts/`; paleidžiama tik atnaujinant šriftą |
| `build_misc.py` | Kainos, apie mus, kontaktai, vaizdo įrašai, privatumo politika, 404 |
| `build_og.py` | Open Graph paveikslėliai (1200×630) į `og/` |
| `build_seo.py` | `sitemap.xml`, `robots.txt`, `llms.txt`, `feed.xml`, `_redirects`, `.htaccess` |
| `build_all.py` | Paleidžia visus žingsnius iš eilės |

Rankiniu būdu tvarkomi failai: `style.css`, `assets-redesign.css`, `main.js`, paveikslėliai, `video/`.

## Du dizainai — kaip 33bots.pl

Lenkiškoje svetainėje perdarytas **tik pagrindinis puslapis** (`assets-redesign.css`, Tailwind,
Space Grotesk), o likę 187 puslapiai tebeturi senąjį `style.css` dizainą. Lietuviška versija tą patį
atkartoja: naujas pagrindinis puslapis + senojo dizaino vidiniai puslapiai.

Kai lenkiškas dizainas bus išplėstas į vidinius puslapius, tą patį reikės padaryti ir čia.
Atnaujinant pagrindinį puslapį: nukopijuokite naują `index.html` į `templates/pl-index.html`,
papildykite `lt_index_strings.TEXTS` naujais tekstais ir paleiskite `build_all.py` — skriptas
išvardija visus neišverstus fragmentus.

## SEO sprendimai

- **hreflang** tarp visų kalbų versijų: `lt` → 33bots.lt, `pl` → 33bots.pl, `de-AT` → 33bots.at,
  `de` → robotollern.de, `x-default` → 33bots.pl. Nustatoma `lt_common.EQUIVALENTS`
  (puslapiams be atitikmens lieka tik savoji `lt` nuoroda ir `x-default` į save).
  Diegimo patikra neleidžia išvežti puslapio, kuriame svetimos kalbos nuoroda rodo
  į 33bots.lt — būtent tokia klaida buvo įsivėlusi pagrindiniame puslapyje.
- **Schema.org**: `ProfessionalService` (bendras `@id`, į kurį nurodo kiti blokai), `WebSite`,
  `Service`, `BreadcrumbList`, `FAQPage`, `BlogPosting`, `VideoObject`, `HowTo`, `OfferCatalog`.
- **Sitemap** su `image:` ir `video:` plėtiniais bei hreflang alternatyvomis pagrindiniam puslapiui.
- **llms.txt** — svetainės santrauka kalbos modeliams (ChatGPT, Perplexity, Claude).
- Unikalūs `title`, `description` ir `canonical` kiekvienam puslapiui; ilgiai neviršija
  65 / 160 simbolių.
- Miestų puslapiai turi savą turinį (vietos renginių scena, tipinės erdvės, regionas), o ne
  pakeistą miesto pavadinimą tame pačiame tekste. Be teksto, kiekvienas miesto puslapis turi
  savo DUK klausimą (surenkamą iš to miesto erdvių sąrašo), savo nuotraukų rinkinį
  (`lt_gallery.rotate_for` — 27 skirtingi rinkiniai 28 miestams), savo aprašymą su apskrities
  pavadinimu ir savą kitų miestų nuorodų rinkinį (sąrašas sukamas nuo esamo miesto, todėl
  vidinių nuorodų svoris pasiskirsto po visus 28, o ne po pirmus devynis).
- Sitemapa ir `llms.txt` puslapių sąrašus ima tiesiai iš generatorių, todėl negali atsilikti nuo
  turinio.
- Silo struktūra: `robotu-nuoma.html` sujungia visas paslaugas ir visus miestus, sugrupuotus pagal
  apskritis.
- Kategoriniai puslapiai (`atrakcijos-renginiams`, `atrakcijos-parodoms`, `modernios-pramogos`,
  `renginio-idejos`) taikosi į bendresnes užklausas, kuriose žodžio „robotas“ dar nėra.
- `AggregateRating` ir `Review` (pagrindinio puslapio `Product` blokas) naudoja tikrus 33bots
  klientų atsiliepimus iš Lenkijos projektų — virš atsiliepimų puslapyje tai pasakyta atvirai.
  Šaltinis vienas: `lt_common.REVIEWS`; `build_index_redesign.check_reviews` statybos metu
  įspėja, jei struktūrizuotas atsiliepimas nebesutampa su matomu tekstu.

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

Svetainė diegiama **automatiškai iš GitHub** — lygiai taip pat kaip 33bots.pl. Kiekvienas
pakeitimas, įkeltas į `claude/lithuanian-33bots-site-4v8qf8` šaką, per kelias sekundes atsiduria
33bots.lt: GitHub Actions patikrina puslapius, o tada serveris pats parsisiunčia paketą iš GitHub
per HTTPS (`narzedzia-serwer/deploy.php`). Rankiniu būdu per FTP nieko kelti nereikia.

Vienkartinis nustatymas (token, `deploy.php` įkėlimas, `DEPLOY_URL` ir `DEPLOY_TOKEN` paslaptys)
aprašytas [`WDROZENIE.md`](WDROZENIE.md).

Svetainė statinė — visas repozitorijos turinys keliamas į serverio šaknį. `_redirects` skirtas
Netlify, `.htaccess` — Apache (HTTPS, non-www, 404, talpykla, gzip).

### Ką padaryti paleidžiant

1. **Domenas ir HTTPS** — nukreipti 33bots.lt į serverį, įjungti sertifikatą.
   Non-www ir HTTPS peradresavimai jau paruošti `.htaccess` / `_redirects`.
2. **Google Search Console** — pridėti 33bots.lt, patvirtinti nuosavybę ir pateikti
   `https://33bots.lt/sitemap.xml` (71 adresas).
3. **Bing Webmaster Tools** — tas pats sitemap; iš čia veikia ir IndexNow.
4. **IndexNow raktas** — sugeneruoti raktą, įkelti kaip `https://33bots.lt/<RAKTAS>.txt`
   ir paleisti `INDEXNOW_KEY=<raktas> ./scripts/indexnow-submit.sh`.
5. **Google Business Profile** — sukurti įrašą Lietuvai; vietinei paieškai tai duoda
   daugiau nei bet koks on-page pakeitimas.
6. **Formspree** — naudojamas tas pats galinis taškas kaip 33bots.pl, todėl lietuviškos ir
   lenkiškos užklausos krenta į tą pačią dėžutę. Susikūrus atskirą formą, adresą keiskite
   dviejose vietose: `lt_common.FORM_ENDPOINT` (pagrindinis puslapis) ir `main.js` pradžioje
   (visi kiti puslapiai).
7. **Google Tag Manager** — dabar naudojamas lenkiškas konteineris `GTM-MR7R7CJ3`
   (`lt_common.GTM`). Jei norite atskirti statistiką, pakeiskite į savo.
8. **Lietuviški kontaktai** — telefonas ir el. paštas struktūrizuotuose duomenyse kol kas
   lenkiški (`+48…`, `kontakt@33bots.pl`). Gavus LT numerį ir pašto dėžutę 33bots.lt domene,
   užpildykite `lt_common.EMAIL_LT`, `PHONE_LT` ir `PHONE_LT_H` — jie automatiškai pakeis
   lenkiškus visuose puslapiuose, formoje ir schema.org blokuose. Vietinis numeris ir adresas
   yra vienas stipriausių vietos signalų Google, todėl verta padaryti prieš Google Business
   Profile kūrimą.

### Patikra po paleidimo

- `https://33bots.lt/robots.txt` ir `/sitemap.xml` atsidaro be klaidų
- Search Console → Patikrinti URL pagrindiniam puslapiui (ar mato kainą ir `Offer`)
- Rich Results Test: FAQ, Service su kaina, BreadcrumbList, ImageGallery
- hreflang poros: 33bots.pl jau nurodo atgal į 33bots.lt (8 puslapiai)

## Nuotraukos

`nuotraukos/` — 16 kadrų iš tikrų 33bots realizacijų (Women in Tech Summit, gala vakarai,
LEX AI akcijos, verslo susitikimai, roboto šuo su kliento ženklinimu). Perimta iš vokiškos
33bots versijos, kad visos kalbų versijos rodytų tuos pačius projektus.

Atvaizdavimas (`lt_gallery.py`):

- `gallery_section()` — pilna mozaikinė galerija (pagrindiniame puslapyje, mazge, `galerija.html`);
  išdėstymo klasės `shot--wide` / `shot--narrow` perimtos iš vokiškos versijos.
- `strip_section(slug)` — kompaktiška juosta paslaugų ir miestų puslapiuose. Nuotraukų rinkinys
  parenkamas pagal puslapio adresą, todėl **kiekvienas puslapis rodo kitas nuotraukas** ir svetainė
  neatrodo monotoniškai.

**Naujų nuotraukų pridėjimas:** įkelkite failus (`.jpg` + `.webp`) į `nuotraukos/`, įrašykite juos
į `lt_gallery.PHOTOS` (failas, išdėstymo klasė, antraštė, alt tekstas) ir paleiskite
`python3 build_all.py`.

## Kainos

Kainos Lietuvos rinkai nustatytos `lt_index_strings.py` viršuje:

| Konstanta | Reikšmė | Kur rodoma |
| --- | --- | --- |
| `PRICE_FROM` | 2 100 € | hero blokas, kainų kortelė, DUK, „Visa diena“ paketas |
| `PRICE_DOG` | 690 € | roboto šuns kortelė, DUK |
| `DISCOUNT` | 15% | „Kelios dienos“ paketas, DUK |

Pakeitus reikšmę ir paleidus `build_all.py`, kaina atsinaujina visose vietose vienu metu —
įskaitant `Offer` bloką struktūrizuotuose duomenyse ir `priceRange` organizacijos apraše
(`lt_common.py`).

**Transportas nėra įskaičiuotas.** Kaip ir 33bots.pl nuo 2026-08-14, atvykimą vertiname pagal
renginio vietą, o 2 100 € yra pradinė kaina už visą realizacijos dieną. Jokiame puslapyje
nerašome „nemokamas transportas" ar „transportas — 0 €".

## Ką dar verta padaryti

- Pakeisti Formspree galinį tašką savu (`lt_common.FORM_ENDPOINT` + `main.js`).
- Įrašyti lietuviškus kontaktus (`lt_common.EMAIL_LT`, `PHONE_LT`, `PHONE_LT_H`).
- Pridėti tikrus Lietuvos projektų atsiliepimus ir case study, kai jų atsiras; `lt_common.REVIEWS`
  ir matomos citatos turi keistis kartu.
- Pridėti hreflang nuorodas į 33bots.lt taip pat 33bots.at ir robotollern.de puslapiuose
  (33bots.pl jau nurodo atgal).
- Įkelti nuotraukų iš pirmųjų Lietuvos renginių ir pridėti jas į `lt_gallery.PHOTOS`.
