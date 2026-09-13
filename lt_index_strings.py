# -*- coding: utf-8 -*-
"""Lietuviški pagrindinio puslapio tekstai — vertimo žemėlapis iš lenkiškos versijos.

Šaltinis: templates/pl-index.html (33bots.pl perdaryto pagrindinio puslapio kopija).
Raktas — lenkiškas tekstas, reikšmė — lietuviškas atitikmuo.
"""

# ── KAINOS LIETUVOS RINKAI ───────────────────────────────────────────────────
# Kainas nustatė įmonė; jos nėra perskaičiuotos iš lenkiškų.
# Pakeitus reikšmes ir paleidus build_all.py, kaina atsinaujina visame puslapyje:
# hero bloke, kainų kortelėje, DUK atsakyme ir struktūrizuotuose duomenyse.
PRICE_FROM = "2 100"          # € be PVM — pradinė kaina už visą realizacijos dieną
PRICE_FROM_PLAIN = "2100"     # ta pati kaina be tarpo (meta, JSON-LD, JS)
PRICE_DOG = "690"             # € be PVM už roboto šunį per dieną
DISCOUNT = "15%"              # nuolaida dviejų ir daugiau dienų realizacijoms

# Transportas NĖRA įskaičiuotas — atvykimą vertiname pagal renginio vietą,
# kaip ir 33bots.pl nuo 2026-08-14. Jokiame puslapyje nerašome „atvykimas pagal vietą".

