# Interview-Prep — Experte Informationssicherheit mit Schwerpunkt SIEM (m/w/d)

**Unternehmen:** Deutsche WertpapierService Bank AG (dwpbank)
**Rolle:** Experte Informationssicherheit mit Schwerpunkt SIEM
**Datum:** 2026-04-17

---

## 1. Wahrscheinliche Fragen & Antwort-Skizzen

**F:** Stellen Sie sich bitte kurz vor und erzählen Sie, was Sie zur dwpbank führt.

**A-Skizze:** Ich bin seit 2023 Information Security Manager bei der DB Systel, dem IT-Partner der Deutschen Bahn, und betreue dort das ISMS für mehrere produktive Anwendungen nach ISO 27001. Vorher kam ich aus der Sprachdatentechnik — Python, NLP, Terminologiemanagement — und habe mich Schritt für Schritt in die Informationssicherheit hineingearbeitet. Die Stelle hier interessiert mich, weil sie genau den Punkt aufgreift, der mir aktuell fehlt: die operative Seite der Cyberabwehr, also der Weg vom analysierten Risiko zur konkreten Detektionsregel. Und das in einem regulierten Wertpapierumfeld, wo genau diese Verbindung aus Regulatorik und Technik zählt.

**Verbindung:** CV — aktuelle Rolle 02/2026 und ISMS-Tenure seit 03/2023; Anschreiben — "Schritt vom analysierten Risiko zur konkreten Detektionsregel".

---

**F:** Sie haben bislang nicht operativ in einem SIEM-Team gearbeitet. Warum trauen Sie sich die Rolle zu?

**A-Skizze:** Ich gehe offen damit um: Ich habe kein SIEM aufgebaut und keine Detektionsregeln in Produktion geschrieben. Was ich mitbringe, ist die Seite davor — Schutzbedarfsanalysen, Bedrohungs- und Risikoanalysen, Ableitung von Maßnahmen, dokumentierte Nachweise. Das ist die fachliche Grundlage für Use Cases. Parallel habe ich in zwei Jahren vier Security-Zertifizierungen neben dem Job durchgezogen — Security+, Network+, ISO 27001 Lead Implementer, AZ-900. Das Tempo ist ein Indikator für die Lerngeschwindigkeit, die ich auch beim Einstieg in die operative SIEM-Arbeit einbringen würde. Wichtig ist mir, dass wir im Gespräch klären, wie der Einstieg konkret aussieht.

**Verbindung:** Anschreiben — Absatz 4 ("Den operativen SIEM-Aufbau bringe ich nicht aus eigener Praxis mit"); CV — Zertifizierungsliste.

---

**F:** Wie würden Sie an eine Bedrohungsanalyse herangehen, um daraus eine Detektionsregel abzuleiten?

**A-Skizze:** Ich fange von der Asset-Seite an: Welche Anwendung, welcher Schutzbedarf, welche Angriffsvektoren sind relevant? Das ist im Grunde derselbe Einstieg wie bei einer Schutzbedarfsanalyse. Danach würde ich mir das passende MITRE-ATT&CK-Mapping für die Technik ansehen — also welche Techniken greifen tatsächlich diese Anwendung an — und von dort aus auf die Protokollquellen gehen: welche Logs habe ich, welche Events zeigen das Verhalten. Die Regel selbst ist dann nur der letzte Schritt, aber aus meiner Sicht der einfachste, wenn Kontext und Logquelle sauber definiert sind. Ehrlich gesagt: Ich habe das bislang bis zum Punkt "Maßnahme ableiten" gemacht, nicht bis zur produktiven Regel im SIEM. Aber der methodische Rahmen ist derselbe.

**Verbindung:** CV — Schutzbedarfsanalysen und Risikobewertungen; ehrlicher Hinweis auf Gap.

---

**F:** Welche regulatorischen Anforderungen treiben eine SIEM-Funktion bei einem Wertpapierdienstleister?

**A-Skizze:** DORA ist aktuell das zentrale Thema — also verpflichtendes ICT-Risk-Management, Incident-Reporting innerhalb enger Fristen, Testing der digitalen Betriebsstabilität. Daneben BAIT beziehungsweise MaRisk für die bankaufsichtlichen Anforderungen und BSI-Grundschutz oder ISO 27001 als Rahmen für das ISMS selbst. Für die SIEM-Funktion bedeutet das konkret: Log-Erfassung muss nachweisbar sein, Alerts müssen klassifiziert und eskaliert werden können, und man braucht belegbare Zeiten für Erkennung und Reaktion. Ich habe DORA und BSI konzeptionell über die PECB- und CompTIA-Zertifizierungen aufgearbeitet und arbeite bei DB Systel mit ISO 27001 produktiv.

