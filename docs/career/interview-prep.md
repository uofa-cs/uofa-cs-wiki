# Software Engineering Interview Prep

The most common mistake UofA CS students make with interview prep is either doing too much of the wrong thing (grinding 500 random LeetCode problems) or doing nothing until two weeks before an interview. This guide gives you a realistic, structured approach that actually works.

---

## The LeetCode Trap

"Just grind LeetCode" is bad advice. Not because LeetCode is wrong, but because the way most people use it is wrong.

The grind approach: open a random problem, get stuck, look at the solution, feel bad, open another one. Repeat for months. You end up having seen hundreds of problems without deeply understanding any pattern. In an actual interview, when you see a problem you haven't seen before, you freeze.

The pattern approach: learn the 10-12 core patterns that cover 90% of interview problems. Practice enough problems per pattern to deeply understand it. When you see a new problem, you recognize which pattern applies and execute.

**Do 150 problems well, not 500 problems poorly.**

---

## The Core Patterns

Every technical interview problem you'll encounter in a software engineering interview maps to one or more of these patterns. Learn them in roughly this order:

### Two Pointers
Used for problems on arrays or strings where you need to find a pair, triplet, or subarray with some property. Classic examples: two sum on sorted array, removing duplicates, container with most water. The key insight: use two indices that move toward or away from each other based on a condition.

### Sliding Window
A subtype of two pointers, specifically for contiguous subarrays or substrings. Fixed-size window for problems like "max sum of k elements." Variable-size window for problems like "longest substring without repeating characters." Know when to shrink the window.

### Binary Search
Don't think of this as just "search in a sorted array." Think of it as "eliminate half the search space at every step." Applications: searching rotated arrays, finding the minimum in a rotated sorted array, binary search on the answer (when you're asked to minimize/maximize something). CMPUT 204 covers this; go back to those notes.

### Tree Traversal
You need BFS and DFS cold. Recursive DFS for most tree problems (pre-order, in-order, post-order). Iterative BFS with a queue for level-order problems. Know what information flows up vs. down in recursive tree problems. Common patterns: finding the lowest common ancestor, validating a BST, calculating tree diameter.

### Graph Algorithms
BFS for shortest path in unweighted graphs, level-order traversal. DFS for connected components, cycle detection, topological sort. Dijkstra's for weighted shortest path. Union-Find (disjoint set) for connected components and cycle detection in undirected graphs (this shows up more than students expect). Topological sort for dependency ordering. CMPUT 204 covers all of these; seriously review that course content.

### Dynamic Programming
The pattern that scares people the most and is most over-studied before it clicks. Start with memoization (top-down recursion + caching). Once you understand why memoization works, rewrite as tabulation (bottom-up DP table). Classic problems to master: climbing stairs, coin change, knapsack, longest common subsequence, longest increasing subsequence, edit distance. The key question: what is the subproblem? What information do I need to solve a smaller version of this problem?

### Stack and Queue Patterns
Stacks for: valid parentheses, monotonic stack problems (next greater element, largest rectangle in histogram), expression evaluation. Queues for: BFS (which you already know). Deques (double-ended queues) for: sliding window maximum. Recognize "I need to maintain a decreasing/increasing sequence" as a monotonic stack problem.

### Heap / Priority Queue
Two use cases that appear constantly: (1) finding k-th largest/smallest elements, (2) merging k sorted lists or streams. Python's `heapq` module is a min-heap by default; to simulate a max-heap, negate values. Know the difference between pushing onto a heap vs. replacing the root.

### Backtracking
Used for generating all possible configurations: permutations, combinations, subsets, N-queens, sudoku solver. The pattern: make a choice, recurse, undo the choice. Know how to prune branches early to avoid re-exploring invalid states.

### Greedy Algorithms
When locally optimal choices lead to a globally optimal solution. Common problems: interval scheduling (sort by end time, pick greedily), jump game, task scheduler. The hard part of greedy: proving it works, which you don't need to do in an interview, but you need to develop intuition for when greedy applies vs. when you need DP.

