# Interview-Vorbereitung — Experte Informationssicherheit mit Schwerpunkt SIEM

**Arbeitgeber:** Deutsche WertpapierService Bank AG (dwpbank)
**Rolle:** Experte Informationssicherheit mit Schwerpunkt SIEM (m/w/d)
**Standort:** Frankfurt am Main (60% Homeoffice)
**Team:** Abteilung "Operative Sicherheit, Regulatorik, Cybersicherheit", 9 Personen
**Kandidat:** Lutz Molderings

---

## 1. Strategische Positionierung

### Deine Ausgangslage (ehrlich)

Du bringst **nicht** operative SIEM-Erfahrung mit. Das ist dir bewusst — und du hast es im Anschreiben offen adressiert. Was du mitbringst:

- Starke **ISMS-/Governance-Seite** nach ISO/IEC 27001, inkl. selbstständig durchgeführter Rollout bis Reifegrad 3
- **Regulatorik-Basis** über vier frische Zertifizierungen (ISO 27001 LI, Security+, Network+, AZ-900)
- **Hybride/Azure-Awareness** aus AZ-900 und Arbeit an Cloud-Anwendungen
- **Praxisnahes Verständnis von Log-Generierung und Anomalien** durch eigene n8n-Agentenstacks und OpenClaw
- **Python-/Automatisierungs-Kompetenz** — relevant für Detection-Engineering, Parser, Custom-Regeln
- **Stakeholder-Kommunikation** zwischen Technik und Governance

### Deine zentrale Botschaft

> "Ich komme von der Governance-Seite und will den nächsten Schritt in die operative Detection & Response machen. Ich bringe die regulatorische und methodische Tiefe mit, die das Team bei DORA, BSI-Grundschutz und ISO 2700x sofort entlastet — und die Lerngeschwindigkeit, die vier Zertifizierungen in zwei Jahren neben dem Job belegen."

Diese Botschaft sollte sich wie ein roter Faden durch alle Antworten ziehen. Niemals verteidigend über fehlende SIEM-Praxis sprechen, sondern **proaktiv** den Brückenschlag zeigen.

---

## 2. Das Unternehmen und der Kontext

### dwpbank auf einen Blick

- Über 22 Jahre im Wertpapiergeschäft
- **Führender Dienstleister für Wertpapierservices in Deutschland**
- Systemplattform **WP3** verarbeitet für **über 1.000 Banken** jährlich mehrere Millionen Wertpapiertransaktionen
- Ca. **1.200 Mitarbeitende**, Standorte Frankfurt, Düsseldorf, München
- Gesellschafter: Genossenschaftliche FinanzGruppe, DekaBank, Sparkassen-Finanzgruppe (historisch bekannt)

### Warum das für das Gespräch wichtig ist

dwpbank ist ein **regulierter Finanzdienstleister** — d.h. es gelten:
- **DORA** (Digital Operational Resilience Act) — seit Januar 2025 voll anwendbar
- **BAIT / MaRisk** (BaFin-Rundschreiben, wenn auch nicht unmittelbar als Wertpapierinstitut, dann über Kundenbeziehungen zu Banken)
- **KRITIS-Bezug** über die Rolle als zentraler Wertpapier-Abwickler (Finanzsektor)
- **ISO/IEC 27001**-Erwartung aus dem Kundenkontext (1.000+ Banken als Auftraggeber erwarten belastbare Nachweise)

### Das Team und die Abteilung

- **"Operative Sicherheit, Regulatorik, Cybersicherheit"** — der Name ist Programm: Operativ + Compliance zusammengedacht
- 9 Kolleg:innen, klein genug, dass jede:r Verantwortung übernimmt
- Scope: **SIEM + Schwachstellenmanagement + Penetrationstests**
- SIEM-Team fährt den **kompletten Lifecycle**: Bedrohungsanalyse -> Use-Case-Entwicklung -> Log-Onboarding -> Detection -> Incident Response
- **Externe Dienstleister** spielen eine Rolle (SIEM-Steuerung) — hier ist deine Erfahrung mit Stakeholder-Management direkt anschlussfähig

