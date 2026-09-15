# Automatyczne wdrożenie 33bots.lt

Dokładnie ten sam mechanizm, co na `33bots.pl`. Po skonfigurowaniu każda zmiana
zatwierdzona na gałęzi `claude/lithuanian-33bots-site-4v8qf8` trafia na
`33bots.lt` w kilkanaście sekund — bez ręcznego wgrywania plików przez FTP.

## Jak to działa

```
zmiana w repozytorium  →  GitHub sprawdza stronę  →  puka do serwera
                                                          ↓
                                   serwer sam pobiera paczkę z GitHuba po HTTPS
```

**Kierunek jest odwrotny niż przy FTP — to serwer sięga po zmiany.** Tak samo jak
na 33bots.pl: hosting blokuje połączenia FTP z adresów serwerowni GitHuba, a
pobieranie po HTTPS z serwera na zewnątrz działa bez przeszkód. Przy okazji jest
bezpieczniej — hasło FTP nigdzie nie wyjeżdża.

Pliki:

- `.github/workflows/wdrozenie.yml` — sprawdzenie strony i sygnał do serwera
- `narzedzia-serwer/deploy.php` — punkt wdrożeniowy, wgrywany na hosting raz

## Konfiguracja — jednorazowo, ok. 10 minut

### Krok 1. Wpisz token do `deploy.php`

Wygeneruj losowy token (min. 16 znaków, najlepiej ok. 40):

```bash
openssl rand -base64 32 | tr -d '/+=' | cut -c1-40
```

Wstaw go w `narzedzia-serwer/deploy.php` w stałej `TOKEN`, w miejsce
`WSTAW_TUTAJ_SWOJ_TOKEN`. **Tej wersji z tokenem nie zatwierdzaj w repozytorium** —
plik z tokenem wgrywasz tylko na serwer.

### Krok 1b. Token GitHuba — tylko dla repozytorium prywatnego

`litwa-strona` jest prywatne, a serwer pobiera paczkę sam. Bez tokenu GitHub odpowiada na
takie pobranie **404** (prywatnych repozytoriów nie ujawnia nawet ich istnieniem), więc
`deploy.php` musi się przedstawić.

Wygeneruj **fine-grained token**: https://github.com/settings/personal-access-tokens/new

| Pole | Wartość |
|---|---|
| Repository access | Only select repositories → `litwa-strona` |
| Permissions → Contents | Read-only |
| Expiration | wedle uznania (po wygaśnięciu wdrożenia przestaną działać) |

Wklej go w `deploy.php` w stałej `GITHUB_TOKEN`. Token zostaje na serwerze — nigdzie go nie
zatwierdzamy w repozytorium.

Alternatywa bez tokenu: ustawić repozytorium jako publiczne (tak działa `33bots`). Wtedy
`GITHUB_TOKEN` zostaje pusty.

### Krok 2. Wgraj punkt wdrożeniowy na serwer

Plik `deploy.php` (ten z wpisanym tokenem) wgraj przez Managera plików do
katalogu, w którym leży strona 33bots.lt — czyli tam, gdzie ma trafiać
`index.html` (zwykle `domains/33bots.lt/public_html`).

Skrypt rozpakowuje stronę **do katalogu, w którym sam leży**, więc jego
umiejscowienie decyduje o tym, gdzie wyląduje strona.

### Krok 3. Sprawdź, czy serwer jest gotowy

Otwórz w przeglądarce, podstawiając swój token:

```
https://33bots.lt/deploy.php?token=TWOJ_TOKEN&test=1
```

Powinieneś zobaczyć wersję PHP, dostępność `ZipArchive` i cURL oraz możliwość
zapisu do katalogu. Bez tokenu albo z błędnym tokenem skrypt zwraca
`Brak dostępu` i nic nie robi.

### Krok 4. Dodaj dwa sekrety na GitHubie

`github.com/oliwierels/litwa-strona` → **Settings** → **Secrets and variables**
→ **Actions** → **New repository secret**

| Nazwa | Wartość |
|---|---|
| `DEPLOY_URL` | `https://33bots.lt/deploy.php` |
| `DEPLOY_TOKEN` | token wpisany w `deploy.php` |

### Krok 5. Uruchom

Zatwierdź dowolną zmianę na gałęzi produkcyjnej — push uruchamia wdrożenie sam. Bez nowego
commita: `Actions` → ostatnie uruchomienie → **Re-run all jobs** (przycisku „Run workflow"
tu nie ma; dlaczego — niżej).

Przed pierwszym uruchomieniem warto zrobić kopię katalogu strony
(Manager plików → zaznacz wszystko → Kompresuj).

---

## Praca na co dzień

Strona jest generowana skryptami, więc po zmianie treści:

```bash
python3 build_all.py
./buduj.sh
```

a potem zatwierdzasz **zarówno skrypty, jak i wygenerowane pliki HTML**.
`buduj.sh` kompiluje arkusz Tailwinda dla trzech stron w nowym dizajnie (`index.html`,
`parduotuve.html`, `roboto-diegimas.html`) i oznacza go w nich sumą kontrolną.
Zatwierdzenie na gałęzi produkcyjnej uruchamia wdrożenie samo.

Ostrzeżenie: wdrażany jest stan repozytorium, a nie wynik `build_all.py`.
Jeśli zmienisz sam skrypt i zapomnisz go uruchomić, na serwer pójdzie stary HTML.

## Bramka bezpieczeństwa

Zanim GitHub poprosi serwer o cokolwiek, sprawdza **wszystkie 72 strony**:

