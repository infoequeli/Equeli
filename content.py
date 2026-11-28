"""Equeli – vsebina strani. Tu urejaš besedila; nato zaženi: python3 build.py"""

SITE = "https://equeli.si"
EMAIL = "info.equeli@gmail.com"
UPDATED = "23. 11. 2026"

# Obrazci so na strani sami (glej forms.py). Povezave do njih:
FORMS = {
    "izvajalci": "/za-izvajalce/#obrazec",
    "ustanove": "/za-sole-in-zavode/#povprasevanje",
    "kontakt": "/kontakt/#obrazec",
    "starsi": "/za-starse/#iskanje",
    "podporniki": "/za-podpornike/#podpora",
}

# Raziskovalna baza (štetje po regijah, stanje 12. 11. 2026). Imen izvajalcev ne objavljamo, dokler jih ne potrdijo.
REGIONS = [("Osrednjeslovenska", 11), ("Podravska", 7), ("Jugovzhodna Slovenija", 6), ("Savinjska", 6),
           ("Goriška", 3), ("Koroška", 3), ("Obalno-kraška", 3), ("Primorsko-notranjska", 3), ("Zasavska", 3),
           ("Gorenjska", 2), ("Posavska", 2), ("Pomurska", 0)]

APPROACHES = {
    "H": ("Hipoterapija", "Rehabilitacijska obravnava, pri kateri se gibanje konja v koraku prenaša na udeleženca. Konja vodi vodnik, terapevt usmerja položaj telesa.", "Fizioterapevt ali delovni terapevt z dodatnim usposabljanjem."),
    "T": ("Terapija s pomočjo konja", "Strokovnjak vključi konja v svoje strokovno delo. Cilji izhajajo iz njegove temeljne stroke.", "Npr. psiholog, socialni delavec, specialni pedagog ali delovni terapevt z dodatnim usposabljanjem."),
    "P": ("Pedagoške in specialnopedagoške intervencije", "Strukturirano delo ob konju za učenje, pozornost, samoregulacijo in socialne veščine.", "Specialni ali socialni pedagog, učitelj ali vzgojitelj z dodatnim usposabljanjem."),
    "S": ("Psihosocialne intervencije", "Izkušnja v odnosu s konjem je izhodišče za delo s čustvi, mejami, zaupanjem in odnosi.", "Psiholog, psihoterapevt, socialni delavec ali svetovalec z dodatnim usposabljanjem."),
    "D": ("Delovnoterapevtsko usmerjene intervencije", "Poudarek na vsakodnevnih aktivnostih, motoriki, senzornih izzivih in samostojnosti.", "Diplomirani delovni terapevt z dodatnim usposabljanjem."),
    "J": ("Prilagojeno jahanje", "Učenje jahanja s prilagojeno opremo in pomočjo. Namen je gibanje, veselje in vključenost, ni zdravstvena obravnava.", "Inštruktor jahanja, pogosto z dodatnim znanjem."),
    "A": ("Aktivnosti s konji", "Strokovno vodene aktivnosti, kot so nega, vodenje in opazovanje črede. Podporni ali izobraževalni namen, ni terapija.", "Strokovni sodelavci z usposabljanjem za aktivnosti s konji."),
}