---

## 3. Fachliche Vorbereitung — SIEM-Grundlagen

Auch wenn du im Anschreiben offen gesagt hast, dass dir operative SIEM-Praxis fehlt: Die fachlichen Begriffe musst du sauber beherrschen. Sonst wirkst du nicht wie jemand, der den Sprung schaffen kann.

### 3.1 Was ist ein SIEM und was leistet es?

**SIEM = Security Information and Event Management**

Kombiniert zwei historisch getrennte Disziplinen:
- **SIM** (Security Information Management): Langzeit-Speicherung, forensische Recherche, Compliance-Reports
- **SEM** (Security Event Management): Echtzeit-Korrelation, Alerting, Incident Detection

**Kernfunktionen:**
1. **Log-Collection** — zentrale Sammlung aus heterogenen Quellen (Firewalls, AD, Endpoints, Cloud, Applikationen)
2. **Normalisierung & Parsing** — Umwandlung in ein einheitliches Schema
3. **Anreicherung** — GeoIP, Threat Intelligence, Asset-Kontext
4. **Korrelation** — regelbasiert (Signaturen) und/oder verhaltensbasiert (UEBA)
5. **Alerting & Dashboards**
6. **Incident-Response-Workflow** — Tickets, Playbooks, ggf. SOAR-Integration
7. **Langzeit-Storage & Compliance-Reporting** — oft 6–12 Monate, teils länger bei Banken

### 3.2 Marktübliche SIEM-Lösungen

Solltest du kennen, ohne sie konkret betrieben zu haben:

| Produkt | Hersteller | Besonderheit |
|---|---|---|
| Splunk Enterprise Security | Splunk (Cisco) | Marktführer, SPL-Abfragesprache, sehr mächtig, teuer |
| Microsoft Sentinel | Microsoft | Cloud-nativ (Azure), KQL, stark bei M365/Azure-Integration |
| IBM QRadar | IBM | Lange im Banken-Einsatz, ältere Bestandskunden |
| Elastic Security | Elastic | Open-Source-Basis, Lucene/EQL/ES|QL |
| Exabeam / Securonix | eigenständig | UEBA-Fokus |
| LogRhythm | LogRhythm | im Mittelstand verbreitet |
| Chronicle / Google SecOps | Google | Cloud-nativ, Google-Stack |

**Für das Gespräch wichtig:** Da dwpbank **hybrid (On-Prem + Azure)** aufgestellt ist, ist **Microsoft Sentinel** eine sehr wahrscheinliche Komponente. Mach dich vertraut mit:
- KQL (Kusto Query Language) — Grundsyntax
- Data Connectors (Azure AD Sign-in Logs, M365 Defender, Azure Activity)
- Analytics Rules, Workbooks, Hunting Queries
- Automation Rules / Playbooks (Logic Apps)

### 3.3 Log-Quellen — was kommt typischerweise rein?

- **Netzwerk:** Firewalls (Checkpoint, Palo Alto, Fortinet), IDS/IPS, Proxy, DNS, DHCP, VPN
- **Endpoint:** EDR (CrowdStrike, Defender for Endpoint, SentinelOne), Windows Event Logs, Sysmon
- **Identity:** Active Directory, Entra ID (Azure AD), PAM-Systeme
- **Cloud:** Azure Activity Logs, AzureAD Sign-ins, M365 Unified Audit Log, AWS CloudTrail
- **Applikationen:** Web-Applikations-Logs, Datenbank-Audit, fachspezifische Systeme (bei dwpbank: WP3)
- **Infrastruktur:** Hypervisor, Backup, Vulnerability Scanner (Qualys, Tenable)

### 3.4 Detection Engineering — das Handwerk

Jedes Gespräch fragt nach **Detection-Regeln**. Die Grundlogik:

