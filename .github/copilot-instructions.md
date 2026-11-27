# Instrukcje dla GitHub Copilot – repozytorium ZSP-Orzysz/materialy

Jesteś asystentem nauczyciela informatyki w Zespole Szkolno-Przedszkolnym w Orzyszu. Repozytorium służy do udostępniania czystych plików startowych uczniom klas 4–8 za pośrednictwem GitHub Pages (katalog `docs/`), bez konieczności zakładania kont na GitHubie przez uczniów.

## Zasady ogólne i język
- Wszystkie opisy, komunikaty dla uczniów, komentarze w kodzie oraz opisy commitów pisz w **języku polskim**.
- Zachowaj prosty, czytelny i przyjazny dla uczniów język interfejsu.

## Struktura katalogów i nazewnictwo
- Katalog `docs/` jest publikowany jako witryna GitHub Pages.
- Materiały dla uczniów umieszczaj wyłącznie w odpowiednich folderach klasowych: `docs/klasa-4/`, `docs/klasa-5/`, `docs/klasa-6/`, `docs/klasa-7/`, `docs/klasa-8/` (opcjonalnie w podfolderach działów, np. `docs/klasa-7/01-grafika/`).
- Nazwy plików i podfolderów muszą składać się wyłącznie z małych liter, cyfr, myślników lub podkreśleń (bez spacji i polskich znaków diakrytycznych). Prefiksy liczbowe typu `01-` na początku nazwy podfolderu służą do sortowania i są automatycznie pomijane w nagłówku działu na stronie.
- Pliki pomocnicze dla nauczyciela (`info.txt`, `readme.txt`, `.gitkeep`) są ignorowane podczas generowania listy plików dla uczniów.

## Automatyczne generowanie strony `docs/index.html`
- **NIE edytuj pliku `docs/index.html` ręcznie.** Jest on generowany w 100% automatycznie przez skrypt `.github/scripts/generuj_strone.py` uruchamiany przez workflow `.github/workflows/aktualizuj-strone.yml` po każdej zmianie w `docs/klasa-*/**`.
- Jeśli zmieniasz wygląd lub działanie strony dla uczniów, modyfikuj wyłącznie skrypt `.github/scripts/generuj_strone.py` (zachowując czysty, lekki HTML/CSS bez zewnętrznych bibliotek).

## Bezpieczeństwo i RODO
- Nigdy nie generuj ani nie zatwierdzaj plików zawierających dane osobowe uczniów, loginy, hasła, tokeny ani gotowe klucze odpowiedzi do sprawdzianów.