- czy znaczniki HTML są domknięte,
- czy wszystkie bloki danych strukturalnych to poprawny JSON,
- czy na każdej stronie jest Google Tag Manager,
- czy `main.js` nie zgubił adresu formularza kontaktowego, a strona z formularzem
  ma jego obsługę,
- czy każda strona ma adres kanoniczny w domenie `33bots.lt` i czy żaden nie
  powtarza się na dwóch stronach,
- czy hreflang obcych wersji językowych nie wskazuje na 33bots.lt, a `x-default`
  strony głównej prowadzi na 33bots.pl (to wyłapuje błąd, przez który generator
  nadpisywał adresy wersji PL własną domeną),
- czy strona nie odwołuje się do pliku, którego nie ma w repozytorium
  (zdjęcia, arkusze, czcionki, podstrony),
- czy `sitemap.xml` to poprawny XML i czy każdy wymieniony adres ma swój plik,
- czy arkusz Tailwinda oznaczony na stronie odpowiada temu w repozytorium (wyłapuje
  pominięte `./buduj.sh`) i czy każda taka strona jest wymieniona w `tailwind.config.js`.

**Gdy którykolwiek warunek nie jest spełniony, wdrożenie się zatrzymuje**
i strona zostaje w poprzedniej, działającej wersji.

## Co nie trafia na serwer

Skrypty `.py`, katalog `templates/` (kopie polskich stron jako źródło portu),
`scripts/`, pliki `.md`, `.gitignore`, `_redirects` (to konfiguracja Netlify —
na Apache czytany jest `.htaccess`), narzędzia budowania arkusza
(`tailwind.config.js`, `tw-input.css`, `buduj.sh`), katalog `.git`, `.github/`,
`narzedzia-serwer/` i sam `deploy.php`.

W odróżnieniu od 33bots.pl **wysyłany jest katalog `og/`** — obrazki Open Graph
litewskiej wersji powstają z generatora i nie ma ich nigdzie indziej. Tak samo
`fonts/`, `nuotraukos/` i `video/`. Listę wykluczeń trzymają stałe na górze
`deploy.php`.

## Czego wdrożenie nie kasuje

Pliki wgrane ręcznie, których nie ma w repozytorium, zostają nietknięte.
Skrypt nadpisuje tylko to, co przychodzi z GitHuba, i pomija pliki o identycznej
treści — dzięki temu typowe wdrożenie dotyka kilku plików, a nie całej strony.

## Gdy coś pójdzie nie tak

Otwórz nieudane uruchomienie w zakładce **Actions** — odpowiedź serwera jest
wypisana w całości.

| Objaw | Przyczyna |
|---|---|
| `Brak dostępu` | Token w `deploy.php` różni się od sekretu `DEPLOY_TOKEN` |
| `Skrypt nie został skonfigurowany` | W `deploy.php` na serwerze został placeholder zamiast tokenu |
| `Brak rozszerzenia ZipArchive` | Hosting nie ma tego rozszerzenia — trzeba zmienić metodę |
| `Pobieranie nie powiodło się (HTTP 404)` | Repozytorium prywatne, a `GITHUB_TOKEN` w `deploy.php` pusty (albo zła nazwa gałęzi) |
| `Pobieranie nie powiodło się (HTTP 401/403)` | Token GitHuba wygasł lub nie obejmuje tego repozytorium |
| `Pobieranie nie powiodło się` | Serwer nie dosięgnął GitHuba — sprawdź ruch wychodzący hostingu |
| Zatrzymanie na bramce | Błąd w którejś stronie; log podaje który. Na serwer nic nie poszło |
| `serwer podaje inną treść strony głównej` | Bufor hostingu — zwykle mija po chwili; to tylko ostrzeżenie |

## Wycofanie zmiany

Cofnij commit (`git revert`) i zatwierdź — wdrożenie uruchomi się samo
i przywróci poprzedni stan strony.

## Bezpieczeństwo

`deploy.php` potrafi nadpisać pliki strony, więc:

- token jest długi i losowy — nie da się go zgadnąć,
- bez poprawnego tokenu skrypt kończy działanie na pierwszej instrukcji,
- pobiera wyłącznie z jednego, wpisanego na stałe repozytorium i jednej gałęzi,
- gdybyś kiedyś zrezygnował z automatu, po prostu usuń plik z serwera.

Zmieniając token, zmień go w obu miejscach naraz: w `deploy.php` na serwerze
i w sekrecie `DEPLOY_TOKEN` na GitHubie.

## Ręczne uruchomienie — bez przycisku „Run workflow"

GitHub pokazuje przycisk **Run workflow** tylko wtedy, gdy plik workflow istnieje na
**domyślnej gałęzi** repozytorium. Tutaj strona i workflow są na gałęzi produkcyjnej,
a domyślna jest `main` — dlatego przycisku nie ma. Zamiast niego:

- **Powtórz ostatni przebieg**: `Actions` → wybierz ostatnie uruchomienie → **Re-run all jobs**.
  Wdroży aktualny stan gałęzi.
- **Albo po prostu zatwierdź zmianę** — każdy push na gałąź produkcyjną uruchamia wdrożenie sam.

Gdyby przycisk był potrzebny na stałe, są dwie drogi: zmienić domyślną gałąź na produkcyjną
albo wgrać kopię `wdrozenie.yml` również na `main` (sam plik na `main` nic nie wdraża —
workflow reaguje wyłącznie na push do gałęzi produkcyjnej).