**Verbindung:** Anschreiben — "DORA, BSI-Grundschutz und Cloud-Sicherheit konzeptionell abgedeckt"; CV — PECB ISO 27001 Implementer.

---

**F:** Wie gehen Sie mit der Steuerung externer Dienstleister um — speziell wenn es um SIEM-Operations geht?

**A-Skizze:** In meiner aktuellen Rolle arbeite ich ohnehin in einem Dreieck aus Anwendungsbetrieb, zentralem CISO-Team und Fachbereich. Das ist strukturell nah an Dienstleistersteuerung — klare Leistungserwartung formulieren, Nachweise einfordern, die Übergabepunkte sauber definieren. Bei einem SIEM-Dienstleister käme hinzu, dass ich die fachlichen Regeln und False-Positive-Bewertungen selbst verantworten muss, während der Dienstleister den Betrieb macht. Das heißt, ich muss genau wissen, was ich detektiert haben will — sonst läuft die Steuerung ins Leere. Diese Erwartungsklärung ist für mich der wichtigste Teil der Zusammenarbeit.

**Verbindung:** CV — Abstimmung mit zentralem CISO-Team und Stakeholdern; Anschreiben — "Steuerung externer Dienstleister".

---

**F:** Erzählen Sie von einem Projekt, in dem Sie eigenständig Verantwortung übernommen haben.

**A-Skizze:** Der ISMS-Rollout für drei produktive Anwendungen bei der Deutschen Bahn. Ich habe das ohne externe Koordinationsunterstützung bis Reifegrad 3 durchgezogen — also Schutzbedarfsanalysen, Risikobewertungen, technische und organisatorische Maßnahmen, revisionssichere Dokumentation, Governance-Reviews. Der Lernweg war steil, weil ich parallel in die Methodik reingewachsen bin. Was ich daraus mitnehme: Man kommt in der Informationssicherheit nur weiter, wenn man Fachbereich, Betrieb und Governance gleichzeitig abholt. Das ist kein Schreibtischthema.

**Verbindung:** CV — 03/2023–01/2026 DB AG, erster Bulletpoint ("Reifegrad 3 ohne externe Koordinationsunterstützung").

---

**F:** Wie bewerten Sie einen Security-Event, wenn er über Nacht als Alert reinkommt?

**A-Skizze:** Ich würde strukturiert vorgehen: Erstens, ist der Alert überhaupt relevant — also welche Asset-Klasse, welcher Schutzbedarf, ist das Produktion oder Test? Zweitens, was sagt der Kontext — gleichzeitig weitere Alerts, ungewöhnliche Uhrzeit, bekannte IOCs? Drittens, welche Eskalationsstufe passt — Incident-Manager informieren, Containment prüfen, oder zunächst weiter beobachten? Mir ist bewusst, dass ich die konkrete Triage-Routine noch aufbauen muss. Was ich mitbringe, ist der klare Kopf für diesen Kategorisierungsschritt — der liegt nah am Risikomanagement-Denken, das ich täglich mache.

**Verbindung:** CV — Risikobewertung und Umsetzung von Sicherheitsmaßnahmen im laufenden Betrieb; ehrlicher Hinweis auf Aufbau der operativen Routine.

---

**F:** Die Umgebung hier ist hybrid — Azure und On-Prem. Was haben Sie im Cloud-Bereich schon gemacht?

**A-Skizze:** Meine Cloud-Basis ist Microsoft AZ-900 — also die Fundamentals, was Azure an Diensten, Identitäten und Sicherheitskonzepten bietet. In meiner aktuellen Rolle habe ich mit Cloud-Anwendungen im Rahmen von Schutzbedarfsanalysen und Risikobewertungen zu tun, also Shared-Responsibility-Fragen, Identity-Kontrollen, Datenklassifizierung. Tief in Azure Sentinel oder Defender-Log-Pipelines bin ich noch nicht — das wäre für mich ein klarer Einarbeitungspunkt in den ersten Monaten. Was ich dafür mitbringe, ist Grundverständnis für Netzwerk und Systeme über Network+ und Security+.

**Verbindung:** CV — Microsoft AZ-900, CompTIA Network+ und Security+; ehrliche Positionierung der Cloud-Tiefe.

---

**F:** Ihr Hintergrund startet im Übersetzen — wie passt das zur Informationssicherheit?

