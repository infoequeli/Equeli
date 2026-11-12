"""Equeli – obrazci na strani.

Oddaje pošilja storitev FormSubmit (https://formsubmit.co) na e-poštni naslov Equeli.
Ob prvi oddaji pride na info.equeli@gmail.com e-pošta za aktivacijo – kliknite »Activate Form«.
Polja urejate tukaj; nato zaženite: python3 build.py
"""
from html import escape as e
from content import SITE, EMAIL, REGIONS, APPROACHES, GUIDES

ACTION = f"https://formsubmit.co/{EMAIL}"
REGION_NAMES = [r for r, _ in REGIONS]

_n = [0]


def _id(name):
    _n[0] += 1
    return f"f{_n[0]}"


def text(name, label, required=False, type="text", auto="", hint="", placeholder=""):
    i = _id(name)
    req = ' required aria-required="true"' if required else ""
    star = ' <span class="req" aria-hidden="true">*</span>' if required else ' <span class="opt">neobvezno</span>'
    h = f'<span class="hint" id="{i}h">{hint}</span>' if hint else ""
    desc = f' aria-describedby="{i}h"' if hint else ""
    ac = f' autocomplete="{auto}"' if auto else ""
    ph = f' placeholder="{e(placeholder)}"' if placeholder else ""
    return f'<div class="field"><label for="{i}">{label}{star}</label>{h}<input id="{i}" name="{e(name)}" type="{type}"{req}{ac}{ph}{desc}></div>'


def area(name, label, required=False, hint="", rows=4):
    i = _id(name)
    req = ' required aria-required="true"' if required else ""
    star = ' <span class="req" aria-hidden="true">*</span>' if required else ' <span class="opt">neobvezno</span>'
    h = f'<span class="hint" id="{i}h">{hint}</span>' if hint else ""
    desc = f' aria-describedby="{i}h"' if hint else ""
    return f'<div class="field"><label for="{i}">{label}{star}</label>{h}<textarea id="{i}" name="{e(name)}" rows="{rows}"{req}{desc}></textarea></div>'


def select(name, label, options, required=False, hint=""):
    i = _id(name)
    req = ' required aria-required="true"' if required else ""
    star = ' <span class="req" aria-hidden="true">*</span>' if required else ' <span class="opt">neobvezno</span>'
    h = f'<span class="hint" id="{i}h">{hint}</span>' if hint else ""
    opts = '<option value="">Izberite</option>' + "".join(f'<option>{e(o)}</option>' for o in options)
    return f'<div class="field"><label for="{i}">{label}{star}</label>{h}<select id="{i}" name="{e(name)}"{req}>{opts}</select></div>'


def radios(name, label, options, required=False, hint=""):
    req = " required" if required else ""
    star = ' <span class="req" aria-hidden="true">*</span>' if required else ' <span class="opt">neobvezno</span>'
    h = f'<span class="hint">{hint}</span>' if hint else ""
    items = "".join(f'<label class="choice"><input type="radio" name="{e(name)}" value="{e(o)}"{req if k == 0 else ""}><span>{e(o)}</span></label>' for k, o in enumerate(options))
    return f'<fieldset class="field"><legend>{label}{star}</legend>{h}<div class="choices">{items}</div></fieldset>'


def checks(prefix, label, options, hint=""):
    """Vsaka izbira je svoje polje (npr. »Pristop: Hipoterapija = da«), da je v e-pošti pregledno."""
    h = f'<span class="hint">{hint}</span>' if hint else ""
    items = "".join(f'<label class="choice"><input type="checkbox" name="{e(prefix)}: {e(o)}" value="da"><span>{e(o)}</span></label>' for o in options)
    return f'<fieldset class="field"><legend>{label} <span class="opt">izberite vse, kar velja</span></legend>{h}<div class="choices">{items}</div></fieldset>'


def group(title, *fields, note=""):
    n = f'<p class="group-note">{note}</p>' if note else ""
    return f'<div class="fgroup"><h3>{title}</h3>{n}<div class="fgrid">{"".join(fields)}</div></div>'


