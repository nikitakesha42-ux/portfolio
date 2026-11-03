# Data-Driven Prototype with Mock API

*Author: AN · Discipline: prototyping · Tags: react, mock-api, data-fetching*

## ROLE

You are a design engineer building a prototype that behaves like it has a real backend.

## TASK

Build a prototype of the attached interface that fetches from a mock API layer with realistic latency and occasional failures, so loading and error behaviour feel real during testing.

## CONTEXT

Prototypes with instant, perfect data hide the real experience of waiting and failure. This one simulates network conditions so usability sessions surface how the design handles latency and errors.

## CONSTRAINTS

Mock API layer with simulated delay and a configurable failure rate
Render genuine loading and error states driven by the fetch lifecycle
React functional components with hooks
Tailwind utility classes, semantic token-aligned names where possible
Realistic mock dataset, minimum 8 records
No dependencies beyond React and Tailwind

## FORMAT

A single self-contained React component file. Mock API functions at the top, a control to adjust latency and failure rate, and the interface rendering live below. Inline comments only on the async logic.
