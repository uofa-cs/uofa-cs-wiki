# Course Reviews: Real Student Perspectives

These reviews are synthesized from student discussions on r/uAlberta and RateMyProfessors data. Difficulty and workload ratings reflect student consensus. Professor recommendations are based on RMP ratings and Reddit sentiment. "Best for industry" ratings reflect how directly the material maps to software engineering roles.

---

## How to Read This Page

- **Difficulty:** Easy / Medium / Hard / Brutal
- **Workload:** Light / Moderate / Heavy / Overwhelming
- **Best prof / Worst prof:** based on RMP + Reddit data (or current instructors if no other professors have taught recently)
- **Industry relevance:** Low / Medium / High / Critical

---

## CMPUT 101: Introduction to Computing

**Difficulty:** Easy | **Workload:** Light | **Industry relevance:** Low

The gentlest introduction to programming at UofA. Designed for students with zero background. If you've already programmed in high school, this is almost certainly too easy; most students with any programming experience report going to almost no classes and still doing well.

**Best profs:** Michael Bowling (4.6/5 RMP) brings genuine enthusiasm and CS research credibility to what could be a throwaway course. Russ Greiner (3.5/5) is another option; goes on tangents but clearly cares about students.

**Student tips:**
- If you have any programming background, consider skipping straight to 174. Talk to an advisor.
- Show up for labs even if lectures seem too slow. Labs count.
- Don't pick this course expecting it to be challenging; treat it as a free GPA boost.

---

## CMPUT 174: Introduction to Computing I

**Difficulty:** Easy-Medium | **Workload:** Moderate | **Industry relevance:** Low (foundational)

First-year Python course. Variables, control flow, functions, recursion, basic data structures. The pace is manageable for students who engage consistently, but students who miss lectures and try to catch up before exams frequently struggle; programming doesn't work that way.

**Best profs:**
- **Osmar Zaiane (4.6/5):** possibly the most beloved professor in the entire CS department. Uses physical props to illustrate programming concepts (reportedly brought a volleyball to class to demonstrate exception handling), calls on students with prizes, genuinely enthusiastic. Heavy workload with 3-4 assessments per week, but you actually learn. "Fantastic prof, the best prof in CS so far," one student wrote.
- **Joerg Sander (4.0/5):** solid and reliable. Explains material thoroughly, responds to emails, good for students without prior experience. "Really engages the class; rather than blasting through solutions he will stop and get the class to solve each problem."
- **Jonathan Schaeffer (4.7/5):** when he teaches 174/175, students consistently rate him among the best they've had. Inspiring lecturer who ties content to real CS history.

**Avoid:**
- Some sections of 174 have had poor instruction in the past; check RMP before registering.

**Student tips:**
- Do your labs independently. Students who collaborate too closely or use AI on labs fail to build the actual skill and later struggle.
- If you have prior Python experience, 174 might feel slow; use the extra time to build personal projects rather than coasting.
- The jump from 174 to 175 is real. Don't let an easy 174 make you complacent.

---

## CMPUT 175: Introduction to Computing II

**Difficulty:** Medium | **Workload:** Moderate-Heavy | **Industry relevance:** Low-Medium (foundational)

Continues from 174. Object-oriented programming, more complex data structures, recursion deepened. The jump from 174 to 175 catches a lot of students by surprise.

**Best profs:** Same as 174: **Zaiane** and **Schaeffer** are consistently praised. One student who got Schaeffer wrote: "Jonathan is an inspiring lecturer and one of the best profs I had this term. I was honestly considering dropping CS until he showed me how interesting it can be."

**Student tips:**
- The OOP concepts introduced here (classes, inheritance, interfaces) will appear in every upper-year course. Don't treat this as just "more Python."
- 175 is a good place to start doing side projects in Python using what you've learned.

---

## CMPUT 274/275: Tangible Computing I & II (Alternative First-Year Stream)

**Difficulty:** Hard | **Workload:** Heavy-Overwhelming | **Industry relevance:** Medium

The alternative to 174/175. Uses Raspberry Pi hardware, covers Python deeply in 274, then C++ in 275. Reddit is divided: students with strong prior experience often found it manageable and preferred the content depth; students who went in without a strong base often found it brutal.

"274/275 are the worst designed classes I've ever taken. You put in 20 hours per week in just one class. Everything is insanely crammed in," one student wrote. But another countered: "I disagree. 274/275 wasn't hard, I got an A in both. The content is much more important than 174/175."

**The honest consensus:** 274/275 works well for students with prior programming experience who want to move faster. It's a rough experience for students without that foundation. Also note: some upper-year professors recommend students retake 204 even after completing 275, since 275 covers algorithms less thoroughly.

