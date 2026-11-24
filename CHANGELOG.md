# Changelog

## 0.2.1 (in progress)

### Word Salad (new)
- New mini game under More: the letters of an anime title are shuffled word by word – unscramble it. **Endless** with a streak, or **2 minutes** on the clock with a personal best.
- 💡 reveals the first letter of the next word (costs 5 seconds on the clock). Any known name of the anime counts as the answer; afterwards you see the key art.
- Titles follow your title language and top N / genre settings. 11 new achievements (now 233), XP for every title, saved in your profile and in backups.

### Languages
- **Spanish, French, Italian and Japanese** are now complete in the client: Animedle, the new achievements and the footer were still English.
- **Party games** (`party.html`) now also speak Spanish, French, Italian and Japanese (before: only German and English).

### Archipelago
- **New guides:** the game page and the setup guides (shown on archipelago.gg and in the Launcher) are rewritten and complete – items, goals, important options, connecting, local servers. The game page now also exists in German.
- The description of `title_language` said a leading "The" counts for the letter – it doesn't (since 0.1.4). Fixed in the option text and the YAML template.

### Fixes (review)
- The achievement **"Tic-Tac-Anime"** (win a 3×3 bingo) could never unlock – the board size was compared wrongly. Fixed; it unlocks with your next 3×3 win.
- **Animedle progress now belongs to the profile** like the other mini games: it is saved in profile backups, taken over by your first profile and removed when a profile is deleted (before, the daily streak was shared by all profiles on the device and missing in backups).
- Party games: the privacy note now says exactly what happens to rooms – "Leave" in the show view deletes the room, rooms left open are locked after 6 hours.

## 0.2.0

### Archipelago
- **Auto-reconnect:** if the connection to the Archipelago server drops during a game, the client reconnects by itself (after 2, 4, 8, 15, then every 30 seconds; at once when the internet is back). The game stays open, guessing pauses meanwhile, and anything that was not sent yet (progress, checks) is sent after reconnecting. A bar shows the status, with "Reconnect now" and "Stop".
- **Collect option:** when another player collects their items from your anime, those anime are marked 📦. A switch while connected decides whether they count towards your goal (on by default, the fastest way through) or whether only anime you guessed yourself count; then the 📦 anime stay guessable.
- **Twitch integration – chat guesses along** *(preview – not tested live on stream yet; feedback welcome!)*: the Twitch button at the top (a dot shows the status). Enter your channel name (no login needed – the page only reads the chat). Correct answers from chat for unlocked anime count like your own and show who guessed them (💬 on the tile, "Chat MVPs"). Modes: automatic or suggestions you accept. Spam protection (one guess per viewer every few seconds), optional `!rate`/`!guess` prefix. The on/off switch keeps the setup, "Remove" deletes it; a notice appears if the channel can't be found or the connection drops. Agree with your multiworld whether chat help is OK.

### Profiles, routes and achievements
- **Profiles:** the new 👤 button at the top. Create one or more profiles on this device; your first profile takes over the records you already have. Offline games and all mini games give XP and unlock achievements – 222 of them, some secret. Bingo counts for your profile when your profile name is one of the players.
- **Archipelago counts too:** playing Archipelago always counts as a play day (daily streaks). If your profile has chosen a route, Archipelago games also give XP and achievements (guessed anime, perks, traps, reaching your goal – new achievements "Multiworld Hero" and "Archipelago Veteran"). Chat guesses from Twitch give no XP.
- **Choose your route:** 7 routes with 10 ranks each, from level 1 to 100 – 1 Saiyan, 2 Pirate, 3 Ninja, 4 Soul Reaper, 5 Hero, 6 Jujutsu Sorcerer, 7 Demon Slayer. All XP go into the route you picked. When a route is maxed you choose the next one, or press "Chronological" to take the lowest-numbered route that isn't maxed yet. Every unlocked rank can be shown as your title.
- **Leaderboards per game** in the profile window: offline wins (anime per minute), Hangman (streak), Bingo (wins by player name), Bingo Time Attack (time per board) and Top 100 (best time per list).
- **Backup:** save the profile as a file or copy it as a code, and load it again (also on another device). The format is described in docs/PROFIL_FORMAT.md, so a later server with real accounts could take it over.

