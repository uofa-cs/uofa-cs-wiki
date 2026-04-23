---
title: "CMPUT 313 — Computer Networks"
course_code: CMPUT 313
course_year: "300"
course_topics:
  - Networks
course_difficulty: Medium
course_workload: Moderate
course_relevance: High
course_units: "3 units (fi 6)(EITHER, 3-0-3)"
hide:
  - navigation
---

# CMPUT 313 — Computer Networks

*3 units (fi 6)(EITHER, 3-0-3)*

**Difficulty:** Medium • **Workload:** Moderate • **Industry relevance:** High

## Calendar Description

Introduction to computer communication networks; protocols for error and flow control; wired and wireless medium access protocols; routing and congestion control; internet architecture and protocols; multimedia transmission; recent advances in networking. Prerequisites: CMPUT 201 and 204, or 275; one of CMPUT 229, E E 380, or ECE 212; and one of STAT 151, 161, 181, 235, 265, SCI 151, or MATH 181.

## Prerequisites

Prerequisites: CMPUT 201 and 204, or 275; one of CMPUT 229, E E 380, or ECE 212; and one of STAT 151, 161, 181, 235, 265, SCI 151, or MATH 181.

## Student Review

**Difficulty:** Medium | **Workload:** Moderate | **Industry relevance:** Medium-High

TCP/IP, routing, DNS, the OSI model, socket programming. Often cited as "boring but useful." Students who go on to do backend or infrastructure work often say they wished they'd paid more attention.

"313 is drier than the desert. Not much relevancy to modern hands-on networking unless you want to get deep into network protocols." But counter-view: "After 313, I finally understood what actually happens when you type a URL."

**Best profs:**
- **Ioanis Nikolaidis (3.5/5):** entertaining, goes on tangents (many interesting), assignments are tough but rewarding. Students who took him for 379 also spoke highly of him. When available, he's a significant upgrade.

**Avoid:**
- **Ehab Elmallah (2.4/5):** dry, monotone, slides ripped straight from the textbook, and teaches "extremely outdated" networking content. Grading criteria described as inconsistent. "Holy shit do I not like his style of teaching." Students who chose 379 (OS) over 313 partly because of Elmallah.

**Student tips:**
- This course pairs well with 379 (operating systems); they cover complementary systems content.
- The concepts are more directly applicable to industry than the course's reputation suggests.

## Why It's a Hidden Gem

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

## Related Pages

- [Course Catalogue](./index.md)
- [Course Guide](../course-guide.md)
- [Hidden Gems](../hidden-gems.md)
- [Professor Guide](../professor-guide.md)

_Calendar source: <https://apps.ualberta.ca/catalogue/course/cmput/313>_
