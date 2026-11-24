# Profil-Format (Export/Import)

Profile liegen im Browser (localStorage). Mit **Profil → Als Datei speichern / Als Code kopieren**
werden sie exportiert. Der Code ist dieselbe JSON-Datei, nur als `AP1-` + Base64 (UTF-8).

Das Format ist so gebaut, dass ein späterer Server (Konten mit Passwort) dieselben Dateien
übernehmen kann: Das Profil hat eine feste `id`, eine Versionsnummer `v` und enthält **keine**
Passwörter. Ein Server würde beim ersten Login die Datei hochladen lassen, sie genauso prüfen
wie der Client (`clean`/`cleanData` in `client/index.html`) und das Profil dem Konto zuordnen.
Das Passwort-Hashing (Argon2/bcrypt) gehört dann allein auf den Server.

```json
{
  "format": "animepelago-profile",
  "v": 1,
  "app": "0.2.0",
  "exported": "2026-11-23T10:00:00.000Z",
  "profile": {
    "id": "p_abc123def456",          // fest, 10–24 Zeichen [a-z0-9] nach "p_"
    "name": "Padd",                  // max. 24 Zeichen
    "created": "…", "updated": "…",  // ISO-Zeit
    "xp": 919,                       // alle EP insgesamt
    "routes": {"ninja": 99000, "saiyan": 142},  // EP je Route (max. 99.000 = Level 100)
    "route": "saiyan",               // aktive Route (null = keine gewählt / gerade voll)
    "lastRoute": "saiyan",
    "title": "ninja:9",              // gewählter Titel = Route:Rang (0-9), null = automatisch
    "stats": { "g": 14, "gGenre": {"Action": 5}, … },   // nur Zahlen (eine Ebene Unterobjekte)
    "ach": { "guess1": "2026-11-23T…" },                 // Erfolg-ID -> Zeitpunkt
    "lastDay": "2026-11-23", "lastExport": "…"
  },
  "data": {                           // Rekorde der Spiele für dieses Profil
    "scores":  [ {done, total, time, helps, pool, goal, mode, date} ],   // Offline-Siege
    "hangman": {streak, solved},
    "top100":  { "<Liste>": {found:[ids], ms, gaveUp, best} },
    "bingo":   {score, full},
    "wordsalad": {streak, best, solved, timedBest},
    "animedle": {played, won, streak, best, lastWin, eStreak, eSolved, daily: {date, guesses:[ids], over, won}}
  }
}
```

Regeln beim Import:
- `format` muss stimmen, `v` darf nicht neuer als der Client sein (sonst „ungültig“).
- Alles wird geprüft und begrenzt (Zahlen, Längen, Anzahl). Unbekannte Felder fallen weg.
- Gleiche `id` = dasselbe Profil → wird überschrieben (Sicherung zurückholen).
- Gleicher Name bei anderer `id` → Name bekommt „(2)“.

Nicht im Export: das laufende Offline-Spiel, die Bingo-Bestenliste nach Namen und die
Time-Attack-Zeiten (die gehören dem Gerät, nicht einem Profil).

Level einer Route: floor((1 + sqrt(1 + 0.4*EP)) / 2), höchstens 100. EP, die noch keiner Route
gehören (xp minus Summe der Routen), wandern in die nächste gewählte Route.

Neue Felder später: `v` erhöhen und im Client eine Umwandlung von älteren Versionen einbauen.
