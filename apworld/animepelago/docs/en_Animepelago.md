# Animepelago

## What is this game?

Animepelago is an anime guessing game. Every anime in your world is a check: type its title in the
[Animepelago web client](https://paddomime.github.io/Animepelago/client/) to send that check. Any known title counts –
English, Romaji, Japanese, German, Spanish, French or Italian, and small typos are forgiven.

You can't guess every anime right away. An anime only becomes guessable once you have the items it needs:
its genres, the first letter of its title, or both – and, if you like, its year, source, season and studio.
These items are spread across the multiworld, so your friends unlock your anime and you unlock their stuff.

The anime come from [AniList](https://anilist.co) (about 1,900 of the best-known series and films). Covers, studios,
episodes and related seasons are loaded live from AniList while you play.

## What does randomization do to this game?

The anime in your world are picked at random (preferring well-known ones), and the unlock items – genres,
letters, years, sources, seasons, studios – are shuffled into the multiworld. Each anime is one location
(e.g. "Attack on Titan"), plus milestone locations such as "Guessed 10 Anime".

A whole franchise counts as one anime: all seasons and films of *Attack on Titan* are one check, and you may
guess it with the name of any part.

## What items are there?

**Unlock items** (progression):
- **Genre: …** – e.g. *Genre: Romance*. With `include_demographics` the target audience counts as a genre too
  (*Genre: Shounen*, *Shoujo*, *Seinen*, *Josei*, *Kids*) – only with `genre_rule: any`.
- **Letter: …** – the first letter of the title in your `title_language` (*Letter: A* … *Letter: Z*, *Letter: #*
  for numbers and symbols). A leading "The" does not count: *The Promised Neverland* is a **P** anime.
- **Year: …**, **Source: …**, **Season: …**, **Studio: …** – only with `unlock_by_year`, `unlock_by_source`,
  `unlock_by_season` or `unlock_by_studio`. Years before 2010 come in ranges (*Year: 2005-2009*, *Year: Before 2000*),
  smaller studios share *Studio: Other*.

**Perks** (`perk_items`, on by default):
- **Sukuna's Finger** – reveals a hint about an anime. With all fingers: **Domain Expansion**, one anime of your
  choice counts as guessed.
- **Dragon Ball** – with all 7 you may wish for a genre of your choice.
- **Senzu Bean** – ends all running trap effects. **Time Leap** – the next trap misses.
- **Stand Arrow** (`stand_arrow_items`) – reveals everything about one anime (year, studio, episodes, format,
  source, season and a blurred cover).
- **Geass** (`geass_items`, at most 10 % of your anime) – pick any anime, even a locked one: it counts as guessed.

**Traps** (`trap_items`, on by default):
- **Kira's Hand** – locks a random genre (or letter) for 60 seconds. It never locks your last free one.
- **Isekai Truck** – shuffles the anime tiles for 60 seconds.
- **Filler Arc** – hides all hints and info for 60 seconds.
- **Tsundere** – for 30 seconds every correct answer is refused once ("B-baka!") – just try again.
- **Death Note** – harmless filler, but with `death_link` it sends a DeathLink.
- With `trap_link` traps are traded with other TrapLink games.

**Fillers:** *Filler Episode*, collectible *Clow Cards* and lots of fun items without effect
(*AYAYA!*, *Straw Hat*, *Omae wa mou shindeiru* …).

**Exodia:** with `goal: exodia` the five pieces of *Exodia the Forbidden One* are in the pool.

## What is the goal?

Depending on `goal`:
- **anime** (default): guess the number of anime set in `anime_goal`.
- **exodia**: collect all 5 Exodia pieces.
- **genre_master**: guess `genre_master_anime` anime in each of `genre_master_genres` different genres.
- **big3_daddy**: guess Goku, Luffy, Naruto and Ichigo – the Big 3 and their "Daddy" Dragon Ball. Each hero opens after you
  guessed his anime and have a "Characters: <Genre>" of it and all 3 Progressive Rarity. With `character_gender: [female]`
  it is Chi-Chi, Boa Hancock, Hinata Hyuga and Orihime Inoue.
- **characters**: guess `character_goal` characters (Waifupelago; turned on automatically).

## Waifupelago (characters)

- `character_rarity` (off / famous_only / medium_and_famous / all): characters of your guessed anime become extra checks.
  You need a "Characters: <Genre>" item of the anime and "Progressive Rarity" – the rarest characters come first, the most famous last.
- `character_max`: at most this many character checks per anime (0 = no limit).
- `character_gender`: which characters can be guessed (female, male, nonbinary).

## Important options

| Option | What it does |
|---|---|
| `anime_count` | How many anime (checks) are in your world. |
| `unlock_mode` | `genres`, `letters` or `both` (default) – what an anime needs before you may guess it. |
| `genre_rule` | `any`: one of its genres is enough (with `genre_step` long genre lists need more). `all`: every genre. |
| `starting_genre` | Which genre you start with, `auto` (default: a rarer genre with enough anime) or `random`. |
| `only_genres` | Play only with anime of certain genres, e.g. `[Romance]`. Then there are no genre items; you start with the items of a few anime (`only_genres_start_anime`). |
| `title_language` | Decides the letters and in which language the client shows titles. |
| `unlock_by_year` / `_source` / `_season` / `_studio` | Extra unlock items on top. |

The full list with explanations is in the YAML template (download button in the client) and in the Options Creator.

## What does another world's item look like in Animepelago?

Items for other players are hidden behind your anime: when you guess an anime correctly, its check is sent and
the item goes to whoever it belongs to.

## When the player receives an item, what happens?

A message appears in the client, newly guessable anime light up, and perks become usable. Traps take effect at once.

## Extras in the client

- **Offline mode and mini games** (Hangman, Word Salad, Animedle with a daily puzzle, Anime Bingo, Top 100) – no server needed.
- **Profiles, routes and achievements**: Archipelago games count for your play days; with a chosen route they also give XP.
- **Twitch integration**: your chat can guess along (read-only, no login). Agree with your multiworld
  whether chat help is OK.
- **Auto-reconnect** if the connection drops; nothing is lost.
