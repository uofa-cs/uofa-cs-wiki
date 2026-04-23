---
title: "Course Catalogue"
hide:
  - navigation
  - toc
---

# Course Catalogue

Every CMPUT course in the UofA undergraduate and graduate calendar. Search by name or code, filter by year, topic area, difficulty, or industry relevance. Each card links to the full course page with the calendar description, prerequisites, and (where students have written one) a real review with professor recommendations and tips.

The catalogue pulls course data from the [UAlberta calendar](https://apps.ualberta.ca/catalogue/course/cmput); difficulty, workload, and industry-relevance ratings are synthesized from student reviews on r/uAlberta and RateMyProfessors.

<div class="course-catalogue" data-courses-url="courses.json">
  <div class="course-controls">
    <div class="course-search">
      <input
        type="search"
        id="course-search"
        placeholder="Search by code, title, or topic (e.g. '204', 'machine learning', 'graphics')…"
        autocomplete="off"
        spellcheck="false"
      />
    </div>
    <div class="course-filters">
      <label class="course-filter">
        <span class="course-filter-label">Year</span>
        <select id="filter-year">
          <option value="">All years</option>
          <option value="100">100-level</option>
          <option value="200">200-level</option>
          <option value="300">300-level</option>
          <option value="400">400-level</option>
          <option value="Graduate">Graduate</option>
        </select>
      </label>
      <label class="course-filter">
        <span class="course-filter-label">Topic</span>
        <select id="filter-topic">
          <option value="">All topics</option>
        </select>
      </label>
      <label class="course-filter">
        <span class="course-filter-label">Difficulty</span>
        <select id="filter-difficulty">
          <option value="">Any</option>
          <option value="Easy">Easy</option>
          <option value="Medium">Medium</option>
          <option value="Hard">Hard</option>
          <option value="Brutal">Brutal</option>
        </select>
      </label>
      <label class="course-filter">
        <span class="course-filter-label">Industry relevance</span>
        <select id="filter-relevance">
          <option value="">Any</option>
          <option value="Critical">Critical</option>
          <option value="High">High</option>
          <option value="Medium">Medium</option>
          <option value="Low">Low</option>
        </select>
      </label>
      <label class="course-filter course-filter--checkbox">
        <input type="checkbox" id="filter-reviewed" />
        <span>Only show reviewed courses</span>
      </label>
      <button type="button" id="filter-clear" class="course-clear">Clear filters</button>
    </div>
  </div>

  <p class="course-count" id="course-count">Loading courses…</p>

  <div class="course-grid" id="course-grid" role="list"></div>

  <p class="course-empty" id="course-empty" hidden>
    No courses match those filters. Try clearing one.
  </p>
</div>
