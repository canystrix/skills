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

Treat every sentence you write as a claim that must map to something in the profile below. If you cannot point to the exact CV entry, certification, or experience item that backs a phrase, rewrite it. When in doubt, acknowledge the gap rather than soften a claim into dishonest territory.

#### Employer and timeline

- **2023 start was at Deutsche Bahn AG, NOT at DB Systel.** Lutz began ISMS work in March 2023 at the DB AG (inside the unit **Corporate Language Solutions**, abbreviated CLS). He moved to **DB Systel GmbH** only in February 2026 as part of an internal transfer.
  - **Never write:** "Seit 2023 bei DB Systel", "Seit 2023 bei der DB Systel GmbH"
  - **Write instead:** "Seit 2023 im Information Security Management nach ISO/IEC 27001 — zunächst bei der Deutschen Bahn AG, seit Anfang 2026 bei der DB Systel GmbH, dem IT-Partner der Deutschen Bahn." Or collapse if the vacancy doesn't care about the unit distinction: "Seit 2023 verantworte ich die Informationssicherheit für Anwendungen in meinem Verantwortungsbereich nach ISO/IEC 27001 (zunächst bei der DB AG, seit 2026 bei DB Systel)."
- **DB Systel identification.** Always: "DB Systel GmbH, dem IT-Partner der Deutschen Bahn" — not "Infrastrukturdienstleister", not just "Deutschen Bahn".

#### Role title and scope

- **Lutz's official internal role title is "Sekundärassetverantwortlicher"** — a DB-konzerninterne Rollenbezeichnung. "Information Security Manager" is the functional/market-standard translation used in CV and cover letter as a role description. Do not claim it is the official title if directly asked. In cover letters, treat "Information Security Manager" as a functional description, not a title claim.
- **ISMS scope is team- and application-level.** Lutz is Sekundärassetverantwortlicher for three productive applications in his own team. He does NOT own corporate-wide policies, does NOT cover other teams/units, does NOT speak for the whole DB group.
  - **Never write:** "konzernweite Richtlinien", "unternehmensweite Sicherheitsrichtlinien", "konzernweites ISMS verantworten", "konzernweit"
  - **Write instead:** "für die Anwendungen und Assets in meinem Verantwortungsbereich", "im Rahmen des ISMS meines Teams", "anwendungsbezogen", "auf Team-Ebene"
- **The governance role belongs to the unit (Corporate Language Solutions), not to Lutz personally.** CLS covers governance for language- and terminology-related applications group-wide. Lutz's role within CLS is Sekundärassetverantwortlicher for a subset of those applications. Do not conflate.

#### Framework experience ladder

This ladder is strict. Do not upgrade a framework into a higher tier than it belongs to.

| Framework | Experience tier | Allowed phrasing |
|---|---|---|
| ISO/IEC 27001 | **Operational** — daily work, PECB-certified | "Tagesgeschäft", "seit 2023 nach ISO/IEC 27001 verantwortlich", "PECB-zertifiziert" |
| BSI IT-Grundschutz | **Indirect** — only via the konzerninternes DB-Schema, which is BSI-oriented; no federführende Grundschutz-Projekte | "im DB-Umfeld über ein am BSI-Schema orientiertes konzerninternes Modell präsent", "konzeptionell bekannt" — NEVER "im operativen Alltag" or "kontinuierlich in meiner Arbeit" |
| NIST (CSF, 800-53) | **Conceptual only** — no production use | "als Rahmen bekannt", "konzeptionell vertraut" — NEVER "operativ", "im Alltag", "arbeite mit" |
| EU-DORA | **Conceptual only** — no federführende Umsetzung | "als regulatorischer Rahmen bekannt", "konzeptionell abgedeckt" — NEVER "setze um", "habe implementiert" |
| NIS2 | **Conceptual only** — beobachtet, kein produktiver Einsatz | "beobachte aktiv", "als Rahmen bekannt" — NEVER "fließt kontinuierlich ein" |
| CompTIA Security+ / Network+ / AZ-900 | Certified — describe as Zertifizierungsbasis, not operational experience | As listed on the CV |

If the vacancy asks for operational experience in a framework that falls into "Indirect" or "Conceptual only", acknowledge the gap ("konzeptionell vertraut, federführende Umsetzung kommt bei CANCOM/…") rather than bridging with weasel words that imply more than is true.

#### Audit experience

- **No external audit-Begleitung.** Lutz has never led or independently accompanied an external audit.
- **Internal audit:** Teilnahme an einer internen Prüfung nach Abschluss des ISMS-Rollouts auf Reifegrad 3.
- **Never write:** "habe mehrere Audits begleitet", "Audit-Begleitung gehört zu meinem Alltag", "externe Auditverantwortung"
- **Write instead (if audit topic is relevant):** "Die Arbeitsweise, die ein Audit gelingen lässt — laufend revisionssichere Dokumentation, nachvollziehbare Risikobehandlung — bringe ich mit. Produktive Audit-Begleitung sehe ich als Aufgabe der Rolle, nicht als vorhandene Erfahrung."

#### Tools and systems

- **No ServiceNow experience.** Never claim it. If the vacancy names it, acknowledge the gap.
- **DB-internal tools (SESAM, IRMA, etc.)** are DB-konzerninterne Systeme without public documentation. Do not name them in cover letters — outside the DB world they are unknown. Describe them by function ("internes Risikomanagement-Tool", "zentrales Dokumentations- und Nachweissystem") if at all.

#### Awareness vs. Wissensvermittlung

