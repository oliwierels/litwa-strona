# -*- coding: utf-8 -*-
"""33bots.lt miestų puslapiai — lokalus SEO."""
from lt_gallery import strip_section
from lt_common import (SITE, head, body_open, nav, crumbs, breadcrumb_ld, contact_section,
                       footer, faq_section, faq_ld, organization_ld, video_section,
                       write, esc, CITIES, city_url)

# slug -> (regionas, erdvių pavyzdžiai, unikalus intro, vietos scenos aprašymas)
CITY_DATA = {
    "vilnius": dict(
        region="Vilniaus apskritis",
        venues=["LITEXPO parodų ir kongresų centras", "Menų fabrikas „Loftas“", "Vilniaus verslo centrai Konstitucijos pr.",
                "viešbučių konferencijų salės senamiestyje", "prekybos centrų atriumai"],
        intro="Vilnius yra didžiausia renginių rinka Lietuvoje — čia vyksta daugiausia tarptautinių "
              "konferencijų, technologijų renginių ir parodų. Kartu tai rinka, kurioje sunkiausia "
              "išsiskirti: sostinės auditorija mato daugiausia ir nustemba mažiausiai.",
        scene="Sostinėje humanoidinis robotas dažniausiai užsakomas technologijų konferencijoms, "
              "startuolių renginiams, bankų ir draudimo bendrovių klientų vakarams bei parodoms "
              "LITEXPO. Antra didelė kategorija — įmonių šventės biurų kvartaluose ir prekybos centrų "
              "atidarymai.",
        extra="Vilniuje dažnai dirbame su renginių agentūromis, kurioms svarbu, kad tiekėjas pats "
              "pateiktų techninę specifikaciją, saugos informaciją ir suderintų viską su objekto "
              "administracija. Visą tai atliekame be papildomų prašymų."),
    "kaunas": dict(
        region="Kauno apskritis",
        venues=["Žalgirio arena", "Kauno kultūros ir konferencijų erdvės", "Kauno LEZ ir pramonės "
                "parkų teritorijos", "universitetų auditorijos", "prekybos centrų atriumai"],
        intro="Kaunas — pramonės, inžinerijos ir studentų miestas, todėl čia robotas dažnai turi ne tik "
              "pramoginį, bet ir technologinį kontekstą. Auditorija linkusi klausti, kaip robotas veikia, "
              "o ne tik fotografuotis.",
        scene="Kaune populiariausi scenarijai — gamybos ir logistikos įmonių renginiai, universitetų "
              "atvirų durų dienos, inžinerinių bendrovių jubiliejai ir technologijų konferencijos. "
              "Studentiškuose renginiuose robotas veikia ypač stipriai.",
        extra="Kauno pramonės įmonėms dažnai svarbu, kad robotą būtų galima pristatyti ir gamyklos "
              "teritorijoje ar sandėlio erdvėje. Tokie scenarijai mums įprasti — svarbu tik lygus "
              "paviršius ir elektros prieiga."),
    "klaipeda": dict(
        region="Klaipėdos apskritis",
        venues=["Švyturio arena", "Klaipėdos kultūrų fabrikas", "uosto ir logistikos įmonių teritorijos",
                "kurortinių viešbučių konferencijų salės", "prekybos centrai"],
        intro="Klaipėda gyvena uosto, logistikos ir vasaros sezono ritmu. Renginių čia daugiausia "
              "gegužę–rugsėjį, o žiemą dominuoja verslo ir uosto sektoriaus formatai.",
        scene="Uostamiestyje robotas dažniausiai reikalingas logistikos ir jūrinio verslo įmonių "
              "renginiams, kruizinio sezono atidarymams, prekybos centrų akcijoms ir vasaros festivalių "
              "zonoms. Neretai vienas užsakymas apima Klaipėdą ir Palangą tą patį savaitgalį.",
        extra="Pajūryje verta iš anksto numatyti atsarginį planą lietaus atveju — robotas puikiai dirba "
              "lauke sausu oru, bet stipriam vėjui ir lietui reikia stogelio arba vidaus alternatyvos."),
    "siauliai": dict(
        region="Šiaulių apskritis",
        venues=["Šiaulių arena", "kultūros centrų salės", "pramonės įmonių teritorijos",
                "prekybos centrų atriumai", "universiteto erdvės"],
        intro="Šiauliai — stiprus pramonės ir logistikos regionas, kuriame renginių pramogų pasirinkimas "
              "vis dar siauresnis nei sostinėje. Būtent todėl humanoidinis robotas čia daro dar didesnį "
              "įspūdį.",
        scene="Šiauliuose populiariausi užsakymai — gamybos įmonių šventės, miesto renginiai, prekybos "
              "centrų atidarymai ir mokyklų bei universiteto technologijų dienos.",
        extra="Regione dažnai užsakoma visos dienos nuoma, nes renginiai vyksta bangomis — svečiai "
              "renkasi per kelias valandas. Tokiu atveju dirbame ciklais: trumpas pasirodymas kas "
              "valandą ir nuotraukų zona tarp jų."),
    "panevezys": dict(
        region="Panevėžio apskritis",
        venues=["Cido arena", "kultūros ir konferencijų centrai", "pramonės parkų teritorijos",
                "prekybos centrai", "miesto aikštės renginiams"],
        intro="Panevėžys yra vienas stipriausių Lietuvos gamybos centrų. Įmonių renginiai čia dažnai "
              "orientuoti į darbuotojus — o robotas yra pramoga, kuri veikia visose amžiaus grupėse ir "
              "visuose skyriuose.",
        scene="Dažniausi formatai — gamybos įmonių vasaros šventės ir jubiliejai, miesto renginiai, "
              "profesinio orientavimo dienos ir prekybos centrų akcijos.",
        extra="Gamybos įmonėms dažnai svarbus employer branding aspektas: įrašai iš šventės su robotu "
              "naudojami darbuotojų paieškos kampanijose. Ženklinimą jūsų logotipu darome be priemokų."),
    "alytus": dict(
        region="Alytaus apskritis",
        venues=["Alytaus kultūros ir komunikacijos erdvės", "pramonės parko teritorijos",
                "miesto aikštės", "mokyklų ir gimnazijų salės", "prekybos centrai"],
        intro="Alytus — Dzūkijos sostinė su aktyvia bendruomenine renginių scena. Miesto ir mokyklų "
              "renginiai čia sutraukia didelę dalį gyventojų, todėl pramogos poveikis pastebimas iš karto.",
        scene="Alytuje robotas dažniausiai užsakomas miesto šventėms, mokyklų ir gimnazijų renginiams, "
              "įmonių jubiliejams bei prekybos centrų akcijoms.",
        extra="Bendruomeniniuose renginiuose rekomenduojame numatyti pažymėtą zoną — susidomėjimas "
              "būna didelis, o aiški tvarka leidžia visiems spėti nusifotografuoti."),
    "marijampole": dict(
        region="Marijampolės apskritis",
        venues=["Marijampolės kultūros centras", "verslo ir logistikos parkų teritorijos",
                "miesto aikštės", "mokymo įstaigų salės", "prekybos centrai"],
        intro="Marijampolė yra svarbus logistikos ir žemės ūkio verslo mazgas pakeliui į Lenkijos sieną. "
              "Renginių scena čia praktiška — vertinamas konkretus rezultatas, o ne efektas dėl efekto.",
        scene="Populiariausi scenarijai — logistikos ir žemės ūkio įmonių renginiai, miesto šventės, "
              "profesinio mokymo įstaigų karjeros dienos.",
        extra="Marijampolė yra patogioje vietoje maršrute iš Lenkijos, todėl čia dažnai suderiname "
              "užsakymus su kitais tos pačios savaitės renginiais — bet kaina dėl to nesikeičia."),
    "mazeikiai": dict(
        region="Telšių apskritis",
        venues=["Mažeikių kultūros centras", "pramonės įmonių teritorijos", "miesto aikštės",
                "mokyklų salės", "prekybos centrai"],
        intro="Mažeikiai — pramoninis Šiaurės Lietuvos miestas, kur didelės įmonės rengia dideles "
              "darbuotojų šventes. Tokiuose renginiuose robotas tampa pagrindiniu vakaro akcentu.",
        scene="Dažniausi užsakymai — pramonės įmonių šventės ir jubiliejai, miesto renginiai, mokyklų "
              "technologijų dienos.",
        extra="Mažeikiai toli nuo sostinės, bet tai nėra kliūtis — dirbame visoje Lietuvoje. "
              "Atvykimo kainą įvertiname pagal vietą ir nurodome pasiūlyme kartu su nuomos kaina."),
    "jonava": dict(
        region="Kauno apskritis",
        venues=["Jonavos kultūros centras", "pramonės įmonių teritorijos", "miesto viešosios erdvės",
                "mokyklų salės", "prekybos centrai"],
        intro="Jonava — chemijos pramonės ir jaunų šeimų miestas netoli Kauno. Renginiai čia dažnai "
              "orientuoti į šeimas, o tai formatas, kuriame robotas veikia patikimiausiai.",
        scene="Populiariausi formatai — miesto ir bendruomenių šventės, įmonių renginiai darbuotojų "
              "šeimoms, mokyklų renginiai.",
        extra="Šeimų renginiuose planuojame trumpesnius, bet dažnesnius pasirodymus — vaikų dėmesys "
              "trumpesnis, o eilė nuotraukoms susidaro greitai."),
    "utena": dict(
        region="Utenos apskritis",
        venues=["Utenos kultūros centras", "pramonės įmonių teritorijos", "Aukštaitijos gamtos "
                "erdvių renginių vietos", "mokyklų salės", "prekybos centrai"],
        intro="Utena yra Aukštaitijos regiono centras su stipria gamybos tradicija ir aktyviu vasaros "
              "renginių sezonu prie ežerų.",
        scene="Utenoje robotas dažniausiai užsakomas įmonių vasaros šventėms, miesto renginiams ir "
              "mokymo įstaigų technologijų dienoms.",
        extra="Sodybų ir lauko renginių atveju svarbiausia elektros prieiga ir lygus paviršius "
              "pasirodymui — visa kita išsprendžiama vietoje."),
    "kedainiai": dict(
        region="Kauno apskritis",
        venues=["Kėdainių kultūros centras", "chemijos ir žemės ūkio įmonių teritorijos",
                "senamiesčio erdvės", "mokyklų salės", "prekybos centrai"],
        intro="Kėdainiai derina istorinį senamiestį su stipria pramone — todėl čia vyksta ir "
              "reprezentaciniai miesto renginiai, ir dideli įmonių vakarai.",
        scene="Dažniausi scenarijai — pramonės įmonių šventės, miesto renginiai senamiestyje ir "
              "mokyklų karjeros dienos.",
        extra="Renginiams istorinėse erdvėse iš anksto suderiname zoną su objekto administracija — "
              "robotui reikia lygaus paviršiaus, o senamiesčio grindinys ne visada tinka pasirodymui."),
    "telsiai": dict(
        region="Telšių apskritis",
        venues=["Telšių kultūros ir meno erdvės", "Žemaitijos regiono renginių vietos",
                "pramonės įmonių teritorijos", "mokyklų salės", "prekybos centrai"],
        intro="Telšiai — Žemaitijos sostinė su stipria kultūros ir meno scena. Renginiai čia dažnai turi "
              "regioninio identiteto akcentą, į kurį robotą galima įpinti kaip kontrastą.",
        scene="Populiariausi užsakymai — miesto ir regiono šventės, meno bei kultūros renginiai, įmonių "
              "vakarai ir mokyklų technologijų dienos.",
        extra="Kultūros renginiuose robotas dažnai naudojamas kaip kontrastas tradicijai — būtent šis "
              "sugretinimas sukuria stipriausią vaizdinę istoriją."),
    "taurage": dict(
        region="Tauragės apskritis",
        venues=["Tauragės kultūros centras", "logistikos ir gamybos įmonių teritorijos",
                "miesto aikštės", "mokyklų salės", "prekybos centrai"],
        intro="Tauragė yra svarbus logistikos taškas maršrute tarp Klaipėdos ir Kauno. Verslo renginiai "
              "čia praktiški, o miesto šventės sutraukia didelę bendruomenės dalį.",
        scene="Dažniausi formatai — logistikos ir gamybos įmonių renginiai, miesto šventės, profesinio "
              "mokymo įstaigų karjeros dienos.",
        extra="Tauragė patogi kaip tarpinis taškas kelionėje į pajūrį — dažnai vienas išvykimas apima "
              "kelis regiono renginius, tačiau tai neturi jokios įtakos jūsų kainai."),
    "palanga": dict(
        region="Klaipėdos apskritis",
        venues=["kurortinių viešbučių konferencijų salės", "Palangos koncertų ir renginių erdvės",
                "vasaros terasos ir lauko scenos", "Basanavičiaus gatvės zona", "SPA kompleksai"],
        intro="Palanga vasarą tampa Lietuvos renginių sostine — čia vyksta įmonių išvažiuojamieji "
              "renginiai, konferencijos prie jūros ir vestuvės. Konkurencija dėl svečių dėmesio čia "
              "didžiausia šalyje.",
        scene="Kurorte robotas dažniausiai užsakomas įmonių išvažiuojamosioms sesijoms, viešbučių "
              "renginiams, vestuvėms ir vasaros kampanijų aktyvacijoms.",
        extra="Vasaros sezonu Palangos savaitgaliai užsipildo anksčiausiai visoje Lietuvoje — dėl "
              "birželio–rugpjūčio datų rekomenduojame kreiptis bent 2–3 mėnesius iš anksto."),
    "druskininkai": dict(
        region="Alytaus apskritis",
        venues=["SPA ir sveikatingumo kompleksų konferencijų salės", "Snow Arena erdvės",
                "viešbučių renginių salės", "kurorto lauko erdvės", "vandens parko zona"],
        intro="Druskininkai yra pagrindinis Lietuvos konferencinio turizmo kurortas — čia įmonės "
              "išvažiuoja dviem dienoms, sujungdamos darbo sesijas ir vakaro programą.",
        scene="Kurorte robotas dažniausiai reikalingas dviejų dienų įmonių renginiams: darbo sesijai "
              "dieną ir vakaro programai su pramoga. Antra kategorija — vestuvės ir šeimų šventės.",
        extra="Dviejų dienų formatams siūlome paketą su tuo pačiu operatoriumi abiem dienoms — tai "
              "pigiau ir logistiškai paprasčiau nei du atskiri užsakymai."),
    "trakai": dict(
        region="Vilniaus apskritis",
        venues=["Trakų pilies prieigų renginių erdvės", "ežerų pakrančių viešbučiai ir sodybos",
                "konferencijų centrai prie Galvės", "lauko scenos", "restoranų terasos"],
        intro="Trakai yra populiariausia vieta netoli Vilniaus, kur įmonės rengia išvažiuojamuosius "
              "renginius, o poros — vestuves. Vaizdinga aplinka reiškia, kad kiekvienas kadras čia "
              "atrodo geriau.",
        scene="Trakuose robotas dažniausiai užsakomas įmonių išvažiuojamiesiems renginiams, vestuvėms "
              "prie ežero ir turizmo sektoriaus aktyvacijoms.",
        extra="Sodybose ir prie ežerų svarbiausia patikrinti elektros prieigą ir paviršių — mediniai "
              "pontonai ir netolygus grindinys pasirodymui netinka, todėl zoną parenkame kartu iš anksto."),
    "visaginas": dict(
        region="Utenos apskritis",
        venues=["Visagino kultūros centras", "energetikos sektoriaus įmonių erdvės",
                "miesto aikštės", "mokyklų salės", "Visagino pramonės parkas"],
        intro="Visaginas — jauniausias Lietuvos miestas su technine, energetikos sektoriaus "
              "bendruomene. Auditorija čia techniškai raštinga: apie robotą klausiama konkrečiai, "
              "o ne tik fotografuojamasi.",
        scene="Visagine robotas dažniausiai užsakomas energetikos ir pramonės įmonių renginiams, "
              "miesto šventėms bei mokyklų technologijų dienoms.",
        extra="Techninėje aplinkoje operatorius skiria daugiau laiko paaiškinimams — jutikliams, "
              "valdymui, judėjimo principui. Tai dažnai vertinama labiau nei pats pasirodymas."),
    "ukmerge": dict(
        region="Vilniaus apskritis",
        venues=["Ukmergės kultūros centras", "pramonės įmonių teritorijos", "miesto viešosios erdvės",
                "mokyklų salės", "prekybos centrai"],
        intro="Ukmergė yra patogioje vietoje tarp Vilniaus ir Panevėžio, todėl čia rengiami tiek "
              "vietos bendruomenės, tiek regioninio masto renginiai.",
        scene="Populiariausi formatai — įmonių šventės, miesto renginiai ir mokyklų bei gimnazijų "
              "technologijų dienos.",
        extra="Patogi vieta prie magistralės reiškia, kad renginiai Ukmergėje logistiškai paprasti — "
              "o atvykimo kainą visada nurodome pasiūlyme."),
    "plunge": dict(
        region="Telšių apskritis",
        venues=["Plungės kultūros centras", "Oginskių dvaro parko erdvės", "gamybos įmonių teritorijos",
                "mokyklų salės", "miesto aikštės"],
        intro="Plungė — Žemaitijos miestas su stipria kultūros tradicija ir gamybos sektoriumi. "
              "Renginiai čia dažnai vyksta istorinėse erdvėse arba jų prieigose.",
        scene="Dažniausi užsakymai — miesto šventės, gamybos įmonių renginiai ir kultūros programos, "
              "kuriose robotas veikia kaip kontrastas tradicijai.",
        extra="Istorinėse erdvėse pasirodymo zoną derinam su objekto administracija iš anksto — "
              "robotui reikia lygaus paviršiaus, o senas grindinys ne visada tinka."),
    "kretinga": dict(
        region="Klaipėdos apskritis",
        venues=["Kretingos kultūros centras", "dvaro ir muziejaus erdvės", "gamybos įmonių teritorijos",
                "mokyklų salės", "miesto aikštės"],
        intro="Kretinga yra pajūrio regiono dalis, todėl vasarą čia jaučiamas kurortinis ritmas, o "
              "likusią metų dalį dominuoja vietos verslo ir bendruomenės renginiai.",
        scene="Populiariausi scenarijai — miesto šventės, įmonių renginiai ir mokyklų programos. "
              "Vasarą užsakymai dažnai derinami su Palanga tą patį savaitgalį.",
        extra="Kadangi Kretinga netoli pajūrio, lauko renginiams verta numatyti atsarginį planą "
              "vėjuotam ar lietingam orui."),
    "silute": dict(
        region="Klaipėdos apskritis",
        venues=["Šilutės kultūros ir pramogų centras", "žemės ūkio verslo teritorijos",
                "Nemuno deltos regiono renginių vietos", "mokyklų salės", "miesto aikštės"],
        intro="Šilutė — Nemuno deltos krašto centras su žemės ūkio ir maisto pramonės verslu. "
              "Renginių scena praktiška, orientuota į bendruomenę ir vietos įmones.",
        scene="Dažniausi formatai — žemės ūkio ir maisto pramonės įmonių renginiai, miesto šventės ir "
              "mokyklų technologijų dienos.",
        extra="Regione dažnai renkamasi visos dienos nuoma, nes svečiai renkasi bangomis — tada "
              "dirbame ciklais su trumpais pasirodymais kas valandą."),
    "radviliskis": dict(
        region="Šiaulių apskritis",
        venues=["Radviliškio kultūros centras", "geležinkelio mazgo ir logistikos teritorijos",
                "gamybos įmonių erdvės", "mokyklų salės", "miesto aikštės"],
        intro="Radviliškis yra svarbus geležinkelio ir logistikos mazgas, todėl daug vietos renginių "
              "susiję su transporto sektoriumi.",
        scene="Populiariausi užsakymai — logistikos ir gamybos įmonių šventės, miesto renginiai bei "
              "profesinio mokymo įstaigų karjeros dienos.",
        extra="Transporto sektoriaus renginiuose robotas natūraliai įsilieja į automatizacijos temą — "
              "tai dažnai naudojama įmonės komunikacijoje apie technologijas."),
    "birstonas": dict(
        region="Kauno apskritis",
        venues=["SPA ir sveikatingumo kompleksų konferencijų salės", "kurorto viešbučiai",
                "Nemuno kilpų regiono renginių vietos", "kurorto lauko erdvės", "restoranų terasos"],
        intro="Birštonas — kompaktiškas kurortas, kuriame vyksta daug įmonių išvažiuojamųjų sesijų ir "
              "nedidelių konferencijų. Erdvės čia jaukios, todėl robotas pastebimas iš karto.",
        scene="Kurorte robotas dažniausiai reikalingas dviejų dienų įmonių renginiams, viešbučių "
              "programoms ir vestuvėms prie Nemuno.",
        extra="Dviejų dienų formatams siūlome paketą su tuo pačiu operatoriumi abiem dienoms — tai "
              "pigiau ir paprasčiau nei du atskiri užsakymai."),
    "elektrenai": dict(
        region="Vilniaus apskritis",
        venues=["Elektrėnų kultūros centras", "ledo arena", "energetikos sektoriaus įmonių erdvės",
                "mokyklų salės", "miesto viešosios erdvės"],
        intro="Elektrėnai — energetikos ir ledo ritulio miestas pusiaukelėje tarp Vilniaus ir Kauno. "
              "Renginiai dažnai susiję su sporto arena arba energetikos sektoriumi.",
        scene="Dažniausi scenarijai — sporto renginiai ir varžybų pertraukų programos, energetikos "
              "įmonių šventės ir miesto renginiai.",
        extra="Ledo arenoje robotas dirba prie tribūnų arba fanų zonoje, ne ant ledo — tam reikia "
              "lygaus, neslidaus paviršiaus ir elektros prieigos."),
    "anyksciai": dict(
        region="Utenos apskritis",
        venues=["Anykščių kultūros centras", "turizmo objektų ir pramogų parkų erdvės",
                "viešbučių konferencijų salės", "miesto aikštės", "mokyklų salės"],
        intro="Anykščiai — vienas stipriausių Lietuvos turizmo centrų, kur renginių sezonas ilgas, o "
              "konkurencija dėl lankytojų dėmesio didelė.",
        scene="Populiariausi užsakymai — turizmo objektų aktyvacijos, miesto šventės, įmonių "
              "išvažiuojamieji renginiai ir vestuvės.",
        extra="Turizmo objektams robotas veikia kaip sezoninis traukos taškas — dažnai užsakomas "
              "savaitgaliams su pasirodymais ciklais visą dieną."),
    "birzai": dict(
        region="Panevėžio apskritis",
        venues=["Biržų kultūros centras", "pilies ir dvaro prieigų erdvės", "alaus pramonės ir "
                "gamybos įmonių teritorijos", "miesto aikštės", "mokyklų salės"],
        intro="Biržai — šiaurės Lietuvos miestas su istoriniu paveldu ir tradicine pramone. Vietos "
              "renginiai sutraukia didelę bendruomenės dalį.",
        scene="Dažniausi formatai — miesto šventės, gamybos įmonių renginiai ir mokyklų programos.",
        extra="Renginiams prie pilies ar dvaro zoną derinam iš anksto — svarbu lygus paviršius ir "
              "elektros prieiga, o istorinėse teritorijose tai ne visada akivaizdu."),
    "rokiskis": dict(
        region="Panevėžio apskritis",
        venues=["Rokiškio kultūros centras", "dvaro ir muziejaus erdvės", "maisto pramonės įmonių "
                "teritorijos", "miesto aikštės", "mokyklų salės"],
        intro="Rokiškis derina stiprią maisto pramonę su gyva kultūros scena — todėl čia vyksta ir "
              "dideli įmonių vakarai, ir bendruomeniniai miesto renginiai.",
        scene="Populiariausi užsakymai — maisto pramonės įmonių šventės, miesto renginiai ir mokyklų "
              "technologijų dienos.",
        extra="Didelėms darbuotojų šventėms rekomenduojame kelis trumpesnius pasirodymus vietoj vieno "
              "ilgo — taip robotą pamato visos svečių bangos."),
    "prienai": dict(
        region="Kauno apskritis",
        venues=["Prienų kultūros ir laisvalaikio centras", "Nemuno kilpų regiono renginių vietos",
                "aviacijos ir sporto erdvės", "mokyklų salės", "miesto aikštės"],
        intro="Prienai yra Nemuno kilpų regiono centras, populiarus tarp aktyvaus poilsio ir "
              "išvažiuojamųjų renginių organizatorių.",
        scene="Dažniausi scenarijai — įmonių išvažiuojamieji renginiai, miesto šventės, sporto "
              "renginiai ir mokyklų programos.",
        extra="Gamtoje ir sodybose svarbiausia elektros prieiga bei lygus paviršius — zoną parenkame "
              "kartu iš anksto, kad renginio dieną nekiltų netikėtumų."),
}


