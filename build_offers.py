# -*- coding: utf-8 -*-
"""33bots.lt paslaugų (landing) puslapiai."""
from lt_common import (SITE, head, body_open, nav, crumbs, breadcrumb_ld, contact_section,
                       footer, faq_section, faq_ld, organization_ld, video_section,
                       service_ld, write, CITIES, city_url)

CITY_CHIPS = "\n".join(
    f'      <a href="{city_url(s)}">{n}</a>' for s, n, _, _ in CITIES[:10]
)

PAGES = [
    dict(
        slug="humanoidinio-roboto-nuoma.html",
        title="Humanoidinio roboto nuoma — Unitree G1 visoje Lietuvoje | 33bots",
        desc="Humanoidinio roboto Unitree G1 nuoma visoje Lietuvoje. Operatorius, transportas ir "
             "ženklinimas įskaičiuoti į kainą. Pasiūlymas per 24 val.",
        keywords="humanoidinio roboto nuoma, roboto nuoma, robotų nuoma Lietuvoje, Unitree G1 nuoma",
        crumb="Humanoidinio roboto nuoma",
        eyebrow="Humanoidinio roboto nuoma · Visa Lietuva",
        h1="Humanoidinio roboto<br />nuoma —<br /><em>Unitree G1.</em>",
        lead="Vienas robotas, viena atsakomybė, viena sąskaita. Atvežame Unitree G1 į jūsų renginį bet "
             "kurioje Lietuvos vietoje, paskiriame operatorių ir pasirūpiname visa technine puse — "
             "nuo paruošimo iki išvykimo.",
        tag="Nuoma",
        benefits_title="Ką gaunate<br />išsinuomoję",
        benefits=[
            ("Pilna paslauga", "Robotas neatvyksta dėžėje su instrukcija. Atvažiuoja operatorius, "
                               "kuris paruošia, valdo ir prižiūri robotą visą renginio laiką."),
            ("Nemokamas transportas", "Vilnius, Kaunas, Klaipėda ar mažas miestelis — atvykimo kaina "
                                      "ta pati: nulis eurų. Be kilometrų limito ir minimalaus atstumo."),
            ("Ženklinimas be priemokų", "Jūsų logotipas ir QR kodas ant roboto krūtinės, spalvinis "
                                        "akcentas ir pritaikyta programa — įskaičiuota į nuomos kainą."),
            ("Draudimas ir sauga", "Veiklai taikoma civilinės atsakomybės draudimo apsauga, o robotas "
                                   "LiDAR jutikliais realiu laiku aptinka žmones ir kliūtis."),
            ("Lankstūs paketai", "Nuo trijų valandų pasirodymo iki kelių dienų parodos. Mokate už tai, "
                                 "ko iš tikrųjų reikia, be primestų priedų."),
            ("Atsakymas per 24 val.", "Užklausas peržiūrime kiekvieną darbo dieną. Gaunate konkrečią "
                                      "kainą ir laisvas datas, o ne bendrą kainoraštį."),
        ],
        body_h2_1="Kas yra humanoidinio roboto nuoma",
        body_1="<p>Humanoidinio roboto nuoma — tai paslauga, kai renginio dienai gaunate ne tik įrangą, "
               "bet ir komandą, kuri ją valdo. 33bots atveju tai reiškia robotą <strong>Unitree G1</strong>, "
               "sertifikuotą operatorių, transportą, paruošimą vietoje ir pasirodymo scenarijų, suderintą "
               "su jūsų renginio programa.</p>"
               "<p>Skirtingai nei perkant robotą, nuomos atveju nereikia investuoti į įrangą, mokymus, "
               "servisą ir sandėliavimą. Mokate už konkretų renginį, o visa rizika bei techninė priežiūra "
               "lieka mūsų pusėje. Detalų kaštų palyginimą rasite straipsnyje "
               "<a href=\"blog-kiek-kainuoja-roboto-nuoma.html\">kiek kainuoja roboto nuoma</a>.</p>",
        body_h2_2="Kam dažniausiai nuomojamas robotas",
        body_2="<p>Dažniausi scenarijai Lietuvoje — <a href=\"robotas-parodoms.html\">parodų stendai</a>, "
               "<a href=\"robotas-konferencijai.html\">konferencijos ir gala vakarai</a>, "
               "<a href=\"robotas-atidarymui.html\">atidarymai bei produktų pristatymai</a> ir "
               "<a href=\"robotas-imones-sventei.html\">įmonių šventės</a>. Vis dažniau robotas nuomojamas "
               "ir turinio gamybai: reklaminėms sesijoms, vaizdo klipams bei socialinių tinklų kampanijoms.</p>"
               "<p>Nesvarbu, koks formatas — logika ta pati: robotas sustabdo žmones, o jūsų komanda gauna "
               "progą pradėti pokalbį. Tai vienintelė renginio pramoga, kuri vienu metu veikia kaip "
               "atrakcija, turinio šaltinis ir kontaktų generavimo įrankis.</p>",
        faq=[
            ("Kokiam laikui galima išsinuomoti robotą?",
             "Nuo kelių valandų iki kelių savaičių. Trumpiausias standartinis paketas — iki 3 valandų, "
             "populiariausias — visa renginio diena (iki 8 val.), o parodoms siūlome kelių dienų nuomą "
             "su tuo pačiu operatoriumi."),
            ("Ar reikia savo darbuotojo robotui valdyti?",
             "Ne. Robotą valdo mūsų operatorius, kuris atvyksta kartu su įranga. Jūsų komandai lieka tik "
             "renginio turinys — techninė pusė yra mūsų atsakomybė."),
            ("Ar galima išsinuomoti kelis robotus vienu metu?",
             "Taip, didesniems projektams galime skirti daugiau nei vieną robotą su atskirais operatoriais. "
             "Tokius užsakymus rekomenduojame derinti bent kelias savaites iš anksto."),
            ("Ar nuoma apima roboto programavimą pagal mūsų scenarijų?",
             "Taip. Prieš renginį aptariame, ko norite: pasitikti svečius, vesti trumpą pasirodymą, šokti "
             "su publika ar dirbti prie stendo. Pagal tai paruošiame veiksmų seką ir ženklinimą."),
            ("Kas atsitiks, jei renginys bus atšauktas?",
             "Sutartyje aiškiai numatome atšaukimo sąlygas ir datų perkėlimo galimybę. Stengiamės būti "
             "lankstūs — ypač jei renginys keliamas, o ne atšaukiamas visiškai."),
        ],
        related=[("robotas-renginiui.html", "Robotas renginiui"),
                 ("robotas-parodoms.html", "Robotas parodoms"),
                 ("robotas-konferencijai.html", "Konferencijos ir gala"),
                 ("kainos.html", "Kas įeina į kainą"),
                 ("blog-kaip-issinuomoti-robota.html", "Nuomos vadovas")],
    ),
    dict(
        slug="robotas-renginiui.html",
        title="Robotas renginiui — humanoidas, kuris sustabdo minią | 33bots",
        desc="Robotas renginiui visoje Lietuvoje: Unitree G1 pasitinka svečius, veda pasirodymą ir "
             "šoka. Operatorius ir transportas kainoje.",
        keywords="robotas renginiui, robotas į renginį, renginių pramoga, humanoidas renginyje",
        crumb="Robotas renginiui",
        eyebrow="Robotas renginiui · Pramoga, apie kurią kalbama",
        h1="Robotas renginiui,<br />kuris sustabdo<br /><em>minią.</em>",
        lead="Konferencija, atidarymas, gala vakaras ar vasaros šventė — humanoidinis robotas Unitree G1 "
             "tampa renginio centru per pirmas penkias minutes. Ir lieka juo iki pabaigos.",
        tag="Renginiai",
        benefits_title="Kodėl robotas<br />veikia renginyje",
        benefits=[
            ("Pirmas įspūdis", "Robotas pasitinka svečius prie įėjimo, sveikinasi ir nukreipia. Renginys "
                               "prasideda nuo emocijos, o ne nuo registracijos eilės."),
            ("Programos taškas", "Trumpas pasirodymas scenoje tarp pranešimų atgaivina salę geriau nei "
                                 "kavos pertrauka. Choreografija derinama su jūsų muzika."),
            ("Turinio mašina", "Kiekvienas svečias nufilmuoja robotą. Jūsų renginys plinta socialiniuose "
                               "tinkluose be papildomo reklamos biudžeto."),
            ("Pokalbio pradžia", "Svečiai lengviau užkalba vieni kitus ir jūsų komandą, kai turi bendrą "
                                 "temą. Robotas nulaužia ledus greičiau nei bet kuris moderatorius."),
            ("Prekės ženklo signalas", "Įmonė, kuri į renginį atveža humanoidą, komunikuoja inovatyvumą "
                                       "be nė vienos skaidrės."),
            ("Veikia bet kur", "Konferencijų salė, sandėlis, lauko scena ar prekybos centro atriumas — "
                               "robotas puikiai juda ant įvairių paviršių."),
        ],
        body_h2_1="Kaip robotas įsilieja į renginio programą",
        body_1="<p>Prieš renginį aptariame scenarijų: kada robotas pasirodo, ką daro ir kaip bendrauja su "
               "svečiais. Populiariausias formatas — <strong>trys trumpi pasirodymai</strong> per dieną: "
               "svečių pasitikimas, pasirodymas scenoje ir laisvas bendravimas per networking dalį.</p>"
               "<p>Tarp pasirodymų robotas lieka prieinamas nuotraukoms — tai natūraliai sukuria eilę prie "
               "jūsų stendo ar zonos. Operatorius valdo tempą taip, kad robotas visada atrodytų šviežiai, "
               "o baterijos keitimas nepatektų į renginio kulminaciją.</p>",
        body_h2_2="Kokiems renginiams tinka labiausiai",
        body_2="<p>Geriausiai pasiteisina renginiai, kur svarbus <strong>WOW efektas ir turinys</strong>: "
               "<a href=\"robotas-konferencijai.html\">konferencijos</a>, "
               "<a href=\"robotas-parodoms.html\">parodos</a>, "
               "<a href=\"robotas-atidarymui.html\">atidarymai</a>, "
               "<a href=\"robotas-imones-sventei.html\">įmonių šventės</a> ir net "
               "<a href=\"robotas-vestuvems.html\">vestuvės</a>.</p>"
               "<p>Jei nesate tikri, ar robotas tinka jūsų formatui — parašykite. Dažnai pasiūlome "
               "konkretų scenarijų dar prieš pasiūlymą, kad galėtumėte įsivaizduoti rezultatą. "
               "Palyginimą su kitomis pramogomis rasite "
               "<a href=\"blog-robotas-ar-kitos-pramogos.html\">šiame straipsnyje</a>.</p>",
        faq=[
            ("Kiek vietos reikia robotui renginyje?",
             "Minimaliai apie 2×2 m saugios erdvės pasirodymui ir standartinis 230 V lizdas. Didesnei "
             "choreografijai patogiau turėti 4×4 m, bet tai nėra būtina sąlyga."),
            ("Ar robotas gali kalbėti su svečiais?",
             "Taip — robotą galima paruošti trumpiems pasisakymams ir pasisveikinimams, taip pat "
             "reaguoti į svečius operatoriaus valdymu. Turinį suderiname iš anksto."),
            ("Ar robotas veikia lauke?",
             "Taip, esant sausam orui robotas puikiai juda asfaltu, plytelėmis ir net trumpa žole. "
             "Lietaus atveju rekomenduojame numatyti stogelį arba vidaus alternatyvą."),
            ("Kiek iš anksto reikia rezervuoti?",
             "Populiariausiais mėnesiais (rugsėjis–gruodis, gegužė–birželis) rekomenduojame kreiptis "
             "bent 3–4 savaites iš anksto. Skubiems atvejams visada verta paskambinti."),
            ("Ar galime robotą naudoti savo prekės ženklo komunikacijai?",
             "Būtinai. Ženklinimas logotipu ir QR kodu įskaičiuotas, o pasirodymo scenarijų galime "
             "pritaikyti prie kampanijos žinutės."),
        ],
        related=[("humanoidinio-roboto-nuoma.html", "Nuomos sąlygos"),
                 ("robotas-imones-sventei.html", "Įmonės šventė"),
                 ("video-realizacijos.html", "Vaizdo įrašai"),
                 ("kainos.html", "Kainos"),
                 ("blog-kodel-robotas-renginyje.html", "Kodėl robotas renginyje")],
    ),
    dict(
        slug="robotas-parodoms.html",
        title="Robotas parodoms — daugiau lankytojų prie stendo | 33bots",
        desc="Humanoidinis robotas parodų stende: sustabdo lankytojų srautą ir padeda rinkti kontaktus. "
             "Kelių dienų nuoma su operatoriumi ir transportu.",
        keywords="robotas parodoms, robotas parodų stende, robotas mugėms, parodos stendas, LITEXPO robotas",
        crumb="Robotas parodoms",
        eyebrow="Robotas parodoms · Stendas, pro kurį nepraeisi",
        h1="Robotas parodoms —<br />stendas, pro kurį<br /><em>nepraeisi.</em>",
        lead="Parodoje laimi ne gražiausias stendas, o tas, prie kurio žmonės sustoja. Humanoidinis robotas "
             "Unitree G1 sustabdo srautą fiziškai — o jūsų komandai lieka pradėti pokalbį.",
        tag="Parodos",
        benefits_title="Ką robotas duoda<br />parodų stendui",
        benefits=[
            ("Srauto stabdymas", "Lankytojai sustoja patys, be flaierių ir be hostesių, kurios kabina "
                                 "praeivius. Prie stendo susidaro natūrali minia."),
            ("Ilgesnis kontaktas", "Vidutinis laikas prie stendo pailgėja kelis kartus — o kiekviena "
                                   "papildoma minutė yra proga kvalifikuoti kontaktą."),
            ("QR kodas ant roboto", "Ženklinimas apima QR kodą, vedantį į jūsų nusileidimo puslapį, "
                                    "katalogą arba kontaktų formą. Nuskaitymai matomi analitikoje."),
            ("Kelių dienų paketas", "Robotas lieka visai parodai su tuo pačiu operatoriumi. Nereikia "
                                    "kasdien iš naujo derinti logistikos."),
            ("Turinys iš parodos", "Įrašai iš stendo tinka socialiniams tinklams ir po parodos — "
                                   "kampanija tęsiasi, kai konkurentų stendai jau išardyti."),
            ("Konkurencinis skirtumas", "Kol kiti dalina tušinukus, jūs turite vienintelį humanoidą "
                                        "salėje. Lankytojai prisimena būtent tai."),
        ],
        body_h2_1="Kaip suplanuoti robotą stende",
        body_1="<p>Svarbiausias sprendimas — <strong>roboto vieta stende</strong>. Geriausiai veikia "
               "pozicija ties stendo kraštu, matoma iš pagrindinio praėjimo, su bent 2×2 m laisvos erdvės. "
               "Robotas turi būti matomas iš toli, bet ne blokuoti įėjimo į stendą.</p>"
               "<p>Antras sprendimas — <strong>pasirodymų grafikas</strong>. Rekomenduojame fiksuotas "
               "valandas (pvz. kas valandą po 10 minučių) ir tai paskelbti stende bei socialiniuose "
               "tinkluose. Lankytojai grįžta konkrečiu laiku, o jūsų komanda gali planuoti susitikimus.</p>",
        body_h2_2="Kontaktų rinkimas aplink robotą",
        body_2="<p>Robotas pritraukia dėmesį, bet kontaktus surenka jūsų komanda. Praktikoje geriausiai "
               "veikia paprastas mainų principas: nuotrauka su robotu mainais už trumpą registraciją, "
               "arba QR kodo nuskaitymas dėl konkrečios naudos — pasiūlymo, demonstracijos, katalogo.</p>"
               "<p>Daugiau praktinių mechanikų aprašėme straipsnyje "
               "<a href=\"blog-robotas-parodu-stende.html\">robotas parodų stende — kaip generuoti "
               "kontaktus</a>. Jei planuojate ir konferencijos dalį, palyginkite scenarijus "
               "<a href=\"robotas-konferencijai.html\">konferencijų puslapyje</a>.</p>",
        faq=[
            ("Ar robotas gali dirbti visas parodos dienas?",
             "Taip. Kelių dienų paketas apima robotą, operatorių ir transportą visoms parodos dienoms. "
             "Baterijos keičiamos per suplanuotas pertraukas, todėl stendas nelieka tuščias."),
            ("Ar reikia atskiro leidimo iš parodos organizatoriaus?",
             "Paprastai pakanka standartinio stendo derinimo. Kai kurie organizatoriai prašo informacijos "
             "apie įrangos galią ir saugą — visus dokumentus pateikiame iš anksto."),
            ("Kokio dydžio stendui robotas tinka?",
             "Nuo maždaug 9 m² stendo. Mažesniuose stenduose robotas dirba statiškai (pasisveikinimai, "
             "nuotraukos), didesniuose — su pilna choreografija."),
            ("Ar robotas triukšmauja?",
             "Ne, roboto judesiai tylūs ir netrukdo pokalbiams stende. Garsą kontroliuojame per savo "
             "kolonėlę, kurios garsumą galima laisvai reguliuoti."),
            ("Ar galime robotą naudoti pristatymui scenoje parodos metu?",
             "Taip — daug klientų derina stendo darbą su trumpu pasirodymu parodos scenoje. Tai "
             "suplanuojame kartu su jūsų programa."),
        ],
        related=[("robotas-konferencijai.html", "Konferencijos"),
                 ("humanoidinio-roboto-nuoma.html", "Nuomos sąlygos"),
                 ("robotu-nuoma-vilnius.html", "Robotas Vilniuje"),
                 ("kainos.html", "Kainos"),
                 ("blog-robotas-parodu-stende.html", "Kontaktų rinkimo vadovas")],
    ),
    dict(
        slug="robotas-konferencijai.html",
        title="Robotas konferencijai ir gala vakarui — Unitree G1 | 33bots",
        desc="Humanoidinis robotas konferencijoje ar gala vakare: pasitinka svečius ir tampa programos "
             "akcentu. Nuoma visoje Lietuvoje su operatoriumi.",
        keywords="robotas konferencijai, robotas gala vakarui, konferencijos pramoga, renginio vedėjas robotas",
        crumb="Konferencijos ir gala vakarai",
        eyebrow="Konferencijos ir gala vakarai · Programa, kuri įsimena",
        h1="Robotas konferencijai<br />ir gala vakarui —<br /><em>programa, kuri įsimena.</em>",
        lead="Geriausios konferencijos prisimenamos ne dėl skaidrių. Humanoidinis robotas Unitree G1 tampa "
             "programos akcentu, kurį svečiai mini dar savaitėmis po renginio.",
        tag="Konferencijos",
        benefits_title="Robotas konferencijos<br />programoje",
        benefits=[
            ("Svečių registracija", "Robotas pasitinka atvykstančius, sveikinasi ir sukuria eilę, kurioje "
                                    "žmonės nesierzina, o filmuoja."),
            ("Scenos akcentas", "Trumpas pasirodymas prieš pagrindinį pranešėją arba po pertraukos — "
                                "salė vėl susikaupia be jokių raginimų."),
            ("Gala vakaro kulminacija", "Šokio pasirodymas su DJ muzika arba apdovanojimų įteikimo dalis "
                                        "su robotu — vakaro momentas, kuris patenka į visų telefonus."),
            ("Networking katalizatorius", "Per kavos pertraukas robotas veikia kaip magnetas, aplink kurį "
                                          "natūraliai užsimezga pokalbiai."),
            ("Rėmėjų vertė", "Robotas su rėmėjo ženklinimu suteikia partneriui matomumą, kurio neduoda "
                             "logotipas ant roll-up'o."),
            ("Turinys po renginio", "Įrašai iš pasirodymo tinka ataskaitai rėmėjams ir kitų metų "
                                    "renginio reklamai."),
        ],
        body_h2_1="Kaip robotą įtraukti į konferencijos scenarijų",
        body_1="<p>Konferencijoje robotas veikia geriausiai, kai turi <strong>aiškias laiko juostas</strong>. "
               "Klasikinis planas: 30 minučių prie registracijos, 5–7 minučių pasirodymas atidaryme, "
               "laisvas bendravimas per pietų pertrauką ir finalinis akcentas prieš uždarymą.</p>"
               "<p>Gala vakaruose logika kitokia — svarbiausias yra vienas stiprus momentas. Dažniausiai tai "
               "šokio pasirodymas po vakarienės arba roboto pasirodymas įteikiant pagrindinį apdovanojimą. "
               "Operatorius derina laiką su renginio vedėju ir technikos komanda.</p>",
        body_h2_2="Ką paruošti iš organizatoriaus pusės",
        body_2="<p>Reikia nedaug: 230 V lizdo, maždaug 2×2 m saugios erdvės, prieigos į salę likus "
               "45 minutėms iki pasirodymo ir kontakto su garso technikais, jei robotas pasirodo scenoje. "
               "Visa kita — mūsų atsakomybė.</p>"
               "<p>Jei renginys apima ir parodinę dalį, apžiūrėkite "
               "<a href=\"robotas-parodoms.html\">roboto parodoms pasiūlymą</a>, o dėl datų ir kainos "
               "žiūrėkite <a href=\"kainos.html\">kainų puslapį</a>. Konferencijas Vilniuje aptariame "
               "<a href=\"robotu-nuoma-vilnius.html\">atskirame puslapyje</a>.</p>",
        faq=[
            ("Ar robotas gali vesti renginio dalį?",
             "Robotas gali pristatyti pranešėją, pasakyti trumpą tekstą ir atlikti pasirodymą. Pilną "
             "vedimą rekomenduojame palikti žmogui — robotas veikia stipriausiai kaip akcentas, o ne "
             "kaip visos programos vedėjas."),
            ("Ar galima roboto tekstą pritaikyti mūsų renginiui?",
             "Taip. Prieš renginį suderiname pasisakymų turinį, kalbą ir toną. Tekstus galime paruošti "
             "lietuvių arba anglų kalba."),
            ("Kiek trunka pasiruošimas salėje?",
             "Apie 30–45 minutes. Per tą laiką patikriname erdvę, garsą ir atliekame bandomąjį paleidimą, "
             "kad pasirodymas vyktų be netikėtumų."),
            ("Ar robotas tinka formaliam gala vakarui?",
             "Taip — pasirodymo tonas visiškai priklauso nuo scenarijaus. Formaliems vakarams renkamės "
             "santūresnę choreografiją ir trumpesnį pasirodymą."),
            ("Ar galite dirbti su mūsų renginių agentūra?",
             "Žinoma. Dažnai dirbame kaip subrangovai agentūroms — pateikiame visą techninę informaciją, "
             "rizikos vertinimą ir derinamės su gamybos komanda."),
        ],
        related=[("robotas-renginiui.html", "Robotas renginiui"),
                 ("robotas-parodoms.html", "Parodos"),
                 ("robotas-imones-sventei.html", "Įmonės šventė"),
                 ("video-realizacijos.html", "Vaizdo įrašai"),
                 ("kainos.html", "Kainos")],
    ),
    dict(
        slug="robotas-imones-sventei.html",
        title="Robotas įmonės šventei ir komandos renginiui | 33bots",
        desc="Humanoidinis robotas įmonės šventėje, vasaros renginyje ar jubiliejuje — pramoga, kurios "
             "nepamiršta. Nuoma visoje Lietuvoje su operatoriumi.",
        keywords="robotas įmonės šventei, komandos renginys, vasaros šventė, jubiliejus, darbuotojų renginys",
        crumb="Įmonės šventės",
        eyebrow="Įmonės šventės · Pramoga, kurios nepamiršta",
        h1="Robotas įmonės<br />šventei —<br /><em>pramoga be klišių.</em>",
        lead="Kiekvienais metais tas pats fokusnininkas ir ta pati grupė? Humanoidinis robotas yra pramoga, "
             "kurios dauguma jūsų kolegų dar niekada nematė gyvai.",
        tag="Įmonės šventės",
        benefits_title="Kodėl robotas veikia<br />darbuotojų renginyje",
        benefits=[
            ("Visiems įdomu", "Robotas veikia visose amžiaus grupėse ir visuose skyriuose — nuo IT iki "
                              "gamybos. Nereikia rinktis, kam patiks."),
            ("Ledlaužis", "Naujoje komandoje arba po susijungimo robotas duoda bendrą temą, nuo kurios "
                          "prasideda pokalbiai."),
            ("Šokių aikštelė", "Su DJ muzika robotas perima aikštelę ir įtraukia net tuos, kurie "
                               "paprastai nešoka."),
            ("Nuotraukos komandai", "Bendros nuotraukos su robotu tampa vidinės komunikacijos turiniu ir "
                                    "employer branding medžiaga."),
            ("Employer branding", "Įrašai iš šventės rodo, kad jūsų įmonė investuoja į darbuotojų patirtį — "
                                  "tai mato ir kandidatai."),
            ("Vidus ar laukas", "Restoranas, sodyba, gamyklos aikštelė ar biuro terasa — robotas prisitaiko "
                                "prie erdvės."),
        ],
        body_h2_1="Formatai, kurie veikia įmonių šventėse",
        body_1="<p>Populiariausias variantas — <strong>robotas kaip vakaro akcentas</strong>: pasirodymas "
               "po vakarienės, kai svečiai jau atsipalaidavę, ir po jo laisvas bendravimas su nuotraukomis. "
               "Toks formatas užima 2–3 valandas ir dažniausiai telpa į standartinį paketą.</p>"
               "<p>Antras dažnas variantas — <strong>robotas visą dieną</strong> vasaros šventėje ar "
               "atvirų durų dienoje, kai svečiai renkasi bangomis. Tada robotas dirba ciklais: trumpas "
               "pasirodymas kas valandą ir nuotraukų zona tarp jų.</p>",
        body_h2_2="Jubiliejai ir apdovanojimų vakarai",
        body_2="<p>Įmonės jubiliejuje robotas gali dalyvauti simboliniame momente — įnešti apdovanojimą, "
               "pradėti atgalinį skaičiavimą arba pristatyti vadovą. Tai suteikia vakarui kulminaciją, "
               "kurios nereikia aiškinti.</p>"
               "<p>Jei planuojate formalesnį renginį su pranešimais, žiūrėkite "
               "<a href=\"robotas-konferencijai.html\">konferencijų ir gala vakarų pasiūlymą</a>. "
               "Vestuvėms turime <a href=\"robotas-vestuvems.html\">atskirą puslapį</a>.</p>",
        faq=[
            ("Ar robotas tinka šventei sodyboje už miesto?",
             "Taip. Transportas įskaičiuotas nepriklausomai nuo atstumo, o robotas juda ir kietu grindiniu, "
             "ir trumpa žole. Reikia tik elektros lizdo netoliese."),
            ("Kiek žmonių renginyje yra optimalu?",
             "Robotas gerai veikia nuo 30 iki kelių šimtų svečių. Didesniems renginiams rekomenduojame "
             "planuoti kelis trumpesnius pasirodymus vietoj vieno ilgo."),
            ("Ar robotas gali dalyvauti komandos formavimo žaidimuose?",
             "Taip — galime paruošti trumpas interaktyvias veiklas, kuriose komandos varžosi arba atlieka "
             "užduotis kartu su robotu."),
            ("Ar galima robotą ženklinti mūsų vidiniu logotipu ar šventės identitetu?",
             "Taip, ir tai nekainuoja papildomai. Dažnai klientai naudoja šventės logotipą ar šūkį."),
            ("Ar dirbate ir savaitgaliais bei vakarais?",
             "Taip. Dauguma įmonių švenčių vyksta penktadienių vakarais ir šeštadieniais — tai mums "
             "įprastas darbo laikas."),
        ],
        related=[("robotas-renginiui.html", "Robotas renginiui"),
                 ("robotas-vestuvems.html", "Vestuvės"),
                 ("robotas-konferencijai.html", "Gala vakarai"),
                 ("kainos.html", "Kainos"),
                 ("video-realizacijos.html", "Vaizdo įrašai")],
    ),
    dict(
        slug="robotas-atidarymui.html",
        title="Robotas atidarymui ir produkto pristatymui | 33bots",
        desc="Humanoidinis robotas parduotuvės atidaryme ar produkto pristatyme — pritraukia praeivius "
             "ir žiniasklaidą. Nuoma visoje Lietuvoje.",
        keywords="robotas atidarymui, produkto pristatymas, parduotuvės atidarymas, rinkodaros kampanija robotas",
        crumb="Atidarymai ir pristatymai",
        eyebrow="Atidarymai ir pristatymai · Dėmesys pirmą dieną",
        h1="Robotas atidarymui —<br />dėmesys jau<br /><em>pirmą dieną.</em>",
        lead="Naujos vietos ar produkto atidarymas turi tik vieną progą sukurti pirmą įspūdį. Humanoidinis "
             "robotas paverčia praeivius lankytojais, o lankytojus — turinio kūrėjais.",
        tag="Atidarymai",
        benefits_title="Ką robotas duoda<br />atidarymui",
        benefits=[
            ("Praeivių stabdymas", "Prekybos centre ar gatvėje robotas veikia kaip gyva iškaba — žmonės "
                                   "sustoja patys, be dalomosios medžiagos."),
            ("Žiniasklaidos kabliukas", "Robotas atidaryme yra vaizdinė istorija, kurią vietinė "
                                        "žiniasklaida noriai filmuoja."),
            ("Eilė, kuri atrodo gerai", "Susidariusi minia pati savaime signalizuoja, kad vieta verta "
                                        "dėmesio."),
            ("Produkto kontekstas", "Robotą galima integruoti į pristatymo scenarijų — nuo juostelės "
                                    "perkirpimo iki produkto pateikimo."),
            ("Kampanijos turinys", "Įrašai iš atidarymo naudojami visą kampaniją, ne tik atidarymo dieną."),
            ("Ženklinimas įskaičiuotas", "Logotipas ir QR kodas ant roboto veda tiesiai į akciją, "
                                         "registraciją ar el. parduotuvę."),
        ],
        body_h2_1="Atidarymo scenarijus su robotu",
        body_1="<p>Standartinis planas: robotas dirba prie įėjimo pusvalandį prieš oficialią pradžią, "
               "dalyvauja <strong>simboliniame atidarymo momente</strong>, tada 2–3 valandas bendrauja su "
               "lankytojais nuotraukų zonoje. Jei atidarymas trunka visą dieną, dalijame į ciklus.</p>"
               "<p>Prekybos centruose svarbu iš anksto suderinti vietą su administracija — robotui reikia "
               "matomos, bet nekliudančios pozicijos ir elektros prieigos. Visą techninę informaciją "
               "pateikiame dokumentu, kurį galite persiųsti centro vadybininkui.</p>",
        body_h2_2="Produkto pristatymai ir rinkodaros kampanijos",
        body_2="<p>B2B pristatymuose robotas dažnai naudojamas kaip <strong>metafora</strong>: technologijų "
               "įmonė pristato naują sprendimą kartu su humanoidu, ir žinutė apie inovaciją perduodama be "
               "vienos skaidrės. Retail'e robotas dirba kaip demonstratorius prie naujo produkto.</p>"
               "<p>Ilgesnėms kampanijoms siūlome kelių dienų nuomą su tuo pačiu operatoriumi — žr. "
               "<a href=\"humanoidinio-roboto-nuoma.html\">nuomos sąlygas</a>. Turinio gamybai skirtas "
               "sesijas taip pat aptariame individualiai.</p>",
        faq=[
            ("Ar robotas gali dirbti prekybos centro atriume?",
             "Taip, tai vienas dažniausių scenarijų. Reikia suderinimo su centro administracija, elektros "
             "lizdo ir maždaug 2×2 m zonos."),
            ("Ar galite atvykti anksti ryte prieš atidarymą?",
             "Taip. Paruošimo laiką derinamės pagal jūsų grafiką — dažnai atvykstame likus 1–2 val. iki "
             "durų atidarymo."),
            ("Ar robotas gali dalyvauti juostelės perkirpime?",
             "Taip, tai populiarus akcentas. Scenarijų paruošiame iš anksto, kad momentas atrodytų sklandžiai "
             "ir tiktų fotografams."),
            ("Ar galima nuomotis robotą kelioms atidarymo dienoms iš eilės?",
             "Taip — kelių dienų paketai dažnai naudojami tinklų atidarymams keliuose miestuose. Logistiką "
             "planuojame kaip vieną projektą."),
            ("Ar padedate su komunikacija žiniasklaidai?",
             "Galime pateikti techninę informaciją apie robotą, nuotraukas ir vaizdo medžiagą, kurią "
             "galėsite naudoti pranešime spaudai."),
        ],
        related=[("robotas-renginiui.html", "Robotas renginiui"),
                 ("robotas-parodoms.html", "Parodos"),
                 ("humanoidinio-roboto-nuoma.html", "Nuomos sąlygos"),
                 ("kainos.html", "Kainos"),
                 ("blog-robotas-ar-kitos-pramogos.html", "Pramogų palyginimas")],
    ),
    dict(
        slug="robotas-vestuvems.html",
        title="Robotas vestuvėms — netikėta pramoga svečiams | 33bots",
        desc="Humanoidinis robotas vestuvėse: pasitinka svečius, šoka ir sukuria kadrus, kurių niekas "
             "nesitikėjo. Nuoma visoje Lietuvoje su operatoriumi.",
        keywords="robotas vestuvėms, vestuvių pramoga, robotas vestuvėse, netikėta pramoga svečiams",
        crumb="Robotas vestuvėms",
        eyebrow="Vestuvės · Pramoga, kurios niekas nesitiki",
        h1="Robotas vestuvėms —<br />pramoga, kurios<br /><em>niekas nesitiki.</em>",
        lead="Svečiai matė gyvą muziką, fotobūdelį ir šaltąjį fejerverką. Humanoidinio roboto — ne. Todėl "
             "būtent apie jį kalbės ir po metų.",
        tag="Vestuvės",
        benefits_title="Robotas vestuvių<br />programoje",
        benefits=[
            ("Svečių pasitikimas", "Robotas sveikina atvykstančius prie įėjimo — vakaras prasideda nuo "
                                   "šypsenų ir telefonų."),
            ("Pirmasis šokis+", "Po oficialios dalies robotas gali prisijungti prie aikštelės ir "
                                "pradėti vakarą su energija."),
            ("Nuotraukų zona", "Kadrai su robotu tampa alternatyva fotobūdelei — ir jų nereikia "
                               "spausdinti, kad pasklistų."),
            ("Vaikams ir seneliams", "Vienintelė pramoga, kuri vienodai veikia penkiamečiui ir "
                                     "aštuoniasdešimtmečiui."),
            ("Momentas įrašuose", "Vestuvių videografas gauna medžiagos, kokios dar nefilmavo — jūsų "
                                  "filmas tampa unikalus."),
            ("Diskretiškas valdymas", "Operatorius dirba fone ir nesikiša į vakaro eigą — pasirodymai "
                                      "derinami su vedėju."),
        ],
        body_h2_1="Kada vestuvėse pasirodo robotas",
        body_1="<p>Praktiškai geriausiai veikia du momentai: <strong>svečių pasitikimas</strong> prieš "
               "ceremoniją arba prieš vakarienę, ir <strong>vakaro pradžia šokių aikštelėje</strong>, kai "
               "reikia įžiebti energiją. Kai kurios poros renkasi robotą kaip staigmeną antrai pusei — "
               "tada scenarijų derinam tik su vienu iš jūsų.</p>"
               "<p>Standartinis vestuvių paketas trunka 2–3 valandas ir apima pasitikimą, vieną pasirodymą "
               "ir laisvą bendravimą su svečiais. Visą laiką robotą prižiūri operatorius, kuris derina "
               "veiksmus su vestuvių vedėju.</p>",
        body_h2_2="Ką reikia žinoti planuojant",
        body_2="<p>Reikia elektros lizdo, maždaug 2×2 m erdvės ir lygaus paviršiaus pasirodymui — "
               "restorano salė, terasa ar sodybos kiemas tinka puikiai. Jei vakaras vyksta lauke, verta "
               "numatyti atsarginį planą lietaus atveju.</p>"
               "<p>Rezervuoti verta iš anksto: vestuvių sezonas Lietuvoje trumpas, o šeštadieniai "
               "užsipildo greitai. Kainos ir paketų logiką rasite <a href=\"kainos.html\">kainų "
               "puslapyje</a>, o kitus formatus — <a href=\"robotas-renginiui.html\">renginių puslapyje</a>.</p>",
        faq=[
            ("Ar robotas netrukdys ceremonijai?",
             "Ne. Robotas dalyvauja tik suderintuose momentuose, o operatorius laikosi vestuvių vedėjo "
             "grafiko. Per ceremoniją robotas paprastai lieka paruošimo zonoje."),
            ("Ar robotas gali įteikti žiedus?",
             "Techniškai tai įmanoma ir kartais taip darome, bet rekomenduojame tai aptarti iš anksto — "
             "svarbiausiam momentui visada siūlome atsarginį planą."),
            ("Ar robotas tinka vestuvėms sodyboje?",
             "Taip, jei yra elektra ir lygus paviršius pasirodymui. Transportas įskaičiuotas nepriklausomai "
             "nuo atstumo nuo miesto."),
            ("Ar galime pasirinkti muziką pasirodymui?",
             "Taip. Choreografiją derinam prie jūsų pasirinkto kūrinio, jei jis tinka pagal tempą — "
             "tai aptariame prieš renginį."),
            ("Kiek laiko iš anksto rezervuoti robotą vestuvėms?",
             "Vasaros šeštadieniams rekomenduojame kreiptis 2–3 mėnesius iš anksto. Ne sezono metu "
             "dažnai pavyksta suderinti ir greičiau."),
        ],
        related=[("robotas-imones-sventei.html", "Įmonės šventė"),
                 ("robotas-renginiui.html", "Robotas renginiui"),
                 ("kainos.html", "Kainos"),
                 ("video-realizacijos.html", "Vaizdo įrašai"),
                 ("humanoidinio-roboto-nuoma.html", "Nuomos sąlygos")],
    ),
]


