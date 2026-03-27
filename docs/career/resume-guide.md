# Resume Guide for UofA CS Students

Your resume is a filtering document, not a biography. Recruiters at large companies spend 6–10 seconds on an initial pass. At smaller companies, a hiring manager might read it more carefully — but only if it passes the first 10 seconds. This guide is about building a resume that clears both filters.

---

## The One-Page Rule

One page. Always, until you have 5+ years of full-time industry experience.

No exceptions for students. Not for co-op students with multiple work terms. Not for PhD students. One page.

If your resume is overflowing onto a second page, you're not including too much experience — you're including too much irrelevant content. Cut it.

---

## Format: ATS-First, Human-Readable Second

Most large companies (and a surprising number of mid-size ones) use Applicant Tracking Systems to parse resumes before a human ever sees them. ATS parsers are notoriously bad at reading:

- Tables and multi-column layouts
- Text boxes and graphics
- Fancy fonts and icons
- Headers/footers (some parsers miss content in these entirely)
- PDF files created from design tools (Canva, Adobe Illustrator)

**Use a simple, single-column format.** Clean fonts: Calibri, Garamond, Helvetica, or similar. Margins around 0.5–1 inch. Font size 10–12pt for body text. Your resume should look clean when viewed as plain text, not just as a PDF.

**LaTeX is the gold standard for CS student resumes.** Jake's Resume template (search "Jake's Resume LaTeX") is widely used in CS hiring circles and produces clean, ATS-friendly output. Overleaf has several good CS-specific templates. The slight extra effort of LaTeX is worth it — the output looks more polished than Word and it forces you into a clean structure.

If you're not using LaTeX, use Word or Google Docs with a minimal template. Avoid Canva for technical roles.

---

## Resume Sections, In Order

### 1. Header

