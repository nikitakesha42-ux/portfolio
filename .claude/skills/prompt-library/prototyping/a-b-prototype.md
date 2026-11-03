# A/B Prototype

*Author: AN · Discipline: prototyping · Tags: react, ab-testing*

## ROLE

You are a design engineer building a prototype to compare two design directions for the same problem.

## TASK

Build a prototype that renders two distinct design directions for the attached flow side by side (or via a toggle), using the same mock data, so a team can evaluate them against each other in a session.

## CONTEXT

Choosing between directions in the abstract leads to opinion-led debates. A working side-by-side comparison on identical data lets the team judge against behaviour and clarity rather than description.

## CONSTRAINTS

Both directions must use the same underlying mock data
Each direction should represent a genuinely different approach, not a restyle
React functional components with hooks
Tailwind utility classes, semantic token-aligned names where possible
Include a short labelled note stating what each direction optimises for
No dependencies beyond React and Tailwind

## FORMAT

A single self-contained React component file with a toggle or split layout switching between Direction A and Direction B, a shared mock data array at the top, and a label above each describing its strategic intent.
