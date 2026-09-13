# -*- coding: utf-8 -*-
"""Parduotuvės puslapio vertimo žemėlapis (PL → LT).

Šaltinis: templates/pl-sklep.html. Raktas — lenkiškas tekstas tiksliai taip, kaip jis
yra šablone (tarpai suspausti į vieną); reikšmė — lietuviškas vertimas. Ko čia nėra,
generatorius išvardija kaip „neišversta“, todėl atnaujinus lenkišką puslapį iš karto
matyti, kas pasikeitė.
"""

TEXTS = {
    # Navigacija ir poraštė
    "33BOTS": "33BOTS",
    "Realizacje": "Realizacijos",
    "Wynajem": "Nuoma",
    "Wynajem na eventy": "Nuoma renginiams",
    "Wdrożenia": "Diegimai",
    "Sklep": "Parduotuvė",
    "Oferta": "Paslaugos",
    "Blog": "Blogas",
    "Strona główna": "Pradžia",
    "Instagram": "Instagram",
    "LinkedIn": "LinkedIn",
    "TikTok": "TikTok",
    "© 2026 33bots. Wszelkie prawa zastrzeżone.": "© 2026 33bots. Visos teisės saugomos.",
    "Używamy plików cookie do celów analitycznych.": "Naudojame slapukus analitikos tikslais.",
    "Rozumiem": "Supratau",
    "Roboty humanoidalne · wynajem, wdrożenia, sprzedaż":
        "Humanoidiniai robotai · nuoma, diegimai, pardavimas",

    # Antraštė
    "Sklep — kup robota humanoidalnego Unitree G1 lub robota-psa | 33bots":
        "Parduotuvė — humanoidinis robotas Unitree G1 ir robotas šuo | 33bots",
    "Sprzedaż robotów · sprowadzamy na zamówienie":
        "Robotų pardavimas · užsakome gamintojo",
    "Kup własnego robota.": "Įsigykite savo robotą.",
    "My zajmiemy się resztą.": "Visa kita — mūsų rūpestis.",
    "Zamawiasz u nas, my sprowadzamy robota prosto od producenta, przechodzimy przez odprawę celną i dostarczamy go pod Twój adres.":
        "Užsakote pas mus, o mes parvežame robotą tiesiai iš gamintojo, sutvarkome muitinės formalumus ir pristatome nurodytu adresu.",
    "Uruchomienie i szkolenie wliczone — nie zostajesz sam z instrukcją po chińsku.":
        "Paleidimas ir mokymai įskaičiuoti — neliekate vienas su instrukcija kinų kalba.",
    "~30 dni": "~30 dienų",
    "od zamówienia do dostawy": "nuo užsakymo iki pristatymo",
    "0 zł": "0 €",
    "za odprawę i transport": "muitinei ir transportui",
    "Zobacz roboty": "Žiūrėti robotus",
    "Jak wygląda zakup ↓": "Kaip vyksta pirkimas ↓",

    # Robotai
    "Roboty": "Robotai",
    "Co możesz u nas zamówić": "Ką galite pas mus užsisakyti",
    "Każdy robot sprowadzamy na konkretne zamówienie, dlatego cenę podajemy po rozmowie — zależy od modelu, wersji wyposażenia i aktualnego kursu.":
        "Kiekvieną robotą parvežame pagal konkretų užsakymą, todėl kainą pateikiame po pokalbio — ji priklauso nuo modelio, komplektacijos ir esamo valiutų kurso.",
    "Najczęściej wybierany": "Dažniausiai renkamas",
    "Unitree G1": "Unitree G1",
    "Unitree G1 — robot humanoidalny": "Unitree G1 — humanoidinis robotas",
    "Robot humanoidalny": "Humanoidinis robotas",
    "Dwunożny humanoid, który chodzi, gestykuluje, tańczy i pozuje do zdjęć. Ten sam model, którym obsługujemy eventy w całej Polsce.":
        "Dvikojis humanoidas, kuris vaikšto, gestikuliuoja, šoka ir pozuoja nuotraukoms. Tas pats modelis, kurį vežame į renginius visoje Lietuvoje.",
    "Wzrost": "Ūgis",
    "132 cm": "132 cm",
    "Waga": "Svoris",
    "35 kg": "35 kg",
    "Stopnie swobody": "Laisvės laipsniai",
    "Prędkość": "Greitis",
    "do 2 m/s": "iki 2 m/s",
    "Wycena indywidualna": "Individuali kaina",
    "Cena zależy od wersji i kursu — podajemy ją w ciągu doby.":
        "Kaina priklauso nuo versijos ir kurso — pateikiame ją per parą.",
    "Zapytaj o cenę": "Klauskite kainos",
    "Zapytaj o cenę →": "Klauskite kainos →",
    "Robot-pies": "Robotas šuo",
    "Robot-pies — robot czworonożny": "Robotas šuo — keturkojis robotas",
    "Robot czworonożny": "Keturkojis robotas",
    "Zwinny, szybki i odporny na trudniejszy teren. Świetnie sprawdza się w plenerze i tam, gdzie humanoid miałby za mało miejsca.":
        "Vikrus, greitas ir atsparus sudėtingesniam paviršiui. Puikiai tinka lauke ir ten, kur humanoidui pritrūktų vietos.",
    "Konstrukcja": "Konstrukcija",
    "czworonożna": "keturkojė",
    "Teren": "Paviršius",
    "także nierówny": "tinka ir nelygus",
    "Branding": "Ženklinimas",
    "możliwy": "galimas",
    "Sterowanie": "Valdymas",
    "pilot lub scenariusz": "pultas arba scenarijus",
    "Dobierzemy model do tego, jak chcesz go używać.":
        "Modelį parinksime pagal tai, kaip ketinate jį naudoti.",
    "Polecane": "Rekomenduojame",
    "Robot z wdrożeniem": "Robotas su diegimu",
    "Robot z wdrożeniem — sprzęt, oprogramowanie, szkolenie":
        "Robotas su diegimu — įranga, programinė įranga, mokymai",
    "Sprzęt + oprogramowanie + szkolenie": "Įranga + programinė įranga + mokymai",
    "Sam robot to dopiero początek. W tym pakiecie dostajesz go gotowego do pracy: mówiącego po polsku, znającego Twoją ofertę, z przeszkolonym zespołem.":
        "Vien robotas — tik pradžia. Šiame pakete gaunate jį paruoštą darbui: kalbantį lietuviškai, žinantį jūsų pasiūlymą, su apmokyta komanda.",
    "Robot wraz z dostawą i uruchomieniem": "Robotas su pristatymu ir paleidimu",
    "Oprogramowanie do mowy po polsku": "Programinė įranga kalbai lietuviškai",
    "Baza wiedzy o Twojej firmie": "Žinių bazė apie jūsų įmonę",
    "Szkolenie zespołu z obsługi": "Komandos mokymai",
    "Wsparcie po starcie": "Pagalba po paleidimo",
    "Zakres ustalamy pod Twoje zastosowanie.": "Apimtį deriname pagal jūsų panaudojimą.",
    "Co dokładnie obejmuje wdrożenie →": "Kas tiksliai įeina į diegimą →",

    # Pirkimo eiga
    "Jak wygląda zakup": "Kaip vyksta pirkimas",
    "Cztery kroki, żadnych niespodzianek": "Keturi žingsniai, jokių netikėtumų",
    "Zapytanie i wycena": "Užklausa ir kaina",
    "Piszesz, czego potrzebujesz. Oddzwaniamy, doradzamy model i podajemy konkretną cenę.":
        "Parašote, ko reikia. Susisiekiame, patariame dėl modelio ir pateikiame konkrečią kainą.",
    "Zamówienie i faktura": "Užsakymas ir sąskaita",
    "Potwierdzasz zamówienie, wystawiamy fakturę proforma. Po jej opłaceniu zamawiamy sprzęt.":
        "Patvirtinate užsakymą, išrašome išankstinę sąskaitą. Ją apmokėjus užsakome įrangą.",
    "Sprowadzenie": "Parvežimas",
    "Zamawiamy u producenta i przeprowadzamy przez odprawę celną. Zwykle zajmuje to około miesiąca.":
        "Užsakome pas gamintoją ir pervedame per muitinę. Paprastai tai užtrunka apie mėnesį.",
    "Dostawa i uruchomienie": "Pristatymas ir paleidimas",
    "Przywozimy robota, uruchamiamy na miejscu i pokazujemy, jak go obsługiwać.":
        "Atvežame robotą, paleidžiame vietoje ir parodome, kaip jį valdyti.",
    "Odprawa po naszej stronie": "Muitinė — mūsų rūpestis",
    "Cło, transport i formalności importowe bierzemy na siebie. Cena w wycenie jest ceną końcową.":
        "Muitą, transportą ir importo formalumus pasiimame sau. Pasiūlyme nurodyta kaina yra galutinė.",
    "Gwarancja producenta": "Gamintojo garantija",
    "Robot objęty jest gwarancją, a jej obsługą zajmujemy się my — nie piszesz do Chin.":
        "Robotui taikoma garantija, o jos administravimu rūpinamės mes — jums nereikia rašyti į Kiniją.",
    "Faktura VAT": "PVM sąskaita faktūra",
    "Sprzedaż na firmę z fakturą, więc zakup możesz rozliczyć w kosztach.":
        "Parduodame įmonėms su sąskaita faktūra, todėl pirkimą galite įtraukti į sąnaudas.",

    # DUK
    "Zanim zamówisz": "Prieš užsakant",
    "Dlaczego czekam około miesiąca?": "Kodėl laukiama apie mėnesį?",
    "Roboty sprowadzamy na konkretne zamówienie prosto od producenta — nie trzymamy ich na magazynie, bo to sprzęt wysokiej wartości w wielu wariantach. Na ten czas składa się produkcja, transport i odprawa celna. Termin potwierdzamy przy zamówieniu i informujemy o postępach.":
        "Robotus parvežame pagal konkretų užsakymą tiesiai iš gamintojo — sandėlyje jų nelaikome, nes tai didelės vertės įranga su daug variantų. Į tą laiką įeina gamyba, transportas ir muitinės procedūros. Terminą patvirtiname užsakant ir informuojame apie eigą.",
    "Dlaczego nie ma cen na stronie?": "Kodėl puslapyje nėra kainų?",
    "Cena zależy od modelu, wersji wyposażenia, zakresu oprogramowania i aktualnego kursu walut. Podawanie jednej kwoty byłoby mylące, dlatego wyceniamy każde zamówienie osobno — zwykle w ciągu doby od rozmowy, bez zobowiązań z Twojej strony.":
        "Kaina priklauso nuo modelio, komplektacijos, programinės įrangos apimties ir valiutų kurso. Nurodyti vieną sumą būtų klaidinga, todėl kiekvieną užsakymą vertiname atskirai — paprastai per parą po pokalbio ir be jokių įsipareigojimų iš jūsų pusės.",
    "Czy muszę płacić całość z góry?": "Ar reikia sumokėti visą sumą iš karto?",
    "Warunki płatności ustalamy przy zamówieniu i zapisujemy w umowie. Zamówienie u producenta uruchamiamy po opłaceniu faktury proforma — dopóki tego nie zrobisz, nic się nie dzieje i nic Cię nie wiąże.":
        "Mokėjimo sąlygas suderiname užsakant ir įrašome į sutartį. Užsakymą gamintojui pateikiame apmokėjus išankstinę sąskaitą — kol to nepadarysite, niekas nevyksta ir niekas jūsų nesaisto.",
    "Czy robot będzie mówił po polsku?": "Ar robotas kalbės lietuviškai?",
    "Sam robot w wersji fabrycznej nie jest przygotowany pod polską mowę ani pod Twoją firmę. Odpowiada za to nasze oprogramowanie, które wchodzi w skład pakietu z wdrożeniem — robot mówi wtedy po polsku i zna Twoją ofertę. Możesz je dokupić także później.":
        "Gamyklinis robotas nėra paruoštas nei lietuvių kalbai, nei jūsų įmonei. Už tai atsakinga mūsų programinė įranga, kuri įeina į paketą su diegimu — tada robotas kalba lietuviškai ir žino jūsų pasiūlymą. Ją galima įsigyti ir vėliau.",
    "Może najpierw wypożyczę i sprawdzę?": "Gal pirma išsinuomoti ir pažiūrėti?",
    "To rozsądna kolejność i często ją doradzamy. Wynajmij robota na jedno wydarzenie, zobacz na własne oczy, jak reagują ludzie, a dopiero potem zdecyduj o zakupie. Warunki wynajmu znajdziesz na stronie głównej.":
        "Tai protinga eilės tvarka ir dažnai ją patariame. Išsinuomokite robotą vienam renginiui, savo akimis pamatykite, kaip reaguoja žmonės, ir tik tada spręskite dėl pirkimo. Nuomos sąlygas rasite pagrindiniame puslapyje.",

    # Forma
    "Zamów robota": "Užsakyti robotą",
    "Wycenę podajemy zwykle w ciągu doby.": "Kainą paprastai pateikiame per parą.",
    "i termin dostawy.": "ir pristatymo terminą.",
    "Imię i nazwisko *": "Vardas ir pavardė *",
    "E-mail *": "El. paštas *",
    "Telefon": "Telefonas",
    "— opcjonalnie": "— nebūtina",
    "Firma": "Įmonė",
    "Czym jesteś zainteresowany? *": "Kas jus domina? *",
    "Jeszcze nie wiem — proszę o doradztwo": "Dar nežinau — prašau patarimo",
    "Do czego potrzebujesz robota?": "Kam jums reikia roboto?",
    "Wyślij zapytanie": "Siųsti užklausą",
    "Wysłanie formularza niczego nie zamawia ani do niczego nie zobowiązuje — to początek rozmowy i podstawa do wyceny.":
        "Formos išsiuntimas nieko neužsako ir niekuo neįpareigoja — tai pokalbio pradžia ir pagrindas kainai apskaičiuoti.",
}