**Best profs:**
- **Michael Bowling (4.6/5)** and **Omid Ardakanian (4.5/5)** are both praised for 275.
- **Paul Lu (2.2/5)** has a difficult reputation for 274: unclear explanations, exams described as "multiple guessers that have 6 choices that are all right and ask you which one is more right."

**Student tips:**
- If you're considering 274/275, be honest about your background. If you have 2+ years of prior programming, go for it. Otherwise, 174/175 and a higher GPA is probably the smarter play.
- If you take 275, still consider taking 204 later; it covers algorithms in more depth.

---

## CMPUT 201: Practical Programming Methodology

**Difficulty:** Hard-Brutal | **Workload:** Heavy | **Industry relevance:** High

The rite of passage for any UofA programmer, no matter the experience. The course focuses on C99: a walkthrough of basic syntax before delving into pointers, memory management, structs and unions, the preprocessor, implementing abstract data structures, bitwise operators and bitfields in C. 201 covers a lot more C than 275.

Alongside learning C, this will be your first encounter with GitHub. You will learn how to do Git operations individually: cloning, adding/pushing, (and if the TAs update the lab) resolving merge conflicts. You also learn debugging with gdb, and programming in vim; though most students debug with `printf` and use Remote SSH to connect to the lab machines.

The TA's—who design nearly every lab—and the professors will not hold back. Labs and In-Class Coding will require knowledge about algorithms and data structures from 175, complementing 272 and 204 as well. Linked Lists alongside sorting algorithms are required to know. Despite the low averages and the soul-crushing assignments, you will become a more resilient programmer.

**Professors:**
- **Henry Tang:** A very good professor. He teaches well; his notes cover the subject thoroughly and he speaks clearly. However, he still has the same level of difficulty and will curve a lot less leniently than Dr. Lin.
- **Guohui Lin:** Also a good professor. Don't let RMP brainwash you into thinking he sucks. He has a thick Chinese accent and has a shabby microphone setup, but he is equally as knowledgeable. His notes are better as additional information after reading the textbook, though you can do well just by his notes alone. Has a very lenient curve!

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

**Best profs:**
- **Martin Mueller (2.7/5):** mixed. Some students find his lectures too vague ("huge walls of text"), but others note he is easy to get a good grade with if you put in the work. Assignments are fair.
- **Zachary Friggstad (3.7/5):** highly recommended. Very smart, active on Discord, approachable. Goes fast in lectures but willing to slow down if you ask. "Insanely smart guy, and watching him solve Kattis problems in class was an experience in itself."
- **Mohammad Salavatipour:** mentioned positively by students in Reddit threads for both 204 and 272.

**Student tips:**
- Do practice problems beyond the assignments. 204 material is best learned by doing, not reading.
- If you plan to do competitive programming (CMPUT 403), start building those habits now.
- This course is harder than 201 in a different way; it's abstract, not mechanical. Budget time accordingly.

---

## CMPUT 229: Computer Organization and Architecture

**Difficulty:** Brutal | **Workload:** Overwhelming | **Industry relevance:** Medium

Assembly language, MIPS, CPU design, memory hierarchy. Consistently cited by students as the hardest course in the program. One student's RMP review: *"One time a friend asked me, 'How's life besides 229?' I quickly answered, 'There is no life besides 229.'"*

The course genuinely matters; understanding what happens at the hardware level makes you a better programmer. But the execution has varied wildly by professor, and the workload (weekly labs, difficult midterms) is punishing.

**Best profs:**
- **Jose Nelson Amaral (3.7/5):** polarizing but often excellent. Passionate, makes dry material genuinely exciting, has industry connections (his students go to Google, IBM). His labs are extremely hard and his exams tough. "Nelson is incredibly passionate and his lectures are excellent. He has extremely high standards but sets his students up well to meet them." Some students found him too demanding and felt he played favorites.

**Avoid:**
- **Karim Ali (2.7/5):** very poor reviews. "Imagine a class where the average GPA for the entire class was 1.6." His midterms reportedly don't match what was taught. One student suggested: "Take 229 with Mike [another instructor] and watch Nelson's videos on YouTube."

**Student tips:**
- If you're registering and Nelson is teaching, take him, but go in knowing it will be a grind. If you have the choice, multiple students recommend watching Nelson's free YouTube lecture series even if you're in a different section.
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

**Best profs:**
- **Lorna Stewart (3.9/5):** highly recommended. Posts all notes online (great typed notes), clear lectures, lenient on missed quizzes (weight transfers to final). "I feel sorry to know that this is her last semester to teach because this class is comprehensive and builds great foundations." If she's still teaching, take her.
- **Mohammad Salavatipour:** mentioned positively by Reddit users.

