#!/usr/bin/env python3
"""
build-skills.py — regenerate Claude Code skills from assets/prompts.json.

Reads the single source of truth (assets/prompts.json) and writes one skill
per phase into .claude/skills/prompt-library/<phase>/:

  SKILL.md               ← orchestrator for the phase (routes to prompts)
  <slug>.md              ← one prompt per file, RTCCF body
  ...

Install path (once, globally for your user):
  ln -s "$(pwd)/.claude/skills/prompt-library" ~/.claude/skills/prompt-library
Or copy if you prefer a snapshot:
  cp -R .claude/skills/prompt-library ~/.claude/skills/prompt-library

Re-run this script whenever you edit prompts.json and the installed skills update
immediately (if you symlinked) or after the next copy (if you didn't).

Usage:
  python3 scripts/build-skills.py            # build with defaults
  python3 scripts/build-skills.py --clean    # delete the output dir first
"""
from __future__ import annotations
import argparse, json, re, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "prompts.json"
OUT = ROOT / ".claude" / "skills" / "prompt-library"

PHASES = {
    "ux-research": {
        "title": "UX Research",
        "desc":  "Full UX Research phase — surveys, interviews, synthesis. Use when running a discovery sprint, planning user research, interviewing a stakeholder, writing a survey, or synthesising data into a problem statement, needs, HMW statements or a research report.",
        "groups": [
            ("Planning (new research)", [
                "stakeholder-interview-guide",
                "bgoalc-user-interview-script",
                "user-survey-to-validate-behavioural-patterns",
                "tasks-usability-test-script",
            ]),
            ("Analysing (after data collection)", [
                "behavioural-breakdown",
                "clustering-behaviours-into-core-user-needs",
                "reframing-the-problem",
                "problem-statement",
                "problem-statement-stress-test",
                "hmw-statements",
            ]),
            ("Reporting & next steps", [
                "prime-research-report",
                "rapid-ideation",
            ]),
        ],
    },
    "writing": {
        "title": "Writing",
        "desc": "Copy, content and documentation prompts. Use when critiquing/rewriting copy, writing release notes, auditing microcopy, or compiling a discovery sprint document.",
        "groups": [
            ("Working on live copy", [
                "critique-rewrite-of-existing-copy",
                "ux-microcopy-audit",
            ]),
            ("Shipping updates", [
                "release-notes",
            ]),
            ("Stakeholder documents", [
                "discovery-sprint-compilation",
            ]),
        ],
    },
    "design-systems": {
        "title": "Design Systems",
        "desc": "Design systems prompts for tokens, components, APIs and accessibility. Use when auditing a component API or tokens, reviewing accessibility against WCAG 2.2 AA, or building a production-ready component.",
        "groups": [
            ("Audits", [
                "component-audit",
                "accessibility-conformance-audit",
            ]),
            ("Build", [
                "component-api-design-review",
                "production-ready-component-set",
            ]),
        ],
    },
    "prototyping": {
        "title": "Prototyping",
        "desc": "Prototyping prompts for flows, states, interactions and A/B comparisons. Use when building a working React prototype that covers happy/unhappy paths, compares directions, simulates a mock API, or specifies micro-interactions.",
        "groups": [
            ("Behaviour & states", [
                "interactive-state-prototype",
                "data-driven-prototype-with-mock-api",
                "motion-micro-interaction-spec",
            ]),
            ("Comparisons", [
                "a-b-prototype",
            ]),
            ("UI builds", [
                "multi-currency-wallet-ui",
                "recipient-facing-status-states-react-tailwind",
            ]),
        ],
    },
    "design-engineering": {
        "title": "Design Engineering",
        "desc": "Design engineering prompts for building single-file HTML tools — interview guides, surveys, research reports, HMW guides, Netlify forms. Use when turning a research artefact into a working, deployable HTML document.",
        "groups": [
            ("Interactive guides", [
                "interactive-interview-guide",
                "bgoalc-interactive-interview-guide",
                "tasks-interactive-interview-guide",
                "interactive-prime-research-report",
                "research-report-interactive-hmw-guide",
            ]),
            ("Surveys & forms", [
                "styling-the-validation-survey",
                "adding-netlify-form",
            ]),
        ],
    },
}


