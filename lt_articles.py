# -*- coding: utf-8 -*-
"""33bots.lt blogo straipsnių turinys."""

# Kiekvienas straipsnis: slug, title, desc, tag, h1, lead, published, sections[(h2, html)], faq
ARTICLES = [
    dict(
        slug="blog-kiek-kainuoja-roboto-nuoma.html",
        title="Kiek kainuoja humanoidinio roboto nuoma Lietuvoje? Kainos 2026",
        desc="Nuo ko priklauso roboto nuomos kaina, kas įeina į paketą ir kokių paslėptų mokesčių "
             "saugotis. Skaidrus vadovas organizatoriams.",
        keywords="kiek kainuoja roboto nuoma, roboto nuomos kaina, humanoidinio roboto kaina, robotas renginiui kaina",
        tag="Kainos · Paketai",
        card="Skaidrus vadovas po roboto nuomos kaštus Lietuvoje: kas įeina į kainą, kaip skaičiuojamas "
             "pasiūlymas ir kaip vertiname atvykimą.",
        h1="Kiek kainuoja<br />humanoidinio roboto<br />nuoma?",
        lead="Trumpas atsakymas: priklauso nuo trukmės, formato ir to, kiek paslaugų įeina į paketą. "
             "Ilgas atsakymas — šiame straipsnyje, su visais kintamaisiais, kuriuos verta patikrinti "
             "prieš pasirašant sutartį.",
        published="2026-02-10", modified="2026-07-20",
        sections=[
            ("Nuo ko priklauso roboto nuomos kaina",
             "<p>Humanoidinio roboto nuomos kaina Lietuvoje formuojama iš kelių aiškių dedamųjų. "
             "Svarbiausia — <strong>renginio trukmė</strong>: trijų valandų pasirodymas ir visos dienos "
             "darbas parodoje yra du visiškai skirtingi produktai. Antra — <strong>formatas</strong>: "
             "statiška nuotraukų zona reikalauja mažiau paruošimo nei choreografija scenoje su garso "
             "sistema.</p>"
             "<p>Trečias veiksnys — <strong>data</strong>. Rugsėjis–gruodis ir gegužė–birželis yra "
             "renginių sezono piko mėnesiai, todėl populiariausios datos užsipildo anksti. Ketvirtas — "
             "<strong>papildomos paslaugos</strong>: ženklinimas, individualus scenarijus, antras "
             "operatorius, kelių dienų logistika.</p>"
             "<p>Ką reikia žinoti apie kainą iš karto: rimtos įmonės nepateikia vienos „kainos už "
             "robotą\" internete, nes kiekvienas renginys skiriasi. Bet turi pateikti <strong>aiškią "
             "kainą per 24 valandas</strong> po to, kai gauna renginio detales — jei to nedaro, tai "
             "signalas.</p>"),
            ("Kas turi įeiti į nuomos kainą",
             "<p>Rinkoje pasitaiko modelis, kai bazinė kaina atrodo patraukliai, o paskui atsiranda "
             "priedai. Todėl vertinant pasiūlymus svarbu lyginti ne skaičių, o <strong>paketo "
             "turinį</strong>. Standartinis pilnas paketas turėtų apimti:</p>"
             "<ul>"
             "<li><strong>Robotą</strong> ir visą reikalingą įrangą (baterijos, valdymas, garsas).</li>"
             "<li><strong>Operatorių</strong> visą renginio laiką — ne tik atvežimui ir paleidimui.</li>"
             "<li><strong>Atvykimą</strong> į renginio vietą — vertiname pagal lokaciją.</li>"
             "<li><strong>Paruošimą vietoje</strong> ir bandomąjį paleidimą prieš renginį.</li>"
             "<li><strong>Draudimą</strong> — civilinės atsakomybės apsaugą veiklai.</li>"
             "<li><strong>Ženklinimą</strong> jūsų logotipu ir QR kodu.</li>"
             "</ul>"
             "<p>33bots atveju operatorius, ženklinimas, scenarijaus paruošimas ir draudimas yra "
             "standartas, o ne priedas. Atvykimą vertiname atskirai — pagal renginio vietą, ir sumą "
             "nurodome pasiūlyme.</p>"),
            ("Paketai ir tipiniai formatai",
             "<div class=\"data-table-wrap\">"
             "<table class=\"data-table\">"
             "<thead><tr><th>Paketas</th><th>Trukmė</th><th>Kam tinka</th><th>Kas įeina</th></tr></thead>"
             "<tbody>"
             "<tr><td><strong>Impulsas</strong></td><td>iki 3 val.</td><td>Pertrauka konferencijoje, "
             "stendo atidarymas, trumpas pasirodymas</td><td>Robotas, operatorius, "
             "trumpas pasirodymas</td></tr>"
             "<tr><td><strong>Standartas</strong></td><td>iki 8 val.</td><td>Visa renginio diena, "
             "įmonės šventė, gala vakaras</td><td>Robotas, operatorius su asistentu, ženklinimas, "
             "bendravimas su svečiais</td></tr>"
             "<tr><td><strong>Multi-Day</strong></td><td>2–7+ dienų</td><td>Parodos, festivaliai, "
             "ilgesnės kampanijos</td><td>Skirtas operatorius, pilnas pritaikymas, visa logistika</td></tr>"
             "</tbody></table></div>"
             "<p>Praktikoje daugiausia užsakymų būna „Standartas\" paketo — jis padengia tipinę "
             "konferencijos ar įmonės šventės dieną. Parodoms beveik visada renkamasi kelių dienų "
             "variantas, nes kasdienis logistikos derinimas kainuoja daugiau nei nuolatinė nuoma.</p>"),
            ("Nuoma ar pirkimas — kada kas apsimoka",
             "<p>Humanoidinis robotas yra investicija, kurios kaina siekia dešimtis tūkstančių eurų, ir "
             "tai tik pradžia. Prie įsigijimo kainos prisideda operatoriaus mokymai, techninė priežiūra, "
             "atsarginės dalys, programinės įrangos atnaujinimai, transportavimo įranga, sandėliavimas "
             "ir draudimas.</p>"
             "<p>Paprasta taisyklė: jei planuojate <strong>iki 10–15 renginių per metus</strong>, nuoma "
             "beveik visada pigesnė ir paprastesnė. Pirkimas pradeda turėti prasmę tik tada, kai robotas "
             "tampa nuolatine verslo dalimi — pavyzdžiui, agentūroms, kurios jį naudoja kelis kartus "
             "per savaitę.</p>"
             "<div class=\"callout\"><p><strong>Svarbu:</strong> nuomos atveju technologijos senėjimo "
             "rizika lieka nuomotojui. Humanoidinių robotų karta keičiasi kas 2–3 metus — nuomojantis "
             "jūs visada gaunate aktualų modelį.</p></div>"),
            ("Kaip palyginti kelis pasiūlymus",
             "<p>Prieš renkantis paprašykite kiekvieno tiekėjo atsakyti į tuos pačius klausimus: kiek "
             "kainuoja transportas į jūsų miestą; ar operatorius lieka visą renginį; ar ženklinimas "
             "įskaičiuotas; kokia atšaukimo tvarka; ar veikla apdrausta. Skirtumai išryškėja būtent "
             "šiuose atsakymuose, o ne bazinėje kainoje.</p>"
             "<p>Detalų klausimų sąrašą surinkome straipsnyje "
             "<a href=\"blog-kaip-issinuomoti-robota.html\">kaip išsinuomoti robotą — pilnas vadovas</a>. "
             "Jei norite konkrečios kainos savo renginiui — <a href=\"kainos.html\">peržiūrėkite, kas "
             "įeina į mūsų paketus</a> arba parašykite mums.</p>"),
        ],
        faq=[
            ("Ar galima gauti kainą iš karto internete?",
             "Ne — ir tai sąmoningas sprendimas. Kaina priklauso nuo trukmės, formato ir datos, todėl "
             "vietoj bendro kainoraščio pateikiame konkrečią kainą per 24 valandas po užklausos."),
            ("Kiek kainuoja atvykimas?",
             "Atvykimą vertiname pagal renginio vietą ir sumą nurodome pasiūlyme kartu su nuomos "
             "kaina. Dirbame visoje Lietuvoje — nuo Vilniaus iki Mažeikių."),
            ("Ar reikia mokėti avansą?",
             "Taip, data rezervuojama avansu — tai standartinė renginių rinkos praktika. Likusi suma "
             "mokama pagal sutartyje numatytą tvarką."),
            ("Ar kaina keičiasi savaitgaliais?",
             "Savaitgaliai ir vakarai yra įprastas renginių laikas, todėl bazinė logika nesikeičia. "
             "Kainai labiau įtakos turi sezonas ir trukmė nei savaitės diena."),
        ],
        related=[("kainos.html", "Kas įeina į kainą"),
                 ("blog-kaip-issinuomoti-robota.html", "Nuomos vadovas"),
                 ("humanoidinio-roboto-nuoma.html", "Nuomos sąlygos")],
    ),
    dict(
        slug="blog-kodel-robotas-renginyje.html",
        title="5 priežastys, kodėl jūsų renginiui reikia humanoidinio roboto",
        desc="Robotas renginyje nėra žaisliukas — tai rinkodaros sprendimas. Kaip humanoidas generuoja "
             "kontaktus, organinį pasiekiamumą ir lieka svečių atmintyje.",
        keywords="robotas renginyje, kodėl robotas renginiui, renginio pramoga, renginių rinkodara",
        tag="Renginiai · Strategija",
        card="Robotas renginyje — ne žaisliukas, o rinkodaros sprendimas. Kodėl G1 generuoja kontaktus, "
             "virusinį pasiekiamumą ir lieka svečių atmintyje savaitėms.",
        h1="5 priežastys, kodėl<br />jūsų renginiui reikia<br />humanoido.",
        lead="Renginių biudžetai mažėja, o lūkesčiai auga. Humanoidinis robotas yra viena iš nedaugelio "
             "investicijų, kuri vienu metu veikia kaip pramoga, turinio šaltinis ir kontaktų generavimo "
             "įrankis.",
        published="2026-01-18", modified="2026-07-15",
        sections=[
            ("1. Robotas sustabdo žmones — tiesiogine prasme",
             "<p>Renginiuose dėmesys yra ribotas išteklius. Lankytojas praeina pro dešimtis stendų, "
             "baneriu ir ekranų, ir beveik nė vienas jo nesustabdo. Humanoidinis robotas sustabdo — nes "
             "smegenys negali jo ignoruoti. Judantis, žmogaus formos objektas įjungia dėmesį "
             "automatiškai, dar prieš racionalų sprendimą.</p>"
             "<p>Praktikoje tai atrodo paprastai: prie stendo su robotu susidaro minia, o aplinkiniai "
             "stendai lieka tušti. Jūsų komandai nebereikia kabinti praeivių — žmonės jau stovi ir "
             "žiūri, o pokalbį pradėti daug lengviau.</p>"),
            ("2. Gaunate kontaktus, kurių kitaip nebūtų",
             "<p>Dėmesys pats savaime nėra rezultatas. Bet dėmesys plius paprasta mainų mechanika duoda "
             "kontaktus. Veikiantis modelis: nuotrauka su robotu mainais į trumpą registraciją arba QR "
             "kodas ant roboto krūtinės, vedantis į konkretų pasiūlymą.</p>"
             "<p>Svarbus niuansas — kontaktai, surinkti aplink robotą, dažnai yra kokybiškesni nei "
             "surinkti loterijos būdu. Žmogus, kuris sustojo dėl technologijos, jau parodė susidomėjimą "
             "inovacijomis, o tai daugeliui B2B įmonių yra tinkamas signalas.</p>"),
            ("3. Organinis pasiekiamumas, už kurį nemokate",
             "<p>Kiekvienas svečias, kuris nufilmuoja robotą, tampa jūsų renginio platintoju. Skirtingai "
             "nei mokama reklama, šis turinys neatrodo kaip reklama — todėl ir veikia. Vienas geras "
             "įrašas iš renginio dažnai surenka daugiau peržiūrų nei visa mėnesio socialinių tinklų "
             "kampanija.</p>"
             "<p>Tai taip pat medžiaga, kurią naudosite vėliau: ataskaitoje rėmėjams, kitų metų renginio "
             "reklamai, employer branding turiniui. Renginys baigiasi per dieną, o įrašai dirba mėnesius.</p>"),
            ("4. Prekės ženklo signalas be nė vienos skaidrės",
             "<p>Įmonė, kuri į renginį atveža humanoidinį robotą, komunikuoja apie save daugiau nei "
             "dvidešimties skaidrių pristatymas. Žinutė perskaitoma akimirksniu: čia žmonės, kurie "
             "domisi technologijomis ir nebijo rizikuoti.</p>"
             "<p>Ypač stipriai tai veikia technologijų, logistikos, finansų ir gamybos sektoriuose, kur "
             "inovatyvumo įvaizdis tiesiogiai susijęs su pardavimais ir talentų pritraukimu.</p>"),
            ("5. Pokalbių tema, kuri lieka po renginio",
             "<p>Klausimas, kurį verta užduoti planuojant biudžetą: apie ką svečiai kalbės kitą dieną? "
             "Retai apie maistą ar apie pranešėją. Beveik visada apie tai, ko nesitikėjo pamatyti.</p>"
             "<p>Humanoidinis robotas Lietuvoje vis dar yra retenybė — daugumai svečių tai bus pirmas "
             "kartas, kai jie mato tokį įrenginį gyvai. Būtent tai paverčia renginį prisimenamu, o ne "
             "dar vienu punktu kalendoriuje.</p>"
             "<div class=\"callout\"><p>Norite pamatyti, kaip tai atrodo praktikoje? Peržiūrėkite "
             "<a href=\"video-realizacijos.html\">įrašus iš renginių</a> arba palyginkite robotą su "
             "kitomis pramogomis <a href=\"blog-robotas-ar-kitos-pramogos.html\">šiame straipsnyje</a>.</p></div>"),
        ],
        faq=[
            ("Ar robotas tinka rimtam B2B renginiui?",
             "Taip. Pasirodymo tonas visiškai priklauso nuo scenarijaus — formaliems renginiams "
             "renkamės santūresnį formatą, kur robotas veikia kaip technologijos demonstracija, o ne "
             "kaip šou."),
            ("Kiek žmonių turi būti renginyje, kad robotas apsimokėtų?",
             "Robotas veikia jau nuo kelių dešimčių svečių, bet didžiausią vertę duoda renginiuose nuo "
             "100 dalyvių, kur svarbus ir turinio pasiekiamumas."),
            ("Ar robotas pakeičia kitas pramogas?",
             "Dažniausiai jis jas papildo. Robotas duoda WOW efektą ir turinį, o muzika ar maistas "
             "kuria bendrą renginio atmosferą."),
        ],
        related=[("robotas-renginiui.html", "Robotas renginiui"),
                 ("blog-robotas-ar-kitos-pramogos.html", "Pramogų palyginimas"),
                 ("video-realizacijos.html", "Vaizdo įrašai")],
    ),
    dict(
        slug="blog-unitree-g1-specifikacija.html",
        title="Unitree G1 — specifikacija, galimybės ir kodėl tinka renginiams",
        desc="Unitree G1 techninė specifikacija: 132 cm, 35 kg, 43 laisvės laipsniai, 2 m/s. Palyginimas "
             "su kitais humanoidais ir praktinės galimybės renginiuose.",
        keywords="Unitree G1, Unitree G1 specifikacija, humanoidinis robotas, G1 robotas, robotas 43 DOF",
        tag="Technologijos · Unitree G1",
        card="Viskas apie robotą Unitree G1: 132 cm ūgis, 43 DoF, 2 m/s greitis. Specifikacijų lentelės "
             "ir palyginimas su kitais humanoidais.",
        h1="Unitree G1 —<br />specifikacija ir<br />galimybės.",
        lead="Unitree G1 yra vienas prieinamiausių pilnai funkcionalių humanoidinių robotų rinkoje — ir "
             "kartu vienas tinkamiausių renginiams. Štai kodėl, su skaičiais.",
        published="2026-03-05", modified="2026-07-18",
        sections=[
            ("Techninė specifikacija",
             "<div class=\"data-table-wrap\">"
             "<table class=\"data-table\">"
             "<thead><tr><th>Parametras</th><th>Reikšmė</th><th>Ką tai reiškia praktikoje</th></tr></thead>"
             "<tbody>"
             "<tr><td>Ūgis</td><td>~132 cm</td><td>Matomas minioje, bet nekelia grėsmės pojūčio — idealus "
             "bendravimui su svečiais ir vaikais</td></tr>"
             "<tr><td>Svoris</td><td>~35 kg</td><td>Transportuojamas be specialios technikos, telpa į "
             "įprastą furgoną</td></tr>"
             "<tr><td>Laisvės laipsniai</td><td>iki 43 DOF</td><td>Sklandūs, natūralūs judesiai — gestai, "
             "pasisveikinimai, choreografija</td></tr>"
             "<tr><td>Judėjimo greitis</td><td>iki ~2 m/s</td><td>Gali judėti kartu su žmonių srautu, "
             "vaikščioti po stendą ir salę</td></tr>"
             "<tr><td>Jutikliai</td><td>LiDAR, kompiuterinė rega</td><td>Realiu laiku aptinka kliūtis ir "
             "žmones — pagrindas saugiam darbui minioje</td></tr>"
             "<tr><td>Maitinimas</td><td>keičiama baterija</td><td>Darbas ciklais visą dieną, be ilgų "
             "prastovų įkrovimui</td></tr>"
             "</tbody></table></div>"
             "<p>Skaičiai svarbūs, bet renginiuose lemia ne jie, o <strong>judesio kokybė</strong>. "
             "43 laisvės laipsniai reiškia, kad G1 juda ne kaip mechanizmas, o kaip kūnas — būtent dėl "
             "to žmonės reaguoja emociškai.</p>"),
            ("Ką G1 realiai daro renginyje",
             "<p>Praktinės galimybės, kurias naudojame kasdien:</p>"
             "<ul>"
             "<li><strong>Vaikščiojimas ir orientacija</strong> — robotas juda po stendą ar salę, "
             "apeidamas žmones ir kliūtis.</li>"
             "<li><strong>Gestai ir pasisveikinimai</strong> — rankos paspaudimas, mostas, nusilenkimas, "
             "pozavimas nuotraukoms.</li>"
             "<li><strong>Choreografija</strong> — įrašyti šokių sekvencijos, derinamos su renginio "
             "muzika.</li>"
             "<li><strong>Balso pasisakymai</strong> — iš anksto paruošti tekstai lietuvių ar anglų "
             "kalba per garso sistemą.</li>"
             "<li><strong>Ženklinimas</strong> — logotipas ir QR kodas ant krūtinės, spalviniai akcentai.</li>"
             "</ul>"
             "<p>Ko G1 nedaro: neveda viso renginio savarankiškai, nepriima nenumatytų sprendimų ir "
             "nepakeičia žmogaus vedėjo. Tai įrankis, kurį valdo operatorius — ir būtent todėl jis "
             "veikia patikimai.</p>"),
            ("Kuo G1 skiriasi nuo kitų humanoidų",
             "<p>Rinkoje yra didesnių ir technologiškai sudėtingesnių humanoidų, bet renginiams svarbu "
             "kitas dalykas — <strong>patikimumas ir logistika</strong>. G1 pranašumai šioje "
             "kategorijoje:</p>"
             "<ul>"
             "<li><strong>Dydis</strong>: pakankamai didelis, kad būtų įspūdingas, pakankamai mažas, "
             "kad tilptų į bet kurią salę.</li>"
             "<li><strong>Transportuojamumas</strong>: 35 kg galima pervežti standartiniu automobiliu "
             "be specialios įrangos.</li>"
             "<li><strong>Paruošimo greitis</strong>: nuo atvykimo iki pirmo pasirodymo — apie "
             "30–45 minutes.</li>"
             "<li><strong>Judesio natūralumas</strong>: 43 DOF suteikia sklandumą, kurio neturi "
             "paprastesni modeliai.</li>"
             "</ul>"
             "<p>Jei svarstote tarp humanoido ir paprastesnio mobilaus roboto, palyginimą rasite "
             "straipsnyje <a href=\"blog-humanoidinis-ar-mobilus-robotas.html\">humanoidinis ar mobilus "
             "robotas</a>.</p>"),
            ("Kada G1 yra tinkamiausias pasirinkimas",
             "<p>G1 geriausiai tinka, kai renginyje reikia <strong>artimo kontakto su žmonėmis</strong>: "
             "parodų stenduose, konferencijų registracijose, įmonių šventėse, prekybos centrų "
             "atidarymuose. Ten, kur svarbu, kad žmonės galėtų prieiti, nusifotografuoti ir pabendrauti.</p>"
             "<p>Mažiau tinka scenarijams, kur reikia nešti sunkius krovinius, dirbti sudėtingomis "
             "oro sąlygomis arba veikti visiškai autonomiškai be operatoriaus. Tokiems poreikiams "
             "egzistuoja kitos robotų klasės.</p>"),
        ],
        faq=[
            ("Ar Unitree G1 yra dirbtinio intelekto robotas?",
             "G1 naudoja kompiuterinę regą ir jutiklių duomenų apdorojimą judesiui bei orientacijai. "
             "Renginiuose jį valdo operatorius pagal iš anksto suderintą scenarijų — tai užtikrina, kad "
             "pasirodymas vyktų nuspėjamai."),
            ("Kiek laiko veikia baterija?",
             "Priklausomai nuo intensyvumo, vienas ciklas trunka apie valandą aktyvaus darbo. Baterijos "
             "keičiamos per suplanuotas pertraukas, todėl robotas gali dirbti visą dieną."),
            ("Ar robotas gali lipti laiptais?",
             "G1 techniškai geba judėti nelygiu paviršiumi, bet renginiuose laiptų vengiame dėl saugumo. "
             "Perkėlimams tarp aukštų naudojame liftą arba nešame robotą."),
            ("Ar galima robotą pamatyti prieš renginį?",
             "Taip — didesniems projektams organizuojame demonstraciją arba vaizdo skambutį su robotu, "
             "kad galėtumėte pamatyti jį veikiantį prieš pasirašydami sutartį."),
        ],
        related=[("humanoidinio-roboto-nuoma.html", "Nuomos sąlygos"),
                 ("blog-humanoidinis-ar-mobilus-robotas.html", "Humanoidas ar mobilus robotas"),
                 ("video-realizacijos.html", "Vaizdo įrašai")],
    ),
    dict(
        slug="blog-robotas-parodu-stende.html",
        title="Robotas parodų stende — kaip paversti dėmesį kontaktais",
        desc="Praktinis vadovas, kaip humanoidinį robotą panaudoti parodų stende: vietos parinkimas, "
             "pasirodymų grafikas, kontaktų rinkimo mechanikos ir dažniausios klaidos.",
        keywords="robotas parodų stende, parodos stendas, kontaktų rinkimas parodoje, lead generation paroda",
        tag="Parodos · Kontaktų rinkimas",
        card="Kaip humanoidinis robotas sustabdo minią parodose ir paverčia srautą realiais verslo "
             "kontaktais. Mechanikos ir stendo išdėstymo patarimai.",
        h1="Robotas parodų stende —<br />kaip paversti dėmesį<br /><em>kontaktais.</em>",
        lead="Robotas pritrauks minią net jei nieko nedarysite. Bet minia ir kontaktų sąrašas yra du "
             "skirtingi dalykai — tarp jų reikia mechanikos.",
        published="2026-04-02", modified="2026-07-22",
        sections=[
            ("Kur stende statyti robotą",
             "<p>Dažniausia klaida — robotas statomas stendo gilumoje, „kad netrukdytų\". Rezultatas: "
             "žmonės sustoja praėjime, žiūri iš toli ir eina toliau, o jūsų komanda net nespėja "
             "užkalbinti.</p>"
             "<p>Veikianti pozicija — <strong>stendo krašte, matoma iš pagrindinio praėjimo</strong>, su "
             "2×2 m laisvos erdvės aplink. Robotas turi būti matomas iš toli, bet žmogus turi žengti į "
             "stendo teritoriją, kad prieitų arčiau. Tai natūraliai įtraukia lankytoją į jūsų erdvę.</p>"
             "<div class=\"callout\"><p><strong>Praktinis patarimas:</strong> palikite aiškų priėjimo "
             "koridorių. Jei prie roboto susidaro spūstis, kuri blokuoja įėjimą į stendą, prarandate "
             "būtent tuos lankytojus, kurie norėjo pakalbėti su jūsų komanda.</p></div>"),
            ("Pasirodymų grafikas, kuris grąžina žmones",
             "<p>Nuolat veikiantis robotas per dieną tampa fonu. Todėl geriau dirbti "
             "<strong>ciklais</strong>: fiksuotas pasirodymas kas valandą (pvz. 10 minučių), o tarp jų — "
             "laisvas bendravimas ir nuotraukos.</p>"
             "<p>Grafiką verta paskelbti stende ir socialiniuose tinkluose. Tai duoda du efektus: "
             "lankytojai grįžta konkrečiu laiku, o jūsų komanda gali planuoti susitikimus aplink "
             "pasirodymus, o ne atsitiktinai.</p>"),
            ("Kontaktų rinkimo mechanikos",
             "<p>Keletas modelių, kurie veikia parodose:</p>"
             "<ul>"
             "<li><strong>Nuotrauka mainais į registraciją</strong> — svečias nusifotografuoja su robotu, "
             "o nuotrauką atsiunčiate el. paštu. Paprasta, savanoriška, teisėta.</li>"
             "<li><strong>QR kodas ant roboto</strong> — nuskaitymas veda į nusileidimo puslapį su "
             "konkrečia nauda (kainoraštis, demonstracija, katalogas).</li>"
             "<li><strong>Trumpa demonstracija po pasirodymo</strong> — po roboto pasirodymo jūsų "
             "specialistas 3 minutes pristato produktą jau susirinkusiai auditorijai.</li>"
             "<li><strong>Konkursas su robotu</strong> — dalyviai registruojasi, o laimėtojas skelbiamas "
             "paskutinę parodos dieną, kad srautas grįžtų.</li>"
             "</ul>"
             "<p>Bendra taisyklė: mainai turi būti akivaizdūs ir greiti. Jei registracija trunka ilgiau "
             "nei 30 sekundžių, dauguma pasitrauks.</p>"),
            ("Dažniausios klaidos",
             "<p><strong>Per mažai žmonių stende.</strong> Robotas sukuria srautą, kurio nespėja "
             "aptarnauti du žmonės. Parodos dienoms su robotu planuokite bent 3–4 komandos narius.</p>"
             "<p><strong>Nėra aiškaus kito žingsnio.</strong> Žmogus nusifotografavo — ir kas toliau? "
             "Jei nėra paruoštos frazės ir aiškaus pasiūlymo, kontaktas prarandamas.</p>"
             "<p><strong>Robotas be ženklinimo.</strong> Nuotrauka su neženklintu robotu pasklinda "
             "socialiniuose tinkluose be jūsų prekės ženklo. Logotipas ir QR kodas ant krūtinės "
             "išsprendžia tai už 0 €.</p>"
             "<p>Daugiau apie parodų formatą — <a href=\"robotas-parodoms.html\">roboto parodoms "
             "puslapyje</a>. Jei renginys apima ir konferencinę dalį, žiūrėkite "
             "<a href=\"robotas-konferencijai.html\">konferencijų pasiūlymą</a>.</p>"),
        ],
        faq=[
            ("Kiek komandos narių reikia stende su robotu?",
             "Rekomenduojame bent 3–4 žmones. Robotas generuoja srautą, kurio maža komanda paprasčiausiai "
             "nespėja aptarnauti — o neaptarnautas lankytojas yra prarastas kontaktas."),
            ("Ar robotas tinka mažam stendui?",
             "Nuo maždaug 9 m² — taip. Mažesniuose stenduose robotas dirba statiškai: sveikinasi, pozuoja "
             "nuotraukoms, bet neatlieka pilnos choreografijos."),
            ("Ar galime patys valdyti robotą stende?",
             "Robotą valdo mūsų operatorius. Tai užtikrina saugumą minioje ir reiškia, kad jūsų komanda "
             "gali visą dėmesį skirti pokalbiams su lankytojais."),
        ],
        related=[("robotas-parodoms.html", "Robotas parodoms"),
                 ("robotas-konferencijai.html", "Konferencijos"),
                 ("kainos.html", "Kainos")],
    ),
    dict(
        slug="blog-kaip-issinuomoti-robota.html",
        title="Kaip išsinuomoti humanoidinį robotą — pilnas vadovas 2026",
        desc="Žingsnis po žingsnio: nuo užklausos iki renginio dienos. Ką patikrinti renkantis nuomos "
             "įmonę, kokius klausimus užduoti ir kaip pasiruošti renginiui.",
        keywords="kaip išsinuomoti robotą, roboto nuoma vadovas, roboto nuomos sutartis, robotų nuoma",
        tag="Vadovas · Nuoma",
        card="Kaip išsinuomoti humanoidinį robotą žingsnis po žingsnio: ką apima paslauga, į ką atkreipti "
             "dėmesį renkantis įmonę ir kada robotas turi daugiausia prasmės.",
        h1="Kaip išsinuomoti<br />humanoidinį robotą —<br />pilnas vadovas.",
        lead="Roboto nuoma nėra sudėtinga, jei žinote, ko klausti. Šis vadovas sudėlioja visą procesą — "
             "nuo pirmos užklausos iki renginio pabaigos.",
        published="2026-05-12", modified="2026-07-24",
        sections=[
            ("Žingsnis 1: apsibrėžkite, ko norite",
             "<p>Prieš rašydami užklausą atsakykite sau į keturis klausimus: <strong>kada</strong> "
             "(data ir valandos), <strong>kur</strong> (miestas ir vieta), <strong>kiek žmonių</strong> "
             "ir <strong>kokio efekto tikitės</strong> — pramoga svečiams, kontaktų rinkimas ar turinys "
             "socialiniams tinklams.</p>"
             "<p>Šie keturi duomenys leidžia pateikti tikslų pasiūlymą iš karto, be kelių dienų "
             "susirašinėjimo. Jei kai kurių dar nežinote — tai irgi normalu, tiesiog paminėkite.</p>"),
            ("Žingsnis 2: patikrinkite tiekėją",
             "<p>Klausimai, kuriuos verta užduoti kiekvienai įmonei:</p>"
             "<ul>"
             "<li>Ar robotas <strong>jūsų nuosavas</strong>, ar nuomojamas iš tarpininko?</li>"
             "<li>Ar operatorius lieka <strong>visą renginio laiką</strong>?</li>"
             "<li>Kiek kainuoja <strong>atvykimas</strong> į mano miestą?</li>"
             "<li>Ar veikla <strong>apdrausta</strong> civilinės atsakomybės draudimu?</li>"
             "<li>Ar <strong>ženklinimas</strong> įskaičiuotas į kainą?</li>"
             "<li>Kokia <strong>atšaukimo</strong> ir datos perkėlimo tvarka?</li>"
             "<li>Ar galima pamatyti <strong>įrašų iš tikrų renginių</strong>, ne tik gamintojo "
             "reklamos?</li>"
             "</ul>"
             "<div class=\"callout\"><p>Paskutinis punktas svarbiausias. Gamintojo reklaminiai įrašai "
             "atrodo įspūdingai, bet nieko nesako apie tai, kaip įmonė dirba realiame renginyje. "
             "Prašykite medžiagos iš jų pačių projektų — mūsų rasite "
             "<a href=\"video-realizacijos.html\">čia</a>.</p></div>"),
            ("Žingsnis 3: sutartis ir rezervacija",
             "<p>Sutartyje turi būti aiškiai nurodyta: renginio data ir valandos, vieta, kas įeina į "
             "paslaugą, kaina su PVM, mokėjimo grafikas, atšaukimo sąlygos ir atsakomybės ribos. "
             "Data paprastai rezervuojama avansu — tai standartinė renginių rinkos praktika.</p>"
             "<p>Verta iš anksto aptarti ir <strong>plano B</strong>: kas bus, jei renginys keliamas, "
             "jei lauko renginį sugadins lietus arba jei pasikeis salė. Gera nuomos įmonė turi atsakymus "
             "į visus tris klausimus.</p>"),
            ("Žingsnis 4: pasiruošimas renginio dienai",
             "<p>Iš jūsų pusės reikia nedaug, bet tai turi būti sutvarkyta iš anksto:</p>"
             "<ul>"
             "<li><strong>230 V lizdas</strong> netoli roboto zonos.</li>"
             "<li><strong>2×2 m laisvos erdvės</strong> (didesnei choreografijai — daugiau).</li>"
             "<li><strong>Prieiga</strong> likus 45 minutėms iki pirmo pasirodymo.</li>"
             "<li><strong>Kontaktinis asmuo</strong> vietoje, kuris žino programos grafiką.</li>"
             "<li><strong>Ryšys su garso technikais</strong>, jei robotas pasirodo scenoje.</li>"
             "</ul>"
             "<p>Visa kita — atvykimas, paruošimas, valdymas, išardymas — yra nuomos įmonės "
             "atsakomybė.</p>"),
            ("Žingsnis 5: išnaudokite renginį iki galo",
             "<p>Dažna klaida — robotas užsakomas, pasirodo, ir tuo viskas baigiasi. Tuo tarpu didžiausia "
             "vertė dažnai sukuriama <strong>po renginio</strong>: įrašai socialiniams tinklams, "
             "nuotraukos svečiams, medžiaga ataskaitai rėmėjams.</p>"
             "<p>Susitarkite iš anksto, kas filmuos, ir suplanuokite bent vieną kadrą, kurį tikrai "
             "norite turėti. Konkretų kainų paaiškinimą rasite straipsnyje "
             "<a href=\"blog-kiek-kainuoja-roboto-nuoma.html\">kiek kainuoja roboto nuoma</a>, o "
             "paketų turinį — <a href=\"kainos.html\">kainų puslapyje</a>.</p>"),
        ],
        faq=[
            ("Kiek iš anksto reikia rezervuoti robotą?",
             "Sezono metu (rugsėjis–gruodis, gegužė–birželis) rekomenduojame 3–4 savaites. Ne sezono "
             "metu dažnai pavyksta suderinti ir per kelias dienas."),
            ("Ar galiu robotą išsinuomoti be operatoriaus?",
             "Ne. Operatorius yra privaloma paslaugos dalis — tai saugumo ir įrangos apsaugos klausimas, "
             "o kartu ir garantija, kad pasirodymas pavyks."),
            ("Ar reikia specialių leidimų renginiui su robotu?",
             "Uždarose patalpose paprastai ne. Viešose erdvėse ir prekybos centruose gali reikėti "
             "administracijos suderinimo — visą techninę informaciją pateikiame dokumentu."),
            ("Kas atsitiks, jei robotas suges renginio metu?",
             "Operatorius turi atsarginę įrangą svarbiausioms dalims ir žino, kaip greitai atkurti darbą. "
             "Sutartyje taip pat numatome, kaip elgiamės, jei pasirodymas neįvyktų dėl techninių priežasčių."),
        ],
        related=[("humanoidinio-roboto-nuoma.html", "Nuomos sąlygos"),
                 ("blog-kiek-kainuoja-roboto-nuoma.html", "Kainos"),
                 ("kainos.html", "Kas įeina į kainą")],
    ),
    dict(
        slug="blog-robotas-ar-kitos-pramogos.html",
        title="Renginio pramoga: robotas ar kitos galimybės? Palyginimas",
        desc="Robotas, fokusnininkas, VR zona, fotobūdelė ar gyva muzika — palyginimas pagal WOW efektą, "
             "soc. tinklų pasiekiamumą ir verslo vertę.",
        keywords="renginio pramoga, renginių pramogos, atrakcija renginiui, fotobūdelė ar robotas, VR zona",
        tag="Pramogos · Palyginimas",
        card="Populiariausių renginių pramogų palyginimas pagal WOW efektą, socialinių tinklų "
             "pasiekiamumą ir verslo vertę.",
        h1="Renginio pramoga:<br />robotas ar kitos<br /><em>galimybės?</em>",
        lead="Biudžetas ribotas, o pasirinkimų daug. Sąžiningas palyginimas — kada robotas yra geriausias "
             "sprendimas, o kada verta rinktis ką kita.",
        published="2026-06-08", modified="2026-07-19",
        sections=[
            ("Palyginimo lentelė",
             "<div class=\"data-table-wrap\">"
             "<table class=\"data-table\">"
             "<thead><tr><th>Pramoga</th><th>WOW efektas</th><th>Turinys soc. tinklams</th>"
             "<th>Verslo vertė</th><th>Kam tinka</th></tr></thead>"
             "<tbody>"
             "<tr><td><strong>Humanoidinis robotas</strong></td><td>Labai aukštas</td><td>Labai aukštas</td>"
             "<td>Aukšta — kontaktai, prekės ženklo signalas</td><td>B2B renginiai, parodos, "
             "konferencijos</td></tr>"
             "<tr><td>Fotobūdelė</td><td>Žemas</td><td>Vidutinis</td><td>Žema</td><td>Vestuvės, "
             "neformalios šventės</td></tr>"
             "<tr><td>VR zona</td><td>Vidutinis</td><td>Žemas (sunku filmuoti)</td><td>Vidutinė</td>"
             "<td>Technologijų renginiai, jauna auditorija</td></tr>"
             "<tr><td>Fokusnininkas</td><td>Vidutinis</td><td>Žemas</td><td>Žema</td><td>Vakarienės, "
             "mažesnės grupės</td></tr>"
             "<tr><td>Gyva muzika</td><td>Vidutinis</td><td>Žemas</td><td>Žema — kuria atmosferą</td>"
             "<td>Vakariniai renginiai, gala</td></tr>"
             "<tr><td>Karikatūristas</td><td>Žemas</td><td>Vidutinis</td><td>Žema</td><td>Ilgesni "
             "renginiai su laukimo zonomis</td></tr>"
             "</tbody></table></div>"
             "<p>Lentelė supaprastinta sąmoningai. Realybėje viskas priklauso nuo tikslo — todėl toliau "
             "apie tai detaliau.</p>"),
            ("Kada robotas yra geriausias pasirinkimas",
             "<p>Robotas laimi, kai renginio tikslas yra <strong>dėmesys ir turinys</strong>. Tai reiškia "
             "parodas, kur reikia sustabdyti srautą; konferencijas, kur reikia programos akcento; "
             "atidarymus, kur reikia pritraukti praeivius; ir B2B renginius, kur svarbus inovatyvumo "
             "įvaizdis.</p>"
             "<p>Robotas taip pat laimi, kai svarbu, kad renginys būtų <strong>prisimenamas</strong>. "
             "Lietuvoje humanoidas vis dar retenybė — daugumai svečių tai pirmas kartas gyvai. "
             "Fotobūdelė ar fokusnininkas tokio efekto nebeduoda, nes juos visi matė.</p>"),
            ("Kada verta rinktis ką kita",
             "<p>Būkime sąžiningi — robotas nėra atsakymas į viską:</p>"
             "<ul>"
             "<li><strong>Jei tikslas — šokių aikštelė visą naktį</strong>, geras DJ padarys daugiau nei "
             "robotas.</li>"
             "<li><strong>Jei renginys labai mažas</strong> (iki 30 žmonių uždaroje patalpoje), efektas "
             "gali neatpirkti investicijos.</li>"
             "<li><strong>Jei svarbiausia svečiams išsinešti fizinį suvenyrą</strong>, karikatūristas ar "
             "spausdinama fotobūdelė gali tikti geriau.</li>"
             "<li><strong>Jei biudžetas labai ribotas</strong> ir renginys neturi rinkodaros tikslo, "
             "pramoga gali būti paprastesnė.</li>"
             "</ul>"
             "<p>Dažniausias praktinis sprendimas — <strong>derinys</strong>: robotas kaip pagrindinis "
             "akcentas plius muzika atmosferai. Tada renginys turi ir įsimenamą momentą, ir gerą foną.</p>"),
            ("Kaip vertinti grąžą",
             "<p>Renginio pramogos vertę verta matuoti ne emocijomis, o keliais paprastais rodikliais: "
             "kiek kontaktų surinkta, kiek įrašų apie renginį pasirodė socialiniuose tinkluose, kiek "
             "žmonių sustojo prie stendo ir kiek laiko praleido.</p>"
             "<p>Humanoidinio roboto atveju šiuos rodiklius lengva sekti — QR kodo nuskaitymai matomi "
             "analitikoje, o įrašai su robotu paprastai lengvai atpažįstami. Apie mechanikas rašėme "
             "straipsnyje <a href=\"blog-robotas-parodu-stende.html\">robotas parodų stende</a>.</p>"),
        ],
        faq=[
            ("Ar galima derinti robotą su kitomis pramogomis?",
             "Taip, ir dažniausiai taip ir daroma. Robotas duoda WOW momentą ir turinį, o muzika ar "
             "maistas kuria bendrą renginio atmosferą — jie nekonkuruoja."),
            ("Ar robotas nenustelbs pagrindinio renginio turinio?",
             "Ne, jei pasirodymai suplanuoti. Todėl dirbame ciklais ir derinam grafiką su renginio "
             "programa — robotas sustiprina programą, o ne konkuruoja su ja."),
            ("Kuri pramoga duoda daugiausia socialinių tinklų pasiekiamumo?",
             "Iš mūsų patirties — humanoidinis robotas su aiškiu ženklinimu. Svarbu, kad logotipas būtų "
             "matomas kadre, nes tada kiekvienas svečio įrašas dirba jūsų prekės ženklui."),
        ],
        related=[("robotas-renginiui.html", "Robotas renginiui"),
                 ("blog-kodel-robotas-renginyje.html", "Kodėl robotas renginyje"),
                 ("kainos.html", "Kainos")],
    ),
    dict(
        slug="blog-humanoidinis-ar-mobilus-robotas.html",
        title="Humanoidinis ar mobilus robotas renginiui — ką rinktis?",
        desc="Humanoidas, mobilus robotas ar interaktyvus kioskas? Palyginimas pagal poveikį svečiams, "
             "logistiką, kainą ir pritaikymo scenarijus renginiuose.",
        keywords="humanoidinis robotas, mobilus robotas, interaktyvus kioskas, robotų tipai renginiams",
        tag="Robotų tipai",
        card="Kodėl humanoidinis robotas daro didesnį įspūdį nei mobilus robotas ar interaktyvus kioskas? "
             "Palyginimas ir patarimai prieš nuomą.",
        h1="Humanoidinis ar<br />mobilus robotas —<br /><em>ką rinktis?</em>",
        lead="Ne kiekvienas robotas veikia vienodai. Skirtumas tarp humanoido ir mobilios platformos "
             "renginyje yra didesnis, nei atrodo iš specifikacijų.",
        published="2026-06-20", modified="2026-07-21",
        sections=[
            ("Trys robotų klasės renginiuose",
             "<p><strong>Humanoidiniai robotai</strong> — žmogaus formos, vaikšto ant dviejų kojų, turi "
             "rankas ir galvą. Pavyzdys: Unitree G1. Stiprybė — emocinis poveikis ir bendravimas su "
             "žmonėmis.</p>"
             "<p><strong>Mobilūs robotai</strong> — platformos ant ratų, dažnai su ekranu. Stiprybė — "
             "stabilumas, ilgas veikimo laikas, gebėjimas vežti daiktus (pvz. gėrimus).</p>"
             "<p><strong>Interaktyvūs kioskai</strong> — statiški ekranai su sąsaja. Stiprybė — "
             "paprastumas ir kaina, bet tai nėra robotas visa to žodžio prasme.</p>"),
            ("Kodėl humanoidas veikia stipriau",
             "<p>Priežastis psichologinė. Žmogaus smegenys reaguoja į <strong>žmogaus formą ir "
             "judesį</strong> visiškai kitaip nei į mašiną ant ratų. Humanoidas, kuris pasisveikina "
             "ranka ir nusilenkia, sukelia socialinę reakciją — žmonės jam šypsosi, sveikinasi atgal ir "
             "nori nusifotografuoti.</p>"
             "<p>Mobilus robotas su ekranu sukelia susidomėjimą, bet ne tą patį emocinį atsaką. "
             "Praktikoje tai matosi paprastai: prie humanoido susidaro eilė nuotraukoms, prie mobilios "
             "platformos — ne.</p>"),
            ("Kada mobilus robotas yra geresnis",
             "<p>Būtų nesąžininga sakyti, kad humanoidas visada laimi. Mobilus robotas geresnis, kai:</p>"
             "<ul>"
             "<li>Reikia <strong>vežioti daiktus</strong> — gėrimus, dalomąją medžiagą, prizus.</li>"
             "<li>Renginys trunka <strong>labai ilgai be pertraukų</strong> ir svarbus ištvermės "
             "rodiklis.</li>"
             "<li>Erdvė yra <strong>labai didelė</strong> ir reikia nuolatinio judėjimo dideliais "
             "atstumais.</li>"
             "<li>Biudžetas <strong>griežtai ribotas</strong>, o užtenka technologijos akcento.</li>"
             "</ul>"
             "<p>Taip pat verta žinoti, kad mobilios platformos dažnai lengviau derinamos viešose "
             "erdvėse, nes jų judesys nuspėjamesnis.</p>"),
            ("Praktinis pasirinkimo kriterijus",
             "<p>Paprastas klausimas, kuris beveik visada duoda atsakymą: <strong>ar norite, kad žmonės "
             "fotografuotųsi su robotu?</strong></p>"
             "<p>Jei taip — reikia humanoido. Nuotrauka su žmogaus formos robotu yra turinys, kurį žmonės "
             "skelbia savo profiliuose. Nuotrauka su platforma ant ratų — ne.</p>"
             "<p>Jei pagrindinis tikslas yra funkcija (vežimas, informacijos rodymas, navigacija), "
             "mobilus robotas gali būti racionalesnis. Detalią Unitree G1 specifikaciją rasite "
             "<a href=\"blog-unitree-g1-specifikacija.html\">atskirame straipsnyje</a>.</p>"),
        ],
        faq=[
            ("Ar humanoidinis robotas sudėtingesnis logistiškai?",
             "Šiek tiek — reikia lygaus paviršiaus ir saugios zonos. Bet Unitree G1 sveria tik apie "
             "35 kg ir telpa į įprastą automobilį, todėl transportavimas nėra problema."),
            ("Ar galima renginyje turėti abu tipus?",
             "Taip, didesniuose projektuose tai pasitaiko: humanoidas dirba kaip pramogos akcentas, o "
             "mobili platforma atlieka funkcinę užduotį."),
            ("Kuris variantas brangesnis?",
             "Humanoidų nuoma paprastai kainuoja daugiau dėl įrangos vertės ir būtino operatoriaus. "
             "Bet vertinant pagal sukurtą dėmesį ir turinį, kaina už rezultatą dažnai būna palankesnė."),
        ],
        related=[("blog-unitree-g1-specifikacija.html", "Unitree G1 specifikacija"),
                 ("humanoidinio-roboto-nuoma.html", "Nuomos sąlygos"),
                 ("robotas-renginiui.html", "Robotas renginiui")],
    ),
    dict(
        slug="blog-roboto-sauga-renginyje.html",
        title="Roboto sauga renginyje — ką turi žinoti organizatorius",
        desc="Jutikliai, saugos zona, draudimas ir operatoriaus vaidmuo. Praktinis saugos vadovas "
             "renginių organizatoriams, planuojantiems humanoidinį robotą.",
        keywords="roboto sauga, robotas renginyje sauga, draudimas robotas, saugos zona robotui",
        tag="Sauga · Organizatoriams",
        card="Jutikliai, draudimas, saugos zona ir operatoriaus vaidmuo. Praktinis saugos vadovas "
             "renginių organizatoriams.",
        h1="Roboto sauga renginyje —<br />ką turi žinoti<br /><em>organizatorius.</em>",
        lead="Klausimas, kurį anksčiau ar vėliau užduoda kiekvienas organizatorius ir kiekvienas salės "
             "administratorius. Atsakymas — konkretus ir dokumentuojamas.",
        published="2026-07-04", modified="2026-07-25",
        sections=[
            ("Kaip robotas „mato\" žmones",
             "<p>Unitree G1 naudoja <strong>LiDAR jutiklius ir kompiuterinę regą</strong>. Praktiškai tai "
             "reiškia, kad robotas realiu laiku kuria aplinkos vaizdą ir aptinka kliūtis bei žmones dar "
             "prieš prisiliesdamas. Judant minioje tai yra pagrindinė apsaugos linija.</p>"
             "<p>Antra linija — <strong>operatorius</strong>, kuris visą laiką mato robotą ir gali "
             "nedelsdamas sustabdyti judesį. Renginiuose niekada nenaudojame pilnai autonominio režimo "
             "be priežiūros: kiekvieną pasirodymą prižiūri žmogus.</p>"),
            ("Saugos zona ir erdvės planavimas",
             "<p>Standartinis reikalavimas — <strong>2×2 m laisvos erdvės</strong> pasirodymui, o "
             "aktyvesnei choreografijai patogiau turėti 4×4 m. Zona turi būti lygi, sausa ir be laidų "
             "ant grindų.</p>"
             "<ul>"
             "<li>Vengiame laiptų ir staigių lygio pokyčių pasirodymo zonoje.</li>"
             "<li>Šlapias ar labai slidus paviršius — netinka.</li>"
             "<li>Prie roboto neturi būti atviros ugnies ar nestabilios dekoracijos.</li>"
             "<li>Nuotraukų metu operatorius nurodo saugų atstumą ir prižiūri eilę.</li>"
             "</ul>"
             "<div class=\"callout\"><p>Praktikoje didžiausia rizika nėra robotas — tai susijaudinę "
             "žmonės, kurie staiga prieina iš nugaros. Todėl operatorius visada valdo ne tik robotą, bet "
             "ir aplink esančią minią.</p></div>"),
            ("Draudimas ir dokumentai",
             "<p>Mūsų veiklai taikoma <strong>civilinės atsakomybės draudimo apsauga</strong>. Salėms, "
             "prekybos centrams ir parodų organizatoriams pateikiame techninę informaciją apie įrangą, "
             "galios poreikį ir saugos priemones — dokumentą galite persiųsti savo objekto "
             "administracijai.</p>"
             "<p>Jei objektas turi savo reikalavimus (pvz. rizikos vertinimo formą ar įrangos sertifikatų "
             "kopijas), tiesiog praneškite iš anksto — tokius prašymus gauname reguliariai ir turime "
             "paruoštus atsakymus.</p>"),
            ("Vaikai, minios ir specifinės situacijos",
             "<p>Robotas puikiai veikia renginiuose su vaikais — būtent jie reaguoja stipriausiai. Bet "
             "tokiuose renginiuose operatorius dirba griežčiau: aiškiai apibrėžia zoną, o nuotraukas "
             "organizuoja eilėje, o ne chaotiškai.</p>"
             "<p>Didelėse miniose (prekybos centrų atidarymai, festivaliai) rekomenduojame fizinį zonos "
             "žymėjimą — juostelę arba stovus. Tai kainuoja nedaug, bet leidžia robotui dirbti sklandžiai "
             "ir be pertrūkių.</p>"
             "<p>Turite specifinį scenarijų? Aptarkime jį iš anksto — "
             "<a href=\"kontaktai.html\">susisiekite</a>, ir paruošime saugos planą būtent jūsų vietai.</p>"),
        ],
        faq=[
            ("Ar robotas gali atsitrenkti į žmogų?",
             "Jutikliai aptinka žmones realiu laiku, o operatorius bet kada gali sustabdyti judesį. "
             "Būtent dėl šio dvigubo saugumo lygio robotas gali dirbti tiesiai minioje."),
            ("Ar reikia atskiro draudimo iš renginio organizatoriaus pusės?",
             "Ne — mūsų veikla apdrausta civilinės atsakomybės draudimu. Jei objektas prašo papildomų "
             "dokumentų, pateikiame juos iš anksto."),
            ("Ar robotas saugus vaikams?",
             "Taip, ir vaikų renginiuose dirbame dažnai. Skirtumas tik organizacinis: aiškiai pažymėta "
             "zona ir nuotraukos eilės tvarka."),
            ("Ką daryti, jei salė turi savo saugos reikalavimus?",
             "Praneškite apie juos užklausos metu. Pateikiame techninę specifikaciją, galios poreikį ir "
             "saugos priemonių aprašą, kurį galima pridėti prie objekto dokumentų."),
        ],
        related=[("humanoidinio-roboto-nuoma.html", "Nuomos sąlygos"),
                 ("kontaktai.html", "Kontaktai"),
                 ("robotas-renginiui.html", "Robotas renginiui")],
    ),
]
