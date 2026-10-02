# First Year Survival Guide

First year CS at UofA is where a lot of students either build good habits or fall into bad ones that take two years to undo. This guide is the advice you'd get from a senior student who actually made it through, not the sanitized version from an orientation pamphlet.

Let's be direct: first year is not that hard academically if you stay on top of it. The students who struggle aren't usually the ones who lack intelligence; they're the ones who underestimated how quickly things compound when you fall behind in a programming course.

---

## Your First Programming Courses: 174/175 vs 274/275

This is one of the first real decisions you make as a CS student.

### CMPUT 174 and 175 (Standard Stream)

This is the default entry point. Both courses use Python, which is the right language to start with; it's readable, the syntax doesn't fight you, and the ecosystem is enormous. 174 covers the basics: variables, control flow, functions, recursion. 175 goes further into object-oriented programming, data structures, and more complex problem-solving.

These are manageable courses if you engage consistently. The students who fail 174/175 are almost always students who skipped lectures, fell behind on assignments, and then tried to cram before exams. Programming doesn't work like that. You can't memorize your way through debugging a recursive function at 11pm the night before a deadline.

### CMPUT 274 and 275 (Accelerated Stream)

CMPUT 274 and 275 are **Accelerated Introduction to the Foundations of Computation I and II**. According to the catalogue, 274 covers procedural programming and basic algorithm design (lists, queues, trees, sorting, searching) in **Python, developed on Linux**, and 275 adds object-oriented programming in **C++** along with more complex algorithms such as shortest paths, divide and conquer, and dynamic programming ([CMPUT 274](https://apps.ualberta.ca/catalogue/course/cmput/274), [CMPUT 275](https://apps.ualberta.ca/catalogue/course/cmput/275)). Both are taught studio-style: lectures and labs blended into 3-hour sessions, twice a week, with limited enrollment. The catalogue strongly recommends Python or prior computing background for 274. There's no hardware component in the current course descriptions.

The tradeoff: it's faster and more intense. Student opinion on r/uAlberta is genuinely divided. A student with prior experience said: "274/275 wasn't hard, I got an A in both. The content is much more important than 174/175." But a student without prior experience said: "274/275 are the worst designed classes I've ever taken. You put in 20 hours per week in just one class. Everything is insanely crammed in."

**The honest community consensus:** 274/275 works well for students with solid prior programming experience. For students entering with limited background, the pace is brutal and the GPA damage is real.

**Know the credit rules before you pick:** you can't get credit for both 274 and 174 or 175, or for both 275 and 175. You also **can't get credit for both 275 and 201**, and the program calendar says students who take 275 must replace 201 with another CMPUT course at the 200-level or above ([calendar](https://calendar.ualberta.ca/preview_program.php?catoid=69&poid=110935)). In exchange, 275 satisfies the "201 or 275" prerequisite on courses like 229 and 301.

If you have real programming experience and want a faster, C++-flavoured intro: 274/275. If you want to protect your GPA in first year and have no strong background: 174/175, and use the extra time to build side projects.

Both paths work. Choose based on your honest self-assessment.

---

## Math: Don't Blow It Off

CS students sometimes treat math as an obstacle rather than a tool. That's a mistake. Here's what you're looking at in first year:

**Calculus I and II (MATH 134/144/154, then MATH 136/146/156)**
These are the calculus options the program lists; Honors students can also take MATH 117/118 (Honors Calculus I and II) ([calendar](https://calendar.ualberta.ca/preview_program.php?catoid=69&poid=110935)). Calculus I is a prerequisite for CMPUT 204, so take it in your first semester. If you took calculus in high school, the first course will feel familiar. Don't get complacent; university grading is different from high school, and the pace is faster. Do the problem sets. Calculus II is where students who coasted sometimes hit a wall. Keep up with the material weekly.

**MATH 125: Linear Algebra I** (or MATH 127, Honors Linear Algebra I, for Honors students)
Take this in first year. Linear algebra is the math that directly powers machine learning, computer graphics, and a lot of scientific computing. It's a prerequisite or corequisite for CMPUT 267, 304, 325, and 466. Students who defer it end up taking ML courses without the proper mathematical grounding.

**Intro stats (STAT 151, 235, or 265)**
Statistics is more useful than most CS students realize until they're in industry or doing ML work. Every CS path requires an intro stats course, and it's a prerequisite for CMPUT 200, 261, 304, and 313. Take it in first year. Honors and the AI and Software Practice Options also require a second course (STAT 252 or 266); don't leave it for later.

---

## How to Not Fail: The Basics That Aren't Obvious

**Don't skip lectures in 174/175.** Programming courses are taught with a specific pedagogy; each lecture builds on the previous one. If you miss two lectures and don't read the slides and test the code yourself, you will not be able to figure out the assignment. This is not like a history course where you can read the textbook later. The compounding is real.

**Do the assignments yourself.** Not because of academic integrity concerns (though those exist), but because the act of struggling through a problem and actually solving it is how you learn to program. Students who copy or over-collaborate end up failing practical assessments and interviews because they never built the actual skill. Do the work.

**Start assignments early.** This is the most repeated advice in university and the most ignored. Programming assignments take twice as long as you estimate, especially when you hit a bug you don't understand. Start with enough time to get stuck, ask for help, and still finish before the deadline.

**Office hours are not just for when you're failing.** TAs and professors at UofA are generally accessible and more helpful than you expect. Going to office hours when you're confused is table stakes. Going to office hours to discuss interesting problems or follow up on lecture topics is how you start building relationships with faculty, which matters if you ever want a reference letter or a research opportunity.

---

## Finding Your People: Study Groups and Community

University is social in ways that high school wasn't. The people you study with in first year often become your professional network, your collaborators, and your friends for the next decade.

**Form study groups early.** Your lab sections are a natural place to find people; you're all working through the same problems. Introduce yourself. Ask someone if they want to compare approaches to an assignment. It's less awkward than it sounds.

**The CS Discord servers:** there are student-run Discord communities for UofA CS. Ask around in your courses or look for them posted on Canvas. These are genuinely useful for quick questions, course-specific channels, and finding people to study with.

**UACS (Undergraduate Association of Computing Science):** UACS is the CS undergraduate student association. Its office is CSC 1-40, and it runs things like lab intros at the start of the year and tutor connections ([department student groups page](https://www.ualberta.ca/en/computing-science/resources/student-groups.html), [uacs.ca](https://uacs.ca)). Getting involved is one of the better ways to become a regular part of the CS student community and meet upper-year students who'll share course tips and point you toward opportunities.

---

## Setting Up Your Environment: Do This Right From Day One

**Do not use IDLE for CMPUT 174.** IDLE is Python's built-in editor and it is completely adequate for toy scripts and nothing else. Get a real IDE from the start. VS Code is the standard recommendation; it's free, extensible, supports every language you'll encounter, and has excellent Python support. PyCharm is another good option for Python specifically.

Getting comfortable with a proper development environment in first year pays off for every year after. Setting up syntax highlighting, a debugger, and a terminal you understand makes everything faster and less frustrating.

**Start using version control immediately.** This means Git. Even for first-year assignments. Get a GitHub account, initialize a repo for each course (keep them private if your department requires it), and commit your work regularly. You will not regret this habit. The students who learn Git properly in first year have a real advantage; it comes up in every internship application and every technical interview eventually. The students who learn it properly in third year wish they'd learned it in first year.

You don't need to master Git immediately. Learn `git init`, `git add`, `git commit`, `git push`, and `git status`. That's enough to get started.

---

## Navigating Course Information

**Canvas is the official LMS:** your assignments, grades, announcements, and course materials will be posted there. Check it regularly. Some instructors also maintain separate course websites with readings or supplementary material; check the syllabus for links.

**Ask upper-years.** This is consistently more useful than any website. In UACS, a club, or the Discord, ask how a course is run, what the workload looks like, and which TAs are most helpful. Students who went through a course recently have better signal than a four-year-old anonymous review.

**Check who's teaching.** The [course catalogue](https://apps.ualberta.ca/catalogue/course/cmput) shows scheduled sections and instructors for upcoming terms. Courses can change a lot depending on how they're run in a given term, so look at the current offering, not what someone remembers from years ago.

**Treat RateMyProfessors with skepticism.** Sample sizes are often tiny, reviews skew toward people who had a very good or very bad time, and a hard course often gets reviewed as a "bad professor." Use it as one weak signal at most.

---

## Grades, Scholarships, and the Jason Lang

Your first-year grades matter more than you might expect, not because employers will scrutinize your first-year GPA, but because of scholarship eligibility.

**The Jason Lang Scholarship** is a provincial scholarship available to Alberta students continuing post-secondary education. As of **August 1, 2025**, the required GPA was increased to **3.5 on a 4.0 scale** for eligible students taking at least an 80% course load in the previous fall and winter terms. Previously, the cutoff was **3.2**, so this is meaningfully more competitive now. At UofA, 3.5 is roughly an A- average, so this is no longer a "decent grades" scholarship.

Losing scholarship money because of a bad first semester (especially when the courses are genuinely manageable) is an entirely preventable outcome. Stay on top of your coursework.

More broadly: building good study habits in first year makes every subsequent year easier. The students who develop solid work habits (starting assignments early, attending office hours, reviewing material before exams) consistently outperform their raw ability in the long run.

---

## Getting Involved Beyond Coursework

First year is not too early to start building the things that matter for your career.

**Hackathons:** Events like [HackED](https://hacked-2026.devpost.com/), the annual hackathon run by the University of Alberta Computer Engineering Club, run during the school year and are excellent. You build something over a weekend, meet people from all years, and often end up with a project you can put on your resume. Go, even if you think you're not ready. Everyone builds something scrappy at hackathons; the point is to build and learn, not to ship a polished product.

**CS Clubs and Student Organizations:** Besides UACS, the department lists groups like Ada's Team (diversity in computing) and a Programming Club for contests ([student groups](https://www.ualberta.ca/en/computing-science/resources/student-groups.html)), and the Students' Union has hundreds more. Getting involved in clubs is a natural way to meet people with similar interests and get exposure to areas of CS outside the curriculum.

**Research Curiosity:** If you find yourself genuinely interested in a research area after a course, don't wait until third year to do something about it. Professors post about research opportunities; some are open to taking motivated undergrads early. Even just reading papers in an area you find interesting puts you ahead of your peers. UofA has strong research groups in AI, HCI, systems, and theory; these are legitimate research opportunities that can lead to grad school, publications, or just a much deeper understanding of CS than coursework alone provides.

---

## Real Student Perspectives on First Year

These are the patterns students on r/uAlberta consistently report:

**"First year midterms hit differently"**
Many first-year posts each semester follow the same arc: "I did fine in high school, I understood 174, but my first midterms were lower than expected." University grading is harder, the curve isn't as forgiving, and the speed is faster. This doesn't mean you're failing; it means calibrate early. One Reddit user advised incoming students: "Frosh get pretty damn surprised by that first bunch of midterms. If 174 turns out to be easy-peasy, take the win and enjoy the GPA boost. I guarantee you will want that boost when reality sets in."

**On skipping ahead**
If you have prior experience and consider skipping 174 to go straight to 175: it's technically possible in some cases but the advice is mixed. Students with strong backgrounds who took 174 say: "Use the extra time to build side projects. That's what gets you far." Students who skipped 174 and went to 175 sometimes found the assumed background knowledge more demanding than expected.

**On course load**
A common first-year question: "Is taking 174, Calculus I, MATH 125, and STAT 151 too much?" The consensus answer: that's manageable if you stay on top of it. You can't take 201 in your first semester anyway (it requires 175), and 229 requires 201. MATH 125 (Linear Algebra) is more important to do early than most students realize; it feeds into 267, 304, and the ML courses. For 204, what you need is 175, 272, and Calculus I.

**On engagement**
Intro programming courses reward active engagement more than most. Watching someone write code in lecture is not the same as writing it yourself; type along, re-run the examples, and break them on purpose.

**On mental health**
This comes up in the community more than you'd expect. University transitions are hard regardless of academic preparation. "Look out for your mental health at uni. It can be pretty stressful in this madhouse." This is sincere advice, not filler. Connecting with people in your cohort, getting outside the apartment, and not treating every grade as an identity crisis are skills that matter as much as anything in the syllabus.

---

## The Real Goal of First Year

First year exists to build your foundation. The goal isn't a 4.0 GPA (though that's fine if you can manage it), and it isn't cramming as many hard courses as possible to prove something.

The goal is to emerge from first year with:
- Solid programming fundamentals you actually understand
- Math skills that won't embarrass you in upper-year courses
- Good work habits that scale as the difficulty increases
- At least a few people in your cohort you study with and learn from
- Some idea of what areas of CS interest you most

Get those things right and the rest of the degree takes care of itself. The students who hit the ground running in first year are the ones who end up with strong internships in third year and job offers before they graduate. It all connects, so start well.
