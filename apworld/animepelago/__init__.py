"""Animepelago: ein Anime-Ratespiel fuer Archipelago.

Jeder Anime ist ein Check. Du darfst einen Anime erst raten, wenn du die passenden
Items hast: seine Genres (eines oder alle, je nach Genre Rule), seinen Anfangsbuchstaben
oder beides (Unlock Mode), dazu auf Wunsch Jahr, Vorlage, Jahreszeit und Studio (Unlock by Year/Source/Season/Studio).

Buchstaben und die Extra-Kategorien sind "Einzelwert-Kategorien": jeder Anime hat genau einen Wert
(z. B. Letter A, Year 2013), und man braucht genau dieses Item.
"""

import logging
from typing import Any

from BaseClasses import ItemClassification, Region, Tutorial
from Options import OptionError
from worlds.AutoWorld import WebWorld, World
from worlds.generic.Rules import set_rule

from .data import ANIME, ANIME_BY_ID, DATA_VERSION, DEMOGRAPHICS, GENRES, HAS_CATEGORY, HAS_DEMOGRAPHICS, LETTERS
from .Items import (CLOW_CARD, CLOW_CARD_MAX, EXODIA_PIECES, EXTRA_CATEGORIES, FILLER_ITEM, FLAVOR_FILLERS, GAME, ITEMS, AnimepelagoItem, extra_item,
                    genre_item, item_name_groups, item_name_to_id, letter_item)
from .Locations import (LOCATION_ID_OFFSET, MILESTONES, AnimepelagoLocation, location_name_groups,
                        location_name_to_id, milestone_name)
from .Options import AnimepelagoOptions, option_groups

# So viele Anime muessen am Anfang (nur mit den Start-Genres) erratbar sein,
# sonst haette der Spieler keinen Einstieg.
MIN_START_ANIME = 3

# Mit zwei oder mehr Kategorien (z. B. Genres UND Buchstaben) gibt es viele Freischalt-Items. Darunter waere das Spiel zu klein.
MIN_ANIME_BOTH = 50


class AnimepelagoWeb(WebWorld):
    theme = "partyTime"
    option_groups = option_groups
    tutorials = [
        Tutorial("Multiworld Setup Guide", "How to play Animepelago with Archipelago.",
                 "English", "setup_en.md", "setup/en", ["paddomime"]),
        Tutorial("Multiworld Setup Guide", "So spielst du Animepelago mit Archipelago.",
                 "Deutsch", "setup_de.md", "setup/de", ["paddomime"]),
    ]


def pool_size_for(count: int) -> int:
    """Aus wie vielen der beliebtesten Anime gezogen wird (fest eingebaut, keine Option mehr)."""
    return max(500, 2 * count)


