from BaseClasses import Location

from .data import ANIME, BIG3, CHARACTER_TIERS, character_total
from .Items import GAME

# Location-ID = Offset + AniList-ID. So bleibt jede ID bei jedem Datenbank-Update gleich,
# und der Client kann sie ohne Tabelle ausrechnen.
LOCATION_ID_OFFSET = 7_418_000_000
MILESTONE_ID_OFFSET = 7_419_000_000

# "Guessed N Anime": zusaetzliche Checks fuer eine bestimmte Anzahl erratener Anime.
MILESTONES = [1, 2, 3, 5, 10, 15, 20, 25, 30, 40, 50, 75, 100, 150, 200, 250, 300, 400, 500, 600, 700, 800, 900, 1000]


def milestone_name(n: int) -> str:
    return f"Guessed {n} Anime"


# Waifupelago: "<Anime> - Character N". ID = Offset + AniList-ID * Block + N (fest, auch nach Updates gleich)
CHARACTER_ID_OFFSET = 8_000_000_000
CHARACTER_BLOCK = 10_000


def character_location(anime_name: str, n: int) -> str:
    return f"{anime_name} - Character {n}"


# Sicherheitsnetz: AniList-IDs ab 1 000 000 wuerden in den Bereich der Meilensteine rutschen
assert all(0 < a["id"] < MILESTONE_ID_OFFSET - LOCATION_ID_OFFSET for a in ANIME), "AniList-ID zu gross"

location_name_to_id: dict[str, int] = {a["name"]: LOCATION_ID_OFFSET + a["id"] for a in ANIME}
for _n in MILESTONES:
    location_name_to_id[milestone_name(_n)] = MILESTONE_ID_OFFSET + _n

assert all(character_total(a) < CHARACTER_BLOCK for a in CHARACTER_TIERS), "Zu viele Figuren fuer einen Anime"
_char_names: set[str] = set()
for _a in ANIME:
    for _n in range(1, character_total(_a["id"]) + 1):
        _name = character_location(_a["name"], _n)
        location_name_to_id[_name] = CHARACTER_ID_OFFSET + _a["id"] * CHARACTER_BLOCK + _n
        _char_names.add(_name)

# Ziel "Big 3 + Daddy": die vier Helden bzw. Heldinnen als eigene Orte
BOSS_ID_OFFSET = 7_419_500_000


def boss_location(name: str) -> str:
    return f"Boss: {name}"


BOSS_NAMES = [n for _, hero, heroine in BIG3 for n in (hero, heroine)]
for _i, _n in enumerate(BOSS_NAMES):
    location_name_to_id[boss_location(_n)] = BOSS_ID_OFFSET + _i

location_name_groups: dict[str, set[str]] = {
    "Bosses": {boss_location(n) for n in BOSS_NAMES},
    "Characters": _char_names,
    "Anime": {a["name"] for a in ANIME},
    "Milestones": {milestone_name(n) for n in MILESTONES},
}


class AnimepelagoLocation(Location):
    game = GAME