---

## The UofA Advantage

You're not starting from zero. Two UofA courses directly map to interview prep:

**CMPUT 204 (Algorithms I):** Covers sorting, graph algorithms (BFS, DFS, Dijkstra, Bellman-Ford), dynamic programming, greedy algorithms. If you paid attention and did the assignments, you already know the theory behind most interview patterns. Go back to your CMPUT 204 notes and review the algorithms before you start LeetCode.

**CMPUT 403 (Competitive Programming):** This is the most directly useful course for technical interviews in the entire CS program. It trains you to solve algorithmic problems under time pressure, which is exactly what technical interviews test. If you haven't taken it and you're career-focused, put it on your schedule.

---

## A Realistic Study Plan

**3 months before you want to interview:**

Month 1: Work through the NeetCode 150 (free roadmap at neetcode.io). The problems are organized by pattern, which is exactly how you should be learning. Do the video explanation for each pattern, then try the problems. For the first week, focus on arrays and hashing, two pointers, and sliding window. These are the most common patterns in screening rounds.

Month 2: Complete the NeetCode 150. Focus on trees, graphs, and dynamic programming: these are the hardest categories and need the most repetition. Time yourself: 20-30 minutes per problem in practice. If you're past 30 minutes and stuck, look at the approach (not the full solution), then try again.

Month 3: Review patterns you're weakest on. Do a few problems in each category you haven't touched in a while. Start doing practice sessions where you solve 2 problems in 45 minutes (simulating a phone screen). Begin mock interviews.

**Ongoing:** Easy problems should take under 15 minutes. If they don't, you need more practice on fundamentals. Medium problems are the bread and butter of real interviews; most of your prep time should go here. Hard problems appear rarely outside of Google-level interviews. Don't sacrifice medium practice for hard problem grinding.

---

## System Design Interviews

For internships at most companies, you won't face formal system design rounds. For new grad roles at larger companies (Amazon, Google, Shopify, Clio at the senior intern/new grad level), system design starts appearing.

The questions are high-level: "Design a URL shortener." "Design a notification system." "Design a social media feed." You're not expected to have a perfectly architected answer; you're expected to demonstrate structured thinking.

A solid approach to any system design question:
1. Clarify requirements (functional and non-functional: scale, latency, consistency requirements)
2. Estimate scale (users, requests per second, data size)
3. High-level design (client, load balancer, services, database, cache)
4. Deep dive into key components (database schema, API design, caching strategy)
5. Discuss tradeoffs

The best preparation resource is **"Designing Data-Intensive Applications" by Martin Kleppmann.** Read it. It covers databases, replication, consistency models, message queues, and stream processing at a depth that makes system design interviews feel manageable. It's also just a genuinely important book for understanding how real software systems work.

Common system design topics to be comfortable with: SQL vs. NoSQL tradeoffs, caching (where to put it, what to cache, cache invalidation), horizontal vs. vertical scaling, CDNs, message queues, API design (REST vs. GraphQL).

---

## Behavioral Interviews

Technical ability gets you through the coding round. Behavioral interviews determine whether you get the offer.

Use the **STAR format** for every behavioral answer: Situation, Task, Action, Result.

