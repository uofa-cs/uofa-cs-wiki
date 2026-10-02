# Degree Planning for BSc CS

Finishing your CS degree efficiently, without sacrificing your GPA, your sanity, or the courses that actually matter, requires planning from the start. This guide is written around the plain Major in Computing Science. If you're in Honors, the AI Option, or the Software Practice Option, the same prerequisite chains apply but you have more required courses; see the [Program Overview](./program-overview.md) and the [calendar](https://calendar.ualberta.ca/preview_program.php?catoid=69&poid=110935).

The single biggest mistake first-year students make is not understanding prerequisite chains early enough. Miss the right course in first semester and you're pushing senior courses into a fifth year. This guide exists to stop that from happening to you.

---

## How to Use BearTracks Effectively

BearTracks is UofA's student portal for registration, grades, and degree auditing. Learn it early.

**The Audit Tool** is one of the most useful features most students ignore. It shows exactly which requirements you've completed, which are in progress, and which you still need. Run it every semester before registration opens. Don't wait for your advisor to tell you what you need; you should already know.

**Add/Drop Deadlines:** There are two that matter. The early withdrawal deadline (usually around week 2) lets you drop a course with no record of it. The late withdrawal deadline (usually around week 6-8) lets you drop with a "W" on your transcript, visible, but not counted against your GPA. After that deadline, you're stuck with whatever grade you get. Mark both dates in your calendar the moment each semester starts.

**Waitlists:** Popular courses fill fast. Get on waitlists for courses you need as early as possible during your registration window. Check BearTracks regularly when classes start; students drop, and spots open up in the first two weeks. If you're stuck on a waitlist for a course you genuinely need, email the instructor. It sometimes works.

**Registration Windows:** Your window opens based on your credit count. This creates a real advantage for students who are further along. In your first year, you register last and courses fill up. This is normal. It also means your first-year course selection is somewhat constrained by availability, so know your backup options.

---

## Prerequisite Chains: The Critical Paths

Get these wrong and you will lose semesters. Memorize them.

