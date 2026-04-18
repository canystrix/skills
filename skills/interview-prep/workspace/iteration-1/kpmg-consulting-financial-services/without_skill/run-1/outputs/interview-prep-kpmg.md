# Interviewvorbereitung — KPMG

**Rolle:** Senior Consultant Cyber Security Financial Services (w/m/d)
**Unternehmen:** KPMG AG Wirtschaftsprüfungsgesellschaft
**Bereich:** Financial Services Technology- und Enabling Services
**Standorte:** Frankfurt, München, Stuttgart, Mannheim, Mainz, Jena
**Kandidat:** Lutz Molderings
**Vorbereitungsdatum:** 17.04.2026

---

## 1. Rollenanalyse auf einen Blick

KPMG sucht hier keinen reinen ISMS-Manager, sondern einen beratenden Umsetzer für Finanzdienstleister. Der Schwerpunkt liegt eindeutig auf:

- **SOC-Projekten** (Aufbau/Optimierung von Security Operation Centern, Analyse- und Incident-Response-Prozesse)
- **SIEM** (Use-Case-Erstellung in Splunk, QRadar, Elastic Stack)
- **IAM / Berechtigungsmanagement** (Konzepte einführen, optimieren, implementieren)
- **Security Policies & IT-Architektur** (Einhaltung sicherstellen)
- **Projektmanagement** (Analysephase bis Go-Live)

Regulatorischer Kontext (nicht explizit genannt, aber für FS-Beratung bei KPMG zentral):
DORA, BAIT/VAIT/KAIT/ZAIT, MaRisk AT 9, EBA-Guidelines zu ICT-Risk, BaFin-Rundschreiben, NIS2.

### Wo du stark passt

- ISO/IEC 27001 ISMS, Schutzbedarfsanalyse, Risikobehandlung — praktisch, nicht nur theoretisch
- Berechtigungskonzepte / Access Management aus dem laufenden Betrieb
- Stakeholder-Kommunikation zwischen technischem Betrieb und CISO-Governance
- Python/Automatisierung + Agentic AI (n8n, OpenClaw) — selten in Beratungsprofilen, für FS-Kunden mit KI-Governance-Fragen ein Asset
- Sehr gute deutsche und englische Sprachkenntnisse (C1 DE ist Pflicht — bei dir Muttersprache)

### Wo du Lücken hast — bitte bewusst darauf vorbereiten

- **SIEM-Tools im Detail** (Splunk/QRadar/Elastic Stack): keine Hands-on-Erfahrung laut CV
- **SOC-Betrieb**: Konzeptionell vertraut (Incident Response als Security+-Thema), aber kein Projekt gebaut/begleitet
- **Klassische Beratungserfahrung**: bisher keine externe Kundenprojekterfahrung, sondern Inhouse-Governance
- **Reisebereitschaft**: KPMG-Consulting bedeutet Kundenprojekte vor Ort — darauf solltest du eine Antwort haben
- **Branchenerfahrung Financial Services**: Bahn-Konzern ist regulierter Umgebung, aber keine Bank/Versicherung

---

## 2. Vermutete Interview-Struktur bei KPMG

KPMG-Consulting-Prozesse laufen üblicherweise so ab:

1. **Erstes Gespräch** (30–45 min) mit HR + fachlichem Ansprechpartner: Motivation, Werdegang, grobe Passung
2. **Zweitgespräch / Fachgespräch** (60–90 min) mit Manager/Senior Manager: fachliche Tiefe, Case Study, manchmal Fit-Fragen
3. **Ggf. Gespräch mit Partner** oder strukturiertes Assessment: Consulting-Skills, Stressresistenz, Präsentation

Dieses Dokument bereitet auf Stufe 1 und 2 vor.

---

## 3. Typische Fragen — mit Antwortstrategien

### 3.1 Motivation & Kulturfit

