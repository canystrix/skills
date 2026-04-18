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

**Factual constraints — identical to the cover-letter skill:**

- **ISMS scope is team- and application-level, never corporate-wide.** Lutz does Schutzbedarfsanalysen, Risikobehandlung, and Risikobeurteilung for the applications and assets in his team's responsibility. He does not author or own corporate-wide IS policies. This constraint applies to every sentence you write — including Q&A answer sketches, highlights, and framing suggestions.
  - Never write: "konzernweiter ISMS-Kontext", "konzernweite Richtlinien", "konzernweites ISMS", "unternehmensweite Sicherheitsrichtlinien", "verantworte konzernweit". The word *konzernweit* may appear only when Lutz is explicitly disclaiming that scope ("nicht konzernweit", "keine konzernweite Richtlinienautorenschaft").
  - Write instead: "Anwendungen und Assets in meinem Verantwortungsbereich", "im Rahmen des ISMS meines Teams", "anwendungsbezogen", "auf Team-Ebene".
- DB Systel is always identified as "DB Systel GmbH, dem IT-Partner der Deutschen Bahn" — never "Infrastrukturdienstleister" or just "Deutsche Bahn".
- Current role (02/2026–present): combined Information Security Manager + Language Data Engineer at DB Systel. ISMS work at DB/DB Systel began March 2023.
- Do not invent qualifications, certifications, or experiences that aren't in the CV/cover letter. If the vacancy asks for something Lutz doesn't have, treat it as a gap (section 2) — don't manufacture coverage.

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

- ISMS-Rollout für drei produktive Anwendungen eigenständig bis Reifegrad 3 gehoben — ohne externe Koordinationsunterstützung
- Agentic AI in der Praxis: n8n-Automatisierungen im Arbeitsalltag + OpenClaw als privates Open-Source-Projekt; Verständnis für agentische Risiken (unkontrollierte Tool-Calls, Datenexfiltration, Prompt Injection)
- Python- und NLP-Schulungen für Kolleg:innen — kann technische Themen anschlussfähig erklären
- Duale Expertise: Sprachtechnologie/NLP + Informationssicherheit — selten und gerade für AI-Governance-nahe Rollen relevant

Pick what actually fits the role — don't include all four if only two match.

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