Prepare stories for these prompts (you'll face one or more of them at every company):
- A time you faced a technical challenge and how you resolved it
- A time you disagreed with a teammate or manager
- A project you're proud of and why
- A failure or mistake and what you learned
- A time you had to learn something quickly under pressure
- A time you delivered under a deadline

UofA gives you material here. CMPUT 301 and CMPUT 401 group projects involve real collaboration under deadlines. CMPUT 401 specifically has client-facing work. These are legitimate stories.

Be specific. "I worked on a project" is not a STAR story. "In CMPUT 401, our team had a client who changed the requirements two weeks before the final demo. I proposed we scope down to the core feature set and communicated this clearly to the client. We shipped on time and the client was satisfied" is a STAR story.

---

## Company-Specific Notes

**Amazon:** Heavy on behavioral questions. They use their Leadership Principles as the framework (Customer Obsession, Deliver Results, Bias for Action, etc.). Prepare STAR stories that align with these. Technical interviews are LeetCode medium difficulty. The OA (online assessment) is two problems in 90 minutes; practice timed sessions.

**Google:** Notoriously difficult. Problems can be genuinely hard. LeetCode hard is not uncommon. The saving grace is that the interview process is more conversational than other companies; talking through your thinking matters. Apply early in your degree, accept you might not pass, treat it as learning, and try again.

**Microsoft:** Similar difficulty to Amazon. Mix of behavioral and technical. LeetCode medium is the right bar to prepare for.

**Shopify:** Strong engineering culture. Problems are practical; they want to see you write good, readable code. Less pure algorithm, more "show me you can build things." Their take-home projects (if assigned) should be treated seriously.

**Canadian mid-size companies (Clio, Wealthsimple, Benevity):** More practical coding, less pure LeetCode. Take-home projects are common. Focus on writing clean code and being able to explain your decisions.

**Edmonton companies (Jobber, AltaML, ATB):** Generally more relaxed interview processes than FAANG. Often: HR screen, one or two technical rounds focused on practical coding and conversation, possibly a take-home. Less likely to encounter hard algorithmic problems. Still prepare; don't walk in without having reviewed fundamentals.

---

## The Interview Itself

**Phone screen format:** Usually 45 minutes. One or two coding problems in a shared editor (Coderpad, HackerRank, Google Docs depending on the company). Talk out loud as you think. Start with a brute-force approach and state the time complexity before optimizing. Interviewers want to see your thinking process, not just your final answer.

**Virtual on-site:** Multiple back-to-back rounds, 45-60 minutes each. May include system design, behavioral, and multiple coding rounds. Take short mental breaks between rounds if you can. It's a long day.

**When you're stuck in an interview:** Say something. "I'm thinking about how to approach the subproblem of X" is better than silence. Ask clarifying questions. State the brute-force solution and its complexity before asking if you should optimize. Interviewers almost always prefer engaged thinking to quiet staring.

---

## Mock Interviews: Do Not Skip This

Writing code silently to yourself is completely different from explaining your approach out loud while someone watches. Most students discover this the hard way in their first real interview.

Practice talking through problems with another person before you interview.

**Free options:**
- **Pramp** (pramp.com): Peer-to-peer mock interviews, free, matches you with another student at a similar level.
- **Interviewing.io** (interviewing.io): Anonymous mock interviews with real engineers. Some free sessions.
- **Classmates:** Find one or two people who are also preparing and do weekly mock sessions. Take turns being interviewer and interviewee.

Even doing two or three mock interviews dramatically improves performance in real ones.

---

## After Rejection

You will get rejected. Multiple times. From companies you felt great about after the interview.

Technical interviews have significant randomness. A problem that's easy for you might match a gap in someone else's knowledge. An interviewer who had a bad morning affects the interview. Someone internal referred a different candidate. Rejection is not a verdict on your ability.

Ask for feedback after rejection; most companies won't give detailed feedback due to legal caution, but some will. Worth asking politely.

Standard wait periods before reapplying: 6 months for most companies, 12 months for Google and Amazon. Track when you applied so you know when you're eligible to try again.

The students who land good offers are rarely the ones who got it on the first try. They're the ones who kept preparing, kept applying, and treated every interview, successful or not, as a calibration point.

---

## Summary

1. Learn patterns, not random problems. Use NeetCode 150 as your roadmap.
2. Start preparing 3 months before you want to interview.
3. Do timed practice sessions. Simulate real interview conditions.
4. Do mock interviews with another person before your first real interview.
5. Prepare STAR stories for behavioral rounds.
6. Apply broadly; the interview-to-offer rate at any individual company is low.
7. Rejection is normal. Keep going.
