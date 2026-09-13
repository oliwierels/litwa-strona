# -*- coding: utf-8 -*-
"""Diegimų puslapio vertimo žemėlapis (PL → LT).

Šaltinis: templates/pl-wdrozenia.html. Veikia taip pat kaip lt_shop_strings:
raktas — lenkiškas tekstas iš šablono, reikšmė — lietuviškas vertimas.
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
    "Wdrożenie robota humanoidalnego w firmie — sprzedaż, mowa, szkolenie | 33bots":
        "Humanoidinio roboto diegimas įmonėje — pardavimas, kalba, mokymai | 33bots",
    "Wdrożenia dla firm": "Diegimai įmonėms",
    "Robot, który zostaje u Ciebie": "Robotas, kuris lieka pas jus",
    "na stałe — i wie, co mówić.": "visam laikui — ir žino, ką sakyti.",
    "Kupujesz robota humanoidalnego, a my bierzemy na siebie całą resztę: dostawę, uruchomienie, oprogramowanie do mowy z wiedzą o Twojej ofercie i szkolenie zespołu.":
        "Jūs įsigyjate humanoidinį robotą, o mes pasiimame visa kita: pristatymą, paleidimą, kalbos programinę įrangą su žiniomis apie jūsų pasiūlymą ir komandos mokymus.",
    "Odbierasz gotowe narzędzie, nie karton z elektroniką.":
        "Gaunate paruoštą įrankį, o ne dėžę su elektronika.",
    "Porozmawiajmy o wdrożeniu": "Pakalbėkime apie diegimą",
    "Porozmawiajmy": "Pakalbėkime",
    "Zobacz sklep": "Žiūrėti parduotuvę",
    "Zobacz realizacje": "Žiūrėti realizacijas",
    "Mówi po polsku": "Kalba lietuviškai",
    "Zna Twoją ofertę": "Žino jūsų pasiūlymą",
    "Szkolenie w cenie": "Mokymai kainoje",
    "Wsparcie po starcie": "Pagalba po paleidimo",

    # Apimtis
    "Zakres wdrożenia": "Diegimo apimtis",
    "Cztery rzeczy, które dostajesz": "Keturi dalykai, kuriuos gaunate",
    "Sam robot to dopiero początek. Bez konfiguracji i przeszkolonej obsługi stoi w kącie — dlatego wdrożenie obejmuje komplet.":
        "Vien robotas — tik pradžia. Be konfigūracijos ir apmokytos komandos jis stovi kampe, todėl diegimas apima visą komplektą.",
    "Robot i uruchomienie": "Robotas ir paleidimas",
    "Sprowadzamy robota, dostarczamy pod wskazany adres i uruchamiamy na miejscu. Sprawdzamy przestrzeń, zasilanie i sieć, po czym przekazujemy sprzęt gotowy do pracy.":
        "Parvežame robotą, pristatome nurodytu adresu ir paleidžiame vietoje. Patikriname erdvę, elektros maitinimą ir tinklą, po to perduodame įrangą, paruoštą darbui.",
    "Bez niespodzianek:": "Jokių netikėtumų:",
    "formalności celne i logistykę bierzemy na siebie. Ty podajesz adres i termin.":
        "muitinės formalumus ir logistiką pasiimame sau. Jūs nurodote adresą ir terminą.",
    "Oprogramowanie do mowy": "Kalbos programinė įranga",
    "Robot mówi po polsku naturalną mową i odpowiada na pytania. Wgrywamy mu wiedzę o Twojej firmie — ofertę, nazwy produktów, najczęstsze pytania klientów — oraz ustalamy charakter, w jakim ma się odzywać.":
        "Robotas kalba lietuviškai natūralia kalba ir atsako į klausimus. Įkeliame jam žinias apie jūsų įmonę — pasiūlymą, produktų pavadinimus, dažniausius klientų klausimus — ir suderiname, kokiu tonu jis turi kalbėti.",
    "To jest sedno wdrożenia:": "Tai yra diegimo esmė:",
    "robot bez wiedzy o Twojej firmie jest ozdobą. Z nią zaczyna realnie obsługiwać ludzi.":
        "robotas be žinių apie jūsų įmonę yra tik dekoracija. Su jomis jis ima realiai aptarnauti žmones.",
    "Przed uruchomieniem wgrywamy mu wiedzę o Waszej firmie: ofertę, nazwy i opisy produktów, najczęstsze pytania klientów, godziny otwarcia, dane kontaktowe. Ustalamy też, jak ma się zachowywać i czego nie powinien mówić. Gdy oferta się zmienia, bazę wiedzy aktualizujemy.":
        "Prieš paleidimą įkeliame jam žinias apie jūsų įmonę: pasiūlymą, produktų pavadinimus ir aprašymus, dažniausius klientų klausimus, darbo laiką, kontaktus. Taip pat suderiname, kaip jis turi elgtis ir ko neturėtų sakyti. Pasikeitus pasiūlymui, žinių bazę atnaujiname.",
    "Szkolenie zespołu": "Komandos mokymai",
    "Uczymy Waszych ludzi obsługi: uruchamiania, prowadzenia pokazu, ładowania, zmiany scenariuszy i zasad bezpieczeństwa w tłumie. Zostawiamy instrukcję napisaną po ludzku.":
        "Išmokome jūsų žmones valdyti robotą: paleisti, vesti pasirodymą, krauti, keisti scenarijus ir laikytis saugos taisyklių minioje. Paliekame žmogiškai parašytą instrukciją.",
    "Po szkoleniu radzicie sobie sami": "Po mokymų susitvarkote patys",
    "— nie musicie nas wzywać za każdym razem, gdy robot ma wyjść do ludzi.":
        "— nereikia mūsų kviesti kaskart, kai robotas turi išeiti pas žmones.",
    "Zostajemy w kontakcie po uruchomieniu: pomagamy przy pytaniach, aktualizujemy bazę wiedzy, gdy zmienia się oferta, i doradzamy przy nowych scenariuszach.":
        "Po paleidimo liekame su jumis: padedame iškilus klausimams, atnaujiname žinių bazę pasikeitus pasiūlymui ir patariame dėl naujų scenarijų.",
    "Zakres i czas wsparcia": "Pagalbos apimtį ir trukmę",
    "ustalamy przy wycenie — zależą od tego, jak intensywnie robot ma pracować.":
        "suderiname rengdami pasiūlymą — jos priklauso nuo to, kaip intensyviai robotas dirbs.",

    # Eiga
    "Jak to przebiega": "Kaip tai vyksta",
    "Od rozmowy do pierwszego dnia pracy": "Nuo pokalbio iki pirmos darbo dienos",
    "Rozmowa": "Pokalbis",
    "Ustalamy, do czego robot ma służyć i gdzie będzie pracował.":
        "Išsiaiškiname, kam robotas skirtas ir kur jis dirbs.",
    "Wycena i umowa": "Kaina ir sutartis",
    "Konkretna kwota z rozpisanym zakresem. Bez pozycji „do ustalenia\".":
        "Konkreti suma su išskaidyta apimtimi. Jokių eilučių „bus suderinta“.",
    "Sprowadzenie robota": "Roboto parvežimas",
    "Zamawiamy sprzęt i zajmujemy się transportem oraz odprawą. Zwykle około miesiąca.":
        "Užsakome įrangą ir pasirūpiname transportu bei muitine. Paprastai apie mėnesį.",
    "Konfiguracja": "Konfigūracija",
    "Mowa, wiedza o firmie, charakter i scenariusze pod Wasze zastosowanie.":
        "Kalba, žinios apie įmonę, charakteris ir scenarijai pagal jūsų poreikį.",
    "Szkolenie i start": "Mokymai ir startas",
    "Uczymy zespół, uruchamiamy robota i zostajemy w kontakcie.":
        "Apmokome komandą, paleidžiame robotą ir liekame su jumis.",

    # Kur veikia
    "Gdzie się sprawdza": "Kur tai veikia",
    "Miejsca, w których robot pracuje codziennie": "Vietos, kuriose robotas dirba kasdien",
    "Recepcja i lobby": "Registratūra ir holas",
    "Wita gości, kieruje do właściwej osoby, skraca oczekiwanie.":
        "Pasitinka svečius, nukreipia pas reikiamą žmogų, sutrumpina laukimą.",
    "Showroom i salon": "Salonas ir showroom",
    "Opowiada o produktach, zatrzymuje przechodniów, zbiera uwagę.":
        "Pasakoja apie produktus, sustabdo praeivius, patraukia dėmesį.",
    "Galeria handlowa": "Prekybos centras",
    "Stały punkt, do którego ludzie wracają — i przyprowadzają znajomych.":
        "Nuolatinė vieta, į kurią žmonės grįžta — ir atsiveda pažįstamus.",
    "Muzeum i centrum nauki": "Muziejus ir mokslo centras",
    "Oprowadza, tłumaczy eksponaty, rozmawia z grupami szkolnymi.":
        "Veda ekskursijas, paaiškina eksponatus, kalbasi su mokinių grupėmis.",
    "Uczelnia i szkoła": "Universitetas ir mokykla",
    "Narzędzie dydaktyczne i wizytówka kierunku podczas dni otwartych.":
        "Mokymo priemonė ir studijų krypties vizitinė kortelė per atvirų durų dienas.",
    "Agencja eventowa": "Renginių agentūra",
    "Własny robot w ofercie zamiast podnajmowania go przy każdym zleceniu.":
        "Savas robotas pasiūlyme vietoj nuomos kiekvienam užsakymui.",

    # Realizacijos
    "Zrealizowane wdrożenia": "Įgyvendinti diegimai",
    "Pierwsze wdrożenie startuje w najbliższych dniach":
        "Pirmasis diegimas startuoja artimiausiomis dienomis",
    "Opiszemy je tutaj razem ze zdjęciami i efektami — bez koloryzowania. Do tego czasu najlepszym dowodem naszego doświadczenia są realizacje eventowe: kilkadziesiąt pokazów w całej Polsce i za granicą, materiały w Teleexpressie TVP i reportaż TVP Gdańsk.":
        "Aprašysime jį čia kartu su nuotraukomis ir rezultatais — be gražinimo. Iki tol geriausias mūsų patirties įrodymas yra renginių realizacijos: kelios dešimtys pasirodymų Lenkijoje ir užsienyje, siužetai Lenkijos televizijoje TVP.",
    "Case study LEX AI": "Atvejo analizė: LEX AI",

    # DUK
    "Częste pytania": "Dažni klausimai",
    "Czym wdrożenie różni się od wynajmu?": "Kuo diegimas skiriasi nuo nuomos?",
    "Przy wynajmie przywozimy robota na wydarzenie i zabieramy go po zakończeniu — obsługą zajmuje się nasz operator. Przy wdrożeniu robot staje się Waszą własnością, pracuje u Was na co dzień, a obsługuje go przeszkolony zespół. Wynajem sprawdza się przy pojedynczych wydarzeniach, wdrożenie wtedy, gdy robot ma być stałym elementem firmy.":
        "Nuomos atveju atvežame robotą į renginį ir pasiimame jį po pabaigos — valdo mūsų operatorius. Diegimo atveju robotas tampa jūsų nuosavybe, dirba pas jus kasdien, o valdo jį apmokyta jūsų komanda. Nuoma tinka pavieniams renginiams, diegimas — kai robotas turi tapti nuolatine įmonės dalimi.",
    "Ile to kosztuje?": "Kiek tai kainuoja?",
    "Cena zależy od modelu robota oraz zakresu oprogramowania i wsparcia, dlatego wyceniamy każde wdrożenie osobno. Wycenę przygotowujemy po krótkiej rozmowie o tym, do czego robot ma służyć — bez zobowiązań z Waszej strony.":
        "Kaina priklauso nuo roboto modelio bei programinės įrangos ir pagalbos apimties, todėl kiekvieną diegimą vertiname atskirai. Pasiūlymą parengiame po trumpo pokalbio apie tai, kam robotas skirtas — be jokių įsipareigojimų iš jūsų pusės.",
    "Ile trwa całe wdrożenie?": "Kiek trunka visas diegimas?",
    "Najdłuższy etap to sprowadzenie robota — zwykle około miesiąca od zamówienia. Konfigurację oprogramowania i przygotowanie bazy wiedzy prowadzimy równolegle, więc po dostawie zostaje uruchomienie i szkolenie, czyli zazwyczaj jeden dzień u Was.":
        "Ilgiausias etapas — roboto parvežimas, paprastai apie mėnesį nuo užsakymo. Programinės įrangos konfigūraciją ir žinių bazę ruošiame lygiagrečiai, todėl po pristatymo lieka paleidimas ir mokymai — paprastai viena diena pas jus.",
    "Skąd robot wie, co odpowiadać?": "Iš kur robotas žino, ką atsakyti?",
    "Kto może obsługiwać robota po szkoleniu?": "Kas gali valdyti robotą po mokymų?",
    "Dowolna osoba z Waszego zespołu — nie trzeba mieć wykształcenia technicznego. Szkolenie obejmuje uruchamianie, prowadzenie pokazu, ładowanie, zmianę scenariuszy i zasady bezpieczeństwa. Zostawiamy instrukcję napisaną prostym językiem, żeby dało się do niej wrócić.":
        "Bet kuris jūsų komandos žmogus — techninio išsilavinimo nereikia. Mokymai apima paleidimą, pasirodymo vedimą, krovimą, scenarijų keitimą ir saugos taisykles. Paliekame paprasta kalba parašytą instrukciją, prie kurios visada galima grįžti.",
    "Co z gwarancją i serwisem?": "O kaip su garantija ir servisu?",
    "Robot objęty jest gwarancją producenta, a my pośredniczymy w jej obsłudze — nie musicie kontaktować się z Chinami. Zakres wsparcia technicznego po uruchomieniu ustalamy przy wycenie, zależnie od tego, jak intensywnie robot ma pracować.":
        "Robotui taikoma gamintojo garantija, o mes tarpininkaujame ją administruojant — jums nereikia susisiekti su Kinija. Techninės pagalbos apimtį po paleidimo suderiname rengdami pasiūlymą, atsižvelgdami į tai, kaip intensyviai robotas dirbs.",

    # Forma
    "Opowiedz, do czego": "Papasakokite, kam",
    "potrzebujesz robota.": "jums reikia roboto.",
    "Oddzwonimy, doradzimy model i zakres, a potem przygotujemy wycenę. Bez zobowiązań.":
        "Susisieksime, patarsime dėl modelio ir apimties, o paskui parengsime pasiūlymą. Be įsipareigojimų.",
    "Imię i nazwisko *": "Vardas ir pavardė *",
    "E-mail *": "El. paštas *",
    "Telefon": "Telefonas",
    "Firma": "Įmonė",
    "Do czego ma służyć robot? *": "Kam bus naudojamas robotas? *",
    "Wyślij zapytanie": "Siųsti užklausą",
    "Odpowiadamy w ciągu 24 godzin roboczych.": "Atsakome per 24 darbo valandas.",
}

ATTRS = {
    "Kupujesz robota humanoidalnego, my konfigurujemy mowę i wiedzę o Twojej firmie oraz szkolimy zespół z obsługi. Dostawa, uruchomienie na miejscu i wsparcie po starcie.":
        "Jūs įsigyjate humanoidinį robotą, mes sukonfigūruojame kalbą ir žinias apie jūsų įmonę bei apmokome komandą. Pristatymas, paleidimas vietoje ir pagalba po starto.",
    "Robot na stałe w Twojej firmie: sprzęt, oprogramowanie do mowy z wiedzą o Twojej ofercie i szkolenie zespołu.":
        "Robotas nuolat jūsų įmonėje: įranga, kalbos programinė įranga su žiniomis apie jūsų pasiūlymą ir komandos mokymai.",
    "Gdzie miałby pracować, jakie zadania ma wykonywać, czy macie już pomysł na scenariusz.":
        "Kur jis dirbtų, kokias užduotis atliktų, ar jau turite scenarijaus idėją.",
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
    "Odezwiemy się na": "Susisieksime adresu",
    "w ciągu 24 godzin roboczych": "per 24 darbo valandas",
    "Wysyłanie...": "Siunčiama...",
    "Wysyłanie…": "Siunčiama…",
    "WDROŻENIE — zapytanie ze strony": "DIEGIMAS — užklausa iš svetainės",
    "Spróbuj ponownie": "Bandykite dar kartą",
    "Coś poszło nie tak": "Kažkas nepavyko",
    "Formularz — błąd wysyłki": "Forma — siuntimo klaida",
    "Zapytanie o wdrożenie": "Užklausa dėl diegimo",
}
