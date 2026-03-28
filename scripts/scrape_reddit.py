#!/usr/bin/env python3
"""Scrape r/uAlberta Reddit threads about CMPUT courses, profs, internships, and CS career advice."""

import json
import time
import urllib.request
import urllib.error
import os

OUTPUT_DIR = "/tmp/uofa-cs-wiki/sources/reddit"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Key threads to scrape
THREADS = [
    # Course advice and reviews
    ("cb8r0r", "good_and_bad_cmput_profs"),
    ("15i2dmm", "cmput_courses_advice"),
    ("1boo5cb", "300_cmput_course_recommendation"),
    ("1jdmatn", "last_year_cmput_course_recommendations"),
    ("wb9mvl", "deciding_cmput_courses"),
    ("13xfdth", "suggestions_cmput_courses"),
    ("1eg45db", "advice_cmput_201_272"),
    ("vbi9tg", "cmput301_229_204_one_sem"),
    ("uv7jov", "cmput_174_175_vs_274_275"),
    ("1eyq32p", "rate_my_cs_timetable"),
    ("bm9tbu", "hardest_cmput_course"),
    ("ruvwc6", "hardest_classes_ualberta"),
    ("5305ya", "struggling_cmput_204"),
    ("1l7cq8a", "how_brutal_cmput_379"),
    ("rket1r", "cmput_course_load"),
    ("kl25t9", "cmput_201_advice"),
    ("knjlmm", "advice_cmput_last_semester"),
    ("184rzfh", "is_cmput_101_hard"),
    ("1238he3", "cmput_101_difficulty"),
    ("o7clfw", "cmput_201_lin_or_buro"),
    ("18d7wju", "cmput_229_or_291"),
    ("17h9xqu", "possible_course_selection"),
    ("mgj0c9", "will_i_survive_229_301"),
    ("1jzj7yz", "cmput_301_3rd_year"),
    
    # Internships and careers
    ("18iwujb", "cs_internships_coops"),
    ("1i2bqd3", "computer_engineer_software_coop"),
    ("14ikahf", "internship_software_engineer_edmonton"),
    ("13ie0j9", "software_engineering_coop"),
    ("hej9p7", "cs_projects_internships"),
    ("11fd8z2", "cs_undergrads_coop_internship"),
    ("s2omhd", "coop_jobs_outside_edmonton"),
    ("i39ujv", "coop_internship_salary_thread"),
    ("1crkhd6", "how_does_coop_work"),
    ("e8qhwf", "uofa_coop_cs"),
]

# Additional search-based threads
SEARCH_QUERIES = [
    "CMPUT+easy+courses",
    "CMPUT+professor+recommendation",
    "cs+degree+worth+it",
    "cs+specialization+vs+honors",
    "edmonton+tech+jobs",
    "CMPUT+403+competitive+programming",
    "CMPUT+415+compiler",
    "CMPUT+313+networking",
    "CMPUT+382+GPU",
    "CMPUT+267+machine+learning",
    "CMPUT+466",
    "CMPUT+404+web",
    "CMPUT+379+operating+systems",
    "research+undergrad+cs",
    "NSERC+USRA+ualberta",
]

def extract_comments(data, depth=0):
    """Recursively extract comments from Reddit JSON."""
    comments = []
    if isinstance(data, dict):
        if data.get("kind") == "Listing":
            for child in data.get("data", {}).get("children", []):
                comments.extend(extract_comments(child, depth))
        elif data.get("kind") == "t1":
            comment_data = data.get("data", {})
            body = comment_data.get("body", "")
            if body and body != "[deleted]" and body != "[removed]":
                comments.append({
                    "author": comment_data.get("author", "[deleted]"),
                    "body": body,
                    "score": comment_data.get("score", 0),
                    "depth": depth,
                })
            # Process replies
            replies = comment_data.get("replies", "")
            if isinstance(replies, dict):
                comments.extend(extract_comments(replies, depth + 1))
    elif isinstance(data, list):
        for item in data:
            comments.extend(extract_comments(item, depth))
    return comments

