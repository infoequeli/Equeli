"""Equeli – shematski zemljevid Slovenije s številom organizacij po regijah."""
from html import escape as e

OUT = [(13.71,46.52),(13.95,46.48),(14.25,46.44),(14.55,46.40),(14.75,46.47),(14.90,46.60),(15.05,46.65),(15.40,46.66),(15.65,46.70),(15.98,46.68),(16.05,46.84),(16.30,46.87),(16.42,46.73),(16.60,46.48),(16.38,46.52),(16.25,46.38),(15.90,46.27),(15.65,46.18),(15.60,46.00),(15.70,45.85),(15.40,45.68),(15.30,45.47),(14.95,45.48),(14.60,45.63),(14.40,45.48),(14.05,45.48),(13.60,45.47),(13.70,45.58),(13.90,45.65),(13.58,45.80),(13.60,45.98),(13.47,46.10),(13.48,46.22),(13.40,46.30),(13.70,46.40)]
CEN = {"Pomurska": (16.15, 46.66), "Podravska": (15.80, 46.45), "Koroška": (14.98, 46.57), "Savinjska": (15.36, 46.33),
       "Zasavska": (14.97, 46.07), "Posavska": (15.48, 45.98), "Jugovzhodna Slovenija": (15.10, 45.73), "Osrednjeslovenska": (14.58, 45.98),
       "Gorenjska": (14.18, 46.33), "Primorsko-notranjska": (14.28, 45.66), "Goriška": (13.75, 46.10), "Obalno-kraška": (13.85, 45.58)}
SHORT = {"Jugovzhodna Slovenija": "Jugovzhodna", "Primorsko-notranjska": "Primorsko-notr.", "Osrednjeslovenska": "Osrednjeslovenska"}


def P(lon, lat):
    return ((lon - 13.3) * 0.695 * 300, (46.95 - lat) * 300)


def _smooth(points):
    n = len(points); d = []
    for i in range(n):
        p0, p1, p2, p3 = points[i - 1], points[i], points[(i + 1) % n], points[(i + 2) % n]
        if i == 0:
            d.append(f"M{p1[0]:.1f} {p1[1]:.1f}")
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d.append(f"C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]:.1f} {p2[1]:.1f}")
    return "".join(d) + "Z"


def regions_map(regions, caption=""):
    mx = max(n for _, n in regions) or 1
    outline = _smooth([P(*p) for p in OUT])
    dots = []
    for r, n in regions:
        x, y = P(*CEN[r])
        rad = 9 + (n / mx) ** 0.5 * 34 if n else 9
        lab = SHORT.get(r, r)
        if n:
            dots.append(f'<g class="rm-dot"><title>{e(r)}: {n}</title><circle cx="{x:.0f}" cy="{y:.0f}" r="{rad:.0f}" class="rm-c" style="--o:{0.35 + 0.65 * n / mx:.2f}"/>'
                        f'<text x="{x:.0f}" y="{y + 5:.0f}" class="rm-n">{n}</text><text x="{x:.0f}" y="{y + rad + 16:.0f}" class="rm-l">{e(lab)}</text></g>')
        else:
            dots.append(f'<g class="rm-dot"><title>{e(r)}: še ni izvajalca</title><circle cx="{x:.0f}" cy="{y:.0f}" r="{rad:.0f}" class="rm-c0"/>'
                        f'<text x="{x:.0f}" y="{y + rad + 16:.0f}" class="rm-l">{e(lab)}</text></g>')
    svg = (f'<svg class="rmap" viewBox="0 0 710 470" role="img" aria-label="Zemljevid Slovenije s številom organizacij po regijah">'
           f'<path d="{outline}" class="rm-land"/>{"".join(dots)}</svg>')
    lst = "".join(f'<li><span>{e(r)}</span><b class="tnum">{n if n else "–"}</b></li>' for r, n in regions)
    return f'<figure class="regions-map"><figcaption><b>Organizacije v raziskovalni bazi</b><span>{caption}</span></figcaption>{svg}<ol class="rm-list">{lst}</ol></figure>'
