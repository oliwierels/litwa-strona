# 33bots.lt — lietuviška 33bots svetainė

Statinė svetainė (HTML + CSS + JS). Puslapiai generuojami bendru 33bots generatoriumi,
kuris kuria ir 33bots.de bei 33bots.at: tas pats dizainas kaip 33bots.pl, ta pati
dviejų žingsnių forma, tie patys automatiniai testai.

## Kaip sugeneruoti svetainę

Šaltiniai yra repozitorijoje `oliwierels/33bots`, kataloge `tresci/zagranica/`:

| Failas | Ką daro |
| --- | --- |
| `rynki.py`, skyrius `LT` | pagrindinio puslapio tekstai, kainos, DUK, realizacijos, navigacija, poraštė, klientų pavadinimai |
| `glowa-lt.html` | pagrindinio puslapio `<head>`: title, meta, hreflang, CSP, GTM, schema.org |
| `podstrony/lt/*.html` | vidiniai puslapiai: JSON antraštė (title, description, hreflang, DUK, schema.org) ir turinys |
| `buduj_glowna.py lt <repo>` | `index.html` |
| `buduj_podstrony.py lt <repo>` | vidiniai puslapiai ir `feed.xml` |
| `buduj_mape.py <repo> 33bots.lt` | `sitemap.xml` — iš sugeneruotų puslapių (canonical, hreflang, og:image, VideoObject) |
| `buduj_llms.py lt <repo>` | `llms.txt` — faktai ir puslapių sąrašas, sugrupuotas kaip poraštėje |

```bash
cd 33bots/tresci/zagranica
python3 buduj_glowna.py lt /kelias/iki/litwa-strona
python3 buduj_podstrony.py lt /kelias/iki/litwa-strona
python3 buduj_mape.py /kelias/iki/litwa-strona 33bots.lt
python3 buduj_llms.py lt /kelias/iki/litwa-strona
```

Prieš įkeliant: `python3 auditas.py . 33bots.lt` (title ir description ilgiai, canonical,
hreflang, schema.org) ir Playwright testai `qa/zagranica.spec.mjs` 33bots repozitorijoje —
`.lt` tikrinama kartu su `.de` ir `.at`.

## Rankiniu būdu tvarkomi failai

- `parduotuve.html`, `roboto-diegimas.html` — perkelti iš 33bots.pl (Tailwind,
  `assets-redesign.css`), redaguojami tiesiai HTML. Pakeitus klases — `./buduj.sh`.
- `.htaccess`, `_redirects` — 301 nukreipimai, saugumo antraštės, CSP. CSP antraštė turi
  sutapti su CSP `glowa-lt.html`: galioja abi, todėl siauresnė užblokuotų analitiką.
- `robots.txt`, `css/site.css`, `js/strona.js`, `fonts/`, paveikslėliai, `video/`, `og/`.

## Faktai, kurie turi sutapti visuose puslapiuose

- Visa renginio diena — nuo 2 100 € be PVM. Trumpesnis pasirodymas (kelios valandos) —
  individuali kaina, visada mažesnė nei visos dienos. Nuo dviejų dienų — −15 % kiekvienai dienai.
- Į kainą įeina: sertifikuotas operatorius, atvykimas, ženklinimas (logotipas ir QR kodas),
  civilinės atsakomybės draudimas. Atvykimas įskaičiuotas, o renginio vieta turi įtakos
  galutinei sumai — kaip 33bots.pl.
- Rezervacija be avanso, sąskaita po renginio. Atsakymas per 24 darbo valandas.
- Unitree G1: 132 cm, 35 kg, 23 laisvės laipsniai, iki 2 m/s. Vietoje reikia ~2×2 m ir
  230 V lizdo; atvykstame ~1,5 val. iki pirmo pasirodymo, operatorius pasiruošia per 30–45 min.
- Robotas kalba lietuviškai ir bet kuria kita kalba. Daugiau nei 40 renginių penkiose šalyse.
- Niekur nerašome „nemokamas“ ir „kostiumas“ — „įskaičiuota į kainą“ ir „ženklinimas“.
  Testai tai tikrina ir matomame tekste, ir puslapio kode (meta, schema.org).
- Lenkiškų įmonių ir vietovių pavadinimai rodomi lietuviškai (Verslininkų ložė, Rekord grupė,
  Mikolaikai); tarptautiniai prekių ženklai lieka kaip yra.

## SEO

- **Renginių gidas** (`blog.html`): gidai apie pramogas renginiams, renginių ir vestuvių
  vedėjus, fotobūdeles, pramogas vestuvėms, kalėdinius vakarėlius ir komandos formavimą.
  Robotas juose — viena iš pramogų, o ne vienintelis sprendimas: taip svetainė gauna
  užklausas, kuriose žodžio „robotas“ nėra. Gidai turi `"gidas"` lauką JSON antraštėje,
  pagal kurį sudaromas rodyklės puslapis.
- **Robotas vedėjas** (`robotas-vedejas.html`) — paslaugos puslapis vedėjo užklausoms,
  hreflang pora su 33bots.de `roboter-eventmoderation.html`.
- **Miestai**: 18 puslapių; dešimt mažesnių sujungti (301) su apskrities centru.
- **Sujungti puslapiai (301)**: `atrakcijos-renginiams`, `modernios-pramogos`,
  `blog-renginio-pramogos-idejos`, `blog-robotas-ar-kitos-pramogos` → `pramogos-renginiams`;
  `blog-kaledinio-renginio-planavimas` → `kaledinio-vakarelio-idejos`.
- **hreflang**: `lt` ↔ `pl` / `de` / `de-AT`, `x-default` → 33bots.pl — tik puslapiams su
  tikru atitikmeniu, abiem kryptimis.
- **IndexNow**: po kiekvieno diegimo GitHub Actions praneša tik pasikeitusius adresus
  (raktas — `da66134087cc25b2d1bc36011f30f615.txt`).

## Diegimas

Svetainė diegiama **automatiškai iš GitHub**, kaip 33bots.pl. Kiekvienas pakeitimas šakoje
`claude/lithuanian-33bots-site-4v8qf8` per kelias sekundes atsiduria 33bots.lt: GitHub Actions
patikrina puslapius, o serveris pats parsisiunčia paketą per HTTPS (`narzedzia-serwer/deploy.php`).
Vienkartinis nustatymas aprašytas [`WDROZENIE.md`](WDROZENIE.md).

## Ką dar verta padaryti

- **Lietuviškas telefono numeris** — vienas stipriausių vietos signalų Google. Gavus numerį,
  įrašyti į `rynki.py` (LT `kontakt_lista`, `stopka_kontakt`) ir `glowa-lt.html`.
- **Google Business Profile** Lietuvai.
- **Search Console ir Bing Webmaster Tools** — pateikti `https://33bots.lt/sitemap.xml`.
- Tikri Lietuvos projektų atsiliepimai ir case study, kai jų atsiras.