### Bingo
- **2–6 sides:** choose how many players or teams play, each with its own name, colour and symbol (✕ ◯ △ □ ☆ ◇). Enter team members (comma-separated) to make a side a team – inside a team the players take turns.
- **Scoreboard:** every side always shows its fields and wins in a clear box above the grid; the side whose turn it is is highlighted; teams also show each player's fields.
- **Time Attack:** alone or together as a team (great on Discord), in any size: fill the **whole** board as fast as possible. Just type an anime – it goes into the selected field or automatically into a free field where it fits. Wrong answers cost 10 seconds. Only complete boards count; best times are saved per player/team name and per board.
- **Seed mode & editor:** every board has a **board code** – share it and others get exactly the same board (great for comparing Time Attack times). Save boards, and build your own in the new editor ("🔑 Bingo seed & editor" under More): pick the category of every row and column, see live how many anime fit each field, let the rest fill at random, then play versus or Time Attack. The editor warns about fields without answers and boards where you can get stuck.
- **🔥 Risk Bingo:** a hidden mode – it only appears for a profile with the achievement "Playing with Fire" (fill a bingo board of 5×5 or larger completely while your profile is active). Guests never see it. Huge boards from 7×7 to 10×10: every field has at least 1–3 answers (your choice) and the whole board can be filled – but one anime in the wrong field can lock you out. Fields with only 1–5 answers left show a 🔥 with the number (more flames appear as anime are used). The game spots dead ends at once. For every 10 anime you enter you earn one clear: Time Attack +5:00 per clear; versus only your own fields and it costs your turn.
- **New category: single years** (🗓️ 2010–2026, own checkbox). Years and decades never cross on a board (no "2010s × 2013"): if both appear, they are all rows or all columns.
- **Letter pairs:** a letter category is now randomly a single letter or a pair like "🔤 J / K" (title starts with one of the two). Every pair contains a rare letter (E, J, O, U, V, Y, Z, Q, X …) plus a fitting partner, so rare letters finally show up too. Letters and letter pairs never cross on a board.

### Animedle (new)
- New mini-game under More: guess the anime – every guess shows per hint whether it matches (🟩), is close (🟨) or is different (🟥): genres, demographic, year (with ⬆️/⬇️), season, source, studio, popularity (with ⬆️/⬇️), first letter (with ⬅️/➡️) and number of words in the title (with ⬆️/⬇️).
- **Daily puzzle:** the same anime for everyone each day (from the 300 most popular), progress survives a reload, daily streak, and a "Share result" button that copies an emoji grid without spoilers (for Discord / chat).
- **Suggestions while typing** (like Loldle): every anime whose title starts with what you typed, A–Z, with logo and year – in your title language first, then matches from other languages (e.g. romaji). Arrow keys + Enter or a click guesses it.
- **Endless** mode with the same settings as Hangman (top N, only one genre).
- 11 new achievements (category Animedle), XP for every solved puzzle (bonus for the daily).

### Party games (new)
- New page `party.html` ("🎉 Party games" under More) – play together online, e.g. over Discord. The host opens a room and shares the show view; everyone joins with the room code on their phone or a second window and answers in secret – answers are revealed at the same time. Player bar with names, colours, who has answered and points.
- **Blind Ranking:** place anime on spots 1–N without knowing what comes next, then compare with AniList popularity.
- **Higher or Lower:** more popular / newer? Players see both anime with their logos on their phone.
- **Bingo over the distance:** everyone sees the same board (3×3 to 6×6, with anime logos) on their own device – *against each other* (first one to name a fitting anime gets the field; 3×3/4×4 first line wins, from 5×5 most fields; wrong answer = 3 s pause) or *together* (co-op time attack, wrong answer +10 s). Tap a field to aim for it, otherwise the best free field is picked. The show view has a "Play along" link that opens the player view in a new tab.

