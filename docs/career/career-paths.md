# Career Paths for UofA CS Students

UofA CS gives you a solid foundation across fundamentals (algorithms, systems, theory), but it doesn't tell you what to do with that foundation. This guide breaks down the major CS and software career paths: what they actually involve day-to-day, which UofA courses are most relevant, what skills you need to build on your own, and an honest take on demand, salary, and difficulty.

No path here is universally better than another. The right one depends on what kind of problems you find interesting, what you're actually good at, and what tradeoffs you're willing to accept.

---

## Backend Engineering

### What it is
Backend engineers build and maintain the server-side systems that power applications: APIs, services, databases, business logic, data pipelines. When you use an app and something happens (you place an order, send a message, submit a form), backend systems are doing the work invisibly.

### Day-to-day
Designing RESTful or GraphQL APIs, writing and maintaining services, writing database queries and optimizing slow ones, debugging production issues, reviewing other engineers' code, writing tests, and occasionally staring at a distributed systems problem that shouldn't be this hard.

### Relevant UofA courses
- **CMPUT 291** (Databases): directly applicable; SQL fluency is non-negotiable
- **CMPUT 313** (Computer Networks): understanding HTTP, TCP, how the internet actually works
- **CMPUT 379** (Operating Systems): processes, concurrency, the stuff that comes up in interviews
- **CMPUT 404** (Web Applications): closest UofA gets to applied web backend work
- **CMPUT 391** (Multimedia DB and Data Mining): useful if you work with complex data
- **CMPUT 481** (Distributed Systems): essential for understanding modern backend architecture

### Skills to build independently
Python, Go, or Java (Go is increasingly dominant for new backend work; Python is ubiquitous; Java/Kotlin is strong at enterprise companies). Docker and containerization. REST API design. SQL fluency (PostgreSQL in particular). Basic message queues (Kafka, RabbitMQ). HTTP fundamentals. Writing tests.

### Companies and market
Every tech company has backend roles. This is the highest-demand path in software engineering; far more backend openings than any other specialty. Edmonton has solid backend opportunities at Jobber, ATB, TELUS, Benevity, and others. Entry-level to senior trajectory is well-defined and compensation is strong.

### Honest assessment
Best risk-adjusted career path for most CS students. High demand, clear learning progression, widely applicable across industries. Not flashy, but the engineering is genuinely interesting when you're working on systems at scale. If you're not sure what you want to do, start here.

---

## Frontend / Web Development

### What it is
Frontend engineers build what users see and interact with: web interfaces, browser applications, component libraries, and increasingly mobile web experiences.

### Day-to-day
Writing HTML, CSS, and JavaScript/TypeScript. Building components in React, Vue, or similar frameworks. Working closely with designers to translate mockups into real interfaces. Performance optimization (why is this page slow?). Ensuring accessibility. Cross-browser testing.

### Relevant UofA courses
UofA barely teaches this. CMPUT 404 touches on web fundamentals but doesn't go deep on modern frontend. The skills here are almost entirely self-taught.

### Skills to build independently
This is the path most dependent on self-learning. You need: TypeScript (not just JavaScript; TypeScript is now the professional standard), React or Vue, CSS (actually knowing it, not just cargo-culting), browser APIs, accessibility fundamentals, performance profiling tools, and at least a working knowledge of how the backend you're consuming is built.

### Companies and market
Frontend roles are everywhere. However, pure frontend positions are becoming rarer; most companies want full-stack engineers who can do both frontend and backend at a reasonable level. Edmonton in particular skews toward backend-heavy teams. If you want to specialize in frontend, Toronto and Vancouver have larger UI-focused teams (consumer products, design-heavy apps).

### Honest assessment
Lower ceiling than backend at most companies, but still a legitimate path. The caveat is that "I only do frontend" is harder to sustain long-term as the industry pushes toward full-stack. If frontend is your interest, build it seriously; the gap between mediocre and excellent frontend engineers is large and visible.

---

## Full-Stack Development

