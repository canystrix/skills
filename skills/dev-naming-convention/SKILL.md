---
name: dev-naming-convention
description: Tiebreaker naming rule for free-form files and folders in /Users/canystrix/dev — use lowercase kebab-case when no ecosystem convention applies. Use this skill when creating, renaming, or auditing names where you'd otherwise have to choose between styles (docs, data files, project folders, notes, configs, non-code assets). Do NOT use it to override language- or framework-mandated names — those follow their own rules (PEP 8 for Python, Django app dirs, vendor folders, etc.). Use this when asked to "audit", "fix", or "check" naming consistency in the dev workspace.
---

# Dev Workspace Naming Convention

A tiebreaker for free-form names. Ecosystem rules always win.

## Scope

This skill applies **only to names where no ecosystem convention exists** — docs, data files, project folders, notes, scripts in non-code roles, asset filenames, etc. Where a language, framework, or tool dictates naming, follow that — don't apply this skill on top.

In particular:
- **Python files (`.py`)** follow **PEP 8** — lowercase, with underscores if readability needs them (`detect_lang.py`, `step_1_logic.py`). Hyphens are illegal in Python module names. Never kebab-case a `.py` file, even one that is "only a script" — the cost of accidental drift outweighs the gain.
- **Python packages** (directories with `__init__.py`) use lowercase, ideally no separator; underscores allowed if needed.
- **Django apps** use whatever style the project already established (often `PascalCase`); match the project.
- **Framework/tool-generated names** (`manage.py`, `migrations/0001_initial.py`, `package.json`, `Dockerfile`, etc.) are left alone.
- **Vendor / third-party sample folders** keep their upstream names.

If you would naturally follow an ecosystem rule, just do that. This skill does not need to weigh in.

## The Rule (for free-form names only)

**Lowercase kebab-case.** Every word lowercase, separated by hyphens. No underscores, no spaces, no camelCase, no PascalCase, no mixed case.

```
good:  iso-27001-gap-analysis.md
good:  mqxliff-term-extractor/        (project folder, not a Python package)
good:  2026-04-16-review-notes.md
good:  alignment-report.json

bad:   ISO_27001_Gap_Analysis.md
bad:   MQXLIFFTermExtractor/
bad:   review_notes_april.md
```

**Language:** English. Domain terms with no clean English equivalent (`mqxliff`, `plunet`, `cls`) are acceptable.

**Extensions:** Always lowercase — `.md`, `.json`, `.csv`, never `.MD`, `.JSON`.

**Numbers and dates:** Inline — `iso-27001`, `v1-2`, `2026-04-16-notes.md`, `chunk-01`.

**Abbreviations:** Keep established ones intact and lowercase — `nlp`, `api`, `csv`, `llm`, `mqxliff`, `cls`. Do not expand them.

---

## When Creating New Files or Folders

For free-form names, apply kebab-case automatically — don't wait to be asked. For names governed by an ecosystem (any `.py` file, framework dirs, tool-generated files), use the convention that ecosystem expects.

---

## When Asked to Audit Naming

Scan the target path recursively. For each item:

1. Skip hidden directories and build artifacts (`.git/`, `.venv/`, `__pycache__/`, `dist/`, `build/`, `node_modules/`).
2. Skip anything governed by an ecosystem rule (Python files, framework dirs, vendor samples, tool-generated names).
3. Flag remaining free-form names that aren't lowercase kebab-case.
4. Group violations by directory.

Report format:

```
Free-form violations in dev/lang-ops/
  My Notes.md       → my-notes.md
  data_export.csv   → data-export.csv

Ecosystem-governed (kept as-is):
  manage.py, step_1_logic.py, migrations/0001_initial.py, Krake/
```

Then ask: "Rename these now, or review first?"

---

## When Renaming Files

Propose all renames before executing any. Confirm, then apply in one pass. Before renaming, check for references in docs, scripts, or config and update them in the same pass.

---

## Edge Cases

**Clashes:** Append a disambiguator — `meeting-notes-2.md` — or use a date prefix.

**Version strings:** `v1`, `v2`, `v1-2` are fine. Avoid `V1` or `Version1`.

**Sequences:** Zero-pad when order matters — `chunk-01`, `chunk-02`.

**Underscore-prefixed dirs (`_in`, `_out`, `_drafts`):** Treat as acceptable role markers; don't flag.

**Externally-generated asset filenames** (exports from SDL Trados, memoQ, etc. with spaces or locale tags): flag in audits but note that renaming may break upstream workflow references. Ask before applying.
