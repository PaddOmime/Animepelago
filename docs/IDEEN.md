# Ideen und Plan

Gemerkte Wünsche und Vorschläge. Erledigtes wandert in den CHANGELOG.
**1.0 ist veröffentlicht (24.11.2026).** Alles, was bis dahin erledigt wurde, steht im CHANGELOG.

---

## 1.0.x – Kleinkram nach dem Release
- [ ] **Firebase aufräumen:** alte Party-Räume automatisch löschen – **zusammen machen**
- [ ] Wortsalat: Überspringen im 2-Minuten-Modus kostet evtl. 3 Sekunden (gegen „leichte Titel ausrollen“)
- [ ] Übersetzungen ES/FR/IT/JA von Muttersprachlern gegenlesen lassen
- [ ] **Twitch Variante B** (Spiel antwortet im Chat, „✅ X hat #12 erraten“, MVP) – nur wenn der Chat es will

## 2.0 – Charaktere 🧑‍🎤 und neues UI

### UI-Überarbeitung (Pflicht für 2.0)
- [ ] Erst sammeln: Was stört heute? (Screenshots, Handy und PC)
- [ ] **Plan (abgesegnet):**
  1. Start = 5 große Kacheln: 🌐 Archipelago · 🎮 Offline · 🧩 Minispiele · 🎉 Party · 👤 Profil
  2. Minispiele-Seite: eine Kachel pro Spiel (Symbol, ein Satz, Bestwert); Risiko-Bingo + Editor unter Bingo
  3. Einstellungen nur bei Bedarf: Standardwerte + großer „▶ Spielen“, Seltenes unter „⚙️ Mehr Optionen“
  4. feste Kopfzeile: ← Zurück · Modus · Profil/Sprache/⚙️ (Twitch, Farbenblind, Hell/Dunkel ins Einstellungsfenster)
  5. im Spiel nur das Spiel; Statistik/Erfolge im Ergebnis-Fenster
- [ ] einheitliches Design für alle Minispiele (Kopfzeile, Knöpfe, Ergebnis-Fenster, Teilen)
- [ ] Handy zuerst: große Tipp-Flächen, nichts läuft über den Rand
- [ ] Profil, Erfolge und Routen übersichtlicher (eigene Seite statt Fenster?)
- [ ] Hell/Dunkel, Farbenblind-Modus beibehalten; Schrift und Farben festlegen (kleines Design-System)
- [ ] Party-Seite (Show-Ansicht und Handy) im selben Stil
- [ ] Ablauf: erst Skizzen/Mockups, dann bauen – Bedienung der Archipelago-Verbindung darf sich nicht verschlechtern


### Figuren-Spiele (abgestimmt 26.11.)
- [ ] **Wer ist das?** (Hauptfeature): Bild verpixelt/Silhouette, wird mit jedem Fehlversuch klarer;
      Tagesrätsel, Endlos, auf Zeit. Bild nur live von AniList, nichts speichern.
  - Text-Hinweise der Reihe nach: Genre → Rolle → Geschlecht → Anime → Anfangsbuchstabe
  - Antwort zählt mit Vor-/Nachname, Spitzname, kleine Tippfehler okay; Vorschläge beim Tippen wie Animedle
- [ ] **Aus welchem Anime?**: Figur wird gezeigt, Anime nennen (leichter Einstieg)
- [ ] **Impostor**: 4 Figuren, 3 aus demselben Anime – finde den Impostor (kleine Among-Us-Anspielung im Text, keine fremden Grafiken)
- [ ] **Animedle-Option** „Anime / Figur raten“ (Characterdle); **Tagesrätsel bleibt Anime**
- [ ] **Wortsalat-Option** „Anime-Titel / Figurenname“
- [ ] **Figuren-Bingo** als eigener Modus: Felder = Anime, man trägt passende Figuren ein
- [ ] Bingo: neue Felder rund um Figuren (weibl. Hauptfigur, Name auf S, mehr als 50 Figuren …) – **alles als Optionen**, weiter ausbaubar
- nicht geplant: Higher or Lower mit Figuren, Japanischer Name, Tabu

### Party
- [ ] **Silhouetten-Buzzer**: wer die Figur zuerst erkennt, gewinnt die Runde
- [ ] **Anime-Draft**: reihum Figuren fürs Team wählen, dann abstimmen; mit Themen (Schwertkämpfer, Nahkämpfer …) – Themen brauchen eigene Daten, später ausbauen
- [ ] **Blind-Ranking**: Option „Anime / Figuren“
- [ ] **Wer würde gewinnen?** (Abstimmung, ohne Wertung)
- [ ] **Team oder Pass** (alle Figuren): „Würdest du die Figur in dein Abenteuer-Team holen?“ – Abstimmung, ohne Wertung
- [ ] **Smash or Pass** (eigener Modus): **nur Figuren, die im Werk sicher volljährig sind** – braucht Altersangaben
      (gleiche Quellenregel: offiziell > Wikidata > Fandom); Figuren ohne gesichertes Alter kommen nicht vor.
      Kein „stell dir vor, sie wäre 18“ für minderjährige Figuren.

### Archipelago (Waifupelago)
- [ ] Figuren als **Checks**, Figuren als **Hinweis-Items**, **Charakter-Karten** als Füller mit Album, Ziel **„Erkenne N Figuren“** (Filter Waifu/Husbando/alle)
- [ ] Option: Figuren eines Anime erst **freigeschaltet, wenn der Anime erraten** ist
- [ ] Option: Anime **und** Figuren gleichzeitig raten (gemischt)
- [ ] **Waifupelago** = Option von Animepelago (dieselbe APWorld): `waifupelago: off / on / mixed`
  - Anzeigename im Client umschaltbar auf **Husbandopelago** (nur der Name)
  - eigene Option `character_gender: [female, male, nonbinary]` (Standard alle; ohne Angabe nur bei „alle“)

### Regeln für Figuren-Daten
- [ ] **Was der Autor / das offizielle Werk sagt, gilt.** Reihenfolge: offizielle Angabe (Databook, Vivre Card, SBS,
  offizielle Seite, Interview) > Wikidata > Fandom. Abweichungen in eine Korrekturliste – **immer mit Quelle**, z. B.
  `"Yamato (One Piece)": {"gender": "f", "source": "Vivre Card, Sept. 2021", "note": "Tochter von Kaido, sieht sich als Oden"}`
- [ ] **Mehrere oder unklare Angaben werden IMMER von Hand geprüft** (`raw/figuren_pruefen.tsv`), erst dann ins Spiel
- [ ] **Nebenfiguren bleiben drin**, kommen aber seltener dran: sanfte Gewichtung nach Bekanntheit
      (Wikidata: Anzahl Wikipedia-Artikel; später evtl. AniList-Rolle live)
- [x] Datenstand (25.11.): ~18.000 Figuren; Top 300: 69 % mit Figuren; Geschlecht bei 55 %; 145 zu prüfen → Lücken mit Fandom füllen

### Glossar / Lexikon (Profil)
- [ ] Jeder erratene Anime und jede erratene Figur wird **ab sofort im Hintergrund** im Profil vermerkt
- [ ] Das Glossar selbst wird sichtbar, wenn man eine **Route geschafft** hat (Belohnung)
- [ ] Eintrag erst offen, wenn genau dieser Anime / diese Figur erraten wurde; vorher „???“
- [ ] nur Text-Daten (Name, Anime, Jahr …) gespeichert; Bilder live von AniList
- [ ] Lieblingsfigur als Avatar (Bild live), Erfolge („100 Figuren“, „Alle Strohhüte“), Sammelalbum = Teil des Glossars

### Profil
- [ ] neue Erfolge für Charakter-Spiele; eventuell eine 8. Route (z. B. „Isekai-Held“ oder „Idol“)

### Daten (zuerst klären!)
- [ ] **Abdeckung zählen:** Für wie viele unserer ~1.900 Anime gibt es brauchbare Figuren-Daten?
- [ ] **Quellen** (Lizenz beachten, nichts Fremdes ungeprüft speichern):
  - **Wikidata** (CC0): Figuren-Listen je Anime, oft mit Geschlecht – frei nutzbar
  - **aniSearch**: Figuren mit Namen in 6 Sprachen und Synchro-Status – **Anfrage per Mail läuft/geplant**
    (api@anisearch.com), erst nach Zustimmung nutzen
  - **AniList**: Rolle, Beliebtheit, Bilder – wie bisher nur **live** im Browser laden, nicht speichern
  - **Fandom** (CC BY-SA): Lücken füllen, dann mit Quellenangabe und die Liste getrennt unter CC BY-SA
- [ ] Bilder **nie** im Repo speichern, nur live von der Quelle anzeigen
- [ ] Zitate („Wer hat das gesagt?“) nur sehr vorsichtig (Urheberrecht) – eher weglassen

### Sonstiges für 2.0
- [ ] **Hinweis-Karten** „Errate den Anime an Ort, Waffe, Aussehen …“: Text-Hinweise für die Top 300 (von schwer nach leicht),
      von Paddo & Co. gegengelesen
- [ ] **Quiz-Editor** für eigene Runden (Bild-Links, in Firebase gespeichert; keine fremden Bilder speichern)
- [ ] Bingo-Kategorie „Hat eine deutsche Synchro“ (braucht aniSearch-Daten)
- [ ] Später: echte Konten über Firebase Authentication (Profil-Datei hochladen, Format steht schon in docs/PROFIL_FORMAT.md)

## 3.0 – Openings 🎵
- [ ] AnimeThemes (api.animethemes.moe/api/...) – seit ca. 16.11.2026 503, abwarten
- [ ] fetch_animethemes.py auf neue Adressen (/api) bringen, Abdeckung zählen
- [ ] Opening-Quiz; Ausweichlösung prüfen (offizielle YouTube-Einbettungen)
- [ ] Hinweis für Videos auf dem Kanal: Musik ist urheberrechtlich geschützt (Content ID)

## Weitere Wünsche (ohne feste Version)
- [ ] DeathLink-Variante: ein Fehlversuch, wenn ein anderer Spieler stirbt
- [ ] Top 100 als Archipelago-Ziel („Errate 50 der Top 100 Action“)
- [ ] Top-Listen: Mindestbekanntheit (z. B. 5.000 AniList-Nutzer), damit sehr unbekannte Titel nicht reinrutschen
- [ ] Kurzserien (corrections.json „short_series“) gesammelt als Option anbieten
- [ ] Beispiel-YAMLs („kurz und leicht“, „nur ein Genre“, „mit Fallen“)
- [ ] Party: Anime-Pitch-Generator (Cover/Story zu gewürfeltem Fake-Anime, dann ranken)

## Eigenes Projekt danach (NICHT Teil von Animepelago)
- [ ] **Videospiel-Guesser** (Name offen, z. B. Gamepelago / Pixelpelago) – nach Animepelago 3.0
  - eigenes Repo, eigene APWorld, eigene Seite (eigener Archipelago-Spielname)
  - Code von Animepelago als Kopie übernehmen (Raten, Offline, Profile, Minispiele, Party-Räume)
  - Kategorien z. B. Genre, Plattform, Entwickler, Jahrzehnt, Buchstabe; Reihen wie bei uns die Franchises
  - Datenquellen prüfen: Wikidata (CC0), IGDB (Nutzungsbedingungen vorher lesen)
  - Bild-Quiz ist hier leichter: IGDB (Screenshots, Artworks, Charaktere), Steam (Screenshots, Trailer) –
    Nutzungsbedingungen für Bilder vorher prüfen