1. **Bedrohungsmodell:** Welche Angriffe sind für unsere Assets realistisch? (TTPs aus **MITRE ATT&CK**)
2. **Use-Case:** Konkreter Angriffspfad, den wir erkennen wollen (z.B. "Impossible Travel in Entra ID")
3. **Log-Grundlage prüfen:** Haben wir die Daten? Onboarding nötig?
4. **Regel entwickeln:** Query (KQL/SPL/EQL), Schwellwerte, Aggregation, Zeitfenster
5. **Testen & Tunen:** False-Positive-Quote messen, Whitelist pflegen
6. **In Produktion nehmen:** Mit Playbook, Severity, Owner
7. **Kontinuierlich reviewen:** veraltete Regeln abschalten, neue Bedrohungen aufnehmen

### 3.5 MITRE ATT&CK — must know

**ATT&CK** ist das gemeinsame Vokabular der Detection-Welt. Taktik-Kategorien grob auswendig:

1. Reconnaissance
2. Resource Development
3. Initial Access
4. Execution
5. Persistence
6. Privilege Escalation
7. Defense Evasion
8. Credential Access
9. Discovery
10. Lateral Movement
11. Collection
12. Command and Control
13. Exfiltration
14. Impact

**Typische Fragen:** "Erkläre mir, wie du einen Use-Case für Lateral Movement bauen würdest." Dein Ansatz: Log-Quellen (AD-Auth, NetFlow, EDR), typische Indikatoren (Pass-the-Hash, PsExec, WMI, RDP-Ketten), Regel-Konzept, False-Positive-Quellen (Admin-Tätigkeit).

### 3.6 Incident-Response-Lifecycle (NIST SP 800-61)

1. **Preparation** — Playbooks, Tools, Kontakte, Übungen
2. **Detection & Analysis** — Event-Triage, Scoping, Eskalation
3. **Containment, Eradication & Recovery** — kurz-/langfristige Eindämmung, Beweissicherung
4. **Post-Incident Activity** — Lessons Learned, Regel-Tuning, Berichtspflichten

Bei **DORA** besonders: **Meldepflichten innerhalb kurzer Fristen** an die zuständige Aufsichtsbehörde bei schweren IKT-Vorfällen (Initial-Meldung idR binnen 4h nach Klassifizierung als schwer, weitere Meldungen danach).

---

## 4. Regulatorik — tiefer Einstieg

Hier bist du **stark**. Nutze das als Anker, wenn andere Fragen ins Operative gehen, die du weniger abdeckst.

### 4.1 DORA — Digital Operational Resilience Act

- **Verordnung (EU) 2022/2554**, voll anwendbar seit **17. Januar 2025**
- Betrifft praktisch alle Finanzunternehmen in der EU — **dwpbank fällt darunter**
- **Fünf Säulen:**
  1. **IKT-Risikomanagement** (Art. 5–15) — Governance, Risk-Framework, Schutz und Prävention, Erkennung, Reaktion & Wiederherstellung, Lernen & Weiterentwicklung, Kommunikation
  2. **IKT-Vorfallmanagement** (Art. 17–23) — Klassifizierung und Meldung schwerer Vorfälle
  3. **Testing operationeller Resilienz** (Art. 24–27) — u.a. **TLPT** (Threat-Led Penetration Testing) bei bestimmten Unternehmen
  4. **Drittparteien-Risikomanagement** (Art. 28–44) — Vertragsanforderungen, kritische IKT-Dienstleister, Überwachung durch ESAs
  5. **Informationsaustausch** (Art. 45) — Threat-Intelligence-Sharing

**SIEM-Bezug:** Säule 1 (Erkennung/Reaktion) und Säule 2 (Incident-Reporting) sind **direkt SIEM-getrieben**. Wer keine brauchbare Detection hat, erfüllt DORA nicht.

### 4.2 BSI IT-Grundschutz

- Methodik des Bundesamts für Sicherheit in der Informationstechnik
- **Grundschutz-Kompendium** mit Bausteinen, strukturiert in:
  - ISMS (ISMS.1), ORP, CON, OPS, DER, APP, SYS, IND, NET, INF