**Avoid:**
- **Randy Goebel (1.8/5):** "Genuinely the worst prof I have seen in the university. Shouts at people if they leave class even 10 mins early." Multiple reviews describe him as refusing to teach, directing students to the textbook instead. His exams are reportedly much harder than the course material covered in lectures.

**Student tips:**
- If you get Stewart (or her notes are available), the course is very manageable.
- Do all the practice problems. The exam questions mirror practice closely.

---

## CMPUT 291: Introduction to File and Database Management

**Difficulty:** Medium | **Workload:** Moderate | **Industry relevance:** High

SQL, relational models, NoSQL (MongoDB), query optimization basics. Two big assignments and two group projects in most sections (a Python SQLite project and a MongoDB project). Students generally find the course reasonable; it's considered significantly lighter than 229.

"I think Davood [Rafiei] is actually a pretty good prof and most of the hate is for the course. The course is pretty difficult and it is quite unique compared to other CS courses, meaning you probably need to put in more time than usual."

**Best profs:**
- **Davood Rafiei (2.5/5):** mixed but not as bad as his RMP score suggests. Does many examples in class, exams are fair. Main complaint: lectures occasionally unorganized, not enough prep material for midterm/final.
- **Joerg Sander (4.0/5):** when he teaches 291/291-adjacent courses, ratings are strong.

**Avoid:**
- **Mario Nascimento (2.7/5):** students describe eClass as disorganized, TAs who can't help, and a course structure that doesn't reward effort.

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

**Current instructors:**
- **Hazel Campbell:** main instructor in recent offerings. Some students find her online participation-mark setup useful, since it can reduce the need for in-person attendance and recordings are typically available on Zoom.
- **Abram Hindle (4.1/5):** teaches 301 in some terms. Students consistently value his industry experience and structured course delivery.

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

**Best profs:**
- **Ioanis Nikolaidis (3.5/5):** entertaining, goes on tangents (many interesting), assignments are tough but rewarding. Students who took him for 379 also spoke highly of him. When available, he's a significant upgrade.

**Avoid:**
- **Ehab Elmallah (2.4/5):** dry, monotone, slides ripped straight from the textbook, and teaches "extremely outdated" networking content. Grading criteria described as inconsistent. "Holy shit do I not like his style of teaching." Students who chose 379 (OS) over 313 partly because of Elmallah.

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

**Best profs:**
- **Omid Ardakanian (4.5/5):** Lectures have solid coverage, despite being a little monotone. Omid is accommodating; midterm and final described as 'very reasonable if you pay attention.'"
- **Ioanis Nikolaidis (3.5/5):** "Entertaining, but goes on tangents. Hard assignments, hard tests. 'Very bright individual and one of the better profs in the department.'"

**Avoid:**
- **Ehab Elmallah (2.4/5):** Also teaches 379 sometimes. Same issues as in 313: boring, ineffective teaching. One RMP review: 'Prof took a normally curved 300-level class and said nah, what if average GPA was 2.3?' Another: 'Only 1 or 2 people got an A out of about 100.'"
- **Paul Lu (2.5/5):** "Often teaches 379 and 481. While lectures in 481 are extremely engaging, I found his coverage of 379 left alot to be desired, as deep discussion of the material and intricacies asked after in the exams was largely absent. The assignments for this course were not particularly engaging or relevant. Not terribly difficult, but you should find another offering for the sake of your own learning."

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

**Best profs:**
- **Zachary Friggstad (3.7/5):** highly recommended. Brilliant, active on Discord, will accept imperfect solutions in spirit. "Amazing CMPUT 403. Definitely recommend him." Also described as someone who "was a father to me. A watchful protector of the CS department."

**Student tips:**
- You need 204 first. No exceptions.
- Do problems on Kattis regularly throughout the semester; don't try to cram.
- If you're applying to Google, Meta, or any company that does hard algorithm interviews: this course maps directly to what they ask. There is no better use of an elective slot.

---

## CMPUT 404: Web Applications and Architecture

**Difficulty:** Medium | **Workload:** Heavy | **Industry relevance:** High

Web protocols, HTTP, REST APIs, front-end and back-end web development. The material is highly practical and directly applicable to most industry roles, though some students report that specific tooling examples can feel slightly outdated in certain offerings.

**Instructor note:**
- **Hazel Campbell (2.0/5):** ratings are often low, but some students say her classes are not as bad as the rating suggests. A common view is that many low reviews come from students who struggled with grades. The key is staying on top of the course load, since grading is driven mostly by ongoing project work.

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

**Best profs:**
- **Ron Unrau (5/5):** "Ron's lectures are interesting and engaging, given his personal experience in industry. He is also understanding and gives fair exams, in addition to ample resources to prepare."
- **Nelson Amaral (5/5):** "Likewise, a great instructor who may still appear throughout the semester, even with Prof. Unrau. His lecture videos are available to those who do not attend class in person and have aged well since their creation in 2020, as both instructors use his slide presentations."

