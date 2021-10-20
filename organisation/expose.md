# Expose Master-Thesis

Student: Daniel Koch

Matrikelnummer: 2060256

## Problemstellung und Kontext

Bei der Entwicklung einer neuen Web-/Mobile Applikation müssen sich Entwickler um Aufgaben kümmern, die bereits in vorherigen Projekten ähnlich erledigt wurden. Ohne eine Wiederverwendung der vorherigen Artefakte erscheint das nicht sehr effizient.

Im Bereich der Entwicklung lassen sich die folgenden wiederkehrenden Aufgaben finden:

- Benutzerverwaltung mit verschiedenen Login-Mechanismen und Sicherheitseinstellungen (Passwortkomplexität, MFA) und Rollensystemen
- Entwicklung von REST- und GraphQL-APIs
- Synchronisation von Offline-Daten und Echtzeitfähigkeit
- Ablage, Verarbeitung und Darstellung von Medien-Dateien (Bilder, Videos o.Ä.)

Im Bereich der Bereitstellung lassen sich ebenfalls wiederkehrende Aufgaben finden:

- Setup der Hosting-Umgebung inklusive Setup des DNS, des Monitoring, des Logging, der Access Controls und TLS-Zertifikaten
- Setup des Continuous Deployments inklusive Vorschau von Pull-Requests und Benachrichtigungen bei Builds
- Skalierung der Applikation bei erhöhter Last

Die Aufgaben für die Entwicklung und Bereitstellung einer neuen Applikation sind zwar immer sehr individuell, dennoch gibt es eine gewisse Schnittmenge, die wiederverwendet werden kann.

Sowohl der Cloud Service AWS Amplify als auch Firebase haben sich die schnelle Entwicklung von skalierbaren Web- & Mobile Apps zum Ziel gesetzt, indem sie die genannten Aufgaben in ein Framework als Backend-as-a-Service (BaaS) bündelt und anbietet.

## Zielsetzung

Das Ziel der Arbeit ist es, AWS Amplify und Firebase zu vergleichen. Damit soll evaluiert werden, welches der beiden Cloud-Dienste für zukünftige Web-Applikationen in (Kunden-)Projekten eingesetzt werden soll.

Um ein möglichst reales Szenario abzubilden, soll es sich bei der Web-Applikation um eine Video-Plattform handeln. Im folgenden wird eine erste Skizze der Plattform dargestellt:

**Objekte**

- Video:
  - Titel
  - Beschreibung
  - Datei
  - Thumbnail
  - Ersteller (= User)
  - Erstelldatum
- User:
  - Email
  - Passwort
  - Vorname
  - Nachname
  - Rolle (admin, user)

**Funktionale Anforderungen:**

- Videos auflisten:
  - Ein User sieht eine Liste aller Videos.
  - Die Videos können nach den folgenden Kriterien gefiltert werden (Meine Videos wenn eingeloggt, heute hochgeladen).
  - Die Videos können auch nach dem Titel gesucht werden.
- Video-Upload:
  - Ein User lädt ein neues Video hoch. Dabei soll das Video automatisch transcodiert und ein Wasserzeichen gesetzt werden. Im Anschluss wird das Video dann freigeschalten. Außerdem soll ein Thumbnail generiert werden.
  - Voraussetzungen:
    - Der User ist eingeloggt
- Video bearbeiten:
  - Die Attribute Titel und Beschreibung können bearbeitet werden.
  - Voraussetzungen:
    - Der User ist eingeloggt
    - Der User ist entweder admin oder der Ersteller des Videos
- Video löschen:
  - Videos können gelöscht werden.
  - Voraussetzungen:
    - Der User ist eingeloggt
    - Der User ist entweder admin oder der Ersteller des Videos

**Nicht funktionale Anforderungen:**

- Wenn ein anderer User ein neues Video hochlädt, bearbeitet oder löscht, wird jedes laufende Frontend benachrichtigt und dementsprechend aktualisiert.

## Forschungsfrage

Welcher der beiden Cloud-Dienste AWS Amplify und Firebase eignet sich besser für die Entwicklung einer Web-Applikation unter Berücksichtigung bestimmter Heuristiken wie Cloud-Kosten, Wiederverwendbarkeit von Code, Entwicklungszeit, Wartbarkeit, Flexibilität des Frameworks und sonstigen Risiken.

## Methodik

Durch den Vergleich von AWS Amplify und Firebase mit definierten Heuristiken.

## Scope der Arbeit

Der Scope der Arbeit umfasst die Konzeption und Entwicklung der genannten Web-Plattform für beide Cloud-Dienste, um damit besser die Forschungsfrage beantworten zu können.

## Arbeitstitel

Vergleich von AWS Amplify und Firebase als Backend-as-a-Service Plattformen