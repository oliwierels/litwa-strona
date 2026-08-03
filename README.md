# 33bots.lt — litewska wersja strony

Litewski odpowiednik [33bots.pl](https://33bots.pl) — wynajem humanoidalnych robotów
Unitree G1 na eventy, targi i konferencje.

Layout, UI, CSS i JS pochodzą **bezpośrednio z repo `oliwierels/33bots`** (`style.css`,
`main.js`, zdjęcia robota, wideo). Przetłumaczona jest treść, a ceny przeliczone na EUR.

## Uruchomienie lokalne

```bash
python3 -m http.server 8000
# → http://localhost:8000
```

## Pliki

```
index.html   # cała strona (LT)
style.css    # skopiowane 1:1 z 33bots.pl
main.js      # skopiowane z 33bots.pl, komunikaty przetłumaczone na LT
favicon.svg, og-image.jpg
robot-g1.jpg/.webp, robot-g1-960.webp, robot-g1-action.jpg/.webp
video/33bots-robot-event.mp4 + poster
robots.txt, sitemap.xml
```

## Cennik (LT)

| Pozycja | Cena |
|---|---|
| Robot humanoidalny Unitree G1 | **2 100 – 2 500 € / dzień, be PVM** |
| Robot-pies (dodatek) | 700 € / dzień, be PVM |
| Realizacje 2-dniowe i dłuższe | −15% na każdy dzień |

Ceny są przeliczeniem cennika PL (5500–6500 zł / 1900 zł) z zachowaniem proporcji,
przy dolnym progu **2100 €** zgodnie z wytyczną. **Do zatwierdzenia przed publikacją.**

Miejsca do zmiany przy korekcie cen: sekcja `#kainos`, JSON-LD `AggregateOffer`
(`lowPrice`/`highPrice`), FAQ (pierwsze pytanie + JSON-LD `FAQPage`), meta description i OG.

## Różnice względem wersji polskiej

| Element | PL | LT | Powód |
|---|---|---|---|
| Podstrony (oferta, blog, miasta, case studies) | ~200 plików HTML | brak | w repo LT nie ma odpowiedników — usunięte, żeby nie było martwych linków |
| Nawigacja | dropdown „Oferta" + Blog | anchory jednej strony + przełącznik PL | jw. |
| Lista miast | linki do stron miast | zwykły tekst (30 miast LT) | jw. |
| GTM + Albacross | aktywne | wykomentowany placeholder GTM | brak ID dla LT |
| Telefony | +48 531 408 004, +48 601 499 947 | te same | **brak numeru LT — do dodania** |
| E-mail | kontakt@33bots.pl | info@33bots.lt | **do potwierdzenia, że skrzynka istnieje** |

Sekcje „Mus rodė nacionalinėje televizijoje" i „Mumis pasitikėjo" zachowują prawdziwe
referencje (TVP, Teleexpress, Perspektywy, DSV, Cashify, LEX AI) — opisane po litewsku
jako realizacje w Polsce.

## Do zrobienia przed publikacją

1. **Formspree** — `main.js` → `FORMSPREE_ENDPOINT` wskazuje na formularz PL
   (`mnjwvray`). Leady z LT trafią do tej samej skrzynki; jeśli mają być osobno,
   załóż nowy formularz.
2. **Numer telefonu LT** i weryfikacja adresu `info@33bots.lt`.
3. **GTM** — wklej ID litewskiego kontenera w `index.html` (blok na górze `<head>`).
4. **Polityka prywatności** — link w banerze cookies prowadzi do `#` (tak samo jak w PL).
5. **Ceny** — zatwierdzić przeliczenie EUR.

## SEO

- `hreflang` LT ↔ PL + `x-default`, canonical na `https://33bots.lt/`
- JSON-LD: `Product` + `AggregateOffer` (EUR 2100–2500) + `AggregateRating` + `Review`,
  osobny blok `FAQPage`
- Open Graph i Twitter Card (`og-image.jpg` jest bez tekstu, więc działa dla obu języków)
- `robots.txt`, `sitemap.xml` z alternatywami językowymi
