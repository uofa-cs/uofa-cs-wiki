# Course Reviews: Real Student Perspectives

These reviews combine student discussions and first-hand contributions from UofA students. Difficulty and workload ratings reflect student consensus. "Industry relevance" reflects how directly the material maps to software engineering roles.

> **About instructor notes.** This wiki doesn't rank professors. Where instructors are mentioned, it's to describe how their sections have been run (notes, assessments, pacing), so you can pick the style that suits you. Instructors change every term: check who's teaching in the [course catalogue](https://apps.ualberta.ca/catalogue/course/cmput) before you register.

---

## How to Read This Page

- **Difficulty:** Easy / Medium / Hard / Brutal
- **Workload:** Light / Moderate / Heavy / Overwhelming
- **Industry relevance:** Low / Medium / High / Critical

---

## CMPUT 101: Introduction to Computing

**Difficulty:** Easy | **Workload:** Light | **Industry relevance:** Low

The gentlest introduction to programming at UofA. Designed for students with zero background. If you've already programmed in high school, this is almost certainly too easy; most students with any programming experience report going to almost no classes and still doing well.

**Student tips:**
- If you have any programming background, consider skipping straight to 174. Talk to an advisor.
- Show up for labs even if lectures seem too slow. Labs count.
- Don't pick this course expecting it to be challenging; treat it as a free GPA boost.

---

## CMPUT 174: Introduction to Computing I

**Difficulty:** Easy-Medium | **Workload:** Moderate | **Industry relevance:** Low (foundational)

First-year Python course. Variables, control flow, functions, recursion, basic data structures. The pace is manageable for students who engage consistently, but students who miss lectures and try to catch up before exams frequently struggle; programming doesn't work that way.

**Instructor notes:**
- **Osmar Zaiane:** interactive lectures with props and in-class questions. Expect frequent assessments (3-4 per week in past offerings), which keeps you on pace but adds up.
- **Joerg Sander:** works through problems with the class rather than presenting finished solutions; students without prior experience have found this approachable.

**Student tips:**
- Do your labs independently. Students who collaborate too closely or use AI on labs fail to build the actual skill and later struggle.
- If you have prior Python experience, 174 might feel slow; use the extra time to build personal projects rather than coasting.
- The jump from 174 to 175 is real. Don't let an easy 174 make you complacent.

---

## CMPUT 175: Introduction to Computing II

**Difficulty:** Medium | **Workload:** Moderate-Heavy | **Industry relevance:** Low-Medium (foundational)

Continues from 174. Object-oriented programming, more complex data structures, recursion deepened. The jump from 174 to 175 catches a lot of students by surprise.

**Student tips:**
- The OOP concepts introduced here (classes, inheritance, interfaces) will appear in every upper-year course. Don't treat this as just "more Python."
- 175 is a good place to start doing side projects in Python using what you've learned.

---

## CMPUT 274/275: Accelerated Introduction to the Foundations of Computation I & II

**Difficulty:** Hard | **Workload:** Heavy-Overwhelming | **Industry relevance:** Medium