GUIDES = [
    {"slug": "avtizem", "title": "Avtizem",
     "card": "Strukturirano okolje, komunikacija, regulacija in socialne veščine.",
     "lede": "Za starše in skrbnike otrok in mladostnikov z avtizmom. Kateri programi s konji obstajajo, kdo jih izvaja in kaj vprašati, preden se odločite.",
     "summary": ["Delo ob konju poteka v predvidljivem, strukturiranem okolju, ki ga strokovnjak prilagodi otroku.",
                 "Cilji so lahko komunikacija, uravnavanje čustev in vedenja, socialne veščine ali gibanje. Pristop izberete glede na cilj.",
                 "Program ne nadomešča obravnave pri zdravniku, psihologu ali v šoli."],
     "approaches": "TPDA",
     "questions": ["Kakšne izkušnje imate z otroki z avtizmom in kakšno izobrazbo imate?",
                   "Kako prilagodite okolje (hrup, število ljudi, potek srečanja)?",
                   "Kako otroka pripravite na novo okolje? Je mogoč predhodni ogled?",
                   "Kako boste postavili cilje in ali sodelujete s šolo ali drugimi strokovnjaki?",
                   "Kaj se zgodi, če otrok med srečanjem potrebuje premor?"],
     "slovenia": "V raziskovalni bazi Equeli vsaj 6 izvajalcev v javnih opisih izrecno navaja delo z otroki z avtizmom, med njimi samostojni strokovnjaki in konjeniški centri v več regijah. Podatke še preverjamo."},
    {"slug": "gibalne-tezave", "title": "Cerebralna paraliza in gibalne težave",
     "card": "Hipoterapija, delovna terapija s konjem in prilagojeno jahanje.",
     "lede": "Za otroke in odrasle z gibalnimi izzivi ter njihove bližnje. Kaj je hipoterapija, kako se razlikuje od prilagojenega jahanja in kje se izvaja.",
     "summary": ["Za gibalne cilje se najpogosteje ponuja hipoterapija, ki jo izvaja fizioterapevt ali delovni terapevt z dodatnim usposabljanjem.",
                 "Pred vključitvijo je potrebna ocena primernosti. Pri nekaterih stanjih hipoterapija ni primerna.",
                 "Prilagojeno jahanje je rekreacija in ni zdravstvena obravnava."],
     "approaches": "HDJ",
     "questions": ["Kdo vodi obravnavo in kakšno izobrazbo ter usposabljanje ima?",
                   "Ali pred vključitvijo potrebujete mnenje zdravnika ali fizioterapevta?",
                   "Kako je urejeno nameščanje na konja (rampa, podest, pomoč)?",
                   "Ali je prostor dostopen z vozičkom? Ali so na voljo dostopne sanitarije?",
                   "Kako spremljate napredek in kako pogosto se srečujemo?"],
     "slovenia": "Hipoterapijo izvajajo nekateri javni zavodi za usposabljanje in rehabilitacijo ter zasebni izvajalci. V raziskovalni bazi Equeli je 20 organizacij, ki navajajo hipoterapijo, delovno terapijo s konjem ali delo z gibalnimi izzivi."},
    {"slug": "adhd", "title": "ADHD in težave s pozornostjo",
     "card": "Pozornost, samoregulacija in samozavest, povezano s šolo.",
     "lede": "Za starše otrok, ki težko ohranjajo pozornost, so zelo nemirni ali impulzivni. Kateri programi s konji obstajajo in kako izbrati.",
     "summary": ["Najpogosteje se ponuja pedagoško ali specialnopedagoško usmerjeno delo ob konju.",
                 "Cilji so lahko pozornost, samoregulacija, sledenje navodilom in samozavest.",
                 "Dobro je, da so cilji povezani s šolo in vsakdanjim življenjem."],
     "approaches": "PTS",
     "questions": ["Kakšne izkušnje imate z otroki z ADHD?", "Kako je srečanje strukturirano in koliko traja?",
                   "Ali je program individualen ali v skupini?", "Ali sodelujete z učitelji ali šolsko svetovalno službo?",
                   "Kako boste skupaj z nami spremljali napredek?"],
     "slovenia": "V raziskovalni bazi Equeli vsaj 4 izvajalci v javnih opisih izrecno navajajo ADHD ali težave s pozornostjo, več pa jih navaja učne in vedenjske težave. Podatke še preverjamo."},
    {"slug": "motnje-v-dusevnem-razvoju", "title": "Downov sindrom in motnje v duševnem razvoju",
     "card": "Gibanje, komunikacija, samostojnost in druženje, za otroke in odrasle.",
     "lede": "Za otroke in odrasle ter njihove bližnje. Programi s konji lahko podpirajo gibanje, komunikacijo, samostojnost in druženje.",
     "summary": ["Programi so namenjeni otrokom in odraslim; nekateri izvajalci organizirajo tudi skupine in tabore.",
                 "Tempo in komunikacija se prilagodita udeležencu.",
                 "Pred jahanjem nekateri izvajalci zahtevajo zdravniško mnenje. Vprašajte vnaprej."],
     "approaches": "TDHJ",
     "questions": ["Ali imate izkušnje s to skupino, tudi z odraslimi?", "Ali pred vključitvijo potrebujete zdravniško mnenje?",
                   "Kako prilagodite komunikacijo in potek srečanja?", "Ali so mogoči skupinski programi ali tabori?"],
     "slovenia": "Programe s konji izvajajo nekateri centri za usposabljanje, delo in varstvo (CUDV) ter zasebni izvajalci. V raziskovalni bazi Equeli več izvajalcev izrecno navaja Downov sindrom ali motnje v duševnem razvoju. Podatke še preverjamo."},
    {"slug": "ucne-custvene-vedenjske-tezave", "title": "Učne, čustvene in vedenjske težave",
     "card": "Težave v šoli, z obvladovanjem čustev, vedenjem ali samozavestjo.",
     "lede": "Za starše otrok in mladostnikov, ki imajo težave v šoli, z obvladovanjem čustev, vedenjem ali samozavestjo.",
     "summary": ["Konj se odziva na vedenje neposredno, kar strokovnjak uporabi za učenje samoregulacije in sodelovanja.",
                 "Pri učnih težavah je pogostejše pedagoško delo, pri čustvenih in vedenjskih pa psihosocialno.",
                 "Pomembna je izobrazba izvajalca in sodelovanje s šolo ali drugimi strokovnjaki."],
     "approaches": "PST",
     "questions": ["Kakšna je vaša temeljna stroka (pedagog, psiholog, socialni delavec)?", "Kako boste postavili cilje in kako bomo starši vključeni?",
                   "Ali ponujate tudi programe za šole ali skupine?", "Kdaj boste predlagali drugo obliko pomoči?"],
     "slovenia": "V raziskovalni bazi Equeli vsaj 8 izvajalcev izrecno navaja učne ali vedenjske težave, več kot 10 pa čustvene izzive. Nekateri ponujajo tudi programe za šole. Podatke še preverjamo."},
    {"slug": "tesnoba-samopodoba-odnosi", "title": "Tesnoba, samopodoba in odnosi",
     "card": "Za mladostnike in odrasle: čustva, meje, zaupanje in samozavest.",
     "lede": "Za mladostnike in odrasle, ki iščejo podporo pri čustvih, samozavesti, mejah ali odnosih.",
     "summary": ["Izkušnja v odnosu s konjem je izhodišče za pogovor o čustvih, mejah in zaupanju.",
                 "Delo poteka večinoma ob konju na tleh, jahanje ni nujno.",
                 "Pomembno je, da ima izvajalec ustrezno temeljno izobrazbo (npr. psiholog, psihoterapevt, socialni delavec)."],
     "approaches": "STA",
     "questions": ["Kakšno izobrazbo imate in ali ste vpisani v register svoje stroke?", "Kako poteka delo, če se med srečanjem odprejo težke vsebine?",
                   "Kako je poskrbljeno za zaupnost?", "Kdaj boste predlagali drugo obliko pomoči?"],
     "slovenia": "V raziskovalni bazi Equeli več kot 10 izvajalcev navaja čustvene izzive, samopodobo ali psihosocialno delo. Podatke še preverjamo.",
     "alert": "<strong>Če ste v hudi stiski</strong>, ne čakajte na program. Obrnite se na osebnega zdravnika, pokličite Klic v duševni stiski (01 520 99 00) ali Samarijan (116 123). V nujnih primerih pokličite 112."},
    {"slug": "aktivnost-ob-konjih", "title": "Aktivnost ob konjih",
     "card": "Prilagojeno jahanje, druženje in čas v naravi, brez terapevtskih ciljev.",
     "lede": "Za vse, ki želijo varno in prijetno izkušnjo s konji: prilagojeno jahanje, druženje, gibanje in čas v naravi.",
     "summary": ["Prilagojeno jahanje je učenje jahanja s prilagojeno opremo in pomočjo.",
                 "Aktivnosti s konji potekajo pogosto na tleh: nega, vodenje, opazovanje črede.",
                 "Gre za rekreacijo in druženje, ne za zdravstveno obravnavo."],
     "approaches": "JA",
     "questions": ["Kdo vodi aktivnost in kakšno usposobljenost ima za delo z osebami s posebnimi potrebami?",
                   "Kakšna varnostna oprema je na voljo (čelada, prilagojeno sedlo)?",
                   "Koliko ljudi pomaga pri jahanju (vodnik, spremljevalci ob strani)?",
                   "Ali so na voljo skupinski termini, tabori ali družinske aktivnosti?"],
     "slovenia": "V raziskovalni bazi Equeli je 20 organizacij, ki navajajo prilagojeno ali terapevtsko jahanje oziroma aktivnosti s konji: konjeniški klubi, društva, kmetije in centri. Podatke še preverjamo."},
]



# Rubrike člankov
RUBRICS = [
    ("obiski", "Obiski na terenu", "camera", "Zapisi in fotografije z obiskov izvajalcev po Sloveniji."),
    ("strokovnjaki", "Pogovori s strokovnjaki", "mic", "Kako delajo, kaj jih vodi in kaj svetujejo."),
    ("starsi", "Vprašanja staršev", "message", "Odgovori na pogosta vprašanja družin."),
    ("raziskava", "Iz raziskave", "chart", "Ugotovitve nacionalnega pregleda področja."),
    ("analize", "Strokovne analize", "book", "Analize in raziskovalni prispevki o intervencijah s pomočjo konj."),
]

