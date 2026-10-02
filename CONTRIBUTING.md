# Contributing to the UAlberta CS Wiki

This wiki exists so the next UofA CS student doesn't have to learn everything the hard way. If something here helped you, the best way to pay it forward is to add what you know.

You don't need to be an expert or know git. You just need to have been there.

---

## The One Rule

**Write what a student can't get by asking a chatbot.**

Generic advice ("start assignments early", "learn Docker", "use STAR for behavioural interviews") is a search or a prompt away, and an AI can write it better than we can. What nobody else has is UofA-specific, first-hand, current knowledge: what 201's in-class coding exercises are actually like, how the SIP portal works in practice, what Jobber's intern interview looked like last fall. That's what belongs here.

---

## Three Ways to Contribute

### 1. Fill out a form (no git needed)

The quickest way to help. Open an issue using one of the forms and a maintainer will turn it into a page:

- [**Course review**](https://github.com/uofa-cs/uofa-cs-wiki/issues/new?template=course-review.yml): share your experience with a course you've taken
- [**Internship write-up**](https://github.com/uofa-cs/uofa-cs-wiki/issues/new?template=internship-writeup.yml): how you got an internship and what it was like
- [**Correction**](https://github.com/uofa-cs/uofa-cs-wiki/issues/new?template=correction.yml): something on the wiki is wrong or out of date

### 2. Edit a page directly

Every page on the site has an edit button that opens the file on GitHub. Make your change and GitHub will walk you through opening a pull request. This is perfect for corrections and adding a tip to an existing course review.

### 3. Open a pull request

For bigger changes:

1. Fork the repository and create a branch with a descriptive name (`update-cmput-379-review`, `add-jobber-internship`).
2. Make your changes. For new pages, start from a template in [`templates/`](https://github.com/uofa-cs/uofa-cs-wiki/tree/main/templates).
3. Open a pull request against `main`. The checklist in the PR description will remind you of the essentials.

For entirely new pages or structural changes, open an issue first so we can agree on scope before you put in the work.

---

## Sourcing Rules

Most of the errors we've had to fix were confident, specific claims with nothing behind them. To keep that from happening again:

**Facts need a source link.** Course titles, prerequisites, degree requirements, scholarship amounts, deadlines, program rules, and company details must link to where they come from. Prefer official sources: the [Academic Calendar](https://calendar.ualberta.ca/), the [course catalogue](https://apps.ualberta.ca/catalogue/course/cmput), Registrar and department pages, company career pages.

**Experience needs a when.** First-hand accounts are the most valuable thing on this wiki, but they age. Sign them with the term: "(took it W26)", "(interned Summer 2025)". Readers can then decide how much weight to give them.

**Time-sensitive pages get a `Last verified` line.** If you check a page's facts against their sources, update the date.

**If you can't verify it, leave it out.** A missing fact is better than a wrong one. Don't fill gaps with plausible guesses, and never let an AI tool fill them for you.

---

## Writing About Instructors

**We don't rank professors.** No tier lists, no "avoid" lists, no RateMyProfessors scores.

You *can* describe how a section was run, so students can pick the style that suits them:

- Good: "In W26, Tang's section had weekly quizzes and posted full typed notes. The curve was stricter than other sections."
- Not okay: "Worst prof in the department, avoid at all costs."

Stick to things a student can act on: notes, assessment format, pacing, availability, recorded lectures. Leave out personal characteristics (accent, appearance, personality) entirely.

---

## Using AI Tools

AI tools are fine for checking grammar, restructuring a draft, or formatting a table. They are not a source. Every fact you submit must come from an official page or your own experience, and every opinion must be yours. If you used AI to help edit, you're still responsible for every claim in the PR.

---

## What Not to Contribute

- **Personal attacks** on professors, TAs, students, or companies. Critique courses, workloads, and processes, not people.
- **Confidential information.** Don't reproduce verbatim interview questions, anything covered by an NDA, or internal company information. "Their phone screen focused on graphs" is fine; the exact question isn't.
- **Course materials.** Don't post assignments, exam questions, or solutions.
- **Undisclosed promotion.** If you're affiliated with a resource you're adding, say so in the PR. We'll only include it if it fills a real gap.
- **Generic filler.** If the paragraph would be equally true at any university, link to a good external resource instead.

---

## Tone

**Be specific.** "291's project has you build a Python + SQLite app and then a MongoDB one" beats "databases are important."

**Be honest and fair.** Don't oversell or undersell UofA, Edmonton, or the job market. If something is mediocre, say so. If something is great, say that too.

**Write to the reader.** Use "you". This is a guide, not an encyclopedia.

**Commit to a recommendation when you can.** If it depends, say what it depends on and what you'd do in the common case.

**Keep it short.** Students skim. Cut anything that doesn't change what the reader will do.

---

## Style and Structure

- **Where pages go:** in the matching folder under `docs/`. Not sure? Ask in an issue.
- **Navigation:** add new pages to [`nav.yml`](https://github.com/uofa-cs/uofa-cs-wiki/blob/main/nav.yml) and to the table of contents in `README.md`.
- **Headings:** one H1 (`#`) per page for the title, H2 for sections, H3 for subsections.
- **File names:** lowercase with hyphens (`edmonton-tech-scene.md`).
- **Links:** relative links between wiki pages (`../courses/course-reviews.md`), full URLs for everything else.
- **Punctuation:** avoid em dashes; use a colon, semicolon, comma, or parentheses instead.

Every pull request is built automatically. If the build fails, it's usually a broken link; the check's log will name the file.

---

## Thank You

Every section here exists because a student sat down and wrote what they knew. If you just finished CMPUT 174 and have thoughts about what would have helped, that's worth writing down. Every year of the degree needs people willing to speak from where they are.

*Questions? [Open an issue](https://github.com/uofa-cs/uofa-cs-wiki/issues).*
