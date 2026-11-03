---
name: prototyping
description: Prototyping prompts for flows, states, interactions and A/B comparisons. Use when building a working React prototype that covers happy/unhappy paths, compares directions, simulates a mock API, or specifies micro-interactions.
---

# Prototyping

This skill is the **Prototyping** phase of my design process — a sequenced set of RTCCF prompts (Role, Task, Context, Constraints, Format).

When the user invokes this skill:

1. Briefly list what's in the phase (the group headings below).
2. Ask **where they are** and offer the groups as a quick menu.
3. Once they pick, read the matching prompt file(s) from this folder (filenames below) and use them as your working instructions. Each file contains one full RTCCF prompt.
4. Ask only for the variables the prompt needs (the product, the data, the research question), then deliver the output in the FORMAT the prompt specifies.
5. If they say "run the whole phase", go through the groups in order.

Prompts in this phase:

## Behaviour & states

- **`interactive-state-prototype.md`** — Interactive State Prototype. Build a prototype that demonstrates every state of the attached flow: idle, loading, empty, error, partial, and success. Include a control panel to switch be…
- **`data-driven-prototype-with-mock-api.md`** — Data-Driven Prototype with Mock API. Build a prototype of the attached interface that fetches from a mock API layer with realistic latency and occasional failures, so loading and error behaviour…
- **`motion-micro-interaction-spec.md`** — Motion & Micro-interaction Spec. Prototype the key micro-interactions for the attached component (e.g. hover, press, toggle, success confirmation). For each, build a working example and docu…

## Comparisons

- **`a-b-prototype.md`** — A/B Prototype. Build a prototype that renders two distinct design directions for the attached flow side by side (or via a toggle), using the same mock data, so a team can e…

## UI builds

- **`multi-currency-wallet-ui.md`** — Multi-Currency Wallet UI. Recreate the provided UI matching exactly what we have in Figma as a layout, following a structured, component-based approach. Ensure this component is in th…
- **`recipient-facing-status-states-react-tailwind.md`** — Recipient-Facing Status States (React + Tailwind). Build a prototype of the transaction list that replaces internal status labels with recipient-facing outcome states, so users understand what has actually ha…

---

Source of truth: `assets/prompts.json` in the portfolio repo. Re-run `scripts/build-skills.py` after editing the JSON and this skill updates.