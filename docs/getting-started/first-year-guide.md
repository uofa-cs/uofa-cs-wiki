# First Year Survival Guide

First year CS at UofA is where a lot of students either build good habits or fall into bad ones that take two years to undo. This guide is the advice you'd get from a senior student who actually made it through — not the sanitized version from an orientation pamphlet.

Let's be direct: first year is not that hard academically if you stay on top of it. The students who struggle aren't usually the ones who lack intelligence — they're the ones who underestimated how quickly things compound when you fall behind in a programming course.

---

## Your First Programming Courses: 174/175 vs 274/275

This is one of the first real decisions you make as a CS student.

### CMPUT 174 and 175 (Standard Stream)

This is the default entry point. Both courses use Python, which is the right language to start with — it's readable, the syntax doesn't fight you, and the ecosystem is enormous. 174 covers the basics: variables, control flow, functions, recursion. 175 goes further into object-oriented programming, data structures, and more complex problem-solving.

These are manageable courses if you engage consistently. The students who fail 174/175 are almost always students who skipped lectures, fell behind on assignments, and then tried to cram before exams. Programming doesn't work like that. You can't memorize your way through debugging a recursive function at 11pm the night before a deadline.

**Best professors for 174/175:** If **Osmar Zaiane** is teaching, register immediately — he is consistently called one of the best professors in the department, with 95%+ would-take-again on RMP. He uses physical props in lectures, calls on students (with prizes, not shame), and makes the material genuinely engaging. His workload is heavy (3–4 assessments per week), so don't take his section if you're overloaded — but if you can, his section is significantly better than alternatives. **Joerg Sander (4.0/5)** and **Jonathan Schaeffer (4.7/5)** also have strong reviews for these courses.

### CMPUT 274 and 275 (Tangible Computing Stream)

The Tangible Computing stream is an alternative intro sequence taught using Raspberry Pi — actual physical hardware. You'll write code that interacts with sensors, motors, and displays. It's hands-on in a way that 174/175 is not, and frankly it's more exciting. You build things you can show people.

The tradeoff: it's harder. Student opinion on r/uAlberta is genuinely divided. A student with prior experience said: "274/275 wasn't hard, I got an A in both. The content is much more important than 174/175." But a student without prior experience said: "274/275 are the worst designed classes I've ever taken. You put in 20 hours per week in just one class. Everything is insanely crammed in."

**The honest community consensus:** 274/275 works well for students with solid prior programming experience. For students entering with limited background, the pace is brutal and the GPA damage is real. One practical note: some upper-year professors recommend taking 204 later even if you complete 275, since 275 covers algorithms less thoroughly than a dedicated algorithms course.

Also notable: professor matters a lot in 274/275. **Michael Bowling (4.6/5)** and **Omid Ardakanian (4.5/5)** have strong reviews for this sequence. **Paul Lu (2.2/5)** for 274 has poor reviews with consistent complaints about unclear explanations and confusing exams.

If you're interested in embedded systems, robotics, or hardware — 274/275. If you want to protect your GPA in first year and have no strong background — 174/175, and use the extra time to build side projects.

Both paths work. Choose based on your honest self-assessment.

---

## Math: Don't Blow It Off

CS students sometimes treat math as an obstacle rather than a tool. That's a mistake. Here's what you're looking at in first year:

**MATH 114 — Calculus I**
Limits, derivatives, basic integration. Standard first-semester university math. If you took calculus in high school, this will feel familiar. Don't get complacent — university grading is different from high school, and the pace is faster. Do the problem sets.

**MATH 115 — Calculus II**
Integration techniques, series, an introduction to multivariable calculus. More abstract than 114. This is where students who coasted through 114 sometimes hit a wall. Keep up with the material weekly.

**MATH 125 — Linear Algebra**
Take this as early as you can. Linear algebra is the math that directly powers machine learning, computer graphics, and a lot of scientific computing. Vectors, matrices, eigenvalues, linear transformations — if you go anywhere near ML in your career, you will use this constantly. Students who defer MATH 125 until third year end up taking ML courses without the proper mathematical grounding.