**F: "Warum KPMG und warum dieser Bereich?"**
Leitfaden für deine Antwort:
- Spezifität statt Floskeln: FS Technology- und Enabling Services (genaue Einheit nennen, signalisiert, dass du die Anzeige gelesen hast)
- Drei Gründe: (1) Beratungsperspektive — andere Häuser, andere Reifegrade; (2) Finanzsektor als regulatorisch anspruchsvollstes Umfeld nach DORA; (3) KPMG-Größe = Zugang zu SOC-/SIEM-Projekten, die man inhouse selten in dieser Dichte sieht.
- Ehrlich über den Wechsel: Du hast drei Jahre inhouse ISMS gemacht, willst jetzt die Bandbreite. Gut formuliert: "Bei DB Systel sehe ich ein ISMS sehr tief. Bei KPMG würde ich viele sehen — das ist bewusst der nächste Schritt."

**F: "Warum vom Konzern in die Beratung — und warum jetzt?"**
- Inhouse = Tiefe, Beratung = Breite. Nach erfolgreichem ISMS-Rollout (Reifegrad 3, ohne externe Begleitung) ist ein natürlicher Moment für Perspektivwechsel.
- Warnung: Vermeide es, DB Systel zu kritisieren. Formuliere positiv: "Ich habe dort viel gebaut. Jetzt will ich das, was ich gebaut habe, in anderen Kontexten wieder erkennen und anpassen."

**F: "Wie stellst du dir den Consultant-Alltag vor?"**
- Zeige, dass du Reisen, Kundenprojekte, Billability, parallele Projekte realistisch einschätzt.
- Ehrlich: Du hast keinen Beratungshintergrund — benenn das, aber zeige, dass du Stakeholder-Management (Brücke CISO-Team ↔ technische Teams ↔ Fachseite) bereits tust. Das ist das Kernhandwerk.

---

### 3.2 Fachfragen ISO 27001 / Risikomanagement

**F: "Erklär uns deine Rolle als ISMS-Verantwortlicher bei DB Systel."**
Kernbotschaft in drei Sätzen:
- Seit 2023 ISMS-Rollout für drei produktive Anwendungen, eigenverantwortlich bis Reifegrad 3 ohne externe Begleitung.
- Schutzbedarfsanalysen, Risikobewertung, Ableitung und Umsetzung technischer/organisatorischer Maßnahmen, Nachweisdokumentation.
- Abstimmung mit zentralem CISO-Team, Governance-Reviews vorbereitet.
Wichtig: **Scope ist Team-/Anwendungsebene**, nicht konzernweit. Du schreibst keine konzernweiten Richtlinien.

**F: "Wie läuft eine Schutzbedarfsanalyse bei dir ab?"**
Strukturiert antworten:
- Grundwerte: Vertraulichkeit, Integrität, Verfügbarkeit, (bei DB oft auch Authentizität/Nichtabstreitbarkeit)
- Methodik: Skala (z. B. normal / hoch / sehr hoch), Schadensszenarien pro Grundwert
- Vererbungsprinzip: Schutzbedarf der verarbeiteten Daten → Anwendung → Infrastruktur
- Ergebnis: Schutzbedarfsklasse, daraus abgeleitet die Maßnahmenkataloge
- Abstimmung: mit Fachseite (wissen, was die Daten bedeuten) und Technik (was ist umsetzbar)

**F: "Wie bewertest du Risiken? Welche Methodik nutzt du?"**
- Eintrittswahrscheinlichkeit × Schadenshöhe in Matrix, qualitativ kalibriert
- Vier Risikobehandlungsoptionen: Vermeiden, Vermindern, Übertragen, Akzeptieren
- Wichtige Abgrenzung: Inherent risk vs. residual risk — welche Controls wirken bereits, welche sind neu
- Bezug zu ISO 27005 und dem Konzernstandard

**F: "ISO 27001 vs. BSI-Grundschutz — wo siehst du Unterschiede?"**
Kurzversion:
- ISO 27001: risikobasiert, international, schlanker Annex A mit 93 Controls (2022)
- BSI-Grundschutz: bausteinbasiert, präskriptiver, deutsch-behördlich, größerer Umfang
- Im Finanzsektor faktisch oft Mischbetrieb: ISO 27001 als Zertifizierungsbasis, BaFin-Vorgaben (BAIT/DORA) als Pflicht on top.

