from BaseClasses import Location

from .data import ANIME
from .Items import GAME

# Location-ID = Offset + AniList-ID. So bleibt jede ID bei jedem Datenbank-Update gleich,
# und der Client kann sie ohne Tabelle ausrechnen.
LOCATION_ID_OFFSET = 7_418_000_000
MILESTONE_ID_OFFSET = 7_419_000_000

# "Guessed N Anime": zusaetzliche Checks fuer eine bestimmte Anzahl erratener Anime.
MILESTONES = [1, 2, 3, 5, 10, 15, 20, 25, 30, 40, 50, 75, 100, 150, 200, 250, 300, 400, 500, 600, 700, 800, 900, 1000]


def milestone_name(n: int) -> str:
    return f"Guessed {n} Anime"


# Sicherheitsnetz: AniList-IDs ab 1 000 000 wuerden in den Bereich der Meilensteine rutschen
assert all(0 < a["id"] < MILESTONE_ID_OFFSET - LOCATION_ID_OFFSET for a in ANIME), "AniList-ID zu gross"

location_name_to_id: dict[str, int] = {a["name"]: LOCATION_ID_OFFSET + a["id"] for a in ANIME}
for _n in MILESTONES:
    location_name_to_id[milestone_name(_n)] = MILESTONE_ID_OFFSET + _n

location_name_groups: dict[str, set[str]] = {
    "Anime": {a["name"] for a in ANIME},
    "Milestones": {milestone_name(n) for n in MILESTONES},
}


class AnimepelagoLocation(Location):
    game = GAME