# Članki. Dodaj nov slovar in zaženi build.py. Objavi samo potrjene vsebine (soglasja za fotografije in izjave!).
# Primer:
# {"slug": "obisk-pri-...", "title": "...", "rubric": "obiski", "date": "2027-01-15", "lede": "Kratek povzetek.",
#  "body": "<p>Besedilo članka v HTML.</p>"}
ARTICLES = [
    dict(slug="meja-kot-dinamika-blizine-in-razdalje", rubric="analize", date="2026-11-27",
         title="Meja kot dinamika bližine in razdalje",
         lede="Kvalitativna analiza individualne terapije s pomočjo konja: kako se osebne meje pokažejo v telesu in prostoru ob konju, ki se giblje prosto.",
         body="""
<p class="art-meta">Avtorica: Ela Rebolj · Kvalitativna analiza · <a href="/assets/doc/meja-kot-dinamika-blizine-in-razdalje.pdf" target="_blank" rel="noopener">Celotna analiza (PDF, 10 strani)</a></p>
<div class="art-stats">
  <div><b>18/20</b><span>udeležencem je konj vsaj enkrat sam pristopil</span></div>
  <div><b>17/20</b><span>udeležencev je doživelo, da se konj odmakne zaradi svojih potreb</span></div>
  <div><b>17/20</b><span>udeležencev je izkušnjo povezalo s svojimi odnosi</span></div>
</div>
<h2>Izhodišče</h2>
<p>Meje navadno razumemo kot nekaj, kar izrečemo z besedami. Kaj pa, če se meja najprej pokaže v telesu in v prostoru? Ko se nam približa nekdo z jeznim izrazom, si izberemo večjo razdaljo. Tudi konj kot čredna žival razdaljo uravnava glede na to, kako varno se počuti. Razdalja med človekom in konjem je zato viden pokazatelj odnosa.</p>
<p>Analiza je odgovarjala na dve vprašanji: kako se v odnosu s prosto gibajočim se konjem kaže dinamika bližine in razdalje ter kako jo udeleženci doživljajo in prenašajo v svoje odnose.</p>
<h2>Kako je potekala</h2>
<ul>
  <li><strong>Udeleženci:</strong> 20 odraslih (11 žensk, 9 moških) v individualni terapiji s pomočjo konja.</li>
  <li><strong>Program:</strong> »Moje meje«, zasnovan v okviru izobraževanja za terapijo s pomočjo konja pri Zavodu Nazaj na konja: 12 srečanj po 60 minut, enkrat tedensko, z delom na tleh ob kobili Nutelli.</li>
  <li><strong>Vaje:</strong> opazovanje konja za ograjo, razdalja v istem prostoru, bližina in umik, vodenje konja ter hoja med točkami v prostoru.</li>
  <li><strong>Podatki in analiza:</strong> terapevtski zapiski in pisne refleksije udeležencev, tematska analiza. Podatki so anonimizirani.</li>
</ul>
<h2>Kaj se je pokazalo</h2>
<p><strong>Vsakdanji vzorci postanejo vidni.</strong> Prilagajanje drugim, potreba po potrditvi, napetost in zadrževanje čustev so se ob konju pokazali v prostoru: kot razdalja, čas v stiku in odziv na konjev prihod ali odhod. Tam jih je bilo mogoče opazovati brez obsojanja.</p>
<p><strong>Ograda kot prostor za raziskovanje.</strong> Konjevo približevanje in umikanje je pri sedmih udeležencih prebudilo teme iz življenja doma, v partnerstvu in na delu. Sprememba položaja, korak nazaj ali v stran, je odprla nov pogled nase in na drugega.</p>
<p><strong>Od drugih k sebi.</strong> Udeleženci, ki so konjev odhod sprva razumeli osebno, so postopno ločili, kaj pripada konju in kaj njim. Ker konj ohranja svojo voljo, se je pozornost premaknila k lastnemu dihu, nameri in umiku.</p>
<blockquote><p>Na začetku: »V začetku ure sem samo z opazovanjem konja takoj šla v občutek, da me NE MARA.«<br>Proti koncu: »Sprejemam, da ima svoj prostor in sem s tem ok.«</p></blockquote>
<blockquote><p>Na začetku: »… prepozno prepoznam, da svoj prostor potrebujem …«<br>Proti koncu: »… kako fino je tudi stopiti korak nazaj ali se obrniti stran …«</p></blockquote>
<h2>Sklep</h2>
<p>Meja ni le nekaj, kar izrečemo. Je dinamika bližine in razdalje med dvema bitjema z lastno voljo. Konj, ki prihaja in odhaja v svojem ritmu, pokaže, da v odnosu najbolj vplivamo na svoj odziv.</p>
<div class="callout"><strong>Omejitve.</strong> Zapiske je vodila izvajalka sama, refleksije so samoporočila, število srečanj se je med udeleženci razlikovalo, analiza je opisna in vključuje eno skupino. Kodiranje je preliminarno, naslednji korak je preverba z drugim koderjem.</div>
<p><a class="btn btn-dark" href="/assets/doc/meja-kot-dinamika-blizine-in-razdalje.pdf" target="_blank" rel="noopener">Preberite celotno analizo (PDF)</a></p>
<h2>Viri</h2>
<ul class="refs">
  <li>Callara, A. L. idr. (2024). Unveiling directional physiological coupling in human–horse interactions. <em>iScience</em>, 27, 110857.</li>
  <li>Cartaud, A. idr. (2018). Physiological response to facial expressions in peripersonal space determines interpersonal distance in a social interaction context. <em>Frontiers in Psychology</em>, 9, 657.</li>
  <li>Mellody, P. <em>Facing Codependence</em>.</li>
  <li>Starling, M., McLean, A. in McGreevy, P. (2016). The contribution of equitation science to minimising horse-related risks to humans. <em>Animals</em>, 6(3), 15.</li>
  <li>Van Dierendonck, M. (2005). Social contact in horses. V: <em>The Human-Animal Relationship</em>.</li>
  <li>von Mohr, M. idr. (2023). My social comfort zone: Attachment anxiety shapes peripersonal and interpersonal space. <em>iScience</em>, 26(2), 105955.</li>
</ul>
"""),
]

