# Ideen und Plan bis 1.0

Gemerkte Wuensche und Vorschlaege. Erledigtes wandert in den CHANGELOG.

## Naechste Schritte (Stand 23.11.)
- [ ] Review des neuen Codes (Profile, Import, Routen, Neuverbinden, Bingo-Modi) – geplant fuer Sonntag
- [ ] APWorld-Tests (Archipelago-Testsystem) + .bat zum Starten
- [ ] Firebase eintragen, pushen, Release 0.2.0 (heute Abend), Abgleich mit dem PC-Ordner
- [ ] Playtests (Paddo): Multiworld mit Neuverbinden und !hint, Time Attack im Discord, Profile/Routen, Handy

## Fuer 1.0 (wichtig)
- [x] TMDB-Logo und Hinweis im Client (0.2.0)
- [x] Erster echter Multiworld-Test (Persona 5 Royal, Banjo-Tooie, SM64, Animepelago): lief fluessig, Release/Collect ok
- [x] Option: eingesammelte (Collect) Anime zaehlen fuers Ziel, an/aus (0.2.0)
- [ ] Weitere Multiworld-Tests: Neuverbinden mitten im Spiel, Hinweise
- [x] Automatisch neu verbinden, wenn die Verbindung zum Server abbricht – 0.2.0 (im Browser mit Schein-Server getestet; echter Test in der nächsten Multiworld)
- [ ] Tests in der APWorld (Archipelago-Testsystem)

## Fuer 1.0 (sollte)
- [ ] Beispiel-YAMLs ("kurz und leicht", "nur ein Genre", "mit Fallen")
- [x] Farbenblind-Modus (Richtig/Falsch auch per Symbol) – 0.2.0
- [ ] Training-Unterlagen (offline/Training) auf den neuen Stand bringen

## Wuensche
- [x] **Profil im Offline-Modus:** sich einen eigenen Spielernamen geben (uebergeordnetes Profil), unter dem Offline-Spiele, Top-100-Fortschritt und Bestzeiten gespeichert werden
- [x] **Team-Modus im Bingo:** Team 1 gegen Team 2 statt nur Spieler gegen Spieler – 0.2.0
- [x] **Profile + Level + Erfolge (lokal, Weg A)** – 0.2.0, Export/Import serverfertig (docs/PROFIL_FORMAT.md)
- [ ] Später vielleicht: echte Konten mit Server (Weg B), dann Profil-Datei hochladen
- [x] **Bingo Time Attack** (5×5, allein/Team) – 0.2.0
- [ ] DeathLink (z. B. ein Fehlversuch, wenn ein anderer Spieler stirbt)
- [ ] Tipp-Hilfe: bei unbekannter Eingabe aehnliche Titel vorschlagen
- [ ] Top 100 als Archipelago-Ziel ("Errate 50 der Top 100 Action")
- [ ] Top-Listen: Mindestbekanntheit (z. B. 5.000 AniList-Nutzer), damit sehr unbekannte Titel wie *Kagirinaki Rakuen* nicht reinrutschen
- [ ] Kurzserien (corrections.json "short_series") gesammelt als Option anbieten

## Bingo (Wünsche der Kollegen)
- [x] Spielerzahl einstellbar: 2–6 Seiten, jede Spieler oder Team – 0.2.0
- [x] Zufalls- und Seed-Modus: Board-Code zum Teilen, Boards speichern, Bingo-Editor (Kategorien selbst anordnen) – 0.2.0
- [x] Risiko-Bingo 7×7–10×10 (freigeschaltet nach einem vollen 5×5, 🔥 bei 1–5 Lösungen, je 10 Einträge eine Räumung, Time Attack +5:00) – 0.2.0

