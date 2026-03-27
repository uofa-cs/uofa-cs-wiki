# System Design

System design is one of those topics nobody teaches you in school, but industry expects you to know. This guide gives you the mental model, the core concepts, and a path to actually learn it.

---

## What Is System Design?

System design is the process of defining the architecture, components, and interactions of a large-scale software system to meet specific requirements. In interviews, it shows up as the classic "how would you build Twitter?" question. In real jobs, it's the decisions you make every day: where to put data, how services talk to each other, what happens when traffic spikes.

The interview version is a 45-minute open-ended conversation where you're expected to sketch out a system — databases, caching layers, APIs, queues — while discussing tradeoffs. There's no single correct answer. The goal is to show you understand how systems fail at scale and how to design around those failures.

The real-world version is less dramatic but just as important. You're deciding whether to add a cache, whether to split a service out, how to handle a database that's getting too slow. These decisions affect performance, reliability, and how much pain your team feels at 2am.

---

## Why UofA Doesn't Teach This

UofA's CS program teaches you the components. You'll learn operating systems, networks, databases, algorithms. What it doesn't teach you is how to combine them at scale for real-world systems.

This isn't a knock on UofA specifically — it's true of most CS programs. Academia focuses on fundamentals, which is correct. But it means you graduate knowing what a B-tree index is without knowing when to add one, knowing what TCP is without knowing how load balancers use it, knowing what a database transaction is without knowing what happens when you have ten million users hitting the same table.

System design bridges that gap. It's applied engineering judgment built on top of the fundamentals you learned in class.

---

## Why It Matters for Your Career

**For interviews:** Senior-level interviews almost always include system design rounds. But increasingly, even junior roles at FAANG and big tech companies include a basic system design component. If you're applying to Amazon, Google, Meta, Microsoft, or well-funded startups, expect to be asked something in this space — even as a new grad.

**For the actual job:** You will make architectural decisions from day one, even as a junior. "Should we store this in Redis or the database?" is a system design question. "Why is this API slow?" often has a system design answer. The engineers who get promoted fastest are the ones who understand how the pieces fit together, not just how to write code.

---

## Core Concepts

### Scalability

**Vertical scaling** means making one machine bigger — more CPU, more RAM, faster disks. It's easy to do and has no code changes, but it has a hard ceiling and a single point of failure.

**Horizontal scaling** means adding more machines and distributing load across them. It's more complex but theoretically unlimited. Most modern systems scale horizontally. The challenge is that your application needs to be stateless, or you need to share state (via a database or cache) across instances.

### Load Balancing

A load balancer sits in front of your servers and distributes incoming traffic across them. Common algorithms: round-robin, least connections, IP hash (useful when you need session stickiness).

In practice: nginx is used for this in many setups. AWS has the Application Load Balancer (ALB). You encounter load balancing the moment you have more than one server.

CMPUT 313 (Computer Networks) gives you the networking foundation to understand how traffic flows and where a load balancer sits in the stack.

### Caching

Caching is storing the result of an expensive operation so you don't have to repeat it. It's one of the highest-leverage performance improvements in any system.

**Redis** and **Memcached** are in-memory key-value stores used as caches. Redis is more feature-rich (supports sorted sets, pub/sub, persistence). Memcached is simpler and faster for pure caching.

**What to cache:** expensive database queries, results of external API calls, rendered HTML, session data. Don't cache things that change every request.

**Eviction policies:** LRU (Least Recently Used) is the most common. When the cache is full, evict the item that hasn't been accessed longest. LFU (Least Frequently Used) evicts items accessed least often. TTL (time-to-live) automatically expires entries after a set duration.

**CDNs** (Content Delivery Networks) are geographically distributed caches for static assets. Images, CSS, JavaScript — serve them from a CDN edge node close to the user instead of from your origin server. Cloudflare and AWS CloudFront are common choices.

Cache invalidation (knowing when to clear or update a cache) is famously one of the hard problems in computer science. Design for it from the start.

### Databases: SQL vs NoSQL

**SQL databases** (PostgreSQL, MySQL) are relational, ACID-compliant, and have been the default for decades. Use them when your data has clear relationships, when you need transactions, when you're not sure what you need. PostgreSQL can handle enormous scale with proper indexing and query optimization. Don't reach for NoSQL just because it sounds more scalable.

**NoSQL databases** come in several flavors:
- **Document stores** (MongoDB): store JSON-like documents. Good for flexible schemas.
- **Key-value stores** (DynamoDB, Redis): extremely fast for simple lookups by key.
- **Column-family stores** (Cassandra): optimized for write-heavy workloads and time-series data.
- **Graph databases** (Neo4j): for relationship-heavy data like social networks.

**Replication** copies data across multiple database nodes. Primary-replica setups let you scale reads by routing queries to replicas. If the primary fails, a replica can be promoted.

**Sharding** splits data across multiple databases by some key (e.g., user ID). It's complex and introduces new failure modes. Only shard when you've exhausted other options.

CMPUT 291/391 (Databases) gives you the foundations here. The gap is learning how these concepts extend to distributed, high-traffic scenarios.

### Message Queues

Message queues decouple services. Instead of Service A directly calling Service B, A drops a message in a queue and B processes it when ready. This makes systems more resilient — if B is slow or temporarily down, messages queue up rather than causing A to fail.