# Centri – samo javno dostopni podatki (register Nazaj na konja, spletne strani centrov, Konjeniška zveza Slovenije).
# confirmed=True: center je potrdil sodelovanje z Equeli -> javno prikazan. Ostali so v bazi, a skriti.
# Brez telefonov in e-pošte. group: javni | register | potrjeni | drugi | organizator
# potrjeni = center je podatke sam posredoval prek obrazca Equeli. space: neobvezno, prostori. programs: neobvezno, imena programov.
# offer: kode pristopov iz APPROACHES (H, T, P, S, D, J, A). who: komu je program namenjen.
REG = "https://nakonju.si/terapevti/"
KZS = "https://www.konj-zveza.org/jahalne-sole-klubi/"
CENTERS = [
    # --- javni zavodi ---
    dict(name="CIRIUS Kamnik", place="Kamnik", region=["Osrednjeslovenska"], group="javni", offer=["H", "D", "J"],
         who="Otroci in mladostniki z gibalno oviranostjo", team="Fizioterapevti in delovni terapevti zavoda", horses="",
         url="https://cirius-kamnik.si/", reg=""),
    dict(name="CUDV Dobrna", place="Dobrna", region=["Savinjska"], group="javni", offer=["H"],
         who="Otroci, mladostniki in odrasli z gibalnimi in razvojnimi ovirami", team="Doc. dr. Tine Kovačič, magister fizioterapije", horses="2",
         url="https://centerdobrna.si/", reg=REG + "tine-kovacic/", confirmed=True),
    dict(name="CUDV Draga", place="Ig", region=["Osrednjeslovenska"], group="javni", offer=["H", "D", "P", "J"],
         who="Otroci, mladostniki in odrasli z motnjami v duševnem razvoju", team="Strokovni tim centra", horses="",
         url="https://www.center-db.si/", reg="", confirmed=True),
    dict(name="CIRIUS Vipava", place="Vipava", region=["Goriška"], group="javni", offer=["H"],
         who="Učenci zavoda – otroci in mladostniki s posebnimi potrebami; sodeluje tudi z društvi za otroke s posebnimi potrebami",
         team="Dve hipoterapevtki s pomočniki", horses="1",
         programs="Hipoterapija dvakrat na teden v okviru športnega dne. Tudi otroci, ki ne jahajo, sodelujejo pri delu s konjem: čiščenje in vodenje. Izvajanje je odvisno od vremena.",
         url="https://www.cirius-vipava.si/", reg="", confirmed=True),
    dict(name="CUDV Radovljica", place="Radovljica", region=["Gorenjska"], group="javni", offer=["H"],
         who="Uporabniki centra; hipoterapija je del rednih programov zavoda in je omogočena vsem uporabnikom, pri katerih ni kontraindikacij",
         team="Diplomirani fizioterapevt s specializacijo za hipoterapijo; v timu še športni pedagog, delovni terapevt, habilitator in varuh",
         horses="", programs="Hipoterapija na kmetiji hipoterapevta",
         url="", reg="", confirmed=True),
    dict(name="Bolnišnica za otroke in mladostnike Rakitna", place="Rakitna", region=["Osrednjeslovenska"], group="javni", offer=["S", "A"],
         who="Otroci in mladostniki v bolnišnični obravnavi", team="Terapevtski tim bolnišnice", horses="",
         url="https://mkz-rakitna.si/", reg=""),
    dict(name="ZUDV dr. Marijana Borštnarja Dornava", place="Dornava", region=["Podravska"], group="javni", offer=["P"],
         who="Otroci in mladostniki z motnjami v duševnem razvoju", team="Strokovni tim zavoda", horses="",
         url="https://www.zavod-dornava.si/", reg=""),
    # --- strokovnjaki v registru Nazaj na konja ---
    dict(name="Zavod Nazaj na konja", place="Starošince, Cirkovce", region=["Podravska"], group="register", offer=["T", "S"],
         who="Otroci in mladostniki s posebnimi potrebami, učnimi, vedenjskimi in duševnimi izzivi", team="Metka Demšar Goljevšček, Kaja Koleša, Maša Bastič", horses="5",
         url="https://nakonju.si/", reg=REG + "metka-demsar-goljevscek/", confirmed=True),
    dict(name="Terapevtsko-konjeniški zavod Olsen", place="Pivka", region=["Primorsko-notranjska"], group="register", offer=["D", "T"],
         who="Otroci z gibalnimi, vedenjskimi, socialnimi in kognitivnimi izzivi", team="Maja Kristan Kirn, dipl. delovna terapevtka", horses="3",
         url="https://www.zavod-olsen.si/", reg=REG + "maja-kristan-kirn/", confirmed=True),
    dict(name="Konjeniško-terapevtski zavod Arion", place="Ljubljana in Mislinja", region=["Osrednjeslovenska", "Koroška"], group="register", offer=["P"],
         who="Otroci in mladostniki", team="Tajda Knez, mag. inkluzivne in socialne pedagogike", horses="5",
         url="", reg=REG + "tajda-knez/", confirmed=True),
    dict(name="Moonrise – terapije s pomočjo konj", place="Domžale", region=["Osrednjeslovenska"], group="register", offer=["T", "D", "A"],
         who="Otroci, mladostniki, odrasli in starejši, šolske in vrtčevske skupine ter uporabniki zavodov; individualno, v manjših skupinah ali za razrede",
         programs="Terapije s pomočjo konj (30 ali 45 minut, individualno); Poni jezdeci za otroke do 8 let (priprava in nega konja, vodene aktivnosti v maneži, vodeno jahanje); sprostitveno jahanje za tiste, ki želijo stik s konjem brez učenja jahanja; aktivnosti s konji za skupine s poudarkom na komunikaciji, zaupanju, odnosih in sodelovanju. Cena individualnega dela od 20 do 70 €.",
         team="Tanja Slovenec, dipl. delovna terapevtka in terapevtka s pomočjo konj", horses="3",
         space="Zunanja jahalnica ali ograda, sanitarije, parkirišče",
         url="https://moonrise.si/", reg=REG + "tanja-slovenec-terapevtka-s-pomocjo-konja/", confirmed=True),
    dict(name="Zavedno delo s konji, Rock Ranč", place="Šentvid pri Stični", region=["Osrednjeslovenska"], group="register", offer=["T", "P", "S", "J", "A"],
         who="Otroci, mladostniki, odrasli in starejši, šolske in vrtčevske skupine ter uporabniki zavodov; individualno, v manjših skupinah ali za razrede",
         programs="Različni programi, prilagojeni posamezniku: za vsakega iščemo najbolj primerne dejavnosti in načine, kako ga konji lahko podprejo. Cena je odvisna od programa.",
         team="Živa Logar, specialna in rehabilitacijska pedagoginja, terapevtka za intervencije s pomočjo konj, inštruktorica in jahalna pedagoginja (NPK iz konjeništva), mentorica bodočim terapevtom; veterinarka z znanji osteopatije za konje, jahalna pedagoginja in učiteljica metode Movement Based Learning. Obe sta trenerki konj po konjem prijaznih pristopih.",
         horses="20", space="Zunanja jahalnica ali ograda, sanitarije, parkirišče",
         url="https://rockranch.si/", reg=REG + "ziva-logar-terapevtka-s-pomocjo-konja/", confirmed=True),
    dict(name="Marengo dežela", place="Koprivnica", region=["Posavska"], group="register", offer=["T", "A"],
         who="Downov sindrom, avtizem, cerebralna paraliza, motnje v duševnem razvoju", team="Natalija Oštir, univ. dipl. socialna delavka", horses="3",
         url="https://www.facebook.com/MarengoDezela/", reg=REG + "natalija-ostir/", confirmed=True),
    dict(name="Konjeniški zavod EPONA", place="Novo mesto", region=["Jugovzhodna Slovenija"], group="register", offer=["T", "H", "A"],
         who="Otroci, mladostniki in odrasli s posebnimi potrebami z najrazličnejšimi primanjkljaji", team="dr. Sabina Devjak Novak", horses="2",
         url="", reg=REG + "sabina-devjak-novak/", confirmed=True),
    dict(name="Terapija s pomočjo konja Češča vas", place="Novo mesto", region=["Jugovzhodna Slovenija"], group="register", offer=["T"],
         who="Otroci in odrasli s posebnimi potrebami", team="Polona Pušavec, univ. dipl. socialna delavka", horses="2",
         url="", reg=REG + "polona-pusavec/"),
    dict(name="Terapevtski zavod Pokrov dom", place="Trbovlje", region=["Zasavska"], group="register", offer=["T"],
         who="Samozavest, komunikacija in čustveni izzivi", team="Maruša Čamer, dipl. vzgojiteljica", horses="1",
         url="", reg=REG + "marusa-camer/"),
    dict(name="Športno-terapevtski klub Pegasus", place="Gabrovka", region=["Zasavska"], group="register", offer=["T", "P", "A"],
         who="Otroci, mladostniki in odrasli; individualno in v manjših skupinah",
         programs="Terapija s pomočjo konja s poudarkom na celostnem razvoju: socialne veščine, osebnostna rast, samoopazovanje, koncentracija, učno področje in motorika",
         team="Irena K. Kovač, prof. športne vzgoje, kineziologinja, terapevtka s pomočjo konja (specializacija 2013)",
         horses="2", space="Zunanja jahalnica ali ograda, sanitarije, parkirišče",
         url="https://pegasusclub.weebly.com/", reg=REG + "irena-k-kovac/", confirmed=True),
    dict(name="Hijaterapija, Konjeniški klub Rojnik", place="Grosuplje", region=["Osrednjeslovenska"], group="register", offer=["S"],
         who="Otroci in mladostniki", team="Julija Božič, mag. psihologije; Katra Zajc Švara, mag. socialnega dela", horses="2",
         url="", reg=REG + "julija-bozic/"),
    dict(name="Posestvo Jurečič – terapije s konji", place="Ljubljana", region=["Osrednjeslovenska"], group="register", offer=["S"],
         who="Čustvene in vedenjske težave", team="Nastja Krajšek, psihoterapevtske znanosti", horses="4",
         url="", reg=REG + "nastja-krajsek/"),
    dict(name="Štala Glinšek", place="Velenje", region=["Savinjska"], group="register", offer=["T"],
         who="Motnje v duševnem razvoju, avtizem, senzorne, komunikacijske in gibalne težave", team="Elizabeta Fijavž, specialna pedagoginja", horses="1",
         url="", reg=REG + "elizabeta-fijavz/"),
    dict(name="Terapija s pomočjo konja – Sara Krašovec", place="Škofja vas", region=["Savinjska"], group="register", offer=["T"],
         who="Motnje v duševnem razvoju, avtizem, čustveno-vedenjske in gibalne težave", team="Sara Krašovec", horses="1",
         url="", reg=REG + "sara-krasovec/"),
    dict(name="Zavod Škatlica", place="Sveti Tomaž", region=["Podravska"], group="register", offer=["S", "P"],
         who="Avtizem, ADHD in vedenjski izzivi", team="Dora Klar", horses="2",
         url="https://www.skatlica.si/", reg=""),
    dict(name="zGIBka", place="Povir pri Sežani", region=["Obalno-kraška"], group="register", offer=["T", "A"],
         who="Vedenjsko-čustvene in učne težave, tesnoba, samopodoba", team="Taja Tavčar, prof. razrednega pouka", horses="1",
         url="https://www.zgibka.com/", reg=REG + "taja-tavcar-terapevtka-s-pomocjo-konja/"),
    dict(name="Pedagoške intervencije – Andreja Zega", place="Ajdovščina", region=["Goriška"], group="register", offer=["P"],
         who="ADHD, avtizem, učne in vedenjske težave; tudi skupine", team="Andreja Zega, prof. razrednega pouka", horses="1",
         url="", reg=REG + "andreja-zega/"),
    dict(name="Konjeniški center AMAY", place="Ložnica pri Žalcu", region=["Savinjska"], group="register", offer=["T", "P", "S", "D", "J", "A"],
         who="Otroci, mladostniki, odrasli in starejši; individualno, v manjših skupinah, za šole, vrtce in zavode", team="Maya Mlinar, vodja programov; Tajda Knez, strokovna sodelavka", horses="",
         space="Pokrita jahalnica, dostop za invalidski voziček, sanitarije, parkirišče",
         url="https://amay-si.com/", reg="", confirmed=True),
    dict(name="Zavod Na drugačni poti", place="Sodražica", region=["Jugovzhodna Slovenija"], group="register", offer=["T", "S"],
         who="Otroci in mladostniki; individualno delo, prilagojeno razvojni stopnji in potrebam posameznika",
         programs="Psihoterapevtsko in psihosocialno delo z otroki in mladostniki v naravnem okolju ob živalih: nedirektivni pristopi, pogovor, igra in ustvarjanje. Cilj je krepiti čustveno pismenost, samopodobo in kakovost odnosov ter spodbujati osebnostno rast",
         team="Ajda Čampa, mag. psihosoc. svet., specializantka psihoterapije otrok in mladostnikov, edukantka psihodinamske psihoterapije, terapevtka s pomočjo konj",
         horses="", space="Zunanja jahalnica ali ograda, sanitarije, parkirišče",
         url="https://www.instagram.com/drugacna_pot/", reg="", confirmed=True),
    dict(name="Zavod Hipo Team", place="Brje pri Dobravljah", region=["Goriška"], group="register", offer=["H", "P", "A"],
         who="Otroci, mladostniki in odrasli s posebnimi potrebami; programi za društva in zavode",
         team="Kristina Naglost, terapevtka s pomočjo konja (prva generacija usposabljanja v Starošincih)", horses="1",
         programs="Hipoterapija v sodelovanju s fizioterapevti-hipoterapevti z Vipavske doline, pedagoško jahanje in aktivnosti s konji, več kot 25 let",
         url="", reg="", confirmed=True),
    dict(name="Društvo Ha-Li", place="Pivka", region=["Primorsko-notranjska"], group="register", offer=["A"],
         who="Delavnice, tudi za osebe s posebnimi potrebami", team="Katarina Žmak, strokovna sodelavka", horses="4",
         url="", reg=REG + "katarina-zmak/"),
    dict(name="Kmetija Tomaževi", place="Hruševje", region=["Obalno-kraška"], group="register", offer=["A"],
         who="Osebe s posebnimi potrebami", team="Zala Stegel, strokovna sodelavka", horses="2",
         url="", reg=REG + "zala-stegel-strokovna-sodelavka-za-izvajanje-aktivnosti-s-pomocjo-konja/"),
    # --- drugi centri (ponudba po navedbah centrov) ---
    dict(name="Konjeniški klub Celje", place="Škofja vas", region=["Savinjska"], group="drugi", offer=["T", "J"],
         who="Individualno, 30-minutna srečanja", team="Nina Korošec Mladenović, mag. inkluzivne pedagogike", horses="",
         url="https://skonji.si/", reg=""),
    dict(name="Zavod Pegaz", place="Sevno pri Novem mestu", region=["Jugovzhodna Slovenija"], group="drugi", offer=["T"],
         who="Terapije in strokovna predavanja", team="", horses="", url="https://zavod-pegaz.si/", reg=""),
    dict(name="Društvo Hippos", place="Slovenska Istra", region=["Obalno-kraška"], group="drugi", offer=["H", "J", "A"],
         who="Otroci; hipoterapija in terapevtsko jahanje", team="", horses="4", url="https://drustvohippos.si/", reg=""),
    dict(name="Konjeniški center Si", place="Ljubljana, Stožice", region=["Osrednjeslovenska"], group="drugi", offer=["H", "P", "S", "J"],
         who="Hipoterapija, pedagoško in psihoterapevtsko jahanje, prilagojeno športno jahanje", team="", horses="",
         url="https://www.konjeniskicenter.com/", reg=""),
    dict(name="Zavod Villa Artemida", place="Mirna Peč", region=["Jugovzhodna Slovenija"], group="register", offer=["T", "J", "A"],
         who="Otroci, mladostniki, odrasli, starejši, šolske in vrtčevske skupine ter uporabniki zavodov; individualno in v skupinah",
         programs="Terapije in aktivnosti s konji",
         team="Urša Rangus, inštruktorica jahanja, dipl. terapevtka s pomočjo konj, dipl. vzgojiteljica predšolskih otrok, vodja programov",
         horses="5", space="Zunanja jahalnica ali ograda, klančina za vzpenjanje, dostop za invalidski voziček, sanitarije, parkirišče",
         url="https://villa-artemida.si/", reg="", confirmed=True),
    dict(name="Zavod 16 podkvic", place="Litija", region=["Zasavska"], group="drugi", offer=["J"],
         who="Terapevtsko jahanje", team="", horses="", url=KZS + "zavod-16-podkvic/", reg=""),
    dict(name="Pesniški dvor", place="Pesnica pri Mariboru", region=["Podravska"], group="drugi", offer=["J", "A", "T"],
         who="Terapevtsko jahanje, aktivnosti in terapije s pomočjo konja", team="", horses="",
         url=KZS + "drustvo-za-aktivnosti-in-terapijo-s-pomocjo-konja-pesniski-dvor-happf-farm/", reg=""),
    dict(name="Posestvo Marsilea", place="Pacinje, Dornava", region=["Podravska"], group="drugi", offer=["J"],
         who="Terapevtsko jahanje, tudi za člane društva Sonček Ptuj–Ormož", team="", horses="",
         url="https://spc-cid.si/posestvo-marsilea/", reg=""),
    dict(name="Konjeniško-terapevtski zavod KONI", place="Ravne na Koroškem", region=["Koroška"], group="drugi", offer=["A"],
         who="Konjeniške aktivnosti", team="", horses="", url=KZS + "konjeniski-center-lava-2/", reg=""),
    # --- društva, ki programe organizirajo ---
    dict(name="Sonček – Mariborsko društvo za cerebralno paralizo", place="Maribor", region=["Podravska"], group="organizator", offer=["J", "H"],
         who="Člani društva; terapevtsko jahanje na partnerskih lokacijah", team="", horses="", url="https://www.soncek.org/drustva/", reg=""),
    dict(name="Sonček Ptuj–Ormož", place="Ptuj", region=["Podravska"], group="organizator", offer=["H"],
         who="Člani društva; hipoterapija na Posestvu Marsilea", team="", horses="", url="https://www.soncek.org/drustva/", reg=""),
    dict(name="Društvo Sonček Posavje", place="Leskovec pri Krškem", region=["Posavska"], group="organizator", offer=["H", "J"],
         who="Člani društva", team="", horses="", url="https://www.soncek.org/drustva/", reg=""),
    dict(name="Društvo Sonček Celje", place="Celje", region=["Savinjska"], group="organizator", offer=["J"],
         who="Člani društva", team="", horses="", url="https://www.soncek.org/drustva/", reg=""),
    dict(name="Sonček – Gorenjsko društvo za cerebralno paralizo", place="Kranj", region=["Gorenjska"], group="organizator", offer=["H"],
         who="Člani društva", team="", horses="", url="https://www.soncek.org/drustva/", reg=""),
    dict(name="Sonček – Primorsko društvo za cerebralno paralizo", place="Nova Gorica", region=["Goriška"], group="organizator", offer=["H"],
         who="Člani društva; hipoterapija v Brjah", team="", horses="", url="https://www.soncek.org/drustva/", reg=""),
    dict(name="Sonček – Notranjsko društvo za cerebralno paralizo", place="Slavinje", region=["Primorsko-notranjska"], group="organizator", offer=["H", "J"],
         who="Člani društva; Brinje pri Vipavi", team="", horses="", url="https://www.soncek.org/drustva/", reg=""),
    dict(name="Sonček – Društvo za cerebralno paralizo Dolenjske in Bele krajine", place="Novo mesto", region=["Jugovzhodna Slovenija"], group="organizator", offer=["H", "J"],
         who="Člani društva", team="", horses="", url="https://www.soncek.org/drustva/", reg=""),
    dict(name="Društvo za cerebralno paralizo Ponikve", place="Videm-Dobrepolje", region=["Osrednjeslovenska"], group="organizator", offer=["H"],
         who="Člani, tudi odrasli", team="", horses="", url="https://www.soncek.org/drustva/", reg=""),
]


