---
title: "CMPUT 391 — Database Management Systems"
course_code: CMPUT 391
course_year: "300"
course_topics:
  - Databases
course_units: "3 units (fi 6)(EITHER, 3-0-3)"
hide:
  - navigation
---

# CMPUT 391 — Database Management Systems

*3 units (fi 6)(EITHER, 3-0-3)*

## Calendar Description

This course covers the implementation of RDBMSs and some non- relational data models, along with their query languages. Topics: compilation, execution, and optimization of SQL queries; concurrent execution of transactions; indexing; advanced constructs in SQL; semi-structured data models and query languages; distributed and parallel databases; NoSQL and cloud-based database systems. Prerequisites: CMPUT 201 and 204, or 275; and CMPUT 291.

## Prerequisites

Prerequisites: CMPUT 201 and 204, or 275; and CMPUT 291.

## Why It's a Hidden Gem

**Why almost nobody takes it:** Students take CMPUT 291, learn SQL, and think they're done with databases. They're not.

**Availability note:** CMPUT 391 has not been taught in recent semesters, so plan around limited or uncertain scheduling.

**Why you should take it:** CMPUT 291 teaches you to use databases. CMPUT 391 teaches you how databases actually work. That's a different thing, and it matters enormously:

- **Query optimization:** how the query planner decides to execute your SQL, what indexes actually do internally (B-trees), why certain queries are slow and how to fix them
- **Transaction management:** ACID properties, isolation levels, deadlock detection, why "just use a transaction" is not a sufficient answer
- **Concurrency control:** how multiple simultaneous queries don't corrupt your data
- **Distributed databases:** how data gets replicated, partitioned (sharding), and kept consistent across nodes. CAP theorem. This is the foundation for understanding systems like Cassandra, DynamoDB, and CockroachDB.

**For data engineering and backend roles:** This is the difference between a developer who can write SQL and a developer who understands why their queries are slow and how to design schemas that perform at scale. The latter is significantly more valuable and significantly rarer.

When you're debugging a slow query in production at 2am, you want to know what an execution plan is. This course is where you learn that.

## Related Pages

- [Course Catalogue](./index.md)
- [Course Guide](../course-guide.md)
- [Hidden Gems](../hidden-gems.md)
- [Professor Guide](../professor-guide.md)

_Calendar source: <https://apps.ualberta.ca/catalogue/course/cmput/391>_
