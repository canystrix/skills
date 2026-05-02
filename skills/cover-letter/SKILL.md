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
- **Lutz is an Information Security Manager *embedded in a Fachbereich* (Corporate Language Solutions, CLS), not part of a central CISO function.** This positioning is important: he is the ISM *within* a business unit, responsible for the security of that unit's applications. He is *not* a central security advisor speaking *to* Fachbereiche from outside.
  - **Write:** "Information Security Manager im Fachbereich Corporate Language Solutions", "ISM auf Anwendungsebene innerhalb der CLS-Einheit"
  - **Never write:** anything that implies central-CISO scope or cross-Fachbereich advisory authority
- **ISMS scope is team- and application-level.** Lutz is Sekundärassetverantwortlicher for the productive applications in his own team. He does NOT own corporate-wide policies, does NOT cover other teams/units, does NOT speak for the whole DB group.
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

**Important — BSI IT-Grundschutz and NIS2 should be present in the Anschreiben and CV when role-relevant.** The "Indirect" and "Conceptual only" tiers do *not* mean *„remove from the document"*; they mean *„use the tier-correct phrasing"*. For regulated finance, KRITIS-adjacent, public-sector, or other role contexts where these frameworks are part of the operating environment, omitting them altogether weakens the application unnecessarily.

- **BSI IT-Grundschutz** is part of Lutz's working vocabulary via the konzerninternes DB-Schema (BSI-orientiert). Mention it at the *„im DB-Umfeld über ein am BSI-Schema orientiertes konzerninternes Modell präsent"* / *„konzeptionell bekannt"* tier — it shows that he speaks the BSI language and can read Bausteine, even if no federführende Grundschutz-Projekterfahrung exists yet.
- **NIS2** belongs in the regulatorisch-aware vocabulary. Mention it as *„als regulatorischer Rahmen aktiv beobachtet"* / *„konzeptionell abgedeckt"* — signals awareness of the directive without overclaiming productive Umsetzungserfahrung.

The rule is: **mention at the correct tier, do not omit defensively, do not upgrade the tier**. The phrasing in the ladder above is the green-light language for these frameworks.

#### Practice claim discipline (universal rule)

The framework ladder above is one application of a more general principle: **every concrete practice claim must survive a 5-minute focused drill from a sharp interviewer.** The drill is a three-step probe: *„Was genau?"* → *„Wie viele / wie oft?"* → *„Produktiv oder Sandbox / Eigenanteil oder Beitrag?"*. If at any step the wording breaks because the actual scope is narrower than implied, the wording is too broad and must be rewritten before submission.

Apply the drill explicitly to the four high-risk claim families below. These have produced concrete Anschreiben failures before — they must not slip past again.

##### Agentic AI / n8n / OpenClaw — work vs. private split

This is **the** rule that produced the dwpbank Anschreiben failure. Read carefully.

**At work, do not mention n8n or agentic AI at all.** Both are off-limits for any work-related claim:
- No *„produktiv mit n8n"*, no *„agentenbasierte Automatisierung"*, no *„AI-Agent-Knoten"*, no work-context claim that names n8n specifically or agentic-AI as a work tool.
- **What CAN be mentioned at work:** *„Workflow-Automation"* in generic terms, when relevant — e.g. *„meine Tätigkeit umfasst Workflow-Automatisierung im LDE-Kontext"*. No tool name attached.

**Agentic AI and OpenClaw belong in the private-interest section only**, and only when role-relevant:
- **OpenClaw** — Lutz is contributor (Peter Steinberger is the creator). Mention as: *„im Privaten Contributor bei OpenClaw, einem Open-Source-Agenten-Framework von Peter Steinberger"*.
- **Agentic AI in general** — frame as private interest plus risk-awareness, not work practice: *„privat verfolge ich agentische AI-Architekturen und ihre Risiken (OWASP LLM Top 10)"*.
- Surface this private-interest paragraph **only when the role touches AI, LLM-security, or agentic-system risk**. For unrelated roles (pure ISMS, pure SIEM ops, pure GRC), leave it out.

**Never write — even if the underlying activity is real:**
- *„produktiv mit agentenbasierter Automatisierung"*
- *„nutze n8n bei der DB"* / *„im Konzern setze ich n8n ein"*
- *„mein Open-Source-Agenten-Framework"* (authorship implication)
- *„ich habe entwickelt"* in conjunction with OpenClaw
- Any wording that places OpenClaw or agentic AI in the work context

