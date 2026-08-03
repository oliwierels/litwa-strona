# 33bots.lt — landing page (LT)

Litewska wersja strony 33bots. Statyczny HTML/CSS/JS — bez build-stepu, bez zależności,
bez zewnętrznych requestów (fonty systemowe, ikony jako inline SVG).

## Uruchomienie lokalne

```bash
python3 -m http.server 8000
# → http://localhost:8000
```

## Struktura

```
index.html            # cała strona (jeden plik, wszystkie sekcje)
assets/css/styles.css # style + responsywność
assets/js/main.js     # nawigacja, animacje, kalkulator ROI, formularz
assets/img/favicon.svg
assets/img/og.png     # obrazek Open Graph 1200×630
assets/img/og.html    # szablon do regeneracji og.png (nieużywany przez stronę)
robots.txt, sitemap.xml, site.webmanifest
```

## Konfiguracja przed publikacją

| Co | Gdzie | Uwaga |
|---|---|---|
| Domena | `index.html` — `canonical`, `hreflang`, `og:url`, JSON-LD; `robots.txt`; `sitemap.xml` | wszędzie wpisane `https://33bots.lt/` |
| E-mail | `index.html` (sekcja kontaktu, stopka), `assets/js/main.js` → `FALLBACK_EMAIL` | obecnie `info@33bots.lt` |
| Endpoint formularza | `assets/js/main.js` → `FORM_ENDPOINT` | **pusty** — patrz niżej |
| Ceny | `index.html` sekcja `#kainos` + JSON-LD `offers.price` | 2 100 € / 4 900 € / indywidualnie, wszystko **be PVM** |
| Założenia kalkulatora | `assets/js/main.js` → `UPLIFT` (0.30), `IMPLEMENTATION` (2100) | |

### Formularz kontaktowy

Dopóki `FORM_ENDPOINT` jest pusty, formularz otwiera klienta pocztowego (`mailto:`)
z wypełnioną treścią. Po wpisaniu adresu endpointu wysyła `POST` z JSON-em
(`name, company, email, phone, budget, message, gdpr`) — działa z Formspree,
Make, n8n, Zapier Webhooks lub własnym API.

Walidacja (wymagane: imię, e-mail, zgoda RODO) i honeypot na boty są po stronie klienta —
**walidację i antyspam trzeba powtórzyć po stronie serwera.**

## SEO

- semantyczny HTML, jeden `h1`, hierarchia nagłówków
- meta description, Open Graph, Twitter Card
- `hreflang` LT ↔ PL (`33bots.pl`) + `x-default`
- JSON-LD: `Organization`, `WebSite`, `Service` (z ceną od 2100 EUR), `FAQPage`
- `sitemap.xml` z alternatywami językowymi, `robots.txt`
- zero blokujących zasobów zewnętrznych → dobre Core Web Vitals

### Regeneracja og.png

Zrzut `assets/img/og.html` w rozdzielczości 1200×630 (dowolne narzędzie, np. Chromium headless).

## Dostępność

Skip link, focus-visible, `aria-expanded` na menu, `aria-live` na kalkulatorze i statusie
formularza, obsługa Escape, pełne wsparcie `prefers-reduced-motion`.

## Elementy konwersyjne

CTA w nawigacji, hero (×2), kalkulatorze, każdym pakiecie, stopce oraz przyklejony
CTA na mobile · kalkulator ROI · cennik z wyróżnionym pakietem · dowody społeczne
(statystyki, case'y, cytat) · FAQ zdejmujące obiekcje · formularz z pytaniem o budżet.

## Treść

Copy (statystyki, case studies, cytat) to **placeholdery** napisane pod strukturę strony —
przed publikacją należy podmienić je na realne dane 33bots.
