---
code: CMPUT 325
title: Non-Procedural Programming Languages
units: 3.0
description: A study of the theory, run-time structure, and implementation of selected non-procedural programming languages. Languages will be selected from the domains of functional, and logic-based languages.
prerequisites: CMPUT 201 and 204, or 275; and one of MATH 102, 125, 126, or 127.
corequisites: ''
exclusions: ''
terms:
- W27
- W26
- W25
- W24
- W23
- W22
- W21
- W20
latest_term: W27
catalogue: https://apps.ualberta.ca/catalogue/course/cmput/325
difficulty: Medium
workload: Moderate
languages: ["Lisp", "Prolog"]
last_verified: '2026-10-01'
---

# CMPUT 325: Non-Procedural Programming Languages

## What Students Say

> Imported from the original course reviews page, which mixed student contributions with summarized Reddit discussion. Tips aren't term-stamped yet; if you've taken this course recently, [add your experience](https://github.com/uofa-cs/uofa-cs-wiki/issues/new?template=course-review.yml).

The course begins with the Functional Programming paradigm via Lisp. Functional Programming is completely new if coming from a typical procedural programming background (Python, C; programming involving the execution of instructions top-down), but the paradigm is still fit for general purpose uses. Much of Functional Programming revolves around recursion and in particular defining functions which treat a list elementwise before recursing. Discussion on FP concludes with lambda calculus, which describes how higher-order lambda functions work both fundamentally and through Lisp.

The second half of the course covers the Logical Programming paradigm, which is more polarizing among students who've taken the course; Prolog is arguably a bigger leap than Lisp as the paradigm revolves around defining logical facts and rules to determine solutions. Prolog uses a solution finder that runs a depth-first search on some tree of all possible solutions given a query (goal) and your facts and rules. We also touch on Prolog's feasibility for database querying using various built-in functions. Following coverage of Logical Programming basics, discussion transitions to Constraint Logical Programming in Prolog, which is about restricting the possibilities for a solution to achieve a complex goal more dynamically (e.g., creating a valid Sudoku table).

New to the course as of Winter 2026 is Answer Set Programming, which is **not** general purpose, but opens up possibilities as far as solving difficult problems with less complexity.

**Reviews:** "325 was much more useful and fun. It'll help teach you recursion really well." Another student: "313 is boring and relatively painful to study for but will teach you some fantastic concepts. 325 is more fun."

**Student tips:**
- If you've only programmed in Python/Java/C, functional programming will feel alien at first. Stick with it; the perspective shift is the whole point.