def form(fid, subject, intro, groups, consent, submit):
    return f"""<form class="eform" id="{fid}" action="{ACTION}" method="POST" accept-charset="UTF-8" novalidate>
  <input type="hidden" name="_subject" value="{e(subject)}">
  <input type="hidden" name="_next" value="{SITE}/hvala/">
  <input type="hidden" name="_template" value="table">
  <input type="hidden" name="_captcha" value="false">
  <input type="hidden" name="Obrazec" value="{e(subject)}">
  <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
  <div class="form-head"><p class="form-intro">{intro}</p><p class="form-legend"><span class="req">*</span> obvezno polje</p></div>
  {''.join(groups)}
  <div class="fgroup consent">
    <label class="choice block"><input type="checkbox" name="Soglasje" value="da" required><span>{consent} Več v <a href="/zasebnost/">obvestilu o zasebnosti</a>.</span></label>
  </div>
  <div class="form-error" role="alert" hidden>Prosimo, izpolnite označena polja.</div>
  <div class="form-foot"><button class="btn btn-dark btn-lg" type="submit">{submit}</button><span class="form-time">Odgovorimo v nekaj delovnih dneh.</span></div>
</form>"""


# ---------------- Obrazec za izvajalce ----------------
def provider_form():
    return form("obrazec", "Equeli – prijava izvajalca",
        "Izpolnite, kar veste. Manjkajoče lahko dopolnimo po telefonu ali ob obisku. Profil objavimo šele, ko ga potrdite.",
        [
            group("Organizacija",
                text("Ime organizacije ali izvajalca", "Ime organizacije ali izvajalca", True, auto="organization"),
                select("Pravna oblika", "Pravna oblika", ["Zavod", "Društvo", "Javni zavod", "Konjeniški center ali kmetija", "Samostojni podjetnik", "Posameznik", "Drugo"], True),
                radios("Vloga", "Kako delujete?", ["Programe izvajamo sami", "Programe koordiniramo, izvajajo drugi", "Oboje"], True),
                text("Spletna stran", "Spletna stran ali družbeno omrežje", type="url", auto="url", placeholder="https://"),
            ),
            group("Kontaktna oseba",
                text("Ime in priimek", "Ime in priimek", True, auto="name"),
                text("Vloga v organizaciji", "Vloga v organizaciji", placeholder="npr. vodja programov"),
                text("E-pošta", "E-pošta", True, type="email", auto="email"),
                text("Telefon", "Telefon", type="tel", auto="tel"),
            ),
            group("Lokacija",
                select("Regija", "Regija", REGION_NAMES, True),
                text("Kraj izvajanja", "Kraj ali naslov izvajanja", True, auto="address-level2", hint="Če izvajate na več lokacijah, jih naštejte."),
            ),
            group("Programi",
                checks("Pristop", "Pristopi, ki jih izvajate", [v[0] for v in APPROACHES.values()]),
                checks("Skupina", "Komu so programi namenjeni", ["Otroci", "Mladostniki", "Odrasli", "Starejši", "Šolske in vrtčevske skupine", "Uporabniki zavodov"]),
                checks("Oblika", "Oblika dela", ["Individualno", "V manjših skupinah", "Za razrede ali večje skupine", "Tabori ali počitniški programi"]),
                area("Opis programov", "Kratek opis programov", hint="Cilji, trajanje srečanj, potek. Nekaj stavkov je dovolj."),
                text("Cena", "Okvirna cena", hint="Npr. 35 € za 45 minut. Napišite, če ceno želite objaviti."),
            ),
            group("Strokovna ekipa",
                area("Ekipa", "Kdo izvaja programe", True, hint="Ime, osnovna stroka (npr. fizioterapevt, specialni pedagog) in usposabljanje za delo s konjem."),
                radios("Register", "Ali ste vpisani v register usposobljenih strokovnjakov Zavoda Nazaj na konja?", ["Da", "Ne", "V postopku", "Ne vem"], True),
                text("Drugo usposabljanje", "Drugo usposabljanje ali certifikat", hint="Npr. tuja usposabljanja, članstvo v strokovnih združenjih."),
            ),
            group("Konji in prostor",
                text("Število konj", "Število konj v programih", type="number"),
                checks("Prostor", "Infrastruktura", ["Pokrita jahalnica", "Zunanja jahalnica ali ograda", "Klančina ali dvižna naprava za vzpenjanje", "Dostop za invalidski voziček", "Sanitarije", "Parkirišče"]),
            ),
            group("Sodelovanje",
                checks("Interes", "Kaj vas zanima", ["Sodelovanje s šolami in vrtci", "Sodelovanje z zavodi", "Projekti s podporo podjetij ali fundacij", "Obisk in predstavitev na Equeli"]),
                area("Sporočilo", "Še kaj, kar želite sporočiti", rows=3),
            ),
        ],
        "Soglašam, da Equeli moje podatke uporabi za pripravo profila in za stik z mano. Javno bodo objavljeni samo podatki, ki jih potrdim.",
        "Pošljite prijavo")


