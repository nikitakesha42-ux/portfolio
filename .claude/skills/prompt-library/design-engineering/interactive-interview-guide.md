# Interactive Interview Guide

*Author: AN · Discipline: design-engineering · Tags: interactive-guide, vanilla-js, html*

## ROLE

You are a design engineer building interactive single-file HTML tools for research workflows.

## TASK

Format this as an interactive HTML document.
The document should work as a live interview guide with the following features.

## CONTEXT

A fixed sidebar with session metadata, a running timer with start and reset, and a section list that highlights the active section based on scroll position, including when the user reaches the last section. Each question card should have an expandable notes field for typing during the session, an "if needed" prompt styled more subtly than the main question, and a mark as done button that applies a visual completion state without hiding the content. An export notes button in the bottom right that opens a new tab with all notes collected cleanly.

## CONSTRAINTS

All scripts wrapped in DOMContentLoaded.

## FORMAT

Use the following design: background #F1F0ED, primary text #0D0D0D, secondary text #666666, accent #A6A295, white #FFFFFF for cards. Font: Inter. Clean, minimal layout with generous spacing. The layout should be fully responsive with a two column structure on desktop, sidebar fixed on the left and content scrolling on the right.