### What it is
Full-stack engineers work across both the frontend and backend. They can build a feature end-to-end: the database schema, the API endpoint, the frontend component, the test.

### Day-to-day
Roughly split between backend and frontend work, depending on the sprint. At smaller companies and startups, you might own entire features solo. At larger companies, you might specialize more in practice even with a full-stack title.

### Relevant UofA courses
Combination of backend and frontend recommendations above. CMPUT 404 is the most directly applicable UofA course.

### Skills to build independently
Everything from both the backend and frontend sections, at a "good enough" rather than "deep specialist" level. The key is being genuinely competent on both sides: not just technically capable, but able to make real architectural decisions on each end.

### Market
Most common role type at startups and mid-size companies. If you're going to work in Edmonton's tech scene, full-stack versatility is a practical advantage. Many job postings in Edmonton technically want full-stack even when they say "backend engineer."

### Honest assessment
The most practically useful path for the Edmonton market and for smaller companies generally. The tradeoff is breadth over depth; you won't be the go-to expert on either side. That's fine for most roles, but if you want to be the senior distributed systems architect someday, you'll need to pick a specialty to go deep on eventually.

---

## Software Engineering

### What it is
Software engineering is broader than full-stack. Full-stack usually means building across frontend and backend for product features. Software engineers are more of an all-arounder: people who make complex systems work together across whatever technologies the problem requires. That can include system architecture, APIs, databases, infrastructure, testing, networking concerns, CI/CD, framework integration, and sometimes ML-enabled systems.

### Day-to-day
Designing system architecture, breaking ambiguous problems into concrete components, choosing frameworks and tools, integrating services and databases, debugging failures that span multiple layers, setting up testing and deployment workflows, reviewing design and code, and learning new technology quickly when the problem demands it.

### Relevant UofA courses
- **CMPUT 201** (Practical Programming Methodology): useful for learning Unix tooling, introductory Git workflows, debugging, and other practical software engineering basics
- **CMPUT 229** (Computer Organization): lower-level than most SWE work and mainly useful here because it leads into `CMPUT 379`; most software engineers will not touch this level much unless they want to go into embedded or systems work
- **CMPUT 267** (Machine Learning I): mostly theory, but useful if you want to move toward the MLE side of software engineering; `CMPUT 469` is the more practical follow-up
- **CMPUT 291** (Introduction to File and Database Management): databases are part of almost every serious software system
- **CMPUT 301** (Introduction to Software Engineering): build an Android app in a team while learning requirements, revision control, Git conflicts, software architecture, testing, and basic product/project management
- **CMPUT 313** (Computer Networks): useful when systems need to communicate reliably across services and environments
- **CMPUT 379** (Operating Systems): important for understanding concurrency, processes, resource management, and runtime behavior
- **CMPUT 401** (Software Process and Product Management): software development from a process perspective; useful for understanding how substantial systems are specified and shipped
- **CMPUT 402** (Software Quality): testing, reviews, continuous integration, and quality tooling
- **CMPUT 404** (Web Applications and Architecture): modern web architecture, web services, frameworks, and integration patterns
- **CMPUT 469** (Artificial Intelligence Capstone): practical team-based AI/ML project work; closest thing to a `401`-style product/project course for the MLE side
- **CMPUT 481** (Parallel and Distributed Systems): valuable if you want to design systems that scale across machines

### Skills to build independently
One strong backend language and ecosystem. Enough frontend skill to build and debug interfaces when needed. SQL and database design. System design. Linux fundamentals. Docker and cloud basics. Testing discipline. CI/CD workflows. Ability to read documentation quickly, pick up unfamiliar frameworks, and connect components that were not designed by the same team.

### Market
This is the broadest title on the page and also one of the most common. Many companies hire "software engineers" when they actually want someone who can move across backend, infrastructure, data, APIs, and product work depending on what the team needs. In practice, these roles often lean backend-heavy, but the expectation is broader engineering judgment rather than a narrow specialty.

