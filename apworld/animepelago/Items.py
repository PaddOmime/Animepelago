from BaseClasses import Item, ItemClassification

from .data import BASE_GENRES, CATEGORIES, DEMOGRAPHICS, GENRES, LETTERS

GAME = "Animepelago"

# Eigener ID-Bereich, damit sich nichts mit anderen Spielen ueberschneidet.
# Bleibt unter 2^53, damit auch JavaScript-Clients die Zahlen exakt lesen koennen.
ITEM_ID_OFFSET = 7_417_000_000


def genre_item(genre: str) -> str:
    return f"Genre: {genre}"


def letter_item(letter: str) -> str:
    return f"Letter: {letter}"


# Waifupelago: Figuren eines Anime sind erratbar, wenn man eins der "Characters: <Genre>"-Items seiner Genres hat
# und genug "Progressive Rarity" (erst die seltensten Figuren, zuletzt die bekanntesten).
def character_item(genre: str) -> str:
    return f"Characters: {genre}"


PROGRESSIVE_RARITY = "Progressive Rarity"
CHARACTER_CARD = "Character Card"


# Zusatz-Kategorien: Schluessel -> (Name im Item, ID-Bereich). Bereiche nie aendern.
EXTRA_CATEGORIES = {"year": ("Year", 600), "source": ("Source", 700), "season": ("Season", 750), "studio": ("Studio", 800)}


def extra_item(category: str, value: str) -> str:
    return f"{EXTRA_CATEGORIES[category][0]}: {value}"


EXODIA_PIECES = [
    "Exodia the Forbidden One",
    "Right Arm of the Forbidden One",
    "Left Arm of the Forbidden One",
    "Right Leg of the Forbidden One",
    "Left Leg of the Forbidden One",
]

# Name -> (ID, Standard-Klasse, Anzahl im Pool). Die Anzahl gilt fuer die Spezial-Items.
# IDs niemals aendern oder neu vergeben, nur hinten anhaengen.
ITEMS: dict[str, tuple[int, ItemClassification, int]] = {}

for _i, _g in enumerate(GENRES):
    ITEMS[genre_item(_g)] = (ITEM_ID_OFFSET + _i, ItemClassification.progression, 1)

ITEMS.update({
    # Hilfreich (die Wirkung steckt im Client)
    # Sukuna's Finger: deckt einen Hinweis zu einem Anime auf ("Fuer Anime #17 wurde aufgedeckt: ...").
    # Alle Finger im Spiel gefunden -> Domain Expansion: ein Anime nach Wahl gilt als erraten.
    "Sukuna's Finger": (ITEM_ID_OFFSET + 100, ItemClassification.useful, 20),
    # Dragon Ball: sind alle 7 da, darf man ein Genre nach Wahl freischalten (die Logik verlaesst sich nicht darauf)
    "Dragon Ball":     (ITEM_ID_OFFSET + 101, ItemClassification.useful, 7),
    # Geass: ein Anime nach Wahl gilt sofort als erraten (auch gesperrte). Anzahl per YAML (geass_items).
    "Geass":           (ITEM_ID_OFFSET + 102, ItemClassification.useful, 10),
    # Stand Arrow: deckt bei einem Anime nach Wahl alle Infos auf (Jahr, Studio, Folgen, Cover ...). Anzahl per YAML.
    "Stand Arrow":     (ITEM_ID_OFFSET + 103, ItemClassification.useful, 10),
    # Senzu-Bohne: hebt auf Knopfdruck alle laufenden Fallen-Wirkungen auf
    "Senzu Bean":      (ITEM_ID_OFFSET + 104, ItemClassification.useful, 3),
    # Time Leap: die naechste Falle geht daneben (passiver Schutz)
    "Time Leap":       (ITEM_ID_OFFSET + 105, ItemClassification.useful, 3),
    # Falle: Kira's Hand sperrt 60 Sekunden lang ein zufaelliges Genre
    "Kira's Hand":     (ITEM_ID_OFFSET + 200, ItemClassification.trap, 5),
    # Death Note: Filler; mit DeathLink eine Falle, die einen DeathLink sendet (siehe create_item)
    "Death Note":      (ITEM_ID_OFFSET + 201, ItemClassification.filler, 1),
    # Weitere Fallen: Isekai-Truck mischt die Felder, Filler Arc blendet Hinweise aus, Tsundere lehnt Antworten ab
    "Isekai Truck":    (ITEM_ID_OFFSET + 202, ItemClassification.trap, 3),
    "Filler Arc":      (ITEM_ID_OFFSET + 203, ItemClassification.trap, 3),
    "Tsundere":        (ITEM_ID_OFFSET + 204, ItemClassification.trap, 3),
    # Fueller
    "Filler Episode":  (ITEM_ID_OFFSET + 300, ItemClassification.filler, 0),
})

