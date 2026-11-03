# Recipient-Facing Status States (React + Tailwind)

*Author: AN · Discipline: prototyping · Tags: react, tailwind, fintech, ux-copy*

## ROLE

You are a Design Engineer building a React prototype. You specialise in translating product concepts into clean, production-ready UI using React, Tailwind, and token-based design systems.

## TASK

Build a prototype of the transaction list that replaces internal status labels with recipient-facing outcome states, so users understand what has actually happened from the recipient's perspective rather than guessing at internal pipeline state.

## CONTEXT

The current transaction list shows statuses like "Sent" and "Added" alongside an initiation date. Research shows users interpret "Sent" as "received", creating confusion and avoidable support contacts. This prototype should replace those internal labels with outcome-oriented language that reflects the recipient's reality:  "Recipient notified" — transfer is on its way but not yet landed "Funds available in account" — recipient can access the money "Awaiting bank processing" — transfer is queued at the receiving bank  The visual reference is the existing transaction list: a white surface, circular transaction type icons, recipient name + status + date on the left, amount on the right. Positive amounts (received/added) appear in green. The design should feel native to our design system — clean, minimal, trustworthy.

## CONSTRAINTS

Use React functional components with hooks Use Tailwind utility classes for all styling — no custom CSS Use semantic token-aligned class names where possible (e.g. text-primary, bg-surface) Match the existing Wise transaction list layout: icon · name/status/date · amount Support three transaction states: notified, available, processing Each state should have a distinct but subtle visual treatment (label colour, icon or indicator) Amounts should be formatted with currency code (e.g. 49 EUR, + 50 EUR) Positive/incoming amounts should render in green Use realistic mock data — minimum 4 transactions covering all three states Keep the component small and focused — TransactionList composed of TransactionRow No external dependencies beyond React and Tailwind

## FORMAT

Deliver a single self-contained React component file that can be dropped into a Vite or Next.js project. Include:  TransactionRow — renders a single transaction with icon, recipient name, recipient-facing status label, date, and amount TransactionList — renders the full list with a "Transactions" heading and a "See all" link Mock data array at the top of the file covering all three states Inline comments only where the status logic needs explanation