def shown_centers():
    """Centri, ki so potrdili sodelovanje in so javno prikazani."""
    return [c for c in CENTERS if c.get("confirmed")]


# ---------------- MREŽA SODELOVANJ ----------------
# Obstoječa sodelovanja med centri in ustanovami (šole, vrtci, zavodi, društva).
# center  = točno ime centra iz CENTERS (center mora biti prikazan, confirmed=True)
# partner = ime ustanove; kraj; regija (ena od REGIONS); vrsta = Šola / Vrtec / Zavod / Društvo / Občina / Drugo / Center (sodelovanje med centri – ne prikažemo med ustanovami)
# kaj     = kratko, kaj izvajajo skupaj
# vir     = "potrjeno" (potrdili obe strani) | "center" (navedel center) | "javno" (javni vir, npr. spletna stran ustanove)
# porocilo = (neobvezno) povezava do javnega poročila o skupnem programu; prikaže se le, če obstaja
PARTNERSHIPS = [
    # Iz javnih virov (19. 11. 2026) – v potrditev poslano centrom po e-pošti; vir_url = kje je sodelovanje objavljeno.
    # Rock Ranč – navedla Živa Logar v obrazcu (22. 11. 2026), objava potrjena
    dict(center="Zavedno delo s konji, Rock Ranč", partner="Strokovni center Kranj", kraj="Kranj", regija="Gorenjska", vrsta="Zavod", kaj="Projekt aktivnosti s pomočjo konj za mladostnike (2026), načrtujejo nadaljevanje", vir="potrjeno", vir_url="https://vzkranj.splet.arnes.si/2026/08/02/rock-ranc/"),
    dict(center="Zavedno delo s konji, Rock Ranč", partner="OŠ Ferda Vesela Šentvid pri Stični", kraj="Šentvid pri Stični", regija="Osrednjeslovenska", vrsta="Šola", kaj="Sodelovanje s šolo", vir="center"),
    dict(center="Zavedno delo s konji, Rock Ranč", partner="CSD Grosuplje (Palčica)", kraj="Grosuplje", regija="Osrednjeslovenska", vrsta="Zavod", kaj="Sodelovanje s CSD", vir="center"),
    dict(center="Zavedno delo s konji, Rock Ranč", partner="Strokovni center Višnja Gora", kraj="Višnja Gora", regija="Osrednjeslovenska", vrsta="Zavod", kaj="Izobraževanje strokovnih delavk in obisk mladostnikov na ranču", vir="potrjeno"),
    dict(center="Zavedno delo s konji, Rock Ranč", partner="Bolnišnica za otroke Šentvid pri Stični", kraj="Šentvid pri Stični", regija="Osrednjeslovenska", vrsta="Zavod", kaj="Sodelovanje z bolnišnico", vir="center"),
    dict(center="Zavedno delo s konji, Rock Ranč", partner="Zavod Nazaj na konja", kraj="Starošince", regija="Podravska", vrsta="Center", kaj="Strokovno sodelovanje", vir="center"),
    dict(center="Zavedno delo s konji, Rock Ranč", partner="Vzgojni zavod Veržej", kraj="Veržej", regija="Pomurska", vrsta="Zavod", kaj="Erasmus+ projekt Konjerastniki", vir="javno", vir_url="https://www.vzgojni-zavod-verzej.si/2026/06/01/konjerastniki-zakljucek-projekta/"),
    dict(center="Zavod Škatlica", partner="Vzgojni zavod Veržej", kraj="Veržej", regija="Pomurska", vrsta="Zavod", kaj="Erasmus+ projekt Konjerastniki", vir="javno", vir_url="https://www.vzgojni-zavod-verzej.si/2026/06/01/konjerastniki-zakljucek-projekta/"),
    dict(center="Zavod Hipo Team", partner="CIRIUS Vipava", kraj="Vipava", regija="Goriška", vrsta="Zavod", kaj="Hipoterapija", vir="center"),
    dict(center="Zavod Hipo Team", partner="Sonček – Primorsko društvo za cerebralno paralizo", kraj="Nova Gorica", regija="Goriška", vrsta="Društvo", kaj="Hipoterapija in aktivnosti s konji", vir="center"),
    dict(center="Zavod Hipo Team", partner="Sožitje Ajdovščina-Vipava", kraj="Ajdovščina", regija="Goriška", vrsta="Društvo", kaj="Aktivnosti s konji", vir="center"),
    dict(center="Zavod Hipo Team", partner="Sonček – Notranjsko društvo za cerebralno paralizo", kraj="Slavinje", regija="Primorsko-notranjska", vrsta="Društvo", kaj="Hipoterapija", vir="center"),
    dict(center="Marengo dežela", partner="Društvo Sožitje Krško", kraj="Krško", regija="Posavska", vrsta="Društvo", kaj="Redno sodelovanje", vir="center"),
    dict(center="Marengo dežela", partner="Društvo Sožitje Brežice", kraj="Brežice", regija="Posavska", vrsta="Društvo", kaj="Redno sodelovanje", vir="center"),
    dict(center="Marengo dežela", partner="Društvo za cerebralno paralizo Sonček Posavje", kraj="Leskovec pri Krškem", regija="Posavska", vrsta="Društvo", kaj="Redno sodelovanje", vir="center"),
    dict(center="Marengo dežela", partner="OŠ dr. Mihajla Rostoharja Krško", kraj="Krško", regija="Posavska", vrsta="Šola", kaj="Občasno sodelovanje", vir="center"),
    dict(center="Konjeniški zavod EPONA", partner="Polžek – društvo za otroke s posebnimi potrebami", kraj="Novo mesto", regija="Jugovzhodna Slovenija", vrsta="Društvo", kaj="Terapije s pomočjo konja za otroke", vir="center"),
    dict(center="Konjeniški zavod EPONA", partner="Sonček – Društvo za cerebralno paralizo Dolenjske in Bele krajine", kraj="Novo mesto", regija="Jugovzhodna Slovenija", vrsta="Društvo", kaj="Terapije s pomočjo konja", vir="center"),
    dict(center="Marengo dežela", partner="OŠ Ane Gale Sevnica", kraj="Sevnica", regija="Posavska", vrsta="Šola", kaj="Občasno sodelovanje", vir="center"),
]


