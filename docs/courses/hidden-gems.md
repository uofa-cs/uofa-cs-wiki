# Hidden Gems: UofA CS Courses Most People Skip (But Shouldn't)

The CS program has a few courses that almost nobody talks about but that are genuinely excellent, either for interview prep, for career differentiation, or just for becoming a better engineer. This is the list of courses that upper-year students and recent grads consistently say they wish they had taken, or are glad they did when no one told them to.

---

## CMPUT 403: Algorithmics in Competitive Programming

Note: CMPUT 303 (Algorithmics in Practice) is a separate course, and **you can't get credit for both 303 and 403** ([CMPUT 403](https://apps.ualberta.ca/catalogue/course/cmput/403)). Pick one.

**Why almost nobody takes it:** It sounds intimidating. "Competitive programming" makes people think it's for math olympiad types who live and breathe algorithms. It's not. It's a structured course that teaches exactly the patterns that show up in technical interviews.

**What students actually say:** Reddit reviews of 403 are consistently positive. The format (weekly problem sets on Kattis) is uncomfortable at first and then deeply satisfying for students who stick with it.

**Why you should take it:** This is the best interview prep course at UofA, and most people don't know it exists. The curriculum covers:

Even though it is heavy on weekly problem sets, many students find it friendlier during exam season because there is no traditional midterm or final exam. CMPUT 403 still includes a project, so the workload is consistent across the term rather than concentrated into finals period.

- **Segment trees and Fenwick trees:** range query data structures that show up in medium-hard LeetCode problems
- **Binary search tricks:** not just "binary search on sorted array" but binary search on the answer, on the search space, applied to non-obvious problems
- **Advanced graph algorithms:** shortest paths, minimum spanning trees, topological sort, SCC (strongly connected components), network flow
- **String algorithms:** KMP, suffix arrays, string hashing. These are consistently tested at companies like Google and Meta
- **Dynamic programming optimization:** divide and conquer DP, convex hull trick, bitmask DP
- **Geometry:** computational geometry problems, convex hull

If you're applying to Google, Meta, Microsoft, Shopify, or any company that does algorithm-heavy interviews (which is most of them for new grad roles), the patterns in this course are exactly what you need to know. LeetCode by itself is unstructured. This course gives you the mental framework to actually recognize and solve novel problems.

**When to take it:** Third year is ideal. The catalogue requires 201 (or 275), 204, and any 300-level CMPUT course, so it can't come before your first 300-level course. Taking it in third year means you can reinforce and apply the material during your most active internship application period.

**Format:** Mostly problem sets. You solve algorithmic problems under time pressure. It's uncomfortable at first and then deeply satisfying. This is what top engineers do for fun.

---

## CMPUT 382: Introduction to GPU Programming (Not Recently Offered)

