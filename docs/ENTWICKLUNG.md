# Animepelago

Anime-Ratespiel mit Archipelago-Anbindung.

## Ordner

- `apworld/`   die Archipelago-Welt (Quellcode). Gebaut: `animepelago.apworld` + Vorlage `Animepelago.yaml` (kommen ins Release)
- `client/`    das Web-Spiel: `index.html`, `game_data.js` (nur IDs, Genres, verschleierte Titel, Namen als Pruefsumme;
               Cover, Studio, Folgen usw. holt der Client live von AniList), `Animepelago.yaml` (fuer den Download-Knopf)
               `party.html` (Party-Spiele, Online-Raeume ueber Firebase), `twitch_icon.svg`, `tmdb_logo.svg`
- `docs/`      diese Anleitung, `ERFOLGE.md` (alle Erfolge und Raenge), `PROFIL_FORMAT.md` (Profil-Sicherung),
               `FIREBASE_EINRICHTEN.md` + `firebase_rules.json` (Party-Datenbank), `IDEEN.md` (Fahrplan)
- `offline/`   **alles, was NICHT auf GitHub kommt** (steht in `.gitignore`)
  - `skripts/`               die Skripte zum Bauen der Datenbank
    - `fetch_anilist.py`     Anime von AniList holen (inkl. Staffel-Ketten)
    - `fetch_wikidata.py`    Titel in weiteren Sprachen von Wikidata (frei nutzbar)
    - `fetch_animethemes.py` Songs von AnimeThemes (fuer spaeter)
    - `franchise.py`         Regel, welche Staffeln/Filme zu einem Anime gehoeren
    - `review_specials.py`   listet OVAs/Specials in `specials_review.json` zum Entscheiden
    - `build.py`             baut die Spieldateien fuer Client und APWorld
    - `client_pack.py`       macht die Client-Datei klein und spoilerarm
    - `pack_apworld.py`      packt die APWorld und prueft, ob die YAML-Vorlage noch passt
  - `raw/`                   Rohdaten (AniList, Wikidata)
  - `output/`                komplette Datenbank zum Nachschauen
  - `corrections.json`       deine Handkorrekturen
  - `specials_review.json`   deine Entscheidungen zu OVAs/Specials/Filmen

## Taeglicher Gebrauch (Ordner `offline/skripts`)

- `anime_holen.bat`  fragt, wie viele weitere beliebte Anime geholt werden sollen, und baut danach alles neu
- `top_holen.bat`    holt die 100 bestbewerteten Anime (insgesamt und je Genre) fuer das Minispiel "Top 100" und baut neu
- `update.bat`       fragt alle gespeicherten Anime neu ab (Folgen, Beliebtheit, neue Staffeln, Zielgruppen) und baut neu
- `bauen.bat`        baut alles aus den gespeicherten Daten neu, ohne AniList zu fragen (inkl. Wikidata-Titel)
- `vorlage.bat`      erzeugt die YAML-Vorlage mit deinem Archipelago und kopiert sie nach `apworld/` und `client/`
                     (vorher die neue `.apworld` nach `custom_worlds` kopieren)
- danach `client/index.html` neu laden

`anime_holen.bat`, `top_holen.bat` und `update.bat` nie gleichzeitig laufen lassen. Welche Anime im Spiel sind, steht in `offline/raw/seeds.json`.

## Titelsprachen

Englisch, Romaji und Japanisch kommen von AniList. Deutsch, Spanisch, Franzoesisch, Italienisch und Portugiesisch
kommen von Wikidata (`fetch_wikidata.py`). Eine Sprache kommt ins Spiel, wenn mindestens 25 % der Anime einen eigenen
Titel darin haben (`TITLE_LANGUAGE_MIN` in `build.py`). Zum Raten zaehlen alle Namen, auch aus anderen Sprachen.

## Release

`apworld/animepelago.apworld` + `apworld/Animepelago.yaml` zusammen hochladen. Nach Aenderungen an den Optionen
die Vorlage mit `vorlage.bat` neu erzeugen (`bauen.bat` warnt, wenn sie veraltet ist).