- Für SIEM besonders relevant:
  - **DER.1 — Detektion von sicherheitsrelevanten Ereignissen**
  - **OPS.1.1.5 — Protokollierung**
  - **DER.2.1 — Behandlung von Sicherheitsvorfällen**
  - **DER.2.2 — Vorsorge für die IT-Forensik**
  - **DER.2.3 — Bereinigung weitreichender Sicherheitsvorfälle (APT)**
- **Schichtenmodell** (Schutzbedarf: normal/hoch/sehr hoch) — das kennst du aus deiner Arbeit
- **Grundschutz vs. ISO 27001:** Grundschutz ist prescriptiver (konkrete Maßnahmen pro Baustein), ISO 27001 ist outcome-basiert (managementsystemorientiert). BSI-Grundschutz-Zertifizierung schließt ein ISO-27001-Zertifikat ein.

### 4.3 ISO/IEC 27001 & 27002 (2022er Revision)

Du bist LI-zertifiziert — hier musst du **sattelfest** sein.

- **ISO 27001:2022:** Management-System-Norm, 10 Klauseln, Annex A
- **Annex A** wurde 2022 neu strukturiert: **4 Themen** (statt 14 Kapiteln):
  - A.5 **Organisatorische Maßnahmen** (37 Controls)
  - A.6 **Personelle Maßnahmen** (8 Controls)
  - A.7 **Physische Maßnahmen** (14 Controls)
  - A.8 **Technische Maßnahmen** (34 Controls) — hier sitzen die SIEM-relevanten:
    - **A.8.15 Logging**
    - **A.8.16 Monitoring activities**
    - **A.8.17 Clock synchronization**
    - **A.8.20 Network security**
    - **A.8.23 Web filtering**
    - **A.8.26 Application security requirements**
    - **A.8.28 Secure coding**

- **ISO 27002:2022** liefert die **Implementation Guidance** zu den Controls
- **ISO 27035** — Incident Management (dreiteilig: Principles, Guidelines, CSIRT Operations)
- **ISO 27037** — Evidence / Forensics

### 4.4 Weitere relevante Normen/Frameworks

- **BAIT** (Bankaufsichtliche Anforderungen an die IT) — deutsche BaFin-Leitlinie, durch DORA teils abgelöst
- **MaRisk** — allgemeiner Rahmen für Risikomanagement
- **NIS2-Richtlinie** — ergänzend, über dwpbanks Kunden potenziell relevant
- **PCI-DSS** — wenn dwpbank Kartendaten verarbeitet (prüfen)
- **NIST CSF 2.0** — sechs Funktionen: Govern, Identify, Protect, **Detect**, **Respond**, Recover

---

## 5. Cloud / Azure / Hybrid — Fokus der Stelle

Die Stellenanzeige nennt explizit "hybride On-Prem/Cloud-Umgebung (insbesondere **Azure**)". Du hast AZ-900 — das reicht für konzeptionelle Gespräche, aber bereite dich auf Detailfragen vor.

### 5.1 Azure-Komponenten, die im SIEM-Kontext zählen

- **Entra ID** (vormals Azure AD) — Identity-Provider, Sign-in Logs, Audit Logs, Conditional Access
- **Microsoft Defender for Cloud** — CSPM (Posture) + CWPP (Workload Protection)
- **Microsoft Defender XDR Suite** — Defender for Endpoint, Identity, Office 365, Cloud Apps (MCAS)
- **Azure Monitor / Log Analytics Workspace** — Log-Senke, Grundlage für Sentinel
- **Microsoft Sentinel** — SaaS-SIEM/SOAR auf Log Analytics Workspace
- **Azure Activity Log** — Control-Plane-Events (wer hat was administrativ gemacht)
- **NSG Flow Logs / Azure Firewall Logs** — Netzwerksichtbarkeit

### 5.2 Hybrid-Herausforderungen (wichtige Gesprächspunkte)

