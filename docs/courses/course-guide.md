# UofA CS Course Guide — What Actually Matters for Industry

This is an opinionated guide, not the official calendar. It's written from the perspective of someone who has been through the program and watched classmates go on to internships and jobs at Google, Amazon, Shopify, RBC, and startups. Some courses look great on paper and teach you nothing useful. Others are underrated. This guide cuts through it.

> **Take CMPUT 204 seriously. It is the single most important course for software engineering interviews.**

For detailed course-by-course reviews including difficulty ratings, workload estimates, and best/worst professor recommendations backed by RMP data and student Reddit discussions, see the [Course Reviews](./course-reviews.md) page. For a full professor guide with tier list, see [Professor Guide](./professor-guide.md).

---

## Foundation Courses — Everyone Needs These

These are your first two years. Don't try to optimize them — just pass them well and understand the fundamentals. Every single course here has downstream consequences.

### CMPUT 174 / 175 — Introduction to Computing I & II

**What it is:** Python basics, functions, recursion, basic data structures. If you've never programmed before, this is where you start. If you have, it's still worth paying attention — the formal thinking about recursion and abstraction is more rigorous than most high school or self-taught experience.

**Reality check:** Survival is the goal for many students in 175 — the jump from 174 is real. The recursive thinking introduced here is foundational for everything in your upper years. Don't blow it off.

**Industry relevance:** Low directly, high indirectly. This is where you build your programming instincts.

---

### CMPUT 201 — Practical Programming Methodology

**What it is:** C programming. Memory management. Pointers. makefiles. Debugging with gdb. Version control introduced here for many students.

**Why it matters:** This course introduces real development discipline. You learn what's actually happening in memory when you write code. You understand pointers, stack vs heap, segfaults. Every backend engineer, systems programmer, and SWE who has worked with performance-sensitive code will tell you that understanding C-level memory makes you a better programmer in every language. This course is crucial.

**Industry relevance:** Medium-high. Not because you'll write C at most jobs, but because you'll finally understand what your programs are actually doing. This makes you dangerous in a good way.

---

### CMPUT 204 — Algorithms I

**What it is:** Asymptotic analysis (Big-O), sorting algorithms, divide and conquer, graph algorithms (BFS, DFS, Dijkstra, etc.), dynamic programming, greedy algorithms.

**Why it matters:** This is THE most important course for software engineering interviews. Every major tech company — FAANG, Shopify, Microsoft, and most mid-sized companies — will ask you algorithmic coding problems. The material in CMPUT 204 maps directly to LeetCode medium and hard problems.

- Big-O: You will be asked about complexity in every interview.
- Sorting: QuickSort, MergeSort — you need to know them cold.
- Graph algorithms: BFS/DFS come up constantly. Dijkstra is fair game.
- Dynamic programming: The hardest topic, the most commonly tested.

**Take it seriously.** Do extra problems. Review the textbook. Revisit the material before every interview season.

**Industry relevance:** CRITICAL. There is no course at UofA more directly connected to getting a job.

---

### CMPUT 272 — Formal Systems and Logic

**What it is:** Propositional logic, predicate logic, proofs, set theory, formal reasoning.

**Why it matters:** Tedious? Yes. A prerequisite for upper-year courses and for thinking rigorously about correctness? Also yes. You'll use the proof techniques and logical thinking in 379, 304, and any ML/AI courses. Push through it.

**Industry relevance:** Low directly, foundational indirectly.

---

### CMPUT 229 — Computer Organization and Architecture

**What it is:** Assembly language, digital circuits, ALU design, memory hierarchy (registers, cache, RAM, disk), pipelining.

**Why it matters:** This is where you find out how computers actually work. After this course, "the computer does X" becomes "the CPU fetches the instruction, decodes it, executes it, and writes back to a register, and if it's a cache miss, here's what happens." That mental model pays dividends. Systems roles at any level require this understanding. Even web devs benefit — knowing why cache locality matters makes you a better programmer.

**Student reality:** Consistently cited as one of the hardest courses in the program. One student described the semester memorably: *"One time a friend asked me, 'How's life besides 229?' I quickly answered, 'There is no life besides 229.'"* Workload-wise, it's heavy regardless of instructor. Professor matters enormously here — see [Course Reviews](./course-reviews.md#cmput-229--computer-organization-and-architecture) for specific professor guidance.

