# Animepelago

## Was ist das für ein Spiel?

Animepelago ist ein Anime-Ratespiel. Jeder Anime in deiner Welt ist ein Check: Tippe seinen Titel im
[Animepelago-Webclient](https://paddomime.github.io/Animepelago/client/) ein, um den Check zu senden. Jeder bekannte
Titel zählt – Englisch, Romaji, Japanisch, Deutsch, Spanisch, Französisch oder Italienisch –, und kleine Tippfehler
werden verziehen.

Du kannst nicht jeden Anime sofort raten. Ein Anime wird erst ratbar, wenn du die nötigen Items hast:
seine Genres, den Anfangsbuchstaben seines Titels oder beides – und auf Wunsch Jahr, Vorlage, Jahreszeit und Studio.
Diese Items sind in der Multiworld verteilt: Deine Mitspieler schalten deine Anime frei und du ihre Sachen.

Die Anime kommen von [AniList](https://anilist.co) (rund 1.900 der bekanntesten Serien und Filme). Cover, Studios,
Folgen und zugehörige Staffeln lädt der Client beim Spielen live von AniList.

## Was macht der Randomizer?

Die Anime deiner Welt werden zufällig ausgewählt (bekannte bevorzugt), und die Freischalt-Items – Genres,
Buchstaben, Jahre, Vorlagen, Jahreszeiten, Studios – werden in die Multiworld gemischt. Jeder Anime ist eine
Location (z. B. „Attack on Titan“), dazu kommen Meilensteine wie „Guessed 10 Anime“.

Eine ganze Reihe zählt als ein Anime: Alle Staffeln und Filme von *Attack on Titan* sind ein Check, und du darfst
ihn mit dem Namen jedes Teils raten.

## Welche Items gibt es?

**Freischalt-Items** (Progression):
- **Genre: …** – z. B. *Genre: Romance*. Mit `include_demographics` zählt die Zielgruppe als zusätzliches Genre
  (*Genre: Shounen*, *Shoujo*, *Seinen*, *Josei*, *Kids*) – nur mit `genre_rule: any`.
- **Letter: …** – der Anfangsbuchstabe des Titels in deiner `title_language` (*Letter: A* … *Letter: Z*,
  *Letter: #* für Zahlen und Zeichen). Ein „The“ am Anfang zählt nicht: *The Promised Neverland* ist ein **P**-Anime.
- **Year: …**, **Source: …**, **Season: …**, **Studio: …** – nur mit `unlock_by_year`, `unlock_by_source`,
  `unlock_by_season` oder `unlock_by_studio`. Jahre vor 2010 gibt es als Zeiträume (*Year: 2005-2009*,
  *Year: Before 2000*), kleinere Studios teilen sich *Studio: Other*.

**Hilfen** (`perk_items`, standardmäßig an):
- **Sukuna's Finger** – verrät einen Hinweis zu einem Anime. Mit allen Fingern: **Domain Expansion**, ein Anime
  deiner Wahl zählt als erraten.
- **Dragon Ball** – mit allen 7 darfst du dir ein Genre wünschen.
- **Senzu Bean** – beendet alle laufenden Fallen. **Time Leap** – die nächste Falle geht daneben.
- **Stand Arrow** (`stand_arrow_items`) – zeigt alles über einen Anime (Jahr, Studio, Folgen, Format, Vorlage,
  Jahreszeit und ein verschwommenes Cover).
- **Geass** (`geass_items`, höchstens 10 % deiner Anime) – wähle einen beliebigen Anime, auch einen gesperrten:
  Er zählt sofort als erraten.

**Fallen** (`trap_items`, standardmäßig an):
- **Kira's Hand** – sperrt ein zufälliges Genre (oder einen Buchstaben) für 60 Sekunden. Nie dein letztes freies.
- **Isekai Truck** – mischt die Anime-Kacheln für 60 Sekunden.
- **Filler Arc** – blendet alle Hinweise und Infos für 60 Sekunden aus.
- **Tsundere** – 30 Sekunden lang wird jede richtige Antwort einmal abgelehnt („B-baka!“) – einfach nochmal.
- **Death Note** – harmloser Füller, mit `death_link` sendet er aber einen DeathLink.
- Mit `trap_link` werden Fallen mit anderen TrapLink-Spielen getauscht.

**Füller:** *Filler Episode*, sammelbare *Clow Cards* und viele Spaß-Items ohne Wirkung
(*AYAYA!*, *Straw Hat*, *Omae wa mou shindeiru* …).

**Exodia:** Mit `goal: exodia` liegen die fünf Teile von *Exodia the Forbidden One* im Pool.

## Was ist das Ziel?

Je nach `goal`:
- **anime** (Standard): Errate so viele Anime wie in `anime_goal` eingestellt.
- **exodia**: Sammle alle 5 Exodia-Teile.
- **genre_master**: Errate `genre_master_anime` Anime in `genre_master_genres` verschiedenen Genres.

## Wichtige Optionen

| Option | Bedeutung |
|---|---|
| `anime_count` | Wie viele Anime (Checks) in deiner Welt sind. |
| `unlock_mode` | `genres`, `letters` oder `both` (Standard) – was ein Anime braucht, bevor du ihn raten darfst. |
| `genre_rule` | `any`: eines seiner Genres reicht (mit `genre_step` brauchen lange Genre-Listen mehr). `all`: alle Genres. |
| `starting_genre` | Mit welchem Genre du startest, `auto` (Standard: ein selteneres Genre mit genug Anime) oder `random`. |
| `only_genres` | Nur Anime bestimmter Genres, z. B. `[Romance]`. Dann gibt es keine Genre-Items; du startest mit den Items einiger Anime (`only_genres_start_anime`). |
| `title_language` | Bestimmt die Buchstaben und in welcher Sprache der Client die Titel zeigt. |
| `unlock_by_year` / `_source` / `_season` / `_studio` | Zusätzliche Freischalt-Items. |

Alle Optionen mit Erklärung stehen in der YAML-Vorlage (Download-Knopf im Client) und im Options Creator.

## Wie sehen Items anderer Spieler in Animepelago aus?

Items für andere Spieler stecken hinter deinen Anime: Errätst du einen Anime richtig, wird sein Check gesendet und
das Item geht an den, dem es gehört.

## Was passiert, wenn ich ein Item bekomme?

Der Client zeigt eine Meldung, neu ratbare Anime leuchten auf, Hilfen werden nutzbar. Fallen wirken sofort.

## Extras im Client

- **Offline-Modus und Minispiele** (Galgenmännchen, Wortsalat, Animedle mit Tagesrätsel, Anime-Bingo, Top 100) – ohne Server.
- **Profile, Routen und Erfolge**: Archipelago-Spiele zählen als Spieltage; mit gewählter Route geben sie auch EP.
- **Twitch-Integration**: Dein Chat rät mit (nur lesend, ohne Login). Sprecht in eurer Multiworld ab,
  ob Chat-Hilfe okay ist.
- **Automatisches Neu-Verbinden**, wenn die Verbindung abbricht; dabei geht nichts verloren.