**Kafka** is the industry standard for high-throughput event streaming. Built for durability, replay, and massive scale. Used heavily in data pipelines.

**RabbitMQ** is a traditional message broker — simpler, good for task queues and background jobs.

**Amazon SQS** is AWS's managed queue service. Easy to use if you're already on AWS.

Common use cases: sending emails asynchronously, processing payments in the background, fan-out notifications to many subscribers.

### Microservices vs Monolith

A **monolith** is one codebase that does everything. A **microservices** architecture splits the application into many small, independently deployable services.

The correct take: start with a monolith. Microservices solve organizational and scaling problems that startups and most mid-sized companies don't have yet. They add enormous operational complexity — service discovery, distributed tracing, inter-service authentication, network latency between services.

If you're designing a system in an interview or in a new project, a well-structured monolith is a defensible and often correct answer. Migrate to microservices when you have a specific problem that justifies the complexity.

### API Design

**REST** is the dominant API style. Resources are nouns, HTTP verbs (GET, POST, PUT, DELETE) are actions. Stateless. Easy to cache. Most web APIs are REST.

**GraphQL** lets clients request exactly the data they need. Useful when you have many different clients (web, mobile, third-party) with different data requirements. Adds complexity on the server side.

**gRPC** uses Protocol Buffers (binary format) and HTTP/2. Much faster than REST for internal service-to-service communication. Not human-readable, so harder to debug. Common in microservices backends.

### CAP Theorem

The CAP theorem states that a distributed system can only guarantee two of three properties: **Consistency**, **Availability**, and **Partition Tolerance**.

Since network partitions (split-brain scenarios) are unavoidable in distributed systems, you're really choosing between CP (consistent but may be unavailable during partitions) and AP (always available but may return stale data during partitions).

**CP systems** (e.g., HBase, Zookeeper): return an error rather than stale data.
**AP systems** (e.g., Cassandra, DynamoDB): return the best available data even if potentially stale.

Which you choose depends on your use case. A bank should probably be CP. A social media feed can be AP.

### Rate Limiting and Authentication at Scale

**Rate limiting** protects your APIs from abuse and overload. Common algorithms: token bucket (users get tokens that replenish over time), sliding window (track requests in a rolling time window). At scale, rate limiters are implemented in Redis so they work across multiple server instances.

**Authentication at scale** typically uses JWTs (JSON Web Tokens) — stateless tokens that contain claims and are verified cryptographically, without hitting a database on every request. OAuth 2.0 is the standard for third-party auth. At the infrastructure level, API gateways (Kong, AWS API Gateway) handle auth, rate limiting, and routing in one place.

---

## How UofA Courses Connect

| Course | System Design Relevance |
|---|---|
| CMPUT 313 – Computer Networks | Load balancing, CDNs, DNS, HTTP internals |
| CMPUT 291/391 – Databases | Database design, indexing, transactions, replication |
| CMPUT 379 – Operating Systems | Process management, memory, file systems, I/O |
| CMPUT 481 – Distributed Systems | The most directly relevant course — Paxos, CAP theorem, distributed consensus |

Take CMPUT 481 if you can. It's the closest thing UofA has to formal system design education, and it covers the theoretical foundations that explain why distributed systems behave the way they do.

---

## Resources

**"Designing Data-Intensive Applications" by Martin Kleppmann** — This is the book. It's dense but comprehensive. Covers databases, replication, partitioning, distributed transactions, stream processing. Read this and you'll have a stronger foundation than most practicing engineers. Read chapters relevant to what you're studying, not necessarily cover to cover.

**System Design Primer (GitHub)** — Free, open source, covers all the major topics with diagrams. Good starting point. Search "system design primer" on GitHub. The README alone is worth bookmarking.

**ByteByteGo** — Alex Xu's YouTube channel and newsletter. Visual, well-explained, covers specific systems (URL shortener, YouTube, etc.). The newsletter is free and worth subscribing to.

**Grokking the System Design Interview (Educative)** — Paid but often discounted. Good structured practice problems with worked solutions. Useful specifically for interview prep.

---

## When to Start

After second year, once you've taken networks and databases, you have enough foundation to start learning system design meaningfully. You don't need to wait until you're interviewing.

A reasonable timeline:
- **2nd year:** Read the System Design Primer. Understand load balancing, caching, database basics.
- **3rd year:** Start working through Kleppmann's book. Practice designing simple systems on paper.
- **4th year / before interviews:** Mock system design interviews. Practice talking through your reasoning out loud.

---

## How to Practice

The most effective practice is designing systems from scratch, explaining your reasoning, and then comparing your design to known approaches.

**Start with a URL shortener.** It's the "hello world" of system design. You need to handle a massive number of read requests, generate short codes, store mappings. It touches caching, databases, hashing, and horizontal scaling.

**Then design a chat app.** Real-time messaging, presence (online/offline status), message history. Introduces WebSockets, pub/sub messaging, and the complexity of ordering messages across distributed nodes.

**Then design a ride-sharing system.** Location tracking, matching drivers to riders, surge pricing, notifications. Involves geospatial queries, event streaming, real-time updates.

For each design: start by clarifying requirements (how many users? read-heavy or write-heavy?), estimate scale, identify the core bottlenecks, pick the components that solve those bottlenecks, and discuss tradeoffs. This is exactly what a good system design interview looks like.