## Chat rät mit (wichtig, nach 0.2.0)
- [x] **Twitch-Chat** (Fokus) – 0.2.0, Variante A gebaut (mit Schein-Chat getestet; echter Test im Stream): Chat ohne Konto/Server im Browser mitlesen (anonym), Kanalname eintragen
  - `!rate Titel` oder nur Titel (einstellbar); richtig + freigeschaltet = zählt, Log „erraten von X“, 💬 am Feld
  - Modus „Automatisch“ oder „Vorschläge“ (Streamer klickt an); Spam-Schutz (z. B. 1 Versuch / 5 s pro Zuschauer)
  - Chat-Bestenliste für den Stream; standardmäßig aus (Fairness in Multiworlds)
  - auch für Offline, Top 100 („Chat gegen Streamer“), später Party-Spiele
  - Bedienung (Paddos Wunsch): Knopf „Twitch-Integration“ → einrichten; danach **An/Aus-Schalter**
    (Ausschalten behält die Integration), **„Entfernen“** löscht sie; muss eine bestehende Integration neu
    angemeldet werden („Authenticate“), erscheint ein deutlicher Hinweis
  - Entschieden: **Variante A** – nur mitlesen, ohne Twitch-Anmeldung (Kanalname reicht). Hinweis-Leiste
    trotzdem einbauen (Kanal nicht gefunden / Verbindung getrennt). Später optional B: Twitch-Login, damit das
    Spiel im Chat antwortet („✅ X hat #12 erraten“, MVP) – dann Anmeldung prüfen und bei Ablauf Hinweis zeigen.
- YouTube-Chat: nicht geplant (Fokus Twitch)

## Party-Spiele (für den Kanal, zu dritt über Discord)
Technik: Firebase (Spark, kostenlos) für Live-Räume – Show-Ansicht wird im Discord geteilt, jeder hat einen
Controller am Handy/zweiten Fenster. Gemeinsame Spielerleiste (Namen frei eintragbar, Farben, wer dran ist,
verdeckt abgeben, gleichzeitig aufdecken, Punkte). Später: Konten über Firebase Authentication.
- [x] Grundgerüst: party.html (Raum, Show-Ansicht, Controller, Spielerleiste, Firebase über REST, Testmodus ohne Firebase)
- [ ] Firebase-Projekt anlegen (Paddo, Anleitung docs/FIREBASE_EINRICHTEN.md) und Adresse eintragen
- [x] Blind Ranking
- [x] Higher or Lower
- [ ] Anime-Pitch-Generator (Cover/Story zu gewürfeltem Fake-Anime, dann ranken)
- [ ] Silhouetten-Buzzer
- [ ] Animedle (eher solo)
- [ ] Anime-Tabu – verschoben auf 2.0 (mit Charakteren als verbotene Wörter)
- [ ] Anime-Draft – verschoben auf 2.0 (mit Charakteren)

## Roadmap nach 1.0
### 2.0 – Charaktere
- [ ] Charakter-Daten holen (Grundlage Wikidata (CC0), Lücken über Fandom (CC BY-SA, mit Quellenangabe,
      Liste getrennt unter CC BY-SA veröffentlichen); Rolle/Beliebtheit von AniList nur live, nicht speichern;
      Bilder nur live anzeigen). Erst zählen, wie viele unserer Anime auf Wikidata Charaktere haben.
- [ ] Anime-Draft mit Charakteren
- [ ] Anime-Tabu mit Hauptcharakteren als verbotene Wörter
- [ ] Weitere Ideen: „Wer ist der Charakter?“, Charakter-Blind-Ranking
- [ ] „Errate den Anime an Ort, Waffe, Aussehen …“: Hinweis-Karten als Text für die Top 300 (von schwer nach leicht,
      von Claude geschrieben, von Paddo & Co. gegengelesen) + Quiz-Editor für eigene Runden (Bild-Links, in Firebase;
      keine fremden Bilder speichern; Screenshots in Videos: Zitatrecht beachten)

### 3.0 – Openings
- [ ] AnimeThemes (api.animethemes.moe/api/...) – seit ca. 16.11.2026 503, abwarten
- [ ] fetch_animethemes.py auf neue Adressen (/api) bringen, Abdeckung zählen
- [ ] Opening-Quiz; Ausweichlösung prüfen (offizielle YouTube-Einbettungen)
- [ ] Hinweis für Videos auf dem Kanal: Musik ist urheberrechtlich geschützt (Content ID)

## Eigenes Projekt danach (NICHT Teil von Animepelago)
- [ ] **Videospiel-Guesser** (Name offen, z. B. Gamepelago / Pixelpelago) – nach Animepelago 3.0
  - eigenes Repo, eigene APWorld, eigene Seite (eigener Archipelago-Spielname)
  - Code von Animepelago als Kopie übernehmen (Raten, Offline, Profile, Minispiele, Party-Räume)
  - Kategorien z. B. Genre, Plattform, Entwickler, Jahrzehnt, Buchstabe; Reihen wie bei uns die Franchises
  - Datenquellen prüfen: Wikidata (CC0), IGDB (Nutzungsbedingungen vorher lesen)
  - passt zum Kanal-Format „Spiele-Cover designen und ranken“
  - Bild-Quiz ist hier leichter: IGDB (Screenshots, Artworks, Charaktere), Steam (Screenshots, Trailer),
    z. B. „Screenshot-Zoom“, „Erkenne das Spiel an der Figur“ – Nutzungsbedingungen für Bilder vorher prüfen

