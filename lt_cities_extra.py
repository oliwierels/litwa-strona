# -*- coding: utf-8 -*-
"""Papildomas kiekvieno miesto turinys: formatai ir logistika.

Iki 2026-09 miesto puslapyje savito teksto buvo vos 60–107 žodžiai iš maždaug 865 — visa
kita (navigacija, paslaugų aprašas, DUK, poraštė) kartojosi visuose puslapiuose. Google
tokį rinkinį vertina kaip ploną turinį ir atidėlioja indeksavimą.

Čia surašyta tai, ko niekur kitur nėra: kokie renginių formatai konkrečiame mieste
vyrauja ir ką verta suplanuoti iš anksto. Tai mūsų pačių darbo informacija, o ne faktai
apie miestą — todėl ją galima patikrinti ir ji nesensta taip greitai kaip statistika.
"""

PAPILDOMAI = {
    "vilnius": dict(
        formats="Sostinėje dažniausias užsakymas — konferencijos atidarymas arba vakarinė programa: robotas pasitinka svečius registracijoje, vėliau pasirodo scenoje su trumpu pristatymu, o pabaigoje dirba nuotraukų zonoje. Antras pagal dažnumą formatas — parodų stendas, kur robotas dirba ciklais visą dieną ir tampa priežastimi užsukti būtent pas jus.",
        logistics="Vilniuje beveik visada dirbame su renginių agentūromis arba objekto technine tarnyba, todėl atvykstame likus 60–90 minučių iki pradžios: reikia praeiti apsaugą, suderinti krovininį liftą ir patikrinti elektros tašką salėje. Sostinės objektuose dažnai prašoma techninės specifikacijos ir draudimo liudijimo iš anksto — abu dokumentus pateikiame patys, be atskiro priminimo."),
    "kaunas": dict(
        formats="Kaune vyrauja du scenarijai: gamybos ar inžinerinės įmonės šventė ir studentiškas arba universitetinis renginys. Pirmuoju atveju robotas dirba prie scenos ir apdovanojimų dalies, antruoju — laisvoje erdvėje, kur aplink jį susidaro nuolatinė eilė klausimų ir nuotraukų.",
        logistics="Gamyklos teritorijoje pasirodymą planuojame ne cecho viduryje, o prie įėjimo arba valgyklos zonos — ten yra lygios grindys ir elektra, o darbo srautas netrikdomas. Universitetų pastatuose svarbiausia iš anksto sutarti dėl liftų ir laiptų: robotą nešame dėžėje, kuri netelpa į siaurus senų pastatų liftus."),
    "klaipeda": dict(
        formats="Uostamiestyje dažniausiai užsakoma vasaros sezono programa: prekybos centro akcija, miesto šventės zona arba jūrinio verslo įmonės vakaras. Nuo gegužės iki rugsėjo dalis užsakymų sujungiami su Palanga — tą patį savaitgalį dirbame dviejose vietose.",
        logistics="Pajūryje visada sutariame atsarginę vidaus vietą: robotas puikiai dirba lauke, bet stiprus vėjas su smėliu ir lietus yra riba, kurios neperžengiame — tai įrangos sauga, ne kaprizas. Jei renginys vyksta ant kranto ar pontone, zoną tikriname iš anksto: reikia kietos, lygios dangos."),
    "siauliai": dict(
        formats="Šiauliuose stipriausiai veikia gamybos įmonių šventės ir miesto renginiai, kur svečiai renkasi bangomis. Tokiais atvejais dirbame ciklais: trumpas pasirodymas kas valandą, o tarp jų — nuotraukų zona su operatoriumi.",
        logistics="Regione dažnai tenka dirbti didelėse, aidinčiose erdvėse (arena, sporto salė), todėl garsą deriname su objekto technika iš anksto — kitaip roboto balsas paskęsta patalpos aide. Prašome numatyti 230 V lizdą ne toliau kaip 15 metrų nuo pasirodymo zonos."),
    "panevezys": dict(
        formats="Panevėžyje beveik visi užsakymai ateina iš gamybos sektoriaus: vasaros šventė darbuotojams su šeimomis, jubiliejus arba profesinio orientavimo diena. Šeimų formate planuojame trumpesnius, bet dažnesnius pasirodymus — vaikų dėmesys trumpas, o eilė nuotraukoms susidaro per kelias minutes.",
        logistics="Jei renginys vyksta įmonės teritorijoje, iš anksto suderiname įvažiavimą ir vietą prie įėjimo — robotą vežame mikroautobusu ir reikia sustoti arti durų. Employer branding atveju rekomenduojame numatyti fotografą: medžiaga iš šventės vėliau dirba darbuotojų paieškos kampanijose."),
    "alytus": dict(
        formats="Alytuje daugiausia dirbame bendruomeniniuose formatuose: miesto šventė, mokyklos ar gimnazijos renginys, prekybos centro akcija. Tai formatai, kuriuose robotas per dieną pamatomas didelės miesto dalies, o susidomėjimas išlieka vienodai didelis nuo pirmos iki paskutinės valandos.",
        logistics="Masiniuose renginiuose būtina pažymėta zona ir bent vienas jūsų žmogus eilei tvarkyti — operatorius vienas nespėja ir vesti pasirodymo, ir prižiūrėti minios. Lauko aikštėse tikriname dangą: trinkelės su dideliais tarpais robotui netinka."),
    "marijampole": dict(
        formats="Marijampolėje vyrauja logistikos ir žemės ūkio verslo renginiai bei profesinio mokymo karjeros dienos. Antruoju atveju robotas veikia kaip technologijų argumentas: mokiniai klausia apie valdymą, jutiklius ir programavimą, todėl operatorius skiria daugiau laiko paaiškinimams nei pačiam pasirodymui.",
        logistics="Miestas yra patogiame maršrute iš Lenkijos, todėl kelias dienas iš eilės vykstančius užsakymus regione deriname tarpusavyje. Jūsų kainai tai įtakos neturi — atvykimą vertiname pagal renginio vietą, o ne pagal tai, kiek dar dirbame tą savaitę."),
    "mazeikiai": dict(
        formats="Mažeikiuose dominuoja didelės pramonės įmonių šventės — kelių šimtų ar net tūkstančio žmonių formatas. Tokiuose renginiuose robotas dirba kaip vakaro akcentas: pasirodymas scenoje, o po jo ilga nuotraukų sesija, kuri trunka tiek, kiek yra norinčiųjų.",
        logistics="Atstumas nuo sostinės reiškia, kad išvykstame dieną anksčiau arba labai anksti ryte — dėl to prašome patvirtinti datą bent prieš tris savaites. Didelėse šventėse rekomenduojame du trumpesnius pasirodymus vietoj vieno ilgo, kad robotą pamatytų ir vėliau atvykę svečiai."),
    "jonava": dict(
        formats="Jonavoje daugiausia užsakymų iš chemijos pramonės įmonių ir miesto bendruomenės renginių, dažnai orientuotų į šeimas. Šeimų formate robotas dirba trumpais ciklais, o tarp jų vyksta nuotraukų zona — tai leidžia išlaikyti tvarką ir nesudaryti spūsties.",
        logistics="Iki Kauno vos pusvalandis, todėl Jonavos renginius neretai deriname su tos pačios savaitės užsakymais Kaune — logistiškai tai paprasčiausias regionas Lietuvoje. Vidaus erdvėse pakanka 2×2 m ir lizdo; lauke — kietos dangos."),
    "utena": dict(
        formats="Utenoje persipina du sezonai: šiltuoju metu — lauko renginiai prie ežerų ir sodybose, šaltuoju — gamybos įmonių šventės ir miesto kultūros renginiai. Sodybų formatas reikalauja daugiausia planavimo, bet duoda geriausią vaizdinę medžiagą.",
        logistics="Sodybose ir prie vandens elektros tašką tikriname iš anksto — generatorius be stabilizatoriaus robotui netinka. Zoną renkamės atokiau nuo kranto ir smėlio: drėgna ar biri danga trukdo judėti, o vakare reikia bent minimalaus apšvietimo pasirodymui."),
    "kedainiai": dict(
        formats="Kėdainiuose dažniausi užsakymai — didelių chemijos ir žemės ūkio įmonių vakarai bei reprezentaciniai miesto renginiai senamiestyje. Reprezentaciniame formate robotas dirba tyliau ir trumpiau: pasitinka svečius ir pasirodo vieną kartą, be ilgos pramoginės dalies.",
        logistics="Senamiesčio erdvėse zoną derinam su objekto administracija iš anksto — istorinis grindinys robotui netinka, todėl ieškome lygaus paviršiaus arba naudojame podiumą. Įmonių teritorijose apribojimų paprastai nėra, svarbu tik įvažiavimas ir elektra."),
    "telsiai": dict(
        formats="Telšiuose ir aplinkiniame regione vyrauja kultūros bei bendruomenės renginiai, o šalia jų — gamybos įmonių šventės. Kultūros formate robotas dažnai naudojamas kaip kontrastas tradicijai: tai duoda stipriausią vaizdinę istoriją ir geriausiai veikia socialiniuose tinkluose.",
        logistics="Žemaitijoje atstumai tarp objektų dideli, todėl vieną dieną planuojame vieną renginį — jokių skubotų persikėlimų iš miesto į miestą. Jei pasirodymas vyksta dvaro ar muziejaus erdvėje, iš anksto suderiname, kur robotas gali judėti, o kur ne."),
    "taurage": dict(
        formats="Tauragėje dažniausiai dirbame logistikos ir gamybos įmonių renginiuose bei miesto šventėse. Verslo formatas čia trumpas ir konkretus: pasirodymas, keli klausimai apie technologiją ir nuotraukos — be ilgos scenarijaus dalies.",
        logistics="Miestas yra patogiame maršrute link pajūrio, todėl vasaros sezonu užsakymus deriname su Klaipėdos ir Palangos renginiais. Sandėlių ir gamyklų erdvėse svarbiausia lygi danga: robotui netinka nelygus betonas su siūlėmis ir nuolydžiais."),
    "palanga": dict(
        formats="Palangoje sezonas trumpas ir intensyvus: įmonių išvažiuojamieji renginiai, konferencijos prie jūros ir vestuvės. Vestuvių formate robotas dirba per svečių pasitikimą ir vakarinę dalį — tai du trumpi pasirodymai, o ne viena ilga programa.",
        logistics="Birželio–rugpjūčio savaitgaliai užsipildo anksčiausiai visoje Lietuvoje, todėl dėl datos rekomenduojame kreiptis prieš 2–3 mėnesius. Terasose ir lauko scenose visada sutariame atsarginį planą lietui, o vakariniam pasirodymui prašome numatyti apšvietimą — tamsoje robotas atrodo įspūdingai tik tada, kai jį matyti."),
    "druskininkai": dict(
        formats="Druskininkuose dominuoja dviejų dienų formatas: pirmą dieną darbo sesijos ir vakaro programa, antrą — laisvalaikio dalis. Robotą dažniausiai įtraukiame į vakaro programą ir kitos dienos atidarymą, todėl viena nuoma padengia du skirtingus renginio momentus.",
        logistics="Dviem dienoms siūlome tą patį operatorių abiem dienoms — tai pigiau ir logistiškai paprasčiau nei du atskiri užsakymai, o robotas lieka objekte per naktį saugioje patalpoje. SPA ir vandens zonose nedirbame: drėgmė ir slidžios grindys yra riba, kurios neperžengiame."),
    "trakai": dict(
        formats="Trakuose beveik visi užsakymai yra išvažiuojamieji įmonių renginiai ir vestuvės prie ežerų. Aplinka čia vaizdinga, todėl robotą planuojame ten, kur kadras natūraliai gražus — prie vandens, terasoje arba sodybos kieme, o ne uždaroje salėje.",
        logistics="Sodybose ir prie ežerų tikriname du dalykus: elektros prieigą ir dangą. Mediniai pontonai, žvyras ir šlaitai netinka — zoną parenkame kartu iš anksto pagal nuotraukas. Nuo Vilniaus vos pusvalandis, todėl atvykimas čia yra vienas pigiausių šalyje."),
    "birstonas": dict(
        formats="Birštone vyrauja nedidelės konferencijos ir įmonių išvažiuojamosios sesijos — dažnai 30–80 žmonių. Kompaktiškose erdvėse robotas pastebimas iš karto, todėl scenarijų darome trumpesnį: vienas pasirodymas ir ilgesnė laisva dalis, kurios metu žmonės patys prieina.",
        logistics="Kurorto viešbučiuose salės nedidelės, todėl zonai pakanka 2×2 m, bet svarbu, kad ji nebūtų tarp stalų — robotui reikia kelio, kuriuo prieitų prie svečių. Dviejų dienų formatui siūlome tą patį paketą kaip Druskininkuose."),
    "anyksciai": dict(
        formats="Anykščiuose sezonas ilgas, o auditorija — turistinė: robotas dažniausiai užsakomas savaitgaliams prie turizmo objektų, kur dirba ciklais visą dieną. Antras formatas — miesto ir bendruomenės šventės, kuriose pasirodymas įtraukiamas į bendrą programą.",
        logistics="Turizmo objektuose svarbiausia suderinti vietą su lankytojų srautu: robotas turi būti matomas, bet netrukdyti praėjimo. Visą dieną trunkantiems užsakymams planuojame baterijų keitimo pertraukas kas kelias valandas — tam reikia uždaros patalpos su lizdu netoli pasirodymo zonos."),
}
