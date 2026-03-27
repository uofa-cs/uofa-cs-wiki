# Side Projects

Your GPA tells recruiters you can do coursework. Your projects tell them you can build things. In industry hiring, especially for internships and new grad roles, what you've built matters more than your transcript.

This guide covers what to build, when to build it, how to make it stand out, and how to avoid the mistakes that make projects invisible on a resume.

---

## Why Projects Matter More Than GPA

Most software engineering hiring decisions are made by engineers, not HR. Engineers look at your GitHub before your transcript. They want to know: can you build things? Can you figure things out independently? Do you have taste?

A 3.3 GPA with three solid deployed projects will outperform a 4.0 with nothing to show in most industry hiring processes. This is especially true at startups and mid-sized tech companies. FAANG has GPA cutoffs at the screening stage, but even there, a compelling project portfolio can get your resume surfaced by a referral that bypasses the filter.

The other thing projects do: they give you something to talk about in interviews. Behavioral questions like "tell me about a technical challenge you faced" hit different when you actually have a story from something you built for yourself, not from a group assignment where you weren't sure whose code was whose.

---

## Year-by-Year Project Ideas

### Year 1: Get Comfortable Coding

You're learning the basics. The goal isn't to build something impressive — it's to build the habit of writing code outside of assignments.

**Good first projects:**
- A Python script that automates something tedious (rename files, scrape a webpage, send yourself a daily email with something useful)
- A text-based game (guess the number, hangman, a simple RPG with a command line interface)
- A web scraper that collects data you actually care about (game prices, weather, sports scores)
- A simple calculator with a GUI (Tkinter in Python is straightforward)

The bar is low here. Done is better than perfect. The point is getting reps finishing things.

### Year 2: Full Stack Experience

You've got your fundamentals. Now build something with multiple layers — a backend that talks to a database, a frontend that talks to the backend. This is when things get interesting.

**Good Year 2 projects:**
- A REST API with a real database. Use Flask or FastAPI with PostgreSQL. Build something like a personal finance tracker, a recipe manager, a simple inventory system.
- A Discord bot. Discord's API is well-documented, bots are immediately usable, and it's genuinely fun to build something your friends interact with.
- A full web app: FastAPI or Django backend + React or plain JavaScript frontend. A Reddit clone, a personal blog with a CMS, a booking system.
- A data analysis project with real data. Find a public dataset you care about (Statistics Canada, Kaggle, open government data). Clean it, analyze it, make visualizations. Use pandas and matplotlib or seaborn.

By the end of Year 2, you should understand what it means for a frontend to call a backend endpoint and get data from a database back. That mental model is foundational for everything else.

### Year 3: Production-Ready Thinking

This is the year to deploy something. "Works on my machine" doesn't count. The difference between a project that runs locally and a project that's live on the internet is enormous — for your learning and for your resume.

**Year 3 goals:**
- Deploy something. Render, Railway, Fly.io, Vercel, or a $6/month VPS. It doesn't matter where, just get it live with a real URL.
- Build something with auth. User registration, login, sessions or JWTs, password hashing. Every real application has auth and it's genuinely non-trivial to get right.
- Integrate a real external API. Stripe for payments, Twilio for SMS, OpenAI for AI features, Mapbox for maps, a government open data API. This shows you can read documentation and integrate third-party services — a core real-world skill.
- Make your first open source contribution. Doesn't have to be a big contribution. Fix a typo in the docs, close a small bug, add a test case. The goal is to understand how open source development works.

A deployed project with auth and a third-party API integration is a genuinely solid resume line at this stage.

### Year 4: Portfolio Pieces

You're close to entering the industry. Your projects should be things you're comfortable demoing in an interview and talking about in depth.

**Year 4 goals:**
- Build something that solves a real problem — preferably one you or people around you actually have. The best projects come from genuine frustration with something that doesn't exist or doesn't work well.
- Write a technical blog post about something you built or learned. This demonstrates communication skills, which engineering managers care about more than most students expect. dev.to and Medium are easy starting points.
- Take your CMPUT 401 (Software Product Management) or CMPUT 404 capstone seriously. These courses are designed to produce portfolio pieces. Don't phone it in — treat it like a professional project.
- If you have time, build something that uses a technically interesting approach: a distributed system, a compiler, a browser extension, a machine learning model in production, a blockchain application.

---

## What Makes a Project Stand Out

**It solves a real problem.** The best projects scratch your own itch. "I was annoyed that X didn't exist, so I built it" is a compelling interview story. Todo app clones are not.

**It has a good README.** This is non-negotiable. Your README should cover: what the project does, why you built it, how to run it locally, what technologies it uses, and ideally a screenshot or demo GIF. Engineers will look at your README before they look at your code. If it doesn't have one, the project doesn't exist.

**It's deployed.** A live URL beats a local setup every time. "You can try it at [url]" in an interview is immediately more impressive than "you can clone the repo and run npm install."

**It has tests.** Even a modest test suite signals engineering maturity. It says you thought about edge cases, you care about correctness, and you've worked in codebases that take quality seriously. Most student projects have no tests at all — having some immediately differentiates yours.

**The commit history shows real development.** Commit history is a story of how you built something. A project with 200 meaningful commits shows iterative development. A project with one commit that says "add all files" looks like you dropped in a tutorial. Commit as you go. Write reasonable commit messages.

