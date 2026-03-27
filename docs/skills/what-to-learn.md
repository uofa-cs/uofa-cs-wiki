# What to Learn: Bridging the UofA–Industry Gap

UofA's CS program will make you a decent computer scientist. It will not, by default, make you a hireable software developer. Those are related but distinct things. This guide covers the gap between what the degree teaches and what you actually need to get and keep a job in industry.

---

## What UofA Actually Teaches Well

Give credit where it's due. UofA does a solid job on a few things:

- **Algorithms and data structures** (CMPUT 204): if you actually engage with this course, you'll have a real foundation. LeetCode medium problems become manageable.
- **Theory** (CMPUT 272, 304): useful for understanding computation. Most industry devs don't use it daily, but it shapes how you think.
- **Systems** (CMPUT 379, 429): process management, OS internals, networking. Systems courses are some of the most transferable content in the program.
- **Databases** (CMPUT 291): relational models, SQL basics, ER diagrams. Good foundation, though you'll need to go deeper.
- **Software engineering concepts** (CMPUT 301): version control, basic agile, UML. More useful than it gets credit for.

The program gives you thinking tools. What it doesn't give you is hands-on craft.

---

## What UofA Doesn't Teach (That Industry Expects)

Here's what will catch you off guard at your first internship if you haven't self-taught it:

- **Docker and containerization**: nearly every company uses this. You won't see it in a UofA course.
- **CI/CD pipelines**: automated testing, deployment, GitHub Actions — not taught.
- **Cloud services**: AWS, GCP, Azure. The labs are on-prem. Industry is not.
- **REST API design**: you might build something for 301 but never learn the conventions, status codes, auth patterns, or versioning strategies.
- **Testing culture**: unit tests, integration tests, test coverage. Most UofA students graduate having never written a single test.
- **Agile/Scrum in practice**: CMPUT 301 brushes this but real sprint planning, standups, and Jira tickets are learned by doing.
- **Code reviews**: giving and receiving feedback on code professionally is a skill. You don't practice it in class.
- **Meaningful version control**: committing "update" 47 times is not how professionals work.

None of these are hard to learn. They're just not in the curriculum.

---

## Year-by-Year Roadmap

### Year 1: Foundation Habits

The degree starts with CMPUT 174/175. You're learning to program. Alongside that:

**Git — actually learn it.** Not just `git add . && git commit -m "stuff" && git push`. Learn branching, what a commit actually is, how to read `git log`, what merge conflicts look like and how to resolve them. This is the one tool you'll use every single day for the rest of your career.

**Linux basics.** The CS labs run Linux. If you're on Windows, install WSL2 now. Learn `ls`, `cd`, `grep`, `chmod`, `ssh`, pipes, redirects. An hour with a Linux tutorial pays back hundreds of hours of frustration.

**VSCode setup.** Get comfortable with your editor. Learn keyboard shortcuts. Install extensions. A well-configured editor makes you faster.

**Python beyond 174.** The course teaches you enough to pass. Go further: list comprehensions, dictionaries, file I/O, basic OOP. Write a small project — a CLI tool, a simple game, a web scraper. Anything that's yours.

**Build something small.** It doesn't have to be impressive. A command-line quiz app. A to-do list. A weather fetcher using a free API. The point is going from zero to working without a course holding your hand.

### Year 2: Become Technically Useful

By now you've done CMPUT 201 (C, memory management), 204 (algorithms), and maybe 291 (databases). You have some real CS knowledge. Time to convert it into practical skills.

**REST APIs — build one end-to-end.** Learn HTTP methods (GET, POST, PUT, DELETE), status codes, JSON, authentication (JWTs or API keys). Use FastAPI or Django REST Framework (Python people) or Express (Node). Build something: maybe a simple notes API with user accounts. Then call your own API from a frontend or Postman.

**SQL — go deeper.** CMPUT 291 gives you basics. Actually master it: JOINs of all types, GROUP BY, subqueries, window functions (ROW_NUMBER, LAG, LEAD), CTEs. SQL is used everywhere. Being actually good at it sets you apart.

**A web framework.** Pick one: Django, FastAPI, Express, Rails. Just one. Build something real with it. Don't framework-hop.

**Basic Docker.** Install Docker. Write a Dockerfile for one of your projects. Understand images vs containers. Run `docker build` and `docker run`. That's enough for year 2.

**Start LeetCode.** You don't need to grind 500 problems. Start doing easy problems in your primary language. Build the habit. By year 3, move to mediums.

### Year 3: Professional-Grade Habits

You're doing upper-level courses now — systems, compilers, distributed systems. This is when your side projects should start looking closer to professional work.

**Docker Compose.** Your app has a database, a backend, maybe a cache. Docker Compose ties them together. Write a `docker-compose.yml` for a project. This is standard in any modern dev environment.

**CI/CD with GitHub Actions.** Every project you push to GitHub should have a pipeline. Set up a workflow that runs your tests, lints your code, and (optionally) deploys on push to main. GitHub Actions is free and the YAML syntax is learnable in an afternoon.