TEXTS = {
    # ── Navigacija ──────────────────────────────────────────────────────────
    "Realizacje": "Realizacijos",
    "Możliwości": "Galimybės",
    "Cennik": "Kainos",
    "Proces": "Procesas",
    "Oferta": "Paslaugos",
    "Darmowa wycena": "Nemokama sąmata",
    "Darmowa wycena →": "Nemokama sąmata →",

    # ── Hero ────────────────────────────────────────────────────────────────
    "Wynajem robotów humanoidalnych · cała Polska":
        "Humanoidinių robotų nuoma · visa Lietuva",
    "Wynajem robotów humanoidalnych": "Humanoidinių robotų nuoma",
    "na wydarzenia, które": "renginiams, kurie",
    "zapadają w pamięć.": "įsimenami ilgam.",
    "Humanoid Unitree G1 na Twoich targach, konferencji albo gali. Cały dzień pokazu —":
        "Humanoidas Unitree G1 jūsų parodoje, konferencijoje ar gala vakare. Visa pasirodymo diena —",
    "transport, operator i branding w cenie": "operatorius ir ženklinimas kainoje",
    "z certyfikowanym operatorem i Twoim brandingiem":
        "su sertifikuotu operatoriumi ir jūsų ženklinimu",
    "od 5 500 zł": f"nuo {PRICE_FROM} €",
    "za cały dzień · cena wyjściowa": "už visą dieną · pradinė kaina (be PVM)",
    "za cały dzień · zero dopłat": "už visą dieną · pradinė kaina (be PVM)",
    "Odbierz darmową wycenę": "Gaukite nemokamą sąmatą",
    "Zobacz cennik ↓": "Žiūrėti kainas ↓",
    "Zero zaliczki": "Jokio avanso",
    "Faktura po evencie": "Sąskaita po renginio",
    "Darmowy transport": "Atvykimas visoje Lietuvoje",
    "Dojazd w całej Polsce": "Atvykimas visoje Lietuvoje",
    "Wycena w 24 h": "Kaina per 24 val.",
    "Przewiń": "Slinkti",

    # ── Pasitikėjimas ───────────────────────────────────────────────────────
    "Zaufali nam": "Mumis pasitikėjo",
    "Fundacja Perspektywy": "Perspektywy fondas",
    "Widziani w TVP": "Rodyti per TVP",

    # ── Galerija ────────────────────────────────────────────────────────────
    "Co robi na evencie": "Ką jis daro renginyje",
    "Najedź na kadr — pas się zatrzyma, a nagranie ruszy. Kliknij, żeby powiększyć.":
        "Užveskite pelę ant kadro — juosta sustos, o įrašas pajudės. Spustelėkite, kad padidintumėte.",
    "14 zdjęć z prawdziwych realizacji. Bez stocków, bez renderów.":
        "16 nuotraukų iš tikrų realizacijų. Jokių stock nuotraukų, jokių renderių.",
    "Czerwony dywan": "Raudonas kilimas",
    "Wszyscy wyciągają telefony": "Visi traukia telefonus",
    "Taniec · najedź": "Šokis · užveskite",
    "Ulica przystaje": "Gatvė sustoja",
    "Eventy plenerowe": "Lauko renginiai",
    "Robot-pies w brandingu": "Robotas šuo su ženklinimu",
    "Pokazy nocne": "Naktiniai pasirodymai",
    "Women in Tech Summit": "Women in Tech Summit",
    "Goście robią zdjęcia": "Svečiai fotografuoja",
    "Także w deszczu": "Ir per lietų",
    "Logo i kod QR · 0 zł": "Logotipas ir QR kodas · 0 €",
    "Marketing w mieście": "Rinkodara mieste",
    "Pałacowe wnętrza": "Rūmų interjerai",
    "Spotkania firmowe": "Verslo susitikimai",
    "Wśród gości": "Tarp svečių",
    "więcej uwagi niż jakakolwiek inna atrakcja": "daugiau dėmesio nei bet kuri kita pramoga",
    "0 zł": "0 €",
    "za branding — Twoje logo i kod QR na robocie":
        "už ženklinimą — jūsų logotipas ir QR kodas ant roboto",
    "Teleexpress TVP": "Teleexpress TVP",
    "nasz robot w ogólnopolskiej telewizji": "mūsų robotas nacionalinėje televizijoje",
    "Wszystkie realizacje wideo": "Visi vaizdo įrašai",

    # ── Galimybės ───────────────────────────────────────────────────────────
    "To nie atrakcja na kwadrans.": "Tai ne pramoga ketvirčiui valandos.",
    "To temat rozmów na tygodnie.": "Tai pokalbių tema savaitėms.",
    "Przed wydarzeniem robot dostaje głos, charakter i wiedzę o tym, co się u Ciebie dzieje.":
        "Prieš renginį robotas gauna balsą, charakterį ir žinias apie tai, kas vyksta pas jus.",
    "Efekt: sala cichnie, telefony idą w górę, a goście opowiadają o tym jeszcze długo po powrocie do domu.":
        "Rezultatas: salė nutyla, telefonai kyla į viršų, o svečiai apie tai pasakoja dar ilgai grįžę namo.",
    "Mówi i rozmawia po polsku": "Kalba ir bendrauja lietuviškai",
    "Wita gości, odpowiada na pytania, żartuje i zapowiada punkty programu — naturalną mową, bez sztucznego, robotycznego brzmienia. Ludzie zagadują go z ciekawości, a zostają na dłuższą rozmowę.":
        "Pasitinka svečius, atsako į klausimus, juokauja ir pristato programos punktus — natūralia kalba, be dirbtinio robotiško skambesio. Žmonės užkalbina jį iš smalsumo, o lieka ilgesniam pokalbiui.",
    "Zatańczysz ze mną?": "Pašoksi su manimi?",
    "Chętnie. Mam 23 stopnie swobody i zero wstydu — prowadzisz czy prowadzę?":
        "Mielai. Turiu 23 laisvės laipsnius ir jokio drovumo — tu vedi ar aš?",
    "Dlaczego to robi wrażenie:": "Kodėl tai daro įspūdį:",
    "nikt nie nagrywa eksponatu. Wszyscy nagrywają kogoś, kto właśnie im odpowiedział — i wysyłają to znajomym jeszcze tego samego wieczoru.":
        "niekas nefilmuoja eksponato. Visi filmuoja tą, kuris ką tik jiems atsakė — ir siunčia tai draugams dar tą patį vakarą.",
    "Osobowość i baza wiedzy pod Ciebie": "Charakteris ir žinių bazė pagal jus",
    "Przed eventem ustalamy charakter robota i wgrywamy mu wiedzę o tym, co się u Was dzieje: czyj to jubileusz, kto występuje na scenie, jakie hasło przewodnie ma wydarzenie i co warto wypomnieć z przymrużeniem oka.":
        "Prieš renginį suderiname roboto charakterį ir įkeliame jam žinias apie tai, kas vyksta pas jus: kieno tai jubiliejus, kas pasirodo scenoje, koks renginio šūkis ir ką verta paminėti su humoru.",
    "Elegancki konferansjer": "Elegantiškas vedėjas",
    "Żartowniś": "Juokdarys",
    "Ekspert techniczny": "Technikos ekspertas",
    "Wie, co dzieje się na scenie": "Žino, kas vyksta scenoje",
    "Zna Wasze wewnętrzne żarty": "Žino jūsų vidinius juokus",
    "największy szum robi moment, w którym robot mówi coś, czego nie miał prawa wiedzieć. Wtedy sala głośnieje, a ludzie wołają znajomych.":
        "didžiausią įspūdį palieka akimirka, kai robotas pasako tai, ko neturėjo teisės žinoti. Tada salė sugaudžia, o žmonės šaukia draugus.",
    "Pozuje do zdjęć": "Pozuoja nuotraukoms",
    "Ustawia się do selfie, macha do kamery, pozuje z gośćmi. Kolejka tworzy się sama.":
        "Pozuoja asmenukėms, mojuoja kamerai, fotografuojasi su svečiais. Eilė susidaro savaime.",
    "Zdjęcia krążą po social mediach jeszcze w trakcie imprezy.":
        "Nuotraukos plinta socialiniuose tinkluose dar renginio metu.",
    "Tańczy do muzyki": "Šoka pagal muziką",
    "Pełne choreografie zgrane z rytmem — od spokojnych po widowiskowe.":
        "Pilnos choreografijos pagal ritmą — nuo ramių iki įspūdingų.",
    "Moment, w którym cała sala wyciąga telefony naraz.":
        "Akimirka, kai visa salė vienu metu traukia telefonus.",
    "Scenariusz na Twój dzień": "Scenarijus jūsų dienai",
    "Powitanie gości, zapowiedź prelegenta, odliczanie do północy, wręczenie nagrody.":
        "Svečių pasitikimas, pranešėjo pristatymas, atgalinis skaičiavimas iki vidurnakčio, apdovanojimo įteikimas.",
    "Zaskoczenie w idealnym momencie, a nie atrakcja stojąca z boku.":
        "Netikėtumas tinkamiausiu momentu, o ne pramoga, stovinti nuošalyje.",
    "Nosi Twoją markę": "Nešioja jūsų prekės ženklą",
    "Logo i kod QR na klatce piersiowej, strój dobrany do charakteru wydarzenia.":
        "Logotipas ir QR kodas ant krūtinės, apranga pagal renginio pobūdį.",
    "Twoje logo trafia na setki zdjęć zrobionych przez gości. Bez dopłat.":
        "Jūsų logotipas patenka į šimtus svečių darytų nuotraukų. Be priemokų.",
    "Wystarczy jedna rozmowa — mówisz, jakie wrażenie chcesz zrobić, a my przygotowujemy głos, charakter i scenariusz.":
        "Užtenka vieno pokalbio — pasakote, kokį įspūdį norite padaryti, o mes paruošiame balsą, charakterį ir scenarijų.",
    "Wszystko w cenie wynajmu.": "Viskas nuomos kainoje.",
    "Omów swój scenariusz": "Aptarkime jūsų scenarijų",

    # ── Kainos ──────────────────────────────────────────────────────────────
    "Najlepsze ceny w Polsce": "Skaidrios kainos visoje Lietuvoje",
    "Realnie taniej za tę jakość po prostu się nie da. Wynajmiesz robota na kilka godzin, cały dzień albo na całe targi —":
        "Robotą galite išsinuomoti kelioms valandoms, visai dienai arba visai parodai —",
    "a to, co usłyszysz w wycenie, zobaczysz na fakturze":
        "o tai, ką išgirsite pasiūlyme, pamatysite sąskaitoje",
    "Krócej niż dzień": "Trumpiau nei diena",
    "Kilka godzin": "Kelios valandos",
    "Efektowne wejście, powitanie gości albo kulminacyjny moment wieczoru.":
        "Įspūdingas įėjimas, svečių pasitikimas arba vakaro kulminacija.",
    "Wycena indywidualna — zawsze taniej niż pełny dzień.":
        "Individuali kaina — visada pigiau nei visa diena.",
    "Najczęściej wybierane": "Dažniausiai renkamasi",
    "Cały dzień": "Visa diena",
    "Pełna obsługa od montażu po finał.": "Pilna paslauga nuo paruošimo iki finalo.",
    "Dwa dni i więcej": "Dvi dienos ir daugiau",
    "Wielodniowo": "Kelios dienos",
    "Targi, festiwale, roadshow.": "Parodos, festivaliai, roadshow.",
    "Rabat naliczamy na każdy dzień realizacji.":
        "Nuolaidą taikome kiekvienai realizacijos dienai.",
    "Wszystko w cenie": "Viskas kainoje",
    "Cena wyjściowa": "Pradinė kaina",
    "W cenie wyjściowej": "Į pradinę kainą įeina",
    "Scenariusz i konfiguracja": "Scenarijus ir konfigūracija",
    "To standard wynajmu, nie płatny dodatek.": "Tai nuomos standartas, o ne mokamas priedas.",
    "Bez ukrytych kosztów.": "Jokių paslėptų kaštų.",
    "Dojazd wyceniamy według lokalizacji eventu.":
        "Atvykimą įvertiname pagal renginio vietą.",
    "Cena wyjściowa za cały dzień realizacji. Ostateczną kwotę podajemy w wycenie — zależy od lokalizacji i zakresu eventu.":
        "Pradinė kaina už visą realizacijos dieną (be PVM). Galutinę sumą pateikiame pasiūlyme — "
        "ji priklauso nuo renginio vietos ir apimties.",
    "Unitree G1 · cały dzień": "Unitree G1 · visa diena",
    "od": "nuo",
    "zł": "€",
    "Za cały dzień realizacji. Ostateczna cena zależy wyłącznie od lokalizacji eventu.":
        "Už visą realizacijos dieną. Galutinė kaina priklauso tik nuo renginio vietos.",
    "Robot przez cały dzień": "Robotas visą dieną",
    "Certyfikowany operator": "Sertifikuotas operatorius",
    "Transport w całej Polsce": "Atvykimas visoje Lietuvoje",
    "Branding: logo i kod QR": "Ženklinimas: logotipas ir QR kodas",
    "Choreografie i interakcje": "Choreografijos ir bendravimas",
    "Ubezpieczenie OC": "Civilinės atsakomybės draudimas",
    "Cena zawiera absolutnie wszystko.": "Aiškios sąlygos nuo pat pradžių.",
    "ZERO dopłat.": "Jokių paslėptų kaštų.",
    "Opcja dodatkowa": "Papildoma galimybė",
    "Robot-pies": "Robotas šuo",
    "Duet nie do pobicia: humanoid robi show, pies kradnie serca gości. W Twoim brandingu.":
        "Nenugalimas duetas: humanoidas daro šou, šuo pavagia svečių širdis. Su jūsų ženklinimu.",
    "za dzień": "už dieną",
    "Dodaj do wyceny →": "Pridėti į pasiūlymą →",
    "Rabat długoterminowy": "Nuolaida ilgesnėms realizacijoms",
    "na": "kiekvienai",
    "każdy dzień": "dienai",
    "przy realizacjach dwudniowych i dłuższych. Targi, festiwale, roadshow.":
        "dviejų dienų ir ilgesnėms realizacijoms. Parodos, festivaliai, roadshow.",

    # ── Procesas ────────────────────────────────────────────────────────────
    "Jak działamy": "Kaip dirbame",
    "Bezstresowo od pierwszego telefonu": "Be streso nuo pirmo skambučio",
    "Rezerwujesz termin za darmo. Płacisz dopiero po udanym evencie. Całe ryzyko bierzemy na siebie.":
        "Datą rezervuojate nemokamai. Mokate tik po pavykusio renginio. Visą riziką prisiimame mes.",
    "Szybki kontakt": "Greitas kontaktas",
    "Zostawiasz kontakt. Dwie minuty roboty.": "Paliekate kontaktus. Dvi minutės darbo.",
    "Telefon i wycena": "Skambutis ir kaina",
    "Oddzwaniamy i podajemy konkretną kwotę — zwykle tego samego dnia.":
        "Perskambiname ir pasakome konkrečią sumą — dažniausiai tą pačią dieną.",
    "Prosta umowa": "Paprasta sutartis",
    "Bezpłatna rezerwacja, zero zaliczki.": "Nemokama rezervacija, jokio avanso.",
    "Możliwy dłuższy termin płatności.": "Galimas ilgesnis mokėjimo terminas.",
    "My pracujemy, Ty odpoczywasz i zajmujesz się gośćmi.":
        "Mes dirbame, jūs ilsitės ir rūpinatės svečiais.",
    "Najpierw efekt, potem płatność. Nie odwrotnie.":
        "Pirmiausia rezultatas, paskui mokėjimas. Ne atvirkščiai.",

    # ── Atsiliepimai ────────────────────────────────────────────────────────
    "„Efekt przerósł nasze najśmielsze oczekiwania. Zainteresowanie było ogromne przez cały czas trwania wydarzenia.\"":
        "„Rezultatas pranoko drąsiausius lūkesčius. Susidomėjimas buvo milžiniškas visą renginio laiką.“",
    "Karolina M. · marketing, branża IT": "Karolina M. · rinkodara, IT sektorius",
    "„Jedna z najlepszych decyzji organizacyjnych. Reakcje uczestników to dla nas najlepsza recenzja.\"":
        "„Vienas geriausių organizacinių sprendimų. Dalyvių reakcijos mums yra geriausias įvertinimas.“",
    "Piotr Z. · gala firmowa": "Piotr Z. · įmonės gala vakaras",
    "„Niesamowite zasięgi w social mediach. Tego rodzaju zainteresowania nie da się po prostu kupić.\"":
        "„Neįtikėtini pasiekiamumo skaičiai socialiniuose tinkluose. Tokio susidomėjimo tiesiog nenusipirksi.“",
    "Magdalena T. · targi technologiczne": "Magdalena T. · technologijų paroda",

    # ── DUK ─────────────────────────────────────────────────────────────────
    "Zanim zapytasz": "Prieš paklausiant",
    "Ile dokładnie kosztuje wynajem?": "Kiek tiksliai kainuoja nuoma?",
    "Od 5500 zł za cały dzień realizacji — to cena wyjściowa, a ostateczna kwota zależy od lokalizacji i zakresu eventu; podajemy ją w wycenie. W cenie wyjściowej: certyfikowany operator, branding, przygotowanie scenariusza i ubezpieczenie OC — dojazd wyceniamy według lokalizacji. Robota wynajmiesz też na krótszy pokaz, np. kilka godzin podczas przerwy konferencyjnej — wtedy wyceniamy indywidualnie i zawsze taniej niż pełny dzień. Przy realizacjach 2-dniowych i dłuższych obowiązuje 15% zniżki na każdy dzień. Robot-pies to dodatkowe 1900 zł za dzień.":
        f"Nuo {PRICE_FROM} € be PVM už visą realizacijos dieną — tai pradinė kaina, o galutinė suma "
        f"priklauso nuo renginio vietos ir apimties; ją pateikiame pasiūlyme. Į pradinę kainą įeina "
        f"sertifikuotas operatorius, ženklinimas, scenarijaus paruošimas ir civilinės atsakomybės "
        f"draudimas — atvykimą įvertiname pagal vietą. Robotą galima išsinuomoti ir trumpesniam "
        f"pasirodymui, pvz. kelioms valandoms per konferencijos pertrauką — tada kainą skaičiuojame "
        f"individualiai ir visada pigiau nei visa diena. Dviejų dienų ir ilgesnėms realizacijoms "
        f"taikoma {DISCOUNT} nuolaida kiekvienai dienai. Roboto šuo — papildomai {PRICE_DOG} € už dieną.",
    "Od 5500 zł za cały dzień realizacji — ostateczna kwota zależy wyłącznie od lokalizacji eventu. Robota wynajmiesz też na krótszy pokaz, np. kilka godzin podczas przerwy konferencyjnej — wtedy wyceniamy indywidualnie i zawsze taniej niż pełny dzień. Przy realizacjach 2-dniowych i dłuższych obowiązuje 15% zniżki na każdy dzień. W cenie transport, operator, branding i ubezpieczenie; robot-pies to dodatkowe 1900 zł za dzień.":
        f"Nuo {PRICE_FROM} € už visą realizacijos dieną — galutinė suma priklauso tik nuo renginio vietos. "
        f"Robotą galima išsinuomoti ir trumpesniam pasirodymui, pvz. kelioms valandoms per konferencijos "
        f"pertrauką — tada kainą skaičiuojame individualiai ir visada pigiau nei visa diena. Dviejų dienų ir "
        f"ilgesnėms realizacijoms taikoma {DISCOUNT} nuolaida kiekvienai dienai. Į kainą įeina transportas, "
        f"operatorius, ženklinimas ir draudimas; roboto šuo — papildomai {PRICE_DOG} € už dieną.",
    "Czy robot mówi i rozmawia z gośćmi?": "Ar robotas kalba ir bendrauja su svečiais?",
    "Tak. Robot mówi po polsku naturalną syntezą mowy — wita gości, odpowiada na pytania i zapowiada punkty programu. Przed wydarzeniem ustalamy jego charakter oraz wgrywamy wiedzę o Twojej firmie: ofertę, nazwy produktów, najczęstsze pytania klientów i agendę eventu. Konfiguracja jest wliczona w cenę wynajmu.":
        "Taip. Robotas kalba lietuviškai natūralia kalbos sinteze — pasitinka svečius, atsako į klausimus ir "
        "pristato programos punktus. Prieš renginį suderiname jo charakterį ir įkeliame žinias apie jūsų įmonę: "
        "paslaugas, produktų pavadinimus, dažniausius klientų klausimus ir renginio darbotvarkę. Konfigūracija "
        "įskaičiuota į nuomos kainą.",
    "Czy muszę wpłacać zaliczkę?": "Ar reikia mokėti avansą?",
    "Nie. Rezerwacja terminu jest bezpłatna i bez zaliczki. Fakturę wystawiamy dopiero po zakończonym wydarzeniu, a w razie potrzeby ustalimy dłuższy termin płatności.":
        "Ne. Datos rezervacija nemokama ir be avanso. Sąskaitą išrašome tik po įvykusio renginio, o prireikus "
        "suderiname ilgesnį mokėjimo terminą.",
    "Czy muszę umieć sterować robotem?": "Ar reikia mokėti valdyti robotą?",
    "Nie. Przez cały event obecny jest nasz certyfikowany operator — odpowiada za konfigurację, obsługę i bezpieczeństwo pokazu.":
        "Ne. Visą renginį dalyvauja mūsų sertifikuotas operatorius — jis atsako už konfigūraciją, valdymą ir "
        "pasirodymo saugumą.",
    "Czy robot jest bezpieczny dla gości?": "Ar robotas saugus svečiams?",
    "Tak. LiDAR i wizja komputerowa pozwalają omijać ludzi i przeszkody w czasie rzeczywistym, nad pokazem czuwa operator, a realizacja objęta jest ubezpieczeniem OC.":
        "Taip. LiDAR ir kompiuterinė rega leidžia realiu laiku apeiti žmones ir kliūtis, pasirodymą prižiūri "
        "operatorius, o veiklai taikoma civilinės atsakomybės draudimo apsauga.",
    "Dojeżdżacie do mojego miasta?": "Ar atvažiuojate į mano miestą?",
    "Tak — dojeżdżamy do każdego miasta w Polsce, od Szczecina po Rzeszów, od Gdańska po Karpacz. Koszt dojazdu ustalamy przy wycenie, zależnie od lokalizacji eventu.":
        "Taip — atvažiuojame į kiekvieną Lietuvos miestą, nuo Klaipėdos iki Visagino, nuo Palangos iki "
        "Druskininkų. Atvykimo kainą suderiname rengiant pasiūlymą, priklausomai nuo renginio vietos.",
    "Tak — do każdego miasta w Polsce, bez dopłat i bez limitu kilometrów. Od Szczecina po Rzeszów, od Gdańska po Karpacz.":
        "Taip — į kiekvieną Lietuvos miestą, be priemokų ir pagal renginio vietą. Nuo Klaipėdos iki Visagino, "
        "nuo Palangos iki Druskininkų.",

    # ── Kontaktai ───────────────────────────────────────────────────────────
    "Sprawdź, czy Twój": "Patikrinkite, ar jūsų",
    "termin jest wolny.": "data laisva.",
    "Zostaw kontakt — oddzwonimy i podamy konkretną kwotę. Bez zobowiązań, bez zaliczki.":
        "Palikite kontaktus — perskambinsime ir pasakysime konkrečią sumą. Jokių įsipareigojimų, jokio avanso.",
    "✓ Odpowiedź w 24 h": "✓ Atsakymas per 24 val.",
    "✓ Zero zaliczki": "✓ Jokio avanso",
    "✓ Cała Polska": "✓ Visa Lietuva",
    "01 — Dane kontaktowe": "01 — Kontaktiniai duomenys",
    "02 — Twój event": "02 — Jūsų renginys",
    "Imię i nazwisko *": "Vardas ir pavardė *",
    "Firma": "Įmonė",
    "E-mail *": "El. paštas *",
    "Telefon": "Telefonas",
    "Dalej — opowiedz o evencie": "Toliau — papasakokite apie renginį",
    "Planowana data eventu": "Planuojama renginio data",
    "Miasto / Miejsce": "Miestas / vieta",
    "Opisz swój event *": "Papasakokite apie renginį *",
    "← Wróć": "← Atgal",
    "Wyślij i odbierz darmową wycenę": "Siųsti ir gauti nemokamą sąmatą",
    "Odpowiadamy w ciągu 24 godzin roboczych.": "Atsakome per 24 darbo valandas.",

    # ── Poraštė ─────────────────────────────────────────────────────────────
    "Targi": "Parodos",
    "Konferencje": "Konferencijos",
    "Blog": "Blogas",
    "Wypożyczenie robota": "Roboto nuoma",
    "Wynajem robota w Twoim mieście ▾": "Roboto nuoma jūsų mieste ▾",
    "© 2026 33bots. Wszelkie prawa zastrzeżone.": "© 2026 33bots. Visos teisės saugomos.",
    "Używamy plików cookie do celów analitycznych.":
        "Naudojame slapukus analizės tikslais.",
    "Rozumiem": "Supratau",
}

