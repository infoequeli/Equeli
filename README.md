# EQUELI – spletna stran

Statična spletna stran za Cloudflare Pages. Brez strežnika, brez baze, brez piškotkov.

## Struktura
- `build.py` – vsa vsebina (vodniki, besedila, regije, povezave na obrazce) in generator strani.
- `public/` – zgrajena stran, ki jo objavi Cloudflare.
- `public/assets/` – oblikovanje (`style.css`), skripte (`app.js`), ikona.

## Sprememba vsebine
1. Uredi besedilo v `build.py`.
2. Zaženi `python3 build.py`.
3. Shrani spremembe v GitHub (commit + push). Cloudflare objavi samodejno.

## Nastavitev Cloudflare Pages (enkratno)
1. Cloudflare → Workers & Pages → Create → Pages → Connect to Git → izberi repozitorij `equeli`.
2. Framework preset: **None**. Build command: *pusto*. Build output directory: **public**.
3. Save and Deploy. Stran bo na `https://equeli.info-equeli.workers.dev` (ali podobnem naslovu).
4. Ko bo domena, jo dodaj pod Custom domains in v `build.py` popravi `SITE`.

## Obrazci
Začasno vodijo na delujoče obrazce na equeli.wordpress.com. Ko bodo obrazci v Tallyju,
zamenjaj povezave v slovarju `FORMS` v `build.py` in posodobi stran Zasebnost.

## Pravila
- Ne dodajaj nepotrjenih podatkov o izvajalcih. Raziskovalna baza ostane zasebna in ni v tem repozitoriju.
- Vodnike pred širšo promocijo pregleda strokovnjak.
