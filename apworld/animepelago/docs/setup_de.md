# Animepelago Einrichtung

## Was du brauchst

- [Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases) **0.6.8 oder neuer** (nur zum Generieren –
  gespielt wird im Browser).
- `animepelago.apworld` und `Animepelago.yaml` aus den
  [Animepelago-Releases](https://github.com/PaddOmime/Animepelago/releases).
- Einen Browser (PC oder Handy). Sonst musst du nichts installieren: Das Spiel läuft unter
  **<https://paddomime.github.io/Animepelago/client/>**.

## 1. APWorld installieren

Doppelklick auf `animepelago.apworld` (der Archipelago Launcher installiert sie), oder kopiere die Datei in den Ordner
`custom_worlds` deiner Archipelago-Installation. Danach den Launcher neu starten.

## 2. YAML erstellen

- Nimm `Animepelago.yaml` aus dem Release (oder den Knopf **📄 Animepelago.yaml herunterladen** im Webclient),
  oder erstelle eine mit dem **Options Creator** im Archipelago Launcher.
- Trage deinen `name` ein und passe die Optionen an. Jede Option ist in der Datei erklärt; die wichtigsten sind
  `anime_count`, `anime_goal`, `unlock_mode`, `genre_rule` und `title_language`.

## 3. Generieren und hosten

Lege die YAMLs eurer Gruppe in den Ordner `Players`, starte im Launcher **Generate** und lade das Ergebnis auf
[archipelago.gg/uploads](https://archipelago.gg/uploads) hoch, um den Raum zu hosten.
Das Hosten auf archipelago.gg ist am einfachsten (siehe „Lokale Server“ unten).

## 4. Verbinden und spielen

1. Öffne **<https://paddomime.github.io/Animepelago/client/>**.
2. Gib im Reiter **Archipelago** den Server (z. B. `archipelago.gg`), den Port eures Raums, deinen Slot-Namen und,
   falls gesetzt, das Passwort ein. Dann **Verbinden** drücken.
3. Tippe Anime-Titel ins Ratefeld. Jeder bekannte Titel zählt (Englisch, Romaji, Japanisch, Deutsch, Spanisch,
   Französisch, Italienisch), kleine Tippfehler sind okay. Gesperrte Anime zeigen, welche Items ihnen noch fehlen.
4. Chat und Befehle (z. B. `!hint`) kommen ins Nachrichtenfeld unten.

Der Client merkt sich deine Verbindungsdaten. Bricht die Verbindung ab, verbindet er sich von selbst neu;
noch nicht gesendeter Fortschritt wird danach nachgeschickt.

## Lokale Server

Der Webclient läuft über https. Browser erlauben ihm deshalb nur **verschlüsselte** Verbindungen (`wss://`).
Räume auf archipelago.gg können das. Ein Server auf deinem eigenen PC meist nicht – dann lade den Client herunter
(den Ordner `client` aus dem Repository) und öffne `index.html` lokal.

## Gut zu wissen

- **DeathLink / TrapLink:** schaltest du mit `death_link` / `trap_link` in deiner YAML ein.
- **Collect:** Sammelt ein anderer Spieler seine Items aus deiner Welt ein, werden diese Anime mit 📦 markiert.
  Ein Schalter im Client entscheidet, ob sie für dein Ziel zählen.
- **Twitch-Chat** *(Vorschau)*: Mit dem Twitch-Knopf rät dein Chat mit. Sprecht vorher in eurer Multiworld ab,
  ob das okay ist.
- **Profile:** Lege ein Profil an (👤) und wähle eine Route – dann geben auch deine Archipelago-Spiele EP und Erfolge.
- **Probleme oder Ideen?** Schreib ein Issue auf [GitHub](https://github.com/PaddOmime/Animepelago/issues).
