# Math and Stats for CS

Every Major and Honors path needs Calculus I and II, linear algebra, and an intro stats course; Honors and both Options add a second stats course. Which versions you take matters more than it looks, because some upper-year CMPUT courses only accept certain ones.

Requirements below are from the [2026-27 Computing Science subject area](https://calendar.ualberta.ca/preview_program.php?catoid=69&poid=110935); course details are from the [MATH](https://apps.ualberta.ca/catalogue/course/math) and [STAT](https://apps.ualberta.ca/catalogue/course/stat) catalogues.

---

## What Each Path Requires

| | Calculus I | Calculus II | Linear algebra | Intro stats | Second stats |
|---|---|---|---|---|---|
| **Major** (incl. AI and Software Practice Options) | MATH 134, 144, or 154 | MATH 136, 146, or 156 | MATH 125 | STAT 151, 235, or 265 | AI and SPO only: STAT 252 or 266 |
| **Honors** (all three versions) | MATH 117, 134, 144, or 154 | MATH 118, 136, 146, or 156 | MATH 125 or 127 | STAT 151, 235, or 265 | STAT 252 or 266 |
| **Minor** | None listed | None listed | None listed | None listed | None |

**MATH 114 is not on any CS list**, and the catalogue shows no scheduled offerings of it since Fall 2022 ([MATH 114](https://apps.ualberta.ca/catalogue/course/math/114)). Older advice that mentions it is out of date.

**Major students and the Honors courses:** the Major lists don't include MATH 117, 118, or 127. If you're in the Major and want to take them, confirm with CS advising ([csugrad@ualberta.ca](mailto:csugrad@ualberta.ca)) that they'll count before you register.

---

## Calculus

| Course | Term | Notes |
|---|---|---|
| [MATH 134](https://apps.ualberta.ca/catalogue/course/math/134) / [136](https://apps.ualberta.ca/catalogue/course/math/136) | 134 Fall, Winter, Spring/Summer; 136 Winter only | Life Sciences context. 136 includes differential equations and modelling. |
| [MATH 144](https://apps.ualberta.ca/catalogue/course/math/144) / [146](https://apps.ualberta.ca/catalogue/course/math/146) | Fall, Winter, Spring/Summer | Mathematical and Physical Sciences context. 144 adds Taylor polynomials. |
| [MATH 154](https://apps.ualberta.ca/catalogue/course/math/154) / [156](https://apps.ualberta.ca/catalogue/course/math/156) | Fall, Winter, Spring/Summer | Business and Economics context. 156 adds multivariate optimization and probability. |
| [MATH 117](https://apps.ualberta.ca/catalogue/course/math/117) / [118](https://apps.ualberta.ca/catalogue/course/math/118) (Honors) | 117 Fall only; 118 Winter only | 4 hours/week of lecture. 117 needs Math 30-1 **and Math 31** and is designed for students with 80%+ in both. 118 needs 117 (other calc I courses by department consent). |

You can only get credit for one Calculus I (MATH 100, 113, 114, 117, 134, 144, 154, SCI 100) and one Calculus II (MATH 101, 115, 118, 136, 146, 156, SCI 100). MATH 100 is restricted to Engineering students.

**Which to pick:** all of the regular options satisfy every CMPUT prerequisite, and any Calculus II leads to [MATH 214](https://apps.ualberta.ca/catalogue/course/math/214) (Calculus III). **144/146** is the natural default for CS since its applications are mathematical rather than biological or business. Take **117/118** only if you're in (or heading to) Honors, have Math 31, and want proof-heavier math.

## Linear Algebra

| Course | Term | Notes |
|---|---|---|
| [MATH 125](https://apps.ualberta.ca/catalogue/course/math/125) Linear Algebra I | Every term, incl. Spring/Summer | Systems, matrices, determinants, intro eigenvalues. Needs Math 30-1. |
| [MATH 127](https://apps.ualberta.ca/catalogue/course/math/127) Honors Linear Algebra I | Fall only | Adds abstract vector spaces, fields, and an intro to groups and rings. Honors lists only. |
| [MATH 225](https://apps.ualberta.ca/catalogue/course/math/225) Linear Algebra II | Every term | Inner product spaces, Gram-Schmidt, QR and least squares, diagonalization. Needs Calculus I and 125/127. |

Credit is allowed in only one of MATH 102, 125, 127. **Take linear algebra in first year**: it's a prerequisite or corequisite for six CMPUT courses (table below). MATH 225 isn't required by any CS path, but you need it (or 227) for CMPUT 340 and as a corequisite for STAT 266.

## Statistics

| Course | Prerequisites | Notes |
|---|---|---|
| [STAT 151](https://apps.ualberta.ca/catalogue/course/stat/151) Intro Applied Statistics I | Math 30-1 or 30-2 | The usual intro choice. Can't combine with 161 or 235. |
| [STAT 235](https://apps.ualberta.ca/catalogue/course/stat/235) Intro Statistics for Engineering | MATH 100; coreq MATH 101 | Intended for Engineering students (others get 3 units). |
| [STAT 265](https://apps.ualberta.ca/catalogue/course/stat/265) Probability and Statistics I | **Coreq MATH 209, 214, or 217** | Probability-first: combinatorics, Bayes, random variables, multivariate distributions. |
| [STAT 252](https://apps.ualberta.ca/catalogue/course/stat/252) Intro Applied Statistics II | STAT 141, 151, 161, 235, or SCI 151 | Regression, ANOVA, data analysis. |
| [STAT 266](https://apps.ualberta.ca/catalogue/course/stat/266) Probability and Statistics II | MATH 209/214/217 **and** STAT 265 (or 281); coreq MATH 225 or 227 | Sampling distributions, likelihood, estimation, hypothesis testing. |

**Which to pick:**

- **151 → 252** needs no extra math. It's the right default, especially for the plain Major (where you only need the intro course).
- **265 → 266** costs you MATH 214 (Calculus III) and MATH 225 on top, but gives you the probability foundation ML courses lean on, and **STAT 265 alone satisfies CMPUT 365's** "267, 466, or STAT 265" prerequisite. Worth it if you're doing the AI Option and like math; plan 214 in second year so 265 can go alongside it.

---

## Which CMPUT Courses Lean on Which Math

From each course's [catalogue entry](https://apps.ualberta.ca/catalogue/course/cmput). "Coreq" means it can be taken the same term.

| Math | CMPUT courses that require it |
|---|---|
| Calculus I | 204, 267, 328 |
| Calculus II | 466, 467 |
| Calculus III (MATH 209, 214, or 217) | 340 |
| Linear algebra I (MATH 102, 125, 126, or 127) | 267 (coreq), 304, 325, 328, 466, 474 |
| Linear algebra II (MATH 225 or 227) | 340 |
| Intro stats (STAT 151, 161, 181, 235, 265, SCI 151, or MATH 181) | 200, 261, 267 (coreq), 304, 313, 328, 340, 466 |
| STAT 265 | 365 (as an alternative to CMPUT 267 or 466) |

The ML sequence is the most math-hungry: **CMPUT 267** wants Calculus I done before it and linear algebra and stats done by the same term, and **466/467** add Calculus II. CMPUT 204 can't start until Calculus I is done, so don't defer it.

---

!!! note "Taken these? Help the next student."
    This page is official facts only. What it can't tell you: how 144 compares to 117 in practice, whether 127 is worth it over 125, how 265 feels without much calculus behind you, or which stats course actually helped in 267. If you've taken any of these, add your experience through the [course review form](https://github.com/uofa-cs/uofa-cs-wiki/issues/new?template=course-review.yml) and sign it with the term you took it (e.g. "took it F25").

<!-- Student experience notes go below this line, signed with the term taken. -->

---

*Last verified: October 2026 against the [2026-27 calendar](https://calendar.ualberta.ca/preview_program.php?catoid=69&poid=110935) and the [course catalogue](https://apps.ualberta.ca/catalogue/course/math).*