# Spass-Fueller ohne Wirkung (nur zur Auflockerung). Nummern 301 ff. -- nur hinten anhaengen, nie umsortieren!
FLAVOR_FILLERS = [
    "AYAYA!",
    "Ara Ara",
    "Nya!",
    "Gum-Gum Fruit",
    "Flame-Flame Fruit",
    "Usopp's Slingshot",
    "Nami's Clima-Tact",
    "Waifu",
    "Zangetsu",
    "Hogyoku",
    "Cursed Technique Lapse: Blue",
    "Cursed Technique Reversal: Red",
    "Hollow Purple",
    "Philosopher's Stone",
    "Husbando",
    "Straw Hat",
    "Sogeking's Mask",
    "Naruto's Headband",
    "Gojo's Blindfold",
    "Tanjiro's Hanafuda Earrings",
    "Inosuke's Boar Mask",
    "Saitama's Gloves",
    "Survey Corps Cloak",
    "3D Maneuver Gear",
    "Den Den Mushi",
    "Going Merry",
    "Thousand Sunny",
    "NerveGear",
    "My name is Sogeking! Born on Sniper Island, 100 shots, 100 hits!",
    "Nico Nico Nii",
    "Moon Prism Power, Make Up!",
    "Tuxedo Mask's Top Hat",
    "Yowai mo",
    "Omae wa mou shindeiru",
    "Nani?!",
    "Hisashiburi da na, Mugiwara",
    "ORA ORA ORA",
    "MUDA MUDA MUDA",
    "Daisukiiiiii",
    "The One Piece is REAL!",
    "Have a Plus Ultra Day",
    "Clow Card",
]
# Die Clow Card ist ein Sammel-Fueller: Je nach Weltgroesse bis zu 53 Stueck (wie im Original)
CLOW_CARD = "Clow Card"
CLOW_CARD_MAX = 53
for _i, _name in enumerate(FLAVOR_FILLERS):
    ITEMS[_name] = (ITEM_ID_OFFSET + 301 + _i, ItemClassification.filler, 0)

for _i, _l in enumerate(LETTERS):
    ITEMS[letter_item(_l)] = (ITEM_ID_OFFSET + 500 + _i, ItemClassification.progression, 1)

for _cat, (_label, _offset) in EXTRA_CATEGORIES.items():
    for _i, _v in enumerate(CATEGORIES.get(_cat, [])):
        ITEMS[extra_item(_cat, _v)] = (ITEM_ID_OFFSET + _offset + _i, ItemClassification.progression, 1)

# Sicherheitsnetz: Jede Zusatz-Kategorie hat einen festen ID-Bereich. Hat eine Liste zu viele Werte,
# wuerde sie in den naechsten Bereich hineinragen. Dann lieber sofort einen klaren Fehler.
_ranges = sorted(o for _, o in EXTRA_CATEGORIES.values()) + [1000]
for _cat, (_label, _offset) in EXTRA_CATEGORIES.items():
    _room = _ranges[_ranges.index(_offset) + 1] - _offset
    assert len(CATEGORIES.get(_cat, [])) <= _room, f"Zu viele Werte fuer {_label}: {len(CATEGORIES[_cat])} > {_room}"

for _i, _piece in enumerate(EXODIA_PIECES):
    # Klasse haengt vom Spielmodus ab (Exodia-Ziel: progression, sonst filler), siehe create_item.
    ITEMS[_piece] = (ITEM_ID_OFFSET + 400 + _i, ItemClassification.filler, 1)

# Waifupelago (ab 2.0): Bereich 1000 ff.
for _i, _g in enumerate(BASE_GENRES):
    ITEMS[character_item(_g)] = (ITEM_ID_OFFSET + 1000 + _i, ItemClassification.progression, 1)
ITEMS[PROGRESSIVE_RARITY] = (ITEM_ID_OFFSET + 1100, ItemClassification.progression, 0)
ITEMS[CHARACTER_CARD] = (ITEM_ID_OFFSET + 1101, ItemClassification.filler, 0)

# Keine zwei Items duerfen dieselbe ID haben
assert len({v[0] for v in ITEMS.values()}) == len(ITEMS), "Doppelte Item-IDs"

item_name_to_id: dict[str, int] = {name: data[0] for name, data in ITEMS.items()}

item_name_groups: dict[str, set[str]] = {
    "Genres": {genre_item(g) for g in GENRES},
    "Demographics": {genre_item(g) for g in DEMOGRAPHICS},
    "Letters": {letter_item(l) for l in LETTERS},
    "Exodia": set(EXODIA_PIECES),
    **{_label + "s": {extra_item(_cat, v) for v in CATEGORIES.get(_cat, [])} for _cat, (_label, _) in EXTRA_CATEGORIES.items()},
    "Traps": {"Kira's Hand", "Death Note", "Isekai Truck", "Filler Arc", "Tsundere"},
    "Perks": {"Sukuna's Finger", "Dragon Ball", "Geass", "Stand Arrow", "Senzu Bean", "Time Leap"},
    "Fillers": {"Filler Episode", *FLAVOR_FILLERS, CHARACTER_CARD},
    "Character Unlocks": {character_item(g) for g in BASE_GENRES} | {PROGRESSIVE_RARITY},
}

FILLER_ITEM = "Filler Episode"


class AnimepelagoItem(Item):
    game = GAME
