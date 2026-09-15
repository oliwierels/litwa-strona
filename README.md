# 33bots.lt — lietuviška 33bots svetainė

Statinė svetainė (HTML + CSS + vanilla JS), generuojama Python skriptais. Lietuviška
33bots.pl / 33bots.at versija, pritaikyta Lietuvos rinkai: savas turinys, miestų puslapiai
ir lokalus SEO.

## Kaip sugeneruoti svetainę

```bash
pip install Pillow          # reikalinga tik Open Graph paveikslėliams
python3 build_all.py        # visi puslapiai ir SEO failai
./buduj.sh                  # Tailwind arkušas perdaryto dizaino puslapiams
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
| `lt_port.py` | Bendri lenkiško šablono perkėlimo įrankiai (vertimas, meta, hreflang, kontaktai) |
| `lt_links.py` | Lenkiškų adresų ir nuotraukų kelių atitikmenys |
| `build_shop.py` | `parduotuve.html` — robotų pardavimas (perkelta iš `sklep.html`) |
| `lt_shop_strings.py` | Parduotuvės vertimo žemėlapis |
| `build_deploy.py` | `roboto-diegimas.html` — diegimai įmonėms (perkelta iš `wdrozenia.html`) |
| `lt_deploy_strings.py` | Diegimų puslapio vertimo žemėlapis |
| `buduj.sh` | Tailwind arkušas (`assets-redesign.css`) + versijos žyma puslapiuose |
| `templates/pl-index.html` | Lenkiškos versijos kopija — porto šaltinis |
| `build_index.py` | Senasis pagrindinio puslapio variantas (nebenaudojamas; iš jo imamas DUK sąrašas) |
| `build_offers.py` | 16 paslaugų puslapių (renderina `PAGES` + `PAGES2`) |
| `build_hub.py` | `robotu-nuoma.html` — paslaugų ir miestų mazgas (silo struktūra) |
| `build_blog.py` | Blogo indeksas ir 14 straipsnių |
| `build_cities.py` | 18 miestų puslapių su savitu vietos turiniu |
| `lt_cities_extra.py` | Kiekvieno miesto formatai ir logistika — savitas turinys, kurio nėra kituose puslapiuose |
| `build_fonts.py` | Parsisiunčia Inter (latin + latin-ext) į `fonts/`; paleidžiama tik atnaujinant šriftą |
| `build_misc.py` | Kainos, apie mus, kontaktai, vaizdo įrašai, privatumo politika, 404 |
| `build_og.py` | Open Graph paveikslėliai (1200×630) į `og/` |
| `build_seo.py` | `sitemap.xml`, `robots.txt`, `llms.txt`, `feed.xml`, `_redirects`, `.htaccess` |
| `build_all.py` | Paleidžia visus žingsnius iš eilės |

Rankiniu būdu tvarkomi failai: `style.css`, `assets-redesign.css`, `main.js`, paveikslėliai, `video/`.

## Du dizainai — kaip 33bots.pl

Lenkiškoje svetainėje perdaryti **trys puslapiai** (`assets-redesign.css`, Tailwind,
Space Grotesk): pagrindinis, parduotuvė ir diegimai; likusieji tebeturi senąjį `style.css`
dizainą. Lietuviška versija tą patį atkartoja: `index.html`, `parduotuve.html` ir
`roboto-diegimas.html` — naujas dizainas, visi kiti — senasis.

Arkušas kompiliuojamas `./buduj.sh` (Tailwind 3.4 per `npx`, konfigūracija
`tailwind.config.js`). Skriptas pažymi kiekvieną puslapį arkušo turinio kontroline suma
(`assets-redesign.css?v=…`), todėl naršyklė niekada nerodo seno arkušo. **Pridėjus naują
perdaryto dizaino puslapį, įrašykite jį į `tailwind.config.js`** — kitaip jo klasės į arkušą
nepateks. Diegimo patikra abu dalykus tikrina ir sustabdo išleidimą, jei `./buduj.sh`
pamirštas.

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
- Miestų puslapių yra 18, ne 28. Dešimt mažiausių buvo sujungti (301) su savo apskrities
  centru: kiekvienas jų turėjo vos 60–70 žodžių savito teksto iš ~865, o toks rinkinys
  Google akyse yra plonas turinys, kurį jis atidėlioja. Nukreipimų sąrašas —
  `lt_common.SUJUNGTI_MIESTAI`, o jį `build_seo` paverčia `.htaccess` ir `_redirects`
  taisyklėmis.
- Likusieji puslapiai turi savą turinį (vietos renginių scena, tipinės erdvės, regionas,
  populiariausi formatai ir logistikos pastabos) — savito teksto padvigubėjo nuo ~74 iki
  ~148 žodžių, o tekstų sutapimas tarp miestų nukrito nuo 0,53 iki 0,44 (6-gramų Jaccard). Be teksto, kiekvienas miesto puslapis turi
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
4. **IndexNow** — jau veikia automatiškai: raktas yra `build_seo.INDEXNOW_KEY`, jo failas
   generuojamas į svetainės šaknį, o po kiekvieno diegimo GitHub Actions praneša Bing,
   Seznam ir Yandex tik tuos adresus, kurių failai pasikeitė. Rankiniu būdu nieko daryti
   nereikia; `scripts/indexnow-submit.sh` lieka atskiriems adresams paskelbti.
5. **Google Business Profile** — sukurti įrašą Lietuvai; vietinei paieškai tai duoda
   daugiau nei bet koks on-page pakeitimas.
6. **Formspree** — naudojamas tas pats galinis taškas kaip 33bots.pl, todėl lietuviškos ir
   lenkiškos užklausos krenta į tą pačią dėžutę. Susikūrus atskirą formą, adresą keiskite
   dviejose vietose: `lt_common.FORM_ENDPOINT` (pagrindinis puslapis) ir `main.js` pradžioje
   (visi kiti puslapiai).
7. **Google Tag Manager** — dabar naudojamas lenkiškas konteineris `GTM-MR7R7CJ3`
   (`lt_common.GTM`). Jei norite atskirti statistiką, pakeiskite į savo.
8. **Telefonas** — el. paštas jau lietuviškas (`kontakt@33bots.lt`), o telefono kol kas
   nerodome niekur: lenkiškas numeris lietuviškoje svetainėje yra silpnas vietos signalas.
   Gavus LT numerį užpildykite `lt_common.PHONE_LT` ir `PHONE_LT_H` — numeris savaime grįš į
   navigaciją, poraštę, kontaktų puslapį, formos klaidos pranešimą, `llms.txt` ir schema.org
   blokus. Vietinis numeris yra vienas stipriausių vietos signalų Google, todėl verta padaryti
   prieš Google Business Profile kūrimą.

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

## Parduotuvė ir diegimai

Be nuomos svetainė turi dvi komercines sekcijas, perkeltas iš 33bots.pl:

- `parduotuve.html` — roboto pirkimas nuosavybėn (Unitree G1, robotas šuo, robotas su diegimu).
  Kainų puslapyje nėra sąmoningai, kaip ir lenkiškoje versijoje: robotai vežami pagal užsakymą,
  todėl kaina pateikiama po pokalbio. Struktūrizuoti duomenys — `Product` su techniniais
  parametrais ir `FAQPage`.
- `roboto-diegimas.html` — kas vyksta nusipirkus: pristatymas ir paleidimas, kalbos programinė
  įranga su žiniomis apie įmonę, komandos mokymai, pagalba po starto. Struktūrizuoti duomenys —
  `Service` ir `FAQPage`.

Abu puslapiai generuojami iš lenkiškų šablonų (`templates/pl-sklep.html`,
`templates/pl-wdrozenia.html`) taip pat, kaip pagrindinis puslapis. Atnaujinus lenkišką versiją:
nukopijuokite naują HTML į `templates/`, paleiskite generatorių ir jis išvardys visus
neišverstus fragmentus.

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
- Įrašyti lietuvišką telefono numerį (`lt_common.PHONE_LT`, `PHONE_LT_H`).
- Įkelti `kontakt@33bots.lt` dėžutę — adresas jau rodomas visuose puslapiuose.
- Pridėti tikrus Lietuvos projektų atsiliepimus ir case study, kai jų atsiras; `lt_common.REVIEWS`
  ir matomos citatos turi keistis kartu.
- Pridėti hreflang nuorodas į 33bots.lt taip pat 33bots.at ir robotollern.de puslapiuose
  (33bots.pl jau nurodo atgal).
- Įkelti nuotraukų iš pirmųjų Lietuvos renginių ir pridėti jas į `lt_gallery.PHOTOS`.