# Atributų tekstai (alt, aria-label, placeholder, title)
ATTRS = {
    # Nuotraukų alt tekstai (tie patys kadrai kaip lt_gallery.PHOTOS)
    "Uczestniczki Women in Tech Summit nagrywające robota humanoidalnego telefonami":
        "Women in Tech Summit dalyvės filmuoja humanoidinį robotą telefonais",
    "Robot humanoidalny w cekinowym smokingu na czerwonym dywanie gali":
        "Humanoidinis robotas blizgančiu smokingu ant gala vakaro raudonojo kilimo",
    "Robot humanoidalny na różowym wybiegu Women in Tech Summit przed publicznością":
        "Humanoidinis robotas ant rožinio podiumo Women in Tech Summit renginyje prieš publiką",
    "Robot humanoidalny w koszulce LEX AI na starówce, przechodnie robią zdjęcia":
        "Humanoidinis robotas su LEX AI marškinėliais senamiestyje — praeiviai fotografuoja",
    "Zbliżenie robota humanoidalnego w koronie i cekinowym smokingu":
        "Humanoidinio roboto stambus planas su karūna ir blizgančiu smokingu",
    "Goście gali fotografujący robota humanoidalnego przy ściance sponsorskiej":
        "Gala vakaro svečiai fotografuoja humanoidinį robotą prie rėmėjų sienos",
    "Robot humanoidalny w smokingu we wnętrzu pałacowej sali balowej":
        "Humanoidinis robotas smokingu rūmų pokylių salėje",
    "Robot humanoidalny wśród rozbawionych gości gali z kieliszkami":
        "Humanoidinis robotas tarp linksmų gala vakaro svečių su taurėmis",
    "Robot humanoidalny macha ręką na tarasie nad mariną z jachtami":
        "Humanoidinis robotas mojuoja terasoje virš jachtų prieplaukos",
    "Robot humanoidalny w czerwonej pelerynie podczas nocnego pokazu przy zabytkowej kamienicy":
        "Humanoidinis robotas raudonu apsiaustu naktiniame pasirodyme prie istorinio pastato",
    "Robot humanoidalny LEX AI idący ulicą starówki z teczką w dłoni":
        "Humanoidinis robotas su LEX AI ženklinimu ir portfeliu senamiesčio gatvelėje",
    "Robot humanoidalny w firmowej koszulce na tarasie podczas spotkania biznesowego":
        "Humanoidinis robotas su įmonės marškinėliais terasoje verslo susitikime",
    "Robot-pies w firmowej koszulce klienta podczas akcji promocyjnej salonu samochodowego":
        "Robotas šuo su kliento įmonės marškinėliais akcijoje automobilių salone",
    "Robot humanoidalny w czerwonej koszulce trzymający parasol podczas deszczu":
        "Humanoidinis robotas raudonais marškinėliais per lietų laiko skėtį",
    "Robot humanoidalny Unitree G1 — wynajem na eventy w całej Polsce":
        "Humanoidinis robotas Unitree G1 — nuoma renginiams visoje Lietuvoje",
    # og:image:alt lenkiškame šablone yra be žodžio „całej“ — be šios eilutės
    # pagrindinio puslapio meta duomenyse likdavo lenkiškas tekstas.
    "Robot humanoidalny Unitree G1 — wynajem na eventy w Polsce":
        "Humanoidinis robotas Unitree G1 — nuoma renginiams visoje Lietuvoje",

    # Sąsajos elementai
    "Powiększone zdjęcie": "Padidinta nuotrauka",
    "Poprzednie zdjęcie": "Ankstesnė nuotrauka",
    "Następne zdjęcie": "Kita nuotrauka",
    "Zamknij": "Uždaryti",
    "Otwórz menu": "Atidaryti meniu",
    "Zamknij menu": "Uždaryti meniu",
    "33bots — blog RSS": "33bots — blogo RSS",

    # Formos laukai
    "Jan Kowalski": "Jonas Jonaitis",
    "Nazwa firmy": "Įmonės pavadinimas",
    "kontakt@firma.pl": "info@imone.lt",
    "np. Warszawa, Hala X": "pvz. Vilnius, LITEXPO",
    "Rodzaj eventu (targi, konferencja, gala...), orientacyjna liczba gości, jak długo chcesz mieć robota i cokolwiek jeszcze uważasz za ważne.":
        "Renginio tipas (paroda, konferencija, gala vakaras...), apytikslis svečių skaičius, kiek laiko norite roboto ir viskas, kas jums atrodo svarbu.",
}


# Tekstai, esantys inline JavaScript kode (formos pranešimai, mygtukų būsenos)
JS_TEXTS = {
    "Odezwiemy się na": "Susisieksime adresu",
    "Wiadomość wysłana": "Užklausa išsiųsta",
    "Wysyłanie...": "Siunčiama...",
    "Wysyłanie…": "Siunčiama…",
    "Spróbuj ponownie": "Bandykite dar kartą",
    "To pole jest wymagane": "Šis laukas privalomas",
    "Nieprawidłowy format": "Neteisingas formatas",
    "Sprawdź to pole": "Patikrinkite šį lauką",
    "Coś poszło nie tak": "Kažkas nepavyko",
    "w ciągu 24 godzin roboczych": "per 24 darbo valandas",
    "Formularz kontaktowy": "Kontaktinė forma",
    "Formularz — błąd wysyłki": "Forma — siuntimo klaida",
}

# Papildomi tekstai, kurių nebuvo pirminiame žemėlapyje
TEXTS.update({
    "Realizacja": "Realizacija",
    "TikTok": "TikTok",
})
