---
name: interview-prep
description: Generate a tailored German interview-prep document for Lutz Molderings from a specific vacancy, his CV, and his cover letter. Trigger whenever the user wants to prepare for, practice, or rehearse a job interview, mentions "Vorstellungsgespräch", "Bewerbungsgespräch", "Interview-Vorbereitung", "interview prep", "practice interview", "get ready for the interview", "prep for [company] interview", or is working inside a `job-applications/<company>` folder and asks for interview support — even when the word "skill" is never used. Always use this skill when interview preparation is the task and an application folder is in scope.
---

# Interview Prep

Generate German interview preparation material for Lutz Molderings, grounded strictly in his real application (CV + cover letter) and the specific vacancy. Produce both a `.md` and a `.docx` (via python-docx).

The prep document has four sections, each with its own purpose:

1. **Wahrscheinliche Fragen & Antwort-Skizzen** — the 10–15 questions an interviewer is most likely to ask for this role, each with a concrete draft answer grounded in Lutz's CV or cover letter.
2. **Lücken & Risiken** — weak spots in the application the interviewer may probe (missing requirements, thin experience, potential contradictions), with suggested framing.
3. **Gesprächs-Highlights** — the strongest achievements, numbers, and stories Lutz should weave into answers regardless of which question comes up.
4. **Fragen an das Unternehmen & Recherche** — smart, role-specific questions Lutz should ask the interviewer, plus a pre-interview research checklist.

---

## Step 1 — Locate sources

Work inside `/Users/canystrix/dev/job-applications/<company>/`. The application folder is the canonical source of truth.

Find these three inputs in priority order. If any is missing, stop and ask the user — don't generate prep from partial data.

**Vacancy**
1. `vacancy-*.md` in the company folder (already extracted in canonical form)
2. A `.md` file whose name matches the role title (older pattern from some folders)
3. A `.pdf` file containing the posting — extract with pdfplumber:
   ```python
   import pdfplumber
   with pdfplumber.open("<path>") as pdf:
       text = "\n".join(page.extract_text() or "" for page in pdf.pages)
   ```
   Save as `vacancy-<role-slug>.md` if it isn't already saved — future runs should use the canonical markdown.

**Cover letter (Anschreiben)**
1. `anschreiben-lutz-molderings-<company>.md` (preferred — clean text)
2. `anschreiben-lutz-molderings-<company>.docx` — read with python-docx:
   ```python
   from docx import Document
   text = "\n".join(p.text for p in Document("<path>").paragraphs)
   ```
3. `Anschreiben.pdf` — extract with pdfplumber

**CV (Lebenslauf)**
1. `lebenslauf-lutz-molderings-<company>.md` or `.docx` in the company folder
2. Otherwise, the master CV at `/Users/canystrix/dev/job-applications/lebenslauf.pdf` — extract with pdfplumber. This is the canonical CV and is expected in most runs.

Read all three sources completely before drafting. The quality of the prep depends on how well you've understood the specific vacancy and how it matches Lutz's application.

---

## Step 2 — Analyze

