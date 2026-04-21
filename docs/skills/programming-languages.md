# Programming Languages: What UofA Teaches vs What Industry Uses

Language debates online are mostly noise. But choosing what to invest your time in matters when you're a student with limited hours. Here's an honest breakdown of what UofA teaches, what actually gets used in industry, and how to think about learning languages strategically.

---

## Languages You'll Encounter at UofA

**Python** is the backbone of the first two years. CMPUT 174 and 175 use it. Most 300-level AI and ML courses use it. By the time you graduate, you'll be comfortable with Python whether you tried to be or not.

**C** shows up in CMPUT 201 and runs through 229 (computer organization) and 379 (operating systems). The point isn't that you'll write C in industry; it's that C forces you to understand what's actually happening: pointers, memory allocation, the stack vs heap, undefined behavior. This understanding bleeds into every other language you use. Take it seriously.

**C++** appears in some upper-year electives, particularly graphics and systems-adjacent courses. It's not heavily taught but it's available.

**Java** comes up in a few 300-level courses. It's verbose, object-oriented to a fault, and not exciting. It's also used heavily in enterprise software, Android development, and many large-scale backend systems. Don't dismiss it because it's boring.

**Haskell and Prolog** appear in CMPUT 325 (programming languages). These are mind-expanding, not career-defining. Haskell in particular will change how you think about functions, types, and immutability, which will make you better at Python, TypeScript, and everything else.

**Racket** shows up in parts of 174/175 for functional programming concepts. Same story as Haskell: the value is conceptual, not practical.

---

## Going Deeper on Languages You Already Know

### Python

You'll leave 174/175 able to write Python. To actually be productive professionally, go deeper:

- **List comprehensions and generator expressions**: not just stylistic shortcuts, they're idiomatic Python and appear everywhere.
- **Decorators**: used heavily in frameworks like Flask, FastAPI, Django. Understanding how they work demystifies a lot of "magic."
- **Async/await**: modern Python backends are async. `asyncio`, `httpx`, async SQLAlchemy; you'll need this for FastAPI or any high-throughput service.
- **Type hints**: Python 3.5+ supports type annotations. Tools like `mypy` and `pyright` check them statically. All serious Python codebases use type hints now.
- **The ecosystem**: `pip`, `virtualenv`/`venv`, `poetry` or `uv` for dependency management. Know how to set up a project properly, not just `pip install everything globally`.

Python is the most employable language for ML/AI and a top choice for backend web. The depth here is worth it.

### C

You learn enough C in 201 to survive 229 and 379. After that, most students don't touch it again. That's fine for most career paths, but if you go into systems programming, embedded, or security work, actually being proficient in C is a differentiator.

Understanding C (even if you never write it professionally) makes you a better developer everywhere. When you understand why a Python `list` is slower than a C array, or why copying strings naively causes bugs, or what a segfault actually means, you have an intuition that most developers lack.

---

## Languages Worth Learning on Your Own

### JavaScript and TypeScript

UofA barely teaches web development. This is a significant gap because the web is where most software runs, and JavaScript/TypeScript is the language of the web.

JavaScript runs in browsers and (via Node.js) on servers. TypeScript is JavaScript with a static type system layered on top; it catches bugs before they happen, makes refactoring safer, and is now the default choice for any serious JavaScript project.

If you have any interest in web development, frontend or backend, learn TypeScript. Start with JavaScript basics, then add TypeScript. Learn React for frontend. Learn Express or Fastify (Node.js) for backend. The ecosystem is massive and jobs are abundant.

### Go

Go (Golang) is a statically typed, compiled language designed at Google. It's fast, the concurrency model (goroutines and channels) is elegant, and it compiles to a single binary with no runtime dependencies. This makes it excellent for building services, CLI tools, and infrastructure.

Go is used heavily in cloud-native infrastructure (Docker, Kubernetes, and most of their tooling are written in Go), at companies like Google, Cloudflare, Uber, and Dropbox, and increasingly for backend API services.

If you're interested in backend development or infrastructure, Go is worth learning in your 3rd or 4th year. It has a small standard library but a thoughtful one, and the language is deliberately simple; most people feel productive in Go quickly.

### Rust

Rust is the hardest language on this list. It introduces a new concept (the borrow checker) that takes real time to internalize. In exchange, it gives you memory safety without garbage collection and performance close to C.