def benefits_grid(items):
    cards = "\n".join(f"""      <div class="use-item">
        <span class="use-num">{i + 1:02d}</span>
        <h3>{t}</h3>
        <p>{d}</p>
      </div>""" for i, (t, d) in enumerate(items))
    return cards


def build_page(p):
    url = f"{SITE}/{p['slug']}"
    crumb_items = [("Pradžia", f"{SITE}/"), (p["crumb"], url)]
    ld = [
        organization_ld(),
        service_ld(p["crumb"], p["desc"], url),
        breadcrumb_ld(crumb_items),
        faq_ld(p["faq"]),
    ]
    html = head(title=p["title"], description=p["desc"], slug=p["slug"], keywords=p["keywords"],
                og_image=f"{SITE}/og/{p['slug'].replace('.html', '.jpg')}",
                extra_ld=ld, preload_hero=True)
    html += body_open()
    html += nav()
    html += crumbs([("Pradžia", "index.html"), (p["crumb"], None)])

    html += f"""
  <section class="hero hero--sub">
    <div class="hero__content">
      <p class="hero__eyebrow">{p['eyebrow']}</p>
      <h1 class="hero__title">{p['h1']}</h1>
      <p class="hero__sub">{p['lead']}</p>
      <div class="hero__ctas">
        <a href="#kontaktai" class="btn-primary">Gauti pasiūlymą</a>
        <a href="#nauda" class="btn-ghost">Kodėl verta ↓</a>
      </div>
      <div class="hero__trust">
        <span class="hero__trust-item">✓ Nemokamas transportas</span>
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
               alt="Humanoidinis robotas Unitree G1 — {p['crumb'].lower()} Lietuvoje"
               class="hero__robot-img"
               width="600" height="800"
               loading="eager"
               fetchpriority="high" />
        </picture>
      </div>
      </div>
    </div>
  </section>

  <!-- NAUDA -->
  <section class="section" id="nauda">
    <div class="section-header">
      <span class="tag">{p['tag']}</span>
      <h2 class="section-title">{p['benefits_title']}</h2>
    </div>
    <div class="use-grid">
{benefits_grid(p['benefits'])}
    </div>
  </section>

  <!-- TEKSTAS -->
  <section class="section">
    <div style="max-width:1000px; margin:0 auto; display:grid; grid-template-columns:repeat(auto-fit,minmax(320px,1fr)); gap:var(--s7);">
      <div>
        <h2 class="section-title" style="font-size:clamp(1.6rem,3vw,2.4rem); margin-bottom:var(--s4);">{p['body_h2_1']}</h2>
        <div class="article-body" style="max-width:none;">{p['body_1']}</div>
      </div>
      <div>
        <h2 class="section-title" style="font-size:clamp(1.6rem,3vw,2.4rem); margin-bottom:var(--s4);">{p['body_h2_2']}</h2>
        <div class="article-body" style="max-width:none;">{p['body_2']}</div>
      </div>
    </div>
  </section>

  <!-- PROCESAS -->
  <section class="section process-section">
    <div class="section-header">
      <span class="tag">Kaip tai veikia</span>
      <h2 class="section-title">Nuo užklausos<br />iki pasirodymo</h2>
    </div>
    <div class="process">
      <div class="process-step">
        <span class="process-step__n">01</span>
        <div><h3>Užklausa</h3><p>Parašykite datą, miestą ir renginio tipą. Atsakome per 24 val.</p></div>
      </div>
      <div class="process-step">
        <span class="process-step__n">02</span>
        <div><h3>Scenarijus ir kaina</h3><p>Pasiūlome konkretų scenarijų ir kainą be paslėptų mokesčių.</p></div>
      </div>
      <div class="process-step">
        <span class="process-step__n">03</span>
        <div><h3>Sutartis</h3><p>Aiškios sąlygos, datos rezervacija avansu.</p></div>
      </div>
      <div class="process-step">
        <span class="process-step__n">04</span>
        <div><h3>Renginio diena</h3><p>Atvykstame anksčiau, paruošiame ir išbandome. Jūs nieko nedarote.</p></div>
      </div>
      <div class="process-step">
        <span class="process-step__n">05</span>
        <div><h3>Pasirodymas</h3><p>Robotas dirba, svečiai filmuoja, jūs renkate kontaktus.</p></div>
      </div>
    </div>
  </section>

"""
    html += video_section()
    html += faq_section(p["faq"])

    related = "\n".join(f'      <a href="{u}">{t} →</a>' for u, t in p["related"])
    html += f"""  <!-- SUSIJĘ -->
  <section class="section" style="padding-top:0;">
    <div style="max-width:900px; margin:0 auto;">
      <p style="font-size:0.75rem; color:var(--text-3); text-transform:uppercase; letter-spacing:0.1em; font-weight:700; margin-bottom:var(--s3);">Taip pat verta pažiūrėti</p>
      <div class="related-links">
{related}
      </div>
      <p style="font-size:0.75rem; color:var(--text-3); text-transform:uppercase; letter-spacing:0.1em; font-weight:700; margin:var(--s6) 0 var(--s3);">Robotų nuoma miestuose</p>
      <div class="related-links">
{CITY_CHIPS}
      </div>
    </div>
  </section>

"""
    html += contact_section(heading="Gaukite pasiūlymą<br />savo renginiui.")
    html += footer()
    write(p["slug"], html)


def build():
    for p in PAGES:
        build_page(p)


if __name__ == "__main__":
    build()