### Honest assessment
Best fit for people who like being the all-arounder. If you enjoy solving messy technical problems, learning new tools quickly, and making different technologies work together, this path makes sense. It is probably the path that benefits from the most overall knowledge, and in practice you may end up taking more courses across different areas than you would for a narrower path. That does not mean you need every course listed here. "Software engineer" is a broad title and many SWE roles still lean toward specific areas like backend, infrastructure, data, or ML. The practical approach is to build broad foundations first, then choose more specialized courses once you know which parts of software engineering you actually like.

---

## ML / AI Engineering

### What it is
A field with two distinct sub-paths that get conflated:

**ML Research**: training and improving models, writing papers, advancing the state of the art. Mostly lives in academia and research labs.

**ML Engineering**: taking models (yours or others') and building the infrastructure to deploy them, serve them at scale, monitor them, and retrain them. More software engineering than math.

### Day-to-day
Research path: reading papers, designing experiments, implementing model architectures, running training jobs, analyzing results. Engineering path: building data pipelines, model serving infrastructure, monitoring dashboards, feature stores, A/B testing frameworks.

### Relevant UofA courses
- **CMPUT 267** (Machine Learning): the core intro course
- **CMPUT 365** (Reinforcement Learning): UofA has world-class RL researchers; this is a genuine differentiator
- **CMPUT 466** (Machine Learning, grad-level intro)
- **CMPUT 467** (Text Analytics)
- **CMPUT 461** (Natural Language Processing)
- **CMPUT 463** (Probabilistic Graphical Models)

### Skills to build independently
Python is mandatory. PyTorch is the dominant framework for research; TensorFlow still exists in production systems. Statistics and linear algebra fluency (not just having taken the courses, but being comfortable with the concepts). For ML engineering specifically: data pipeline tools (Spark, Airflow), model serving (FastAPI, Triton, SageMaker), experiment tracking (MLflow, Weights & Biases).

### Edmonton market
Amii (Alberta Machine Intelligence Institute) is the connective tissue of Edmonton's AI ecosystem. They bridge UofA research and industry application. AltaML does applied ML work and has historically been accessible to students. ATB Financial has interesting data and ML problems. For pure ML research, UofA's connections to Sutton, Bowling, and the broader RL research community are a legitimate advantage you won't get at most universities.

### Honest assessment
Hot field with high compensation potential, especially for ML engineers who can deploy and scale models in production. The research path requires graduate school and tolerance for low probability of breakthrough. The engineering path is increasingly accessible and well-paid. Be honest about which sub-path you're actually building toward.

---

## DevOps / Infrastructure / Site Reliability Engineering

### What it is
DevOps and infrastructure engineers build and maintain the systems that let other engineers ship code reliably: CI/CD pipelines, cloud infrastructure, monitoring and alerting, deployment automation. Site Reliability Engineering (SRE) is Google's formalization of this: applying software engineering discipline to operations problems.

### Day-to-day
Writing Terraform to provision cloud resources, configuring Kubernetes deployments, building CI/CD pipelines, debugging why a service is down at 2am, setting up monitoring and alerting, improving deployment speed and reliability, writing runbooks.

### Relevant UofA courses
- **CMPUT 379** (Operating Systems): essential foundation
- **CMPUT 481** (Distributed Systems): directly applicable
- **CMPUT 313** (Computer Networks): networking fundamentals matter here
- **CMPUT 402** (Software Quality): covers testing, reviews, continuous integration, and software quality tools, all of which map well to CI/CD and reliability work

### Skills to build independently
Docker and Kubernetes (not optional; these are table stakes now). Terraform or Pulumi for infrastructure as code. AWS, GCP, or Azure: pick one and learn it well. Linux systems administration fundamentals. Bash scripting. Prometheus/Grafana for monitoring. CI/CD tools (GitHub Actions, Jenkins, CircleCI). A programming language for automation (Python or Go).

### Market and salary
Often overlooked by CS students who want to write application code, but DevOps/SRE is in extremely high demand and at big companies, SRE roles pay as well or better than senior software engineers. The skill set is legitimately different from application development and takes time to build.

### Honest assessment
Underrated path. The work is genuinely interesting (you're reasoning about complex distributed systems), the demand is high, and the compensation at senior levels is excellent. If you find yourself fascinated by how systems fail and how to make them more reliable, this is worth exploring deliberately rather than accidentally ending up here.

---

## Security / Cybersecurity

### What it is
Two main paths: **offensive security** (pen testing, red teaming, vulnerability research: finding and exploiting weaknesses) and **defensive security** (blue teaming, threat detection, security engineering: building and monitoring defenses).

### Day-to-day
Offensive: running penetration tests against client systems, writing exploit code, documenting vulnerabilities, sometimes doing bug bounty hunting. Defensive: monitoring security alerts, incident response, building detection rules, security code review, vulnerability management.

### Relevant UofA courses
- **CMPUT 331** (Cryptography): foundational for understanding security at a deep level
- **CMPUT 333** (Computer Security): directly applicable
- **CMPUT 229** (Computer Organization): understanding systems at a low level is crucial for real security work
- **CMPUT 313** (Computer Networks): network security requires solid networking knowledge
- **CMPUT 379** (Operating Systems): OS internals are relevant for privilege escalation, kernel vulnerabilities

### Skills to build independently
Networking fundamentals (TCP/IP, DNS, TLS: really understand them, not just name-drop them). Common vulnerabilities (OWASP Top 10 is the baseline). Tools: Burp Suite for web security, Nmap, Metasploit for pen testing. CTFs (Capture the Flag competitions) are the best practical training; HackTheBox and TryHackMe are good platforms. For cryptography: actually understanding RSA, AES, hash functions, not just knowing they exist.

### Market
Government of Canada has substantial security teams: the Communications Security Establishment (CSE), RCMP, and various federal departments. Private sector: security consulting firms, financial institutions, and any large company with a security program. Bug bounty hunting is a real income path for skilled offensive researchers.

### Honest assessment
High skill ceiling, specialized, and genuinely important work. The path from CS graduate to competent security engineer is longer and more self-directed than backend development; the field rewards people who are genuinely curious about how things break. If that's you, it's a compelling path.

---

## Game Development

### What it is
Writing software for games: gameplay systems, physics, rendering, AI, tools. Ranges from AAA engine development at large studios to indie games to game tooling companies.

### Day-to-day
Implementing gameplay mechanics, debugging physics interactions, writing shaders, optimizing frame rate, building editor tools, working with game designers and artists to realize their vision in code.

### Relevant UofA courses
- **CMPUT 250** (Computers and Games): intro course
- **CMPUT 350** (Advanced Game Console Programming)
- **CMPUT 411** (Computer Graphics)
- **CMPUT 382** (GPU Computing)
- **CMPUT 256** (Introduction to Computer Animation)

### Skills to build independently
C++ for Unreal Engine (the dominant AAA engine) or C# for Unity (dominant in indie and mid-size studios). Graphics APIs (OpenGL as a foundation, Vulkan or DirectX for serious work). Physics simulation. Data-oriented design for performance. Profiling and optimization; games are one of the most performance-constrained domains in software.

### Market
Alberta: EA's main Canadian studio is in Burnaby, BC. Edmonton has some indie studios and game tooling companies. Game development roles are geographically concentrated in major cities.

### Honest assessment
Game development salaries are noticeably lower than equivalent-skill web/systems software engineering roles, and the industry has faced significant layoffs in recent years. The work can be creatively fulfilling in ways that enterprise software isn't. Go into it knowing this tradeoff. The technical skills (graphics, performance optimization, C++) are genuinely transferable to other domains like simulation, VR/AR, and embedded systems if you decide to exit.

---

## Embedded / Systems Programming

### What it is
Software that runs close to hardware: firmware for microcontrollers, operating system components, device drivers, real-time systems. The software in your car, your medical devices, industrial equipment, and aerospace systems.

### Day-to-day
Writing C or C++ for resource-constrained environments, debugging hardware/software interactions, writing and testing against real-time constraints, reading datasheets, using logic analyzers and oscilloscopes, dealing with hardware that doesn't behave the way the documentation says it does.

### Relevant UofA courses
- **CMPUT 229** (Computer Organization): mandatory foundation
- **CMPUT 274/275** (Intro to Tangible Computing): good practical introduction
- **CMPUT 379** (Operating Systems): OS internals directly applicable
- **CMPUT 329** (Fundamentals of Digital Logic and Design)
- **CMPUT 415** (Compiler Design): valuable for understanding what your code actually does

### Skills to build independently
C is mandatory. C++ is increasingly used. RTOS (FreeRTOS is the most common open-source option). Microcontroller programming (Arduino is the entry point; STM32 or NXP Kinetis for real work). Debugging with JTAG/SWD. Reading and interpreting hardware documentation.

### Alberta market
This is an underappreciated angle for Alberta specifically. The oil and gas industry uses enormous amounts of embedded software for instrumentation, control systems, and field devices. Companies in the pipeline monitoring, oilfield services, and industrial automation space need embedded engineers and the competition for that talent is lower than web development. Medical devices is another strong path (medical device companies exist in Edmonton and Calgary). Aerospace has a smaller but real presence.

### Honest assessment
Niche but durable. The people who are good at this are relatively rare compared to web developers, which means compensation can be strong and job security tends to be high. The learning curve is steeper early on (hardware is unforgiving) but the skills are genuinely specialized and hard to replace.

---

## Blockchain / Web3

### What it is
Protocol development, smart contract engineering, and decentralized application development. Spans from low-level consensus mechanism work to application-layer smart contracts to tooling and infrastructure.

There's an important distinction: **protocol layer** (working on Ethereum, Solana, or other blockchain clients; this is real distributed systems engineering) versus **application layer** (writing Solidity contracts to build DeFi apps; more accessible but more volatile as a career path).

### Relevant skills
Protocol layer: Go or Rust, distributed systems fundamentals, cryptography, P2P networking. Application layer: Solidity for Ethereum-based work, Rust for Solana, basic understanding of EVM, smart contract security.

### Market
Highly cyclical and correlated with crypto market conditions. Compensation in bull markets can be exceptional; well-funded protocols pay top-of-market salaries and token grants. In bear markets, many companies collapse. The engineering talent that survives market cycles tends to migrate toward the protocol and infrastructure layer rather than application-layer speculation.

The Ethereum Protocol Fellowship (mentioned here because it's genuinely one of the best structured ways into protocol-layer work for serious engineers: competitive, pays a stipend, and provides mentorship from core developers).

### Honest assessment
Be skeptical of hype. A lot of "blockchain jobs" are at poorly-run projects with more token allocation than engineering substance. The genuine engineering work at the protocol layer is interesting and well-compensated; it's real distributed systems and cryptography. Apply the same scrutiny you'd apply to any startup: Does this company have a sustainable business? Is the engineering work real? Don't let market excitement override judgment about company quality.

---

## Research

### What it is
Advancing the state of knowledge rather than shipping products. Happens in academia (professors, PhD students, postdocs) and at industry research labs (Google DeepMind, Microsoft Research, Meta AI, etc.).

### What it requires
For academic research: typically BSc → MSc → PhD → postdoc → faculty position. Long path with high variance outcomes. For industry research labs: a strong PhD and publication record is the normal entry point, though some research engineering roles are accessible with a strong MSc.

### UofA's position
UofA punches well above its weight in AI and ML research. Richard Sutton (reinforcement learning), Michael Bowling, and their connections to DeepMind and the Amii ecosystem make UofA a legitimate research institution, not just a teaching university. If you want to pursue research in RL or ML broadly, being at UofA and getting into a research lab as an undergrad (via USRA or just emailing professors) is a genuine advantage.

### Honest assessment
Research is the highest variance path. The upside is working on important problems with smart people and having real intellectual freedom. The downside is a long training period with relatively low pay (PhD stipends), high competitiveness for faculty positions, and no guarantee of outcomes. If research is your genuine calling, go for it with eyes open. If you're considering it because you don't know what else to do, that's the wrong reason; the industry paths above will serve you better.