**F: "Welche wichtigen Änderungen brachte ISO 27001:2022?"**
- Annex A von 114 auf 93 Controls reduziert, neu gruppiert in 4 Themen (Organizational, People, Physical, Technological)
- 11 neue Controls: Threat intelligence, Cloud services, ICT readiness for business continuity, Physical security monitoring, Configuration management, Information deletion, Data masking, DLP, Monitoring activities, Web filtering, Secure coding
- Übergangsfrist bis Oktober 2025 — mittlerweile verpflichtend.

---

### 3.3 Fachfragen SOC / SIEM — deine Schwachstelle, bereite dich gezielt vor

Du musst hier nicht vortäuschen, dass du Splunk operativ gefahren hast. Aber zeige konzeptuelles Verständnis.

**F: "Wie würdest du den Aufbau eines SOCs für eine Bank konzeptionell angehen?"**
Antworte in Phasen:
1. **Scope & Anforderungen**: regulatorische Treiber (DORA, BAIT), Schutzbedarf der Assets, bestehende Monitoring-Landschaft
2. **Target Operating Model**: intern / hybrid / MSSP? Level-Struktur (L1 Triage, L2 Analyse, L3 Hunting/IR)
3. **Use Cases priorisieren**: MITRE ATT&CK als Referenzrahmen, Crown Jewels zuerst
4. **Technologie**: SIEM-Auswahl, Logquellen-Onboarding, SOAR-Integration
5. **Prozesse**: Incident Response Plan, Playbooks, Eskalationspfade
6. **Metriken**: MTTD, MTTR, Coverage, False-Positive-Rate
7. **Kontinuierliche Verbesserung**: Purple Teaming, Lessons Learned

**F: "Was ist ein guter SIEM Use Case? Wie priorisierst du?"**
- Mapping auf MITRE ATT&CK Techniken, kombiniert mit Bedrohungslage und Kronjuwelen der Organisation
- Qualitätskriterien: klar definierte Logquelle, niedrige False-Positive-Rate, nachvollziehbare Response-Action, Tuning möglich
- Beispiele: Brute-Force auf privilegierte Accounts, Impossible Travel, Privilegieneskalation, DNS-Tunneling, ungewöhnliche Outbound-Volumen

**F: "Kennst du Splunk / QRadar / Elastic Stack?"**
Ehrliche Antwort: "Nicht operativ. Ich kenne die Rollen im SIEM-Ökosystem konzeptionell — Datasources, Parser/Normalisierung, Korrelationsregeln, Dashboards, Alerting. Splunk-SPL, QRadar-AQL, KQL bei Elastic habe ich mir nicht angeeignet, weil mein aktueller Scope das nicht erfordert. Das ist ein Bereich, den ich bei KPMG aufbauen würde — inhaltlich kann ich mit Use-Case-Diskussionen beginnen, Tooling lerne ich schnell." Diese Art Ehrlichkeit punktet bei KPMG mehr als vorgetäuschtes Wissen.

**F: "Was ist der Unterschied zwischen SIEM und SOAR?"**
- SIEM = Sammlung, Korrelation, Alerting. Reaktiv: meldet.
- SOAR = Automatisierung der Response. Playbooks orchestrieren Aktionen (z. B. User sperren, Ticket öffnen, Forensik-Daten sichern).
- In modernen SOCs laufen beide zusammen, zunehmend ergänzt um XDR-Plattformen.

**F: "Was ist MITRE ATT&CK und wie nutzt man es?"**
- Knowledge Base von Taktiken, Techniken, Sub-Techniken realer Angreifer
- Im SOC: Use-Case-Coverage mappen ("welche Technik erkennen wir, welche nicht")
- In Red/Purple-Teaming: Szenarien aufbauen
- Für Risikobewertung: Bedrohungslagebezug statt abstrakter Wahrscheinlichkeit