# ---------------- KOORDINATE ZA ZEMLJEVID MREŽE ----------------
# Približna lega po kraju (lat, lng). Ključ = ime centra iz CENTERS ali ime partnerja iz PARTNERSHIPS.
# Nov center ali partner brez koordinat se na zemljevidu ne pokaže (v seznamu pa je).
COORDS = {
    "CUDV Dobrna": (46.3366, 15.2264),
    "CUDV Draga": (45.9612, 14.5282),
    "CIRIUS Vipava": (45.8466, 13.9620),
    "Zavod Nazaj na konja": (46.3890, 15.7980),
    "Terapevtsko-konjeniški zavod Olsen": (45.6820, 14.1960),
    "Konjeniško-terapevtski zavod Arion": (46.0700, 14.4700),
    "Moonrise – terapije s pomočjo konj": (46.1360, 14.6000),
    "Zavedno delo s konji, Rock Ranč": (45.9530, 14.8430),
    "Marengo dežela": (46.0130, 15.3900),
    "Konjeniški zavod EPONA": (45.7880, 15.1250),
    "Polžek – društvo za otroke s posebnimi potrebami": (45.8040, 15.1560),
    "Sonček – Društvo za cerebralno paralizo Dolenjske in Bele krajine": (45.8075, 15.1610),
    "Športno-terapevtski klub Pegasus": (45.9980, 14.9290),
    "Konjeniški center AMAY": (46.2630, 15.1780),
    "Zavod Hipo Team": (45.8870, 13.7740),
    "Društvo Sožitje Krško": (45.9590, 15.4920),
    "Društvo Sožitje Brežice": (45.9040, 15.5920),
    "Društvo za cerebralno paralizo Sonček Posavje": (45.9370, 15.4620),
    "OŠ dr. Mihajla Rostoharja Krško": (45.9640, 15.4850),
    "OŠ Ane Gale Sevnica": (46.0080, 15.3150),
    "Sonček – Primorsko društvo za cerebralno paralizo": (45.9560, 13.6480),
    "Sožitje Ajdovščina-Vipava": (45.8870, 13.9090),
    "Sonček – Notranjsko društvo za cerebralno paralizo": (45.7160, 14.2450),
    "Strokovni center Kranj": (46.2390, 14.3556),
    "Vzgojni zavod Veržej": (46.5840, 16.1650),
    "OŠ Ferda Vesela Šentvid pri Stični": (45.9500, 14.8410),
    "CSD Grosuplje (Palčica)": (45.9550, 14.6580),
    "Strokovni center Višnja Gora": (45.9580, 14.7460),
    "Bolnišnica za otroke Šentvid pri Stični": (45.9545, 14.8470),
}