**Write instead — when role-relevant:**
- *„Beruflich mit Workflow-Automation befasst; privat Contributor bei OpenClaw, einem Open-Source-Agenten-Framework von Peter Steinberger, mit Fokus auf den Risiken agentischer Systeme nach OWASP LLM Top 10."*

If the role does not touch AI/LLM/agentic, the entire topic stays out of the Anschreiben — not as a defensive omission, but because it isn't relevant.

##### Advisory scope

- **Lutz advises within his SAV scope: PAVs of his applications (typically in different Fachbereichen) and the platform/operations team.** He does NOT advise corporate Fachbereiche bank- or group-wide.
- The vacancy phrase *„Fachbereiche beraten"* often implies cross-organizational advisory at corporate scale (Treasury, Risk, Compliance, etc.). Plain mirroring of this phrase in the Anschreiben overscopes Lutz's reality.
  - **Never write:** plain "Fachbereiche beraten" or "Beratung der Fachbereiche" without scope qualification
  - **Write instead:** "Beratung der Primärassetverantwortlichen meiner Anwendungen — die in unterschiedlichen Fachbereichen sitzen — sowie des Plattform-Teams in sicherheitsrelevanten Fragen", or "Beratung der Asset-Owner und Plattform-Teams im Verantwortungsbereich"
- The PAV-advisory angle is methodisch real and defensible (risk acceptance, Schutzbedarf, Restrisiko-Aufklärung). Use it, but scope it.

##### BCM / Notfallplanung

- **Lutz's applications are NOT KRITIS-relevant and NOT BCM-relevant in the enterprise sense (BSI 200-4 / ISO 22301).** They are corporate language-service tools — failure causes business inconvenience, not safety or regulatory incidents.
- What Lutz actually does: **Asset-level Notfallkonzepte gemäß ISO 27001 Annex A 5.30** — Wiederanlauf, Backup-Konzept, Eskalations- und Kontaktpfade, Notbetriebs-Verfahren. RTOs typischerweise im Tagesbereich.
  - **Never write:** "Verantwortung für Business Continuity Management", "BCM-relevante Maßnahmen", "Notfallplanung für KRITIS-Systeme", "Disaster Recovery für geschäftskritische Anwendungen"
  - **Write instead:** "Erstellung und Pflege von Notfallkonzepten auf Anwendungsebene gemäß ISO 27001 Annex A 5.30 — Wiederanlauf, Backup-Konzept, Eskalationswege"
- If the vacancy explicitly demands BCM ownership (KRITIS bank, regulated finance), this becomes a Section-2 risk in the prep doc, not a claimed competence.

##### Authorship vs. contribution

For every project, system, or framework Lutz didn't build alone, state the role accurately:
- **Contributor / Beiträger** — code, docs, ideas added to someone else's project (OpenClaw)
- **Anwendungsverantwortlicher / Operator** — runs an existing system in production (BahnGPT consumer, the four CLS apps)
- **Author / Architect** — designed and built (the in-house CLS Eigenentwicklung; n8n workflows he personally built)

Never let the wording imply authorship where the role is contribution or operation.

#### Audit experience

- **Lutz has not undergone any audits — neither internal nor external.** Do not claim audit participation in any form.
- **What he has built is audit-readiness, not audit experience.** The applications and documentation in his Verantwortungsbereich are maintained at audit-ready state — laufend revisionssichere Dokumentation, nachvollziehbare Risikobehandlung, geprüfte Maßnahmenwirksamkeit — but no audit (internal or external) has actually been conducted on them with his participation.
- **Never write:** "habe Audits begleitet", "Audit-Begleitung gehört zu meinem Alltag", "Teilnahme an internen Prüfungen", "externe Auditverantwortung"
- **Write instead (if audit topic is relevant):** "Audit-Readiness ist Tagesgeschäft — die Anwendungen in meinem Verantwortungsbereich sind durchgängig auf Audit-Niveau dokumentiert: revisionssichere Nachweisführung, nachvollziehbare Risikobehandlung, belegbare Maßnahmenwirksamkeit. Die Begleitung eines tatsächlichen Audits sehe ich als Aufgabe der nächsten Rolle, nicht als vorhandene Erfahrung."
- This distinction matters: Audit-Readiness is a *state of preparedness* (real, ongoing); Audit-Begleitung is an *event-driven process* (not yet experienced).

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
8. **5-minute drill test for every concrete practice claim.** For each tool/activity/scope claim, simulate the three-step probe: *„Was genau?"* → *„Wie viele / wie oft?"* → *„Produktiv oder Sandbox / Eigenanteil oder Beitrag?"*. If any step would expose a narrower reality than the wording suggests — rewrite. Apply especially to:
   - n8n / agentic-AI at work — **forbidden**. n8n must not appear in any work claim; agentic AI must not be framed as a work activity. If these appear in the work context, remove.
   - OpenClaw / agentic AI in the private-interest section — only if role-relevant; OpenClaw is contributor (never author).
   - "Fachbereiche beraten" or similar (PAV-Scope vs. corporate-wide)
   - BCM / Notfallplanung (Annex A 5.30 Asset-Level vs. enterprise-BCM)
   - Audit claims — only Audit-Readiness, never Audit-Begleitung
   - Authorship vs. contribution / operation across all named systems