Name (large, readable), followed by:
- Professional email address (your name@domain, not xXgamer420Xx@hotmail.com)
- Phone number
- LinkedIn URL (customize it: linkedin.com/in/yourname)
- GitHub URL (github.com/yourhandle)
- City, Province (Edmonton, AB is fine — you don't need your full street address)

No photo. No date of birth. No objective statement — it wastes valuable space and adds nothing.

### 2. Education

**University of Alberta** — BSc Computing Science [Specialization if applicable], Expected Graduation: Month Year.

Include GPA if it's 3.5 or above. Leave it off if it's below 3.2. The 3.2–3.5 range is your call — if the rest of your resume is strong, omit it; if you're thin on experience, it can help.

You don't need to list every relevant course. A "Relevant Coursework" line is optional and only worth including if you're very early in your degree and have no other material to fill the page.

Drop high school entirely after your first year at UofA.

### 3. Technical Skills

This section gets scanned both by ATS and by technical interviewers. Structure it by category:

- **Languages:** Python, JavaScript, Java, C, SQL (list what you actually know)
- **Frameworks/Libraries:** React, Node.js, Django, PyTorch, Spring (list what you've used on real projects)
- **Tools:** Git, Docker, Linux, Postman, Figma
- **Cloud/Infrastructure:** AWS (S3, EC2, Lambda), GCP, Azure — only if you've used them

**Be honest.** If you list React on your resume, expect React questions in the interview. If you've only done one tutorial, don't list it. Experienced interviewers can immediately tell the difference between someone who has worked with a technology and someone who just put it on their resume. A shorter, honest skills section is better than a padded, dishonest one.

Do not list things like "Microsoft Office" or "Google Suite" — these are assumed and waste space.

### 4. Experience

List in reverse chronological order (most recent first). For each role:

- **Company Name** | Role Title | Location (or Remote) | Month Year – Month Year
- 2–4 bullet points per role

**Bullet point formula:** Action verb + what you did + measurable impact or result.

Good: "Reduced API response time by 40% by implementing Redis caching layer, improving p95 latency from 800ms to 480ms"
Bad: "Worked on backend performance improvements"

Strong action verbs: built, designed, implemented, reduced, improved, automated, deployed, led, architected, refactored, migrated, scaled, optimized, shipped, integrated.

Avoid: "assisted with," "helped," "was responsible for," "worked on." These are weak and vague.

If you don't yet have tech-specific work experience (no internships, no RA roles), include relevant part-time work briefly. A barista job doesn't need three bullets — one line noting "customer service role while pursuing degree" is sufficient. Keep the focus on technical content above all.

### 5. Projects

This is often the most important section for students early in their degree who don't yet have internship experience. 3–4 projects is the sweet spot.

For each project:
- **Project Name** | [GitHub link] | [Live link if applicable]
- Tech stack used (bold or inline)
- 2–3 bullets: what it does, what's technically interesting about it, scale/impact if any

"Built a REST API serving 500+ daily users" beats "Built a REST API."
"Trained a custom CNN achieving 92% accuracy on the CIFAR-10 benchmark" beats "Used machine learning."

Where do metrics come from if your project doesn't have real users? Estimate reasonably, use benchmark results, describe scale of data processed, or describe technical complexity. Don't fabricate numbers, but don't undersell either.

**UofA course projects that are legitimate to include:**
- **CMPUT 401** (Software Process and Product): capstone project with real clients. This is real work and deserves real bullets.
- **CMPUT 301** (Introduction to Software Engineering): group project, Android app development. Legitimate.
- **CMPUT 404** (Web Applications and Architecture): involves building actual web projects. List it with the stack and what you built.
- **CMPUT 466** (Machine Learning) / **CMPUT 361** (Information Retrieval): if your project was interesting and had measurable results, include it.
- **CMPUT 455** / **CMPUT 496** (Game/AI work): if you built something notable, include it.

Don't include toy tutorial projects (the Django blog tutorial, the React to-do list). Only include projects where you made real decisions and built something non-trivial.

### 6. Optional Sections

Include these only if they're meaningful:
- **Awards/Honors:** Dean's List, scholarships, hackathon wins
- **Volunteer/Activities:** CS club executive roles, hackathon organizing, tutoring
- **Research:** If you've published or contributed to a paper, list it

---

## GitHub Profile: Recruiters Actually Check

Your GitHub is a portfolio. Treat it that way.

- **Pin 3–4 of your best repositories.** Not all of them. Pick the ones with the best code quality and the most interesting content.
- **Every pinned repo needs a README.** The README should explain what the project does, what technologies it uses, how to run it, and ideally include a screenshot or demo link.
- Commit history matters to some reviewers. Regular commits over time look better than 500 commits in one day before an application deadline.
- Keep your profile photo and bio professional enough that a recruiter isn't put off by it.

A polished GitHub with three good repos is far more compelling than 20 repos with no READMEs and no explanation of what anything does.

---

## ATS Optimization: Keywords Matter

When you're writing bullets and choosing what to include, use the language of the job posting.

If the job description says "Python," your resume should say "Python" not "scripting" or "back-end development."
If it says "containerization" and you've used Docker, say both "Docker" and "containerization."
If it mentions "REST APIs" and you've built them, use that exact phrase.

This isn't keyword stuffing — it's speaking the same language as the job. ATS parsers match keywords. Humans scanning resumes scan for familiar terms. Both reward alignment with the job description.

---

## Common Mistakes

**Including a photo:** Don't. It's not expected in North American tech hiring and introduces unconscious bias into the screening process. No benefit to you.

**"Objective statement" at the top:** A two-sentence generic objective statement does nothing. Scrap it. Use the space for a project or an extra bullet in experience.

**Vague bullet points:** "Contributed to development of the application" tells a reader nothing. Every bullet should convey what you specifically did and why it mattered.

**Skills inflation:** Listing every technology you've ever touched in a two-hour tutorial. Interviewers will probe your skills. If you can't answer follow-up questions about something on your resume, it's actively harmful to list it.

**Inconsistent formatting:** Mixing date formats (Jan 2024 vs. January 2024 vs. 2024-01), inconsistent use of periods at end of bullets, varying font sizes. These signal carelessness.

**PDF from Canva or a graphic-heavy template:** They look nice on screen. They parse terribly in ATS. Use LaTeX, Word, or Google Docs with a minimal template.

---

## Keeping Your Resume Fresh

Update your resume every 3–4 months even if you're not actively job hunting. It's much easier to capture what you did on a project while it's fresh than to reconstruct it 18 months later. A 30-minute resume review quarterly keeps you always-ready rather than scrambling before every application season.

---

## Quick Reference: The 10-Second Test

Print your resume (or view it at 50% zoom). Ask:
1. Can I immediately see the candidate's name, contact info, and education?
2. Are the most impressive things (internship at a recognizable company, strong project) visible in the top half of the page?
3. Do any bullets tell me what the person did AND what impact it had?
4. Is it visually clean and easy to scan?

If the answer to any of these is no, fix it before sending.