**STAT 151 and 252 — Applied Statistics**
Statistics is more useful than most CS students realize until they're in industry or doing ML work. A/B testing, inference, probability, regression — this comes up everywhere. Take STAT 151 in first or second year. Don't leave both stats courses for later.

---

## How to Not Fail: The Basics That Aren't Obvious

**Don't skip lectures in 174/175.** Programming courses are taught with a specific pedagogy — each lecture builds on the previous one. If you miss two lectures and don't read the slides and test the code yourself, you will not be able to figure out the assignment. This is not like a history course where you can read the textbook later. The compounding is real.

**Do the assignments yourself.** Not because of academic integrity concerns (though those exist) — because the act of struggling through a problem and actually solving it is how you learn to program. Students who copy or over-collaborate end up failing practical assessments and interviews because they never built the actual skill. Do the work.

**Start assignments early.** This is the most repeated advice in university and the most ignored. Programming assignments take twice as long as you estimate, especially when you hit a bug you don't understand. Start with enough time to get stuck, ask for help, and still finish before the deadline.

**Office hours are not just for when you're failing.** TAs and professors at UofA are generally accessible and more helpful than you expect. Going to office hours when you're confused is table stakes. Going to office hours to discuss interesting problems or follow up on lecture topics is how you start building relationships with faculty — which matters if you ever want a reference letter or a research opportunity.

---

## Finding Your People: Study Groups and Community

University is social in ways that high school wasn't. The people you study with in first year often become your professional network, your collaborators, and your friends for the next decade.

**Form study groups early.** Your lab sections are a natural place to find people — you're all working through the same problems. Introduce yourself. Ask someone if they want to compare approaches to an assignment. It's less awkward than it sounds.

**The CS Discord servers** — there are student-run Discord communities for UofA CS. Ask around in your courses or look for them posted in eClass. These are genuinely useful for quick questions, course-specific channels, and finding people to study with.

**The Computer Science Club (CSC) Lounge** — There is a CS student space in the Computing Science building. Hang out there. Students work there, whiteboard problems, procrastinate together. It's one of the better ways to become a regular part of the CS student community. Upper-year students who hang out there are often willing to give advice, share course tips, or point you toward opportunities.

---

## Setting Up Your Environment: Do This Right From Day One

**Do not use IDLE for CMPUT 174.** IDLE is Python's built-in editor and it is completely adequate for toy scripts and nothing else. Get a real IDE from the start. VS Code is the standard recommendation — it's free, extensible, supports every language you'll encounter, and has excellent Python support. PyCharm is another good option for Python specifically.

Getting comfortable with a proper development environment in first year pays off for every year after. Setting up syntax highlighting, a debugger, and a terminal you understand makes everything faster and less frustrating.

**Start using version control immediately.** This means Git. Even for first-year assignments. Get a GitHub account, initialize a repo for each course (keep them private if your department requires it), and commit your work regularly. You will not regret this habit. The students who learn Git properly in first year have a real advantage — it comes up in every internship application and every technical interview eventually. The students who learn it properly in third year wish they'd learned it in first year.

You don't need to master Git immediately. Learn `git init`, `git add`, `git commit`, `git push`, and `git status`. That's enough to get started.

---

## Navigating Course Information

**eClass is the official LMS** — your assignments, grades, announcements, and course materials will be posted there. Check it regularly. Some instructors also maintain separate course websites with readings or supplementary material; check the syllabus for links.

**RateMyProfessors is useful but requires context.** Sample sizes vary enormously by professor — some have 200+ reviews (Guohui Lin), others have 5. A low rating sometimes reflects a genuinely poor teaching experience; sometimes it reflects a hard course. Check the [Professor Guide](../courses/professor-guide.md) for synthesized RMP data alongside Reddit student perspectives before you register.

**Ask upperclassmen.** This is consistently more useful than any website. If you're in the CSC lounge or the Discord, ask which sections of a course are better, which TAs are most helpful, which profs are clearest. Students who went through the courses recently have better signal than a 4-year-old anonymous review.

---

## Grades, Scholarships, and the Jason Lang

Your first-year grades matter more than you might expect — not because employers will scrutinize your first-year GPA, but because of scholarship eligibility.