# Spletne strani partnerjev v mreži (ime iz PARTNERSHIPS -> povezava).
# Kjer ustanova nima svoje strani, je povezava na stran zveze, ki jo navaja.
PARTNER_URLS = {
    "Polžek – društvo za otroke s posebnimi potrebami": "http://www.polzek.si/",
    "CIRIUS Vipava": "https://www.cirius-vipava.si/",
    "Strokovni center Kranj": "https://www.sc-kranj.si/",
    "Vzgojni zavod Veržej": "https://www.vzgojni-zavod-verzej.si/",
    "OŠ dr. Mihajla Rostoharja Krško": "https://osmr.splet.arnes.si/",
    "OŠ Ane Gale Sevnica": "https://www.os-anegale.si/",
    "Društvo Sožitje Krško": "https://www.zveza-sozitje.si/zasavsko-posavsko-in-dolenjsko-podrocje.html",
    "Društvo Sožitje Brežice": "https://www.zveza-sozitje.si/zasavsko-posavsko-in-dolenjsko-podrocje.html",
    "Sožitje Ajdovščina-Vipava": "https://www.zveza-sozitje.si/",
    "Društvo za cerebralno paralizo Sonček Posavje": "https://www.soncek.org/drustva/",
    "Sonček – Primorsko društvo za cerebralno paralizo": "https://www.soncek.org/drustva/",
    "Sonček – Notranjsko društvo za cerebralno paralizo": "https://www.soncek.org/drustva/",
}


