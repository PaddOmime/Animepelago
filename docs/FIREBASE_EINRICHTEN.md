# Firebase für die Party-Spiele einrichten (einmalig, ca. 10 Minuten)

Die Party-Spiele (`client/party.html`) brauchen einen kleinen Live-Speicher, damit Show-Ansicht und
Handys sich übers Internet abgleichen. Dafür nehmen wir die **Firebase Realtime Database** im
kostenlosen **Spark-Tarif** (keine Kreditkarte nötig, kann also nichts kosten).

Ohne Einrichtung laufen die Party-Spiele im **Testmodus**: nur auf einem Gerät mit mehreren Fenstern.

## Schritte

1. **Projekt anlegen**
   - <https://console.firebase.google.com> öffnen und mit deinem Google-Konto anmelden.
   - „Projekt hinzufügen“ (bzw. „Create a project“), Name z. B. `animepelago-party`.
   - Google Analytics: **aus** (brauchen wir nicht).

2. **Datenbank anlegen**
   - Links im Menü: „Build“ / „Erstellen“ → **Realtime Database** → „Datenbank erstellen“.
   - Standort: **Belgien (europe-west1)** – dann liegen die Daten in der EU.
   - Sicherheitsregeln: **„Im gesperrten Modus starten“** (locked mode).

3. **Regeln eintragen**
   - In der Realtime Database oben den Reiter **„Regeln“** öffnen.
   - Alles darin löschen und den Inhalt von `docs/firebase_rules.json` hineinkopieren.
   - **„Veröffentlichen“** klicken.

   Was die Regeln erlauben: nur Räume mit 5-stelligem Code, darin nur Name, Farbe und Antworten der
   Spieler und der Spielstand (alles klein und begrenzt). Räume sind nach 6 Stunden gesperrt.
   Alles andere ist verboten – es kann also niemand fremde Daten in deiner Datenbank ablegen.

4. **Adresse weitergeben**
   - Im Reiter **„Daten“** steht oben die Adresse der Datenbank, etwa
     `https://animepelago-party-default-rtdb.europe-west1.firebasedatabase.app`
   - Diese Adresse schickst du mir (oder trägst sie selbst in `client/party.html` bei
     `const FIREBASE_DB = "";` zwischen die Anführungszeichen ein).
   - Die Adresse ist **nicht geheim** (sie steht später ohnehin in der Seite); geschützt wird alles
     durch die Regeln aus Schritt 3.

Eine „Web-App“ musst du in Firebase **nicht** anlegen und auch keinen API-Schlüssel kopieren:
Die Seite spricht die Datenbank direkt über ihre Web-Adresse an (REST), ohne Firebase-Bibliothek.

## Gut zu wissen
- Spark-Grenzen: 100 gleichzeitige Verbindungen, 1 GB Speicher, ~10 GB Download im Monat.
  Eine Runde mit 4 Leuten braucht davon nur einen winzigen Bruchteil.
- Wird ein Limit doch einmal erreicht, schaltet Firebase die Datenbank bis zum nächsten Monat ab –
  es entstehen **keine Kosten**.
- Alte Räume bleiben klein in der Datenbank liegen (nach 6 Stunden gesperrt). Bei Bedarf kannst du
  im Reiter „Daten“ den Knoten `rooms` einfach löschen.
