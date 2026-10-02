# Curriculum Map

What the degree teaches, and what it doesn't. Course descriptions come from the [course catalogue](https://apps.ualberta.ca/catalogue/course/cmput); languages and tools come from public course sites for the term named. Instructors change things, so check your section's outline.

Remember that the plain Major only requires 174/175 (or 274/275), 204, 272, and two of 201/229/291; everything else on this page is an elective unless you're in an option. See the [Program Overview](../getting-started/program-overview.md) for each path.

---

## Courses, Topics, and Tools

| Course | Main topics | Languages and tools |
|---|---|---|
| [174](https://apps.ualberta.ca/catalogue/course/cmput/174) / [175](https://apps.ualberta.ca/catalogue/course/cmput/175) | Problem solving, control flow, recursion, testing; then objects, ADTs, searching and sorting | Python ([dept comparison](https://www.ualberta.ca/en/computing-science/undergraduate-studies/course-directory/compare-introductory-courses.html)) |
| [274](https://apps.ualberta.ca/catalogue/course/cmput/274) / [275](https://apps.ualberta.ca/catalogue/course/cmput/275) | Accelerated 174/175 plus graph algorithms, DP; studio format | Python on Linux (274); C++ (275); Arduino ([dept comparison](https://www.ualberta.ca/en/computing-science/undergraduate-studies/course-directory/compare-introductory-courses.html)) |
| [201](https://apps.ualberta.ca/catalogue/course/cmput/201) | Professional programming practice, ADTs, Unix tooling | C99, gcc, gdb, valgrind, Makefiles, shell scripts ([Fall 2025 site](https://webdocs.cs.ualberta.ca/~ghlin/cmput201.php)) |
| [204](https://apps.ualberta.ca/catalogue/course/cmput/204) / [304](https://apps.ualberta.ca/catalogue/course/cmput/304) | Algorithm design and analysis; 304 adds NP-completeness and heuristics | Mostly pen and paper |
| [229](https://apps.ualberta.ca/catalogue/course/cmput/229) | Number representation, ISA, assembly, pipelining, memory hierarchy | RISC-V assembly in RARS ([Fall 2026 labs](https://cmput229.github.io/229-labs-RISCV/)) |
| [267](https://apps.ualberta.ca/catalogue/course/cmput/267) | Math of ML: estimation, generalization, regression, classification | Python in Google Colab ([Fall 2025 site](https://vladtkachuk4.github.io/machinelearning1/)) |
| [272](https://apps.ualberta.ca/catalogue/course/cmput/272) | Sets, logic, induction, program correctness | Proofs |
| [291](https://apps.ualberta.ca/catalogue/course/cmput/291) | ER and relational models, SQL, storage and access methods | SQL; Python for the project (catalogue) |
| [301](https://apps.ualberta.ca/catalogue/course/cmput/301) | OO design, UML, design patterns, revision control, unit testing, refactoring | Java/Android team project ([Fall 2026 outline](https://ualberta-cmput301.github.io/general/outline.html)) |
| [303](https://apps.ualberta.ca/catalogue/course/cmput/303) / [403](https://apps.ualberta.ca/catalogue/course/cmput/403) | Contest-style problem solving, weekly problem sets | Kattis; lectures in C++, submit in any Kattis language ([instructor info page](https://friggstad.github.io/cmput403_info.html)) |
| [313](https://apps.ualberta.ca/catalogue/course/cmput/313) | Error/flow control, MAC protocols, routing, congestion control, internet architecture | Not listed publicly |
| [325](https://apps.ualberta.ca/catalogue/course/cmput/325) | Functional and logic programming, lambda calculus | Lisp, Prolog ([dept page](https://www.ualberta.ca/en/computing-science/undergraduate-studies/course-directory/courses/non-procedural-programming-language.html)) |
| [333](https://apps.ualberta.ca/catalogue/course/cmput/333) | Cryptography, authentication protocols, network vulnerabilities | Not listed publicly |
| [350](https://apps.ualberta.ca/catalogue/course/cmput/350) | 2D game engines, memory management, ECS | C++, STL (catalogue) |
| [365](https://apps.ualberta.ca/catalogue/course/cmput/365) | Bandits, MDPs, RL, planning, function approximation | Uses the UofA RL MOOC (catalogue) |
| [379](https://apps.ualberta.ca/catalogue/course/cmput/379) | Processes, synchronization, deadlock, virtual memory, scheduling, file systems | Not listed publicly |
| [393](https://apps.ualberta.ca/catalogue/course/cmput/393) | Scaling data science and ML across machines; big project | New: first listed offering is Winter 2027 |
| [401](https://apps.ualberta.ca/catalogue/course/cmput/401) | Software process and product management; group project | Varies by project |
| [402](https://apps.ualberta.ca/catalogue/course/cmput/402) | Unit to integration testing, reviews, continuous integration, quality tools | Version control and CI services ([dept page](https://www.ualberta.ca/en/computing-science/undergraduate-studies/course-directory/courses/software-quality.html)) |
| [404](https://apps.ualberta.ca/catalogue/course/cmput/404) | Web architecture, protocols, web services, serialization | Django (or Flask), HTML/CSS/JS, Postgres on Heroku ([project spec](https://uofa-cmput404.github.io/general/project.html)) |
| [415](https://apps.ualberta.ca/catalogue/course/cmput/415) | Lexing, parsing, type checking, flow analysis, code generation, optimization | C++, ANTLR, MLIR/LLVM, CMake ([course templates](https://github.com/cmput415)) |
| [466](https://apps.ualberta.ca/catalogue/course/cmput/466) / [467](https://apps.ualberta.ca/catalogue/course/cmput/467) | 466: one-course ML survey. 467: neural nets, generative models, non-iid data | Not listed publicly |
| [481](https://apps.ualberta.ca/catalogue/course/cmput/481) | Thread and data-parallel programming, clusters, performance | Not in the 2026-27 schedule; last offered Winter 2026 |

**Not recently offered** (catalogue term history): [391](https://apps.ualberta.ca/catalogue/course/cmput/391) Database Management Systems (last Winter 2022), [382](https://apps.ualberta.ca/catalogue/course/cmput/382) GPU Programming (last Fall 2024), [411](https://apps.ualberta.ca/catalogue/course/cmput/411) Computer Graphics (last Winter 2025). Don't plan around them.

---

## By Topic

| Topic | Where it's taught | Required? |
|---|---|---|
| Git and version control | 301 (revision control), 402 | Only in the Software Practice Option |
| Testing | Introduced in 174; unit tests in 301; 402 goes deep | 402 only in the Software Practice Option |
| CI/CD | 402 | Only in the Software Practice Option |
| Web backends | 404 (Django/Flask, REST-style node-to-node API) | No |
| Frontend frameworks (React etc.) | Nowhere; 404's spec says it won't cover them | No |
| Databases | 291 (SQL); 393 (scaling) | 291: required in Honors and the Software Practice Option; one of the 201/229/291 picks in the Major |
| Systems and OS | 201, 229, 379, 429 | 201 and 229 required in Honors; 379 only in the Software Practice Option |
| Networking | 313 | No |
| Security | 331 (crypto), 333 (networked systems) | No |
| Distributed systems | 481 (parallel computing, not consensus); 404's project is a distributed social network; 393 | No |
| ML and AI | 261, 267, 365, 366, 466/467, 469, plus 328, 461 | Only in the AI Options |
| Mobile | 301 (Android) | Only in the Software Practice Option |
| Cloud, containers, infrastructure | Nowhere (404 deploys to Heroku, but it isn't taught as a topic) | No |
| System design at scale | Nowhere | No |

---

## Filling the Gaps

One resource per gap. Pick the one that matches what you want to do.

| Gap | Resource |
|---|---|
| System design and data systems | [*Designing Data-Intensive Applications*](https://dataintensive.net) by Martin Kleppmann |
| Distributed systems theory (consensus, replication) | [MIT 6.5840 Distributed Systems](https://pdos.csail.mit.edu/6.824/) (free lectures and Go labs) |
| Frontend and full-stack JavaScript | [Full Stack Open](https://fullstackopen.com/en/) (React, Node, TypeScript) |
| Containers | [Docker's getting-started guide](https://docs.docker.com/get-started/) |
| CI/CD without taking 402 | [GitHub Actions docs](https://docs.github.com/en/actions) |
| Running systems in production | [Google's *Site Reliability Engineering*](https://sre.google/sre-book/table-of-contents/) (free online) |
| Web application security | [OWASP Top 10](https://owasp.org/www-project-top-ten/) |

Course-by-course reading lists are on [Learning Resources](../resources/learning-resources.md). Setup and tooling are on [Tools and Setup](tools-and-setup.md).

---

## AI Coding Agents

AI coding agents are now standard in industry, and course policies vary: 301's Fall 2026 outline allows them but requires you to cite and disclose their use ([outline](https://ualberta-cmput301.github.io/general/outline.html)). See [Learning and Working With AI](learning-with-ai.md) for UofA's rules, what each course allows, and why it matters for in-person assessments.

*Last verified: October 2026.*