**A-Skizze:** Auf den ersten Blick ist das ein Sprung, auf den zweiten gar nicht. Als Language Data Engineer bei der Deutschen Bahn habe ich zwei konzernweite Anwendungen fachlich administriert, Prozesse automatisiert, Architekturdokumentation geschrieben. Das ist schon fachliche Nähe zu Anwendungen und Betrieb. Die Informationssicherheit kam dazu, weil ich gemerkt habe: Governance, Risikodenken und klare Dokumentation sind genau die Disziplinen, in denen ich meine Sprach- und Präzisionsarbeit auf technische Kontexte anwenden kann. Der Wechsel war bewusst, nicht zufällig.

**Verbindung:** CV — Karrierelinie Übersetzer → Language Data Engineer → ISMS; eigenes Narrativ dazu.

---

**F:** Sie bringen Python und NLP mit. Ist das für eine SIEM-Rolle überhaupt nützlich?

**A-Skizze:** Ja, an zwei Stellen. Erstens: Log-Verarbeitung ist am Ende Textverarbeitung — Parser schreiben, Regex optimieren, Anomalien in Events suchen. Da liegt Python nah dran. Zweitens: Ich arbeite bei DB Systel produktiv mit agentischer Automatisierung, n8n und ein eigenes Open-Source-Projekt. Das heißt, ich habe ein praktisches Bild davon, wie Toolketten Logs erzeugen und welche Muster auf abnormales Verhalten hindeuten. Und ich kenne die Risiken — Prompt Injection, unkontrollierte Tool-Calls, Datenabflüsse — aus der Praxis. Diese Klasse von Bedrohungen landet in den nächsten Jahren auch in den Modellen eines Wertpapierdienstleisters.

**Verbindung:** CV — Python/NLP im Language-Data-Engineer-Teil; Anschreiben — Absatz 3 (agentische Automatisierung).

---

**F:** Wie würden Sie einem Fachbereich ohne IT-Hintergrund einen kritischen Security-Vorfall erklären?

**A-Skizze:** Ich fange mit der Geschäftswirkung an, nicht mit der Technik: Was kann nicht mehr, was ist gefährdet, welche Entscheidung steht an. Erst danach gehe ich so weit ins Detail, wie der Gegenüber es braucht. Genau das mache ich in der aktuellen Rolle regelmäßig — Schutzbedarfsanalysen mit Fachbereichen, Risikobewertungen, bei denen die Geschäftsseite die Treiber mitbringt. Und seit Anfang 2026 vermittle ich meinem Team Python- und NLP-Grundlagen. Sicherheitsthemen so zu erklären, dass sie ankommen, ist mir wichtig.

**Verbindung:** Anschreiben — "Sicherheitsthemen so zu erklären, dass sie ankommen"; CV — Python-Schulungen Team, Stakeholder-Kommunikation.

---

**F:** Warum ein Wechsel — und warum gerade jetzt?

**A-Skizze:** Ich bin in der aktuellen Rolle nicht frustriert, im Gegenteil. Aber ich merke, dass ich an der Grenze dessen angekommen bin, was ich im bestehenden Setup an Tiefe in Richtung operative Sicherheit aufbauen kann. Die ISMS-Governance habe ich mir solide erarbeitet; der nächste logische Schritt ist die Detektion- und Response-Seite — und zwar in einem Umfeld, in dem Regulatorik und Technik ohnehin eng verschränkt sind. Ein Wertpapierdienstleister wie die dwpbank ist genau dieses Umfeld. Jetzt deshalb, weil ich mit den aktuellen Zertifizierungen eine saubere Basis habe, auf der ein Einstieg in die SIEM-Arbeit realistisch ist.

**Verbindung:** Anschreiben — Opening und Absatz 4; persönliche Entwicklungslogik.

---

**F:** Wie halten Sie sich in der Informationssicherheit auf dem Laufenden?

**A-Skizze:** Zwei Wege. Einmal über die strukturierten Weiterbildungen — ich habe in zwei Jahren Security+, Network+, ISO 27001 LI und AZ-900 gemacht, das zwingt einen, Themen systematisch zu durchdringen. Zweitens über die Arbeit selbst: Ich lese BSI-Publikationen zu aktuellen Bedrohungen, verfolge DORA-Umsetzungsfragen, und mein privates OpenClaw-Projekt zwingt mich, Risiken neuer Technologien aus der Angreifer- und Verteidigerperspektive zu denken. Das ist kein passives Nachrichtenlesen, sondern fachliche Praxis.

**Verbindung:** CV — vier Zertifizierungen 2025/2026; Anschreiben — OpenClaw und agentische AI-Praxis.

---

**F:** Wo sehen Sie sich in fünf Jahren?