- **Lutz's Python/NLP training is Wissensvermittlung im eigenen Team, NOT Security Awareness in the infosec-specific sense.** Security Awareness refers to phishing training, behaviour coaching, compliance communication — Lutz has not done this.
- If the vacancy asks for Awareness-Maßnahmen, frame the connection carefully: "Meinen didaktischen Ansatz — aktuell bei der Vermittlung von Python und NLP im Team — lässt sich direkt auf Security-Awareness-Formate übertragen." Do not claim existing customer-facing or security-specific awareness experience.

#### Language expertise

- Use "Deutsch und Englisch auf Muttersprachenniveau" — accurate per CV.
- Do not claim other working languages.

#### The no-fabrication rule

If the vacancy asks for something not in the profile, acknowledge the gap rather than fabricate coverage. Proactive gap-naming in the cover letter ("Den operativen SIEM-Aufbau bringe ich nicht aus eigener Praxis mit; das ist mir bewusst.") is a pattern that has worked well in past letters — it signals honesty and turns the gap into a trust signal rather than a vulnerability.

### Pre-submit verification checklist

Before you finalise the letter, read it top to bottom with this checklist in hand:

1. Does any sentence claim operational experience with NIST, EU-DORA, NIS2, or BSI-Grundschutz? If yes — downgrade per the framework ladder.
2. Is there any phrase implying corporate-wide scope ("konzernweit", "unternehmensweit", "konzerninterne Richtlinien")? If yes — rewrite to team-/application-scope.
3. Is the 2023 start correctly placed at DB AG (not DB Systel)?
4. Is ServiceNow or any DB-internal tool name mentioned? Remove.
5. Is "Awareness" used in a way that implies security-awareness experience? Rewrite or soften.
6. Is there any mention of external audit-Begleitung as existing experience? Remove.
7. Does every concrete claim (framework, tool, activity) map to a specific item in the profile below? If not — remove or soften.

Only if every answer is clean, generate the .docx and .md.

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
- Internal title: **Sekundärassetverantwortlicher** (DB-konzerninterne Rollenbezeichnung). "Information Security Manager" is the functional/market description.
- Part of a delivery team that is building its own service — not a pure governance context anymore.
- Responsible for ISMS processes (Schutzbedarfsanalysen, Risikobehandlung, Compliance-Dokumentation) for the applications and assets in his team's area of responsibility, per ISO/IEC 27001
- Risk assessment and coordination of measures with stakeholders and the central CISO team
- Reclassification and update of applications within cross-team governance processes
- Builds and operates agentic automation workflows (n8n, OpenClaw — self-hosted Docker-based agentic AI stack)
- Delivers Python and NLP training to colleagues — independently designed and delivered (Wissensvermittlung, not security awareness)

### Previous Role (03/2023 – 01/2026)
**Information Security Manager (ISMS) / Sekundärassetverantwortlicher** at Deutsche Bahn AG, Frankfurt am Main — within the unit **Corporate Language Solutions (CLS)**
- CLS is a DB-AG-unit with a group-wide governance role for language- and terminology-related applications. Lutz's role inside CLS is application-scoped, not unit-scoped.
- Independently rolled out ISMS for three production applications of his own team — reached maturity level 3 without external coordination support
- Conducted Schutzbedarfsanalysen and risk assessments; derived and implemented technical and organisational measures
- Created audit-ready evidence documentation and prepared governance reviews
- Participated in one internal audit after Reifegrad 3 was reached. No external audit-Begleitung.
- Implemented access concepts, emergency planning, and security measures in live operations

### Earlier Roles at Deutsche Bahn
- **Language Data Engineer** (01/2021 – 01/2026, continues alongside ISM role from 02/2026): Subject matter administrator of two group-wide translation/terminology management applications; process automation with Python and NLP libraries; structured application documentation
  - The CLS unit has shifted from being a pure translation/interpreting service provider toward **providing language-based knowledge infrastructure for the group**. Its curated multilingual terminology database (with ontological relations) feeds multiple downstream systems: the **Konzernregelwerksdatenbank**, Autorenunterstützungsprogramme, the group's **machine translation service**, and — significantly — the **Retrieval layer of BahnGPT (DB's internal LLM)** as grounding data.
  - Lutz's LDE role sits at this data interface — he has operational contact with the **data layer of a productive enterprise AI system**, which is a legitimate differentiator for AI-governance-adjacent roles and can be surfaced when the vacancy asks for AI or data-governance understanding.
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
- **Agentic AI (practical + risk-aware)**: Builds and maintains n8n automation workflows professionally; OpenClaw is a private open-source agentic AI project. Hands-on understanding of agentic risk: uncontrolled tool calls, data exfiltration, prompt injection — valuable in risk analysis and advisory roles. This dual angle (risk understanding + practical adoption) is particularly relevant for consulting or advisory roles.
- **AI data layer (productive contact)**: Via the LDE role, operates at the data layer of DB's internal LLM system (BahnGPT). The CLS-maintained multilingual terminology database feeds grounding data into BahnGPT's RAG layer and into other downstream systems (Konzernregelwerksdatenbank, Autorenunterstützungsprogramme, MT service). This is the strongest differentiator for AI-governance-adjacent roles — surface it when the vacancy mentions AI, data governance, or LLM-related responsibility.
- **Python/NLP**: Practitioner-level; uses it for process automation, text processing, and trains colleagues on it.
- **Communication**: Teaches colleagues technical skills; experienced at advocating security requirements to IT units and business departments without being prescriptive. NOT to be conflated with Security Awareness (see Awareness vs. Wissensvermittlung constraint above).
- **Dual expertise**: The combination of language/NLP background and information security is rare and relevant for roles at the intersection of data, AI, and governance.
