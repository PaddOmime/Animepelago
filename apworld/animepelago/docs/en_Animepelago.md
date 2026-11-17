# Animepelago

Animepelago is an anime guessing game. Every anime in your game is a check: type its name in the
Animepelago web client to send the check.

You may only guess an anime once you have its genres. Depending on your settings you need one of its
genres (`genre_rule: any`) or all of them (`genre_rule: all`). Genres are items in the multiworld.

## Items
- With `only_genres` (e.g. `[Romance]`) your world contains only anime of these genres. There are no genre items then:
  you unlock anime by letters and/or year, source, season and studio. You start with the items of a few random anime
  (`only_genres_start_anime`, 2–8, default 3).
- **Year / Source / Season / Studio: ...** are needed as well when you switch on `unlock_by_year`,
  `unlock_by_source`, `unlock_by_season` or `unlock_by_studio`.
- **Genre: ...** unlocks anime of that genre. With `include_demographics` (on by default) the target audience
  counts as a genre too: Shounen, Shoujo, Seinen, Josei, Kids. Anime without a target audience use only their normal genres.
  This only applies with `genre_rule: any`; with `all` the target audience is ignored.
- **Sukuna's Finger**, **Dragon Ball**: helpful perks.
- **Senzu Bean** ends all running trap effects, **Time Leap** makes the next trap miss.
- Traps: **Kira's Hand** (locks a genre), **Isekai Truck** (shuffles the fields), **Filler Arc** (hides hints),
  **Tsundere** (refuses a correct answer once). With `trap_link` traps are traded with other TrapLink games.
- Goal `genre_master`: guess `genre_master_anime` anime in each of `genre_master_genres` genres.
- **Stand Arrow** (`stand_arrow_items`, default 10, up to 100): reveals all information about an anime of your choice.
- **Geass** (`geass_items`, default 10, at most 10% of your anime): pick any anime, even a locked one,
  and it counts as guessed.
- **Kira's Hand**, **Death Note**: traps.
- **Exodia pieces**: with `goal: exodia`, collect all 5 to win.

## Goal
Guess the number of anime set in `anime_goal`, or collect Exodia.