**A-Skizze:** Realistisch: als jemand, der die Verbindung zwischen ISMS-Governance und operativer Cyberabwehr sauber abdeckt — also jemand, der eine Detektionsregel schreiben oder einen Incident triagieren kann und gleichzeitig die regulatorische Einbettung mitdenkt. Ob das in fünf Jahren eine fachliche Spezialistenrolle ist oder stärker Richtung Team- oder Themenführung geht, lasse ich bewusst offen. Mir ist wichtig, dass ich in der Tiefe bleibe und nicht zu schnell in eine rein managende Rolle abdrifte.

**Verbindung:** persönliche Entwicklungsrichtung; keine Überversprechen.

---

## 2. Lücken & Risiken

**Risiko:** Kein eigenständiger SIEM-Aufbau und keine produktive Detektionsregel-Erfahrung.

**Warum es thematisiert werden könnte:** Die Aufgabenbeschreibung nennt SIEM-Betrieb, Detektionsregeln und Security-Event-Bewertung als zentrale Tätigkeiten. Das Team ist klein (9), also ist die Einarbeitungszeit ein kalkulatorischer Faktor.

**Framing-Vorschlag:** Offen benennen — kein Blendwerk. Gegenwicht: methodische Nähe durch Schutzbedarfs- und Risikoanalysen, belegte Lerngeschwindigkeit (vier Security-Zertifizierungen in zwei Jahren), und ISMS-Rollout bis Reifegrad 3 im Alleingang. Vorschlag, konkret über den Einstiegsweg zu sprechen.

---

**Risiko:** Azure- und Cloud-Tiefe bleibt bei AZ-900-Niveau.

**Warum es thematisiert werden könnte:** Die Rolle betont explizit "hybride On-Prem/Cloud-Umgebung (insbesondere Azure)". Ein Experte soll die Cloud-Seite mittragen.

**Framing-Vorschlag:** AZ-900 als solide Fundament positionieren, kombiniert mit CompTIA Network+ und Security+ für Netz- und Systemgrundlagen. Ehrlich sagen: Sentinel, Defender oder produktive Azure-Log-Pipelines sind Einarbeitungspunkte in den ersten drei bis sechs Monaten. Konkret fragen, welche Azure-Produkte im Einsatz sind.

---

**Risiko:** Erstmals im Bankensektor — keine Wertpapier- oder Finanzdienstleistungserfahrung.

**Warum es thematisiert werden könnte:** Regulatorik im Wertpapiergeschäft hat eigene Ausprägungen (MaRisk, BAIT, WpHG-Aspekte), und Kulturpassung im regulierten Umfeld ist ein häufiges Thema.

**Framing-Vorschlag:** Die Deutsche Bahn AG ist selbst ein stark regulierter Konzern mit eigener Governance-Tiefe — ISO 27001 funktioniert branchenübergreifend. DORA, BSI-Grundschutz, ISO 2700x sind konzeptionell vertraut. Den Sektorwechsel als bewusste Entscheidung benennen: Wertpapierumfeld ist dicht an Regulatorik und Technik, genau die Kombination, die interessiert.

---

**Risiko:** Ungewöhnlicher Karriereweg — Übersetzer, Language Data Engineer, Information Security Manager.

**Warum es thematisiert werden könnte:** Interviewer fragen sich, ob das konsequent verfolgt wurde oder ob hier jemand noch sucht.

**Framing-Vorschlag:** Die Linie offensiv erzählen: Sprache → Datenprozesse → Anwendungsadministration → Informationssicherheit. Jeder Schritt baute auf dem vorigen auf und vertiefte Verständnis für Anwendungen, Betrieb und Governance. Kein Zickzack, sondern eine aufgeschichtete Biografie. Der aktuelle Wechsel in die operative SIEM-Arbeit ist der logische nächste Baustein, nicht ein Neuanfang.

---

**Risiko:** ISMS-Tenure seit 03/2023 ist für eine Expertenrolle eher mittellang.

**Warum es thematisiert werden könnte:** Der Begriff "Experte" in der Jobbezeichnung suggeriert mehrjährige Tiefe. Drei Jahre ISMS kann knapp wirken, wenn der Interviewer strenge Maßstäbe anlegt.

**Framing-Vorschlag:** Nicht in die Defensive — über Inhalt statt Dauer argumentieren. Drei Jahre, davon ein Rollout bis Reifegrad 3 im Alleingang, plus vier Security-Zertifizierungen parallel. Die Tiefe ist nicht Zeitfunktion, sondern Intensität. "Experte" im Sinne der Rolle muss auch die SIEM-Seite abdecken — das ist der Teil, in den ich mit dieser Rolle hineinwachse.