---

### 3.4 IAM / Berechtigungsmanagement — deine Stärke

**F: "Wie hast du Berechtigungskonzepte bei DB Systel umgesetzt?"**
Strukturiere nach:
- Least Privilege als Leitprinzip
- Rollen-/Rechtemodell: RBAC als Basis, Segregation of Duties
- Joiner/Mover/Leaver-Prozesse: Zugriff bei Eintritt minimal provisioniert, bei Rollenwechsel bereinigt, bei Austritt entzogen
- Rezertifizierung: regelmäßige Reviews durch Data Owner
- Nachweisdokumentation für Audits
- Privileged Access: getrennte Accounts, MFA, Session Recording wo möglich

**F: "Was ist der Unterschied zwischen Authentifizierung, Autorisierung, Identitätsnachweis?"**
- Authentifizierung: "Bist du der, der du vorgibst zu sein?" (Passwort, MFA, Zertifikat)
- Autorisierung: "Was darfst du tun?" (Rechte, Rollen)
- Identity Proofing: Einmalige Verifikation der realen Person beim Onboarding
Nachschieben: Accounting/Auditing als vierter Teil (AAA) — wer hat was wann getan.

**F: "Zero Trust — was heißt das für IAM?"**
- "Never trust, always verify"
- Kontinuierliche Verifizierung statt einmaliger Perimeter-Prüfung
- Kontextbezogene Zugriffsentscheidungen: User, Device, Location, Verhalten, Risiko-Score
- Micro-Segmentation + starkes IAM als Fundament
- Realität im FS-Sektor: schrittweiser Umbau, selten Greenfield

---

### 3.5 Regulatorik Financial Services

**F: "Was weißt du über DORA?"**
Kernpunkte:
- **Digital Operational Resilience Act**, EU-Verordnung, seit Januar 2025 anwendbar
- Gilt für Banken, Versicherer, Zahlungsdienstleister, kritische IKT-Drittdienstleister (ICT TPPs)
- Fünf Säulen:
  1. ICT-Risikomanagement (Governance, Prozesse, Controls)
  2. Meldung schwerwiegender IKT-Vorfälle
  3. Digitale operationelle Resilienztests (inkl. Threat-Led Penetration Testing, TLPT)
  4. Management von IKT-Drittparteirisiken (Register, Konzentrationsrisiken, Exit-Strategien)
  5. Informationsaustausch zu Bedrohungslagen
- Wichtige Abgrenzung: DORA löst BAIT nicht komplett ab — BaFin hat Zirkulare angepasst, aber nationale Spezifika bleiben.

**F: "BAIT, VAIT, KAIT, ZAIT — was ist das?"**
- BaFin-Rundschreiben zu IT-Anforderungen für Banken / Versicherer / Kapitalverwaltungsgesellschaften / Zahlungsinstitute
- Konkretisieren MaRisk AT 9 (Auslagerung) und AT 7.2 (IT-Systeme)
- Themen: IT-Strategie, IT-Governance, Berechtigungsmanagement, Projekte, Anwendungsentwicklung, IT-Betrieb, Auslagerungen, kritische Infrastrukturen
- Durch DORA teilweise überlagert, aber weiterhin relevant für nationale Aufsicht.

**F: "Was ist NIS2 und wen betrifft das?"**
- EU-Richtlinie zur Cybersicherheit kritischer und wichtiger Einrichtungen, seit Oktober 2024 anwendbar
- Breiterer Anwendungsbereich als NIS1: deutlich mehr Sektoren, Schwellenwerte nach Unternehmensgröße
- Pflichten: Risikomanagementmaßnahmen, Meldepflichten (24h/72h/1M), Governance-Verantwortung auf Vorstandsebene
- Für FS-Beratung relevant, wenn Kunden gleichzeitig DORA- und NIS2-Scope haben — Überschneidungen managen.