ATTRS = {
    "Robot humanoidalny Unitree G1 — ujęcie studyjne":
        "Humanoidinis robotas Unitree G1 — studijinis kadras",
    "Robot-pies w firmowej koszulce klienta podczas akcji promocyjnej":
        "Robotas šuo su kliento įmonės marškinėliais akcijos metu",
    "Gdzie ma pracować, jakie zadania ma wykonywać, czy potrzebujesz oprogramowania do mowy.":
        "Kur dirbs, kokias užduotis atliks, ar reikia kalbos programinės įrangos.",
    # Formos laukų reikšmės — jos keliauja į užklausos laišką, todėl irgi lietuviškos
    "Unitree G1": "Unitree G1",
    "Robot-pies": "Robotas šuo",
    "Robot z wdrożeniem": "Robotas su diegimu",
    "Jeszcze nie wiem": "Dar nežinau",
    "Jan Kowalski": "Jonas Jonaitis",
    "Nazwa firmy": "Įmonės pavadinimas",
    "kontakt@firma.pl": "info@imone.lt",
    "Ścieżka nawigacji": "Naršymo kelias",
    "Otwórz menu": "Atidaryti meniu",
    "Zamknij menu": "Uždaryti meniu",
}

JS_TEXTS = {
    "To pole jest wymagane": "Šis laukas privalomas",
    "Nieprawidłowy format": "Neteisingas formatas",
    "Sprawdź to pole": "Patikrinkite šį lauką",
    "Zapytanie wysłane": "Užklausa išsiųsta",
    "Wycenę wyślemy na": "Kainą atsiųsime adresu",
    "zwykle w ciągu doby": "paprastai per parą",
    "Wysyłanie...": "Siunčiama...",
    "Wysyłanie…": "Siunčiama…",
    "SKLEP — zapytanie o zakup robota": "PARDUOTUVĖ — užklausa dėl roboto pirkimo",
    "Spróbuj ponownie": "Bandykite dar kartą",
    "Coś poszło nie tak": "Kažkas nepavyko",
    "Formularz — błąd wysyłki": "Forma — siuntimo klaida",
    "Zapytanie o robota": "Užklausa dėl roboto",
    "Zapytanie ze sklepu": "Užklausa iš parduotuvės",
}
