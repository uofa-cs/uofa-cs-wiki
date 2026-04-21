# Learning Resources for UofA CS Students

Your degree teaches you computer science. What you do outside of class determines how good you get at software engineering. The gap between someone who only does coursework and someone who reads widely, builds things, and engages with the broader field compounds dramatically over four years.

This page collects the best resources across books, courses, YouTube, practice platforms, documentation, and newsletters. Not everything, just the best things.

---

## Essential Books

Books are slow and that's the point. They force depth in a way that YouTube and blog posts don't.

**Introduction to Algorithms (CLRS)** by Cormen, Leiserson, Rivest, Stein

The algorithm bible. Referenced constantly in CMPUT 204 and upper-year courses. Dense, rigorous, and comprehensive. Don't try to read it cover to cover; use it as a reference when you encounter a topic you need to understand deeply. The pseudocode is language-agnostic, which teaches you to think algorithmically rather than syntactically. Worth owning.

**Designing Data-Intensive Applications** by Martin Kleppmann

The best book on modern backend engineering and distributed systems. Covers databases, replication, consistency models, stream processing, and more, with the practical nuance that textbooks miss. If you want to work in backend engineering, data engineering, or systems at any level of seriority, read this book. It's accessible without being shallow. One of the most important CS books of the last decade.

**Operating Systems: Three Easy Pieces (OSTEP)** by Remzi & Andrea Arpaci-Dusseau

Free online at ostep.org. Widely regarded as the best OS textbook available, better than most that universities actually use. Covers virtualization, concurrency, and persistence in a way that's engaging and clear. An excellent supplement to CMPUT 379. The chapters are short and self-contained, so it's easy to read alongside coursework.

**Clean Code** by Robert C. Martin