Rust is growing fast in systems programming, WebAssembly, blockchain (it's the primary language for Solana smart contracts), game engine internals, and increasingly in security-critical code. Mozilla rewrote Firefox components in Rust. The Linux kernel now accepts Rust code.

Should you learn Rust? If you're interested in systems, blockchain, security, or just want to deeply understand memory, yes, it's worth it. Don't expect to pick it up in a weekend. But knowing Rust is genuinely impressive to employers in the right domains.

### SQL

SQL is not a "programming language" in the traditional sense but treat it as one. You get basics in CMPUT 291. You should go much further.

The features most developers underuse: **window functions** (ROW_NUMBER, RANK, LAG, LEAD, SUM OVER), **CTEs** (common table expressions for readable complex queries), **indexes and query planning** (understand EXPLAIN ANALYZE in Postgres), **transactions and isolation levels**.

SQL is used in virtually every application that stores data. Being genuinely good at it (not just `SELECT * FROM table` good) is valuable in almost any software job. It's also one of the best ROI skills to develop because most developers aren't very good at it.

---

## Language Recommendations by Career Path

### Backend Web Development
**Python** (FastAPI or Django) or **Go** or **Node.js/TypeScript**. Python is the safest bet if you're already comfortable with it; the ecosystem for web backends is mature and there are many jobs. Go is increasingly popular for performance-sensitive services. TypeScript on Node gives you full-stack JavaScript, which is practical.

### Frontend / Full-Stack Web
**TypeScript** with **React** (most common), **Vue** (also common, cleaner API), or **Svelte** (smaller but growing). There is no escaping JavaScript/TypeScript here. Learn it properly.

### Machine Learning and AI
**Python** is essentially mandatory. PyTorch for deep learning (preferred in research and increasingly in industry over TensorFlow). JAX for high-performance ML research. scikit-learn for classical ML. Knowing how to write efficient Python (vectorized operations, GPU memory management, async data loading) matters as much as knowing the frameworks.

### Systems Programming
**C**, **C++**, **Rust**, **Go**. The right choice depends on the context. C and C++ for traditional systems and anything touching hardware. Rust for new systems code where memory safety matters. Go for higher-level system services (daemons, servers, CLI tools).

### Game Development
**C++** with Unreal Engine is the highest-performance path, used in AAA games. **C#** with Unity is the most accessible and widely used in indie and mid-sized studios. **GDScript** (Python-like) or **C#** with Godot for open-source development. Python is used in some scripting contexts (Blender, pipeline tools) but not in game runtime code.

### Mobile Development
**Swift** for iOS (the only real option for native). **Kotlin** for Android (replaced Java, which still works but Kotlin is preferred). **React Native** (TypeScript/JavaScript) or **Flutter** (Dart) for cross-platform; these let you write once and target both iOS and Android with reasonable performance.

### Blockchain / Web3
**Solidity** for Ethereum smart contracts. It's a Turing-complete language with a C-like syntax and a lot of footguns; security matters enormously here. **Rust** for Solana. **Go** for blockchain infrastructure and nodes (Ethereum clients like Geth are written in Go). If you're going deep into blockchain, learning the EVM internals or consensus mechanisms is more important than the language syntax.

### DevOps and Infrastructure
**Python** for scripting and automation. **Go** for building tools. **Bash** for glue scripts (learn at least enough to not be helpless). **HCL** (HashiCorp Configuration Language) for Terraform infrastructure-as-code. **YAML** for Kubernetes manifests and GitHub Actions pipelines (not really a programming language, but you'll write a lot of it).

---

## How to Think About Languages Strategically

### Learn One Statically Typed, One Dynamically Typed Language Well

Dynamically typed languages (Python, JavaScript, Ruby) are faster to write and more forgiving. Statically typed languages (Go, TypeScript, Java, Rust, C++) catch more bugs at compile time, are easier to refactor safely, and often run faster.

Understanding both paradigms makes you a better developer. You'll understand why type systems exist (not just "annoying rules") and when dynamic typing is an asset vs a liability.

### Language Wars Are Mostly Irrelevant

"Python vs Go," "JavaScript vs TypeScript," "Rust vs C++": most of this debate is unproductive. Languages are tools. The underlying concepts (data structures, concurrency, memory management, type systems, error handling) transfer across languages.

Once you're genuinely good at two or three languages, picking up a new one is a matter of weeks, not months. The things that take time are the idioms, the ecosystem, and the performance characteristics, not the syntax.

### Don't Spread Too Thin

A common mistake is dabbling in ten languages and being mediocre at all of them. For job hunting, it's better to be strong in two or three languages than to have "hello world" experience in ten.

Pick your primary language (probably Python, since UofA gives you a head start). Add a second one that serves a different purpose: TypeScript if you want web, Go if you want backend/systems, Rust if you want something challenging. Get genuinely good at those before adding more.

Depth in a language means: you know the standard library well, you understand common pitfalls, you can read someone else's code in that language and understand what it's doing, and you have opinions about how to structure projects in it.

### SQL Is Non-Negotiable

Whatever path you take, learn SQL properly. It is the one language that cuts across almost every engineering role. Data engineers use it all day. Backend engineers write it for application queries. Data scientists use it to pull training data. Even frontend engineers end up in ORMs that abstract over it. You can't fully escape SQL, so you may as well be good at it.

---

## The Bottom Line

UofA gives you Python, C, and exposure to functional thinking. That's a decent foundation. On top of that, add: TypeScript (if web interests you), Go (if backend/systems appeals), and deep SQL fluency (regardless of path). Be honest about which languages you're actually proficient in on your resume; interviewers will test you on whatever you list.

Pick depth over breadth. The language matters less than what you build with it.
