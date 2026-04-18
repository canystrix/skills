"""Grade interview-prep eval outputs against assertions.

Walks the iteration directory, reads each run's outputs, evaluates the
assertions in eval_metadata.json, and writes grading.json per run.

Output fields follow the skill-creator viewer's expected schema:
- text, passed, evidence
"""

import json
import re
import sys
from pathlib import Path


GERMAN_MARKERS = ["Frage", "Antwort", "Unternehmen", "Rolle", "und", "die", "Sie"]
ROLE_SIEM_TERMS = ["SIEM", "Use Case", "SOC", "Alert", "Detection", "Log"]
FS_REG_TERMS = ["DORA", "BAIT", "MaRisk", "NIS-2", "NIS2"]
CONSULTING_GAP_CUES = [
    "Beratungserfahrung", "Consulting-Erfahrung", "keine Beratung",
    "keine Consulting", "erste Mal in der Beratung", "Inhouse", "inhouse",
    "Wechsel in die Beratung", "erstmalig in die Beratung", "noch keine",
]


def read_md(run_dir):
    """Return the concatenated text of every .md file under outputs/."""
    out = run_dir / "outputs"
    if not out.exists():
        return ""
    parts = []
    for path in out.rglob("*.md"):
        parts.append(path.read_text(encoding="utf-8", errors="ignore"))
    return "\n\n".join(parts)


def has_docx(run_dir):
    """True if any .docx exists under outputs/."""
    out = run_dir / "outputs"
    if not out.exists():
        return False
    return any(out.rglob("*.docx"))


def check_is_german(md):
    """Heuristic: count German markers vs total length."""
    hits = sum(md.count(w) for w in GERMAN_MARKERS)
    return hits >= 5, f"{hits} German markers detected"


def check_section(md, patterns):
    """True if any of the patterns appears as a heading or bold label."""
    for pat in patterns:
        if re.search(pat, md, flags=re.IGNORECASE):
            return True, f"matched '{pat}'"
    return False, f"none of {patterns!r} found"


def check_qa_count(md, minimum=10):
    """Count distinct interview questions — look for F: markers or '?' lines in a questions section."""
    f_markers = len(re.findall(r"^\*\*F:\*\*", md, flags=re.MULTILINE))
    if f_markers >= minimum:
        return True, f"{f_markers} 'F:' markers"
    question_lines = len(re.findall(r"\?[\"')\s]*$", md, flags=re.MULTILINE))
    ok = question_lines >= minimum
    return ok, f"{f_markers} F-markers, {question_lines} '?' line endings"


def check_qa_format(md, minimum=5):
    """True if F:/A-Skizze:/Verbindung: pattern appears minimum times together."""
    pattern = re.compile(
        r"\*\*F:\*\*.+?\*\*A-Skizze:\*\*.+?\*\*Verbindung:\*\*",
        flags=re.DOTALL,
    )
    matches = len(pattern.findall(md))
    return matches >= minimum, f"{matches} full F/A-Skizze/Verbindung triples"


def check_no_konzernweit(md):
    """Fail if corporate-wide ISMS scope is claimed for Lutz.

    Flags only sentences where 'konzernweit'/'unternehmensweit' appears
    *without* a nearby negation (nicht, kein, ohne). Explicitly denying
    corporate-wide scope is the desired behaviour.
    """
    violations = []
    for sentence in re.split(r"(?<=[.!?])\s+|\n", md):
        if re.search(r"konzernweit|unternehmensweit", sentence, flags=re.IGNORECASE):
            if not re.search(r"\bnicht\b|\bkein", sentence, flags=re.IGNORECASE):
                violations.append(sentence.strip()[:80])
    ok = not violations
    evidence = "clean" if ok else f"{len(violations)} claim(s): {violations[:2]}"
    return ok, evidence


def check_db_systel(md):
    """If DB Systel is mentioned, it must be framed as IT-Partner der Deutschen Bahn."""
    mentions = re.findall(r"DB[- ]?Systel", md, flags=re.IGNORECASE)
    if not mentions:
        return True, "DB Systel not mentioned (N/A)"
    ok = bool(re.search(r"IT[- ]?Partner der Deutschen Bahn", md, flags=re.IGNORECASE))
    wrong = bool(re.search(r"Infrastrukturdienstleister", md, flags=re.IGNORECASE))
    return ok and not wrong, f"DB Systel mentioned {len(mentions)}x; IT-Partner={ok}; wrong-framing={wrong}"


def check_role_siem(md):
    hits = sum(1 for t in ROLE_SIEM_TERMS if re.search(t, md, flags=re.IGNORECASE))
    return hits >= 3, f"{hits}/{len(ROLE_SIEM_TERMS)} SIEM terms"


