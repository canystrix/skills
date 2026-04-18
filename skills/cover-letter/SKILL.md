---
name: cover-letter
description: Generate a tailored German cover letter (Anschreiben) for Lutz Molderings based on a job vacancy. Use this skill whenever the user asks to write a cover letter, Anschreiben, or application letter, or says something like "apply to [company]", "write the cover letter for [role]", "generate the Anschreiben", or provides a vacancy PDF/MD and asks for an application document. Always use this skill when working in the job-applications directory and a cover letter is needed.
---

# Cover Letter Generator

Generate a tailored, natural-sounding German cover letter for Lutz Molderings, grounded strictly in his real qualifications and experience. Produce both a `.docx` (via python-docx) and a `.md`.

---

## Step 1 — Find the Vacancy

Look in the current application folder for the vacancy document. Priority order:
1. A `.md` file whose name starts with `vacancy-`
2. A `.pdf` file — extract text with pdfplumber:
   ```python
   import pdfplumber
   with pdfplumber.open("<path>") as pdf:
       text = "\n".join(page.extract_text() or "" for page in pdf.pages)
   ```
   After extracting, derive a slug from the role title (lowercase kebab-case) and save the text as `vacancy-<role-slug>.md` in the application folder. This becomes the canonical source for future runs.

If the company folder doesn't exist yet, create it under `/Users/canystrix/dev/job-applications/<company-name>/` and place the vacancy file there.

Read the full vacancy text before proceeding.

---

## Step 2 — Analyze Requirements

Extract the following from the vacancy, explicitly and in writing (show this to the user before drafting):

**Role summary** — title, company, one-sentence description of the position.

**Must-have requirements** — qualifications and experience the posting treats as required.

**Nice-to-have requirements** — items marked "idealerweise", "von Vorteil", "wünschenswert", etc.

**Tone of the company** — formal/traditional vs. modern/casual (inferred from how the posting is written).

Then map each must-have requirement to a specific item from Lutz's profile (section below). If a requirement cannot be honestly covered by something in the profile, note it as **not covered** — do not invent qualifications.

---

## Step 3 — Draft the Cover Letter

Write 4–5 body paragraphs in German. Follow the prose rules below precisely.

### Structure

1. **Opening** — Hook the reader with what draws Lutz to this specific role or company. Not a generic "I am applying for…" opener. One or two sentences, specific.
2. **Core competence paragraph** — ISMS experience at DB Systel. Ground it in concrete activities (Schutzbedarfsanalysen, Risikobehandlung, etc.), not abstract claims.
3. **Differentiator paragraph** — Whatever is most relevant to the vacancy beyond standard ISMS work. Choose from: agentic AI/automation (n8n, OpenClaw), Python/NLP background, teaching/communication, language expertise. Pick what the vacancy actually asks for.
4. **Fit paragraph** — Tie a specific aspect of the company or role back to something concrete in Lutz's experience. Show you read the vacancy.
5. **Close** — Short, direct expression of interest in an interview. One or two sentences, no filler.

### Prose Rules

**Avoid these patterns:**
- Connector phrases that sound like AI summaries: "Das schafft eine direkte Grundlage für…", "Das gibt mir eine andere Perspektive auf…", "gehören zu meinem Standardrepertoire"
- Noun-heavy bureaucratic constructions: "leite Risikobehandlungsmaßnahmen ab und setze sie um", "verantwortliche Durchführung von"
- Opening with "Hiermit bewerbe ich mich…" or "Ich möchte mich bewerben…"
- Listing skills as a series of nouns without verbs

**Use instead:**
- A colon to pivot into specifics: "Konkret heißt das: Schutzbedarfsanalysen, …"
- Contrast to show perspective: "nicht aus der Vogelperspektive, sondern aus der Praxis"
- Short personal statements at the end of paragraphs, not bureaucratic summaries
- Integrated flow: "von der Ableitung bis zur Umsetzung" instead of "leite ab und setze um"
- Varied sentence rhythm — alternate short punchy sentences with longer structured ones

**Test before finalising:** Read each paragraph aloud mentally. If it sounds like a job description or a bullet list dressed as prose, rewrite it. Ask: could this sentence only have been written by Lutz, or could it describe anyone?

### Factual Constraints — Do Not Violate

- **ISMS scope is team/application-level.** Lutz does Schutzbedarfsanalysen, Risikobehandlung, and Risikobeurteilung for the applications and assets in his team's responsibility. He does not own or author corporate-wide IS policies.
  - Never write: "konzernweite Richtlinien", "unternehmensweite Sicherheitsrichtlinien"
  - Write instead: "Anwendungen und Assets in meinem Verantwortungsbereich", "im Rahmen des ISMS meines Teams"
- **DB Systel identification.** Always: "DB Systel GmbH, dem IT-Partner der Deutschen Bahn" — not "Infrastrukturdienstleister", not just "Deutschen Bahn".
- **Current role start date: February 2026** (combined ISMS + Language Data Engineer role). The ISMS work at DB/DB Systel began March 2023.
- **No invented qualifications.** If the vacancy asks for something not in the profile, acknowledge the gap rather than fabricate coverage.

---

## Step 4 — Generate Outputs

### Naming

Derive `<company>` from the folder name: `/Users/canystrix/dev/job-applications/<company>/`.

- Cover letter docx: `anschreiben-lutz-molderings-<company>.docx`
- Cover letter md: `anschreiben-lutz-molderings-<company>.md`