**F: "Wo überschneiden sich DORA, ISO 27001 und NIS2?"**
Gutes Framing:
- ISO 27001 ist das Rahmenwerk ("wie baue ich ein ISMS")
- DORA/NIS2 sind Pflicht-Anforderungen ("was müssen FS-/KRITIS-Unternehmen nachweisen")
- ISO 27001 als Grundlage erleichtert DORA-Compliance massiv, deckt aber nicht alles ab (z. B. TLPT, Meldepflichten an EU-Aufsicht)
- Praktisch: Control-Mapping zwischen ISO Annex A, DORA RTS, NIS2-Anforderungen, BSI C5 für Cloud-Dienstleister

---

### 3.6 Agentic AI & KI-Governance — dein Differenzierungsmerkmal

Dein Anschreiben hebt das hervor — rechne mit Nachfragen.

**F: "Was meinst du mit Risiken agentenbasierter Systeme?"**
Antworte konkret, nicht schwammig:
- **Prompt Injection / Indirect Prompt Injection**: manipulierte Eingaben (auch aus verarbeiteten Dokumenten/Webseiten) steuern Modellverhalten
- **Tool-Abuse**: Agenten mit Tool-Zugriff führen unbeabsichtigte Aktionen aus (Mails versenden, Dateien löschen, API-Calls)
- **Datenabfluss**: sensitive Daten im Kontext werden in Ausgaben oder externe Systeme exfiltriert
- **Supply-Chain-Risiken**: Model-Repositories, MCP-Server, Tool-Integrationen als neue Angriffsfläche
- **Governance-Lücken**: wer haftet für Agenten-Aktionen, wie werden sie protokolliert, wie rezertifiziert

**F: "Wie würdest du einer Bank helfen, Agentic-AI-Governance einzuführen?"**
Gliederung:
1. **Inventar**: welche Agenten existieren, mit welchen Tools/Datenquellen (Shadow-AI-Problem)
2. **Klassifizierung**: EU AI Act Risk Tiers, regulatorische Zuordnung (DORA-ICT?), Schutzbedarf
3. **Controls**: Human-in-the-Loop für hochrisikobehaftete Aktionen, Least-Privilege für Tools, Output-Filterung, Logging
4. **Testing**: Red-Teaming gegen Prompt Injection, Jailbreaks, Datenleaks
5. **Monitoring**: Abweichungen vom erwarteten Verhalten, Tool-Call-Audit
6. **Policy-Anbindung**: bestehende ISMS-Prozesse um AI-spezifische Controls erweitern

**F: "Du baust OpenClaw — was genau ist das?"**
Kurze, klare Antwort. Du hast das gebaut, also sprich authentisch. Punkte:
- Open-Source-Agenten-Projekt, das du privat entwickelst
- Warum relevant: wer Agentensysteme selbst baut, versteht die Innenseite — Tool-Routing, Context-Handling, Fehlermodi
- Für Beratung: das gibt dir Glaubwürdigkeit bei Kunden, die das Thema abstrakt verhandeln wollen

---

### 3.7 Consulting-Skills & Soft-Fit

**F: "Wie gehst du mit einem Kunden um, der eine Maßnahme ablehnt?"**
- Zuhören, Motiv verstehen (Kosten? Betriebsrisiko? Politik?)
- Optionen darstellen: Risiko akzeptieren (dokumentiert), alternative Controls, stufenweiser Ansatz
- Entscheidung liegt beim Kunden — dein Job ist, die Konsequenz klar zu machen
- Nichts durch die Hintertür diktieren

**F: "Erzähle von einem Projekt, auf das du besonders stolz bist."**
Guter Kandidat: ISMS-Rollout für drei Anwendungen bis Reifegrad 3, ohne externe Begleitung. STAR-Struktur:
- **Situation**: konzernweiter ISMS-Rollout, drei produktive Anwendungen, begrenzte zentrale Unterstützung
- **Task**: Eigenverantwortliche Umsetzung von Schutzbedarf bis Governance-Review-Ready
- **Action**: Schutzbedarfsanalysen mit Fachseite, Risikobewertung, Maßnahmenableitung, Abstimmung mit zentralem CISO-Team, Erstellung revisionssicherer Dokumentation
- **Result**: Reifegrad 3 erreicht, Anwendungen audit-ready, reproduzierbares Vorgehen für weitere Rollouts