# Projekti za podporo (Equeli Impact). Objavimo samo projekte, ki jih je izvajalec potrdil.
# Denar gre neposredno izvajalcu; Equeli sredstev ne zbira in ne posreduje.
PROJECTS = [
    dict(slug="epona-terapije-2027", kind="Terapije", center="Konjeniški zavod EPONA", place="Novo mesto · Jugovzhodna Slovenija",
         title="Redne terapije s pomočjo konja za otroke v letu 2027",
         goal="Otrokom s posebnimi potrebami iz družin, ki si rednih obravnav ne morejo privoščiti, omogočiti celoten cikel terapije s pomočjo konja.",
         who="Otroci s posebnimi potrebami; Epona sodeluje z društvom Polžek in Društvom Sonček Dolenjske in Bele krajine",
         budget=[("Pet obravnav za enega otroka", "220 €"), ("Cel cikel desetih obravnav za enega otroka", "400 €"), ("Cikel desetih obravnav za pet otrok", "2.000 €")],
         total="400 € na otroka", note="Zneski temeljijo na cenah Epone. Podpora je mogoča kot donacija ali sponzorstvo."),
    dict(slug="epona-raziskava-myotonpro", kind="Raziskava", center="Konjeniški zavod EPONA", place="Novo mesto · Jugovzhodna Slovenija",
         title="Klinična raziskava: hipoterapija pri spastični cerebralni paralizi",
         goal="Epona načrtuje klinično raziskavo, kako hipoterapija vpliva na viskoelastične lastnosti ledvenega dela fascije pri osebah s spastično obliko cerebralne paralize. Meritve so neinvazivne in neboleče. Raziskavo je odobrila Komisija za etiko RS.",
         who="Osebe s spastično obliko cerebralne paralize; meritve vsak dan, najmanj šest mesecev",
         budget=[("Naprava MyotonPRO za merjenje lastnosti mehkih tkiv", "7.285 €")],
         total="7.285 €", note="Znesek po aktualni ponudbi proizvajalca.",
         link=("myoton.com", "https://www.myoton.com/")),
    dict(slug="rock-ranc-zavodi-2027", kind="Delavnice in terapije", center="Zavedno delo s konji, Rock Ranč", place="Šentvid pri Stični · Osrednjeslovenska",
         title="Otroci iz zavodov ob konjih v letu 2027",
         goal="Skupinam iz zavodov omogočiti, da tudi v letu 2027 redno prihajajo na ranč. Otroci ob konjih, v naravi in z vrstniki gradijo sodelovanje, zaupanje, zdrave meje in samoregulacijo. Programi so se izkazali, projektna sredstva pa se iztekajo.",
         who="Otroci in mladostniki s posebnimi potrebami ter iz ranljivih okolij; Rock Ranč sodeluje s Strokovnim centrom Kranj, SC Višnja Gora, Bolnišnico za otroke Šentvid pri Stični in CSD Grosuplje (Palčica)",
         budget=[("Dvourna delavnica s konji za skupino petih mladostnikov", "300 €"), ("Dan dejavnosti s konji za cel razred (25 učencev)", "375 €"), ("Deset ur redne terapije s pomočjo konja za enega otroka", "600 €"), ("Deset delavnic za skupino iz zavoda, celo leto", "3.000 €")],
         total="od 300 €", note="Zneski temeljijo na cenah Rock Ranča. Podpora je mogoča kot donacija ali sponzorstvo.",
         link=("rockranch.si", "https://rockranch.si/")),
]