**Industry relevance:** High for systems roles, medium-high for everyone else.

---

## Core Upper-Year Courses

These are typically 3rd-year courses. They're where the program gets real.

### CMPUT 291 — Introduction to File and Database Management

**What it is:** Relational databases, SQL, ER modeling, normalization, indexing, transactions.

**Why it matters:** Every company uses databases. Every single one. You will write SQL in your first job, and probably every job after that. This course teaches you to think in terms of data models, understand query performance, and design schemas. Students who skip this or sleepwalk through it consistently struggle in real work environments.

**Industry relevance:** ESSENTIAL. Backend, data engineering, full-stack — all require this.

---

### CMPUT 301 — Introduction to Software Engineering

**What it is:** Software development lifecycle, requirements, UML, design patterns, agile methodologies, version control workflows, group projects.

**Why it matters:** The theory can feel abstract, but the group project is the real lesson. You'll learn how to work with other programmers on a shared codebase, handle version control conflicts, write documentation others can use, and navigate the dysfunction that happens in every software team. The design patterns (Observer, Factory, Strategy, etc.) also show up in interviews.

**Industry relevance:** Medium-high. Less for the theory, more for the teamwork fundamentals.

---

### CMPUT 379 — Environment and Language Tools for Systems Programming

**What it is:** Processes, threads, inter-process communication, signals, synchronization (mutexes, semaphores), memory management, file systems, and the Linux environment.

**Why it matters:** This is operating systems. If you ever wonder why your program hangs, why a mutex deadlocks, or how Docker containers actually work — this course gives you the language and mental models. Systems engineering roles at cloud companies, game studios, and infrastructure teams require this knowledge. But even application developers benefit from understanding what the OS is doing underneath them.

**Industry relevance:** Critical for systems roles, important for everyone.

---

### CMPUT 313 — Communication Networks

**What it is:** TCP/IP stack, HTTP, DNS, sockets programming, network protocols, application layer to physical layer.

**Why it matters:** You use HTTP every single day as a developer. Understanding what happens when a browser makes a request — from DNS resolution to TCP handshake to HTTP header parsing — makes you dramatically better at building web services, debugging network issues, and designing APIs. Any backend or distributed systems work requires this foundation.

**Industry relevance:** Essential for backend, web, and distributed systems work.

---

### CMPUT 304 — Algorithms II

**What it is:** NP-completeness, reductions, approximation algorithms, randomized algorithms, more advanced graph theory.

**Why it matters:** Less directly useful for coding interviews than 204, but builds important intuition for why some problems are hard and how to approach them. Understanding NP-completeness helps you recognize when to reach for heuristics instead of exact algorithms. Respected by interviewers at senior levels.

**Industry relevance:** Medium-low for interviews, medium-high for senior engineering thinking.

---

## Specialized and Career-Path Specific Courses

These are where you differentiate yourself. Pick based on where you want to go.

### CMPUT 403 — Algorithmics in Competitive Programming

The best interview prep course at UofA. Covers exact patterns that appear in technical interviews: segment trees, binary search tricks, graph algorithms, string algorithms, DP optimization techniques. If you're applying to competitive companies, take this. See the [Hidden Gems guide](hidden-gems.md) for more detail.

### CMPUT 401 / 404 — Software Product Design / Web-Based Information Systems

Real project experience with external clients (401) and comprehensive web development (404). CMPUT 404 is excellent for web and backend careers — you build real systems.

### CMPUT 365 / 466 / 467 — Reinforcement Learning and Machine Learning

World-class instructors. Richard Sutton literally wrote the textbook on reinforcement learning (Sutton & Barto). If you want an ML career, these courses at UofA are a genuine privilege. See the career path section below.

### CMPUT 391 — Advanced Database Management Systems

Goes beyond 291: query optimization, transaction management, distributed databases. Extremely valuable for data engineering and backend roles. Most people stop at 291 — that's a mistake if you're going into data-heavy work.

### CMPUT 382 — GPU Programming and Architecture

CUDA, parallel computing, GPU architecture. Rare and increasingly valuable. Most CS graduates cannot do GPU programming. This opens doors in ML infrastructure, game dev, scientific computing. Hard but worth it.

### CMPUT 415 — Compiler Design

How compilers turn source code into machine code: lexing, parsing, semantic analysis, code generation, optimization. Deep systems understanding. Respected by senior engineers. Relevant for language tooling, developer tools companies, and anyone who wants to understand the full stack.