The accelerated alternative to 174/175. Per the [catalogue](https://apps.ualberta.ca/catalogue/course/cmput/274), 274 covers procedural programming and basic algorithms in Python on Linux, and [275](https://apps.ualberta.ca/catalogue/course/cmput/275) moves to object-oriented programming in C++ with graphs, divide and conquer, and dynamic programming. Both are taught studio-style (two 3-hour blended lecture/lab sessions a week) with limited enrollment, and prior programming background is strongly recommended.

Note that you can't get credit for both 275 and 201, so 275 also covers the role 201 plays in the regular stream.

Students are divided: those with strong prior experience often found it manageable and preferred the depth; those without a strong base often found the pace brutal, with some reporting around 20 hours a week on this one course.

**Student tips:**
- Be honest about your background. If you've programmed seriously before, the accelerated stream is a good fit. Otherwise, 174/175 is the smarter play.

---

## CMPUT 201: Practical Programming Methodology

**Difficulty:** Hard-Brutal | **Workload:** Heavy | **Industry relevance:** High

The rite of passage for any UofA programmer, no matter the experience. The course focuses on C99: a walkthrough of basic syntax before delving into pointers, memory management, structs and unions, the preprocessor, implementing abstract data structures, bitwise operators and bitfields in C. 201 covers a lot more C than 275.

Alongside learning C, this will be your first encounter with GitHub. You will learn how to do Git operations individually: cloning, adding/pushing, (and if the TAs update the lab) resolving merge conflicts. You also learn debugging with gdb, and programming in vim; though most students debug with `printf` and use Remote SSH to connect to the lab machines.

The TA's—who design nearly every lab—and the professors will not hold back. Labs and In-Class Coding will require knowledge about algorithms and data structures from 175, complementing 272 and 204 as well. Linked Lists alongside sorting algorithms are required to know. Despite the low averages and the soul-crushing assignments, you will become a more resilient programmer.

**Instructor notes:**
- **Henry Tang:** thorough notes and clear lectures. Same difficulty as other sections, with a less lenient curve than Dr. Lin's.
- **Guohui Lin:** equally knowledgeable; don't judge the section by online ratings. His notes work best as a supplement after reading the textbook, though you can do well from the notes alone. Has had a lenient curve.

**Student tips:**
- Get the textbook: *C Programming: A Modern Approach* by K. King. It will teach you almost everything about C's syntax and some ADT implementations.
- Labs: Start them early, Chat-GPT will not save you, especially in the later labs. Make sure you get as much help as you can from the TAs.
- Code in the lab machines, use proper compilation flags, (and in the later labs) make sure you write your makefiles and check valgrind in order to get the best grade.
- Weekly Quizzes: Make sure you keep up with them, they're the easiest part of the course!
- In-Class Coding (ICCs): Do "Programming Projects" from the textbook for the earlier ICCs, then try and use leetcode for the later ICCs, especially for linked lists and low-level ICCs.

**Pairs well with:** 204 (sorts and some ADTs have a good cross-over). **Don't pair with:** Any other course with a heavy workload; you will have to make sacrifices.

---

## CMPUT 204: Algorithms I

**Difficulty:** Medium-Hard | **Workload:** Moderate-Heavy | **Industry relevance:** Critical

Big-O analysis, sorting, graphs, dynamic programming, greedy algorithms. This is THE interview course. Everything you will be asked in a technical interview draws from this material.

"Take it seriously. Do extra problems. Review the textbook. Revisit the material before every interview season." That's not fluff; students who get good internships consistently say 204 was where it started.

**Instructor notes:**
- **Martin Mueller:** text-heavy slides; assignments are considered fair and the course rewards steady work.
- **Zachary Friggstad:** fast-paced lectures, but he'll slow down if asked. Active on the course Discord and has solved Kattis problems live in class.

**Student tips:**
- Do practice problems beyond the assignments. 204 material is best learned by doing, not reading.
- If you plan to do competitive programming (CMPUT 403), start building those habits now.
- This course is harder than 201 in a different way; it's abstract, not mechanical. Budget time accordingly.

---

## CMPUT 229: Computer Organization and Architecture

**Difficulty:** Brutal | **Workload:** Overwhelming | **Industry relevance:** Medium

Assembly language (RISC-V, using the RARS simulator; see the [public lab repo](https://cmput229.github.io/229-labs-RISCV/)), CPU design, memory hierarchy. Consistently cited by students as the hardest course in the program: *"One time a friend asked me, 'How's life besides 229?' I quickly answered, 'There is no life besides 229.'"*

The course genuinely matters; understanding what happens at the hardware level makes you a better programmer. But the workload (weekly labs, difficult midterms) is punishing.

**Instructor notes:**
- **José Nelson Amaral:** high standards, hard labs and exams, and very energetic lectures. His recorded lectures are freely available on YouTube and students in other sections use them too.

**Student tips:**
- Whatever section you're in, Amaral's free YouTube lecture series is a widely recommended supplement.
- Pairs reasonably with 291 (databases), which has lighter workload. **Do not** take 229 with 301 and 350 in the same semester.
- The memory hierarchy concepts in 229 directly feed into 379 (Operating Systems); don't treat it as disconnected content.

---

## CMPUT 267: Basics of Machine Learning

**Difficulty:** Hard | **Workload:** Heavy | **Industry relevance:** High

Statistics-heavy intro to ML: linear algebra, probability, gradient descent, regression, classification. This is not a "here's how to use scikit-learn" course. It's mathematical foundations. Uses Julia as the programming language.

One student summarized it well: "It's basically applied stats. That's what a lot of ML is." Another: "My roommate took 267 and it was TOUGH."

**Student tips:**
- Strong stats and linear algebra background (MATH 125, STAT 151/252) helps a lot.
- Don't take this with 379 or other heavy courses. One student who took 379, 401, and 267 in the same semester was specifically advised to drop 267.
- If you want ML but aren't math-comfortable yet, consider 366 (intro to reinforcement learning) first; it's considered lighter and more conceptually accessible.

---

## CMPUT 272: Formal Systems and Logic

**Difficulty:** Medium | **Workload:** Moderate | **Industry relevance:** Low-Medium (foundational)

Propositional logic, predicate logic, proofs, set theory. Dry but necessary. Many students find it tedious; the students who actually absorb the proof-writing skills are better prepared for theory courses.

**Student tips:**
- Do all the practice problems. The exam questions mirror practice closely.
- 272 is a prerequisite for 204, so the proof skills carry straight into algorithms.

---

## CMPUT 291: Introduction to File and Database Management

**Difficulty:** Medium | **Workload:** Moderate | **Industry relevance:** High

SQL, relational models, NoSQL (MongoDB), query optimization basics. Two big assignments and two group projects in most sections (a Python SQLite project and a MongoDB project). Students generally find the course reasonable; it's considered significantly lighter than 229.

"Most of the hate is for the course, not the prof. The course is pretty difficult and quite unique compared to other CS courses, meaning you probably need to put in more time than usual."

**Instructor notes:**
- **Davood Rafiei:** works many examples in class and exams are considered fair. Students have wanted more practice material before the midterm and final.

**Student tips:**
- The group projects are actually interesting and involve real tools (Python+SQLite, MongoDB). Engage with them.
- Start the SQL assignment early; multiple students report it being very time-consuming.
- Good pairs with 229 (manageable combined workload, and 291's disk content connects to 229's memory hierarchy).

---

## CMPUT 301: Introduction to Software Engineering

**Difficulty:** Medium | **Workload:** Heavy (team-dependent) | **Industry relevance:** High

Android development project + software engineering concepts (design patterns, UML, requirements). The project is the course. Your experience with 301 is almost entirely determined by your team. A good team makes it one of the better courses in the program; a bad team makes it one of the most stressful.

"Don't look at GPA or internships when choosing teammates. Look at what they've committed to on GitHub: commit frequency, net lines of code, contribution history." This is actual, verified advice from students.

"If you get a good team who doesn't rely on AI (LLMs are terrible at Android Studio), the class is really light. Exams are basically free if you pay attention and can think critically."

**Instructor notes:**
- **Hazel Campbell:** main instructor in recent offerings. Participation marks can be earned online and lectures are typically recorded on Zoom, which reduces the need for in-person attendance.
- **Abram Hindle:** teaches 301 in some terms. Students value his industry experience and structured delivery.

**Student tips:**
- Teams are formed by lab section, not lecture section. Coordinate with friends so you're in the same lab.
- Screen your team early (before formal team formation if possible). Check reliability and prior contribution history to avoid team project issues later.
- The Firebase database integration is where many groups get stuck. Start early.
- 301 uses Java + Android Studio. Brush up on Java OOP before the semester starts.

---

## CMPUT 313: Communication Networks

**Difficulty:** Medium | **Workload:** Moderate | **Industry relevance:** Medium-High

TCP/IP, routing, DNS, the OSI model, socket programming. Often cited as "boring but useful." Students who go on to do backend or infrastructure work often say they wished they'd paid more attention.

"313 is drier than the desert. Not much relevancy to modern hands-on networking unless you want to get deep into network protocols." But counter-view: "After 313, I finally understood what actually happens when you type a URL."

**Instructor notes:**
- **Ioannis Nikolaidis:** entertaining lectures with frequent (often interesting) tangents; assignments are tough but rewarding.

**Student tips:**
- This course pairs well with 379 (operating systems); they cover complementary systems content.
- The concepts are more directly applicable to industry than the course's reputation suggests.

---

## CMPUT 325: Non-Procedural Programming

**Difficulty:** Medium | **Workload:** Moderate | **Industry relevance:** Medium

The course begins with the Functional Programming paradigm via Lisp (or Haskell). Functional Programming is completely new if coming from a typical procedural programming background (Python, C; programming involving the execution of instructions top-down), but the paradigm is still fit for general purpose uses. Much of Functional Programming revolves around recursion and in particular defining functions which treat an array elementwise before recursing. Discussion on FP concludes with lambda calculus, which describes how higher-order lambda functions work both fundamentally and through Lisp.

The second half of the course covers the Logical Programming paradigm, which is more polarizinng among students who've taken the course; Prolog is arguably a bigger leap than Lisp as the paradigm revolves around defining logical facts and rules to determmine solutions. Prolog uses a solution finder that runs a depth-first search on some tree of all possible solutions given a query (goal) and your facts and rules. We also touch on Prolog's feasibility for database querying using various built-in functions. Following coverage of Logical Programming basics, discussion transitions to Constraint Logical Programming in Prolog, which is about restricting the possibilities for a solution to achieve a complex goal more dynamically (i.e., creating a valid Sudoku table). 

New to the course as of Winter, 2026 is Answer Set Programming, which is **not** general purpose, but opens up possibilities as far as solving difficult problems with less complexity.

**Reviews:** "325 was much more useful and fun. It'll help teach you recursion really well." Another student: "313 is boring and relatively painful to study for but will teach you some fantastic concepts. 325 is more fun."

**Student tips:**
- If you've only programmed in Python/Java/C, functional programming will feel alien at first. Stick with it; the perspective shift is the whole point.
- Take this before 466 (ML) if you can; functional thinking maps well to ML.

---

## CMPUT 379: Operating Systems

**Difficulty:** Medium | **Workload:** Low-Heavy | **Industry relevance:** Critical

Processes, threads, scheduling, virtual memory, memory management, file systems, inter-process commmunication (IPC). For anyone pursuing Computer Science, this course is extremely useful, but it is especially important for anyone pursuing a career in systems. Completion of CMPUT 379 opens up the opportunity for further studies in systems, including CMPUT 481 (Distributed Systems). Students say it is of the most professor-dependent courses in the program; the same material can be result in very different experience depending on who's teaching.

The textbook is completely free online: https://pages.cs.wisc.edu/~remzi/OSTEP/

**Reviews:**
> "It's basically an extension of 201 with more interesting theory and a little bit of new programming. Definitely worth taking."
> "It can be up there in difficulty; my prof curved it so nobody got an A."

**Instructor notes:**
- **Omid Ardakanian:** solid coverage in lectures; accommodating, with a midterm and final described as "very reasonable if you pay attention."
- **Ioannis Nikolaidis:** entertaining with tangents; hard assignments and tests. The textbook is essential in his sections.
- **Paul Lu:** also teaches 481, where students find his lectures very engaging. In 379, one student found that exams asked about intricacies that lectures didn't cover in depth, so lean on the textbook.

**Student tips:**
- The textbook is a must for Nikolaidis sections; his lectures don't cover everything.
- 379 is significantly easier if you're solid on material from 201. Comfort with C (or C++, depending on the instructor) matters.

---

## CMPUT 382: GPU Programming and Architecture

**Difficulty:** Medium | **Workload:** Moderate | **Industry relevance:** High (niche but rare)

CUDA programming, GPU architecture, parallel algorithms. Not widely discussed on Reddit because not many students take it. The few who have report that labs take the full 3 hours but the course isn't disproportionately harder than other 300-level courses. Disorganized in some past offerings.

This course has not been offered since Fall, 2024, with no future semesters listed.

**Student tips:**
- The ability to write GPU code is genuinely rare among CS graduates. This is a strong differentiator if you're going into ML infrastructure, HPC, or graphics.
- Background in 229 (computer organization) helps significantly; GPU optimization requires understanding what hardware is actually doing.

---

## CMPUT 401: Software Process and Product Management

**Difficulty:** Medium | **Workload:** Moderate | **Industry relevance:** Medium

Software development lifecycle, project management, agile, product thinking. More conceptual than 301. Exams are typically manageable; the course leans on readings and projects.

"When I did 401 last fall, the final exam was a take-home written and you had ALL DAY to work on it. The exam itself was not hard at all; mainly some questions asking about terminology and your experience with these terminologies during your project."

**Current instructor:**
- **Mark Polak:** students describe him as chill, approachable, and easy to talk to. He is also noted for strong industry connections, and some students report these relationships can help with referrals.

**Student tips:**
- Pairs surprisingly well with 379; they're both manageable in workload terms and cover different enough material that studying doesn't interfere.
- The exam weight is usually low (many versions are take-home or project-based). Focus energy on the project.
- Expect a lot of meetings. Manage your time carefully: most teams meet TAs at least twice per week (sometimes three times), and you also need regular stakeholder meetings to keep requirements aligned.
- The project is directly industry-related. Your experience can vary a lot based on stakeholder type (startups, established companies, charities, or individual clients).

---

## CMPUT 403: Algorithmics in Competitive Programming

**Difficulty:** Hard | **Workload:** Heavy | **Industry relevance:** Critical

Segment trees, advanced graph algorithms, string algorithms, dynamic programming optimization, computational geometry. The best interview prep course at UofA.

**Instructor notes:**
- **Zachary Friggstad:** active on Discord and generous with partial solutions that get the right idea. Students rave about his offering.

**Student tips:**
- Check the [catalogue](https://apps.ualberta.ca/catalogue/course/cmput/403) for prerequisites (it requires 204 and a 300-level CMPUT course) and register early; seats are limited.
- Do problems on Kattis regularly throughout the semester; don't try to cram.
- If you're applying to Google, Meta, or any company that does hard algorithm interviews: this course maps directly to what they ask. There is no better use of an elective slot.

---

## CMPUT 404: Web Applications and Architecture

**Difficulty:** Medium | **Workload:** Heavy | **Industry relevance:** High

Web protocols, HTTP, REST APIs, front-end and back-end web development. The material is highly practical and directly applicable to most industry roles, though some students report that specific tooling examples can feel slightly outdated in certain offerings.

**Instructor notes:**
- **Hazel Campbell:** grading is driven mostly by ongoing project work, so the key is staying on top of the course load from week one.

**Student tips:**
- If course tooling feels dated, many students successfully use their own modern front-end framework and learn independently, while still meeting project requirements.
- Form your group early, ideally before the class formally requires team formation. Students who pre-screen teammates (reliability, prior project history, communication) report better outcomes.
- The group project can make or break your experience. Even with contribution adjustments, weak team participation can still hurt marks; this is a common reason students drop the course.
- Web development skills built here directly transfer to internship work. Pay attention.

---

## CMPUT 415: Compiler Design

**Difficulty:** Brutal | **Workload:** Overwhelming | **Industry relevance:** Medium-High

Grammars (ANTLR4, finite state automata), lexing, parsing (and the history of parsers), abstract syntax trees (AST), semantic analysis (including variable scopes and lifetime), code generation, LLVM/MLIR, and compiler optimization (basic blocks, dataflow, available expressions), and register allocation. One of the most work-intensive courses in the program on account of the project.

The project is a full LLVM-based compiler for an obscure IBM language (the spec. is 40 pages and glosses over features). Most groups don't finish all features. A part of your evaluation involves competitive testing - students are to write a test suite for their submissions designed to test your adherence to the specification and coverage of edge cases. You get points for causing exceptions in other people's programs, while your submission is tested for its robustness against all the student test cases. 


**Reviews:**
> "The workload never lets up. You constantly need to be working. As soon as an assignment is done, it's in your best interest to start the next one immediately."
> "Without a doubt the most work I've had to do for a CMPUT course. Also the course I learned the most in; in retrospect, I would still take it again."

**Student tips:**
- Proficiency in C++ is assumed - intimate familiarity is essential.
- Look up ANTLR (parser generator) and LLVM/MLIR before the course begins.
- Do not take 415 with other heavy or project-based courses. Despite lectures ending a whole month before the end of the semester, working on the project itself is practically a full-time commitment.
- Despite the challenges, this course is worth it if you're interested in compilers, developer tooling, or understanding how language frontends work.

**Instructor notes:**
- **Ron Unrau:** "Ron's lectures are interesting and engaging, given his personal experience in industry. He is also understanding and gives fair exams, in addition to ample resources to prepare."
- **José Nelson Amaral:** may appear throughout the semester even when Prof. Unrau is the instructor. His lecture videos from 2020 have aged well, since both instructors use his slides.

---

## CMPUT 466: Machine Learning

**Difficulty:** Hard-Brutal (professor-dependent) | **Workload:** Heavy | **Industry relevance:** Critical

Supervised learning, neural networks, probabilistic models, optimization. The experience varies a lot by section, so it's worth asking upper-years about the current instructor.

**Instructor notes:**
- **Dale Schuurmans:** students praise the textbook he uses and describe exams and assignments as fair.
- **Russ Greiner:** enthusiastic lecturer; former students credit his section with launching their interest in ML.

**Student tips:**
- Check who is teaching before registering and ask upper-years how that section has been run (exam format, pacing, practice material).
- Prerequisite-wise, CMPUT 267 and MATH 125 are important. Students who skipped 267 often feel lost on the math.
- If you're going into ML in industry or research: this course is mandatory. Take it with a good prof even if it means waiting a semester.

---

## Summary Table

| Course | Difficulty | Workload | Industry Relevance |
| -------- | ----------- | ---------- | ------------------- |
| 101 | Easy | Light | Low |
| 174 | Easy-Med | Moderate | Low (foundational) |
| 175 | Medium | Moderate-Heavy | Low (foundational) |
| 201 | Hard-Brutal | Heavy | High |
| 204 | Medium-Hard | Moderate-Heavy | Critical |
| 229 | Brutal | Overwhelming | Medium |
| 267 | Hard | Heavy | High |
| 272 | Medium | Moderate | Low-Medium |
| 291 | Medium | Moderate | High |
| 301 | Medium | Heavy (team-dep.) | High |
| 313 | Medium | Moderate | Medium-High |
| 325 | Medium | Moderate | Medium |
| 379 | Medium | Moderate/Heavy | Critical |
| 382 | Medium | Moderate | High (niche) |
| 401 | Medium | Moderate | Medium |
| 403 | Hard | Heavy | Critical |
| 404 | Medium | Heavy | High |
| 415 | Brutal | Overwhelming | Medium-High |
| 466 | Hard-Brutal | Heavy | Critical |

---

## Common Course Combos: What Students Actually Recommend

**The classic 2nd year:** 201 + 204 + 291 + MATH 125. Manageable. 201 and 204 pair well; different kinds of difficulty.

**The notorious combo to avoid:** 229 + 301 + 350 in the same semester. Multiple students describe this as survivable but brutal. If you have no choice, ensure you can drop one.

**Competitive programming path:** 204 → 403 → apply for internships. This sequence is the most direct path to landing technical interviews.

**ML path:** 267 → 466 → 365. Take MATH 125 and STAT 151/252 first.

**Systems path:** 201 → 229 → 379 → 481. The natural progression if you're interested in low-level systems, OS, or parallel and distributed computing.
