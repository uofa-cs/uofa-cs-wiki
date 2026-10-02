---
code: CMPUT 415
title: Compiler Design
units: 3.0
description: Compilers, interpreters, lexical analysis, syntax analysis, syntax- directed translation, symbol tables, type checking, flow analysis, code generation, code optimization.
prerequisites: one of CMPUT 229, E E 380, or ECE 212, and any 300-level Computing Science course.
corequisites: ''
exclusions: ''
terms:
- F26
- F25
- F24
- F23
- F22
- F20
- F18
- F16
latest_term: F26
catalogue: https://apps.ualberta.ca/catalogue/course/cmput/415
difficulty: Brutal
workload: Overwhelming
languages: ["C++", "ANTLR", "MLIR/LLVM", "CMake"]
course_site: "https://cmput415.github.io/415-docs/"
last_verified: '2026-10-01'
---

# CMPUT 415: Compiler Design

## What It Covers

A sequence of team projects in C++ with ANTLR and MLIR/LLVM: Generator, a LOLCODE interpreter, VCalc, and finally a compiler for Gazprea, a language derived from one originally designed at IBM's Hardware Acceleration Laboratory in Markham. Each project also has a competitive testing component, and the current course docs add an individual lab exam after each project: you fix a bug, write a test, and add a feature to a small compiler for an unfamiliar language, on a lab machine. ([course docs](https://cmput415.github.io/415-docs/))

## What Students Say

> Imported from the original course reviews page, which mixed student contributions with summarized Reddit discussion. Tips aren't term-stamped yet; if you've taken this course recently, [add your experience](https://github.com/uofa-cs/uofa-cs-wiki/issues/new?template=course-review.yml).

Grammars (ANTLR4, finite state automata), lexing, parsing (and the history of parsers), abstract syntax trees (AST), semantic analysis (including variable scopes and lifetime), code generation, LLVM/MLIR, compiler optimization (basic blocks, dataflow, available expressions), and register allocation. One of the most work-intensive courses in the program on account of the project.

The Gazprea spec is about 40 pages and glosses over features. Most groups don't finish all features. Part of your evaluation is competitive testing: every team submits a test suite that checks adherence to the specification and coverage of edge cases, every team's compiler is run against every suite, and you earn points both when other teams' compilers fail your tests and when yours passes theirs.

**Reviews:**
> "The workload never lets up. You constantly need to be working. As soon as an assignment is done, it's in your best interest to start the next one immediately."
> "Without a doubt the most work I've had to do for a CMPUT course. Also the course I learned the most in; in retrospect, I would still take it again."

**Student tips:**
- Proficiency in C++ is assumed; intimate familiarity is essential.
- Look up ANTLR (parser generator) and LLVM/MLIR before the course begins.
- Do not take 415 with other heavy or project-based courses. Despite lectures ending a whole month before the end of the semester, working on the project itself is practically a full-time commitment.
- Despite the challenges, this course is worth it if you're interested in compilers, developer tooling, or understanding how language frontends work.

**Instructor notes:**
- **Ron Unrau:** "Ron's lectures are interesting and engaging, given his personal experience in industry. He is also understanding and gives fair exams, in addition to ample resources to prepare."
- **José Nelson Amaral:** may appear throughout the semester even when Prof. Unrau is the instructor. His [2020 lecture videos](https://cmput415.github.io/415-lectures/) have aged well, since both instructors use his slides.
