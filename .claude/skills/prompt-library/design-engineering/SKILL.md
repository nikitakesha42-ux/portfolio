---
name: design-engineering
description: Design engineering prompts for building single-file HTML tools — interview guides, surveys, research reports, HMW guides, Netlify forms. Use when turning a research artefact into a working, deployable HTML document.
---

# Design Engineering

This skill is the **Design Engineering** phase of my design process — a sequenced set of RTCCF prompts (Role, Task, Context, Constraints, Format).

When the user invokes this skill:

1. Briefly list what's in the phase (the group headings below).
2. Ask **where they are** and offer the groups as a quick menu.
3. Once they pick, read the matching prompt file(s) from this folder (filenames below) and use them as your working instructions. Each file contains one full RTCCF prompt.
4. Ask only for the variables the prompt needs (the product, the data, the research question), then deliver the output in the FORMAT the prompt specifies.
5. If they say "run the whole phase", go through the groups in order.

Prompts in this phase:

## Interactive guides

- **`interactive-interview-guide.md`** — Interactive Interview Guide. Format this as an interactive HTML document.
- **`bgoalc-interactive-interview-guide.md`** — BGOALC Interactive Interview Guide. Format this as an interactive HTML document.
- **`tasks-interactive-interview-guide.md`** — TASKS  Interactive Interview Guide. Format this as an interactive HTML document.
- **`interactive-prime-research-report.md`** — Interactive PRIME Research Report. Format this as an interactive HTML document.
- **`research-report-interactive-hmw-guide.md`** — Research Report → Interactive HMW Guide. Convert the attached HTML research report into a single-file interactive HTML HMW guide. Extract all insights, evidence, quotes, data, and priorities directl…

## Surveys & forms

- **`styling-the-validation-survey.md`** — Styling the Validation Survey. Format this as a styled HTML form.
- **`adding-netlify-form.md`** — Adding Netlify Form. Add Netlify form handling to this HTML survey.

---

Source of truth: `assets/prompts.json` in the portfolio repo. Re-run `scripts/build-skills.py` after editing the JSON and this skill updates.