"""Equeli – vodeno iskanje (starši in ustanove). Vprašanja in povezave urejate tukaj."""
import json
from html import escape as e
from content import APPROACHES, REGIONS, CENTERS, GUIDES

WHO_P = [("otrok", "Za otroka"), ("mladostnik", "Za mladostnika"), ("odrasel", "Za odraslo osebo"), ("starejsi", "Za starejšo osebo")]
GOALS_P = [
    ("gibanje", "Gibanje, drža in ravnotežje", ["H", "D", "J"]),
    ("komunikacija", "Komunikacija in govor", ["P", "T", "D"]),
    ("custva", "Čustva in vedenje", ["S", "T", "P"]),
    ("ucenje", "Pozornost in učenje", ["P", "T"]),
    ("samostojnost", "Samostojnost in vsakdanje veščine", ["D", "P"]),
    ("odnosi", "Samozavest in odnosi", ["S", "T"]),
    ("sprostitev", "Sprostitev, gibanje v naravi in druženje", ["A", "J"]),
]
NEEDS_P = [
    ("gibalne", "Cerebralna paraliza ali druge gibalne ovire", ["H", "D", "J"], "gibalne-tezave", "Za hipoterapijo izvajalci običajno potrebujejo mnenje zdravnika ali fizioterapevta."),
    ("avtizem", "Avtizem", ["T", "P", "D"], "avtizem", "Vprašajte, kako izvajalec prilagodi okolje: hrup, število ljudi in predvidljiv potek."),
    ("adhd", "ADHD ali težave s pozornostjo", ["P", "T", "S"], "adhd", ""),
    ("mdr", "Motnje v duševnem razvoju", ["T", "D", "J"], "motnje-v-dusevnem-razvoju", ""),
    ("down", "Downov sindrom", ["T", "D", "J"], "motnje-v-dusevnem-razvoju", "Pri jahanju in hipoterapiji je pogosto potrebno zdravniško mnenje o vratni hrbtenici."),
    ("gluhi", "Gluhota ali naglušnost", [], "", "Večina pristopov je primerna. Vprašajte, ali izvajalec uporablja vizualna navodila ali omogoča tolmača za slovenski znakovni jezik."),
    ("slepi", "Slepota ali slabovidnost", ["J", "A", "H"], "", "Pomembni so jasna glasovna navodila, stalno vodenje konja in znano okolje."),
    ("govor", "Govorno-jezikovne težave", ["P", "T", "D"], "", ""),
    ("senzorne", "Senzorne težave", ["D", "H"], "", ""),
    ("ucne", "Učne težave", ["P"], "ucne-custvene-vedenjske-tezave", ""),
    ("vedenjske", "Vedenjske težave", ["P", "S"], "ucne-custvene-vedenjske-tezave", ""),
    ("custvene", "Tesnoba, depresija ali čustvene stiske", ["S", "T"], "tesnoba-samopodoba-odnosi", "Izberite strokovnjaka s psihološko ali psihoterapevtsko izobrazbo. V stiski je prvi korak osebni zdravnik ali svetovalni center."),
    ("travma", "Travmatska izkušnja", ["S", "T"], "tesnoba-samopodoba-odnosi", "Izberite strokovnjaka s psihološko ali psihoterapevtsko izobrazbo in vprašajte za izkušnje s travmo."),
    ("bolezen", "Kronična bolezen ali rehabilitacija po poškodbi", ["H", "D"], "gibalne-tezave", "Primernost vedno oceni zdravnik."),
    ("demenca", "Demenca ali starostne težave", ["A", "D"], "", ""),
    ("brez", "Nič od tega ali ne vem", [], "", ""),
]

INST_S = [("os", "Osnovna šola"), ("ss", "Srednja šola"), ("vrtec", "Vrtec"), ("cudv", "CUDV ali zavod"), ("dom", "Dom za starejše"), ("drustvo", "Društvo ali NVO")]
AGE_S = [("predsolski", "Predšolski otroci"), ("1-5", "1.–5. razred"), ("6-9", "6.–9. razred"), ("dijaki", "Dijaki"), ("odrasli", "Odrasli"), ("starejsi", "Starejši")]
NEEDS_S = [
    ("splosna", "Splošna populacija, celoten razred", ["P", "A"], ""),
    ("ucne", "Učne težave", ["P"], ""),
    ("vedenjske", "Čustvene in vedenjske težave", ["P", "S"], ""),
    ("avtizem", "Avtizem", ["T", "P", "D"], ""),
    ("mdr", "Motnje v duševnem razvoju", ["T", "D", "J"], ""),
    ("gibalne", "Gibalna oviranost", ["H", "D", "J"], "Za hipoterapijo je potrebna individualna obravnava in mnenje zdravnika."),
    ("gluhi", "Gluhi in naglušni", [], "Vprašajte za vizualna navodila ali tolmača za slovenski znakovni jezik."),
    ("slepi", "Slepi in slabovidni", ["J", "A"], "Pomembna so glasovna navodila in stalno vodenje konja."),
    ("ranljivi", "Ranljive skupine, socialna vključenost", ["S", "A"], ""),
]
GOALS_S = [
    ("delavnica", "Enkratna delavnica ali dan dejavnosti", ["P", "A"]),
    ("program", "Redni program skozi leto", ["P", "T", "S"]),
    ("terapija", "Terapevtski program za posameznike", ["T", "H", "D", "S"]),
    ("rekreacija", "Šola v naravi, tabor ali rekreacija", ["J", "A"]),
    ("predavanje", "Predavanje za strokovne delavce", []),
]