Opinionated and occasionally dated, but foundational. Teaches you to think about code readability, naming, function size, and maintainability. Some of the advice is too dogmatic; take it as a starting point for thinking rather than a rulebook. The core insight (code is read far more than it's written, so optimize for reading) is genuinely important and worth internalizing early.

**The Pragmatic Programmer** by Dave Thomas & Andy Hunt

Short, readable, and full of practical wisdom about software development as a craft and career. Doesn't focus on a specific language or framework; it's about how to think about the practice of programming. Read this in first or second year. It will change how you approach your degree and your projects.

**Computer Networking: A Top-Down Approach** by Kurose & Ross

The standard networking textbook and a genuinely good one. Very readable compared to most textbooks in this space. Excellent supplement to CMPUT 313. If you want to understand HTTP, TCP/IP, DNS, and how the internet actually works, this is the clearest explanation available in book form.

**Structure and Interpretation of Computer Programs (SICP)** by Abelson & Sussman

Free online. The classic MIT intro CS text, now used at far fewer universities than it once was. Written in Scheme (a Lisp dialect). Reading it will expand how you think about computation, abstraction, and programming language design in ways that courses usually don't. Not required, but respected. If you work through even the first three chapters, you'll think differently about code.

**Reinforcement Learning: An Introduction** by Sutton & Barto

Free online at incompleteideas.net. If you're at UofA studying ML or AI, you are studying at one of the world's leading RL research institutions. Richard Sutton is faculty here. Read the textbook by your professor. This is one of the few situations where the definitive book on a subject is authored by someone down the hall from you.

---

## Online Courses

**MIT OpenCourseWare (ocw.mit.edu)**

Free courses from MIT with full lecture notes, problem sets, and exams. The standouts:
- **6.006 Introduction to Algorithms:** excellent parallel to CMPUT 204, rigorous and well-taught
- **6.824 Distributed Systems:** graduate-level, lab assignments build real distributed systems. Challenging but formative if you want systems work.
- **6.004 Computation Structures:** computer architecture from the ground up

**Stanford CS Courses on YouTube**

- **CS231n** (Convolutional Neural Networks / Computer Vision): lecture recordings available. Dense but thorough.
- **CS224n** (NLP with Deep Learning): the best NLP course available online
- **CS229** (Machine Learning by Andrew Ng): the foundational ML course that launched a thousand ML careers. More theoretical than Coursera's ML Specialization.

**fast.ai**

Practical deep learning for coders, taught bottom-up (start building things, then learn the theory). Free. The opposite pedagogical approach from Andrew Ng's courses. Many people find it more motivating because you're building working neural nets from day one. Great starting point if you want to get into ML practically rather than theoretically.

**The Odin Project (theodinproject.com)**

Free, open source, project-based web development curriculum. Goes from HTML/CSS through JavaScript, React, Node.js, and databases. One of the best free resources for becoming a competent full-stack web developer. More comprehensive and better structured than most paid bootcamps.

**CS50 (Harvard, via edX)**

The best intro CS course in the world for people who want to truly understand fundamentals. Covers C, algorithms, data structures, web basics, SQL. Free to audit. If you feel shaky on any of these fundamentals from CMPUT 174/175, CS50 is an excellent reset.

---

## YouTube Channels

**Fireship**

Short (5-15 minute), high-information-density tech explainers. Best for quickly understanding what a technology is and why it exists before you decide whether to dig deeper. The "in 100 seconds" series is excellent. Watch regularly to stay aware of the ecosystem.

**ThePrimeagen**

Experienced staff-level developer with strong opinions about programming, tooling (heavy Neovim user), and the industry. More entertainment than tutorial, but honest about what matters in real software work. Good for perspective on what senior engineers actually think about.

**NeetCode**

The best LeetCode explanation channel on YouTube. Covers every major problem pattern with clear, systematic explanations. Organized by topic (trees, graphs, dynamic programming, etc.). If you're doing interview prep, this channel is essential. NeetCode's 150 problem list is one of the most efficient structured study plans available.

**MIT OpenCourseWare Channel**

Full lecture recordings from MIT courses. Use to supplement your UofA courses or explore topics your degree doesn't cover in depth.

**Computerphile**

Computer science concepts explained accessibly for a general audience. Covers everything from Turing machines to SQL injection to floating point precision. Great for understanding the "why" behind concepts that courses teach without much context.

**3Blue1Brown**

Mathematical concepts with stunning visualizations. The "Essence of Linear Algebra" series is the best introduction to linear algebra intuition available anywhere; watch it alongside or before your linear algebra course. The "Neural Networks" series builds genuine intuition for how deep learning works. Highly recommended.

**ByteByteGo**

System design concepts explained clearly, with excellent diagrams. Run by the author of the popular system design interview book. Subscribe to their newsletter too. Essential viewing once you're preparing for intermediate to senior-level interviews.

**Hussein Nasser**

Backend engineering deep dives: databases, networking protocols, proxies, Postgres internals, WebSockets. More technical and detailed than most channels. Good for going deeper once you understand the basics.

---

## Practice Platforms

**LeetCode**

The industry standard for technical interview preparation. Use it strategically: work through problems by topic (arrays/hashing, two pointers, sliding window, trees, graphs, dynamic programming) rather than randomly. Doing 50-100 well-understood problems beats doing 300 problems you barely remember. See the interview prep guide for a more detailed approach.

**Codeforces**

Competitive programming platform with regular contests. Better than LeetCode for developing pure algorithmic thinking; the problems require more creativity and less pattern-matching. If you want to genuinely improve your problem-solving ability, Codeforces contests are more demanding and rewarding than LeetCode grind. Pairs well with CMPUT 204.

**Advent of Code (adventofcode.com)**

Annual programming challenge every December: 25 days of two-part puzzles that increase in difficulty. Excellent for learning a new language (pick something unfamiliar and solve puzzles in it) or sharpening skills in one you know. The community discussions after each puzzle open are excellent for seeing different approaches. Past years are available year-round.

**HackerRank**

Some companies use HackerRank for early-stage screening assessments. The platform's question format and environment are worth practicing in before you encounter it in an actual application. Less useful than LeetCode for general skill building.

**Project Euler (projecteuler.net)**

Math-heavy programming problems that require number theory, combinatorics, and mathematical thinking. Good for a different kind of problem-solving than algorithmic interview prep. Respected in certain technical communities. Optional, but interesting if you have a mathematical bent.

**Exercism (exercism.org)**

Language-specific exercise tracks with optional human mentorship. Excellent for learning a new language properly; exercises are idiomatic and the feedback from mentors teaches you language-specific best practices. Better for language learning than LeetCode, which tends to reward the same patterns regardless of language.

---

## Documentation and References

**MDN Web Docs (developer.mozilla.org)**

The authoritative reference for HTML, CSS, JavaScript, and web APIs. Run by Mozilla. If you're doing anything web-related, bookmark this. Stack Overflow answers go stale; MDN stays current.

**Python Official Docs (docs.python.org)**

Comprehensive, accurate, and often underused. The tutorial section is genuinely good for beginners. The library reference is the authoritative source for everything in the standard library, more reliable than any third-party tutorial.

**DevDocs (devdocs.io)**

Unified documentation browser for dozens of languages and frameworks. Works offline. Useful for having multiple reference docs open simultaneously without 15 browser tabs.

**Reading Open Source Code**

Underrated as a learning method. Find a library you use, read its source code. Understanding how something you rely on is actually implemented builds your sense for good code structure, design patterns, and tradeoffs. Start with small, well-maintained libraries in a language you're comfortable in.

---

## Newsletters

**TLDR Newsletter**

Daily tech news digest in 5-minute reading time. Covers developer tools, AI, startups, and the industry. Consistently useful for staying aware of what's happening without the noise of social media. Free.

**Bytes.dev**

JavaScript and web ecosystem news, written with humor. If you're doing any frontend or Node work, this keeps you current on the ecosystem. Well-curated and entertaining.

**ByteByteGo Newsletter**

Weekly system design deep dives from the ByteByteGo team. Goes well with the YouTube channel. Good for people preparing for mid-to-senior level interviews or just wanting to understand how large systems are built.

**Morning Brew**

Broader tech and business news for context on the industry you're entering. Less technical, more business-focused. Useful for understanding the companies you're applying to and the broader landscape.

---

## A Note on How to Use These Resources

The mistake students make is collecting resources and never using them. Subscribe to fewer things, go deeper on what you actually use.

Pick one book and read it over a semester. Pick one course and finish it. Pick one platform and practice on it consistently. The students who improve fastest are not the ones who have the most bookmarks; they're the ones who ship things, read things end-to-end, and practice consistently over time.

Your courses give you the curriculum. These resources let you go deeper on what interests you, fill gaps your courses don't cover, and stay connected to what's actually happening in the industry. Use them in service of building things, not as a substitute for it.