---

## 3. Gesprächs-Highlights

- **ISMS-Rollout Reifegrad 3 im Alleingang:** Drei produktive Anwendungen bei der Deutschen Bahn AG — Schutzbedarfsanalysen, Risikobehandlung, revisionssichere Dokumentation, Governance-Reviews, ohne externe Koordinationsunterstützung. Belastbares Signal für Eigenständigkeit und methodische Umsetzungsstärke.
- **Vier Security-Zertifizierungen in zwei Jahren neben dem Job:** PECB ISO 27001 Lead Implementer, CompTIA Security+, CompTIA Network+, Microsoft AZ-900. Indikator für Lerngeschwindigkeit und systematischen Aufbau der regulatorischen und technischen Basis.
- **Agentische AI in der Praxis:** n8n-Automatisierungen bei DB Systel im Arbeitsalltag, dazu OpenClaw als privates Open-Source-Projekt. Konkretes Bild davon, wie Toolketten Logs erzeugen, und praktisches Verständnis für agentische Risiken (Prompt Injection, unkontrollierte Tool-Calls, Datenabflüsse) — relevant für zukünftige Bedrohungsmodelle im Finanzsektor.
- **Python- und NLP-Schulungen für das eigene Team:** Eigenständig konzipiert, praxisnah vermittelt. Belegt, dass komplexe technische Themen anschlussfähig erklärt werden können — direkt übertragbar auf die Fachbereichs-Beratung im SIEM-Alltag.

---

## 4. Fragen an das Unternehmen & Recherche

### Fragen, die Lutz stellen kann

**Team & Rolle**

- Wie ist das 9-köpfige Team aufgestellt — wie viele Kolleg:innen sitzen primär auf SIEM-Operations, wie viele auf Schwachstellenmanagement und Penetrationstests, und wie arbeiten die Schwerpunkte zusammen?
- An wen berichtet die Rolle direkt, und wie ist die Schnittstelle zum CISO und zum ISMS-Team organisiert?
- Ist die Stelle neu geschaffen oder wird sie nachbesetzt? Falls nachbesetzt: Was hat der Vorgänger hinterlassen, und wo liegen die offenen Baustellen?

**Technik & Prozesse**

- Welches SIEM-Produkt ist im Einsatz, und wie weit ist die Ablösung oder Weiterentwicklung im Lifecycle fortgeschritten?
- Wie ist die Arbeitsteilung mit den externen Dienstleistern für SIEM-Operations heute geschnitten — was bleibt inhouse, was ist ausgelagert?
- Welche Log-Quellen sind bereits onboarded, und welche gelten aktuell als Lücke?
- Wie groß ist der Azure-Anteil der Sicherheitstelemetrie, und wird Sentinel, Defender oder eine Drittlösung für die Cloud-Detektion eingesetzt?

**Erwartung & Entwicklung**

- Wie würden aus Ihrer Sicht die ersten 90 Tage in der Rolle aussehen, und woran messen Sie Erfolg nach sechs Monaten?
- Wie offen ist das Team für jemanden, der aus der ISMS-Governance kommt und die operative SIEM-Tiefe hier aufbauen will — gibt es Pairing, Mentoring, strukturierte Einarbeitung?

**Richtung**

- Wie weit ist die DORA-Umsetzung im Haus fortgeschritten, und welche Auswirkungen hat das konkret auf die Priorisierung im SIEM-Team?
- Welche Rolle spielt AI-basierte Detektion in der aktuellen Strategie — wird das eher passiv beobachtet oder aktiv pilotiert?

### Recherche-Check

- Interviewer-Namen und LinkedIn-Profile — Rolle, Tenure, fachlicher Fokus
- Aktuelle Pressemitteilungen der dwpbank zu WP3, Cloud-Migration, Partnerschaften oder Regulatorik
- DORA-Umsetzungsstand im deutschen Wertpapier-Sektor — BaFin-Statements, Branchen-Publikationen
- Öffentlich bekannte Sicherheitsvorfälle oder -maßnahmen bei Wertpapierdienstleistern der letzten 12 Monate
- kununu- und Glassdoor-Profile der dwpbank — auffällige Muster zu Interviewstil oder Teamkultur
- BaFin- und EZB-Anforderungen an Banken-SIEM (BAIT, MaRisk-relevante Passagen)
- dwpbank-Struktur: Abteilung "Operative Sicherheit, Regulatorik, Cybersicherheit" im Organigramm — wer leitet, welche Standorte