Prerequisites below are from the [course catalogue](https://apps.ualberta.ca/catalogue/course/cmput) as of October 2026. Always re-check the catalogue entry for a course before you register; they do change.

### The Core CS Chain: 174 → 175 → 201, and 272 → 204
CMPUT 174 and 175 are the intro sequence (Python). 201 (Practical Programming Methodology) is C and Unix development tools, and requires 175. 204 (Algorithms I) is one of the most important courses in the degree.

**204 has three prerequisites, not one:** CMPUT 175 (or 275), **and** CMPUT 272, **and** a first-semester calculus course (one of MATH 100, 114, 117, 134, 144, or 154) ([CMPUT 204](https://apps.ualberta.ca/catalogue/course/cmput/204)). Students who leave 272 to "later" are the ones who end up pushing 204, and everything behind it, back a year.

**Start this chain in your very first semester.** 204 is a prerequisite for a large share of upper-year courses (304, 313, 325, 350, 366, 379, 403, and more). If you have programming experience and want to skip 174, verify with the department before assuming you can.

### Logic: 174 → 272
CMPUT 272 (Formal Systems and Logic in Computing Science) only needs an intro course (174, 175, 274, or a couple of others) ([CMPUT 272](https://apps.ualberta.ca/catalogue/course/cmput/272)), so you can take it as early as your second term. It is a prerequisite for 204, 291, 331, and 366. Don't sleep on this one; it's a different style of thinking from intro programming and students who aren't prepared struggle with it.

### Systems: 201 → 229 → 379
CMPUT 229 (Computer Organization and Architecture I) requires **201** (or 275) ([CMPUT 229](https://apps.ualberta.ca/catalogue/course/cmput/229)), so you cannot take it alongside 201 in the same term. It introduces assembly, memory, and how computers actually work at a low level. 379 (Operating System Concepts) needs 201 and 204 (or 275) **and** 229 ([CMPUT 379](https://apps.ualberta.ca/catalogue/course/cmput/379)). CMPUT 313 (Computer Networks) lists 379 as a corequisite, so plan 379 no later than the term you take 313.

### Databases: 272 + 175 → 291
CMPUT 291 (Introduction to File and Database Management) needs 175 (or 274) and 272, with 201 (or 275) as a corequisite ([CMPUT 291](https://apps.ualberta.ca/catalogue/course/cmput/291)). The DB material is underrated; understanding databases is practically mandatory for any full-stack or backend role.

**About CMPUT 391 (Database Management Systems):** it is still in the calendar, but the catalogue shows no scheduled offerings and its most recent listed term is Winter 2022 ([CMPUT 391](https://apps.ualberta.ca/catalogue/course/cmput/391)). Don't build a plan that depends on it. If you want more hands-on database work, CMPUT 404 (Web Applications and Architecture, needs 291 and 301) is the more realistic option.

### Software Engineering: 201 → 301 → 401/402, and 291 + 301 → 404
CMPUT 301 needs 201 (or 275). 401 (Software Process and Product Management) and 402 (Software Quality) both need 301, and 404 needs 291 and 301 ([catalogue](https://apps.ualberta.ca/catalogue/course/cmput)).

### The Accelerated Sequence: 274 → 275 (Optional)
Instead of 174/175, you can enter through CMPUT 274/275, **Accelerated Introduction to the Foundations of Computation I and II**. Per the catalogue, 274 is procedural programming and basic algorithms in **Python, developed on Linux**, and 275 adds object-oriented programming in **C++** plus more complex algorithms (shortest paths, divide and conquer, dynamic programming) ([CMPUT 274](https://apps.ualberta.ca/catalogue/course/cmput/274), [CMPUT 275](https://apps.ualberta.ca/catalogue/course/cmput/275)). Both are taught studio-style (3-hour combined lecture/lab sessions, twice a week) with limited enrollment, and prior Python or computing background is strongly recommended. There's no hardware component in the current descriptions.

**Credit matters here:** you can't get credit for both 274 and 174 or 175, or for both 275 and 175. You also **can't get credit for both 275 and 201**. The program calendar says students who take 275 must replace 201 with another CMPUT course at the 200-level or above ([calendar](https://calendar.ualberta.ca/preview_program.php?catoid=69&poid=110935)). The upside is that 275 satisfies the "201 or 275" prerequisite on courses like 229, 301, and 379, and the "201 and 204, or 275" prerequisite on several 300-level courses.

---

## Math and Stats Requirements

Don't neglect these. They come back in upper-year CS more than students expect.

**Calculus I (MATH 134, 144, or 154):** Take one of these in your first semester. Honors students can also use MATH 117 (Honors Calculus I). A first-semester calculus course is a prerequisite for CMPUT 204, so this is not optional or deferrable. MATH 114 is not one of the program's listed calculus options; check the [calendar](https://calendar.ualberta.ca/preview_program.php?catoid=69&poid=110935) before taking anything else.

**Calculus II (MATH 136, 146, or 156):** Usually taken in second semester. Honors students can also use MATH 118 (Honors Calculus II). Calculus II shows up as a prerequisite for CMPUT 466 and 467.

**Linear Algebra (MATH 125, or MATH 127 for Honors):** The Major requires MATH 125; Honors accepts MATH 125 or 127 (Honors Linear Algebra I). It's the most practically useful math course for ML, graphics, or scientific computing, and it's a listed prerequisite or corequisite for CMPUT 267, 304, 325, and 466. Take it in first year.

**Intro stats (STAT 151, 235, or 265):** Required in every path. Take it in first year: an intro stats course is a prerequisite for CMPUT 200, 261, 304, 313, and 466, and a corequisite for 267.

**Second stats course (STAT 252 or 266):** Required for Honors and for the AI and Software Practice Options (not the plain Major). Aim to finish it by second year.

---

## Summer Courses: Getting Ahead

Summer is underutilized by most students. It's one of the best ways to accelerate your degree or lighten your fall/winter load.

UofA runs two summer sessions. Not every course is offered in summer, but some key ones are. Check the summer timetable each year; offerings change. Courses that tend to run in summer: some 200-level CS courses, math requirements, and certain science electives.

Taking one or two courses in summer can let you shave a semester off your degree timeline, or give you breathing room to take on an internship during a regular semester without overloading. If you're aiming for a 3-year completion, summer courses are basically mandatory.

Summer courses are faster-paced: a full semester of content in 6 weeks. They require focus, but if you're not also working full-time, they're very manageable.

---

## Course Load: How Many Is Too Many?

**Five courses per semester** is the standard full-time load. This is the pace that a standard 4-year plan assumes. Most students handle 5 courses without too much trouble once they're past first year.

**Six courses** counts as overload and requires approval from the faculty to grant it. It is doable but requires real discipline. The key is not stacking six hard courses together. If you're taking 6, make sure at least one or two are lighter (a breadth elective, a lab course, something you find genuinely easy). Students have finished in three years this way, using overload terms plus summers; it works, but you have to be strategic and willing to put in the hours.

**Do not take six of the hardest CS courses simultaneously.** Stacking 204, 229, 291, and 301 in the same semester with no breathing room is a recipe for a rough GPA and a miserable few months. Spread the challenging courses out.

**Four courses** sometimes makes sense: if you're doing a heavy internship alongside school, if you've had a rough semester and need to recover your GPA, or if you're doing significant research. Don't treat 4-course semesters as failure; treat them as tactical decisions.

---

## Senior Courses to Save for Later

Some courses have soft prerequisites that aren't captured in BearTracks; they assume a level of CS maturity that you genuinely won't have in first or second year, even if you technically meet the listed prerequisites. That said, once you are ready for them, you should take these as soon as possible because most internships and companies expect this knowledge in practice, not just theory.

Save these for third and fourth year if you need the extra time, but do not delay them longer than necessary:

- **CMPUT 301 (Software Engineering):** Group project-heavy. More valuable when you've done some real programming, but still worth taking as soon as you can because it helps you learn how real team projects work.
- **CMPUT 401 (Software Process and Product Management):** Requires 301. Makes more sense once you understand the technical landscape, and it is useful for seeing how software work connects to industry.
- **CMPUT 404 (Web Applications and Architecture):** Requires 291 and 301. Useful course, but you'll get more from it once you've built things on your own. It is especially valuable for learning practical tools and frameworks.
- **CMPUT 403 (Algorithmics in Competitive Programming):** Requires 201 (or 275), 204, and any 300-level CMPUT course. You can't get credit for both 403 and 303 (Algorithmics in Practice).

Many students reach these courses having only done theory-heavy first- and second-year classes and still do not know how to use common tools like Git, Linux, frameworks, or Python virtual environments. If that sounds like you, these courses and the projects they force you to do become even more important. If you are already building projects outside school, you may be better prepared earlier; if not, take these courses as soon as you can handle the prerequisites.

---

## Sample Semester-by-Semester Plans

**These are illustrative only.** Every course below is placed after its catalogue prerequisites as of October 2026, but offerings change term to term, some courses only run in one term, and your path (Honors, AI Option, Software Practice Option, 274/275 entry) changes what you need. Check each course against the [catalogue](https://apps.ualberta.ca/catalogue/course/cmput) and your degree audit before registering.

### Sample 4-Year Plan (Major in Computing Science)

| Term | Courses |
|------|---------|
| Year 1 Fall | CMPUT 174, MATH 134/144/154, + 3 courses (e.g., ENGL/WRS, science, breadth) |
| Year 1 Winter | CMPUT 175, MATH 136/146/156, MATH 125, STAT 151, + 1 course |
| Year 2 Fall | CMPUT 201, CMPUT 272, CMPUT 200, + 2 courses |
| Year 2 Winter | CMPUT 204, CMPUT 229, CMPUT 291, + 2 courses |
| Year 3 Fall | CMPUT 301, CMPUT 379, + 3 courses |
| Year 3 Winter | CMPUT 304, CMPUT 313, + 3 courses |
| Year 4 Fall | CMPUT 401, CMPUT 403, + 3 courses |
| Year 4 Winter | CMPUT 404, + 4 courses |

Why it's ordered this way: 272 comes before 204; 201 comes before 229; 175 and 272 come before 291 (with 201 already done); 201, 204, and 229 come before 379; 379 is taken before (or with) 313; 301 comes before 401; 291 and 301 come before 404; and 403 comes after a 300-level CMPUT course. The plain Major only requires two of 201/229/291, but taking all three keeps the most upper-year doors open.

### Sample Accelerated 3-Year Plan

The 3-year path requires running 6 courses in some semesters and using spring/summer. It only works if the courses you need are actually offered in spring/summer that year, so check the timetable before committing.

| Term | Courses |
|------|---------|
| Year 1 Fall | CMPUT 174, MATH 134/144/154, + 4 courses (6 total) |
| Year 1 Winter | CMPUT 175, MATH 136/146/156, MATH 125, STAT 151, + 2 courses (6 total) |
| Year 1 Spring/Summer | CMPUT 201 and CMPUT 272 if offered, + 1 light course |
| Year 2 Fall | CMPUT 204, CMPUT 229, CMPUT 291, CMPUT 200, + 2 courses |
| Year 2 Winter | CMPUT 301, CMPUT 379, CMPUT 304, + 3 courses |
| Year 2 Spring/Summer | 1-2 courses or an internship |
| Year 3 Fall | CMPUT 313, CMPUT 401, CMPUT 403, + 3 courses |
| Year 3 Winter | CMPUT 404, + remaining requirements |

This requires sustained effort and good time management. The benefit isn't just finishing faster; it's getting to industry sooner, compressing your tuition costs, and having a year of industry experience while your peers are still in school.

---

## A Note on Advising

The CS department has academic advisors. Use them, especially for edge cases like transfer credits, course substitutions, or unusual paths. But don't wait for an advisor to tell you the plan. Come into every advising appointment knowing your degree audit cold, knowing which courses you need, and with specific questions. Advisors are most useful for resolving ambiguity, not for designing your entire plan from scratch.

The students who succeed at degree planning are the ones who take ownership of it from day one.
