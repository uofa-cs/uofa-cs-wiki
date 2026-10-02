# Roadmap: Rebuilding the Wiki

The first version of this wiki was largely AI-generated from scraped Reddit and RateMyProfessors data. A full audit (October 2026) found that it's built on a degree structure that no longer exists, contains invented facts, ranks named professors, and is mostly generic advice students can get from any chatbot. This document lays out how we fix that.

## What this wiki is for

Students already have the Academic Calendar, Reddit, RMP, and AI chatbots. This wiki's job is to be the thing those can't give you: **what a senior UofA CS student knows that the calendar doesn't say and an AI gets wrong.**

Every paragraph should pass one test: **could a student get this by asking a chatbot?** If yes, cut it or link to it.

## What the audit found

1. **The core planning content describes a program that no longer exists.** The 2026-27 calendar has Major, Major AI Option, Major Software Practice Option, matching Honors versions, and a Minor. The wiki still describes General / Specialization / Honors (with a thesis). First-year calculus is MATH 134/144/154 (or 117/118 for Honors), not MATH 114. Nothing mentions the CMPUT 200/300 ethics requirement. The sample degree plans violate prerequisites, and 274/275 no longer use hardware.
2. **Several facts were invented.** A lab that doesn't exist at UofA, a database group built around a Waterloo professor, a "Computing Science Club" (it's UACS), scholarships that don't exist, wrong USRA amounts, "Alberta has no provincial income tax," Benevity as an Edmonton employer, "CS has no co-op" (SIP exists), retired or departed professors as top recommendations.
3. **Professor rankings were a liability.** Named faculty were tiered into "actively avoid" lists using scraped RMP quotes, contradicting our own contributing guidelines.
4. **Most text was generic.** Several pages were 0-15% UofA-specific, with nothing on AI coding agents, the 2025-26 junior market, or how interviews have changed.
5. **The same facts lived in 3-4 places and contradicted each other.**
6. **What works is first-hand student content.** Every merged community PR improved course reviews, and those are the best parts of the wiki.

## Principles

1. **Every UofA-specific fact has a source link and a `last verified` date.** Names, amounts, deadlines, course titles, prerequisites.
2. **One home per fact.** Other pages link; they don't restate.
3. **First-hand over synthesized.** Signed, term-stamped experience ("took it W26") beats scraped summaries.
4. **Describe teaching, don't rank people.** Notes like "the W26 section had weekly quizzes and posted full notes" are welcome. Tier lists, "avoid" lists, and RMP scores are not.
5. **Market content is dated.** "As of Fall 2026…", kept short.
6. **Generic topics get a link, not an essay.**

## New structure

| Section | Contents |
|---|---|
| **Start here** | Home page with paths by year and goal |
| **Program** | Requirements per option (linked to the calendar), prerequisite map and valid sample plans, first-year choices (174 vs 274, which math), SIP/co-op |
| **Courses** | One page per course with structured frontmatter, an index, and math/stats courses |
| **Careers** | SIP vs summer internships, Edmonton employer directory, internship write-ups, interviews and the market in 2026, crowdsourced pay data |
| **Research** | Getting started and funding (USRA, URI, Alberta Innovates), research areas and faculty, grad school (short) |
| **Community** | Verified club directory, annual events calendar |
| **Building skills** | What the degree covers vs. doesn't (by course), UofA dev setup, learning with AI agents, resources by course |
| **FAQ** | Short answers that link to the canonical page |

### Course page template

Facts in frontmatter (machine-checkable), experience in the body (human-written).

```yaml
---
code: CMPUT 201
title: Practical Programming Methodology
prereqs: "CMPUT 175 or 274"
languages: [C]
textbook: "C Programming: A Modern Approach (K. N. King)"
catalogue: https://apps.ualberta.ca/catalogue/course/cmput/201
last_verified: 2026-10-01
---
```

Body sections: What it covers, Workload and assessment, Tips (signed with term), Pairs well / badly with.

## How we use AI this time

- **AI does facts, with citations.** Seeding course pages from the catalogue, rebuilding funding, clubs, and research pages from official sources, checking prerequisite logic.
- **Humans do experience.** Reviews, internship write-ups, and pay data come from people who were there. AI may help edit, never invent.
- **Freshness checks.** Each term, re-verify catalogue data, offerings, links, and deadlines, and open issues for drift.
- **CI.** Link checking, frontmatter validation, and flagging `last_verified` older than a year.

## Phases

### Phase 0: Damage control
- [ ] Remove the professor guide and all "avoid" lists / "worst prof" columns
- [ ] Fix confirmed false claims (degree structure, SIP/co-op, tax, Benevity, SkipTheDishes, TEC Edmonton, invented labs, scholarships, and clubs)
- [ ] Add a "being rebuilt" notice

### Phase 1: Foundations
- [ ] New directory structure and page templates
- [ ] Rewrite CONTRIBUTING around sourcing and the course/internship templates
- [ ] Issue and PR templates
- [ ] Directory-based navigation in `wiki-tooling` so new pages don't need a second PR

### Phase 2: Official-fact pages (rebuilt with sources)
- [ ] Program requirements, prerequisite map, sample plans, first year
- [ ] SIP / co-op
- [ ] Scholarships and research funding
- [ ] Research areas and faculty
- [ ] Clubs and events
- [ ] Dev setup and curriculum coverage map
- [ ] Edmonton employer directory

### Phase 3: Course pages
- [ ] Seed a page per course from the catalogue
- [ ] Migrate existing student reviews into course pages
- [ ] Recruit an owner per area (math has a volunteer in #12)

### Phase 4: First-hand content
- [ ] Internship write-ups (#7)
- [ ] Pay survey
- [ ] Interviews, the market, and AI in 2026
- [ ] Partner with UACS for reach

### Phase 5: Polish
- [ ] Course catalogue view (#8) and better search (#10)
- [ ] Link checking, frontmatter validation, and staleness CI
- [ ] Scheduled freshness audits

## Decisions

Defaults we're proceeding with. Open an issue to challenge any of them.

1. **Professor content:** no rankings or ratings. Descriptive, term-stamped notes about how a section was taught may live on course pages.
2. **Repos:** keep content and tooling separate for now; revisit once navigation is automatic.
3. **Course coverage:** CMPUT courses offered in the last two academic years, plus first-year MATH and STAT.
4. **Affiliated resources:** allowed only with disclosure and only where they fill a real gap.