Both files go inside the application folder.

### Python script

Write a Python script `generate-anschreiben.py` inside the application folder. Follow the exact same python-docx pattern used in `/Users/canystrix/dev/job-applications/generate-docs.py`:
- Same font constants (`FONT_BODY = "Calibri"`, `FONT_SIZE_BODY = 11`, etc.)
- Same `set_margins`, `add_run`, `para_spacing` helper functions
- Same header block: name bold 14pt, contact line 9pt in COLOR_SUBTLE, horizontal rule
- Date line + company address block (if address is known; leave a placeholder if not)
- Subject line bold 12pt
- Salutation
- Body paragraphs (space_after=6)
- Closing + signature

After writing the script, run it:
```bash
cd <application-folder> && python3 generate-anschreiben.py
```

Confirm the `.docx` was created.

### Markdown file

Write the same content as a `.md` file alongside the `.docx`. Format:

```markdown
# Anschreiben — <Role Title>

**Lutz Molderings**
molderings@gmail.com · +49 176-32091033 · Dubliner Str. 3, 60327 Frankfurt am Main

---

Frankfurt am Main, <date>

<Company Name>
<Address if known>

**Bewerbung als <Role Title>**

Sehr geehrte Damen und Herren,

<body paragraphs separated by blank lines>

Mit freundlichen Grüßen

**Lutz Molderings**
```

---

## Step 5 — Archive to Vault

After generating outputs, save a research note to the knowledge base at:
`/Users/canystrix/dev/vault/raw/job-search/<company>-<role-slug>.md`

Format:

```markdown
# <Company> — <Role Title>

**Date seen:** <YYYY-MM-DD>
**Location:** <city/remote>
**Salary:** <if stated>

## Role Summary

<one paragraph>

## Key Requirements

<bulleted list of must-haves and nice-to-haves>

## Coverage Assessment

<the requirement→profile mapping from Step 2: what's covered, what's partial, what's not covered>

## Notes

<anything else worth remembering: tone, company context, fit concerns>
```

After writing the file, update `/Users/canystrix/dev/vault/wiki/job-search/_summaries.md` by appending a one-paragraph entry for this vacancy (following the existing format in that file). If `_summaries.md` does not exist yet, create it.

---

## Lutz's Profile (Canonical Reference)

Use this as the authoritative source. Do not draw on information outside this profile.

### Current Role (02/2026 – present)
**Information Security Manager (ISMS) / Language Data Engineer** at DB Systel GmbH, Frankfurt am Main
- Responsible for ISMS processes (Schutzbedarfsanalysen, Risikobehandlung, Compliance-Dokumentation) for applications and assets in his team's area of responsibility, per ISO/IEC 27001
- Risk assessment and coordination of measures with stakeholders and the central CISO team
- Reclassification and update of applications within cross-team governance processes
- Builds and operates agentic automation workflows (n8n, OpenClaw — self-hosted Docker-based agentic AI stack)
- Delivers Python and NLP training to colleagues — independently designed and delivered

### Previous Role (03/2023 – 01/2026)
**Information Security Manager (ISMS)** at Deutsche Bahn AG, Frankfurt am Main
- Independently rolled out ISMS for three production applications — reached maturity level 3 without external coordination support
- Conducted Schutzbedarfsanalysen and risk assessments; derived and implemented technical and organisational measures
- Created audit-ready evidence documentation and prepared governance reviews
- Implemented access concepts, emergency planning, and security measures in live operations

### Earlier Roles at Deutsche Bahn
- **Language Data Engineer** (01/2021 – 01/2026): Subject matter administrator of two group-wide translation/terminology management applications; process automation with Python and NLP libraries; structured application documentation
- **Project Manager** (01/2016 – 12/2020): Managed translation projects with internal departments and external language service providers
- **Translator and Terminologist** (05/2013 – 12/2015): Technical translations (DE–EN) and maintenance of the group-wide terminology database
- **Freelance Translator** (01/2007 – 04/2013): Technical translations for mechanical engineering companies, based in London and Ho-Chi-Minh City

### Education
- **MSc Translation Studies (Distinction)** — University of Edinburgh, 2007
- **Staatlich geprüfter und beeidigter Übersetzer** — SDI München, 2006

### Certifications
- PECB ISO/IEC 27001 Lead Implementer (2025)
- CompTIA Security+ (2025)
- CompTIA Network+ (2026)
- Microsoft Certified: Azure Fundamentals AZ-900 (2025)
- Language Data Engineer — Loctimize GmbH (2021–2025)

### Languages
Deutsch — Muttersprache · Englisch — Muttersprache

### Unique differentiators (use when relevant to the role)
- **Agentic AI**: Builds and maintains n8n automation workflows professionally; OpenClaw is a private open-source agentic AI project. Has direct hands-on understanding of agentic risk: uncontrolled tool calls, data exfiltration, prompt injection — valuable in risk analysis and advisory roles. At DB Systel, agentic automation is already changing how the team works — not a future prospect but current practice. This dual angle (risk understanding + practical adoption) is particularly relevant for consulting or advisory roles where clients will face the same questions.
- **Python/NLP**: Practitioner-level; uses it for process automation, text processing, and trains colleagues on it.
- **Communication**: Teaches colleagues technical skills; experienced at advocating security requirements to IT units and business departments without being prescriptive.
- **Dual expertise**: The combination of language/NLP background and information security is rare and relevant for roles at the intersection of data, AI, and governance.
