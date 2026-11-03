# Research Report → Interactive HMW Guide

*Author: AN · Discipline: design-engineering · Tags: how-might-we, html-tool, insight-mapping, vanilla-js, data-extraction*

## ROLE

You are a senior UX researcher converting a research report into a working design tool for a product team.

## TASK

Convert the attached HTML research report into a single-file interactive HTML HMW guide. Extract all insights, evidence, quotes, data, and priorities directly from the report. Do not invent content.

## CONTEXT

The research report contains findings from a discovery sprint. Each insight in the report maps to one HMW statement. The output will be used by product designers as a working reference during design sprints.

## CONSTRAINTS

Extract content from the attached report only — do not add or invent insights - One HMW card per insight - No external JavaScript libraries - All scripts wrapped in DOMContentLoaded - Single file, runs in any browser with no dependencies

## FORMAT

Design: background #F1F0ED, primary text #0D0D0D, secondary text #666666, accent #A6A295, white #FFFFFF for cards, border #E2E0DA. Font: Inter from Google Fonts. Layout: two-column on desktop — fixed sidebar 280px on the left, content scrolling on the right with max-width 780px. Single column below 900px. Sidebar: study title and description, section navigation with active scroll highlighting, priority key at the bottom. HMW cards: HMW number, priority badge (Priority 1 red, Priority 2 amber, Priority 3 blue), insight reference pill, bold HMW statement with key words in accent colour, rationale in secondary text. A toggle opens two tabs — Evidence & directions and How to measure success. Evidence tab shows quotes, data pills, constraints, and a 2x2 grid of design direction cards. Metrics tab shows a 2x2 grid of metric cards with coloured type labels (Behavioural blue, Qualitative green, Proxy amber, Usability purple), a bold title, description, and target pill. A tinted note block sits below the grid.
