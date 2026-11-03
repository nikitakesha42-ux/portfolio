---
name: writing
description: Copy, content and documentation prompts. Use when critiquing/rewriting copy, writing release notes, auditing microcopy, or compiling a discovery sprint document.
---

# Writing

This skill is the **Writing** phase of my design process — a sequenced set of RTCCF prompts (Role, Task, Context, Constraints, Format).

When the user invokes this skill:

1. Briefly list what's in the phase (the group headings below).
2. Ask **where they are** and offer the groups as a quick menu.
3. Once they pick, read the matching prompt file(s) from this folder (filenames below) and use them as your working instructions. Each file contains one full RTCCF prompt.
4. Ask only for the variables the prompt needs (the product, the data, the research question), then deliver the output in the FORMAT the prompt specifies.
5. If they say "run the whole phase", go through the groups in order.

Prompts in this phase:

## Working on live copy

- **`critique-rewrite-of-existing-copy.md`** — Critique & Rewrite of Existing Copy. Critically evaluate the attached copy, then rewrite it in three distinct variants that pursue different goals (e.g. build trust, drive action, reduce anxiety…
- **`ux-microcopy-audit.md`** — UX Microcopy Audit. Audit the copy in the attached screens and return every string that should be rewritten. For each, give the current text, the problem, and a rewritten versio…

## Shipping updates

- **`release-notes.md`** — Release Notes. Convert the attached changelog or list of merged changes into release notes a non-technical user can understand. Group changes into New, Improved, and Fixed.

## Stakeholder documents

- **`discovery-sprint-compilation.md`** — Discovery Sprint Compilation. Create a clear, well-structured discovery sprint document from the outputs above.

---

Source of truth: `assets/prompts.json` in the portfolio repo. Re-run `scripts/build-skills.py` after editing the JSON and this skill updates.