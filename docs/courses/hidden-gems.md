# Hidden Gems: UofA CS Courses Most People Skip (But Shouldn't)

The CS program has a few courses that almost nobody talks about but that are genuinely excellent, either for interview prep, for career differentiation, or just for becoming a better engineer. This is the list of courses that upper-year students and recent grads consistently say they wish they had taken, or are glad they did when no one told them to.

---

## CMPUT 403: Algorithmics in Competitive Programming

**Why almost nobody takes it:** It sounds intimidating. "Competitive programming" makes people think it's for math olympiad types who live and breathe algorithms. It's not. It's a structured course that teaches exactly the patterns that show up in technical interviews.

**What students actually say:** One Reddit user who took it with Zachary Friggstad called it "Amazing CMPUT 403. Definitely recommend him." Another noted Friggstad will accept solutions that are correct in spirit even if not perfectly coded, and is consistently available on Discord. The format (weekly problem sets on Kattis) is uncomfortable at first and then deeply satisfying for students who stick with it.

**Why you should take it:** This is the best interview prep course at UofA, and most people don't know it exists. The curriculum covers:

- **Segment trees and Fenwick trees:** range query data structures that show up in medium-hard LeetCode problems
- **Binary search tricks:** not just "binary search on sorted array" but binary search on the answer, on the search space, applied to non-obvious problems
- **Advanced graph algorithms:** shortest paths, minimum spanning trees, topological sort, SCC (strongly connected components), network flow
- **String algorithms:** KMP, suffix arrays, string hashing. These are consistently tested at companies like Google and Meta
- **Dynamic programming optimization:** divide and conquer DP, convex hull trick, bitmask DP
- **Geometry:** computational geometry problems, convex hull

If you're applying to Google, Meta, Microsoft, Shopify, or any company that does algorithm-heavy interviews (which is most of them for new grad roles), the patterns in this course are exactly what you need to know. LeetCode by itself is unstructured. This course gives you the mental framework to actually recognize and solve novel problems.

**When to take it:** Third year is ideal. You need CMPUT 204 first; you won't survive without it. Taking it in third year means you can reinforce and apply the material during your most active internship application period.

**Format:** Mostly problem sets. You solve algorithmic problems under time pressure. It's uncomfortable at first and then deeply satisfying. This is what top engineers do for fun.

---

## CMPUT 382: GPU Programming and Architecture

**Why almost nobody takes it:** It has "GPU" in the name and people assume it's only for game devs or researchers. It's listed as an advanced elective that many students don't even look at.

**What students actually say:** The few Reddit discussions that mention 382 describe it as "not harder than any other 300-level CMPUT." Labs take the full 3 hours. The course has had disorganized offerings in the past (one student described the first lab as "take this old demo and make it run with a newer version of Visual Studio and CUDA libraries"), but nothing unusually brutal. The content itself is consistently described as straightforward once you get past the setup friction.

**Why you should take it:** The ability to write GPU code is rare. Genuinely rare. Most CS graduates, including people from much better-ranked universities, cannot write CUDA. This course teaches:

- **CUDA programming:** writing code that runs on the GPU in parallel, memory hierarchy on GPUs (global, shared, local memory), warp execution, thread divergence
- **Parallel algorithm design:** how to decompose problems for massively parallel execution
- **Performance optimization:** memory coalescing, occupancy, profiling GPU code

**Where this is useful in industry:**

- **ML infrastructure:** training large models requires understanding GPU memory, batching, and kernel optimization. ML engineers who can optimize CUDA kernels are extremely well paid.
- **Game development:** graphics programming, shader optimization, physics simulations on GPU
- **Scientific computing:** computational biology, physics simulations, financial modeling
- **High-performance computing:** any domain dealing with massive data

The job market for people who can write efficient GPU code is strong and getting stronger. Most companies that do serious ML work have "GPU utilization" problems and not enough people to solve them.

**Caveat:** This course is hard. CMPUT 229 (computer organization) is basically a prerequisite in terms of mental model; you need to understand what hardware is doing to write efficient GPU code. Go in knowing that; go in anyway.

---

## CMPUT 415: Compiler Design

**Why almost nobody takes it:** It sounds academic. "Nobody writes compilers in industry," people say. They're wrong, but more importantly, they're missing why this course matters.