### Other
- **Colorblind mode:** the 👁 button at the top switches right/wrong from green/red to blue/orange (Okabe-Ito colours) and adds symbols: crossed-out missing chips and a dashed border on guessable anime. The choice is remembered.
- **Hangman and Animedle show the key art** (AniList cover) with title, genres and an AniList link when the anime is solved or revealed – so you at least see the anime you didn't know.
- Windows (profile, Twitch, info) now close with the ✕ at the top or by clicking outside.
- Fixed: the achievement "Big Board Boss" (win a bingo of 6×7 or larger) was unlocked together with "Playing with Fire" because both had the same internal ID. It now only unlocks with a real 6×7 (or larger) win – profiles that got it by mistake will see it locked again.
- A leading "The" no longer counts for the letter: *The Promised Neverland* is a P anime (Letter clue, Unlock by Letter, Bingo). "T" had 263 anime, now about 100.
- Titles also count without "The" (e.g. "Promised Neverland", "Apothecary Diaries").
- *Time of Eve: The Movie* belongs to *Time of Eve*; *The Garden of Sinners* has its proper name.
- The client shows the TMDB logo next to the data credits at the bottom of the page, as TMDB asks for (logo silhouettes come from TMDB).

## 0.1.3 (Beta)
- **New mini game 🏆 Top 100** (under 🎮 More): name the 100 best-rated anime on AniList, of all time or for one of 18 genres. Every anime counts once (its best-rated part); with timer, best time, "give up" and saved progress.
- **1920 anime** (up from 1470): the 100 best-rated anime of all time and of every genre are in now, including classic OVA works such as *Legend of the Galactic Heroes*, *Hellsing Ultimate*, *Gunbuster* and *Giant Robo*.
- **Canon check for movies, OVAs and specials:** about 1,200 entries were reviewed by hand. Only canon parts count towards their anime (e.g. *Demon Slayer: Mugen Train*, *Dragon Ball Super: Broly*, *The Last: Naruto the Movie*); non-canon movies, recaps and short extras do not, but are still listed in the overview.
- **Franchise fixes:**
  - *Dragon Ball* is split into five anime: *Dragon Ball*, *Z*, *GT*, *Super* (with *Battle of Gods* and *Resurrection 'F'*) and *DAIMA*; *Dragon Ball Z Kai* is left out as a recut.
  - *Berserk* (1997) includes the Golden Age Arc movies and *Berserk* (2016/2017); the *Memorial Edition* recut is left out.
  - *Fate/kaleid liner Prisma☆Illya* is its own anime now; the 2010 *Unlimited Blade Works* movie belongs to the ufotable series.
  - Movies that were separate anime now belong to their series: *Gintama*, *Gurren Lagann*, *Anohana*, *Clannad*, *Orange*, *Love, Chunibyo & Other Delusions*, *Naruto Shippuden* (*The Last*, *Road to Ninja*), *Boruto*.
  - *Kizumonogatari* belongs to the *Monogatari Series*, *Conqueror of Shamballa* to *Fullmetal Alchemist* (2003), *Cyberpunk: Edgerunners 2* to *Cyberpunk: Edgerunners*.
