import os
import re
import html

KLASY = [
    ("klasa-4", "Klasa 4"),
    ("klasa-5", "Klasa 5"),
    ("klasa-6", "Klasa 6"),
    ("klasa-7", "Klasa 7"),
    ("klasa-8", "Klasa 8"),
]
IGNOROWANE = {"info.txt", "readme.txt", ".gitkeep"}


def ladna_nazwa(nazwa):
    czysta = re.sub(r"^\d+[-_]\s*", "", nazwa)
    czysta = czysta.replace("-", " ").replace("_", " ").strip()
    return czysta.capitalize() if czysta else nazwa


def wczytaj_info(folder_path):
    """Zwraca krótki tekst z info.txt (jeśli istnieje i nie jest pusty), lub None."""
    info_path = os.path.join(folder_path, "info.txt")
    if not os.path.isfile(info_path):
        return None
    try:
        with open(info_path, "r", encoding="utf-8") as f:
            linie = [linia.strip() for linia in f if linia.strip()]
        if not linie:
            return None
        return " ".join(linie)
    except OSError:
        return None


def wiersz(url, nazwa):
    ext = os.path.splitext(nazwa)[1].lower()
    etykieta = f"Pobierz {ext}" if ext else "Pobierz"
    return (
        f'        <li><span><code>{html.escape(nazwa)}</code></span>'
        f'<a class="btn" href="{html.escape(url)}" download>{etykieta}</a></li>'
    )


def main():
    sekcje = []
    for folder, tytul in KLASY:
        sciezka_klasy = os.path.join("docs", folder)
        luzem = []
        dzialy = []

        if os.path.isdir(sciezka_klasy):
            for wpis in sorted(os.listdir(sciezka_klasy)):
                pelna = os.path.join(sciezka_klasy, wpis)
                if os.path.isfile(pelna) and wpis.lower() not in IGNOROWANE and not wpis.startswith("."):
                    luzem.append(wpis)
                elif os.path.isdir(pelna) and not wpis.startswith("."):
                    pliki = [
                        f for f in sorted(os.listdir(pelna))
                        if os.path.isfile(os.path.join(pelna, f))
                        and f.lower() not in IGNOROWANE
                        and not f.startswith(".")
                    ]
                    opis_dzialu = wczytaj_info(pelna)
                    if pliki or opis_dzialu:
                        dzialy.append((wpis, pliki, opis_dzialu))

        bloki = []
        opis_klasy = wczytaj_info(sciezka_klasy)
        if opis_klasy:
            bloki.append(f'    <p class="opis-info">{html.escape(opis_klasy)}</p>')

        if luzem:
            bloki.append("    <ul>\n" + "\n".join(wiersz(f"{folder}/{x}", x) for x in luzem) + "\n    </ul>")

        for dz, pliki, opis_dzialu in dzialy:
            licznik = f" ({len(pliki)})" if pliki else ""
            opis_html = f'\n      <p class="opis-info">{html.escape(opis_dzialu)}</p>' if opis_dzialu else ""
            lista_html = (
                "\n      <ul>\n" + "\n".join(f"  {wiersz(f'{folder}/{dz}/{x}', x)}" for x in pliki) + "\n      </ul>"
                if pliki
                else ""
            )
            bloki.append(
                f'    <details open><summary>{html.escape(ladna_nazwa(dz))}{licznik}</summary>{opis_html}{lista_html}\n    </details>'
            )

        if not bloki:
            bloki.append('    <ul><li class="brak">Brak aktualnych plików do pobrania.</li></ul>')

        sekcje.append(f'  <section class="klasa"><h2>{tytul}</h2>\n' + "\n".join(bloki) + "\n  </section>")

    naglowek = """<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Materiały na informatykę – ZSP Orzysz</title>
  <style>
    body { font-family: system-ui, sans-serif; max-width: 840px; margin: 2rem auto; padding: 0 1rem; line-height: 1.5; color: #1e293b; }
    h1 { color: #0f172a; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem; }
    .klasa { background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1rem 1.25rem; margin-bottom: 1.25rem; }
    .klasa h2 { margin-top: 0; margin-bottom: 0.75rem; font-size: 1.2rem; color: #0369a1; }
    .opis-info { margin: 0.35rem 0 0.65rem 0; font-size: 0.95rem; color: #334155; background: #f1f5f9; padding: 0.45rem 0.7rem; border-left: 3px solid #0284c7; border-radius: 4px; }
    details { background: #fff; border: 1px solid #e2e8f0; border-radius: 6px; padding: 0.5rem 0.9rem; margin-bottom: 0.65rem; }
    details:last-child { margin-bottom: 0; }
    summary { font-weight: 600; color: #334155; cursor: pointer; padding: 0.25rem 0; }
    summary:hover { color: #0284c7; }
    ul { list-style: none; padding: 0; margin: 0.4rem 0 0 0; }
    li { display: flex; justify-content: space-between; align-items: center; padding: 0.45rem 0; border-bottom: 1px solid #f1f5f9; }
    li:last-child { border-bottom: none; }
    a.btn { background: #0284c7; color: #fff; text-decoration: none; padding: 0.35rem 0.85rem; border-radius: 6px; font-weight: 600; font-size: 0.9rem; }
    a.btn:hover { background: #0369a1; }
    .brak { color: #64748b; font-size: 0.9rem; font-style: italic; }
  </style>
</head>
<body>
  <h1>Pliki startowe na lekcje informatyki</h1>
  <p>Wybierz swoją klasę oraz dział, a następnie kliknij <strong>Pobierz</strong> przy zadaniu.</p>
"""
    stopka = "\n</body>\n</html>\n"
    strona = naglowek + "\n".join(sekcje) + stopka

    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(strona)


if __name__ == "__main__":
    main()
