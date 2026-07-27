# -*- coding: utf-8 -*-
"""Papildomi 33bots.lt paslaugų puslapiai — antroji frazių banga.

Struktūra tokia pat kaip build_offers.PAGES; abu sąrašai renderinami tuo pačiu šablonu.
"""

PAGES2 = [
    dict(
        slug="unitree-g1-nuoma.html",
        title="Unitree G1 nuoma Lietuvoje — humanoidinis robotas | 33bots",
        desc="Unitree G1 nuoma Lietuvoje: 132 cm, 43 laisvės laipsniai, LiDAR. Robotas su operatoriumi "
             "renginiams ir parodoms. Transportas įskaičiuotas.",
        keywords="Unitree G1 nuoma, Unitree robotas, G1 robotas Lietuvoje, Unitree nuoma",
        crumb="Unitree G1 nuoma",
        eyebrow="Unitree G1 · Nuoma Lietuvoje",
        h1="Unitree G1 nuoma —<br />humanoidas, kurį<br /><em>galite turėti rytoj.</em>",
        lead="Unitree G1 yra tas pats robotas, kurį matote technologijų konferencijų įrašuose ir "
             "gamintojo demonstracijose. Lietuvoje jį galima tiesiog išsinuomoti — su operatoriumi, "
             "transportu ir paruošta programa.",
        tag="Unitree G1",
        benefits_title="Kodėl būtent<br />Unitree G1",
        benefits=[
            ("Tinkamas ūgis", "132 cm — pakankamai įspūdingas, kad matytųsi minioje, ir pakankamai "
                              "nedidelis, kad nekeltų grėsmės pojūčio bendraujant iš arti."),
            ("43 laisvės laipsniai", "Judesys atrodo kaip kūno, o ne kaip mechanizmo. Būtent dėl to "
                                     "žmonės reaguoja emociškai, o ne tik smalsiai."),
            ("LiDAR ir kompiuterinė rega", "Robotas realiu laiku aptinka kliūtis ir žmones — todėl gali "
                                           "dirbti tiesiai minioje, o ne už atitvarų."),
            ("35 kg svoris", "Telpa į įprastą automobilį ir nereikalauja specialios technikos, todėl "
                             "logistika į bet kurį Lietuvos miestą paprasta."),
            ("Greitas paruošimas", "Nuo atvykimo iki pirmo pasirodymo — apie 30–45 minutes. Nereikia "
                                   "planuoti pusdienio montavimui."),
            ("Aktualus modelis", "Nuomojant technologijos senėjimo rizika lieka mums — jūs visada "
                                 "gaunate veikiančią, prižiūrėtą įrangą."),
        ],
        body_h2_1="Ką Unitree G1 daro renginyje",
        body_1="<p>Praktinis repertuaras: <strong>vaikšto</strong> po erdvę apeidamas žmones, "
               "<strong>sveikinasi</strong> ir gestikuliuoja, <strong>pozuoja nuotraukoms</strong>, "
               "<strong>šoka</strong> pagal įrašytas choreografijas ir <strong>pasako</strong> iš anksto "
               "paruoštus tekstus per garso sistemą.</p>"
               "<p>Ko nedaro: neveda viso renginio savarankiškai ir nepriima nenumatytų sprendimų. "
               "G1 renginyje visada valdo operatorius pagal suderintą scenarijų — būtent todėl "
               "pasirodymas vyksta nuspėjamai. Pilną specifikaciją su lentelėmis rasite "
               "<a href=\"blog-unitree-g1-specifikacija.html\">Unitree G1 apžvalgoje</a>.</p>",
        body_h2_2="Nuoma ar pirkimas",
        body_2="<p>Unitree G1 galima nusipirkti, bet kaina yra tik pradžia: prisideda operatoriaus "
               "mokymai, techninė priežiūra, atsarginės dalys, transportavimo įranga, sandėliavimas ir "
               "draudimas. Prie to — atsakomybė, kad įranga veiktų būtent tą vieną vakarą, kai jos "
               "reikia.</p>"
               "<p>Praktinė taisyklė: iki maždaug 10–15 renginių per metus nuoma pigesnė ir paprastesnė. "
               "Skaičius su detalesniu palyginimu — straipsnyje "
               "<a href=\"blog-kiek-kainuoja-roboto-nuoma.html\">kiek kainuoja roboto nuoma</a>, o "
               "paketai — <a href=\"kainos.html\">kainų puslapyje</a>.</p>",
        faq=[
            ("Ar tikrai turite Unitree G1, ar nuomojate iš tarpininkų?",
             "Dirbame su sava įranga. Tai reiškia, kad robotą atveža ir valdo tie patys žmonės, su "
             "kuriais derinote scenarijų — be tarpininkų grandinės ir be netikėtumų renginio dieną."),
            ("Kiek laiko veikia G1 baterija?",
             "Vienas ciklas — apie valandą aktyvaus darbo. Baterijos keičiamos per suplanuotas "
             "pertraukas, todėl robotas gali dirbti visą renginio dieną."),
            ("Ar galima pamatyti robotą prieš užsakant?",
             "Taip. Didesniems projektams organizuojame demonstraciją arba vaizdo skambutį su veikiančiu "
             "robotu, kad matytumėte rezultatą prieš pasirašydami sutartį."),
            ("Ar G1 kalba lietuviškai?",
             "Robotas atkuria iš anksto paruoštus tekstus — juos galime įrašyti lietuvių arba anglų "
             "kalba ir suderinti su jūsų renginio komunikacija."),
            ("Ar galima nuomotis kelis G1 vienu metu?",
             "Taip, didesniems projektams skiriame daugiau nei vieną robotą su atskirais operatoriais. "
             "Tokius užsakymus verta derinti bent kelias savaites iš anksto."),
        ],
        related=[("humanoidinio-roboto-nuoma.html", "Nuomos sąlygos"),
                 ("blog-unitree-g1-specifikacija.html", "G1 specifikacija"),
                 ("video-realizacijos.html", "Vaizdo įrašai"),
                 ("kainos.html", "Kainos"),
                 ("robotu-nuoma.html", "Robotų nuoma Lietuvoje")],
    ),
    dict(
        slug="pramogos-renginiams.html",
        title="Pramogos renginiams — idėja, kurios svečiai dar nematė | 33bots",
        desc="Pramogos renginiams, kurios iš tikrųjų įsimenamos: humanoidinis robotas vietoj eilinės "
             "programos. Palyginimas su kitomis pramogomis ir praktiniai scenarijai.",
        keywords="pramogos renginiams, renginio pramoga, idėjos renginiui, atrakcijos renginiams, "
                 "pramogos įmonių renginiams",
        crumb="Pramogos renginiams",
        eyebrow="Pramogos renginiams · Ne dar vienas fokusnininkas",
        h1="Pramogos renginiams,<br />kurių svečiai<br /><em>dar nematė.</em>",
        lead="Fotobūdelė, fokusnininkas, gyva muzika — visa tai jūsų svečiai jau matė. Humanoidinio "
             "roboto — greičiausiai ne. Ir būtent todėl apie jį kalbės kitą dieną.",
        tag="Pramogos",
        benefits_title="Ko reikalaujame<br />iš geros pramogos",
        benefits=[
            ("Veikia visiems", "Nuo penkiamečio iki senjoro, nuo IT skyriaus iki gamybos — robotas "
                               "nereikalauja pasirinkti, kuriai svečių grupei taikote."),
            ("Sukuria turinį", "Kiekvienas svečias filmuoja. Renginys plinta socialiniuose tinkluose be "
                               "papildomo reklamos biudžeto."),
            ("Neužima programos", "Pasirodymai trumpi ir suplanuoti — pramoga sustiprina programą, o ne "
                                  "konkuruoja su ja."),
            ("Tinka bet kuriai erdvei", "Konferencijų salė, restoranas, sodyba, gamyklos aikštelė ar "
                                        "prekybos centro atriumas."),
            ("Duoda temą pokalbiui", "Svečiai lengviau užkalba vieni kitus, kai turi bendrą temą. "
                                     "Ypač vertinga mišriose grupėse."),
            ("Matuojamas rezultatas", "QR kodas ant roboto rodo nuskaitymus analitikoje — matote, ar "
                                      "pramoga virto kontaktais."),
        ],
        body_h2_1="Kaip pasirinkti pramogą renginiui",
        body_1="<p>Pirmiausia atsakykite, <strong>ko iš tikrųjų norite</strong>: kad svečiams būtų "
               "smagu, kad renginys būtų prisimenamas, kad surinktumėte kontaktus, ar kad gautumėte "
               "turinio socialiniams tinklams. Skirtingi tikslai veda prie skirtingų pasirinkimų.</p>"
               "<p>Jei tikslas — <strong>atmosfera visą vakarą</strong>, geras DJ arba grupė padarys "
               "daugiau. Jei tikslas — <strong>vienas stiprus momentas ir turinys</strong>, humanoidinis "
               "robotas beveik visada laimi. Praktikoje dažniausiai renkamasi derinys: robotas kaip "
               "akcentas plius muzika fonui.</p>",
        body_h2_2="Populiariausi scenarijai Lietuvoje",
        body_2="<p>Pagal formatą: <a href=\"robotas-imones-sventei.html\">įmonių šventės</a> ir "
               "<a href=\"robotas-komandos-formavimui.html\">komandos formavimo renginiai</a>, "
               "<a href=\"robotas-konferencijai.html\">konferencijos ir gala vakarai</a>, "
               "<a href=\"robotas-parodoms.html\">parodų stendai</a>, "
               "<a href=\"robotas-gimtadieniui.html\">gimtadieniai</a> ir "
               "<a href=\"robotas-vestuvems.html\">vestuvės</a>.</p>"
               "<p>Sąžiningą palyginimą su kitomis pramogomis — su lentele pagal WOW efektą, "
               "pasiekiamumą ir verslo vertę — rasite straipsnyje "
               "<a href=\"blog-robotas-ar-kitos-pramogos.html\">robotas ar kitos pramogos</a>. "
               "Daugiau idėjų — <a href=\"blog-renginio-pramogos-idejos.html\">pramogų idėjų "
               "straipsnyje</a>.</p>",
        faq=[
            ("Kiek laiko trunka roboto pasirodymas?",
             "Vienas pasirodymas — 5–15 minučių, priklausomai nuo scenarijaus. Ilgesniuose renginiuose "
             "dirbame ciklais: trumpas pasirodymas kas valandą ir nuotraukų zona tarp jų."),
            ("Ar robotas tinka mažam renginiui?",
             "Nuo maždaug 30 svečių efektas jau matomas. Didžiausią vertę robotas duoda renginiuose nuo "
             "100 dalyvių, kur svarbus ir turinio pasiekiamumas."),
            ("Ar galima derinti robotą su kitomis pramogomis?",
             "Taip, ir taip daroma dažniausiai. Robotas duoda WOW momentą, o muzika ar maistas kuria "
             "bendrą atmosferą — jie vienas kitam netrukdo."),
            ("Kiek iš anksto rezervuoti pramogą?",
             "Sezono metu (rugsėjis–gruodis, gegužė–birželis) rekomenduojame 3–4 savaites. Ne sezono "
             "metu dažnai pavyksta suderinti greičiau."),
        ],
        related=[("robotas-renginiui.html", "Robotas renginiui"),
                 ("robotas-imones-sventei.html", "Įmonės šventė"),
                 ("blog-renginio-pramogos-idejos.html", "Pramogų idėjos"),
                 ("blog-robotas-ar-kitos-pramogos.html", "Palyginimas"),
                 ("kainos.html", "Kainos")],
    ),
    dict(
        slug="robotas-gimtadieniui.html",
        title="Robotas gimtadieniui — staigmena, kurios niekas nesitiki | 33bots",
        desc="Humanoidinis robotas gimtadienio šventėje: pasitinka svečius, šoka ir fotografuojasi. "
             "Nuoma visoje Lietuvoje su operatoriumi ir transportu.",
        keywords="robotas gimtadieniui, gimtadienio pramoga, staigmena gimtadieniui, robotas vaiko gimtadieniui",
        crumb="Robotas gimtadieniui",
        eyebrow="Gimtadieniai · Staigmena, kuri pranoksta lūkesčius",
        h1="Robotas gimtadieniui —<br />staigmena, kurios<br /><em>niekas nesitiki.</em>",
        lead="Vaikui, kuris svajoja apie robotus, arba suaugusiam, kuris „viską jau turi“. Humanoidinis "
               "robotas gimtadienyje yra dovana, kurios negalima išpakuoti — bet apie kurią kalbama metus.",
        tag="Gimtadieniai",
        benefits_title="Robotas gimtadienio<br />šventėje",
        benefits=[
            ("Įėjimo momentas", "Robotas pasitinka jubiliatą arba svečius — vakaras prasideda nuo "
                                "reakcijos, kurios negalima suvaidinti."),
            ("Vaikai apstoja iš karto", "Vaikų gimtadieniuose robotas yra absoliutus centras. Eilė "
                                        "nuotraukoms susidaro per pirmą minutę."),
            ("Suaugusiems irgi veikia", "Apvalūs jubiliejai — 30, 40, 50 — dažnai užsakomi būtent dėl "
                                        "efekto, kurio svečiai nesitiki."),
            ("Šokių aikštelė", "Su muzika robotas perima aikštelę ir įtraukia net tuos, kurie "
                               "paprastai nešoka."),
            ("Nuotraukos visiems", "Kadrai su robotu keliauja į socialinius tinklus patys — jų nereikia "
                                   "prašyti ar spausdinti."),
            ("Namuose ar restorane", "Reikia tik elektros lizdo ir maždaug 2×2 m lygaus paviršiaus."),
        ],
        body_h2_1="Vaikų ir suaugusiųjų gimtadieniai",
        body_1="<p><strong>Vaikų šventėse</strong> planuojame trumpesnius, bet dažnesnius pasirodymus — "
               "vaikų dėmesys trumpesnis, o eilė nuotraukoms susidaro akimirksniu. Operatorius aiškiai "
               "pažymi zoną ir organizuoja nuotraukas eilės tvarka, kad visiems užtektų.</p>"
               "<p><strong>Suaugusiųjų jubiliejuose</strong> logika kita: svarbiausias vienas stiprus "
               "momentas. Dažniausiai tai roboto pasirodymas po vakarienės arba dalyvavimas "
               "simboliniame momente — torto įnešime ar sveikinime.</p>",
        body_h2_2="Ką reikia paruošti",
        body_2="<p>Elektros lizdo, maždaug 2×2 m lygaus paviršiaus ir informacijos, kada tiksliai norite "
               "roboto pasirodymo. Restorano salė, namų kiemas, sodyba ar terasa tinka puikiai — svarbu "
               "tik lygus pagrindas ir sausas oras, jei renginys lauke.</p>"
               "<p>Standartinis gimtadienio paketas trunka 2–3 valandas ir apima pasitikimą, vieną "
               "pasirodymą ir laisvą bendravimą su svečiais. Panašius formatus rasite ir "
               "<a href=\"robotas-vestuvems.html\">vestuvių</a> bei "
               "<a href=\"robotas-imones-sventei.html\">įmonių švenčių</a> puslapiuose.</p>",
        faq=[
            ("Ar robotas saugus vaikams?",
             "Taip — vaikų renginiuose dirbame dažnai. Robotas turi jutiklius, aptinkančius žmones, o "
             "operatorius visą laiką prižiūri zoną ir organizuoja nuotraukas eilės tvarka."),
            ("Ar galima robotą užsakyti į namus?",
             "Taip, jei yra elektros lizdas ir maždaug 2×2 m lygaus paviršiaus. Butuose ir namuose "
             "dirbame reguliariai."),
            ("Nuo kokio amžiaus vaikams įdomu?",
             "Praktiškai nuo maždaug trejų metų. Mažesni vaikai kartais išsigąsta judesio, todėl tokiais "
             "atvejais pradedame lėtai ir iš saugaus atstumo."),
            ("Ar robotas gali padainuoti „Su gimtadieniu“?",
             "Robotas atkuria iš anksto paruoštus garso įrašus, todėl sveikinimą galime paruošti — tik "
             "praneškite apie tai užsakydami."),
            ("Kiek trunka gimtadienio paketas?",
             "Standartiškai 2–3 valandos. Ilgesniems renginiams siūlome visos dienos paketą su "
             "pasirodymais ciklais."),
        ],
        related=[("robotas-vestuvems.html", "Vestuvės"),
                 ("robotas-imones-sventei.html", "Įmonės šventė"),
                 ("pramogos-renginiams.html", "Pramogos renginiams"),
                 ("kainos.html", "Kainos"),
                 ("video-realizacijos.html", "Vaizdo įrašai")],
    ),
    dict(
        slug="robotas-prekybos-centrui.html",
        title="Robotas prekybos centrui — daugiau lankytojų ir dėmesio | 33bots",
        desc="Humanoidinis robotas prekybos centre: pritraukia praeivius, sukuria minią prie parduotuvės "
             "ir generuoja turinį. Nuoma visoje Lietuvoje.",
        keywords="robotas prekybos centrui, robotas parduotuvei, retail pramoga, prekybos centro renginys",
        crumb="Robotas prekybos centrui",
        eyebrow="Retail · Praeiviai virsta lankytojais",
        h1="Robotas prekybos<br />centrui — praeiviai<br /><em>virsta lankytojais.</em>",
        lead="Prekybos centre laimi tas, kas sustabdo srautą. Humanoidinis robotas atriume padaro tai be "
             "flaierių, be garsiakalbių ir be įkyrių pardavėjų.",
        tag="Retail",
        benefits_title="Ką robotas duoda<br />prekybos centrui",
        benefits=[
            ("Sustabdo srautą", "Žmonės sustoja patys. Aplink robotą susidaro minia, kuri savaime "
                                "signalizuoja, kad čia kažkas vyksta."),
            ("Nukreipia į parduotuvę", "Robotą galima pastatyti taip, kad minia formuotųsi prie "
                                       "konkretaus įėjimo arba naujos parduotuvės."),
            ("QR kodas į akciją", "Ženklinimas veda tiesiai į nuolaidą, registraciją ar el. parduotuvę — "
                                  "nuskaitymai matomi analitikoje."),
            ("Savaitgalio traukos taškas", "Šeimos ateina specialiai — vaikams tai atrakcija, tėvams "
                                           "priežastis pasilikti ilgiau."),
            ("Turinys centrui ir nuomininkams", "Įrašai tinka ir prekybos centro, ir konkretaus prekės "
                                                "ženklo komunikacijai."),
            ("Kelių dienų akcijos", "Robotas gali dirbti visą akcijos savaitgalį arba kelias dienas iš "
                                    "eilės su tuo pačiu operatoriumi."),
        ],
        body_h2_1="Kaip suplanuoti robotą prekybos centre",
        body_1="<p>Svarbiausia — <strong>vieta ir suderinimas su administracija</strong>. Robotui reikia "
               "matomos, bet praėjimo neblokuojančios pozicijos ir elektros prieigos. Visą techninę "
               "informaciją — galios poreikį, matmenis, saugos priemones — pateikiame dokumentu, kurį "
               "galite persiųsti centro vadybininkui.</p>"
               "<p>Antra — <strong>grafikas</strong>. Atriume geriausiai veikia fiksuoti pasirodymai "
               "kas valandą po 10 minučių, paskelbti centro socialiniuose tinkluose. Tarp jų robotas "
               "lieka prieinamas nuotraukoms, o srautas nesibaigia.</p>",
        body_h2_2="Parduotuvės atidarymas ir akcijos",
        body_2="<p>Naujos parduotuvės atidarymui robotas dirba prie įėjimo dar prieš oficialią pradžią, "
               "dalyvauja simboliniame momente ir lieka lankytojams. Tai vienas efektyviausių būdų "
               "užtikrinti, kad atidarymo dieną prie durų būtų žmonių — o ne tuščia erdvė "
               "fotografams.</p>"
               "<p>Detalesnį atidarymo scenarijų aprašėme "
               "<a href=\"robotas-atidarymui.html\">atidarymų puslapyje</a>, o kelių dienų nuomos "
               "sąlygas — <a href=\"humanoidinio-roboto-nuoma.html\">nuomos puslapyje</a>.</p>",
        faq=[
            ("Ar reikia prekybos centro administracijos leidimo?",
             "Paprastai taip. Pateikiame techninę specifikaciją, galios poreikį ir saugos priemonių "
             "aprašą — dažniausiai to pakanka suderinimui."),
            ("Kiek vietos reikia atriume?",
             "Maždaug 2×2 m saugios zonos ir standartinis 230 V lizdas. Didesnei choreografijai "
             "patogiau turėti apie 4×4 m."),
            ("Ar robotas gali dirbti kelias dienas iš eilės?",
             "Taip — akcijoms ir atidarymams dažnai renkamasi kelių dienų paketas su tuo pačiu "
             "operatoriumi. Tai pigiau nei keli atskiri užsakymai."),
            ("Ar robotas netrukdys praėjimui?",
             "Zoną parenkame taip, kad minia formuotųsi šalia praėjimo, o ne jame. Prireikus "
             "rekomenduojame fizinį zonos žymėjimą stovais."),
        ],
        related=[("robotas-atidarymui.html", "Atidarymai"),
                 ("humanoidinio-roboto-nuoma.html", "Nuomos sąlygos"),
                 ("robotu-nuoma-vilnius.html", "Robotas Vilniuje"),
                 ("kainos.html", "Kainos"),
                 ("video-realizacijos.html", "Vaizdo įrašai")],
    ),
    dict(
        slug="robotas-mokyklai.html",
        title="Robotas mokyklai ir universitetui — technologijos gyvai | 33bots",
        desc="Humanoidinis robotas mokyklos, gimnazijos ar universiteto renginyje: atvirų durų dienos, "
             "karjeros dienos, STEM pamokos. Nuoma visoje Lietuvoje.",
        keywords="robotas mokyklai, robotas universitetui, STEM renginys, atvirų durų diena, karjeros diena",
        crumb="Robotas mokyklai",
        eyebrow="Švietimas · Technologija, kurią galima paliesti",
        h1="Robotas mokyklai —<br />technologija, kurią<br /><em>galima pamatyti gyvai.</em>",
        lead="Apie humanoidinius robotus mokiniai skaito ir žiūri įrašus. Pamatyti tokį robotą klasėje "
             "arba aktų salėje — visai kitas dalykas, ir būtent tai lieka atmintyje.",
        tag="Švietimas",
        benefits_title="Robotas švietimo<br />renginyje",
        benefits=[
            ("Atvirų durų dienos", "Mokykla ar universitetas, kuris parodo veikiantį humanoidą, "
                                   "įsimenamas geriau nei bet kuris lankstinukas."),
            ("STEM motyvacija", "Robotika, programavimas ir inžinerija tampa apčiuopiami — matomas "
                                "rezultatas, o ne teorija."),
            ("Karjeros dienos", "Įmonės partnerės renginyje su robotu sulaukia kur kas didesnio "
                                "moksleivių dėmesio."),
            ("Tinka visoms grupėms", "Nuo pradinukų iki studentų — skiriasi tik pasakojimo gylis, ne "
                                     "susidomėjimas."),
            ("Medžiaga įstaigai", "Įrašai ir nuotraukos naudojami mokyklos komunikacijai ir kitų metų "
                                  "priėmimo kampanijai."),
            ("Aktų salė ar kiemas", "Reikia tik elektros lizdo ir lygaus paviršiaus — sporto salė, "
                                    "aktų salė ar mokyklos kiemas tinka."),
        ],
        body_h2_1="Formatai švietimo įstaigoms",
        body_1="<p>Populiariausias variantas — <strong>pasirodymas aktų salėje</strong> su trumpu "
               "paaiškinimu, kaip robotas veikia, ir demonstracija: ėjimas, gestai, choreografija. Po "
               "jo — laisvas bendravimas ir nuotraukos mažesnėmis grupėmis.</p>"
               "<p>Antras variantas — <strong>robotas visą atvirų durų dieną</strong>, kai lankytojai "
               "renkasi bangomis. Tada dirbame ciklais: trumpas pasirodymas kas valandą ir nuotraukų "
               "zona tarp jų. Toks formatas užtikrina, kad kiekviena atvykusi grupė pamatys robotą.</p>",
        body_h2_2="Kaip finansuojami tokie renginiai",
        body_2="<p>Praktikoje mokyklų renginius dažnai remia <strong>vietos verslas arba tėvų "
               "komitetas</strong>. Rėmėjui tai patrauklu, nes roboto ženklinimas su logotipu "
               "įskaičiuotas į kainą — įmonė gauna matomumą, o mokykla renginį.</p>"
               "<p>Universitetų atveju dažniausiai užsakoma per karjeros centrus arba fakultetų "
               "renginius kartu su įmonėmis partnerėmis. Sąlygas ir paketus rasite "
               "<a href=\"kainos.html\">kainų puslapyje</a>, o saugos informaciją, kurios dažnai prašo "
               "įstaigos — <a href=\"blog-roboto-sauga-renginyje.html\">saugos vadove</a>.</p>",
        faq=[
            ("Ar robotas saugus mokiniams?",
             "Taip. Jutikliai aptinka žmones realiu laiku, o operatorius visą laiką prižiūri zoną. "
             "Mokyklose papildomai aiškiai pažymime pasirodymo ribas."),
            ("Kiek mokinių gali dalyvauti vienu metu?",
             "Pasirodyme aktų salėje — kiek telpa salėje. Nuotraukų daliai rekomenduojame skirstyti į "
             "grupes po 20–30, kad eilė judėtų sklandžiai."),
            ("Ar galite paaiškinti, kaip robotas veikia?",
             "Taip — operatorius trumpai pristato robotą suprantama kalba: jutiklius, judėjimą, "
             "valdymą. Gylį pritaikome pagal amžiaus grupę."),
            ("Ar dirbate su profesinio mokymo įstaigomis?",
             "Taip. Karjeros ir profesinio orientavimo dienos yra vienas dažniausių scenarijų — ypač "
             "kartu su įmonėmis partnerėmis."),
        ],
        related=[("robotas-renginiui.html", "Robotas renginiui"),
                 ("blog-roboto-sauga-renginyje.html", "Saugos vadovas"),
                 ("kainos.html", "Kainos"),
                 ("robotu-nuoma-kaunas.html", "Robotas Kaune"),
                 ("kontaktai.html", "Kontaktai")],
    ),
    dict(
        slug="robotas-kaledinei-sventei.html",
        title="Robotas kalėdinei šventei — netikėta žiemos programa | 33bots",
        desc="Humanoidinis robotas kalėdiniame įmonės vakarėlyje ar miesto šventėje. Netikėta programos "
             "dalis gruodį. Nuoma visoje Lietuvoje su operatoriumi.",
        keywords="robotas kalėdinei šventei, kalėdinis vakarėlis, įmonės kalėdinis renginys, žiemos šventė",
        crumb="Kalėdinės šventės",
        eyebrow="Kalėdos · Gruodžio programa be klišių",
        h1="Robotas kalėdinei<br />šventei — programa<br /><em>be klišių.</em>",
        lead="Gruodį visi renginiai atrodo panašiai: ta pati muzika, tie patys sveikinimai, ta pati "
             "loterija. Humanoidinis robotas yra vienintelis punktas, kurio programoje niekas "
             "nesitiki.",
        tag="Kalėdos",
        benefits_title="Robotas gruodžio<br />renginiuose",
        benefits=[
            ("Vakarėlio kulminacija", "Pasirodymas po vakarienės, kai svečiai jau atsipalaidavę — "
                                      "momentas, kuris patenka į visų telefonus."),
            ("Dovanų įteikimas", "Robotas gali dalyvauti simboliniame dovanų ar apdovanojimų įteikime "
                                 "vietoj eilinio scenarijaus."),
            ("Šeimų renginiai", "Darbuotojų vaikų šventėse robotas veikia stipriau nei bet kuris kitas "
                                "programos punktas."),
            ("Miesto eglės renginiai", "Lauko šventėse robotas pritraukia srautą prie scenos ar "
                                       "rėmėjo zonos."),
            ("Employer branding", "Įrašai iš kalėdinio renginio dirba visus metus — vidinei "
                                  "komunikacijai ir darbuotojų paieškai."),
            ("Rezervacija iš anksto", "Gruodis — įtempčiausias mėnuo. Ankstyva rezervacija reiškia "
                                      "laisvą pasirinkimą tarp datų."),
        ],
        body_h2_1="Kalėdinio renginio scenarijus su robotu",
        body_1="<p>Įmonės vakarėlyje veikia paprasta struktūra: robotas <strong>pasitinka svečius</strong> "
               "prie įėjimo, per vakarienę lieka paruošimo zonoje, o <strong>po vakarienės atlieka "
               "pasirodymą</strong>, po kurio prasideda laisvas bendravimas ir nuotraukos.</p>"
               "<p>Jei renginyje yra apdovanojimų ar padėkų dalis, robotą verta įtraukti būtent ten — "
               "įteikimo momentas su humanoidu atrodo kitaip nei standartinis kvietimas į sceną.</p>",
        body_h2_2="Kodėl rezervuoti anksti",
        body_2="<p>Gruodis Lietuvoje yra tankiausias renginių mėnuo: didelė dalis įmonių organizuoja "
               "vakarėlius per tas pačias 2–3 savaites, o penktadieniai ir šeštadieniai užsipildo "
               "pirmiausia. Praktiškai tai reiškia, kad <strong>lapkritį geriausios datos jau "
               "užimtos</strong>.</p>"
               "<p>Jei planuojate kalėdinį renginį, verta parašyti rudens pradžioje — tada dar galima "
               "rinktis datą, o ne derintis prie likučių. Kitus žiemos formatus rasite "
               "<a href=\"robotas-imones-sventei.html\">įmonių švenčių puslapyje</a>.</p>",
        faq=[
            ("Kada rezervuoti robotą kalėdiniam renginiui?",
             "Rekomenduojame rugsėjį–spalį. Gruodžio penktadieniai ir šeštadieniai užsipildo "
             "anksčiausiai visoje metų programoje."),
            ("Ar robotą galima papuošti kalėdiškai?",
             "Ženklinimą galime pritaikyti prie šventinio identiteto — logotipas, spalvos, šventinė "
             "grafika. Tai įskaičiuota į kainą."),
            ("Ar robotas dirba lauke žiemą?",
             "Sausu oru trumpai — taip, bet šaltis ir drėgmė riboja darbo laiką. Lauko renginiams "
             "rekomenduojame šildomą palapinę arba vidaus zoną."),
            ("Ar galima robotą užsakyti į vaikų kalėdinę šventę?",
             "Taip, tai vienas populiariausių gruodžio scenarijų. Vaikų renginiuose dirbame trumpesniais "
             "ciklais ir su aiškiai pažymėta zona."),
        ],
        related=[("robotas-imones-sventei.html", "Įmonės šventė"),
                 ("robotas-renginiui.html", "Robotas renginiui"),
                 ("pramogos-renginiams.html", "Pramogos renginiams"),
                 ("kainos.html", "Kainos"),
                 ("kontaktai.html", "Rezervacija")],
    ),
    dict(
        slug="robotas-fotosesijai.html",
        title="Robotas fotosesijai ir reklamos filmavimui | 33bots",
        desc="Humanoidinis robotas Unitree G1 reklamos fotosesijoje, vaizdo klipe ar filmavimo aikštelėje. "
             "Nuoma su operatoriumi visoje Lietuvoje.",
        keywords="robotas fotosesijai, robotas filmavimui, robotas reklamai, robotas vaizdo klipui",
        crumb="Fotosesijos ir filmavimai",
        eyebrow="Turinio gamyba · Kadras, kurio niekas neturi",
        h1="Robotas fotosesijai —<br />kadras, kurio<br /><em>niekas neturi.</em>",
        lead="Stock nuotraukos su robotais atrodo kaip stock nuotraukos. Tikras humanoidas jūsų "
             "aikštelėje atrodo kaip jūsų prekės ženklas — ir būtent taip veikia.",
        tag="Turinio gamyba",
        benefits_title="Robotas filmavimo<br />aikštelėje",
        benefits=[
            ("Valdomas judesys", "Operatorius gali kartoti tą patį judesį tiek kartų, kiek reikia "
                                 "kadrui — be improvizacijos ir be nuovargio."),
            ("Kinematografiška išvaizda", "Sidabrinis korpusas ir mėlynas vizorius gerai reaguoja į "
                                          "šviesą — robotas atrodo brangiau, nei kainuoja."),
            ("Realus, ne CGI", "Tikras objektas aikštelėje reiškia realius šešėlius ir atspindžius — "
                               "nereikia postprodukcijos, kuri kainuoja daugiau nei nuoma."),
            ("Lankstus grafikas", "Filmavimams dirbame pagal aikštelės grafiką, įskaitant ankstyvą rytą "
                                  "ir ilgesnes dienas."),
            ("Kelių dienų projektai", "Ilgesnėms produkcijoms — kelių dienų nuoma su tuo pačiu "
                                      "operatoriumi ir stabiliomis sąlygomis."),
            ("Techninė informacija iš anksto", "Matmenys, svoris, galios poreikis ir saugos zona — "
                                               "pateikiame prieš aikštelės planavimą."),
        ],
        body_h2_1="Kaip planuoti filmavimą su robotu",
        body_1="<p>Prieš aikštelę aptariame <strong>shot listą</strong>: kokių kadrų reikia, kokie "
               "judesiai juose, kiek dublių numatoma. Robotas atlieka iš anksto paruoštas sekas, todėl "
               "kuo tiksliau apibrėžti judesiai, tuo greičiau vyksta filmavimas.</p>"
               "<p>Techniškai reikia lygaus paviršiaus, elektros prieigos ir saugios zonos. Baterijos "
               "keičiamos per pertraukas, todėl ilgesnę dieną planuojame kartu su jūsų grafiku — kad "
               "keitimas nesutaptų su svarbiausiu kadru.</p>",
        body_h2_2="Kam dažniausiai reikia",
        body_2="<p>Dažniausi užsakovai — <strong>technologijų ir pramonės įmonės</strong>, kurioms "
               "reikia įvaizdinės medžiagos apie inovacijas, <strong>reklamos agentūros</strong>, "
               "kuriančios kampanijas klientams, ir <strong>muzikos bei turinio kūrėjai</strong>, "
               "ieškantys vizualiai stipraus elemento.</p>"
               "<p>Jei planuojate ir renginį, ir turinio gamybą, dažnai apsimoka sujungti į vieną "
               "užsakymą — žr. <a href=\"humanoidinio-roboto-nuoma.html\">nuomos sąlygas</a> arba "
               "peržiūrėkite <a href=\"video-realizacijos.html\">turimą medžiagą</a>.</p>",
        faq=[
            ("Ar galime naudoti medžiagą komerciškai?",
             "Taip. Jūsų nufilmuota ar nufotografuota medžiaga priklauso jums — naudojimo sąlygas "
             "aiškiai užfiksuojame sutartyje prieš filmavimą."),
            ("Ar robotas gali atlikti konkretų judesį pagal scenarijų?",
             "Turime paruoštų judesių ir sekų rinkinį. Jei reikia labai specifinio judesio, aptarkime "
             "iš anksto — dalį galima paruošti, dalis techniškai neįmanoma."),
            ("Kiek kainuoja filmavimo diena?",
             "Priklauso nuo trukmės ir vietos. Filmavimams dažniausiai taikomas visos dienos arba kelių "
             "dienų paketas — kainą pateikiame per 24 val. po užklausos."),
            ("Ar robotas veikia lauko aikštelėje?",
             "Sausu oru ir ant lygaus paviršiaus — taip. Lietui ar dulkėtai aplinkai reikia atsarginio "
             "plano, nes tai riboja įrangos darbą."),
        ],
        related=[("humanoidinio-roboto-nuoma.html", "Nuomos sąlygos"),
                 ("video-realizacijos.html", "Vaizdo įrašai"),
                 ("unitree-g1-nuoma.html", "Unitree G1"),
                 ("kainos.html", "Kainos"),
                 ("kontaktai.html", "Kontaktai")],
    ),
    dict(
        slug="robotas-komandos-formavimui.html",
        title="Robotas komandos formavimo renginiui (team building) | 33bots",
        desc="Humanoidinis robotas komandos formavimo renginyje: bendra patirtis, interaktyvios veiklos "
             "ir ledlaužis naujoje komandoje. Nuoma visoje Lietuvoje.",
        keywords="team building robotas, komandos formavimas, komandos renginys, ledlaužis komandai",
        crumb="Komandos formavimas",
        eyebrow="Team building · Bendra patirtis, ne privaloma veikla",
        h1="Robotas komandos<br />renginiui — patirtis,<br /><em>ne privaloma veikla.</em>",
        lead="Dauguma komandos formavimo veiklų nepatinka bent trečdaliui komandos. Humanoidinis robotas "
             "veikia kitaip: nieko neverčia dalyvauti, o visi vis tiek susirenka.",
        tag="Team building",
        benefits_title="Kodėl robotas veikia<br />komandos renginyje",
        benefits=[
            ("Niekas nesijaučia verčiamas", "Nereikia vaidinti, dainuoti ar lipti į virves. Žmonės "
                                            "prieina savo noru — ir todėl įsitraukia."),
            ("Ledlaužis naujoje komandoje", "Po susijungimo ar naujokų bangos robotas duoda bendrą temą, "
                                            "nuo kurios prasideda pokalbiai."),
            ("Veikia tarp skyrių", "Vienintelė veikla, kuri vienodai domina IT, gamybą, buhalteriją ir "
                                   "vadovybę."),
            ("Interaktyvios užduotys", "Galime paruošti trumpas veiklas, kuriose komandos varžosi arba "
                                       "atlieka užduotis kartu su robotu."),
            ("Bendra nuotrauka", "Komandos kadras su robotu tampa vidinės komunikacijos turiniu ir "
                                 "employer branding medžiaga."),
            ("Tinka biure ir sodyboje", "Reikia tik elektros ir lygaus paviršiaus — biuro erdvė, "
                                        "konferencijų salė ar sodybos kiemas."),
        ],
        body_h2_1="Formatai komandos renginiams",
        body_1="<p>Paprasčiausias variantas — <strong>robotas kaip renginio akcentas</strong>: "
               "pasirodymas dienos pradžioje arba po darbo sesijų, o po jo laisvas bendravimas. Toks "
               "formatas užima 2–3 valandas ir netrukdo pagrindinei programai.</p>"
               "<p>Aktyvesnis variantas — <strong>interaktyvios veiklos</strong>: komandos gauna "
               "užduotis, susijusias su robotu, arba varžosi trumpose rungtyse. Tai reikalauja "
               "ankstesnio derinimo, bet įtraukia labiau nei stebėjimas iš šono.</p>",
        body_h2_2="Išvažiuojamieji renginiai",
        body_2="<p>Dažnas scenarijus — dviejų dienų išvyka su darbo sesijomis dieną ir programa vakare. "
               "Populiariausios kryptys Lietuvoje: <a href=\"robotu-nuoma-druskininkai.html\">Druskininkai</a>, "
               "<a href=\"robotu-nuoma-trakai.html\">Trakai</a> ir "
               "<a href=\"robotu-nuoma-palanga.html\">Palanga</a>. Transportas įskaičiuotas, todėl "
               "atstumas nuo miesto kainos nekeičia.</p>"
               "<p>Dviejų dienų formatams siūlome paketą su tuo pačiu operatoriumi abiem dienoms — "
               "pigiau ir logistiškai paprasčiau nei du atskiri užsakymai. Kitus formatus rasite "
               "<a href=\"robotas-imones-sventei.html\">įmonių švenčių puslapyje</a>.</p>",
        faq=[
            ("Kiek žmonių komandoje yra optimalu?",
             "Robotas gerai veikia nuo 20 iki maždaug 200 dalyvių. Didesnėms grupėms rekomenduojame "
             "kelis trumpesnius pasirodymus vietoj vieno ilgo."),
            ("Ar galite paruošti užduotis komandoms?",
             "Taip — trumpas interaktyvias veiklas su robotu paruošiame pagal jūsų tikslus. Tai "
             "aptariame prieš renginį."),
            ("Ar robotas tinka renginiui biure?",
             "Taip, jei yra maždaug 2×2 m laisvos erdvės ir elektros lizdas. Biuruose ir "
             "konferencijų salėse dirbame reguliariai."),
            ("Ar dirbate išvažiuojamuosiuose renginiuose už miesto?",
             "Taip, ir transportas įskaičiuotas nepriklausomai nuo atstumo — sodybos ir kurortai mums "
             "įprasta darbo vieta."),
        ],
        related=[("robotas-imones-sventei.html", "Įmonės šventė"),
                 ("pramogos-renginiams.html", "Pramogos renginiams"),
                 ("robotas-konferencijai.html", "Konferencijos"),
                 ("kainos.html", "Kainos"),
                 ("video-realizacijos.html", "Vaizdo įrašai")],
    ),
    dict(
        slug="robotas-sporto-renginiui.html",
        title="Robotas sporto renginiui ir varžyboms | 33bots",
        desc="Humanoidinis robotas sporto renginyje: pertraukų programa, rėmėjų zona ir turinys "
             "socialiniams tinklams. Nuoma arenose visoje Lietuvoje.",
        keywords="robotas sporto renginiui, robotas arenoje, pertraukų programa, rėmėjų zona, varžybų pramoga",
        crumb="Sporto renginiai",
        eyebrow="Sportas · Pertrauka, kurios nepraleidžia",
        h1="Robotas sporto<br />renginiui — pertrauka,<br /><em>kurios nepraleidžia.</em>",
        lead="Per pertrauką dalis žiūrovų išeina. Humanoidinis robotas aikštelėje yra viena iš nedaugelio "
             "programų, dėl kurios lieka sėdėti — ir traukia telefonus.",
        tag="Sportas",
        benefits_title="Robotas arenoje<br />ir varžybose",
        benefits=[
            ("Pertraukų programa", "Trumpas pasirodymas aikštelės centre išlaiko žiūrovus tribūnose ir "
                                   "sukuria momentą, apie kurį kalbama po rungtynių."),
            ("Rėmėjų vertė", "Robotas su rėmėjo ženklinimu suteikia matomumą, kurio neduoda logotipas "
                             "ant reklaminio skydo."),
            ("Turinys klubui", "Įrašai iš pertraukos plinta klubo ir žiūrovų kanaluose — organinis "
                               "pasiekiamumas be reklamos biudžeto."),
            ("Prizų įteikimas", "Robotas gali dalyvauti apdovanojimų ceremonijoje ar simboliniame "
                                "pradžios momente."),
            ("Fan zona", "Prieš rungtynes robotas dirba fanų zonoje — žiūrovai ateina anksčiau."),
            ("Masiniai renginiai", "Bėgimai, sporto festivaliai ir miesto varžybos — robotas veikia "
                                   "kaip traukos taškas starto ar finišo zonoje."),
        ],
        body_h2_1="Kaip įtraukti robotą į varžybų programą",
        body_1="<p>Arenose robotas dažniausiai dirba <strong>trimis etapais</strong>: fanų zonoje prieš "
               "renginį, trumpame pasirodyme per pertrauką ir nuotraukų zonoje po varžybų. Toks "
               "pasiskirstymas išnaudoja visą renginio laiką, o ne vieną akimirką.</p>"
               "<p>Aikštelės pasirodymui reikia derinimo su arenos technine tarnyba: išėjimo laiko, "
               "garso ir saugios zonos. Visą techninę informaciją pateikiame iš anksto, kad derinimas "
               "su arena vyktų be jūsų tarpininkavimo.</p>",
        body_h2_2="Masiniai ir lauko sporto renginiai",
        body_2="<p>Bėgimuose ir lauko festivaliuose robotas geriausiai veikia <strong>starto arba "
               "finišo zonoje</strong>, kur susidaro didžiausias srautas. Ten pat paprastai yra ir "
               "rėmėjų palapinės, todėl ženklinimas su logotipu dirba tiesiogiai partnerio naudai.</p>"
               "<p>Lauko renginiuose reikia elektros prieigos ir lygaus paviršiaus, o esant lietui — "
               "stogelio. Panašius scenarijus aprašėme "
               "<a href=\"robotas-renginiui.html\">renginių puslapyje</a>, o kainų logiką — "
               "<a href=\"kainos.html\">kainų puslapyje</a>.</p>",
        faq=[
            ("Ar robotas gali dirbti ant sporto salės grindų?",
             "Taip — parketas ir sintetinės dangos tinka puikiai. Svarbu tik, kad paviršius būtų sausas "
             "ir neslidus."),
            ("Ar galima suderinti pasirodymą su arenos garso sistema?",
             "Taip. Turime savo kolonėlę, bet prireikus prisijungiame prie arenos garso — tai "
             "suderiname su technine tarnyba iš anksto."),
            ("Kiek trunka pertraukos pasirodymas?",
             "Standartiškai 3–7 minutės, kad tilptų į pertrauką be programos vėlavimo."),
            ("Ar robotas tinka lauko bėgimo renginiui?",
             "Taip, jei yra elektros prieiga ir lygus paviršius. Lietaus atveju reikia stogelio arba "
             "atsarginio plano."),
        ],
        related=[("robotas-renginiui.html", "Robotas renginiui"),
                 ("robotas-atidarymui.html", "Atidarymai"),
                 ("kainos.html", "Kainos"),
                 ("robotu-nuoma-kaunas.html", "Robotas Kaune"),
                 ("video-realizacijos.html", "Vaizdo įrašai")],
    ),
]