def build_city(slug, name, loc, gen):
    d = CITY_DATA[slug]
    url = f"{SITE}/{city_url(slug)}"
    title = f"Humanoidinio roboto nuoma {loc} renginiams | 33bots"
    # Aprašyme minimas ir regionas — taip kiekvieno miesto santrauka paieškos
    # rezultatuose skiriasi ne tik miesto vardu.
    desc = (f"Humanoidinio roboto Unitree G1 nuoma {loc} ir visoje {d['region']}: renginiams, "
            f"konferencijoms ir parodoms. Operatorius ir ženklinimas kainoje.")
    keywords = (f"roboto nuoma {name}, robotas renginiui {name}, humanoidinis robotas {loc}, "
                f"renginių pramoga {name}, robotų nuoma {gen} regione")

    venues = "\n".join(f"        <li>{v}</li>" for v in d["venues"])

    faq = [
        (f"Kiek kainuoja atvykimas į {loc}?",
         f"Atvykimą į {loc} vertiname pagal renginio vietą ir sumą nurodome pasiūlyme kartu su "
         f"nuomos kaina. Aptarnaujame visą Lietuvą."),
        (f"Kiek iš anksto reikia rezervuoti robotą {loc}?",
         "Sezono metu rekomenduojame 3–4 savaites, ne sezono metu dažnai pavyksta suderinti greičiau. "
         "Skubiems atvejams visada verta paskambinti — kartais turime laisvą langą."),
        (f"Kokių sąlygų reikia renginio vietoje {loc}?",
         "Standartinio 230 V lizdo, maždaug 2×2 m laisvos erdvės ir prieigos likus 45 minutėms iki "
         "pirmo pasirodymo. Visa kita — mūsų atsakomybė."),
        (f"Ar dirbate {gen} rajone už miesto ribų?",
         f"Taip. Aptarnaujame visą {d['region']} ir likusią Lietuvą — sodybas, gamyklų teritorijas ir "
         f"kaimo turizmo sodybas įskaitant."),
        ("Ar galima robotą ženklinti mūsų logotipu?",
         "Taip, ir tai nekainuoja papildomai. Logotipas ir QR kodas ant roboto krūtinės įeina į "
         "standartinį paketą."),
        # Klausimas surenkamas iš to miesto erdvių sąrašo, todėl kiekviename puslapyje
        # skiriasi ir atsako būtent į tai, ko ieško vietos organizatorius.
        (f"Ar galite dirbti tokiose erdvėse kaip {d['venues'][0]}?",
         f"Taip. {name} ir aplinkiniame regione dažniausiai dirbame būtent tokiose vietose: "
         f"{', '.join(d['venues'][:3])}. Robotui reikia tik 230 V lizdo ir maždaug 2×2 m lygaus "
         f"paviršiaus, todėl tinka ir salė, ir atriumas, ir gamyklos cechas. Nežinote, ar jūsų "
         f"erdvė tinka — atsiųskite nuotrauką, atsakysime tą pačią dieną."),
    ]

    ld = [
        organization_ld(),
        f"""{{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Humanoidinio roboto nuoma {esc(loc)}",
  "description": "{esc(desc)}",
  "url": "{url}",
  "serviceType": "Humanoidinio roboto nuoma renginiams",
  "provider": {{"@id": "{SITE}/#organizacija"}},
  "areaServed": [
    {{"@type": "City", "name": "{esc(name)}"}},
    {{"@type": "AdministrativeArea", "name": "{esc(d['region'])}"}}
  ],
  "offers": {{
    "@type": "Offer",
    "priceCurrency": "EUR",
    "availability": "https://schema.org/InStock",
    "url": "{url}"
  }}
}}""",
        breadcrumb_ld([("Pradžia", f"{SITE}/"), ("Miestai", f"{SITE}/kontaktai.html"), (name, url)]),
        faq_ld(faq),
    ]

    html = head(title=title, description=desc, slug=city_url(slug), keywords=keywords,
                og_image=f"{SITE}/og/{city_url(slug).replace('.html', '.jpg')}",
                extra_ld=ld, preload_hero=True)
    html += body_open()
    html += nav()
    html += crumbs([("Pradžia", "index.html"),
                    ("Humanoidinio roboto nuoma", "humanoidinio-roboto-nuoma.html"),
                    (name, None)])

    # Kitų miestų sąrašas sukamas nuo esamo miesto, o ne visada nuo Vilniaus —
    # taip kiekvienas puslapis turi savo nuorodų rinkinį (mažiau kartojimosi) ir
    # vidinė nuorodų svoris pasiskirsto po visus 28 miestus, o ne po pirmus devynis.
    i = next(n for n, c in enumerate(CITIES) if c[0] == slug)
    other = (CITIES[i + 1:] + CITIES[:i])[:9]
    other_links = "\n".join(f'        <a href="{city_url(s)}">{n}</a>' for s, n, _, _ in other)

    html += f"""
  <section class="hero hero--sub hero--split">
    <div class="hero__content">
      <p class="hero__eyebrow">Robotų nuoma · {name} · {d['region']}</p>
      <h1 class="hero__title">Roboto nuoma<br />{loc} —<br /><em>Unitree G1.</em></h1>
      <p class="hero__sub">{d['intro']}</p>
      <div class="hero__ctas">
        <a href="#kontaktai" class="btn-primary">Gauti pasiūlymą {loc}</a>
        <a href="#nauda" class="btn-ghost">Kaip tai veikia ↓</a>
      </div>
      <div class="hero__trust">
        <span class="hero__trust-item">✓ Dirbame {loc}</span>
        <span class="hero__trust-item">✓ Operatorius kainoje</span>
        <span class="hero__trust-item">✓ Ženklinimas be priemokų</span>
        <span class="hero__trust-item">✓ Atsakymas per 24 val.</span>
      </div>
    </div>
    <div class="hero__visual">
      <div class="hero__spotlight" aria-hidden="true"></div>
      <div class="hero__robot-wrap" id="robotWrap">
      <div class="hero__robot">
        <div class="robot-scan" aria-hidden="true"></div>
        <picture>
          <source srcset="robot-g1-960.webp 960w, robot-g1.webp 2390w" sizes="(min-width: 769px) 45vw, 1px" type="image/webp" />
          <img src="robot-g1.jpg"
               alt="Humanoidinis robotas Unitree G1 — nuoma renginiams {loc}"
               class="hero__robot-img"
               width="600" height="800"
               loading="eager"
               fetchpriority="high" />
        </picture>
      </div>
      </div>
    </div>
  </section>

  <!-- VIETOS KONTEKSTAS -->
  <section class="section" id="nauda">
    <div style="max-width:1000px; margin:0 auto; display:grid; grid-template-columns:repeat(auto-fit,minmax(320px,1fr)); gap:var(--s7);">
      <div>
        <h2 class="section-title" style="font-size:clamp(1.6rem,3vw,2.4rem); margin-bottom:var(--s4);">Renginiai {loc} su robotu</h2>
        <div class="article-body" style="max-width:none;">
          <p>{d['scene']}</p>
          <p>{d['extra']}</p>
          <p>Nesvarbu, koks formatas — paslauga ta pati: atvežame robotą, paskiriame operatorių visam renginio laikui ir pasirūpiname technine puse. Jūs rūpinatės svečiais.</p>
        </div>
      </div>
      <div>
        <h2 class="section-title" style="font-size:clamp(1.6rem,3vw,2.4rem); margin-bottom:var(--s4);">Kur dirbame {loc}</h2>
        <div class="article-body" style="max-width:none;">
          <p>Robotui tinka bet kuri erdvė, kurioje yra elektros lizdas ir apie 2×2 m lygaus paviršiaus. {name} ir aplinkiniame regione tai dažniausiai:</p>
          <ul>
{venues}
          </ul>
          <p>Jei nesate tikri, ar jūsų erdvė tinka — atsiųskite nuotrauką ar planą, ir atsakysime tą pačią dieną.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- KĄ GAUNATE -->
  <section class="section" style="padding-top:0;">
    <div class="section-header">
      <span class="tag">{name}</span>
      <h2 class="section-title">Kas įeina į nuomą<br />{loc}</h2>
    </div>
    <div class="use-grid">
      <div class="use-item">
        <span class="use-num">01</span>
        <h3>Robotas ir įranga</h3>
        <p>Unitree G1 su visa reikalinga įranga: baterijomis, valdymu ir garso sistema.</p>
      </div>
      <div class="use-item">
        <span class="use-num">02</span>
        <h3>Operatorius</h3>
        <p>Sertifikuotas operatorius visą renginio laiką — ne tik paleidimui.</p>
      </div>
      <div class="use-item">
        <span class="use-num">03</span>
        <h3>Atvykimas</h3>
        <p>Atvažiuojame į {loc}; atvykimo kainą nurodome pasiūlyme.</p>
      </div>
      <div class="use-item">
        <span class="use-num">04</span>
        <h3>Ženklinimas</h3>
        <p>Jūsų logotipas ir QR kodas ant roboto krūtinės — be priemokų.</p>
      </div>
      <div class="use-item">
        <span class="use-num">05</span>
        <h3>Scenarijus</h3>
        <p>Pasirodymo eiga, suderinta su jūsų renginio programa ir žinute.</p>
      </div>
      <div class="use-item">
        <span class="use-num">06</span>
        <h3>Draudimas</h3>
        <p>Civilinės atsakomybės draudimo apsauga veiklai — ramybė abiem pusėms.</p>
      </div>
    </div>
  </section>

"""
    html += strip_section(city_url(slug), title=f"Kadrai iš mūsų renginių")
    html += video_section(heading=f"Pamatykite robotą<br />prieš užsakant")
    html += faq_section(faq, title=f"Klausimai apie nuomą<br />{loc}")

    html += f"""  <!-- KITI MIESTAI -->
  <section class="section" style="padding-top:0;">
    <div style="max-width:900px; margin:0 auto;">
      <p style="font-size:0.75rem; color:var(--text-3); text-transform:uppercase; letter-spacing:0.1em; font-weight:700; margin-bottom:var(--s3);">Paslaugos {loc}</p>
      <div class="related-links">
        <a href="robotas-renginiui.html">Robotas renginiui →</a>
        <a href="robotas-parodoms.html">Robotas parodoms →</a>
        <a href="robotas-konferencijai.html">Konferencijos ir gala →</a>
        <a href="robotas-imones-sventei.html">Įmonės šventė →</a>
        <a href="kainos.html">Kainos →</a>
      </div>
      <p style="font-size:0.75rem; color:var(--text-3); text-transform:uppercase; letter-spacing:0.1em; font-weight:700; margin:var(--s6) 0 var(--s3);">Kiti miestai</p>
      <div class="related-links">
{other_links}
      </div>
    </div>
  </section>

"""
    html += contact_section(heading=f"Rezervuokite robotą<br />{loc}.",
                            lead=f"Parašykite renginio datą ir vietą {loc} — atsakysime per vieną darbo "
                                 f"dieną su kaina ir laisvomis datomis.")
    html += footer()
    write(city_url(slug), html)


def build():
    for slug, name, loc, gen in CITIES:
        build_city(slug, name, loc, gen)


if __name__ == "__main__":
    build()