# ---------------- Povpraševanje ustanove ----------------
def school_form():
    return form("povprasevanje", "Equeli – povpraševanje ustanove",
        "Opišite, kaj iščete. Pripravimo predlog ustreznih izvajalcev v vaši regiji in vas povežemo z njimi.",
        [
            group("Ustanova",
                text("Ime ustanove", "Ime ustanove", True, auto="organization"),
                select("Vrsta ustanove", "Vrsta ustanove", ["Osnovna šola", "Srednja šola", "Vrtec", "CUDV ali zavod za usposabljanje", "Dom za starejše", "Društvo ali nevladna organizacija", "Drugo"], True),
                select("Regija", "Regija", REGION_NAMES, True),
                text("Kraj", "Kraj", True, auto="address-level2"),
            ),
            group("Kontaktna oseba",
                text("Ime in priimek", "Ime in priimek", True, auto="name"),
                text("Vloga v ustanovi", "Vloga v ustanovi", placeholder="npr. svetovalna delavka, ravnatelj"),
                text("E-pošta", "E-pošta", True, type="email", auto="email"),
                text("Telefon", "Telefon", type="tel", auto="tel"),
            ),
            group("Skupina",
                text("Starost udeležencev", "Starost udeležencev", True, placeholder="npr. 7–9 let"),
                text("Število udeležencev", "Število udeležencev", True, type="number"),
                checks("Prilagoditve", "Potrebne prilagoditve", ["Gibalne ovire ali invalidski voziček", "Senzorne potrebe", "Komunikacijska podpora", "Drugo, opisano spodaj"], hint="Ne navajajte imen ali diagnoz posameznikov."),
            ),
            group("Program",
                checks("Vrsta", "Kaj vas zanima", ["Delavnice za razred ali skupino", "Programi za otroke s posebnimi potrebami", "Prilagojeno jahanje ali aktivnosti", "Predavanje za strokovne delavce", "Ne vem, svetujte nam"]),
                text("Obdobje", "Želeno obdobje", True, placeholder="npr. spomladi 2027, enkrat tedensko"),
                radios("Financiranje", "Financiranje", ["Imamo sredstva", "Delno, iščemo dodatno podporo", "Iščemo financiranje", "Še ne vemo"], True),
                area("Opis potreb", "Opis potreb in ciljev", True, hint="Kaj želite doseči in kaj je za vas pomembno (npr. prevoz, termin, lokacija)."),
            ),
        ],
        "Soglašam, da Equeli podatke uporabi za odgovor in jih posreduje izbranim izvajalcem, da vam pripravijo ponudbo.",
        "Pošljite povpraševanje")


# ---------------- Kontakt ----------------
def contact_form():
    return form("obrazec", "Equeli – sporočilo s spletne strani",
        "Napišite nam. Če iščete izvajalca, navedite regijo in starost, da vam lažje svetujemo.",
        [
            group("Vaši podatki",
                text("Ime", "Ime", True, auto="name"),
                text("E-pošta", "E-pošta", True, type="email", auto="email"),
                select("Pišem kot", "Pišem kot", ["Starš ali skrbnik", "Odrasla oseba zase", "Izvajalec", "Šola, vrtec ali zavod", "Podjetje ali fundacija", "Novinar ali raziskovalec", "Drugo"], True),
                select("Regija", "Regija", REGION_NAMES),
            ),
            group("Sporočilo",
                select("Tema", "Tema", ["Pomoč pri iskanju izvajalca", "Popravek podatkov", "Sodelovanje", "Podpora programom", "Drugo"], True),
                select("Področje", "Področje", [g["title"] for g in GUIDES] + ["Drugo"], hint="Samo če iščete izvajalca."),
                area("Sporočilo", "Sporočilo", True, rows=6),
                note="Ne pošiljajte zdravstvene dokumentacije ali podrobnih podatkov o diagnozah."),
        ],
        "Soglašam, da Equeli moje podatke uporabi za odgovor na sporočilo.",
        "Pošljite sporočilo")
