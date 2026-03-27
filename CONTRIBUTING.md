# Contributing to the UAlberta CS Wiki

This wiki is a community effort. It exists because students took the time to write down what they knew, what they wished they'd known, and what they learned the hard way — so that the next person doesn't have to start from scratch. If you've been helped by something in here, the best way to pay it forward is to contribute something back.

You don't need to be an expert. You just need to have something useful to say.

---

## What to Contribute

**Corrections to outdated information** — This is the most valuable thing you can do. Professor names change, courses change format, companies open and close, salary ranges shift, application timelines move. If you notice something that's no longer accurate, fix it. Don't wait for someone else to do it.

**New sections or pages** — If a topic isn't covered and you have real knowledge of it, add it. Gaps in the wiki are opportunities. Check the table of contents in README.md to see what's missing, and check existing open issues to avoid duplicating work someone else has already started.

**Personal experiences** — Internship stories, course reviews, research experiences, and hiring process walkthroughs are some of the most useful things in this wiki. If you went through a process and came out the other side with knowledge, write it down. First-person accounts are especially valuable in sections like Internships, Career Paths, and Getting into Research.

**Fixing typos and formatting** — Small fixes are welcome. If a heading is off, a link is broken, or a sentence reads awkwardly, fix it. PRs for small corrections are fast to review and always appreciated.

---

## What NOT to Contribute

**Personal attacks on professors or companies** — You can say a course is tedious, a workload is unreasonable, or an interview process is poorly designed. You cannot personally attack an individual or make accusations that aren't substantiated. Be fair and constructive. The goal is to help students make informed decisions, not to settle scores.

**Politically charged content unrelated to CS careers** — This wiki is for CS students navigating their degree and career. It's not the right venue for general political commentary, even if it's something you care deeply about. Keep contributions focused on what's useful to students pursuing CS.

**Confidential information** — Do not include specific interview questions from company interviews (especially if you signed an NDA), internal company information that wasn't publicly shared, or anything that would violate an agreement you made. Writing that "Company X focuses heavily on dynamic programming in phone screens" based on your general impression is fine. Reproducing a verbatim interview question is not.

**Pure opinion without useful information** — "Python is the best language" isn't a contribution. "Python is the most common language for ML/AI roles in Edmonton, and most UofA ML research uses it, so it's a safe first priority if that's your direction" is. Root opinions in something specific and actionable for the reader.

---

## PR Guidelines

**How to submit changes:**

1. Fork the repository.
2. Create a new branch with a short descriptive name: `add-edmonton-salary-ranges`, `update-cmput403-section`, `fix-broken-links`.
3. Make your changes on that branch.
4. Open a pull request against `main` with a clear title and a brief description of what you changed and why.

**PR title format** — Be specific. Good examples:
- "Add 2024 Edmonton tech salary ranges to Career Paths"
- "Update CMPUT 403 section to reflect new project format"
- "Fix broken links in Learning Resources"
- "Add internship experience at Jobber (Summer 2024)"

Bad examples: "Update wiki", "Fix stuff", "Add info".

**Keep PRs focused** — One topic per PR. A PR that updates salary ranges, adds a new course review, and fixes three typos is harder to review than three separate PRs. If you have multiple unrelated changes, split them up.

**Discuss large additions first** — If you're planning to add an entirely new page or make significant structural changes, open an issue first to describe what you're thinking. This avoids situations where you put in a lot of work and then there's a disagreement about scope or framing. For small additions and corrections, just open the PR directly.

**Expect feedback** — Reviewers may ask you to adjust tone, add specifics, or restructure a section. This is normal. The goal is a consistent, high-quality wiki, not just getting words on a page.

---

## Tone Guide

Getting the tone right is the hardest part of contributing to a wiki like this. Here are the principles we aim for:

**Be opinionated but fair.** This wiki earns its value by actually committing to recommendations. You can say a course is tedious, a language isn't worth learning first, or a company has a reputation for long hours — as long as you're being fair and not gratuitously harsh. Hedge when genuine uncertainty exists, not as a way to avoid saying anything.