### CMPUT 481 — Parallel and Distributed Systems

Multi-threading, distributed computing, concurrency patterns, CAP theorem territory. Directly relevant to backend engineering at scale.

### CMPUT 261 — Introduction to Artificial Intelligence

Good survey course covering search, constraint satisfaction, probabilistic reasoning, basic ML. Worth taking as an overview before specializing.

### CMPUT 302 — Human Computer Interaction

Important if you care about product, UX, or user research. Undervalued by pure engineers but essential if you end up in product-facing roles.

---

## Career Path Ratings

Use these as starting points, not rigid rules. A backend engineer who has done some ML courses is more valuable than one who hasn't.

### Backend Engineering

| Course | Rating | Why |
|--------|--------|-----|
| CMPUT 204 | ★★★★★ | Interview prep, algorithms |
| CMPUT 291 | ★★★★★ | Databases are everywhere |
| CMPUT 313 | ★★★★ | Networks, HTTP, APIs |
| CMPUT 379 | ★★★★ | OS fundamentals, processes/threads |
| CMPUT 404 | ★★★★ | Web/backend real projects |
| CMPUT 391 | ★★★★ | Advanced databases, query optimization |
| CMPUT 301 | ★★★ | Team workflow, design patterns |

### ML / AI

| Course | Rating | Why |
|--------|--------|-----|
| CMPUT 365 | ★★★★★ | RL with Sutton — take it |
| CMPUT 466 | ★★★★★ | Core ML course |
| CMPUT 267 | ★★★★ | ML foundations |
| CMPUT 204 | ★★★★ | Algorithms still matter |
| CMPUT 461 | ★★★★ | NLP |
| CMPUT 463 | ★★★ | Probabilistic models |

### Systems / Infrastructure

| Course | Rating | Why |
|--------|--------|-----|
| CMPUT 229 | ★★★★★ | Computer architecture, essential |
| CMPUT 379 | ★★★★★ | OS, the foundation of systems |
| CMPUT 313 | ★★★★ | Networks |
| CMPUT 382 | ★★★★ | GPU programming, rare skill |
| CMPUT 481 | ★★★★ | Distributed systems |
| CMPUT 415 | ★★★ | Compilers, full stack understanding |

### Web / Full-Stack

| Course | Rating | Why |
|--------|--------|-----|
| CMPUT 291 | ★★★★★ | Databases |
| CMPUT 404 | ★★★★★ | Web systems, real projects |
| CMPUT 313 | ★★★★ | HTTP, networking |
| CMPUT 301 | ★★★ | Software engineering process |

### Security

| Course | Rating | Why |
|--------|--------|-----|
| CMPUT 229 | ★★★★ | Architecture, memory exploits |
| CMPUT 331 | ★★★★ | Security fundamentals |
| CMPUT 333 | ★★★★ | Applied cryptography |
| CMPUT 313 | ★★★★ | Network security |
| CMPUT 379 | ★★★★ | OS security, privilege escalation |

### Game Development

| Course | Rating | Why |
|--------|--------|-----|
| CMPUT 350 | ★★★★ | Game programming |
| CMPUT 411 | ★★★★ | Computer graphics |
| CMPUT 382 | ★★★★ | GPU programming |
| CMPUT 250 | ★★★ | Game design fundamentals |
| CMPUT 256 | ★★★ | Digital audio |

---

## Practical Advice

**On 204:** Do LeetCode problems alongside the course. Don't wait until interview season — the material fades fast if you don't reinforce it with practice. Keep a notes doc of patterns. Revisit before every application season.

**On 291:** Actually learn SQL. Use it. Build a small side project with a database. The students who struggle with database questions in interviews are the ones who memorized SQL for the exam and then forgot it.

**On 301:** The group project is the point. Learn to use git properly, write documentation, and give code reviews. These habits will make you stand out immediately in your first internship.

**On course load:** Don't take 204, 272, 229, and 201 all in the same semester unless you're sure you can handle it. These courses reinforce each other but are also each demanding. Talk to upper-year students about scheduling.

**On GPA vs learning:** A 3.5 GPA with solid interview skills beats a 4.0 GPA with no practical knowledge. But a 4.0 with skills is better than both. Take hard courses. Don't optimize purely for grades.