**AWS or GCP free tier.** You don't need to spend money. AWS free tier gives you EC2 (virtual machines), S3 (file storage), RDS (managed Postgres/MySQL), and Lambda (serverless functions). Deploy something. Buy a cheap domain, point it at your EC2. This is what "the cloud" actually means.

**Testing — write tests for everything you build.** Use `pytest` for Python, `Jest` for JavaScript. Aim for at least unit tests on your business logic. If you build a REST API, write integration tests against it. The habit of writing tests is more important than the framework.

**Code reviews.** Contribute to open source or find a club/team where code reviews happen. Giving useful feedback on someone's PR and gracefully receiving feedback on yours are genuine professional skills.

### Year 4: System Thinking

Final year. If you're heading to industry, this is when you want to understand systems at a higher level.

**System design basics.** How do you design a URL shortener? A notification system? A social feed? These are real interview questions. Study: load balancers, caching strategies (Redis), database sharding, message queues (Kafka, RabbitMQ), CDNs. Understand trade-offs, not just buzzwords.

**Message queues.** Async communication between services. AWS SQS, RabbitMQ, Kafka — understand the concept even if you only use one. Decoupling services matters at scale.

**Monitoring and observability.** Logs (structured logging), metrics (Prometheus, Datadog), traces (OpenTelemetry). When something breaks in production at 2am, this is what saves you.

**Deployment pipelines.** Blue-green deployments, canary releases, rollback strategies. Understand how code goes from your laptop to users without downtime.

---

## Specific Topics in Depth

### Docker: Why It Matters

"Works on my machine" is the oldest complaint in software. Docker solves it by packaging your app and its exact dependencies into a container that runs the same everywhere — your laptop, a teammate's machine, a server in AWS.

Every company you interview at either uses Docker or wishes they did. Understanding it is not optional anymore. Start with a simple Dockerfile for one of your projects and work up from there.

### CI/CD: Automate Everything Boring

Continuous Integration (CI) means: every time you push code, automated tests run and tell you if you broke something. Continuous Deployment (CD) means: if those tests pass, the code ships automatically.

GitHub Actions is the right place to learn this. It's free for public repos, has an enormous library of community-built actions, and the YAML files live right in your repo. Write a simple workflow: install dependencies, run tests, done. Add linting. Add deployment later. This is table stakes in any dev job.

### Cloud: AWS Free Tier Is Enough

You don't need to spend money to learn cloud. AWS free tier includes enough to run real projects:

- **EC2**: virtual machines. Spin one up, SSH into it, deploy your app.
- **S3**: file storage. Store user uploads, static assets, backups.
- **RDS**: managed Postgres. No need to manage your own database server.
- **Lambda**: run code without managing servers. Good for event-driven tasks.

GCP (Google Cloud Platform) is equally valid — GCP's free tier is generous and their managed services are well-designed. Pick one and go deep rather than skimming both.

### REST APIs: Build One That Actually Works

Building a toy API is not enough. Build one that has:
- Proper HTTP status codes (200, 201, 400, 401, 403, 404, 422, 500)
- Authentication (JWT tokens or session-based)
- Input validation
- Error handling that returns useful messages
- At least a README explaining how to use it

Django REST Framework and FastAPI are both excellent for Python. FastAPI has better async support and auto-generated docs (Swagger UI). Django REST Framework has more batteries included. Either works.

### Testing: The Skill Nobody Teaches You

In four years of a CS degree, you will almost certainly never be required to write an automated test. This is a massive gap. In industry, untested code is considered incomplete.

Start simple: write `pytest` tests for functions you write. Test the happy path, then edge cases, then error conditions. When you build an API, write integration tests that make real HTTP requests and check responses. The tooling is not complicated — the discipline is what's hard to build.

### Agile/Scrum: Learn By Doing

CMPUT 301 introduces sprints and user stories. But real agile is learned in practice: actual sprint planning meetings, daily standups where people are waiting on you, tickets that get refined, code reviews that gate merges, retrospectives that actually change behavior.

The fastest way to learn this is an internship or a student club that runs real projects. CSSociety, student game dev teams, hackathon projects — any context where people are collaborating on the same codebase over time.

### Version Control Beyond the Basics

Most students use git as a slightly awkward backup system. Professionals use it as a communication tool.

- **Branching strategies**: main/develop/feature branches. Understand trunk-based development vs Gitflow.
- **Pull requests**: write descriptions that explain *why*, not just *what*. Review others' PRs carefully.
- **Rebasing**: clean up a messy branch history before merging. Understand `git rebase -i`.
- **Commit messages**: use Conventional Commits (`feat: add login endpoint`, `fix: handle null user`, `refactor: extract auth middleware`). Your future self and teammates will thank you.
- **git blame, git bisect**: tools for understanding history and tracking down bugs.

---

## The T-Shaped Developer

The best junior hires are T-shaped: broad enough to contribute across a codebase, deep enough in one area to be genuinely useful without constant hand-holding.

The degree gives you a bit of the horizontal bar. Pick one vertical to develop: backend systems, ML pipelines, mobile, dev tools, security. Build things in that area. Have opinions. The depth makes you memorable in interviews and actually valuable once hired.

Broad skills + one real depth = someone worth hiring. This is the goal.