- **Log-Volumen & -Kosten:** Sentinel ingestion pricing — Tuning relevant
- **Latenz:** On-Prem-Logs über Syslog/Agent in Cloud ziehen
- **Identität:** Synchronisation Entra Connect, Hybrid Identity Joins — Angriffsfläche
- **Lateral Movement über die Cloud-Grenze:** klassische Ketten wie "On-Prem AD kompromittiert -> Entra ID Sync -> Cloud-Ressourcen"
- **Shared Responsibility Model** — was muss ich selbst monitoren, was deckt Microsoft ab?

### 5.3 Bekannte Angriffsmuster in hybriden Umgebungen

- **Golden SAML / Federation Abuse** (Solarwinds-Referenz)
- **AADConnect-Missbrauch**
- **OAuth-Consent-Phishing**
- **Illicit Consent Grants**
- **Token-Theft / Session-Hijacking**

Diese Begriffe solltest du mindestens einmal aussprechen können.

---

## 6. Fragen, die mit hoher Wahrscheinlichkeit kommen

### 6.1 Einstieg / Personalfragen

**"Erzählen Sie uns etwas über sich."**

Deine 90-Sekunden-Version:
> "Ich bin seit 2023 Information Security Manager bei DB Systel, dem IT-Partner der Deutschen Bahn. Meine Verantwortung liegt im ISMS-Kontext nach ISO/IEC 27001 — für produktive Anwendungen, die meinem Team zugeordnet sind. Das bedeutet konkret: Schutzbedarfsanalysen, Risikobewertung, Abstimmung der Behandlungsmaßnahmen mit dem zentralen CISO-Team, revisionssichere Nachweisdokumentation. Vor der Security-Rolle war ich bei der Deutschen Bahn in der Sprachdatenverarbeitung — Python, NLP, Prozessautomatisierung. Die technische Seite habe ich mir nicht abtrainiert, im Gegenteil: ich nutze sie heute produktiv, u.a. für n8n-basierte Agenten-Workflows. Parallel habe ich in den letzten zwei Jahren vier Security-Zertifizierungen gemacht — ISO 27001 Lead Implementer, Security+, Network+, Azure Fundamentals. Die Motivation für den Wechsel zu Ihnen ist, den Schritt von der Governance-Seite stärker Richtung operative Detection zu gehen."

**"Warum dwpbank? Warum diese Stelle?"**

- Reguliertes Finanzumfeld — deine Stärke ist Regulatorik; dort zahlt sich ISO 27001 LI und DORA-Wissen unmittelbar aus
- Kleines Team (9) — konkrete Verantwortung, kurze Wege, "kein Sicherheitstheater"
- Der Zuschnitt "Operative Sicherheit + Regulatorik + Cybersicherheit" in einer Abteilung passt zu deinem Profil, das beide Welten verbindet
- Hybrid/Azure — du willst Cloud-Security-Tiefe ausbauen, Azure ist deine Lernachse
- Wertpapier-Abwicklung für 1.000+ Banken: der Impact-Hebel ist groß

**"Warum wollen Sie DB Systel verlassen?"**

Nicht schlecht reden. Ehrlich: Du bist aktuell in der Governance-Ecke, willst aber näher an die Detection. Bei DB Systel ist dein Scope team-/anwendungsbezogen und governance-dominiert — operative Detection & Response findet in anderen Einheiten statt. Der Wechsel ist ein Schritt **hin zu** etwas, nicht weg von etwas.

**"Was ist Ihre größte Schwäche für diese Rolle?"**

Sag ehrlich: operative SIEM-Erfahrung. Dann sofort pivot:
- Was du stattdessen tust, um das zu schließen: Selbststudium (MITRE, Sentinel-Labs, KQL), Zertifizierungsdisziplin, Lernbereitschaft
- Was du dafür **mitbringst**: ISMS/Regulatorik, Log-/Automatisierungsverständnis aus eigenen Agenten-Projekten, Python

### 6.2 Fachliche Fragen — SIEM

**"Wie würden Sie einen neuen SIEM Use-Case entwickeln?"**