**Availability first:** the catalogue currently shows no scheduled offerings of CMPUT 382, and its most recent listed term is Fall 2024 ([CMPUT 382](https://apps.ualberta.ca/catalogue/course/cmput/382)). It's on this list because it's worth grabbing if it comes back, not because you can count on it.

**Why almost nobody takes it:** It has "GPU" in the name and people assume it's only for game devs or researchers.

**What students actually say:** The few Reddit discussions that mention 382 describe it as "not harder than any other 300-level CMPUT." The course has had disorganized offerings in the past, with setup friction around toolchains, but nothing unusually brutal.

**Why you'd take it:** The ability to write GPU code is rare. Per the catalogue, the course covers GPU hardware architecture, algorithmic design, programming languages such as CUDA and OpenCL, and principles of programming GPUs for high performance. That's directly useful in ML infrastructure, graphics and game development, scientific computing, and high-performance computing.

**Prerequisites:** 201 (or 275) and 229 (or an equivalent ECE/EE architecture course). You need to understand what the hardware is doing to write efficient GPU code.

If 382 isn't running, CMPUT 481 (Parallel and Distributed Systems) is the closest alternative for parallel programming (it ran most recently in Winter 2026; check the catalogue for upcoming terms).

---

## CMPUT 415: Compiler Design

**Why almost nobody takes it:** It sounds academic. "Nobody writes compilers in industry," people say. They're wrong, but more importantly, they're missing why this course matters.

**What students actually say:** This is one of the most universally respected "hard" courses in the program. One Reddit review: *"Without a doubt the most work I've had to do for a CMPUT course. Also the course that I learned the most in; in retrospect, I would still take it again."*

The project is a full LLVM-based compiler for a defunct IBM language with a 40-page spec. The spec glosses over features. Most groups don't fully implement everything. The workload "never lets up; as soon as an assignment is done, start the next one immediately."

Before taking it: check the course outline for the implementation language and toolchain, and look up ANTLR (parser generator) and LLVM basics. 415 requires 229 and a 300-level CMPUT course, so it comes late; don't pair it with another heavy course like 466.

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

---

## CMPUT 313: Computer Networks

**Why almost nobody takes it:** It's perceived as boring. Networking? Layers? Who cares?

**What students actually say:** The content itself gets positive retrospective reviews from students who went on to backend or infrastructure work. One Reddit comment captured the dual nature well: "313 is drier than the desert. Not much relevancy to modern hands-on networking that you'd see for most CS work unless you want to get deep into network protocols." But another counter-perspective: the student who took it and later debugged production network issues reported wishing they'd paid more attention.

**Planning note:** 313 requires 201 and 204 (or 275) and an intro stats course, and lists CMPUT 379 as a corequisite ([CMPUT 313](https://apps.ualberta.ca/catalogue/course/cmput/313)), so you'll take it alongside or after operating systems.

**Why you should take it:** You use HTTP every single day. Every API call your code makes, every web page your browser loads, every database query that goes over a network; all of it runs on the protocols this course covers. After taking it, you know:

- What actually happens when you type a URL and press enter (DNS resolution, TCP handshake, HTTP request/response, TLS if HTTPS)
- Why TCP vs UDP matters and when to use each
- What happens at the socket level when two programs communicate
- How routers forward packets, how routing tables work, what BGP is
- Why CDNs exist and how they work
- What the hell "network latency" and "bandwidth" actually mean vs how people misuse these terms

**For backend and distributed systems roles specifically:** This is not optional knowledge. You will debug network issues. You will design systems that communicate over the network. You will be asked in interviews about what happens when a client makes a request. This course gives you the vocabulary and mental models to answer those questions properly.

It's also just deeply satisfying to understand infrastructure you've been using for years. Most developers treat the network as a black box. Don't be most developers.

---

## CMPUT 391: Database Management Systems (Not Offered Since Winter 2022)

**Availability first:** CMPUT 391 is still in the calendar, but the catalogue shows no scheduled offerings and its most recent listed term is Winter 2022 ([CMPUT 391](https://apps.ualberta.ca/catalogue/course/cmput/391)). Don't build a plan around it.

**Why it would be worth it:** CMPUT 291 teaches you to use databases; 391 covers how they work: compilation, execution, and optimization of SQL queries, concurrent transactions, indexing, distributed and parallel databases, and NoSQL/cloud systems. If it ever comes back, take it.

**What to do instead:** Build on 291 with CMPUT 404 (Web Applications and Architecture), side projects with a real database, and reading on query planners and transaction isolation. When you're debugging a slow query in production at 2am, you want to know what an execution plan is.

---

## CMPUT 481: Parallel and Distributed Systems

**Why almost nobody takes it:** It's listed late and people have usually filled their CMPUT elective slots with other things. Also, "parallel" sounds like a research topic. It requires CMPUT 379.

**Why you should take it:** Modern software runs on multiple cores and multiple machines. Understanding how to write correct concurrent programs is a critical skill:

- **Multi-threading:** threads, synchronization primitives, race conditions, deadlocks, lock-free data structures
- **Distributed computing patterns:** how to design systems that span multiple machines, handle partial failures, and maintain consistency
- **Concurrency models:** shared memory vs message passing, actor model
- **Real distributed systems:** MapReduce, consensus algorithms (Paxos, Raft), distributed file systems

**For backend engineering at scale:** Every company of any size runs distributed systems. Understanding why Kafka, Redis, and databases with replication are architected the way they are, and being able to explain it, is the mark of a senior-thinking engineer at a junior or intermediate level. This course gives you that foundation.

---

## CMPUT 365: Introduction to Reinforcement Learning

**Who takes it:** If you're in the AI Option (Major or Honors), CMPUT 365 is **required**, so it's not hidden for you. For everyone else, it's an elective that's easy to overlook because students think RL is exotic and only for researchers. Prerequisites: 175 (or 275) and one of CMPUT 267, CMPUT 466, or STAT 265 ([CMPUT 365](https://apps.ualberta.ca/catalogue/course/cmput/365)).

**Why you should take it:** Richard Sutton and Andrew Barto wrote *Reinforcement Learning: An Introduction*, which is THE textbook in the field, and it's available free online. UofA is one of the major centres for RL research. Taking RL here is an opportunity most non-AI students walk right past.

Even if you never write an RL algorithm in your career:

- The framework for thinking about sequential decision-making under uncertainty is broadly applicable
- The mathematical foundations (Markov decision processes, Bellman equations, value functions) are used in robotics, finance (algorithmic trading), game AI, and recommendation systems
- RL is increasingly integrated with LLMs (RLHF, Reinforcement Learning from Human Feedback, is how ChatGPT was fine-tuned)

If you're heading into ML in any form, CMPUT 267 (Machine Learning I), then 365 and 466 or 467, is one of the strongest academic preparation sequences you can do.

---

## Non-CMPUT Hidden Gems

These are outside the CS department but genuinely valuable.

### STAT 265: Probability and Statistics I

Not technically an elective: it's one of the three options (with STAT 151 and 235) for the intro stats requirement in every CS path. But most students default to STAT 151 without thinking about it. 265 is the more rigorous probability route, it's directly useful for ML and systems work, and it's one of the courses that unlocks CMPUT 365. It has a calculus corequisite (MATH 209, 214, or 217), so plan for that.

### MATH 225: Linear Algebra II

The follow-up to MATH 125: vector spaces, inner product spaces, Gram-Schmidt, QR factorization and least squares, diagonalization, quadratic forms ([MATH catalogue](https://apps.ualberta.ca/catalogue/course/math)). If you're heading into ML or graphics, this is the linear algebra you'll actually lean on, and it's a prerequisite option for CMPUT 340 (Introduction to Numerical Methods).

If you want the abstract algebra behind cryptography instead, look at MATH 228 (Algebra: Introduction to Ring Theory), which covers modular arithmetic, finite fields, and applications like public-key encryption.

### PHIL 220: Symbolic Logic II

Predicate logic with identity, natural deduction, mathematical induction, elementary modal logic, formal axiomatic systems ([PHIL catalogue](https://apps.ualberta.ca/catalogue/course/phil)). This overlaps with programming language theory, type systems, and formal verification. If you find yourself drawn to the theoretical side of CS, it's worth taking. Requires PHIL 120.

### ECE 340: Signals and Systems

**ECE 340 is Discrete Time Signals and Systems**, and its prerequisite is ECE 240 (or E E 238), an Engineering course, so check whether you can realistically get in before planning around it. If you ever work in audio processing, communications systems, digital signal processing, radio frequency (RF), or certain areas of ML (especially time-series or audio ML), this course is foundational. Sampling and aliasing, the Z-transform, discrete-time and discrete Fourier transforms, digital filter design. Most CS students never touch this. The ones who do have a rare skill.

### GEOPH 210: Structure, Dynamics and Evolution of the Earth and Planetary Interiors (Mostly Kidding, Somewhat Serious)

It's not a seismology course as such, but it covers Earth's interior structure from seismology, gravity, and magnetism, along with plate tectonics, earthquakes, and planetary bodies. And seismology is genuinely a data-heavy field. Seismic data processing involves signal processing, large datasets, pattern recognition, and time-series analysis. If you want a bizarre and interesting dataset to work with for personal projects, or if you're curious about scientific computing, a geophysics course is a left-field choice that has produced a few interesting data science portfolios. Edmonton is an energy hub and oil and gas companies hire data scientists. This is the "mostly kidding" entry, but the underlying point is real: niche domain knowledge plus CS skills is a powerful combination in unexpected industries.

---

## The Common Thread

Every course on this list has the same profile: not required by default, not widely advertised, but meaningful in a way that shows up in your work (and in interviews) years after you've taken it. The students who graduate with the strongest reputations (who get calls back from FAANG, who get hired at their dream startups) are usually the ones who took the hard optional courses and actually learned from them.

Most people take the path of least resistance. The courses on this list are the road less taken. Take them.
