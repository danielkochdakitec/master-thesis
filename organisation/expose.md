# Expose

## Problemstellung und Kontext

Bei der Entwicklung einer neuen Web-/Mobile Applikation müssen sich Entwickler um Aufgaben kümmern, die bereits in vorherigen Projekten ähnlich erledigt wurden. Ohne eine Wiederverwendung der vorherigen Artefakte erscheint das nicht sehr effizient.

Im Bereich der **Entwicklung** lassen sich die folgenden wiederkehrenden Aufgaben finden:

- Benutzerverwaltung mit verschiedenen Login-Mechanismen (E-Mail, Phone, Facebook, Google etc.) und Sicherheitseinstellungen (Passwortkomplexität, MFA)
- Entwicklung von REST- und GraphQL-APIs
- Synchronisation von Offline-Daten

Im Bereich der **Bereitstellung** lassen sich auch wiederkehrende Aufgaben finden:

- Setup der Hosting-Umgebung inbegriffen Setup des DNS, des Monitoring, des Logging und der Access Controls
- Setup des Continuous Deployments inbegriffen Vorschau von Pull-Requests und Benachrichtigungen bei Builds

Die Aufgaben sind bei einer neuen Applikation sehr individuell. Dennoch gibt es immer eine gewisse Schnittmenge, die wiederverwendet werden kann.

Der Cloud Service AWS Amplify von Amazon Webservices hat sich die schnelle Entwicklung von skalierbaren Web- & Mobile Apps zum Ziel gesetzt, indem sie die genannten Aufgaben in ein Serverless-Framework als Function as a Service (FaaS) bündelt und anbietet. AWS Amplify nutzt dazu AWS CloudFormation, um gebündelt etliche Cloud-Dienste wie AppSync, DynamoDB, Cognito, API Gateway, S3, Amazon Location Service und viele mehr über AWS Amplify anbieten zu können.

## Zielsetzung
eine Beschreibung des/der Ergebniss/e der Abschlussarbeit: Welche “Liefergegenstände” (engl. Deliverables) liegen am Ende der Arbeit vor? Was soll erreicht werden? (z.B. Entwicklung einer Komponente für …, Portierung eines Systems für … von … nach …, Evaluation einer Technologie namens …)


## Forschungsfragen

Welche wiederkehrende Fragestellung soll beantwortet werden. Hier ist es entscheidend, die Einschränkung der Gültigkeit zu spezifizieren (z.B. Anwendbarkeit eines Verfahrens für einen bestimmten Nutzerkreis – Auftragsmanagement für Außendienstmitarbeiter von KMU im Baugewerbe im ländlichen Bereich)

## Methodik

Wie soll das erreicht werden? (z.B. durch Anwendung aspektorientierter Programmierung, mit der Library xyz, der Programmiersprache abc, durch Experimente mit Arduino/Menschen/AWS/…)

## Scope der Arbeit

Festlegung des Scopes der Arbeit, also was gehört zur erfolgreichen Bearbeitung, was nicht.

## (Arbeits)-Titel

Bewertung von AWS Amplify unter Berücksichtigung spezifischer Projektkonstellationen

Web & Mobile apps with AWS Amplify - a serverless and developer oriented approach for faster development

## Eigene Notizen

- es ist angewandten Forschung / spezifisch: Untersuchung der Anwendbarkeit einer Methodik

- Vorstellung verschiedener Architekturen: Der Standard, Microservice, Serverless
- Was sind Vorteile, um eine Serverless-Architektur zu adaptieren? Kosten? Performance? Verwaltungsaufwand?
- Welche Herausforderungen hat eine Serverless-Architektur? 
- Welche Nachteile gibt es?
- Was ist Amplify in dem Zusammenhang?
- Wie muss eine Architektur aussehen, wenn sie in der Cloud / AWS Amplify liegt.
- Evaluierung von AWS Amplify