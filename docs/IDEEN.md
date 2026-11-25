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


### Hauptfeature: Guess the Anime Character
- [ ] **Wer ist das?** – ein Charakter wird gezeigt, du errätst seinen Namen (oder den Anime, je nach Modus)
  - Bild startet stark verpixelt / als Silhouette / als kleiner Ausschnitt und wird mit jedem Fehlversuch klarer
  - dazu Text-Hinweise der Reihe nach: Anime-Genre → Rolle (Haupt-/Nebenfigur) → Geschlecht → Anime → Anfangsbuchstabe
  - **Endlos** mit Serie, **auf Zeit**, und ein **Tagesrätsel** (für alle gleich, Ergebnis zum Teilen wie Animedle)
  - Antwort zählt mit Vor- oder Nachname, Spitzname, japanischer Schreibweise, kleine Tippfehler okay
  - Vorschläge beim Tippen wie bei Animedle (Name + Anime + Bild klein)
- [ ] **Characterdle** – wie Animedle, aber für Figuren: Anime, Geschlecht, Rolle, Haarfarbe, Alter, Beliebtheit, Jahr des Anime …
  (welche Spalten gehen, hängt von den Daten ab)
- [ ] **Erkenne den Anime an der Figur** – Figur wird gezeigt, du nennst den Anime (leichter Einstieg)

### Weitere Charakter-Spiele
- [ ] **Anime-Draft** (Party): reihum Figuren für ein Team wählen (z. B. „stärkstes Team“), dann abstimmen
- [ ] **Anime-Tabu** (Party): Anime erklären, ohne die Namen der Hauptfiguren zu sagen
- [ ] **Charakter-Blind-Ranking** (Party): Figuren blind auf Plätze 1–N setzen
- [ ] **Silhouetten-Buzzer** (Party): wer die Figur zuerst erkennt, buzzert
- [ ] **Smash or Pass / Wer würde gewinnen?** (Party, Abstimmung) – nur zum Spaß, keine Wertung
- [ ] Charaktere im **Bingo** als neue Kategorie (z. B. „hat eine Figur mit blauen Haaren“) – nur wenn die Daten es hergeben

### Archipelago
- [ ] **Waifupelago** = Option von Animepelago (dieselbe APWorld, kein eigenes Spiel):
  YAML-Option z. B. `waifupelago: off / on / mixed` → Figuren statt/zusätzlich zu Anime raten
  - Anzeigename im Client umschaltbar auf **Husbandopelago** (⚙️ Einstellungen, **nur der Name**)
  - welche Figuren kommen, ist eine **eigene YAML-Option**, z. B. `character_gender: all / female / male`
    (braucht Geschlecht in den Daten; Figuren ohne Angabe nur bei `all`)
- [ ] Option `character_checks`: zu jedem Anime zusätzlich 1–3 Hauptfiguren als Checks (Figur erraten = Check)
- [ ] Charakter-Karten als sammelbare Füller (wie Clow Cards), mit Album im Client
- [ ] neues Ziel: „Erkenne N Figuren“

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