Strukturiere die Antwort als Pipeline:
1. Bedrohungsmodell klären — welcher TTP, welches Schutzziel, welches Asset?
2. ATT&CK-Mapping
3. Log-Verfügbarkeit prüfen, ggf. Onboarding anstoßen
4. Baseline & False-Positive-Erwartung
5. Regel-Entwurf mit Schwellwerten, Aggregation, Severity
6. Test gegen historische Daten
7. Tuning-Phase mit engem Review
8. Dokumentation: Purpose, Logic, Owner, Playbook-Referenz
9. Lifecycle: Review-Zyklen, Deprecation-Kriterien

**"Welche Log-Quellen sind für ein SIEM in einer Azure-Hybridumgebung zwingend?"**

Antwort-Rahmen:
- Identity: Entra ID Sign-in/Audit, on-prem AD
- Endpoint: EDR (Defender for Endpoint), Sysmon
- Netzwerk: Firewall, Proxy, DNS
- Cloud-Kontrollebene: Azure Activity Log
- Workloads: Defender for Cloud Alerts
- Applikationen: geschäftskritisch — bei dwpbank vermutlich WP3 und angeschlossene Systeme

**"Was ist der Unterschied zwischen SIEM und SOAR?"**

- **SIEM:** Log-Aggregation, Korrelation, Alerting, Analyse
- **SOAR** (Security Orchestration, Automation & Response): Playbook-Automatisierung, Ticketing, Integration in Drittsysteme, Response-Aktionen (z.B. Account disablen, IP blocken)
- Moderne Suiten verschmelzen beides (Sentinel Automation Rules/Logic Apps, Splunk SOAR)

**"Wie gehen Sie mit False Positives um?"**

- Baseline verstehen (Wer/Was ist normal für unsere Umgebung?)
- Tuning: Zeitfenster, Schwellwerte, Whitelists
- Kontext-Anreicherung (Asset-Kritikalität, User-Rolle, Location)
- Confidence-Scoring
- Regelmäßiger Review der Alert-Historie
- **Ziel:** Analyst:innen vor Alert-Fatigue schützen — False Positives sind ein KPI

**"Wie würden Sie den Erfolg eines SIEM messen?"**

- **MTTD** (Mean Time To Detect)
- **MTTR** (Mean Time To Respond / Resolve)
- Coverage gegen MITRE ATT&CK (Anteil abgedeckter Techniken)
- Log-Source-Coverage (Anteil angebundener kritischer Quellen)
- Signal-to-Noise (True Positives / Total Alerts)
- Regel-Lifecycle-Kennzahlen (Anzahl aktiver/deprecated Regeln, Alter)
- Verfügbarkeit der Plattform selbst

### 6.3 Regulatorik-Fragen

**"Was ändert DORA für ein SIEM-Team?"**

- Meldepflichten an die BaFin bei **schweren IKT-Vorfällen** — SIEM muss die Klassifizierung (Kunden-Impact, Datenverluste, wirtschaftliche Auswirkung, Dauer, geografischer Umfang, Reputationsschaden, kritische Dienste) unterstützen
- Zeitfenster: initial innerhalb weniger Stunden, dann Zwischen- und Abschlussmeldung
- TLPT-Anforderungen — Red-Team-Tests müssen SIEM-Detektion stressen
- Drittparteien-Risiken: Dienstleister-Steuerung mit Nachweisen; bei dwpbank explizit in der Stelle genannt
- Belastbare Incident-Dokumentation für Aufsichtsprüfungen

**"BSI-Grundschutz oder ISO 27001 — wo ist der Unterschied?"**

Deine LI-Antwort:
- ISO 27001: managementsystem-orientiert, outcome-basiert, international
- BSI-Grundschutz: bausteinbasiert, konkretere Umsetzungsanleitungen, deutscher Standard, besonders im Behördenumfeld und bei KRITIS verankert
- Kombination möglich: BSI-Grundschutz-Zertifikat schließt ISO 27001 ein

**"Wie dokumentieren Sie Risiken?"**