def slugify(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def section(label: str, body: str) -> str:
    body = (body or "").strip()
    if not body:
        return ""
    return f"## {label}\n\n{body}\n"


def write_prompt(folder: Path, p: dict) -> str:
    slug = slugify(p["title"])
    path = folder / f"{slug}.md"
    tags = ", ".join(p.get("tags") or [])
    body = [
        f"# {p['title']}",
        "",
        f"*Author: {p.get('author','AN')} · Discipline: {p['discipline']}" +
            (f" · Tags: {tags}" if tags else "") + "*",
        "",
        section("ROLE",        p.get("role","")),
        section("TASK",        p.get("task","")),
        section("CONTEXT",     p.get("context","")),
        section("CONSTRAINTS", p.get("constraints","")),
        section("FORMAT",      p.get("format","")),
    ]
    path.write_text("\n".join(x for x in body if x is not None))
    return slug


def write_orchestrator(folder: Path, phase_id: str, phase_meta: dict,
                        prompts_in_phase: list[dict], slug_for_title: dict[str,str]) -> None:
    title   = phase_meta["title"]
    desc    = phase_meta["desc"]
    groups  = phase_meta["groups"]

    # map slug → prompt (for pulling one-liners from TASK)
    by_slug = {slug_for_title[p["title"]]: p for p in prompts_in_phase}

    lines = [
        "---",
        f"name: {phase_id}",
        f"description: {desc}",
        "---",
        "",
        f"# {title}",
        "",
        f"This skill is the **{title}** phase of my design process — a sequenced set of RTCCF prompts (Role, Task, Context, Constraints, Format).",
        "",
        "When the user invokes this skill:",
        "",
        "1. Briefly list what's in the phase (the group headings below).",
        "2. Ask **where they are** and offer the groups as a quick menu.",
        "3. Once they pick, read the matching prompt file(s) from this folder (filenames below) and use them as your working instructions. Each file contains one full RTCCF prompt.",
        "4. Ask only for the variables the prompt needs (the product, the data, the research question), then deliver the output in the FORMAT the prompt specifies.",
        "5. If they say \"run the whole phase\", go through the groups in order.",
        "",
        "Prompts in this phase:",
        "",
    ]

    for group_name, slugs in groups:
        # skip groups that have no matching slugs (defensive)
        present = [s for s in slugs if s in by_slug]
        if not present: continue
        lines.append(f"## {group_name}")
        lines.append("")
        for slug in present:
            p = by_slug[slug]
            task_oneline = (p.get("task") or "").strip().split("\n")[0]
            if len(task_oneline) > 160: task_oneline = task_oneline[:157] + "…"
            lines.append(f"- **`{slug}.md`** — {p['title']}. {task_oneline}")
        lines.append("")

    # Any prompts in the discipline that weren't grouped above
    grouped = {s for _, ss in groups for s in ss}
    leftovers = [p for p in prompts_in_phase if slug_for_title[p["title"]] not in grouped]
    if leftovers:
        lines.append("## Other")
        lines.append("")
        for p in leftovers:
            slug = slug_for_title[p["title"]]
            task_oneline = (p.get("task") or "").strip().split("\n")[0]
            if len(task_oneline) > 160: task_oneline = task_oneline[:157] + "…"
            lines.append(f"- **`{slug}.md`** — {p['title']}. {task_oneline}")
        lines.append("")

    lines += [
        "---",
        "",
        f"Source of truth: `assets/prompts.json` in the portfolio repo. Re-run `scripts/build-skills.py` after editing the JSON and this skill updates.",
    ]
    (folder / "SKILL.md").write_text("\n".join(lines))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--clean", action="store_true", help="delete the output folder first")
    args = ap.parse_args()

    with SRC.open() as f:
        doc = json.load(f)
    prompts = doc.get("prompts") if isinstance(doc, dict) else doc
    if not prompts:
        raise SystemExit(f"no prompts in {SRC}")

    if args.clean and OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True, exist_ok=True)

    # bucket by discipline
    by_disc: dict[str, list[dict]] = {}
    for p in prompts:
        by_disc.setdefault(p["discipline"], []).append(p)

    root_readme = [
        "# Prompt Library — Claude Code skills",
        "",
        "Generated from `assets/prompts.json` by `scripts/build-skills.py`.",
        "",
        "## Install",
        "",
        "Symlink (recommended — edits to the JSON flow through automatically after a rebuild):",
        "",
        "```bash",
        "ln -s \"$(pwd)/.claude/skills/prompt-library\" ~/.claude/skills/prompt-library",
        "```",
        "",
        "Or copy a snapshot:",
        "",
        "```bash",
        "mkdir -p ~/.claude/skills && cp -R .claude/skills/prompt-library ~/.claude/skills/",
        "```",
        "",
        "## Use",
        "",
        "In Claude Code, invoke a phase with its slash command:",
        "",
    ]
    total_files = 0
    for phase_id, meta in PHASES.items():
        bucket = by_disc.get(phase_id, [])
        if not bucket: continue
        phase_dir = OUT / phase_id
        phase_dir.mkdir(exist_ok=True)

        slug_for_title: dict[str,str] = {}
        for p in bucket:
            slug_for_title[p["title"]] = write_prompt(phase_dir, p)
            total_files += 1
        write_orchestrator(phase_dir, phase_id, meta, bucket, slug_for_title)
        total_files += 1

        root_readme.append(f"- `/{phase_id}` — {meta['title']} ({len(bucket)} prompts)")

    root_readme += [
        "",
        "Pick a phase, Claude asks where you are, then runs the matching RTCCF prompt file.",
        "",
        "## Rebuild",
        "",
        "```bash",
        "python3 scripts/build-skills.py --clean   # fresh rebuild from prompts.json",
        "```",
    ]
    (OUT / "README.md").write_text("\n".join(root_readme))
    print(f"wrote {total_files + 1} files to {OUT}")


if __name__ == "__main__":
    main()