---

## CMPUT 466: Machine Learning

**Difficulty:** Hard-Brutal (professor-dependent) | **Workload:** Heavy | **Industry relevance:** Critical

Supervised learning, neural networks, probabilistic models, optimization. The capstone ML course. Quality varies enormously by who is teaching.

**Best profs:**
- **Dale Schuurmans (4.1/5):** "Dale is very clever and knows how to make students understand the material. The book he uses is very good. The course itself is not too difficult and his exams and assignments are very fair." Highly recommended; 100% would-take-again on RMP.
- **Russ Greiner (3.5/5):** "Inspirational. His enthusiasm for machine learning is contagious. His ML course is THE foundational course that helped me launch my career in this exciting area."

**Mediocre:**
- **Richard Sutton (3.1/5):** the RL legend, but not a natural classroom teacher. Heavy reading load, forum questions often go unanswered, exams can feel disconnected from lectures. "He understands AI quite deeply, but can't teach." Worth taking for the exposure to foundational RL concepts, but go in knowing you'll do a lot of self-teaching.
- **Csaba Szepesvari (3.1/5):** brilliant researcher, but his teaching style presumes graduate-level math fluency. "An extremely intelligent man; given that, I don't believe he should be allowed to teach any course that isn't a masters course." His exams have been described as masters-level regardless of course level.

**Avoid:**
- **Martha White (2.6/5):** heavy criticism on RMP. Multiple-choice exams with negative marks, assignments with errors that go unfixed, pacing described as impossibly fast. "Somehow worse than XBL. She zooms through lectures so fast no one understands anything."
- **Nidhi Hegde (1.3/5):** the lowest-rated professor in the entire department. 62 reviews, only 6.5% would-take-again. Posts assignments late, no practice exams, unanswered forum questions, unintelligible handwritten notes. "No practice pretty much at all. Only way to learn is reading AI-generated slides."

**Student tips:**
- Check who is teaching before registering. The difference between Schuurmans and Hegde in this course is enormous.
- Prerequisite-wise, CMPUT 267 and MATH 125 are important. Students who skipped 267 often feel lost on the math.
- If you're going into ML in industry or research: this course is mandatory. Take it with a good prof even if it means waiting a semester.

---

## Summary Table

| Course | Difficulty | Workload | Best Prof | Worst Prof | Industry Relevance |
|--------|-----------|----------|-----------|------------|-------------------|
| 101 | Easy | Light | Bowling | - | Low |
| 174 | Easy-Med | Moderate | Zaiane | varies | Low (foundational) |
| 175 | Medium | Moderate-Heavy | Zaiane, Schaeffer | varies | Low (foundational) |
| 201 | Hard-Brutal | Heavy | Nadi, H. Tang | Lin, Buro | High |
| 204 | Medium-Hard | Moderate-Heavy | Friggstad | - | Critical |
| 229 | Brutal | Overwhelming | Amaral (YouTube) | Karim Ali | Medium |
| 267 | Hard | Heavy | Buechler (new) | - | High |
| 272 | Medium | Moderate | Stewart | Goebel | Low-Medium |
| 291 | Medium | Moderate | Rafiei | Nascimento | High |
| 301 | Medium | Heavy (team-dep.) | Hazel (main), Hindle (sometimes) | - | High |
| 313 | Medium | Moderate | Nikolaidis | Elmallah | Medium-High |
| 325 | Medium | Moderate | - | - | Medium |
| 379 | Medium | Moderate/Heavy | Ardakanian | Elmallah | Critical |
| 382 | Medium | Moderate | - | - | High (niche) |
| 401 | Medium | Moderate | Mark Polak | - | Medium |
| 403 | Hard | Heavy | Friggstad | - | Critical |
| 404 | Medium | Heavy | - | H. Campbell | High |
| 415 | Brutal | Overwhelming | Nelson Amaral, Ron Unrau | - | Medium-High |
| 466 | Hard-Brutal | Heavy | Schuurmans | Hegde | Critical |

---

## Common Course Combos: What Students Actually Recommend

**The classic 2nd year:** 201 + 204 + 291 + MATH 125. Manageable. 201 and 204 pair well; different kinds of difficulty.

**The notorious combo to avoid:** 229 + 301 + 350 in the same semester. Multiple students describe this as survivable but brutal. If you have no choice, ensure you can drop one.

**Competitive programming path:** 204 → 403 → apply for internships. This sequence is the most direct path to landing technical interviews.

**ML path:** 267 → 466 (with Schuurmans if possible) → 365. Take MATH 125 and STAT 151/252 first.

**Systems path:** 201 → 229 → 379 → 382. The natural progression if you're interested in low-level systems, OS, or GPU work.
