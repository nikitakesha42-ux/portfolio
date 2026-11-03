---
name: design-systems
description: Design systems prompts for tokens, components, APIs and accessibility. Use when auditing a component API or tokens, reviewing accessibility against WCAG 2.2 AA, or building a production-ready component.
---

# Design Systems

This skill is the **Design Systems** phase of my design process — a sequenced set of RTCCF prompts (Role, Task, Context, Constraints, Format).

When the user invokes this skill:

1. Briefly list what's in the phase (the group headings below).
2. Ask **where they are** and offer the groups as a quick menu.
3. Once they pick, read the matching prompt file(s) from this folder (filenames below) and use them as your working instructions. Each file contains one full RTCCF prompt.
4. Ask only for the variables the prompt needs (the product, the data, the research question), then deliver the output in the FORMAT the prompt specifies.
5. If they say "run the whole phase", go through the groups in order.

Prompts in this phase:

## Audits

- **`component-audit.md`** — Component Audit. Audit these screens and return every element that should become a reusable Figma component. Name each one, describe what makes it distinct, estimate how many…
- **`accessibility-conformance-audit.md`** — Accessibility Conformance Audit. Audit the attached components and list every accessibility issue. For each, name the affected element, the specific success criterion at risk, the impact on …

## Build

- **`component-api-design-review.md`** — Component API Design Review. Review the attached component and propose an improved API. Decide what should be a variant, what should be a boolean, what should be a slot, and what should …
- **`production-ready-component-set.md`** — Production-Ready Component Set. Build a production-ready Avatar component set from the attached Figma:

---

Source of truth: `assets/prompts.json` in the portfolio repo. Re-run `scripts/build-skills.py` after editing the JSON and this skill updates.