---
title: "CMPUT 382 — Introduction to GPU Programming"
course_code: CMPUT 382
course_year: "300"
course_topics:
  - Systems
  - Programming
course_difficulty: Medium
course_workload: Moderate
course_relevance: High
course_units: "3 units (fi 6)(EITHER, 3-0-3)"
hide:
  - navigation
---

# CMPUT 382 — Introduction to GPU Programming

*3 units (fi 6)(EITHER, 3-0-3)*

**Difficulty:** Medium • **Workload:** Moderate • **Industry relevance:** High

## Calendar Description

Graphics processing units (GPU) can be programmed like a coprocessor to solve non-graphics problems, including voice recognition, computational physics, convolutional neural networks, and machine learning. The many processing cores of a GPU support a high-degree of parallelism. Course topics include hardware architecture, algorithmic design, programming languages (e.g., CUDA, OpenCL), and principles of programming for GPUs for high performance. Prerequisites: CMPUT 201 or 275, and one of CMPUT 229, E E 380, or ECE 212.

## Prerequisites

Prerequisites: CMPUT 201 or 275, and one of CMPUT 229, E E 380, or ECE 212.

## Student Review

**Difficulty:** Medium | **Workload:** Moderate | **Industry relevance:** High (niche but rare)

CUDA programming, GPU architecture, parallel algorithms. Not widely discussed on Reddit because not many students take it. The few who have report that labs take the full 3 hours but the course isn't disproportionately harder than other 300-level courses. Disorganized in some past offerings.

**Student tips:**
- The ability to write GPU code is genuinely rare among CS graduates. This is a strong differentiator if you're going into ML infrastructure, HPC, or graphics.
- Background in 229 (computer organization) helps significantly; GPU optimization requires understanding what hardware is actually doing.

## Why It's a Hidden Gem

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

## Related Pages

- [Course Catalogue](./index.md)
- [Course Guide](../course-guide.md)
- [Hidden Gems](../hidden-gems.md)
- [Professor Guide](../professor-guide.md)

_Calendar source: <https://apps.ualberta.ca/catalogue/course/cmput/382>_