**What students actually say:** This is one of the most universally respected "hard" courses in the program. One Reddit review: *"Without a doubt the most work I've had to do for a CMPUT course. Also the course that I learned the most in; in retrospect, I would still take it again."*

The project is a full LLVM-based compiler for a defunct IBM language with a 40-page spec. The spec glosses over features. Most groups don't fully implement everything. The workload "never lets up; as soon as an assignment is done, start the next one immediately."

Before taking it: know Java well (implementation language), look up ANTLR (parser generator) and LLVM basics. Don't take 415 in the same semester as another heavy course like 229 or 466.

**Why you should take it:** Understanding how a compiler works changes how you think about code. By the end of this course, you understand:

- **Lexing and parsing:** how source code text becomes an abstract syntax tree (AST). This is directly relevant to any tool that processes code: linters, formatters, transpilers, IDEs
- **Semantic analysis:** type checking, scope resolution, symbol tables
- **Intermediate representations:** how compilers represent code in a form that can be optimized
- **Code generation and optimization:** how high-level code becomes machine instructions, and how optimizations like dead code elimination, inlining, and loop unrolling work

**Where this is useful:**

- **Developer tooling companies:** JetBrains, GitHub, Sourcegraph, Stripe (their developer tools team), any company building IDE features, static analysis tools, or code generation
- **Programming language work:** designing DSLs (domain-specific languages), building interpreters, working on language runtimes
- **Senior engineering interviews:** explaining you've built a compiler immediately establishes technical credibility. Senior engineers know it's hard.

Beyond career utility, this course makes you a better programmer across the board. You stop thinking of your language as magic and start thinking of it as a tool with understandable behavior.

---

## CMPUT 313: Communication Networks

**Why almost nobody takes it:** It's perceived as boring. Networking? Layers? Who cares?

**What students actually say:** The content itself gets positive retrospective reviews from students who went on to backend or infrastructure work. One Reddit comment captured the dual nature well: "313 is drier than the desert. Not much relevancy to modern hands-on networking that you'd see for most CS work unless you want to get deep into network protocols." But another counter-perspective: the student who took it and later debugged production network issues reported wishing they'd paid more attention.

**The professor factor is significant here.** Ioanis Nikolaidis makes the course genuinely interesting through tangents and enthusiasm, but goes off on many tangents and requires the textbook to fill gaps. Ehab Elmallah, who also teaches 313 and 379, gets poor reviews, described as dry, monotone, and teaching "extremely outdated" networking content. Check who's teaching before registering.

**Why you should take it:** You use HTTP every single day. Every API call your code makes, every web page your browser loads, every database query that goes over a network; all of it runs on the protocols this course covers. After taking it, you know:

- What actually happens when you type a URL and press enter (DNS resolution, TCP handshake, HTTP request/response, TLS if HTTPS)
- Why TCP vs UDP matters and when to use each
- What happens at the socket level when two programs communicate
- How routers forward packets, how routing tables work, what BGP is
- Why CDNs exist and how they work
- What the hell "network latency" and "bandwidth" actually mean vs how people misuse these terms

**For backend and distributed systems roles specifically:** This is not optional knowledge. You will debug network issues. You will design systems that communicate over the network. You will be asked in interviews about what happens when a client makes a request. This course gives you the vocabulary and mental models to answer those questions properly.

It's also just deeply satisfying to understand infrastructure you've been using for years. Most developers treat the network as a black box. Don't be most developers.

---

## CMPUT 391: Database Management Systems (Advanced)

**Why almost nobody takes it:** Students take CMPUT 291, learn SQL, and think they're done with databases. They're not.

**Why you should take it:** CMPUT 291 teaches you to use databases. CMPUT 391 teaches you how databases actually work. That's a different thing, and it matters enormously:

- **Query optimization:** how the query planner decides to execute your SQL, what indexes actually do internally (B-trees), why certain queries are slow and how to fix them
- **Transaction management:** ACID properties, isolation levels, deadlock detection, why "just use a transaction" is not a sufficient answer
- **Concurrency control:** how multiple simultaneous queries don't corrupt your data
- **Distributed databases:** how data gets replicated, partitioned (sharding), and kept consistent across nodes. CAP theorem. This is the foundation for understanding systems like Cassandra, DynamoDB, and CockroachDB.

**For data engineering and backend roles:** This is the difference between a developer who can write SQL and a developer who understands why their queries are slow and how to design schemas that perform at scale. The latter is significantly more valuable and significantly rarer.