## Regeln fuer die Datenbank

- Anime-Check = ein ganzer Anime mit allen Staffeln (Attack on Titan = 1 Check).
- Eigener Name = eigener Anime (Naruto, Naruto Shippuden, Boruto = 3 Checks).
- Filme gehoeren dazu, OVAs und Specials nur, wenn du sie in `specials_review.json` auf `true` setzt.
- Songs: jeder Song ein Check.
- Keine doppelten Abfragen: jede AniList-ID wird nur einmal geholt und gespeichert.

## APWorld (Archipelago 0.6.8)

- `apworld/animepelago.apworld` nach `C:\ProgramData\Archipelago\custom_worlds` kopieren
- `apworld/Animepelago.yaml` als Vorlage fuer die Spieler-YAML nehmen
- Die Anime werden aus den Top 500 gezogen (bei grossen Welten aus den Top "2 x anime_count"), siehe `pool_size_for` in `__init__.py`
- Jeder Anime ist ein Check, dazu "Guessed N Anime"-Meilensteine
- Freischalten (`unlock_mode`): nach Genres, nach Anfangsbuchstaben (A-Z und # fuer Zahlen/Zeichen) oder beides;
  der Buchstabe kommt aus dem englischen, Romaji- oder deutschen Titel (`title_language`), ein fuehrendes "The" zaehlt mit
- Nur bestimmte Genres (`only_genres: [Romance]`): nur Anime mit diesem Genre; dann gibt es keine Genre-Items, freigeschaltet wird
  ueber Buchstaben und/oder Jahr/Vorlage/Jahreszeit/Studio; Start-Items = die Items von N zufaelligen Anime (`only_genres_start_anime`, 2-8, Standard 3);
- Genre-Stufe (`genre_step`, Standard 6): bei "any" braucht ein Anime pro 6 Genres eins mehr (1-5 -> 1, 6-11 -> 2, 12+ -> 3);
  das zufaellige Startgenre kommt aus den selteneren Genres (sonst ist am Anfang zu viel offen);
- Zusatz-Kategorien (`unlock_by_year`, `unlock_by_source`, `unlock_by_season`, `unlock_by_studio`, je true/false):
  Jahr, Vorlage, Jahreszeit und Studio des ersten Teils. Feste Wertelisten in `offline/skripts/common.py` (nur hinten ergaenzen!);
- Zielgruppen (`include_demographics`, Standard an): Shounen, Shoujo, Seinen, Josei und Kids zaehlen als weitere Genres
  (Daten: AniList-Tags der Kategorie "Demographic"; nach dem Update einmal `update.bat` laufen lassen);
- Neu: Senzu-Bohne (alle Fallen weg, per Knopf), Time Leap (naechste Falle geht daneben), Fallen Isekai-Truck,
  Filler Arc und Tsundere, TrapLink (`trap_link`), Ziel Genre-Meister (`goal: genre_master`, 8 Genres x 5 Anime),
  Universal Tracker (interpret_slot_data + re_gen_passthrough), Tippfehler (ein Fehler wird verziehen), Sounds (abschaltbar);
- Stand Arrow (`stand_arrow_items`, Standard 10, max. 100): deckt bei einem Anime nach Wahl alle Infos auf;
- Kira's Hand sperrt ein Genre 60 Sekunden;
- Geass (`geass_items`, Standard 10, max. 50, hoechstens 10 % der Anime): ein Anime nach Wahl gilt als erraten;
- Items: ein Item pro Genre und pro Buchstabe, Sukuna's Finger (20), Dragon Ball (7), Kira's Hand (5, Falle), Death Note (1),
  Exodia-Teile (5; mit `goal: exodia` das Ziel, sonst Filler), Filler Episode
- Nach jedem `build.py` wird die APWorld mit `pack_apworld.py` neu gepackt (passiert in den .bat-Dateien automatisch)
