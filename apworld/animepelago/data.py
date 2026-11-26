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
# Nur die echten Genres (ohne Zielgruppen), z. B. fuer die Figuren-Items "Characters: <Genre>"
BASE_GENRES: list[str] = [g for g in GENRES if g not in DEMOGRAPHICS]

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

# Waifupelago: je Anime die Zahl der Figuren pro Seltenheitsstufe [selten, mittel, bekannt].
# Erzeugt von offline/skripts/build_characters.py (nur Figuren, die ein Bild haben koennen). Fehlt die Datei: keine Figuren.
try:
    _chars = json.loads(pkgutil.get_data(__name__.rsplit(".", 1)[0], "characters_data.json").decode("utf-8"))
except (OSError, ValueError, TypeError):
    _chars = {"version": 0, "tiers": {}}
CHARACTER_DATA_VERSION: int = _chars.get("version", 0)
# Je Anime und Geschlecht ("f", "m", "nb", "o" = ohne Angabe): [selten, mittel, bekannt]. Version 1 kannte kein Geschlecht.
CHARACTER_TIERS: dict[int, dict[str, list[int]]] = {
    int(k): (v if isinstance(v, dict) else {"o": v}) for k, v in _chars.get("tiers", {}).items() if int(k) in ANIME_BY_ID}


def character_total(aid: int) -> int:
    """Alle Figuren eines Anime (alle Geschlechter): so viele Figuren-Orte gibt es hoechstens."""
    return sum(sum(t) for t in CHARACTER_TIERS.get(aid, {}).values())


# Ziel "Big 3 + Daddy": Anime-ID, Held, Heldin (Love Interest). Reihenfolge = feste IDs der Boss-Orte.
BIG3 = [(223, "Goku", "Chi-Chi"), (21, "Monkey D. Luffy", "Boa Hancock"),
        (20, "Naruto Uzumaki", "Hinata Hyūga"), (269, "Ichigo Kurosaki", "Orihime Inoue")]
