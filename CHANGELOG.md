# Changelog

## 0.1.4 (in progress)
- **Collect option:** when another player collects their items from your anime, those anime are marked 📦. A new switch while connected decides whether they count towards your goal (on by default, the fastest way through) or whether only anime you guessed yourself count; then the 📦 anime stay guessable.
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