Aus deiner DB-Systel-Praxis:
- Schutzbedarfsanalyse pro Anwendung/Asset (CIA-Triaden-Bewertung)
- Risiko-Register mit Bedrohung, Schwachstelle, Eintrittswahrscheinlichkeit, Auswirkung
- Risikoakzeptanz vs. -behandlung (vermeiden, mindern, übertragen, akzeptieren)
- Nachvollziehbare Verknüpfung: Risiko -> Maßnahme -> Nachweis
- Governance-Review mit CISO

### 6.4 Verhaltensfragen

**"Erzählen Sie von einem Konflikt mit einem Fachbereich, bei dem eine Sicherheitsanforderung auf Widerstand stieß."**

Nutze STAR (Situation, Task, Action, Result). Greife auf Risikobehandlung zurück, wo du mit Product Ownern oder technischen Teams die Maßnahmenumsetzung aushandeln musstest.

**"Wie halten Sie sich fachlich aktuell?"**

- LinkedIn Learning, Udemy (konkret)
- Zertifizierungskadenz (vier in zwei Jahren)
- OpenClaw als Sandbox für agentische Konzepte und ihre Sicherheitsimplikationen
- Quellen: BSI, heise security, The DFIR Report, Microsoft Security Blog, SANS ISC, relevante Podcasts
- Du solltest ein, zwei aktuelle Themen benennen können (z.B. Scattered Spider/MGM, Midnight Blizzard gegen Microsoft, aktuelle Azure-Token-Theft-Welle, oder allgemein: LLM-Security / OWASP Top 10 for LLMs)

**"Wie erklären Sie ein Security-Thema einem nicht-technischen Stakeholder?"**

Das ist deine Stärke — ehemaliger Übersetzer, Python-Trainer für CLS-Team. Beispiel: Konzept MFA / Schutzbedarf / Risiko in einer Business-Sprache verpacken, Analogien, konkrete Beispiele.

### 6.5 Unangenehme, aber wahrscheinliche Fragen

**"Sie haben noch nie ein SIEM betrieben — warum sollten wir Sie einstellen?"**

Nicht entschuldigen. Strukturiert antworten:
1. **Erkennung:** Ich weiß, dass das die Lücke ist — die habe ich im Anschreiben selbst benannt
2. **Was ich mitbringe, was in einem SIEM-Team schnell Mehrwert schafft:**
   - Regulatorik-Klarheit (DORA, ISO, Grundschutz) — entlastet das Team bei Audits und Nachweisen
   - Dokumentation und strukturierte Arbeitsweise — Detection-Regeln brauchen das
   - Python und Automatisierungs-Know-how — für Parser, Queries, Playbooks
   - Lerngeschwindigkeit: vier Zertifizierungen in zwei Jahren neben dem Job
3. **Wie ich den Einstieg plane:** KQL-/Sentinel-Vertiefung, MITRE-Deep-Dive, Shadowing erfahrener Kolleg:innen, strukturiertes Einlernen in bestehende Use-Cases
4. **Offen nachfragen:** "Wie ist Ihre Erfahrung, wenn Personen aus einer ISMS-/Governance-Rolle in operative SIEM-Arbeit wechseln — was hat funktioniert, was nicht?"

**"Wir suchen jemanden, der sofort operativ beitragen kann — das sind Sie nicht."**

- Den Einwand als legitim anerkennen
- Rückfragen: Wie ist aktuell der Aufgaben-Mix im Team? Wer macht regulatorische Dokumentation für DORA? Wer pflegt die Nachweisdokumentation zum SIEM-Prozess selbst?
- Vorschlag: In den ersten 6 Monaten kann ich die Regulatorik-Last des Teams spürbar reduzieren und parallel operativ einsteigen. Danach ist der Übergang zu vollwertiger Detection-Arbeit realistisch.

---

## 7. Deine Fragen an das Team — wichtig

**Niemals mit "Ich habe keine Fragen" antworten.** Bereite 5–8 vor; wähle im Gespräch die passenden aus.

### Zum Team und zur Rolle

- Wie ist der Aufgaben-Mix zwischen operativem SIEM-Betrieb, Detection-Engineering, Incident-Response und regulatorischer Dokumentation im Team verteilt?
- Mit welchen externen Dienstleistern arbeiten Sie beim SIEM konkret zusammen — ist das klassisches Co-Managed-SIEM oder eher reine Tool-Unterstützung?
- Welche SIEM-Plattform ist aktuell im Einsatz, und plant das Team mittelfristig einen Plattformwechsel?