**F: "Beschreibe eine Situation, in der du mit Widerstand umgehen musstest."**
Denke an: Fachseite, die den Mehraufwand einer Maßnahme nicht sah, oder technisches Team, das ein Control für unverhältnismäßig hielt. Struktur: Position verstehen, Daten/Risiko-Argument aufbauen, Kompromiss finden (Zeitplan, Kompensationsmaßnahme).

**F: "Wie arbeitest du im Team?"**
Dein Profil: Brückenbauer zwischen Technik, Fachseite, Governance. Nenne, dass du Python-Trainings für das CLS-Team hältst — das zeigt Teaching-Kompetenz und Bereitschaft, Wissen zu teilen.

**F: "Wo siehst du dich in fünf Jahren?"**
Ehrliche Antwort, die zu KPMGs Laufbahnmodell passt: Manager-Level, eigene Projekte, Teilverantwortung für ein Themenfeld (z. B. ISMS + AI-Governance im FS-Kontext). Nicht "mit eigener Firma".

---

### 3.8 Mini-Case / Problem Solving

KPMG-Interviews enthalten manchmal einen kleinen Case. Beispiel:

**Case: "Eine mittelgroße Bank will ein SOC aufbauen. Der CISO fragt dich, wo du anfangen würdest."**

Strukturierte Antwort in 2–3 Minuten:
1. **Klären**: Ist-Zustand (Monitoring-Tools vorhanden?), regulatorische Treiber (DORA-Deadline?), Budget/Timeline, Build vs. Buy?
2. **Priorisierung**: Asset-Inventar + Kronjuwelen identifizieren, Use Cases mit höchstem Risk/Reward zuerst
3. **Target Operating Model**: hybrides Modell (interne Analysten + MSSP für 24/7) als typischer Startpunkt für Mid-Size
4. **Quick Wins**: Logquellen-Onboarding für kritische Systeme, Basis-Use-Cases (Auth-Failures, Malware-Signaturen, DLP-Events)
5. **Roadmap**: 6–12 Monate bis Basis-SOC, danach iterativ MITRE-Coverage erweitern
Schluss: "Was mir wichtig ist — keine Technologieauswahl, bevor Use Cases und Prozesse klar sind. SIEM-Tool ohne Use-Case-Strategie wird zur Alert-Flut."

---

## 4. Deine eigenen Fragen ans Unternehmen

Stelle mindestens drei. Wähle aus:

**Zur Rolle:**
- Wie sieht ein typisches Projekt im FS Technology- und Enabling Services aus — eher Auftrag Greenfield-SOC, oder eher Optimierung bestehender Umgebungen?
- Wie ist das Verhältnis von IAM-, SOC-/SIEM- und Policy-Projekten im Team aktuell verteilt?
- In welcher Phase begleitet ihr Kundenprojekte typischerweise — Analyse, Konzept, Implementierung, Betrieb?

**Zur Entwicklung:**
- Ihr erwähnt Rotationsprogramme — wie gelebt ist das bei FS Technology?
- Was unterscheidet bei euch einen erfolgreichen Senior Consultant nach 12–18 Monaten von einem, der sich schwertut?
- Welche Weiterbildungspfade sind für jemanden mit ISMS-Hintergrund typisch — Richtung Manager, Richtung Spezialisierung (Cloud, AI, IAM)?

**Zu Themen, die dich konkret interessieren:**
- Wie positioniert sich KPMG bei AI-Governance-Beratung im FS-Sektor — gibt es eine dedizierte Praxis oder Querschnittsthema?
- Wie handhabt ihr die Überschneidung zwischen DORA-, NIS2- und ISO-27001-Projekten bei Kunden, die mehrfach im Scope sind?

