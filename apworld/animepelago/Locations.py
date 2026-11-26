from BaseClasses import Location

from .data import ANIME, CHARACTER_TIERS
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

assert all(sum(t) < CHARACTER_BLOCK for t in CHARACTER_TIERS.values()), "Zu viele Figuren fuer einen Anime"
_char_names: set[str] = set()
for _a in ANIME:
    for _n in range(1, sum(CHARACTER_TIERS.get(_a["id"], ())) + 1):
        _name = character_location(_a["name"], _n)
        location_name_to_id[_name] = CHARACTER_ID_OFFSET + _a["id"] * CHARACTER_BLOCK + _n
        _char_names.add(_name)

location_name_groups: dict[str, set[str]] = {
    "Characters": _char_names,
    "Anime": {a["name"] for a in ANIME},
    "Milestones": {milestone_name(n) for n in MILESTONES},
}


class AnimepelagoLocation(Location):
    game = GAME