**The Jason Lang Scholarship** is a provincial scholarship available to Alberta students continuing post-secondary education. To maintain eligibility, you need approximately a **3.2 GPA or higher**. The exact cutoff varies, so check the current Alberta Student Aid criteria, but this is roughly the threshold. At UofA, 3.2 on a 4-point scale is a B+ average.

Losing scholarship money because of a bad first semester — especially when the courses are genuinely manageable — is an entirely preventable outcome. Stay on top of your coursework.

More broadly: building good study habits in first year makes every subsequent year easier. The students who develop solid work habits — starting assignments early, attending office hours, reviewing material before exams — consistently outperform their raw ability in the long run.

---

## Getting Involved Beyond Coursework

First year is not too early to start building the things that matter for your career.

**Hackathons** — Events like HackED (UofA's annual hackathon) run during the school year and are excellent. You build something in 24-36 hours, meet people from all years, and often end up with a project you can put on your resume. Go, even if you think you're not ready. Everyone builds something scrappy at hackathons; the point is to build and learn, not to ship a polished product.

**CS Clubs and Student Organizations** — The CS student community at UofA has clubs focused on competitive programming, AI/ML, game development, and more. Getting involved in clubs is a natural way to meet people with similar interests and get exposure to areas of CS outside the curriculum.

**Research Curiosity** — If you find yourself genuinely interested in a research area after a course, don't wait until third year to do something about it. Professors post about research opportunities; some are open to taking motivated undergrads early. Even just reading papers in an area you find interesting puts you ahead of your peers. UofA has strong research groups in AI, HCI, systems, and theory — these are legitimate research opportunities that can lead to grad school, publications, or just a much deeper understanding of CS than coursework alone provides.

---

## Real Student Perspectives on First Year

These are the patterns students on r/uAlberta consistently report:

**"First year midterms hit differently"**
Many first-year posts each semester follow the same arc: "I did fine in high school, I understood 174, but my first midterms were lower than expected." University grading is harder, the curve isn't as forgiving, and the speed is faster. This doesn't mean you're failing — it means calibrate early. One Reddit user advised incoming students: "Frosh get pretty damn surprised by that first bunch of midterms. If 174 turns out to be easy-peasy, take the win and enjoy the GPA boost. I guarantee you will want that boost when reality sets in."

**On skipping ahead**
If you have prior experience and consider skipping 174 to go straight to 175: it's technically possible in some cases but the advice is mixed. Students with strong backgrounds who took 174 say: "Use the extra time to build side projects. That's what gets you far." Students who skipped 174 and went to 175 sometimes found the assumed background knowledge more demanding than expected.

**On course load**
A common first-year question: "Is taking 174, MATH 114, MATH 125, and STAT 151 too much?" The consensus answer: that's manageable if you stay on top of it. The load that kills students is adding a hard CMPUT course (like 201 or 229) to an already full math slate. Don't do 201 in your first semester. MATH 125 (Linear Algebra) is more important to do early than most students realize — it's a prerequisite for 204, 267, and all the ML courses.

**On professors**
The difference between a good and a bad professor in 174/175 is larger than in many other courses, because these courses require active engagement to build programming intuition. A boring lecture in a history class is recoverable. A boring lecture in a programming course where you needed to see the code-writing thought process modeled is harder to recover from.

**On mental health**
This comes up in the community more than you'd expect. University transitions are hard regardless of academic preparation. "Look out for your mental health at uni. It can be pretty stressful in this madhouse." This is sincere advice, not filler. Connecting with people in your cohort, getting outside the apartment, and not treating every grade as an identity crisis are skills that matter as much as anything in the syllabus.

---

## The Real Goal of First Year

First year exists to build your foundation. The goal isn't a 4.0 GPA — though that's fine if you can manage it — and it isn't cramming as many hard courses as possible to prove something.

The goal is to emerge from first year with:
- Solid programming fundamentals you actually understand
- Math skills that won't embarrass you in upper-year courses
- Good work habits that scale as the difficulty increases
- At least a few people in your cohort you study with and learn from
- Some idea of what areas of CS interest you most

Get those things right and the rest of the degree takes care of itself. The students who hit the ground running in first year are the ones who end up with strong internships in third year and job offers before they graduate. It all connects — start well.
