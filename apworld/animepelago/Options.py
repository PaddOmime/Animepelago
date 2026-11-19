from dataclasses import dataclass

from Options import Choice, DeathLink, DefaultOnToggle, OptionGroup, OptionSet, PerGameCommonOptions, Range, Toggle

from .data import ANIME, GENRES, TITLE_LANGUAGES


class Goal(Choice):
    """What you need to win.
    anime: guess the number of anime set in Anime Goal.
    exodia: collect all 5 pieces of Exodia. The pieces become progression items spread across the multiworld.
    genre_master: guess enough anime in enough genres (see Genre Master Genres and Genre Master Anime)."""
    display_name = "Goal"
    option_anime = 0
    option_exodia = 1
    option_genre_master = 2
    default = 0


class GenreMasterGenres(Range):
    """Only with Goal: genre_master. In how many different genres you must master anime.
    Lowered automatically if your anime do not have enough genres."""
    display_name = "Genre Master Genres"
    range_start = 1
    range_end = 18
    default = 8


class GenreMasterAnime(Range):
    """Only with Goal: genre_master. How many guessed anime a genre needs to count as mastered."""
    display_name = "Genre Master Anime"
    range_start = 1
    range_end = 30
    default = 5


class AnimeCount(Range):
    """How many anime are in your game as checks. They are picked at random, preferring well-known anime
    (from the 500 most popular, or from the top "2 x Anime Count" for bigger games).
    With two or more unlock categories (e.g. Unlock Mode "both", or genres plus Unlock by Year) at least 50 anime
    are used (lower values are raised to 50)."""
    display_name = "Anime Count"
    range_start = 10
    range_end = len(ANIME)
    default = min(50, len(ANIME))


class AnimeGoal(Range):
    """How many anime you need to guess to win (only with Goal: anime).
    If this is higher than Anime Count, it is lowered to Anime Count."""
    display_name = "Anime Goal"
    range_start = 1
    range_end = len(ANIME)
    default = 40


class OnlyGenres(OptionSet):
    """Play only with anime of these genres or target audiences, e.g. ["Romance"] or ["Shounen"].
    With several, an anime needs at least one of them. Empty = all anime.
    Genres then do not unlock anything at all (there are no genre items): you unlock anime only by
    letters and/or the Unlock by Year/Source/Season/Studio options. If none of these is on, letters are used.
    Only anime of these genres are picked. If there are fewer than Anime Count, Anime Count is lowered."""
    display_name = "Only Genres"
    valid_keys = frozenset(GENRES)
    default = frozenset()


class OnlyGenresStartAnime(Range):
    """Only with Only Genres: how many random anime you can guess right from the start.
    You get the items (letter, year ...) of exactly this many random anime as starting items.
    Their items may open a few more anime as well."""
    display_name = "Only Genres Start Anime"
    range_start = 2
    range_end = 8
    default = 3


class UnlockMode(Choice):
    """What you need before you may guess an anime.
    genres: its genres (see Genre Rule).
    letters: the first letter of its title (see Title Language).
    both: its genres AND its first letter. Needs at least 50 anime (Anime Count is raised if lower).
    Unlock by Year/Source/Season/Studio can be added on top of any mode."""
    display_name = "Unlock Mode"
    option_genres = 0
    option_letters = 1
    option_both = 2
    default = 2


class UnlockByYear(Toggle):
    """Also need the release year of the first part before you may guess an anime.
    Items like "Year: 2013"; before 2010 in ranges ("Year: 2005-2009", "Year: 2000-2004", "Year: Before 2000")."""
    display_name = "Unlock by Year"


class UnlockBySource(Toggle):
    """Also need what the anime is based on: "Source: Manga", "Source: Light Novel", "Source: Novel",
    "Source: Original", "Source: Visual Novel", "Source: Video Game" or "Source: Other"."""
    display_name = "Unlock by Source"


class UnlockBySeason(Toggle):
    """Also need the season it first aired: "Season: Winter", "Season: Spring", "Season: Summer" or "Season: Fall"."""
    display_name = "Unlock by Season"


class UnlockByStudio(Toggle):
    """Also need a studio of the anime, e.g. "Studio: MADHOUSE". If several studios made it (Attack on Titan:
    WIT STUDIO and MAPPA), any one of them is enough. Smaller studios share "Studio: Other"."""
    display_name = "Unlock by Studio"


# Feste Nummern je Sprache (niemals aendern, nur hinten ergaenzen). Angeboten werden nur Sprachen aus der Datenbank,
# die genug Titel haben (25-%-Regel in offline/skripts/build.py).
_LANGUAGE_VALUES = {"english": 0, "romaji": 1, "german": 2, "spanish": 3, "french": 4, "japanese": 5,
                    "italian": 6, "portuguese": 7}
TitleLanguage = type("TitleLanguage", (Choice,), {
    "__doc__": """Your language preference. It decides the first letter of each anime (only with letters or both)
    and in which language the client shows the anime titles.
    english: Attack on Titan = A.  romaji: Shingeki no Kyojin = S.
    Other languages: the title in that language, e.g. Spirited Away in German = "Chihiros Reise ins Zauberland" = C.
    Anime without a title in that language use the English one.
    japanese: titles are shown in Japanese; the letter comes from the Romaji title (Japanese has no A-Z).
    A leading "The" counts. Titles starting with a number or symbol use the "#" letter.
    Every known title in every language is accepted when guessing.""",
    "__module__": __name__,
    "display_name": "Title Language",
    **{f"option_{lang}": value for lang, value in _LANGUAGE_VALUES.items() if lang in TITLE_LANGUAGES},
    "default": 0,
})