def check_fs_regulatory(md):
    hits = [t for t in FS_REG_TERMS if re.search(t, md, flags=re.IGNORECASE)]
    return bool(hits), f"found: {hits}" if hits else "no FS regulations mentioned"


def check_consulting_gap(md):
    hits = [c for c in CONSULTING_GAP_CUES if c in md]
    return bool(hits), f"cues: {hits}" if hits else "no consulting-gap framing found"


def check_company_questions(md, company_terms):
    """Look for company-specific terms near a 'Fragen an' or 'Rückfragen' section."""
    for term in company_terms:
        if re.search(re.escape(term), md, flags=re.IGNORECASE):
            return True, f"found '{term}'"
    return False, "no company-specific terms in text"


GRADERS = {
    "has_md": lambda md, dr, cfg: (bool(md.strip()), f"{len(md)} chars of markdown"),
    "has_docx": lambda md, dr, cfg: (has_docx(dr), "docx present" if has_docx(dr) else "no .docx found"),
    "is_german": lambda md, dr, cfg: check_is_german(md),
    "section_fragen": lambda md, dr, cfg: check_section(
        md, [r"Wahrscheinliche Fragen", r"## .*Fragen", r"\bF:\b", r"Interviewfragen"]
    ),
    "section_luecken": lambda md, dr, cfg: check_section(
        md, [r"L\u00fccken", r"Risiken", r"Schw\u00e4chen", r"rote Linien"]
    ),
    "section_highlights": lambda md, dr, cfg: check_section(
        md, [r"Highlights", r"St\u00e4rken", r"Gespr\u00e4chs", r"Cheatsheet", r"Cheat Sheet"]
    ),
    "section_fragen_an": lambda md, dr, cfg: check_section(
        md, [r"Fragen an", r"R\u00fcckfragen", r"Gegenfragen", r"Fragen, die"]
    ),
    "qa_count": lambda md, dr, cfg: check_qa_count(md),
    "qa_format": lambda md, dr, cfg: check_qa_format(md),
    "no_konzernweit": lambda md, dr, cfg: check_no_konzernweit(md),
    "db_systel_correct": lambda md, dr, cfg: check_db_systel(md),
    "role_specific_siem": lambda md, dr, cfg: check_role_siem(md),
    "fs_regulatory_coverage": lambda md, dr, cfg: check_fs_regulatory(md),
    "consulting_gap_honest": lambda md, dr, cfg: check_consulting_gap(md),
    "company_specific_questions": lambda md, dr, cfg: check_company_questions(md, cfg["company_terms"]),
}


EVAL_CONFIG = {
    "dwp-bank-siem-expert": {
        "company_terms": ["dwpbank", "dwp-bank", "dwp bank", "WertpapierService"],
    },
    "kpmg-consulting-financial-services": {
        "company_terms": ["KPMG"],
    },
    "qas-company-ag-senior-consultant": {
        "company_terms": ["QAS", "QAS Company"],
    },
}


def grade_run(run_dir, assertions, cfg):
    md = read_md(run_dir)
    expectations = []
    for a in assertions:
        grader = GRADERS.get(a["id"])
        if not grader:
            expectations.append({"text": a["text"], "passed": False, "evidence": f"no grader for id={a['id']}"})
            continue
        try:
            passed, evidence = grader(md, run_dir, cfg)
        except Exception as e:
            passed, evidence = False, f"grader error: {e}"
        expectations.append({"text": a["text"], "passed": passed, "evidence": evidence})
    total = len(expectations)
    passed_count = sum(1 for e in expectations if e["passed"])
    summary = {
        "pass_rate": round(passed_count / total, 4) if total else 0.0,
        "passed": passed_count,
        "failed": total - passed_count,
        "total": total,
    }
    return {"summary": summary, "expectations": expectations}


def main(iteration_dir):
    iter_path = Path(iteration_dir)
    for eval_dir in sorted(iter_path.iterdir()):
        if not eval_dir.is_dir():
            continue
        meta_path = eval_dir / "eval_metadata.json"
        if not meta_path.exists():
            continue
        meta = json.loads(meta_path.read_text())
        cfg = EVAL_CONFIG.get(meta["eval_name"], {"company_terms": []})
        for run_name in ("with_skill", "without_skill"):
            cfg_dir = eval_dir / run_name
            if not cfg_dir.exists():
                continue
            # Grade into each run-N directory (aggregator expects run-* layer)
            run_dirs = sorted(cfg_dir.glob("run-*")) or [cfg_dir]
            for run_dir in run_dirs:
                result = grade_run(run_dir, meta["assertions"], cfg)
                (run_dir / "grading.json").write_text(json.dumps(result, ensure_ascii=False, indent=2))
                s = result["summary"]
                print(f"{meta['eval_name']}/{run_name}/{run_dir.name}: {s['passed']}/{s['total']}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
