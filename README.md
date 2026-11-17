# Animepelago

**An anime guessing game for the [Archipelago](https://archipelago.gg) multiworld randomizer.**

Guess anime to send checks to your friends. Their games send you genres, letters and perks that unlock more anime to guess.

### ▶ [Play now in your browser](https://paddomime.github.io/Animepelago/client/)
Archipelago mode, offline mode and mini games (Hangman, Anime Bingo). No install needed.

> 🇩🇪 Deutsche Anleitung: siehe [unten](#deutsch)

**Status:** beta. Things may still change between versions.

---

## How it works

- Your world contains a number of anime (you choose how many). Each anime you guess is a **check**.
- You may only guess an anime once it is **unlocked**:
  - **Genres:** you need one of its genres (or all of them, if you choose so). Optionally the target audience counts as a genre too (Shounen, Shoujo, Seinen, Josei, Kids).
  - **Letters:** you need the first letter of its title (A–Z, or `#` for numbers and symbols).
  - **Both:** genres and letter.
  - **Optional extras** (each can be switched on): the release **year** of the first part, its **source** (Manga, Light Novel …), the **season** it first aired and its **studio**. Every extra makes the game harder.
- Every known title in any language counts as a correct guess: *Attack on Titan*, *Shingeki no Kyojin* and *L'Attaque des Titans* all work. One typo is forgiven.
- Milestones ("Guessed 10 Anime", …) are extra checks.

### Items

| Item | What it does |
|---|---|
| Genre: … / Letter: … | Unlocks anime |
| Year: … / Source: … / Season: … / Studio: … | Unlocks anime (only with the matching option) |
| Sukuna's Finger | Reveals a hint about an anime. Collect all of them for **Domain Expansion**: one anime of your choice counts as guessed |
| Dragon Ball | Collect all 7 and wish for any genre |
| Geass | Pick any anime, even a locked one; it counts as guessed |
| Senzu Bean | Use it to end all running trap effects |
| Time Leap | The next trap that hits you misses |
| Stand Arrow | Reveals all information about an anime of your choice (year, studio, episodes, format, source, season, blurred cover) |
| Kira's Hand *(trap)* | Locks one of your genres for 60 seconds (a letter if genres don't count in your world). Never your last free one: then it waits until you have a second |
| Isekai Truck *(trap)* | Shuffles the anime fields for 60 seconds (the numbers stay) |
| Filler Arc *(trap)* | Hides all hints and info for 60 seconds |
| Tsundere *(trap)* | For 30 seconds every correct answer is refused once – just try again |
| Death Note | Filler, or a DeathLink trap when DeathLink is on |
| Exodia pieces | Collect all 5 to win (with the Exodia goal) |

## Playing

1. Download `animepelago.apworld` from the [Releases](../../releases) and double-click it (or put it into `custom_worlds` in your Archipelago folder).
2. Create your player YAML: in the Archipelago Launcher use **Generate Template Options**, or start from `Animepelago.yaml` in the release.
3. Generate and host the game as usual.
4. Open the **web client**: **[https://paddomime.github.io/Animepelago/client/](https://paddomime.github.io/Animepelago/client/)**. Enter server, port, your slot name and the password (if any), and start guessing.

### Offline mode

No Archipelago server at hand? Open the web client, choose **Offline**, pick your settings and play alone. Every guessed anime gives you an item from the same pool, and your progress is saved in your browser. There is also **🪢 Hangman**: guess the title letter by letter, every mistake reveals a clue.

### Tracker

Animepelago works with the **Universal Tracker**: it shows which anime are in logic.

### Options

| Option | Meaning |
|---|---|
| `goal` | `anime` (guess a number of anime), `exodia` (collect 5 Exodia pieces) or `genre_master` (master several genres) |
| `genre_master_genres` / `genre_master_anime` | With `genre_master`: in how many genres (default 8) you need how many guessed anime (default 5) |
| `anime_count` | How many anime are checks in your world |
| `only_genres` | Play only with anime of these genres, e.g. `[Romance]` or `[Shounen]`. Genres then unlock nothing; you play with letters and/or the year/source/season/studio options. You start with the items of a few random anime |
| `only_genres_start_anime` | With `only_genres`: how many anime you can guess right from the start (2–8). You get the items of that many random anime |
| `anime_goal` | How many anime you must guess to win |
| `unlock_mode` | `genres`, `letters` or `both` |
| `unlock_by_year` | Also need "Year: 2013" (before 2010 in ranges like "Year: 2005-2009") |
| `unlock_by_source` | Also need "Source: Manga", "Source: Light Novel", … |
| `unlock_by_season` | Also need "Season: Spring", … |
| `unlock_by_studio` | Also need "Studio: MADHOUSE" (smaller studios share "Studio: Other") |
| `title_language` | english, romaji, german, spanish, french or japanese: shown titles and first letters |
| `genre_rule` | `any` genre of an anime unlocks it, or `all` its genres are needed |
| `genre_step` | With `any`: for every N genres an anime has, it needs one more (6: 1–5 genres → 1, 6–11 → 2, 12+ → 3). 0 = off |
| `include_demographics` | Shounen, Shoujo, Seinen, Josei and Kids count as genres (only with `genre_rule: any`) |
| `starting_genre` | Your first genre, or `random` |
| `perk_items` | Sukuna's Fingers, Dragon Balls, Senzu Beans and Time Leaps |
| `geass_items` | Number of Geass (0–50, at most 10% of your anime) |
| `stand_arrow_items` | Number of Stand Arrows (0–100) |
| `trap_items` | Kira's Hand, Isekai Truck, Filler Arc and Tsundere |
| `death_link` | DeathLink |
| `trap_link` | TrapLink: trade traps with other TrapLink games |

## Data and privacy

The game files contain only a small list of anime (AniList IDs, titles, genres and popularity).
Covers, studios, episode counts and related entries are loaded **live from AniList** in your browser while you play and cached there. The client sends nothing anywhere except to your Archipelago server and the AniList API.

## Credits

See [CREDITS.md](CREDITS.md). Animepelago is a free fan project. It is **not affiliated with** AniList, Archipelago or any anime studio or publisher. All anime titles, images and other media belong to their respective owners.

## License

The code is licensed under the [MIT License](LICENSE). Data from third parties keeps its own license, see [CREDITS.md](CREDITS.md).

---

## Deutsch

**Ein Anime-Ratespiel für den Multiworld-Randomizer [Archipelago](https://archipelago.gg).**

Errate Anime, um Checks an deine Mitspieler zu schicken. Ihre Spiele schicken dir Genres, Buchstaben und Perks, die weitere Anime freischalten.

### ▶ [Jetzt im Browser spielen](https://paddomime.github.io/Animepelago/client/)
Archipelago-Modus, Offline-Modus und Minispiele (Galgenmännchen, Anime-Bingo). Keine Installation nötig.

### So funktioniert es

- In deiner Welt sind eine Menge Anime, wie viele, legst du selbst fest. Jeder erratene Anime ist ein **Check**.
- Raten darfst du einen Anime erst, wenn er **freigeschaltet** ist:
  - **Genres:** eines seiner Genres, oder alle, je nach Einstellung. Auf Wunsch zählt auch die Zielgruppe als Genre (Shounen, Shoujo, Seinen, Josei, Kids).
  - **Buchstaben:** der Anfangsbuchstabe des Titels (A–Z, `#` für Zahlen und Zeichen).
  - **Beides:** Genres und Buchstabe.
  - **Optionale Extras** (einzeln zuschaltbar): das **Jahr** des ersten Teils, die **Vorlage** (Manga, Light Novel …), die **Jahreszeit** der Erstausstrahlung und das **Studio**. Jedes Extra macht das Spiel schwerer.
- Jeder bekannte Titel in jeder Sprache zählt: *Attack on Titan*, *Shingeki no Kyojin* oder *L'Attaque des Titans*.
- Meilensteine („Guessed 10 Anime“ …) sind zusätzliche Checks.

### Spielen

1. `animepelago.apworld` aus den [Releases](../../releases) herunterladen und doppelt anklicken (oder in den Ordner `custom_worlds` deiner Archipelago-Installation legen).
2. Die Spieler-YAML erstellen: im Archipelago-Launcher über **Generate Template Options**, oder mit `Animepelago.yaml` aus dem Release.
3. Das Spiel wie gewohnt erstellen und hosten.
4. Den **Web-Client** öffnen: **[https://paddomime.github.io/Animepelago/client/](https://paddomime.github.io/Animepelago/client/)**. Server, Port, Spielername und gegebenenfalls Passwort eingeben und losraten.

**Offline-Modus:** Kein Archipelago-Server zur Hand? Im Web-Client **Offline** wählen, Einstellungen festlegen und allein spielen. Jeder erratene Anime gibt ein Item aus demselben Pool, der Spielstand wird im Browser gespeichert.

Die Items und Optionen sind oben in der englischen Tabelle erklärt.

### Daten

Mitgeliefert wird nur eine kleine Liste: AniList-IDs, Titel, Genres und Beliebtheit. Cover, Studios, Folgen und Teile lädt der Client **live von AniList** und speichert sie in deinem Browser. Der Client schickt nichts woandershin als an deinen Archipelago-Server und an AniList.

### Hinweis

Animepelago ist ein kostenloses Fanprojekt und **nicht verbunden mit** AniList, Archipelago oder Anime-Studios und -Verlagen. Alle Titel, Bilder und Medien gehören den jeweiligen Rechteinhabern. Quellen und Lizenzen: [CREDITS.md](CREDITS.md).