class AnimepelagoWorld(World):
    """Guess anime to send checks. Unlock genres from your friends to be allowed to guess more anime."""

    game = GAME
    web = AnimepelagoWeb()
    options_dataclass = AnimepelagoOptions
    options: AnimepelagoOptions
    topology_present = False

    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id
    item_name_groups = item_name_groups
    location_name_groups = location_name_groups

    # Universal Tracker: kann die Welt ohne YAML aus den slot_data nachbauen
    ut_can_gen_without_yaml = True

    @staticmethod
    def interpret_slot_data(slot_data: dict[str, Any]) -> dict[str, Any]:
        return slot_data

    # ---------- Vorbereitung ----------

    def generate_early(self) -> None:
        # Universal Tracker: dieselbe Welt wie beim Erstellen aus den slot_data nachbauen
        re_gen = getattr(self.multiworld, "re_gen_passthrough", {}).get(self.game)
        if re_gen:
            self._from_slot_data(re_gen)
            return
        mode = self.options.unlock_mode
        self.use_genres = mode.value in (mode.option_genres, mode.option_both)
        self.use_letters = mode.value in (mode.option_letters, mode.option_both)
        # Nur bestimmte Genres (only_genres): Genres schalten dann nichts frei, nur die anderen Kategorien.
        self.only_genres = set(self.options.only_genres.value)
        # Einzelwert-Kategorien in fester Reihenfolge: Buchstabe, dann die gewaehlten Extras
        chosen = {"year": self.options.unlock_by_year, "source": self.options.unlock_by_source,
                  "season": self.options.unlock_by_season, "studio": self.options.unlock_by_studio}
        self.extras = [c for c in EXTRA_CATEGORIES if chosen[c].value]
        # Aeltere Datenbank ohne Werte fuer eine Kategorie: Option abschalten statt eine Welt ohne Items zu bauen
        for c in [c for c in self.extras if not HAS_CATEGORY[c]]:
            logging.warning(f"Animepelago ({self.player_name}): Die Anime-Datenbank hat noch keine Werte fuer "
                            f"'{c}'. unlock_by_{c} wird ignoriert.")
            self.extras.remove(c)
        if self.only_genres & set(DEMOGRAPHICS) and not HAS_DEMOGRAPHICS:
            raise OptionError(f"Animepelago ({self.player_name}): Die Anime-Datenbank hat noch keine Zielgruppen "
                              f"(Shounen, Shoujo ...). Bitte ein normales Genre bei Only Genres waehlen.")
        if self.only_genres:
            self.use_genres = False
            if not self.use_letters and not self.extras:
                logging.warning(f"Animepelago ({self.player_name}): Mit Only Genres gibt es keine Genre-Items. "
                                "Damit es etwas freizuschalten gibt, wird nach Buchstaben freigeschaltet.")
                self.use_letters = True
        self.single_cats = (["letter"] if self.use_letters else []) + self.extras
        count = self.options.anime_count.value
        if self.use_genres + len(self.single_cats) >= 2 and count < MIN_ANIME_BOTH:
            logging.warning(f"Animepelago ({self.player_name}): Mehrere Freischalt-Kategorien brauchen mindestens "
                            f"{MIN_ANIME_BOTH} Anime. Anime Count wird von {count} auf {MIN_ANIME_BOTH} erhoeht.")
            count = MIN_ANIME_BOTH
            self.options.anime_count.value = count
        self.goal_count = min(self.options.anime_goal.value, count)
        self.any_rule = self.options.genre_rule.value == self.options.genre_rule.option_any
        # Bei "any": pro genre_step Genres eines Anime ein weiteres noetig (0 = aus, dann reicht immer eins)
        self.genre_step = self.options.genre_step.value if self.any_rule else 0
        # Sprach-Praeferenz: zeigt die Titel in dieser Sprache an. Japanisch hat kein A-Z,
        # dort kommt der Anfangsbuchstabe deshalb aus dem Romaji-Titel.
        self.display_language = self.options.title_language.current_key
        self.language = "romaji" if self.display_language == "japanese" else self.display_language

        # Nur Anime mit mindestens einem der only_genres
        candidates = sorted(ANIME, key=lambda a: -(a.get("popularity") or 0))
        if self.only_genres:
            candidates = [a for a in candidates if self.only_genres & set(a["genres"] + a.get("demographics", []))]
            if len(candidates) < 10:
                raise OptionError(f"Animepelago ({self.player_name}): Only Genres {sorted(self.only_genres)} "
                                  f"hat nur {len(candidates)} Anime, mindestens 10 noetig.")
            if count > len(candidates):
                logging.warning(f"Animepelago ({self.player_name}): Nur {len(candidates)} Anime mit "
                                f"{sorted(self.only_genres)}. Anime Count wird von {count} darauf gesenkt.")
                count = len(candidates)
                self.options.anime_count.value = count
                self.goal_count = min(self.goal_count, count)
        # Nur aus den beliebtesten Anime waehlen: aus den Top 500, bei grossen Welten aus den Top "2 x Anime Count".
        # So sind es meist bekannte Anime, aber trotzdem jedes Mal andere. (Der Client rechnet offline genauso.)
        pool_size = pool_size_for(count)
        # Zielgruppen nur bei Genre Rule "any": bei "all" waeren sie eine zusaetzliche Pflicht
        self.use_demographics = bool(self.options.include_demographics.value) and self.any_rule
        if self.use_demographics and not HAS_DEMOGRAPHICS:
            logging.warning(f"Animepelago ({self.player_name}): Die Anime-Datenbank hat noch keine Zielgruppen. "
                            "Include Demographics wird ignoriert.")
            self.use_demographics = False
        # Kopien, damit die gemeinsame Liste nicht veraendert wird. Mit Zielgruppen zaehlen diese als Genres.
        pool = [dict(a, genres=a["genres"] + (a.get("demographics", []) if self.use_demographics else []))
                for a in candidates[:pool_size]]
        self.random.shuffle(pool)
        selected = pool[:count]
        rest = pool[count:]
        self.start_genres: set[str] = set()
        self.start_single: dict[str, set[str]] = {c: set() for c in self.single_cats}

        if self.use_genres:
            # Startgenre bestimmen
            if self.options.starting_genre.value == self.options.starting_genre.option_random:
                # Zufaellig unter den selteneren Genres, die genug Anime haben: so ist am Anfang nicht gleich
                # ein grosser Teil offen (ein haeufiges Startgenre wie Action wuerde viel auf einmal oeffnen).
                counts = {g: sum(g in a["genres"] for a in selected) for g in GENRES}
                usable = sorted((g for g in GENRES if counts[g] >= MIN_START_ANIME), key=lambda g: (counts[g], g))
                start = self.random.choice(usable[:4] or [g for g in GENRES if g not in DEMOGRAPHICS and g not in self.only_genres])
            else:
                start = GENRES[self.options.starting_genre.value]
                if start in DEMOGRAPHICS and not self.use_demographics:
                    logging.warning(f"Animepelago ({self.player_name}): Starting Genre {start} braucht "
                                    "Include Demographics. Es wird ein zufaelliges Genre genommen.")
                    usable = [g for g in GENRES if sum(g in a["genres"] for a in selected) >= MIN_START_ANIME]
                    start = self.random.choice(usable or [g for g in GENRES if g not in DEMOGRAPHICS and g not in self.only_genres])

            # Genug Anime mit dem Startgenre sicherstellen (notfalls Anime austauschen)
            have = [a for a in selected if start in a["genres"]]
            if len(have) < MIN_START_ANIME:
                extra = [a for a in rest if start in a["genres"]][:MIN_START_ANIME - len(have)]
                swap = [a for a in selected if start not in a["genres"]]
                self.random.shuffle(swap)
                for new, old in zip(extra, swap):
                    selected[selected.index(old)] = new
            self.selected = selected
            self.start_genres = {start}

            # Bei "all" (oder wenn Anime mehrere Genres brauchen) Start-Genres dazugeben, bis ein paar Anime
            # sofort erratbar sind. Sparsam: je Anime nur so viele (seltene) Genres, wie er wirklich braucht.
            if sum(self._genres_ok(x, self.start_genres) for x in selected) < MIN_START_ANIME:
                counts = {g: sum(g in a["genres"] for a in selected) for g in GENRES}
                def extra_needed(a):
                    need = len(a["genres"]) if not self.any_rule else self.genres_needed(a)
                    return need - sum(g in self.start_genres for g in a["genres"])
                for _ in range(len(selected)):
                    if sum(self._genres_ok(x, self.start_genres) for x in selected) >= MIN_START_ANIME:
                        break
                    rest_anime = [a for a in selected if not self._genres_ok(a, self.start_genres)]
                    a = min(rest_anime, key=lambda a: (extra_needed(a), self.random.random()))
                    missing = sorted((g for g in a["genres"] if g not in self.start_genres), key=lambda g: (counts[g], g))
                    self.start_genres |= set(missing[:extra_needed(a)])
        self.selected = selected

        # Start-Werte je Einzelwert-Kategorie (Buchstabe, Jahr, ...) dazunehmen, bis genug Anime sofort
        # erratbar sind. Jede Kategorie beruecksichtigt die vorherigen, am Ende passen also alle zusammen.
        if self.only_genres:
            # Only Genres: N zufaellige Anime ziehen und ihre Items als Start-Items geben (N per YAML).
            # Bevorzugt Anime, deren Items moeglichst wenige andere mit oeffnen, damit es etwa N offene sind.
            target = min(self.options.only_genres_start_anime.value, len(self.selected))
            while self._count_open(self.start_genres, self.start_single) < target:
                closed = [a for a in self.selected if not self._open(a, self.start_genres, self.start_single)]
                best, best_n = [], None
                for a in self.random.sample(closed, min(60, len(closed))):
                    trial = {c: v | ({self.value_of(a, c)} - {None}) for c, v in self.start_single.items()}
                    n = self._count_open(self.start_genres, trial)
                    if best_n is None or n < best_n:
                        best, best_n = [a], n
                    elif n == best_n:
                        best.append(a)
                pick = self.random.choice(best)
                for c in self.single_cats:
                    value = self.value_of(pick, c)
                    if value is not None:
                        self.start_single[c].add(value)
        for i, cat in enumerate([] if self.only_genres else self.single_cats):
            cats = self.single_cats[:i + 1]
            while self._count_open(self.start_genres, self.start_single, cats) < MIN_START_ANIME:
                gain: dict[str, int] = {}
                for a in self.selected:
                    value = self.value_of(a, cat)
                    if value is not None and value not in self.start_single[cat] and \
                            self._open(a, self.start_genres, self.start_single, cats[:-1]):
                        gain[value] = gain.get(value, 0) + 1
                if not gain:
                    break
                # Zufaellig unter den Werten, die allein schon reichen; sonst der beste.
                # So startet man nicht immer mit "T" (wegen "The" der groesste Buchstabe).
                needed = MIN_START_ANIME - self._count_open(self.start_genres, self.start_single, cats)
                enough = sorted(k for k, v in gain.items() if v >= needed)
                best = max(gain.values())
                self.start_single[cat].add(self.random.choice(enough or sorted(k for k, v in gain.items() if v == best)))

        self.milestones = [n for n in MILESTONES if n <= count]
        self._setup_goal()
        self._finish_setup()

    def _finish_setup(self) -> None:
        self.used_genres = sorted({g for a in self.selected for g in a["genres"]}, key=GENRES.index) \
            if self.use_genres else []
        # Benutzte Werte je Einzelwert-Kategorie (nur die, die bei den gewaehlten Anime vorkommen)
        self.used_single = {c: sorted({v for a in self.selected if (v := self.value_of(a, c)) is not None})
                            for c in self.single_cats}

    def _setup_goal(self) -> None:
        """Genre-Meister: X Genres mit je mindestens K erratenen Anime. Bei zu wenig passenden Genres wird X gesenkt."""
        self.gm_genres = self.options.genre_master_genres.value
        self.gm_anime = self.options.genre_master_anime.value
        if self.options.goal.value != self.options.goal.option_genre_master:
            return
        counts = {g: sum(g in a["genres"] for a in self.selected) for g in GENRES}
        while self.gm_anime > 1 and not any(v >= self.gm_anime for v in counts.values()):
            self.gm_anime -= 1
        possible = sum(v >= self.gm_anime for v in counts.values())
        if possible < self.gm_genres:
            logging.warning(f"Animepelago ({self.player_name}): Genre Master braucht {self.gm_genres} Genres mit je "
                            f"{self.gm_anime} Anime, es gibt nur {possible}. Wird auf {possible} gesenkt.")
            self.gm_genres = max(1, possible)

    def _genre_master_done(self, genres: set, single: dict) -> bool:
        counts: dict[str, int] = {}
        for a in self.selected:
            if self._open(a, genres, single):
                for g in a["genres"]:
                    counts[g] = counts.get(g, 0) + 1
        return sum(v >= self.gm_anime for v in counts.values()) >= self.gm_genres

    def _from_slot_data(self, sd: dict) -> None:
        """Fuer den Universal Tracker: Einstellungen, Anime und Start-Items aus den slot_data uebernehmen."""
        # Der Tracker muss dieselbe Anime-Datenbank haben wie der Server, sonst passen die Regeln nicht.
        if sd.get("data_version") != DATA_VERSION:
            raise OptionError(f"Animepelago: Diese Welt wurde mit Datenbank-Version {sd.get('data_version')} erzeugt, "
                              f"installiert ist Version {DATA_VERSION}. Bitte dieselbe .apworld wie der Host benutzen.")
        missing = [i for i in sd.get("anime", []) if i not in ANIME_BY_ID]
        if missing:
            raise OptionError(f"Animepelago: {len(missing)} Anime dieser Welt fehlen in der installierten .apworld. "
                              "Bitte dieselbe .apworld wie der Host benutzen.")
        mode = sd.get("unlock_mode", "both")
        self.use_genres = mode in ("genres", "both")
        self.use_letters = mode in ("letters", "both")
        self.extras = [c for c in sd.get("extra_unlocks", []) if c in EXTRA_CATEGORIES]
        self.single_cats = (["letter"] if self.use_letters else []) + self.extras
        self.any_rule = sd.get("genre_rule", "any") == "any"
        try:
            self.genre_step = int(sd.get("genre_step", 0))
        except (TypeError, ValueError):
            self.genre_step = 0
        self.use_demographics = bool(sd.get("demographics", False))
        self.only_genres = set(g for g in sd.get("only_genres", []) if g in GENRES)
        self.display_language = sd.get("title_language", "english")
        self.language = sd.get("letter_language", "english")
        self.letter_override = {int(k): v for k, v in sd.get("letters", {}).items() if v in LETTERS}
        self.selected = [dict(ANIME_BY_ID[i], genres=ANIME_BY_ID[i]["genres"] + (
            ANIME_BY_ID[i].get("demographics", []) if self.use_demographics else [])) for i in sd["anime"]]
        self.start_genres = set(g for g in sd.get("start_genres", []) if g in GENRES)
        self.start_single = {c: set(sd.get("start_letters", []) if c == "letter" else sd.get("start_extra", {}).get(c, []))
                             for c in self.single_cats}
        self.milestones = [n for n in sd.get("milestones", []) if n in MILESTONES]
        self.goal_count = int(sd.get("anime_goal", len(self.selected)))
        goal = self.options.goal
        goal.value = {"anime": goal.option_anime, "exodia": goal.option_exodia,
                      "genre_master": goal.option_genre_master}.get(sd.get("goal"), goal.option_anime)
        self.gm_genres = sd.get("genre_master_genres", 0)
        self.gm_anime = sd.get("genre_master_anime", 0)
        self.options.anime_count.value = len(self.selected)
        self._finish_setup()

    def letter_of(self, anime: dict) -> str:
        override = getattr(self, "letter_override", None)
        if override and anime["id"] in override:
            return override[anime["id"]]
        # Falls es fuer die Sprache keinen Buchstaben gibt: Englisch, sonst "#"
        letters = anime["letter"]
        return letters.get(self.language) or letters.get("english") or "#"

    def value_of(self, anime: dict, cat: str):
        """Wert eines Anime in einer Einzelwert-Kategorie (None = unbekannt, zaehlt dann nicht)."""
        return self.letter_of(anime) if cat == "letter" else (anime.get("cat") or {}).get(cat)

    def single_item(self, cat: str, value: str) -> str:
        return letter_item(value) if cat == "letter" else extra_item(cat, value)

    def _genres_ok(self, anime: dict, genres: set) -> bool:
        if not anime["genres"]:
            return True  # nur only_genres-Genres: beim Genre immer offen
        if self.any_rule:
            return sum(g in genres for g in anime["genres"]) >= self.genres_needed(anime)
        return all(g in genres for g in anime["genres"])

    def genres_needed(self, anime: dict) -> int:
        """Bei "any": wie viele Genres ein Anime braucht. Pro genre_step Genres eins mehr (6: 1-5 -> 1, 6-11 -> 2, 12+ -> 3)."""
        n = len(anime["genres"])
        return max(1, min(n, 1 + n // self.genre_step)) if self.genre_step else 1

    def _open(self, anime: dict, genres: set, single: dict, cats=None) -> bool:
        if self.use_genres and not self._genres_ok(anime, genres):
            return False
        for cat in self.single_cats if cats is None else cats:
            value = self.value_of(anime, cat)
            if value is not None and value not in single[cat]:
                return False
        return True

    def _count_open(self, genres: set, single: dict, cats=None) -> int:
        return sum(1 for a in self.selected if self._open(a, genres, single, cats))

    def _owned(self, state) -> tuple[set, dict]:
        genres = {g for g in self.used_genres if state.has(genre_item(g), self.player)}
        single = {c: {v for v in self.used_single[c] if state.has(self.single_item(c, v), self.player)}
                  for c in self.single_cats}
        return genres, single

    # ---------- Orte ----------

    def create_regions(self) -> None:
        menu = Region("Menu", self.player, self.multiworld)
        for a in self.selected:
            menu.locations.append(AnimepelagoLocation(self.player, a["name"], LOCATION_ID_OFFSET + a["id"], menu))
        for n in self.milestones:
            name = milestone_name(n)
            menu.locations.append(AnimepelagoLocation(self.player, name, self.location_name_to_id[name], menu))
        goal = AnimepelagoLocation(self.player, "Goal", None, menu)
        goal.place_locked_item(AnimepelagoItem("Victory", ItemClassification.progression, None, self.player))
        menu.locations.append(goal)
        self.multiworld.regions.append(menu)

    # ---------- Items ----------

    def create_item(self, name: str) -> AnimepelagoItem:
        code, classification, _ = ITEMS[name]
        if name in EXODIA_PIECES and self.options.goal.value == self.options.goal.option_exodia:
            classification = ItemClassification.progression
        if name == "Death Note" and self.options.death_link:
            classification = ItemClassification.trap  # sendet beim Empfang einen DeathLink
        return AnimepelagoItem(name, classification, code, self.player)

    def get_filler_item_name(self) -> str:
        return FILLER_ITEM

    def create_items(self) -> None:
        for g in sorted(self.start_genres, key=GENRES.index):
            self.multiworld.push_precollected(self.create_item(genre_item(g)))
        for c in self.single_cats:
            for v in sorted(self.start_single[c]):
                self.multiworld.push_precollected(self.create_item(self.single_item(c, v)))

        slots = len(self.selected) + len(self.milestones)
        required = [genre_item(g) for g in self.used_genres if g not in self.start_genres]
        required += [self.single_item(c, v) for c in self.single_cats for v in self.used_single[c]
                     if v not in self.start_single[c]]
        exodia_goal = self.options.goal.value == self.options.goal.option_exodia
        if exodia_goal:
            required += EXODIA_PIECES

        if len(required) > slots:
            # Zu wenige Checks fuer alle Genres/Buchstaben: die ueberzaehligen gibt es von Anfang an.
            unlock_names = {self.single_item(c, v): (c, v) for c in self.single_cats for v in self.used_single[c]}
            unlocks = [r for r in required if r.startswith("Genre: ") or r in unlock_names]
            surplus = len(required) - slots
            if surplus > len(unlocks):
                raise OptionError(f"Animepelago ({self.player_name}): Anime Count ist zu klein fuer das Exodia-Ziel.")
            self.random.shuffle(unlocks)
            for name in unlocks[:surplus]:
                self.multiworld.push_precollected(self.create_item(name))
                if name.startswith("Genre: "):
                    self.start_genres.add(name[len("Genre: "):])
                else:
                    c, v = unlock_names[name]
                    self.start_single[c].add(v)
                required.remove(name)
            logging.warning(f"Animepelago ({self.player_name}): {surplus} Freischalt-Items als Start-Items "
                            f"gegeben, weil Anime Count zu klein ist.")

        pool = [self.create_item(n) for n in required]
        free = slots - len(pool)

        # Optionale Spezial-Items in dieser Reihenfolge, solange Platz ist
        optional: list[tuple[str, int, bool]] = []  # (Name, Anzahl, nur komplett)
        # Geass zuerst (vom Spieler gewaehlt), hoechstens 10 % der Anime
        geass = min(self.options.geass_items.value, len(self.selected) // 10)
        if geass < self.options.geass_items.value:
            logging.info(f"Animepelago ({self.player_name}): Geass Items auf {geass} begrenzt "
                            f"(hoechstens 10 % von {len(self.selected)} Anime).")
        if geass:
            optional.append(("Geass", geass, False))
        if self.options.stand_arrow_items.value:
            optional.append(("Stand Arrow", self.options.stand_arrow_items.value, False))
        if self.options.perk_items:
            optional += [("Dragon Ball", 7, True), ("Senzu Bean", 3, False), ("Time Leap", 3, False),
                         ("Sukuna's Finger", 20, False)]
        optional += [("Death Note", 1, False)]  # immer dabei: Filler, mit DeathLink eine Falle
        if self.options.trap_items:
            optional += [("Kira's Hand", 5, False), ("Isekai Truck", 3, False), ("Filler Arc", 3, False),
                         ("Tsundere", 3, False)]
        if not exodia_goal:
            optional += [(p, 1, False) for p in EXODIA_PIECES]
        for name, amount, whole in optional:
            if whole and free < amount:
                continue
            take = min(amount, free)
            pool += [self.create_item(name) for _ in range(take)]
            free -= take

        # Clow Cards zum Sammeln (ohne Wirkung): etwa ein Drittel der freien Plaetze, hoechstens 53 wie im Original
        self.clow_cards = min(CLOW_CARD_MAX, free // 3)
        pool += [self.create_item(CLOW_CARD) for _ in range(self.clow_cards)]
        free -= self.clow_cards
        # Rest: meist "Filler Episode", etwa jedes vierte Mal ein Spass-Fueller (AYAYA!, Waifu ...) ohne Wirkung
        random_flavor = [f for f in FLAVOR_FILLERS if f != CLOW_CARD]
        pool += [self.create_item(self.random.choice(random_flavor) if self.random.random() < 0.25 else FILLER_ITEM)
                 for _ in range(free)]
        self.multiworld.itempool += pool
        # Fuer den Client: wie viele davon wirklich im Spiel sind (alle gefunden -> Spezial-Perk)
        self.perk_counts = {name: sum(1 for i in pool if i.name == name)
                            for name in ("Sukuna's Finger", "Dragon Ball", "Kira's Hand", "Death Note", "Geass", "Stand Arrow",
                                         "Senzu Bean", "Time Leap", "Isekai Truck", "Filler Arc", "Tsundere")}

    # ---------- Regeln ----------

    def set_rules(self) -> None:
        player = self.player
        for a in self.selected:
            location = self.get_location(a["name"])
            genres = [genre_item(g) for g in a["genres"]] if self.use_genres else []
            # Einzelwerte (Buchstabe, Jahr, ...): man braucht jeweils genau dieses Item
            singles = [self.single_item(c, v) for c in self.single_cats if (v := self.value_of(a, c)) is not None]
            if not genres:
                rule = lambda state, s=singles: state.has_all(s, player)
            elif self.any_rule:
                need = self.genres_needed(a)
                rule = lambda state, g=genres, s=singles, n=need: state.has_all(s, player) and state.has_from_list(g, player, n)
            else:
                rule = lambda state, g=genres, s=singles: state.has_all(s, player) and state.has_all(g, player)
            set_rule(location, rule)

        # Schnelle Logik fuer Meilensteine und Ziel: Vorher pro Anime festhalten, welche Items er braucht.
        # Dann wird pro Logik-Zustand nur EINMAL gezaehlt und das Ergebnis gemerkt (Zwischenspeicher).
        # Ohne das wurde die Erzeugung bei vielen Anime (z. B. 900 mit allen Kategorien) extrem langsam.
        self._prepare_fast_rules()
        for n in self.milestones:
            set_rule(self.get_location(milestone_name(n)), lambda state, n=n: self._fast_count(state) >= n)

        if self.options.goal.value == self.options.goal.option_exodia:
            set_rule(self.get_location("Goal"), lambda state: state.has_all(EXODIA_PIECES, player))
        elif self.options.goal.value == self.options.goal.option_genre_master:
            set_rule(self.get_location("Goal"), lambda state: self._fast_genre_master(state))
        else:
            set_rule(self.get_location("Goal"), lambda state: self._fast_count(state) >= self.goal_count)
        self.multiworld.completion_condition[player] = lambda state: state.has("Victory", player)

    def _prepare_fast_rules(self) -> None:
        """Pro Anime: welche Einzel-Items er braucht, welche Genre-Items er hat und wie viele davon noetig sind."""
        self._table = []
        names = set()
        for a in self.selected:
            singles = frozenset(self.single_item(c, v) for c in self.single_cats if (v := self.value_of(a, c)) is not None)
            genres = tuple(genre_item(g) for g in a["genres"]) if self.use_genres else ()
            if not genres:
                need = 0
            elif self.any_rule:
                need = self.genres_needed(a)
            else:
                need = len(genres)
            self._table.append((singles, genres, need, tuple(a["genres"])))
            names |= singles
            names.update(genres)
        self._unlock_names = tuple(sorted(names))
        self._cache: dict[frozenset, tuple[int, bool]] = {}

    def _fast_evaluate(self, state) -> tuple[int, bool]:
        """Zaehlt offene Anime und prueft das Genre-Meister-Ziel fuer einen Logik-Zustand (mit Zwischenspeicher)."""
        owned = frozenset(n for n in self._unlock_names if state.has(n, self.player))
        hit = self._cache.get(owned)
        if hit is not None:
            return hit
        count = 0
        per_genre: dict[str, int] = {}
        for singles, genres, need, raw_genres in self._table:
            if singles and not singles <= owned:
                continue
            if need and sum(g in owned for g in genres) < need:
                continue
            count += 1
            for g in raw_genres:
                per_genre[g] = per_genre.get(g, 0) + 1
        gm = sum(v >= self.gm_anime for v in per_genre.values()) >= self.gm_genres
        if len(self._cache) > 50000:  # Speicher begrenzen
            self._cache.clear()
        self._cache[owned] = (count, gm)
        return count, gm

    def _fast_count(self, state) -> int:
        return self._fast_evaluate(state)[0]

    def _fast_genre_master(self, state) -> bool:
        return self._fast_evaluate(state)[1]

    # ---------- Daten fuer den Client ----------

    def fill_slot_data(self) -> dict[str, Any]:
        return {
            "data_version": DATA_VERSION,
            "anime": sorted(a["id"] for a in self.selected),
            "location_offset": LOCATION_ID_OFFSET,
            "milestones": self.milestones,
            "goal": ["anime", "exodia", "genre_master"][self.options.goal.value],
            "genre_master_genres": self.gm_genres,
            "genre_master_anime": self.gm_anime,
            "trap_link": bool(self.options.trap_link.value),
            "anime_goal": self.goal_count,
            # Tatsaechlicher Modus ("none" = nur die Zusatz-Kategorien, z. B. bei Only Genres)
            "unlock_mode": "both" if self.use_genres and self.use_letters else "genres" if self.use_genres
                           else "letters" if self.use_letters else "none",
            "title_language": self.display_language,  # Anzeige im Client
            "letter_language": self.language,         # Quelle der Anfangsbuchstaben
            "genre_rule": "any" if self.any_rule else "all",
            "genre_step": self.genre_step,
            "demographics": self.use_demographics,
            "only_genres": sorted(self.only_genres, key=GENRES.index),
            "start_genres": sorted(self.start_genres, key=GENRES.index),
            "start_letters": sorted(self.start_single.get("letter", set()), key=LETTERS.index),
            # Zusatz-Kategorien: welche aktiv sind, Start-Werte und die Werte jedes Anime im Spiel
            "extra_unlocks": self.extras,
            "start_extra": {c: sorted(self.start_single[c]) for c in self.extras},
            "extra_values": {str(a["id"]): {c: self.value_of(a, c) for c in self.extras} for a in self.selected},
            # Anfangsbuchstabe jedes Anime im Spiel, damit der Client dieselbe Zuordnung nutzt
            "letters": {str(a["id"]): self.letter_of(a) for a in self.selected},
            "death_link": bool(self.options.death_link.value),
            # Anzahl der Spezial-Items im Spiel. Alle Sukuna-Finger -> Domain Expansion (ein Anime nach Wahl
            # gilt als erraten), alle Dragon Balls -> ein Genre nach Wahl.
            "sukuna_fingers": self.perk_counts["Sukuna's Finger"],
            "dragon_balls": self.perk_counts["Dragon Ball"],
            "geass": self.perk_counts["Geass"],
            "stand_arrows": self.perk_counts["Stand Arrow"],
            "clow_cards": getattr(self, "clow_cards", 0),  # Sammel-Karten ohne Wirkung (Anzeige x/N)
        }