When you're debugging a slow query in production at 2am, you want to know what an execution plan is. This course is where you learn that.

---

## CMPUT 481: Parallel and Distributed Systems

**Why almost nobody takes it:** It's listed late and people have usually filled their CMPUT elective slots with other things. Also, "parallel" sounds like a research topic.

**Why you should take it:** Modern software runs on multiple cores and multiple machines. Understanding how to write correct concurrent programs is a critical skill:

- **Multi-threading:** threads, synchronization primitives, race conditions, deadlocks, lock-free data structures
- **Distributed computing patterns:** how to design systems that span multiple machines, handle partial failures, and maintain consistency
- **Concurrency models:** shared memory vs message passing, actor model
- **Real distributed systems:** MapReduce, consensus algorithms (Paxos, Raft), distributed file systems

**For backend engineering at scale:** Every company of any size runs distributed systems. Understanding why Kafka, Redis, and databases with replication are architected the way they are, and being able to explain it, is the mark of a senior-thinking engineer at a junior or intermediate level. This course gives you that foundation.

---

## CMPUT 365: Introduction to Reinforcement Learning

**Why almost nobody takes it:** Students think RL is exotic and only for researchers. Or they just haven't heard of it.

**Why you should take it:** Richard Sutton is at UofA. He and Andrew Barto wrote *Reinforcement Learning: An Introduction*, which is THE textbook in the field, and it's available free online. Sutton is arguably the most influential living researcher in RL. Taking an RL course at an institution where Sutton works is a genuine privilege that most people walk right past.

Even if you never write an RL algorithm in your career:

- The framework for thinking about sequential decision-making under uncertainty is broadly applicable
- The mathematical foundations (Markov decision processes, Bellman equations, value functions) are used in robotics, finance (algorithmic trading), game AI, and recommendation systems
- RL is increasingly integrated with LLMs (RLHF, Reinforcement Learning from Human Feedback, is how ChatGPT was fine-tuned)

If you're heading into ML in any form, CMPUT 365 followed by 466 (Machine Learning) is one of the strongest academic preparation sequences you can do.

---

## Non-CMPUT Hidden Gems

These are outside the CS department but genuinely valuable.

### STAT 265: Probability Theory

More rigorous than STAT 151 and directly useful for ML, data science, and systems (reliability, performance modeling). Probability is the mathematical language of uncertainty, and working with data means working with uncertainty constantly. This is the most useful science elective most CS students don't take.

### MATH 225: Linear Algebra (Abstract / Group Theory)

Abstract algebra (groups, rings, fields) is the mathematical foundation for cryptography. If you're going into security or any crypto-adjacent work (blockchain, secure systems, applied cryptography), this is relevant. Also: it's a beautiful course that rewards mathematical maturity. Not for everyone, but for the right student it's excellent.

### PHIL 325: Formal Logic

Formal systems, proof theory, model theory. This overlaps with programming language theory, type systems, and formal verification. If you find yourself drawn to the theoretical side of CS (type systems, proof assistants, certified code), this is worth taking. Also counts as a humanities elective.

### ECE 340: Signals and Systems

If you ever work in audio processing, communications systems, digital signal processing, radio frequency (RF), or certain areas of ML (especially time-series or audio ML), this course is foundational. Fourier transforms, Laplace transforms, convolution, filter design. Most CS students never touch this. The ones who do have a rare skill.

### GEOPH 210: Introduction to Seismology (Mostly Kidding, Somewhat Serious)

Look: seismology is genuinely a data-heavy field. Seismic data processing involves signal processing, large datasets, pattern recognition, and time-series analysis. If you want a bizarre and interesting dataset to work with for personal projects, or if you're curious about scientific computing, a geophysics course is a left-field choice that has produced a few interesting data science portfolios. Edmonton is an energy hub and oil and gas companies hire data scientists. This is the "mostly kidding" entry, but the underlying point is real: niche domain knowledge plus CS skills is a powerful combination in unexpected industries.

---

## The Common Thread

Every course on this list has the same profile: not required by default, not widely advertised, but meaningful in a way that shows up in your work (and in interviews) years after you've taken it. The students who graduate with the strongest reputations (who get calls back from FAANG, who get hired at their dream startups) are usually the ones who took the hard optional courses and actually learned from them.

Most people take the path of least resistance. The courses on this list are the road less taken. Take them.