REGION_NAMES = [r for r, _ in REGIONS]


def _centers_json():
    return [dict(n=c["name"], p=c["place"], r=c["region"], o=c["offer"], g=c["group"], u=c["url"] or c["reg"]) for c in CENTERS if c["group"] in ("javni", "register")]


def finder(mode):
    A = {k: dict(n=v[0], d=v[1], w=v[2]) for k, v in APPROACHES.items()}
    if mode == "parents":
        steps = [
            dict(id="who", q="Za koga iščete?", type="one", opts=WHO_P, extra=[("/za-sole-in-zavode/", "Za šolo ali zavod")]),
            dict(id="goals", q="Kaj bi radi podprli?", hint="Izberete lahko več možnosti. Mislite na cilje, ne na diagnozo.", type="many", opts=[(k, l) for k, l, _ in GOALS_P]),
            dict(id="needs", q="Ali gre za katero od teh področij?", hint="Neobvezno. Pomaga nam, da dodamo koristne napotke.", type="many", opts=[(n[0], n[1]) for n in NEEDS_P], optional=True),
            dict(id="region", q="V kateri regiji iščete?", type="region", opts=[(r, r) for r in REGION_NAMES] + [("", "Ni pomembno")]),
        ]
        maps = dict(goals={k: a for k, _, a in GOALS_P}, needs={n[0]: n[2] for n in NEEDS_P},
                    notes={n[0]: n[4] for n in NEEDS_P if n[4]}, guides={n[0]: n[3] for n in NEEDS_P if n[3]},
                    labels={**{k: l for k, l, _ in GOALS_P}, **{n[0]: n[1] for n in NEEDS_P}},
                    goalGuides={"gibanje": "gibalne-tezave", "custva": "tesnoba-samopodoba-odnosi", "ucenje": "adhd", "sprostitev": "aktivnost-ob-konjih"})
        cta = [("za-starse/#iskanje", "Pomagamo vam najti izvajalca", True), ("izvajalci/", "Vsi centri", False)]
    else:
        steps = [
            dict(id="inst", q="Kakšna je vaša ustanova?", type="one", opts=INST_S),
            dict(id="age", q="Kdo bodo udeleženci?", hint="Izberete lahko več možnosti.", type="many", opts=AGE_S),
            dict(id="needs", q="Kakšne so potrebe skupine?", hint="Izberete lahko več možnosti.", type="many", opts=[(n[0], n[1]) for n in NEEDS_S]),
            dict(id="goals", q="Kaj želite organizirati?", type="many", opts=[(k, l) for k, l, _ in GOALS_S]),
            dict(id="region", q="Kje je vaša ustanova?", type="region", opts=[(r, r) for r in REGION_NAMES]),
        ]
        maps = dict(goals={k: a for k, _, a in GOALS_S}, needs={n[0]: n[2] for n in NEEDS_S},
                    notes={**{n[0]: n[3] for n in NEEDS_S if n[3]}, "predavanje": "Predavanja za strokovne delavce ponujajo nekateri izvajalci. Označite to v povpraševanju."},
                    guides={}, labels={**{k: l for k, l, _ in GOALS_S}, **{n[0]: n[1] for n in NEEDS_S}}, goalGuides={})
        cta = [("za-sole-in-zavode/#povprasevanje", "Oddajte povpraševanje", True), ("izvajalci/", "Vsi centri", False)]
    maps["gtitle"] = {g["slug"]: g["title"] for g in GUIDES}
    cfg = dict(mode=mode, steps=steps, maps=maps, A=A, C=_centers_json(), cta=cta)
    data = json.dumps(cfg, ensure_ascii=False).replace("</", "<\\/")
    intro = ("Delo s konji ima več oblik: od fizioterapije na konju do pedagoških delavnic in sproščenih aktivnosti. "
             "Katera je primerna, je odvisno od tega, kaj želite doseči. Odgovorite na nekaj vprašanj, mi pa vam pokažemo možnosti in centre v vaši bližini.") if mode == "parents" else \
            ("Programi s konji za skupine se razlikujejo po namenu, trajanju in strokovnosti. Opišite svojo ustanovo in skupino, "
             "pokažemo vam ustrezne vrste programov in centre v vaši regiji.")
    title = "Poiščite ustrezen pristop" if mode == "parents" else "Kateri program je za vašo skupino?"
    sid = "vodnik-start" if mode == "parents" else "izbira-programa"
    return f"""
<section class="band section" id="{sid}">
  <div class="wrap">
    <div class="head"><p class="kicker">Vodeno iskanje</p><h2>{title}</h2><p class="lede">{intro}</p></div>
    <div class="finder" data-base="/">
      <script type="application/json">{data}</script>
      <div class="fd-top"><span class="fd-n"></span><div class="fd-bar"><i></i></div></div>
      <div class="fd-body" aria-live="polite"></div>
      <div class="fd-nav"><button type="button" class="btn btn-text fd-back">← Nazaj</button><span class="sp"></span><button type="button" class="btn btn-dark fd-next">Naprej</button></div>
      <noscript><p><a href="/vodnik/">Odprite seznam vodnikov</a> ali <a href="/kontakt/">nam pišite</a>.</p></noscript>
    </div>
  </div>
</section>"""
