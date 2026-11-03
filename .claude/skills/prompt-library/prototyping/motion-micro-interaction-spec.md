# Motion & Micro-interaction Spec

*Author: AN · Discipline: prototyping · Tags: micro-interactions*

## ROLE

You are a design engineer specifying and prototyping micro-interactions.

## TASK

Prototype the key micro-interactions for the attached component (e.g. hover, press, toggle, success confirmation). For each, build a working example and document the timing, easing, and properties animated.

## CONTEXT

Motion is usually described in vague words ("snappy", "smooth") that engineers cannot build from. This prototype turns motion into precise, testable values that double as an implementation spec.

## CONSTRAINTS

Specify duration, easing curve, and animated properties for each interaction
Respect prefers-reduced-motion with a non-animated fallback
Keep motion subtle and purposeful, never decorative
CSS transitions/animations only, no animation libraries
All scripts wrapped in DOMContentLoaded

## FORMAT

A single HTML file. For each interaction: a live demo, a short rationale, and a spec table (Property, Duration, Easing, Trigger). Use the design: background #F1F0ED, primary text #0D0D0D, accent #A6A295, white #FFFFFF for cards. Font: Inter.