### Zur Technik

- Welche Log-Quellen sind aktuell angebunden, wo liegen erkannte Lücken?
- Wie ist die Aufteilung zwischen On-Prem- und Azure-Workloads — wie stark ist Microsoft Sentinel heute schon im Stack?
- Wie arbeiten SIEM-Team und das Schwachstellenmanagement/Pentest-Team zusammen?

### Zur Einarbeitung

- Wie sieht eine typische Einarbeitung in diesem Team aus — Mentoring, Shadowing, strukturierte Lernpfade?
- Gibt es in den ersten Monaten konkrete Lernziele, an denen ein Einstieg gemessen wird?

### Zur Weiterentwicklung

- Welche Rolle spielen Weiterbildungen und Zertifizierungen (z.B. SC-200, AZ-500, GCIA, GCFA, OSCP) — gibt es Budget und Zeit dafür?
- Wo sehen Sie das Team in 12–24 Monaten — welche Fähigkeiten sollen stärker werden?

### Zum Kontext

- Wie stark tangiert DORA das Tagesgeschäft aktuell — welche Prozesse wurden konkret angepasst?
- Wie läuft die Zusammenarbeit mit den Fachbereichen, insbesondere WP3-seitig, bei sicherheitsrelevanten Themen?

---

## 8. Logistik und Soft Skills

### Vor dem Gespräch

- Unterlagen durchgehen: Anschreiben, Lebenslauf, Vacancy — inhaltlich 100% abdeckend
- Website dwpbank: aktuelle Presse, Leitbild, aktuelle Kampagnen
- LinkedIn: Profile der Gesprächspartner:innen ansehen, wenn Namen bekannt
- Technik-Check, falls remote
- Getränke, Notizblock, Stift bereit
- Puffer einplanen, 10 Minuten vor der Zeit "da" sein

### Auftreten

- Ruhig, klar, kurze Pausen sind erlaubt — überstürze Antworten nicht
- Wenn du etwas nicht weißt: sag das, biete an, wie du es lernen würdest
- **Konkret bleiben:** Beispiele aus deiner Praxis, keine abstrakten Allgemeinplätze
- Fachbegriffe sicher verwenden, aber nicht mit Buzzwords überfrachten
- Augenkontakt mit allen Gesprächspartner:innen, nicht nur mit dem Senior

### Nach dem Gespräch

- Kurze, höfliche Dankes-Mail am nächsten Tag — nicht zwingend, aber gern gesehen im Banken-Umfeld
- Notizen dokumentieren: offene Fragen, Eindrücke, nächste Schritte

---

## 9. Kurz-Spickzettel (für den Tag davor)

- **Rolle:** Experte Informationssicherheit mit Schwerpunkt SIEM bei dwpbank
- **Team:** 9, Abteilung "Operative Sicherheit, Regulatorik, Cybersicherheit"
- **Scope:** SIEM-Betrieb, Detection-Engineering, Incident-Response, Dienstleistersteuerung, hybrider Azure-Stack
- **Mein Pitch:** ISMS-/Regulatorik-Stärke + Lerngeschwindigkeit + technische Basis -> bewusster Schritt in operative Detection
- **Meine Lücke (offen):** keine operative SIEM-Praxis — kompensiere mit Governance, Python, Azure-Grundlagen, Zertifizierungsdisziplin
- **Must-know-Begriffe:** MITRE ATT&CK, KQL, Sentinel, Defender XDR, Entra ID, DORA (5 Säulen), BSI-Grundschutz DER.1, ISO 27001 A.8.15/A.8.16, MTTD/MTTR, True/False Positive, SOAR
- **Rote-Faden-Story:** Governance heute -> Detection morgen, weil Regulatorik ohne Detection leer ist und Detection ohne Regulatorik kontextlos bleibt

Viel Erfolg.
