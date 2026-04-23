---
title: "CMPUT 415 — Compiler Design"
course_code: CMPUT 415
course_year: "400"
course_topics:
  - Languages
  - Systems
course_difficulty: Brutal
course_workload: Overwhelming
course_relevance: High
course_units: "3 units (fi 6)(EITHER, 3-0-3)"
hide:
  - navigation
---

# CMPUT 415 — Compiler Design

*3 units (fi 6)(EITHER, 3-0-3)*

**Difficulty:** Brutal • **Workload:** Overwhelming • **Industry relevance:** High

## Calendar Description

Compilers, interpreters, lexical analysis, syntax analysis, syntax- directed translation, symbol tables, type checking, flow analysis, code generation, code optimization. Prerequisites: one of CMPUT 229, E E 380, or ECE 212, and any 300-level Computing Science course.

## Prerequisites

Prerequisites: one of CMPUT 229, E E 380, or ECE 212, and any 300-level Computing Science course.

## Student Review

**Difficulty:** Brutal | **Workload:** Overwhelming | **Industry relevance:** Medium-High

Lexing, parsing, ASTs, semantic analysis, code generation, LLVM. One of the most work-intensive courses in the program.

"The workload never lets up. You constantly need to be working on stuff. As soon as an assignment is done, it's in your best interest to start the next one immediately." And: "Without a doubt the most work I've had to do for a CMPUT course. Also the course I learned the most in; in retrospect, I would still take it again."

The project is a full LLVM-based compiler for an obscure IBM language (the spec is 40 pages and glosses over features). Most groups don't finish all features.

**Student tips:**
- Know Java before you start (that's what the implementation uses).
- Look up ANTLR (parser generator) and LLVM before the course begins.
- Do not take 415 with other heavy courses. Three moderate courses + 415 is better than 415 + one other heavy course.
- Despite the pain, this course is worth it if you're interested in compilers, developer tooling, or understanding how languages work.

## Why It's a Hidden Gem

**Why almost nobody takes it:** It sounds academic. "Nobody writes compilers in industry," people say. They're wrong, but more importantly, they're missing why this course matters.

**What students actually say:** This is one of the most universally respected "hard" courses in the program. One Reddit review: *"Without a doubt the most work I've had to do for a CMPUT course. Also the course that I learned the most in; in retrospect, I would still take it again."*

The project is a full LLVM-based compiler for a defunct IBM language with a 40-page spec. The spec glosses over features. Most groups don't fully implement everything. The workload "never lets up; as soon as an assignment is done, start the next one immediately."

Before taking it: know Java well (implementation language), look up ANTLR (parser generator) and LLVM basics. Don't take 415 in the same semester as another heavy course like 229 or 466.

**Why you should take it:** Understanding how a compiler works changes how you think about code. By the end of this course, you understand:

- **Lexing and parsing:** how source code text becomes an abstract syntax tree (AST). This is directly relevant to any tool that processes code: linters, formatters, transpilers, IDEs
- **Semantic analysis:** type checking, scope resolution, symbol tables
- **Intermediate representations:** how compilers represent code in a form that can be optimized
- **Code generation and optimization:** how high-level code becomes machine instructions, and how optimizations like dead code elimination, inlining, and loop unrolling work

**Where this is useful:**

- **Developer tooling companies:** JetBrains, GitHub, Sourcegraph, Stripe (their developer tools team), any company building IDE features, static analysis tools, or code generation
- **Programming language work:** designing DSLs (domain-specific languages), building interpreters, working on language runtimes
- **Senior engineering interviews:** explaining you've built a compiler immediately establishes technical credibility. Senior engineers know it's hard.

Beyond career utility, this course makes you a better programmer across the board. You stop thinking of your language as magic and start thinking of it as a tool with understandable behavior.

## Related Pages

- [Course Catalogue](./index.md)
- [Course Guide](../course-guide.md)
- [Hidden Gems](../hidden-gems.md)
- [Professor Guide](../professor-guide.md)

_Calendar source: <https://apps.ualberta.ca/catalogue/course/cmput/415>_
