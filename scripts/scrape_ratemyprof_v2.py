#!/usr/bin/env python3
"""Scrape RateMyProfessors data for UofA CS professors using correct school ID."""

import json
import os
import urllib.request
import time

OUTPUT_DIR = "/tmp/uofa-cs-wiki/sources/ratemyprof"
os.makedirs(OUTPUT_DIR, exist_ok=True)

RMP_API = "https://www.ratemyprofessors.com/graphql"

# Try both school IDs
SCHOOL_IDS = [
    "U2Nob29sLTE0MDc=",  # School-1407
    "U2Nob29sLTE0NjA=",  # School-1460
]

PROFESSORS = [
    "Zaiane", "Buro", "Guohui Lin", "Paul Lu", "Lorna Stewart",
    "Martin Mueller", "Mario Nascimento", "Abram Hindle", "Hazel Campbell",
    "Zachary Frizell", "James Hoover", "Ioanis Nikolaidis", "Davood Rafiei",
    "Joerg Sander", "Eleni Stroulia", "Omid Ardakanian", "Adam White",
    "Matthew Taylor", "Martha White", "Nidhi Hegde", "Karim Ali",
    "Sarah Nadi", "Jose Nelson Amaral", "Jonathan Schaeffer", "Rich Sutton",
    "Michael Bowling", "Dale Schuurmans", "Csaba Szepesvari", "Randy Goebel",
    "Denilson Barbosa", "Lei Ma", "Di Niu", "Russ Greiner", "Ken Wong",
    "Leah Hackman", "Ehab Elmallah",
]

def search_prof(name, school_id):
    query = json.dumps({
        "query": "query NewSearchTeachersQuery($text: String!, $schoolID: ID!) { newSearch { teachers(query: {text: $text, schoolID: $schoolID}) { edges { cursor node { id legacyId firstName lastName school { name } department avgRating avgDifficulty numRatings wouldTakeAgainPercent teacherRatingTags { tagName tagCount } } } } } }",
        "variables": {"text": name, "schoolID": school_id}
    }).encode()
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic dGVzdDp0ZXN0",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        "Referer": "https://www.ratemyprofessors.com/",
        "Origin": "https://www.ratemyprofessors.com",
    }
    
    req = urllib.request.Request(RMP_API, data=query, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            if "errors" in data:
                print(f"  GraphQL errors: {data['errors']}")
                return []
            edges = data.get("data", {}).get("newSearch", {}).get("teachers", {}).get("edges", [])
            return [e["node"] for e in edges]
    except urllib.error.HTTPError as e:
        body = e.read().decode()[:200]
        print(f"  HTTP {e.code}: {body}")
        return []
    except Exception as e:
        print(f"  Error: {e}")
        return []

def get_ratings(prof_id):
    query = json.dumps({
        "query": "query RatingsListQuery($id: ID!) { node(id: $id) { ... on Teacher { ratings(first: 20) { edges { node { comment date class helpfulRating clarityRating difficultyRating wouldTakeAgain grade thumbsUpTotal thumbsDownTotal } } } } } }",
        "variables": {"id": prof_id}
    }).encode()
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic dGVzdDp0ZXN0",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        "Referer": "https://www.ratemyprofessors.com/",
        "Origin": "https://www.ratemyprofessors.com",
    }
    
    req = urllib.request.Request(RMP_API, data=query, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            return data.get("data", {}).get("node", {}).get("ratings", {}).get("edges", [])
    except Exception as e:
        print(f"  Ratings error: {e}")
        return []

def main():
    print("=== RateMyProfessors Scraper v2 ===")
    all_profs = {}
    
    for school_id in SCHOOL_IDS:
        print(f"\nTrying school ID: {school_id}")
        
        for name in PROFESSORS:
            if name in all_profs:
                continue
            print(f"  Searching: {name}")
            results = search_prof(name, school_id)
            
            for r in results:
                dept = (r.get("department") or "").lower()
                school = (r.get("school", {}) or {}).get("name", "").lower()
                if "albert" in school and ("comput" in dept or not dept):
                    full_name = f"{r['firstName']} {r['lastName']}"
                    print(f"    Found: {full_name} | {r.get('avgRating')}/5 | {r.get('numRatings')} ratings | Diff: {r.get('avgDifficulty')}/5 | WTA: {r.get('wouldTakeAgainPercent')}%")
                    
                    # Get detailed ratings
                    ratings = get_ratings(r["id"])
                    r["reviews"] = [e["node"] for e in ratings]
                    all_profs[full_name] = r
                    break
            
            time.sleep(0.3)
    
    # Save JSON
    with open(os.path.join(OUTPUT_DIR, "all_professors.json"), "w") as f:
        json.dump(all_profs, f, indent=2, default=str)
    
    # Generate markdown summary
    lines = ["# UofA CS Professor Ratings (RateMyProfessors)\n"]
    lines.append("| Professor | Rating | Difficulty | Would Take Again | # Ratings |")
    lines.append("|-----------|--------|------------|-----------------|-----------|")
    
    for name, data in sorted(all_profs.items(), key=lambda x: x[1].get("avgRating", 0) or 0, reverse=True):
        rating = data.get("avgRating", "N/A")
        diff = data.get("avgDifficulty", "N/A")
        wta = data.get("wouldTakeAgainPercent", -1)
        wta_str = f"{wta:.0f}%" if isinstance(wta, (int, float)) and wta >= 0 else "N/A"
        num = data.get("numRatings", 0)
        lines.append(f"| {name} | {rating}/5 | {diff}/5 | {wta_str} | {num} |")
    
    lines.append("")
    
    # Individual prof details
    for name, data in sorted(all_profs.items()):
        lines.append(f"\n## {name}")
        lines.append(f"**Rating:** {data.get('avgRating', 'N/A')}/5 | **Difficulty:** {data.get('avgDifficulty', 'N/A')}/5 | **Would Take Again:** {data.get('wouldTakeAgainPercent', 'N/A')}% | **Ratings:** {data.get('numRatings', 0)}")
        
        tags = data.get("teacherRatingTags", [])
        if tags:
            top_tags = sorted(tags, key=lambda x: x.get("tagCount", 0), reverse=True)[:6]
            lines.append(f"**Tags:** {', '.join(t['tagName'] + ' (' + str(t['tagCount']) + ')' for t in top_tags)}")
        
        reviews = data.get("reviews", [])
        if reviews:
            lines.append("\n**Selected Reviews:**\n")
            for rev in reviews[:8]:
                course = rev.get("class", "N/A")
                grade = rev.get("grade", "N/A")
                diff = rev.get("difficultyRating", "N/A")
                comment = rev.get("comment", "").strip()
                if comment:
                    lines.append(f"- **{course}** (Grade: {grade}, Diff: {diff}/5): {comment[:300]}")
        lines.append("")
    
    with open(os.path.join(OUTPUT_DIR, "summary.md"), "w") as f:
        f.write("\n".join(lines))
    
    print(f"\n=== Done! Found {len(all_profs)} professors ===")

if __name__ == "__main__":
    main()
