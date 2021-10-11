# Expose

## Problemstellung und Kontext

Bei der Entwicklung einer neuen Web-/Mobile Applikation müssen sich Entwickler um Aufgaben kümmern, die bereits in vorherigen Projekten ähnlich erledigt wurden. Ohne eine Wiederverwendung der vorherigen Artefakte erscheint das nicht sehr effizient.

Im Bereich der Entwicklung lassen sich die folgenden wiederkehrenden Aufgaben finden:

- Benutzerverwaltung mit verschiedenen Login-Mechanismen und Sicherheitseinstellungen (Passwortkomplexität, MFA) und Rollensystemen
- Entwicklung von REST- und GraphQL-APIs
- Synchronisation von Offline-Daten und Echtzeitfähigkeit
- Ablage, Verarbeitung und Darstellung von Medien-Dateien (Bilder, Videos o.Ä.)

Im Bereich der Bereitstellung lassen sich ebenfalls wiederkehrende Aufgaben finden:

- Setup der Hosting-Umgebung inklusive Setup des DNS, des Monitoring, des Logging und der Access Controls
- Setup des Continuous Deployments inklusive Vorschau von Pull-Requests und Benachrichtigungen bei Builds
- Skalierung der Applikation bei erhöhter Last

Die Aufgaben für die Entwicklung und Bereitstellung einer neuen Applikation sind zwar immer sehr individuell, dennoch gibt es eine gewisse Schnittmenge, die wiederverwendet werden kann.

Der Cloud Service AWS Amplify von Amazon Webservices hat sich die schnelle Entwicklung von skalierbaren Web- & Mobile Apps zum Ziel gesetzt, indem sie die genannten Aufgaben in ein Serverless-Framework als Function-as-a-Service (FaaS) bündelt und anbietet. AWS Amplify nutzt dazu als Basis die AWS CloudFormation, um gebündelt Cloud-Dienste wie AppSync, DynamoDB, Cognito, API Gateway, S3, Amazon Location Service  über AWS Amplify anbieten zu können. Auch weitere Cloud-Services von AWS können angeschlossen werden.

## Zielsetzung

Das Ziel der Arbeit ist es, eine Web-Applikation mit AWS Amplify zu konzipieren und zu entwickeln. Damit soll evaluiert werden, ob AWS Amplify für künftige Web-Applikationen in (Kunden-)Projekten sinnvoll ist und eingesetzt werden soll.

Um ein möglichst reales Szenario abzubilden, soll es sich bei der Web-Applikation um eine Video-Plattform handeln. Im folgenden wird eine erste Skizze der Plattform dargestellt:

**Objekte**

- Video:
  - Titel
  - Beschreibung
  - Datei
  - Ersteller (= User)
  - Erstelldatum
- User:
  - Email
  - Passwort
  - Rolle (admin, user)
  
**Funktionale Anforderungen:**

- Videos auflisten:
  - Ein User sieht eine Liste aller Videos
  - Die Videos können nach den folgenden Kriterien gefiltert werden (Meine Videos wenn eingeloggt, heute hochgeladen).
- Video-Upload:
  - Ein User lädt ein neues Video hoch.
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

- Das Frontend soll Inhalte in Echtzeit aktualisieren, das heißt, wenn ein anderer User ein neues Video hochlädt, bearbeitet oder löscht, wird jedes laufende Frontend benachrichtigt und dementsprechend aktualisiert.

Auf Grund der Anforderungen ist ein großes Spektrum der Funktionen von AWS Amplify abgedeckt, da die folgenden Features/Cloud-Services genutzt werden können:

- AWS Amplify: als Framework
- AWS AppSync: GraphQL-API & Resolver
- Amazon DynamoDB: NoSQL-Datenbank
- AWS Lambda: Serverless-Umgebung
- Amazon Cognito: "Einfache und sichere Registrierung und Anmeldung von Benutzern und Zugriffskontrolle"
- Amazon S3: "Objektspeicher zum Speichern und Abrufen beliebiger Datenmengen aus allen Speicherorten"
- AWS Elemental MediaConvert: "Verarbeiten Sie Videodateien und -clips, um On-Demand-Inhalte zur Verteilung oder Archivierung vorzubereiten."

Quelle der Service-Beschreibungen: https://aws.amazon.com/de

## Forschungsfragen

- Wie muss eine Serverless-Architektur in AWS Amplify aufgebaut werden?
- Kann durch AWS Amplify und weitere AWS-Dienste Entwicklungszeit und Ressourcen eingespart werden?
- Können durch die Serverless-Architektur von AWS Amplify monatliche Bereitstellungskosten verringert werden?
- Welche zusätzlichen Risiken entstehen durch die Verwendung von AWS Amplify (z.B exorbitante Cloud-Kosten bei Fehlern, Vendor Lock-In, zu starres Framework etc.)
- Und zusammenfassend: Lohnt sich AWS Amplify für die Entwicklung von Web-Plattformen.

## Methodik

Durch die Untersuchung der Anwendbarkeit AWS Amplify als Serverless-Framework mit einer induktiven Argumentationsweise.

## Scope der Arbeit

Der Scope der Arbeit umfasst die Konzeption und Entwicklung der genannten Web-Plattform sowie die Untersuchung des genannten Frameworks. Die Arbeit hat jedoch nicht zum Ziel, AWS Amplify mit anderen Serverless-Frameworks zu vergleichen oder andere Cloud-Anbieter zu beleuchten.

## (Arbeits)-Titel

Entwicklung einer Video-Plattform mit AWS Amplify
