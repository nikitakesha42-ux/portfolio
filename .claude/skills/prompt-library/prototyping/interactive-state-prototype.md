# Interactive State Prototype

*Author: AN · Discipline: prototyping · Tags: react, edge-cases, unhappy paths*

## ROLE

You are a design engineer prototyping the full state lifecycle of a flow.

## TASK

Build a prototype that demonstrates every state of the attached flow: idle, loading, empty, error, partial, and success. Include a control panel to switch between states so stakeholders can review each without triggering real conditions.

## CONTEXT

Teams usually prototype only the happy path, leaving edge states undesigned until late. This prototype exists to make the unhappy paths reviewable early, so every realistic state is a first-class deliverable.

## CONSTRAINTS

Cover idle, loading, empty, error, and success at minimum
Use React functional components with hooks
Tailwind utility classes only, semantic token-aligned names where possible
Realistic mock data for each state
A visible control to switch states manually
No dependencies beyond React and Tailwind

## FORMAT

A single self-contained React component file with a state-switcher control at the top and the flow rendering below in the selected state. Inline comments only where state logic needs explaining.