**Zur Organisation:**
- Wie ist die Reisetätigkeit typischerweise? Projekte tendenziell vor Ort oder remote?
- Wie arbeitet ihr standortübergreifend (Frankfurt, München, Stuttgart)?

---

## 5. Letzter Check vor dem Gespräch

- [ ] Anschreiben und Lebenslauf nochmal durchgehen — alles, was du schreibst, musst du belegen können
- [ ] Einen klaren, dreisätzigen Elevator Pitch parat haben ("Seit 2023 ISMS nach ISO 27001 bei DB Systel…")
- [ ] Drei konkrete Projekt-Stories in STAR-Struktur vorbereitet (ISMS-Rollout, Berechtigungskonzept, Automatisierung)
- [ ] Mindestens zwei Regulatorik-Themen (DORA, NIS2) frisch aufgefrischt
- [ ] Bei SIEM-Tools: ehrlich zu Lücken, zeige Lernbereitschaft — niemals bluffen
- [ ] Eigene Fragen vorbereitet (siehe oben), mindestens drei
- [ ] Notizblock + Stift; Laptop griffbereit bei Remote-Interview; 10 min früher einloggen
- [ ] KPMG-FS-Beratung kurz rechherchieren: Publikationen, aktuelle Studien (z. B. KPMG Cyber Security in Financial Services), LinkedIn-Profile der Interviewer

---

## 6. Rote Flaggen, die du vermeiden solltest

- **Überverkauf deines Scopes**: Nicht behaupten, du verantwortest konzernweite Richtlinien. Dein Scope ist team-/anwendungsbezogen — das ist stark genug.
- **SIEM-Halbwissen**: Wenn du Splunk-SPL nicht kennst, sag das. Fachkollegen bei KPMG merken Bluff sofort.
- **Abwertung des aktuellen Arbeitgebers**: Wechselmotiv positiv formulieren.
- **Generische Beratungsfloskeln**: "Ich will mich weiterentwickeln" ist kein Grund. Spezifisch werden.
- **Keine Fragen stellen**: Wirkt desinteressiert. Immer drei im Köcher.

---

## 7. Schnellreferenz — Begriffe, die sitzen sollten

| Begriff | Kurzdefinition |
|---|---|
| ISMS | Information Security Management System, systematischer Ansatz nach ISO 27001 |
| SoA | Statement of Applicability, Annex-A-Controls mit Anwendbarkeitsbegründung |
| RTO / RPO | Recovery Time / Point Objective, BCM-Kennzahlen |
| MTTD / MTTR | Mean Time To Detect / Respond, SOC-Metriken |
| MITRE ATT&CK | Framework für Angriffs-Taktiken und -Techniken |
| TLPT | Threat-Led Penetration Testing, unter DORA für signifikante Institute |
| RBAC / ABAC | Role- / Attribute-Based Access Control |
| SoD | Segregation of Duties |
| JML | Joiner, Mover, Leaver — IAM-Lifecycle |
| SOC 1 L1/L2/L3 | Level im Security Operations Center, Triage/Analyse/Threat Hunting |
| IOC | Indicator of Compromise |
| TTPs | Tactics, Techniques, Procedures |
| DORA | Digital Operational Resilience Act, EU 2022/2554 |
| BAIT/VAIT/KAIT/ZAIT | BaFin-Rundschreiben IT-Anforderungen Banken/Versicherer/KVGs/ZAGs |
| NIS2 | EU-Richtlinie Cybersicherheit, nationale Umsetzung läuft |
| EU AI Act | EU-Verordnung KI, 2024 in Kraft, gestufte Anwendung bis 2027 |

---

**Viel Erfolg im Gespräch.** Du hast einen klaren fachlichen Kern (ISMS, Risikomanagement, IAM-Praxis), ein seltenes Differenzierungsmerkmal (Agentic AI / Python) und die richtigen Zertifizierungen frisch auf dem Tisch. Die größte Übung ist: ruhig bei SIEM-Lücken bleiben und die Brücke schlagen zwischen dem, was du wirklich kannst, und dem, was KPMG sucht.