**It uses something technically interesting.** Not every project needs a cutting-edge stack, but one or two projects that use something beyond the basics (WebSockets, a vector database, distributed architecture, a novel algorithm) stand out.

---

## Project Red Flags

These things actively hurt your resume:

**"Todo app in React" with no unique twist.** If you're going to build a todo app, it better have something interesting — offline sync, collaborative editing, an unusual technical constraint. Otherwise skip it.

**Tutorial project, zero modifications.** If you followed a tutorial and changed nothing, the project isn't yours. Recruiters and engineers can tell. Build on top of tutorials, don't stop at them.

**No README, no tests, single commit.** This communicates that you don't care about code quality or collaboration. It's worse than not listing the project at all.

**Obviously repackaged coursework.** Submitting your CMPUT 301 group project as a side project is transparent and unimpressive. Build something on your own time.

**"In progress" for more than a year.** Either finish it or remove it from your resume. Perpetually in-progress projects signal poor follow-through.

---

## Open Source Contributions

Contributing to open source is one of the highest signal things you can do as a student. It shows you can work in real codebases, read others' code, follow contribution guidelines, and communicate in code review.

**How to start:**

1. Search GitHub for issues labeled `good first issue` or `beginner-friendly` in projects you actually use.
2. Fix documentation issues first. Typos, unclear explanations, outdated instructions. Low barrier to entry, genuinely useful.
3. Move to small bug fixes. Read the relevant code, understand the issue, write a fix, write a test.
4. Graduate to features once you're familiar with the codebase.

**Beginner-friendly projects:**
- **freeCodeCamp** — enormous codebase, lots of good first issues, very welcoming community
- **scikit-learn** — Python ML library, strong contribution guidelines, good mentorship
- **Homebrew** — macOS package manager, lots of small formula updates
- **VS Code extensions** — building or contributing to an extension is a contained, achievable project
- **Any project you actively use** — you already understand the user perspective

**UofA-adjacent:**
- **Amii / RLAI repos** — Alberta Machine Intelligence Institute has open repos, especially around reinforcement learning research
- **Local Edmonton company repos** — some Edmonton tech companies open source parts of their stack. Check GitHub organizations for companies you're interested in working at.

---

## Hackathons

Hackathons are 24-48 hour events where you build something from scratch. They're valuable for three reasons: you practice shipping fast, you meet other students and industry people, and hackathon projects (if they work) are great resume conversation pieces.

**UofA-specific:**

**HackED** — UofA's main hackathon, typically runs in January or February. Run by the Computing Science Club. A good first hackathon because it's local, friendly, and you'll know people there.

**HackED Beta** — Smaller fall hackathon. Lower-stakes, good for first-timers.

**MLH (Major League Hacking)** — The national/international circuit of student hackathons. Dozens of events across North America each year, many virtual. Check mlh.io for the schedule. Winning or placing at an MLH event is a solid resume line.

**How to actually do well at a hackathon:**

Don't try to build something ambitious. The graveyard of hackathon projects is full of "Uber for X with AI and blockchain" ideas that have zero working code at demo time.

Pick a problem you can actually solve in 24 hours. Build the core feature. Make it demo-able. Polish the demo, not the code. A working prototype that does one thing clearly beats an architectural diagram for something that doesn't run.

Hackathon judges are looking for: does it work, is it creative, does the team understand what they built. That's it.

Hackathon code doesn't need to be good. Hackathon projects don't need to be complete. They need to demonstrate that you can execute under pressure and communicate what you've built.

---

## Your Personal Website

A personal website isn't strictly necessary, but it signals professionalism and gives you a landing page to point people to from your LinkedIn, resume, and GitHub profile.

**What to include:**
- Your name and a one-line bio
- Links to your GitHub, LinkedIn, and resume
- 2-3 highlighted projects with descriptions and links
- Optionally: a blog, your work experience summary, contact info

**Where to host it for free:** GitHub Pages. Create a repository named `yourusername.github.io`, put an `index.html` (or use Jekyll), and it's live. Netlify and Vercel are also free for static sites.

**Don't overthink the design.** Pick a clean template (there are hundreds of free ones for GitHub Pages), customize the content, and ship it. A simple site with good content beats a fancy site you spend three months building and never deploy.

A URL you can put at the top of your resume is worth more than the time you'll spend making it perfect.

---

## Edmonton-Specific Opportunities

**Startup Edmonton** runs events, workshops, and occasionally student project showcases. Worth checking their event calendar — going to a few events gets you in rooms with people who build things professionally and sometimes hire students.

**Amii (Alberta Machine Intelligence Institute)** has student programs and research opportunities. If your projects are ML-adjacent, connecting with Amii can open doors to research roles and industry connections in that space.

**Local tech meetups** (Edmonton JS, Edmonton Python, etc.) sometimes have project demo nights. Presenting a project you built to a room of working engineers is terrifying and extremely good for you.

---

## The Actual Advice

Build things you care about. The projects that turn into good resume pieces are almost always the ones you kept working on because you wanted to use the thing you were building, not because you needed something for your resume.

Ship early, iterate. A live project with rough edges beats a local project that's "almost ready." Get it deployed, get feedback, improve it.

Two or three solid projects beat ten mediocre ones. Quality over quantity. Depth over breadth. Know your projects cold — every design decision, every technical tradeoff, every thing you'd do differently. That's what interviews actually test.