Before writing, produce a short internal mapping (it's fine to show this to the user too):

- **Role type** — ISMS/GRC, SIEM/SOC, consulting, cloud security, audit, etc. This decides which angle of Lutz's profile dominates the answers.
- **Must-have requirements** → which CV/cover-letter points cover each one.
- **Nice-to-have requirements** → same mapping.
- **Gaps** — requirements not covered, or only weakly covered, by Lutz's profile. These are the risks to address in section 2.
- **Company tone** — formal/traditional vs. modern/casual (inferred from how the posting is written). Adjust formality of the prep language accordingly; the whole output stays in German.

**Factual constraints — apply to every Q&A sketch, risk framing, highlight bullet, and company question in this document.**

These constraints mirror the `/cover-letter` skill. Treat every sentence in every section as a claim that must map to the profile below. If you cannot point to the exact CV entry, certification, or experience item that backs a phrase, rewrite it. When in doubt, acknowledge the gap (in Section 2 or directly in the A-Skizze) rather than soften a claim into dishonest territory.

### Employer and timeline

- **2023 start was at Deutsche Bahn AG, NOT at DB Systel.** Lutz began ISMS work in March 2023 at the DB AG inside the unit **Corporate Language Solutions (CLS)**. He moved to **DB Systel GmbH** only in February 2026.
  - Q&A sketches must reflect this accurately. Typical interviewer questions like "Seit wann sind Sie im ISMS tätig?" or "Wie lange sind Sie schon bei DB Systel?" are landmines if the prep doc treats 2023 and DB Systel as the same.
  - **Write:** "Seit 2023 im Information Security Management, zunächst bei der DB AG in der Einheit Corporate Language Solutions, seit Anfang 2026 bei DB Systel im Rahmen eines internen Wechsels."
- **DB Systel identification.** Always: "DB Systel GmbH, dem IT-Partner der Deutschen Bahn" — not "Infrastrukturdienstleister" or just "Deutschen Bahn".

### Role title and scope

- **Lutz's official internal role title is "Sekundärassetverantwortlicher"**, a DB-konzerninterne Rollenbezeichnung. "Information Security Manager" is the functional/market-standard description used in CV and Anschreiben. In the interview, Lutz must be able to state this distinction if asked about his formal title. **Include this as a pre-baked Q&A in Section 1** whenever the vacancy is non-DB-familiar:
  > *"Wie lautet Ihre offizielle Stellenbezeichnung?"* → *"Meine interne Bezeichnung bei DB ist Sekundärassetverantwortlicher. Das ist die DB-konzerninterne Rolle für die Informationssicherheit eines definierten Anwendungs-Assets — funktional entspricht das einem Information Security Manager mit anwendungsbezogenem Scope, analog zur Rollenlogik nach ISO/IEC 27001."*
- **ISMS scope is team- and application-level, never corporate-wide.** Lutz is Sekundärassetverantwortlicher for three productive applications of his own team. He does NOT own corporate-wide policies, does NOT cover other teams/units, does NOT speak for the whole DB group.
  - **Never write:** "konzernweiter ISMS-Kontext", "konzernweite Richtlinien", "konzernweites ISMS", "verantworte konzernweit"
  - **Write instead:** "Anwendungen und Assets in meinem Verantwortungsbereich", "im Rahmen des ISMS meines Teams", "anwendungsbezogen", "auf Team-Ebene"
- **The governance role belongs to the CLS unit, not to Lutz personally.** Do not attribute unit-level governance responsibility to Lutz.

### Framework experience ladder

Strict. Do not upgrade a framework into a higher tier in A-Skizzen, Highlights, or Framing-Vorschläge.

| Framework | Tier | Allowed phrasing |
|---|---|---|
| ISO/IEC 27001 | **Operational** — daily work, PECB-certified | "Tagesgeschäft", "seit 2023 verantwortlich", "PECB-zertifiziert" |
| BSI IT-Grundschutz | **Indirect** — only via the konzerninternes DB-Schema that is BSI-oriented | "im DB-Umfeld über ein am BSI-Schema orientiertes konzerninternes Modell", "konzeptionell bekannt" — NEVER "operativ" oder "fließt kontinuierlich ein" |
| NIST (CSF / 800-53) | **Conceptual only** — no production use | "als Rahmen bekannt", "konzeptionell vertraut" — NEVER "operativ", "im Alltag" |
| EU-DORA | **Conceptual only** | "als regulatorischer Rahmen bekannt", "konzeptionell abgedeckt" — NEVER "setze um" |
| NIS2 | **Conceptual only** | "beobachte aktiv", "als Rahmen bekannt" — NEVER "fließt kontinuierlich ein" |

**If the vacancy names a framework that falls into "Indirect" or "Conceptual only", automatically include in Section 1:**
1. A question like *"Wo liegen Ihre Schwerpunkte bei [Framework X]?"* with an honest A-Skizze that downgrades to the correct tier.
2. A **Kurzbriefing** sub-block directly below that A-Skizze with 3–6 bullets of factual background on the framework (scope, authority, pillars, key terms) so Lutz can use the vocabulary correctly in the interview without overclaiming experience.

### Audit experience

- **No external audit-Begleitung.** Lutz has never led or independently accompanied an external audit.
- **Internal audit:** Teilnahme an einer internen Prüfung nach Abschluss des ISMS-Rollouts auf Reifegrad 3.
- If the vacancy mentions "Begleitung interner und externer Audits", this is a Section-2 risk by default. A-Skizzen must not claim audit-Begleitung as existing experience.

### Tools and systems

- **No ServiceNow experience.** If the vacancy names it, include a ServiceNow Q in Section 1 with an honest A-Skizze ("produktiv noch nicht gearbeitet") plus a **Kurzbriefing** block (IRM modules, continuous compliance, integration with ITSM).
- **DB-internal tools (SESAM, IRMA, …)** are DB-konzerninterne Systeme without public documentation. In Q&A sketches, describe them by function, not by name ("internes Risikomanagement-Tool", "zentrales Dokumentationssystem"). If Lutz would mention a DB-internal tool in a specific answer, add a side-note: "Achtung — außerhalb der DB-Welt unbekannt, Name nur in Kombination mit funktionaler Übersetzung nennen."

### Awareness vs. Wissensvermittlung

- **Lutz's Python/NLP training is Wissensvermittlung im eigenen Team, NOT Security Awareness.** A-Skizzen and Highlights must not frame Python/NLP training as security-awareness experience. If the vacancy asks for Awareness-Maßnahmen, the A-Skizze should build the bridge explicitly ("Der didaktische Ansatz ist übertragbar, Security-Awareness-Formate sind für mich der nächste Schritt") rather than conflating the two.

### CLS transformation and BahnGPT / RAG context (the strongest AI-Governance anchor)

- The CLS unit has shifted from pure translation/interpreting toward providing language-based knowledge infrastructure for the DB group. CLS's curated multilingual terminology database (with ontological relations) feeds downstream systems: the **Konzernregelwerksdatenbank**, Autorenunterstützungsprogramme, the group's **machine translation service**, and the **RAG layer of BahnGPT (DB's internal LLM)**.
- Lutz's LDE role puts him at the **data layer of a productive enterprise AI system**. For vacancies touching AI, LLMs, data governance, or AI-security: surface this as a highlight and Q&A anchor. It is a genuine differentiator that most candidates in ISMS roles do not have.
- **Caveat:** Do not describe BahnGPT architecture in detail — it's a DB-internal system and specifics are likely NDA. Stay at the functional level ("Terminologiedatenbank liefert Grounding-Daten für die interne RAG-Implementation").

### Mirror Anschreiben overclaims into Section 2

If the Anschreiben contains a framework/experience claim that the framework-ladder above would downgrade — for example "BSI IT-Grundschutz fließt kontinuierlich in meine Arbeit ein" while the ladder says BSI is indirect — then that claim MUST appear in Section 2 as a risk with a framing suggestion that lets Lutz reconcile the cover-letter tone with the truthful scope in the interview, WITHOUT openly disowning the Anschreiben.

This is the rule that failed in the first run of this prep — A-Skizzen silently inherited cover-letter overclaims instead of catching them. Every Anschreiben claim must be cross-checked against the framework ladder, the audit rule, and the tools rule before writing A-Skizzen.

### The no-fabrication rule

If the vacancy asks for something not in the profile, acknowledge the gap in Section 2 and give an honest framing. Proactive gap-naming is a trust signal, not a weakness.

---

## Step 3 — Draft the four sections (in German)

All content in German. Use natural, spoken-sounding German in the answer sketches — this is for speaking practice, not written correspondence. The same "not AI-generated connector phrases" rule from the cover-letter skill applies here too: avoid stilted bureaucratic German and noun-heavy constructions. Prefer verbs over nominalisations.

### Section 1 — Wahrscheinliche Fragen & Antwort-Skizzen

Produce 10–15 questions. Cover this mix:

- **Fachliche Fragen** — specific to the role. For an ISMS role: Schutzbedarfsanalyse-Vorgehen, ISO 27001 Annex-A-Controls, Risikobehandlungsoptionen. For a SIEM role: Use-Case-Entwicklung, Alert-Tuning, SOC-Workflows. For consulting: Kundenkommunikation, Projektaufbau. Calibrate to the vacancy.
- **Situative / Erfahrungsfragen** — "Erzählen Sie von einem Projekt, in dem…", "Wie sind Sie mit … umgegangen?" Draw on concrete items from the CV.
- **Motivations- und Fit-Fragen** — "Warum dieser Arbeitgeber?", "Warum jetzt ein Wechsel?", "Warum diese Rolle?"
- **Schwierige Fragen** tied directly to the gaps identified in section 2. These are the ones Lutz most needs to rehearse.
- **Karrierefragen** — "Wo sehen Sie sich in fünf Jahren?" — only if realistic for the role level.

**Always include, regardless of role:**

- A **Hintergrund / Karrierepfad** question ("Ihr Hintergrund ist ungewöhnlich — Übersetzer → Language Data Engineer → ISMS. Wie kam das?"). The A-Skizze should reflect Lutz's real narrative: translator as not-long-term; systematically took on PM/admin/Anwendungsverantwortung; LDE was a hoped-for engineering pivot that stayed niche; ISMS is the first field with a clear career path; systematic certification progression (PECB + CompTIA Sec+/Net+ + AZ-900; CISM + CISSP planned).
- A **Language Data Engineer — what exactly?** question, because the dual title in the current role (ISM + LDE) almost always triggers it. The A-Skizze must include the CLS transformation from pure language service to knowledge infrastructure, the curated terminology database with ontological relations, and the downstream systems it feeds (Konzernregelwerksdatenbank, Autorenunterstützungsprogramme, MT, BahnGPT RAG). Framing: the LDE role puts Lutz at the data layer of a productive AI system — concrete, not theoretical.
- The **official title clarification** (Sekundärassetverantwortlicher ↔ Information Security Manager) whenever the interviewer is unlikely to know DB-internal nomenclature.
- A **Motivations- und Wechselfrage** that honestly reflects: scope expansion (currently only own-team apps), structural context at DB (Einstellungsstopp + Stellenabbau), LDE-niche plateau. Do NOT include missing-Gehaltserhöhung as the primary reason in the main A-Skizze — keep it as a *"Falls Nachfrage"* sub-block the interviewer can trigger, not volunteered upfront.

Format each entry exactly like this:

```
**F:** <Frage>

**A-Skizze:** <2–4 Sätze, als wären sie gesprochen — nicht vorgelesen. Konkret, in der Ich-Form, mit Bezug auf eine echte Erfahrung aus Lebenslauf oder Anschreiben.>

**Verbindung:** <kurzer Hinweis, auf welchen Punkt aus Lebenslauf/Anschreiben sich die Antwort stützt>
```

The A-Skizze is a draft, not a script. One well-matched example is better than a dump of every relevant achievement. Natural spoken German over polished written German — contractions, one-clause sentences, personal phrasing are all welcome.

### Section 2 — Lücken & Risiken

Identify 3–6 realistic risks the interviewer may probe. For each:

```
**Risiko:** <knapp: was fehlt oder angreifbar ist>

**Warum es thematisiert werden könnte:** <Interviewer-Logik — warum diese Lücke aus Sicht des Unternehmens relevant ist>

**Framing-Vorschlag:** <ein bis zwei Sätze, wie Lutz den Punkt ehrlich und souverän einordnet — ohne zu beschönigen und ohne sich kleinzureden>
```

Types of risk to look for:

- Certifications the vacancy requires that Lutz does not hold
- Tools or frameworks named in the vacancy but absent from the CV (e.g. specific SIEM products, GRC tools)
- Industry switch — first time in this sector (Versicherung, Banking, Öffentlicher Dienst, Beratung)
- Level or scope mismatch — e.g. senior role where Lutz's ISMS tenure is shorter than typical, or "konzernweit" language in the posting vs. his team-scoped experience
- Unusual career path — translator → NLP → ISMS can raise "warum der Wechsel?" questions
- Consulting-specific concerns if he's applying to a consulting firm without prior consulting experience

Do not invent weaknesses. If the profile honestly covers a requirement, don't manufacture doubt.

### Section 3 — Gesprächs-Highlights

3–5 bullets — the strongest, most memorable stories or facts Lutz should drop into any fitting answer. Each entry:

```
- **<Schlagwort>:** <ein bis zwei Sätze, konkretes Detail — keine Abstrakta>
```

Source these from the cover-letter's differentiator paragraph and the strongest CV bullets. Typical highlights:

- **ISMS-Rollout Reifegrad 3:** Drei produktive Anwendungen eigenverantwortlich bis Reifegrad 3 gehoben — ohne externe Koordinationsunterstützung, inklusive Schutzbedarfsanalyse, Risikobehandlung, revisionssicherer Nachweisdokumentation.
- **AI-Datenebene + Agentic AI:** Über die LDE-Rolle operativer Kontakt mit der Datenebene eines produktiven AI-Systems — die CLS-Terminologiedatenbank liefert Grounding-Daten für die RAG-Implementation von BahnGPT (DB-interner LLM-Dienst) sowie die Konzernregelwerksdatenbank und Autorenunterstützungsprogramme. Ergänzend produktive n8n-Automatisierungen und OpenClaw als privates Open-Source-Agenten-Framework. Verständnis für agentische Risiken (unkontrollierte Tool-Calls, Datenabflüsse, Prompt Injection) und die AI-Datengovernance-Seite von innen. Für AI-Governance-nahe Rollen der stärkste Differentiator.
- **Systematische Zertifizierungsdichte:** PECB ISO/IEC 27001 Implementer, CompTIA Security+ und Network+, Microsoft Azure Fundamentals — in zwei Jahren neben laufender ISMS-Verantwortung aufgebaut. CISM und CISSP als nächste Schritte geplant.
- **Wissensvermittlung im Team:** Seit Anfang 2026 Python- und NLP-Schulungen für das eigene Team, Inhalte selbst konzipiert — belastbarer Beleg für didaktischen Ansatz. (Nicht als Security Awareness deklarieren.)
- **Duale Expertise:** Sprachtechnologie/NLP + Informationssicherheit — selten und gerade für AI-Governance-nahe Rollen relevant.

Pick what actually fits the role — don't include all five if only two or three match. For AI/LLM/data-governance-adjacent roles, the AI-Datenebene-Highlight is almost always the right lead.

### Section 4 — Fragen an das Unternehmen & Recherche

Two subsections.

**Fragen, die Lutz stellen kann** — 5–8 questions grouped by theme:

- **Team & Rolle** — Alltag, Reporting-Linie, Teamgröße, wie die Stelle entstanden ist
- **Technik & Prozesse** — Tools, Stack, Reifegrad der ISMS-/SOC-/GRC-Funktion, Zusammenarbeit mit dem CISO
- **Erwartung & Entwicklung** — die ersten 90 Tage, Erfolgskriterien, Weiterentwicklungsperspektive
- **Richtung** — strategische Prioritäten, aktuelle Veränderungen, Position zu AI/Automatisierung (nur wenn rollen-relevant)

Each question should be specific enough that only someone who read the vacancy could ask it.

**Recherche-Check** — short bulleted checklist to run before the interview:

- Interviewer-Namen und LinkedIn-Profile
- Aktuelle Unternehmensnews, Akquisitionen, regulatorische Ereignisse
- Produkte/Dienstleistungen der betreffenden Geschäftseinheit
- Bekannte Zertifizierungen und Frameworks im Einsatz
- Glassdoor/kununu-Sentiment — auffällige Red Flags

---

## Step 4 — Generate outputs

### Naming

Derive `<company>` from the folder name (e.g. `dwp-bank`, `qas-company-ag`, `kpmg`).

- Markdown: `interview-prep-<company>.md`
- Word: `interview-prep-<company>.docx`

Both files live inside the company folder.

### Markdown layout

```markdown
# Interview-Prep — <Rollentitel>

**Unternehmen:** <Firmenname>
**Rolle:** <Rollentitel>
**Datum:** <YYYY-MM-DD>

---

## 1. Wahrscheinliche Fragen & Antwort-Skizzen

<10–15 Q&A entries>

---

## 2. Lücken & Risiken

<3–6 risk entries>

---

## 3. Gesprächs-Highlights

<3–5 bullet points>

---

## 4. Fragen an das Unternehmen & Recherche

### Fragen, die Lutz stellen kann

<grouped questions>

### Recherche-Check

<bulleted checklist>
```

### docx

Use the bundled helper at `scripts/md_to_docx.py` (sibling to this SKILL.md). It converts the prep markdown to a clean Calibri-styled Word document using the same font and margin conventions as Lutz's other application documents. Invoke it with the markdown path; it writes a `.docx` of the same stem:

```bash
python3 /Users/canystrix/dev/repos/skills/skills/interview-prep/scripts/md_to_docx.py \
  /Users/canystrix/dev/job-applications/<company>/interview-prep-<company>.md
```

Confirm the `.docx` was created before reporting the task done.

---

## Step 5 — Archive to vault

Save a copy of the interview-prep markdown to:

`/Users/canystrix/dev/vault/raw/job-search/<company>-<role-slug>-interview-prep.md`

Use the exact same content as the file in the application folder. This keeps interview prep in the knowledge base so framings and answers can be reused for similar roles later.

---

## Quality check before finishing

Read the draft as if you were Lutz the night before the interview. Ask:

- Does every answer sketch draw on something real from the CV or cover letter, or is anything invented?
- Would each question plausibly be asked for *this specific role*, or are they generic?
- Are the risks honest, or am I inventing weaknesses that don't exist?
- Do the company-side questions show that the vacancy was actually read?
- Is the German natural and speakable, or does it sound like a written policy document?

If any answer is "no", fix it before writing the files.

### Factual pre-submit checklist

Run this before generating the `.docx`. Every item must be clean.

1. **Timeline:** Is the 2023 ISMS start correctly placed at DB AG / Corporate Language Solutions, and the DB-Systel move at February 2026? No A-Skizze should say "seit 2023 bei DB Systel".
2. **Scope:** No sentence implies corporate-wide scope ("konzernweit", "unternehmensweite Richtlinien", "konzernweiter ISMS-Kontext") unless explicitly disclaiming it.
3. **Frameworks:** Every mention of NIST, EU-DORA, NIS2, or BSI-Grundschutz sits at the correct ladder tier (Indirect / Conceptual only) — no phrase upgrades them to "operativ" or "im Alltag".
4. **Audit:** No A-Skizze claims external audit-Begleitung. If audit is mentioned by the vacancy, the honest internal-audit framing is in place.
5. **ServiceNow and DB-internal tools:** No claimed ServiceNow experience. SESAM / IRMA / other DB-internal tool names appear only with functional translation (or not at all).
6. **Awareness:** Python/NLP training is framed as Wissensvermittlung, not Security Awareness — unless an explicit bridge is built.
7. **Anschreiben-Spiegelung:** Every framework or experience claim in the Anschreiben that the framework-ladder would downgrade has been mirrored into Section 2 as a risk with framing-suggestion.
8. **BahnGPT / RAG:** Functional-level description only, no architecture insider details.
9. **Kurzbriefings present:** For every framework or tool the vacancy names that Lutz doesn't hold operationally, the corresponding Q in Section 1 has a Kurzbriefing sub-block.
10. **Title clarification:** If the interviewer is unlikely to know DB-internal nomenclature, the Sekundärassetverantwortlicher-vs-Information-Security-Manager Q is present.

If any answer is "no", fix it before writing the files.