- **Better names:** "Season 1", "Part I" and "S1" are gone from anime names (e.g. *Natsume's Book of Friends*). Short names count as answers too: "Cyberpunk", "86", "Eighty Six", series names before a dash subtitle (*Code Geass: Akito the Exiled*, *Kaiji*). "Dragon Ball" and "Dragon Ball Z" no longer solve two anime at once.
- Anime without a TV series take their name, logo and cover from their first OVA series, otherwise from their first movie (e.g. *Legend of the Galactic Heroes*, *Mobile Police Patlabor*).
- Option texts in the YAML updated (Unlock by Studio: any studio of the anime counts).

## 0.1.2 (Beta)
- **New interface languages (beta):** Español, Français, Italiano and 日本語, in addition to English and Deutsch. The client picks your browser language automatically. Translations were pre-translated with DeepL and corrected by hand; item names stay in English. Corrections are welcome!
- **Unlock by Studio:** every main studio of an anime counts now, not only the one of season 1 (e.g. *Attack on Titan* opens with WIT STUDIO **or** MAPPA).
- **Logos:** the logo of the first season's series is preferred (e.g. *My Hero Academia* no longer shows a spin-off logo). Own logo picks are possible in `corrections.json`.
- Main studios are now known for all anime (26 newer studios were missing).
- **Clow Cards:** a collectible filler. Depending on the world size up to 53 of them (like the original deck) are in the pool; the client shows *Clow Cards x/N* and celebrates when you have them all. No gameplay effect.
- **13 more joke filler items** (42 in total): *Nico Nico Nii*, *Moon Prism Power, Make Up!*, *Tuxedo Mask's Top Hat*, *Yowai mo*, *Omae wa mou shindeiru*, *Nani?!*, *Hisashiburi da na, Mugiwara*, *ORA ORA ORA*, *MUDA MUDA MUDA*, *Daisukiiiiii*, *The One Piece is REAL!*, *Have a Plus Ultra Day*, *Clow Card*.
- **1470 anime** (up from 978), 1429 of them with logo silhouettes. The web client already uses the new list; it also works with 0.1.1 worlds.

## 0.1.1 (Beta)

### ▶ [Play in your browser](https://paddomime.github.io/Animepelago/client/)

**Install:** download `animepelago.apworld` below and double-click it (or copy it into `custom_worlds`), replacing 0.1.0. Host and all players should use the same version.

### New
- **29 joke filler items** without any effect, just for fun: *AYAYA!*, *Ara Ara*, *Nya!*, *Waifu*, *Husbando*, *Straw Hat*, *Gum-Gum Fruit*, *Den Den Mushi*, *Going Merry*, *Thousand Sunny*, *Zangetsu*, *Hogyoku*, *Hollow Purple*, *Gojo's Blindfold*, *Naruto's Headband*, *Tanjiro's Hanafuda Earrings*, *Inosuke's Boar Mask*, *Saitama's Gloves*, *Survey Corps Cloak*, *3D Maneuver Gear*, *NerveGear*, *Philosopher's Stone* and more. About one in four filler slots gets one of them (item group `Fillers`).
- **Anime Bingo:** choose which theme types appear (Genre, Demographic, Studio, Source, Decade, Season, Letter) and a new **6×7** board (most fields wins). A smarter check makes sure you can never get stuck.
- Bigger Bingo fields and text on desktop screens.

### Fixed
- Titles from Wikidata no longer contain season names (e.g. *"My Hero Academia/Staffel 1"* is now *"My Hero Academia"*, *"Primera temporada de …"* in Spanish, *"saison 1 de …"* in French, *"prima stagione di …"* in Italian). This also fixes the first letter of those anime for Spanish, French and Italian titles.

### Thanks
- **Pulpup** for testing.

---
🇩🇪 **Neu in 0.1.1:** 29 Spaß-Füller ohne Wirkung (AYAYA!, Waifu, Husbando, Strohhut, Teleschnecke …), Bingo mit frei wählbaren Themen und neuem 6×7-Feld, Titel ohne Staffel-Angaben („My Hero Academia/Staffel 1“ → „My Hero Academia“). Danke an **Pulpup** fürs Testen! Bitte die alte `animepelago.apworld` ersetzen; Host und alle Spieler brauchen dieselbe Version.

## 0.1.0 (Beta)
First public beta: 978 anime (968 with logo silhouettes), titles in 7 languages, unlocks by genre / letter / year / source / season / studio, goals (anime, Exodia, Genre Master), perks and traps, DeathLink, TrapLink, Universal Tracker, offline mode, Hangman and Anime Bingo.