def fetch_thread(thread_id, slug):
    """Fetch a Reddit thread and extract comments."""
    url = f"https://old.reddit.com/r/uAlberta/comments/{thread_id}/{slug}/.json?limit=500"
    headers = {"User-Agent": "UofA-CS-Wiki-Scraper/1.0"}
    
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
    except Exception as e:
        print(f"  ERROR fetching {thread_id}: {e}")
        return None
    
    # Extract post
    post_data = data[0]["data"]["children"][0]["data"]
    post = {
        "title": post_data.get("title", ""),
        "selftext": post_data.get("selftext", ""),
        "score": post_data.get("score", 0),
        "num_comments": post_data.get("num_comments", 0),
        "created_utc": post_data.get("created_utc", 0),
        "url": f"https://reddit.com/r/uAlberta/comments/{thread_id}/",
    }
    
    # Extract comments
    comments = []
    if len(data) > 1:
        comments = extract_comments(data[1])
    
    return {"post": post, "comments": comments}

def fetch_search(query):
    """Search r/uAlberta for a query and return thread IDs."""
    url = f"https://old.reddit.com/r/uAlberta/search.json?q={query}&restrict_sr=on&sort=relevance&t=all&limit=5"
    headers = {"User-Agent": "UofA-CS-Wiki-Scraper/1.0"}
    
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
    except Exception as e:
        print(f"  ERROR searching '{query}': {e}")
        return []
    
    results = []
    for child in data.get("data", {}).get("children", []):
        d = child.get("data", {})
        results.append({
            "id": d.get("id"),
            "title": d.get("title"),
            "selftext": d.get("selftext", "")[:500],
            "score": d.get("score", 0),
            "num_comments": d.get("num_comments", 0),
            "url": f"https://reddit.com{d.get('permalink', '')}",
        })
    return results

def thread_to_markdown(thread_data):
    """Convert thread data to readable markdown."""
    post = thread_data["post"]
    lines = []
    lines.append(f"# {post['title']}")
    lines.append(f"**Score:** {post['score']} | **Comments:** {post['num_comments']}")
    lines.append(f"**URL:** {post['url']}")
    lines.append("")
    if post["selftext"]:
        lines.append(post["selftext"])
        lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Comments")
    lines.append("")
    
    for c in sorted(thread_data["comments"], key=lambda x: x["score"], reverse=True):
        indent = "  " * c["depth"]
        lines.append(f"{indent}**u/{c['author']}** (score: {c['score']}):")
        for bodyline in c["body"].split("\n"):
            lines.append(f"{indent}> {bodyline}")
        lines.append("")
    
    return "\n".join(lines)

def main():
    print("=== Scraping Reddit threads ===")
    all_threads = {}
    
    # Fetch known threads
    for thread_id, slug in THREADS:
        print(f"Fetching: {slug} ({thread_id})")
        result = fetch_thread(thread_id, slug)
        if result:
            all_threads[thread_id] = result
            # Save individual markdown
            md = thread_to_markdown(result)
            with open(os.path.join(OUTPUT_DIR, f"{slug}.md"), "w") as f:
                f.write(md)
            print(f"  -> {len(result['comments'])} comments, score {result['post']['score']}")
        time.sleep(1.5)  # Rate limit
    
    # Search for additional threads
    print("\n=== Searching for additional threads ===")
    search_results = {}
    for query in SEARCH_QUERIES:
        print(f"Searching: {query}")
        results = fetch_search(query)
        search_results[query] = results
        
        # Fetch top results we haven't already scraped
        for r in results[:2]:
            tid = r["id"]
            if tid and tid not in all_threads:
                print(f"  Fetching new thread: {r['title'][:60]}...")
                result = fetch_thread(tid, "t")
                if result:
                    all_threads[tid] = result
                    safe_title = r["title"][:50].replace("/", "_").replace(" ", "_").lower()
                    md = thread_to_markdown(result)
                    with open(os.path.join(OUTPUT_DIR, f"search_{safe_title}.md"), "w") as f:
                        f.write(md)
                    print(f"    -> {len(result['comments'])} comments")
                time.sleep(1.5)
        time.sleep(1)
    
    # Save combined JSON for processing
    with open(os.path.join(OUTPUT_DIR, "all_threads.json"), "w") as f:
        json.dump(all_threads, f, indent=2)
    
    # Save search results
    with open(os.path.join(OUTPUT_DIR, "search_results.json"), "w") as f:
        json.dump(search_results, f, indent=2)
    
    print(f"\n=== Done! Scraped {len(all_threads)} threads ===")
    print(f"Output in: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