class GenreRule(Choice):
    """Which genres unlock an anime (only with Unlock Mode genres or both).
    any: one of its genres is enough.
    all: you need every genre of that anime (much harder)."""
    display_name = "Genre Rule"
    option_any = 0
    option_all = 1
    default = 0


def _genre_option_name(genre: str) -> str:
    return "option_" + genre.lower().replace(" ", "_").replace("-", "_")


# StartingGenre: eine Auswahl pro Genre plus "random". Wird aus der Genre-Liste erzeugt.
StartingGenre = type("StartingGenre", (Choice,), {
    "__doc__": "The genre you have unlocked from the start. random picks one that unlocks enough anime.",
    "__module__": __name__,
    "display_name": "Starting Genre",
    **{_genre_option_name(g): i for i, g in enumerate(GENRES)},
    "option_random": len(GENRES),
    "default": len(GENRES),
})


class GenreStep(Range):
    """Only with Genre Rule "any": for every this many genres an anime has, it needs one more of them.
    Example with 6: 1-5 genres -> one genre is enough, 6-11 genres -> two needed, 12 or more -> three needed.
    Makes anime with many genres harder to unlock and spreads your checks over more spheres.
    0 = off (one genre is always enough)."""
    display_name = "Genre Step"
    range_start = 0
    range_end = 12
    default = 6


class IncludeDemographics(DefaultOnToggle):
    """The target audience counts as an extra genre: Shounen, Shoujo, Seinen, Josei, Kids.
    Example: Naruto is Action, Adventure, ... and also Shounen.
    Many anime (e.g. Your Name, Cowboy Bebop) have no target audience; for them only the normal genres count.
    Only used with Genre Rule "any". With "all" the target audience is ignored, so it never becomes an extra requirement."""
    display_name = "Include Demographics"


class PerkItems(DefaultOnToggle):
    """Adds the helpful perk items:
    Sukuna's Finger (up to 20x): each reveals a hint about an anime. With all fingers in your game:
    Domain Expansion, one anime of your choice counts as guessed.
    Dragon Balls (7x): once you have all 7 you may unlock a genre of your choice.
    Senzu Bean (3x): ends all running trap effects when you use it.
    Time Leap (3x): the next trap that hits you misses."""
    display_name = "Perk Items"


class GeassItems(Range):
    """How many Geass are in your game. Each Geass lets you pick any anime (even a locked one):
    it counts as guessed immediately. 0 = no Geass.
    At most 10% of your Anime Count is used (e.g. 50 anime -> at most 5 Geass)."""
    display_name = "Geass Items"
    range_start = 0
    range_end = 50
    default = 10


class TrapLink(Toggle):
    """Trade traps with other games that support TrapLink: when you get a trap, other TrapLink players get one too,
    and their traps hit you as one of the Animepelago traps."""
    display_name = "Trap Link"


class StandArrowItems(Range):
    """How many Stand Arrows are in your game. Each one reveals all information about an anime of your choice
    (year, studio, episodes, format, source, season and a blurred cover). 0 = no Stand Arrows.
    In small worlds there may be less room, then fewer are used."""
    display_name = "Stand Arrow Items"
    range_start = 0
    range_end = 100
    default = 10


class TrapItems(DefaultOnToggle):
    """Adds the trap items:
    Kira's Hand (5x): locks a random genre for 60 seconds.
    Isekai Truck (3x): shuffles the anime fields for 60 seconds (the numbers stay).
    Filler Arc (3x): hides all hints and info for 60 seconds.
    Tsundere (3x): for 30 seconds every correct answer is refused once ("B-baka!"); just try again.
    Kira's Hand details:
    If genres do not unlock anything in your world (e.g. Only Genres), it locks a letter instead.
    It never locks your last free genre/letter: then it waits until you have a second one."""
    display_name = "Trap Items"


@dataclass
class AnimepelagoOptions(PerGameCommonOptions):
    goal: Goal
    genre_master_genres: GenreMasterGenres
    genre_master_anime: GenreMasterAnime
    anime_count: AnimeCount
    anime_goal: AnimeGoal
    only_genres: OnlyGenres
    only_genres_start_anime: OnlyGenresStartAnime
    unlock_mode: UnlockMode
    unlock_by_year: UnlockByYear
    unlock_by_source: UnlockBySource
    unlock_by_season: UnlockBySeason
    unlock_by_studio: UnlockByStudio
    title_language: TitleLanguage
    genre_rule: GenreRule
    genre_step: GenreStep
    include_demographics: IncludeDemographics
    starting_genre: StartingGenre
    perk_items: PerkItems
    geass_items: GeassItems
    stand_arrow_items: StandArrowItems
    trap_items: TrapItems
    death_link: DeathLink
    trap_link: TrapLink


option_groups = [
    OptionGroup("Game", [Goal, GenreMasterGenres, GenreMasterAnime, AnimeCount, AnimeGoal, OnlyGenres, OnlyGenresStartAnime, UnlockMode, UnlockByYear, UnlockBySource, UnlockBySeason, UnlockByStudio, TitleLanguage, GenreRule, GenreStep, IncludeDemographics, StartingGenre]),
    OptionGroup("Items", [PerkItems, GeassItems, StandArrowItems, TrapItems, TrapLink]),
]
