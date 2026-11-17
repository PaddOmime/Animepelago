"""Laedt die Anime-Liste, die offline/skripts/build.py erzeugt (anime_data.json)."""

import json
import pkgutil

_raw = json.loads(pkgutil.get_data(__name__.rsplit(".", 1)[0], "anime_data.json").decode("utf-8"))

DATA_VERSION: int = _raw["version"]
# Jeder Eintrag: {"id": AniList-ID, "name": eindeutiger Name, "genres": [...], "popularity": int}
ANIME: list[dict] = _raw["anime"]
ANIME_BY_ID: dict[int, dict] = {a["id"]: a for a in ANIME}

# Die Genres von AniList (ohne "Hentai"). Feste Reihenfolge, denn sie bestimmt die Item-IDs.
GENRES: list[str] = [
    "Action", "Adventure", "Comedy", "Drama", "Ecchi", "Fantasy", "Horror", "Mahou Shoujo", "Mecha",
    "Music", "Mystery", "Psychological", "Romance", "Sci-Fi", "Slice of Life", "Sports", "Supernatural",
    "Thriller",
]
# Zielgruppen (Shounen, Shoujo ...). Zaehlen als zusaetzliche Genres, wenn "Include Demographics" an ist.
# Hinten angehaengt, damit die Item-IDs der normalen Genres gleich bleiben.
DEMOGRAPHICS: list[str] = ["Shounen", "Shoujo", "Seinen", "Josei", "Kids"]
GENRES += DEMOGRAPHICS

# Anfangsbuchstaben: A-Z und "#" fuer Titel, die mit einer Zahl oder einem Zeichen beginnen.
# Feste Reihenfolge, denn sie bestimmt die Item-IDs.
LETTERS: list[str] = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + ["#"]

# Zusatz-Kategorien (extra_unlocks): feste Wertelisten aus offline/skripts/common.py (bestimmen die Item-IDs).
# Jeder Anime hat dazu "cat": {"year": ..., "source": ..., "season": ..., "studio": ...} (None = unbekannt).
# Titelsprachen, die die 25-%-Regel geschafft haben (build.py). Bestimmen die Auswahl bei title_language.
TITLE_LANGUAGES: list[str] = _raw.get("title_languages", ["english", "romaji", "japanese", "german", "spanish", "french"])

CATEGORIES: dict[str, list[str]] = _raw.get("categories", {"year": [], "source": [], "season": [], "studio": []})

# Hat die Datenbank schon Zielgruppen bzw. Werte fuer die Zusatz-Kategorien? (aeltere Datenbanken nicht)
# Fehlt etwas, schaltet __init__.py die passende Option mit einer Warnung ab, statt eine kaputte Welt zu bauen.
HAS_DEMOGRAPHICS: bool = any(a.get("demographics") for a in ANIME)
HAS_CATEGORY: dict[str, bool] = {c: bool(CATEGORIES.get(c)) and any((a.get("cat") or {}).get(c) for a in ANIME)
                                 for c in ("year", "source", "season", "studio")}