**Be specific.** "CMPUT 291 covers SQL (DDL and DML), ER diagrams, relational algebra, and basic query optimization, with a project that runs through the full database design lifecycle" is useful. "Databases are important for software development" is not. Specificity is what makes this wiki better than a generic CS career guide.

**Be practical.** Write advice you wish you had, not advice that sounds good in theory. "You should build a strong foundation in algorithms" is theory. "Do at least 100 LeetCode problems before applying to any company that does technical screens, and focus on arrays, trees, and graphs first because they account for the majority of what you'll see at the junior level" is practical.

**Be honest.** Don't oversell UofA, Edmonton, or the career prospects available here. Don't undersell them either. Students are making real decisions based on what this wiki says, and they deserve an accurate picture. If something is genuinely mediocre, say so. If something is genuinely great, say that too.

**Write directly to the reader.** Use "you" throughout. This is a guide, not an encyclopedia. "You'll want to start applying to internships in September for summer positions" reads better than "Students are advised to begin their internship applications in September."

**Commit to a recommendation where you can.** "It depends" is often the honest answer, but it's rarely the complete one. If it depends, explain what it depends on and then give a concrete recommendation for the most common case. "It depends on your goals, but for most students who want a software engineering role, picking up Go or TypeScript before graduation is more useful than spending that time on Haskell" is much more useful than "it depends on what kind of career you want."

---

## Keeping Information Current

Information in this wiki has a shelf life. Here's how to handle it responsibly:

**Fix outdated information when you find it.** If you know a company has closed, a course has changed format, or a salary range is no longer accurate, fix it immediately rather than adding a note that it "might be outdated." Stale notes accumulate and make the wiki harder to trust.

**Include dates for time-sensitive information.** Salary ranges, application timelines, company hiring freezes, and similar information should include the year or semester it was accurate. For example: "As of early 2025, junior dev salaries in Edmonton for new grads typically range from $70K–$90K base." This way, even if the numbers drift, readers know what era the data comes from.

**Be transparent about the source of your knowledge.** Firsthand knowledge ("I interned at Company X in 2024 and the process was...") is more reliable than secondhand ("I heard that Company X tends to..."). You don't need to avoid secondhand information, but be clear about what you know directly vs. what you've heard from others. Readers can calibrate accordingly.

---

## File Structure

**Where new pages go:** New pages belong in the appropriate subdirectory under `docs/`. If you're adding a page about a new career path, it goes in `docs/career/`. If you're adding a course review, it goes in `docs/courses/`. If you're not sure where something fits, ask in an issue.

**Update the table of contents:** Every new page needs a corresponding entry in the Table of Contents in `README.md`. Add it under the correct section with a brief description that tells the reader what they'll find on the page.

**Heading levels:** Use consistent heading structure throughout.
- H1 (`#`) — Page title only. One per page.
- H2 (`##`) — Major sections within the page.
- H3 (`###`) — Subsections within a section.
- H4 (`####`) — Use sparingly, only when you genuinely need a fourth level.

**File naming:** All file names are lowercase with hyphens, no spaces, no underscores, no camelCase. Examples: `interview-prep.md`, `edmonton-tech-scene.md`, `first-year-guide.md`.

**Linking between pages:** When you reference another page in the wiki, link to it. Keep links relative so they work regardless of where the wiki is hosted.

---

## Acknowledgments

This wiki was built by UofA CS students who wanted something like this to exist when they were starting out. Every section represents someone sitting down and writing out what they knew, often after learning it the hard way.

Thank you to everyone who has contributed — whether it was a full new page, a paragraph about an internship, or a single corrected fact. It all matters.

If you're reading this and thinking about contributing for the first time: please do. You don't need to be a fourth-year with three internships under your belt. If you just finished CMPUT 174 and have thoughts about what would have helped you, that's worth writing down. The wiki is for every year of the degree, and every year needs people willing to speak from where they are.

---

*Questions about contributing? Open an issue or reach out through the Computing Science Club.*