Only if every answer is clean, generate the .docx and .md.

> **Rule of thumb after the dwpbank Anschreiben experience (April 2026):** the cover letter is a contract for the interview. Every sentence becomes a claim Lutz must defend in person. If a sentence cannot survive a 5-minute drill, it does not belong in the Anschreiben — even when the underlying activity is real, just narrower than the wording.

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
- **At work:** workflow-automation tasks in the LDE context (no specific tool name to be mentioned in cover letters — n8n is off-limits as a work claim).
- **Privately:** contributor to OpenClaw, an open-source agentic-AI framework created by Peter Steinberger. Surfaces as a CV/Anschreiben item only when the role touches AI, LLM security, or agentic-system risk.
- Delivers Python and NLP training to colleagues — independently designed and delivered (Wissensvermittlung, not security awareness)

### Previous Role (03/2023 – 01/2026)
**Information Security Manager (ISMS) / Sekundärassetverantwortlicher** at Deutsche Bahn AG, Frankfurt am Main — within the unit **Corporate Language Solutions (CLS)**
- CLS is a DB-AG-unit with a group-wide governance role for language- and terminology-related applications. Lutz's role inside CLS is application-scoped, not unit-scoped.
- Independently rolled out ISMS for **four production applications** of his own team — reached maturity level 3 without external coordination support. (Note: two of the four are grouped as a single asset for internal SAV-administration purposes. In external materials — Anschreiben, CV, interview prep — always count as four; the internal grouping is an accounting convenience, not a real reduction of scope.)
- Conducted Schutzbedarfsanalysen and risk assessments; derived and implemented technical and organisational measures
- Created audit-ready evidence documentation and prepared governance reviews
- **No audit participation (internal or external).** Applications are maintained in an audit-ready state — but no audit has yet been conducted on them with Lutz's involvement.
- Implemented access concepts, Notfallkonzepte (Asset-Level gemäß ISO 27001 Annex A 5.30, NOT enterprise-BCM), and security measures in live operations

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
- **Agentic AI / OpenClaw (private interest, risk-aware)**: Contributor to OpenClaw, an open-source agentic-AI framework by Peter Steinberger. Privately follows agentic AI architectures and their risks (OWASP LLM Top 10: Excessive Agency, Indirect Prompt Injection, Sensitive Information Disclosure). **Strict scope:** this is a *private* interest, not a *work* claim — n8n and agentic AI must never be tied to Lutz's work context in the Anschreiben. Surface this differentiator only when the role explicitly touches AI, LLM security, or agentic-system risk. For unrelated roles, leave it out.
- **AI data layer (productive contact)**: Via the LDE role, operates at the data layer of DB's internal LLM system (BahnGPT). The CLS-maintained multilingual terminology database feeds grounding data into BahnGPT's RAG layer and into other downstream systems (Konzernregelwerksdatenbank, Autorenunterstützungsprogramme, MT service). This is the strongest differentiator for AI-governance-adjacent roles — surface it when the vacancy mentions AI, data governance, or LLM-related responsibility.
- **Python/NLP**: Practitioner-level; uses it for process automation, text processing, and trains colleagues on it.
- **Communication**: Teaches colleagues technical skills; experienced at advocating security requirements to IT units and business departments without being prescriptive. NOT to be conflated with Security Awareness (see Awareness vs. Wissensvermittlung constraint above).
- **Dual expertise**: The combination of language/NLP background and information security is rare and relevant for roles at the intersection of data, AI, and governance.
