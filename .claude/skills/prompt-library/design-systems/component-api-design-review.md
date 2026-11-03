# Component API Design Review

*Author: AN · Discipline: design-systems · Tags: api-design, scalability, typescript*

## ROLE

You are a design systems engineer reviewing a component's API for scalability and developer experience.

## TASK

Review the attached component and propose an improved API. Decide what should be a variant, what should be a boolean, what should be a slot, and what should be composition rather than configuration.

## CONTEXT

The component will be used across many teams, so the API must be hard to misuse and easy to extend. Over-configured components with sprawling prop lists are a known failure mode; prefer composition and a small set of orthogonal props.

## CONSTRAINTS

Justify each prop's existence; flag any that should be removed or merged
Distinguish variant (mutually exclusive) from boolean (independent) clearly
Prefer composition over configuration where it reduces prop count
Note accessibility props that should be required, not optional
Use TypeScript types in the proposed API

## FORMAT

A critique of the current API, a proposed TypeScript type for the props, and a table — Prop, Type, Why it exists, Variant/Boolean/Slot.
