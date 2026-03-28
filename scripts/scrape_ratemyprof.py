#!/usr/bin/env python3
"""Scrape RateMyProfessors data for UofA CS professors."""

import json
import os
import urllib.request
import urllib.error
import time

OUTPUT_DIR = "/tmp/uofa-cs-wiki/sources/ratemyprof"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# RateMyProfessors GraphQL API
RMP_API = "https://www.ratemyprofessors.com/graphql"

# UofA school ID on RMP
UOFA_SCHOOL_ID = "U2Nob29sLTE0NjA="  # Base64 encoded School-1460

# Known CMPUT professors to search for
PROFESSORS = [
    "Osmar Zaiane",
    "Michael Buro",
    "Guohui Lin",
    "Paul Lu",
    "Lorna Stewart",
    "Martin Mueller",
    "Mario Nascimento",
    "Abram Hindle",
    "Hazel Campbell",
    "Nelson Chicken",
    "Zachary Frizell",
    "James Hoover",
    "Ioanis Nikolaidis",
    "Davood Rafiei",
    "Joerg Sander",
    "Eleni Stroulia",
    "Omid Ardakanian",
    "Adam White",
    "Matthew Taylor",
    "Martha White",
    "Nidhi Hegde",
    "Karim Ali",
    "Sarah Nadi",
    "Jose Nelson Amaral",
    "Jonathan Schaeffer",
    "Rich Sutton",
    "Michael Bowling",
    "Dale Schuurmans",
    "Csaba Szepesvari",
    "Randy Goebel",
    "Denilson Barbosa",
    "Menghan Hu",
    "Lei Ma",
    "Di Niu",
    "Zichen Wang",
    "Russ Greiner",
    "Ken Wong",
    "Joe Gualtieri",
    "Mani Fathian",
    "Xiaoqi Tan",
]

def search_professor(name):
    """Search for a professor on RMP using their GraphQL API."""
    query = {
        "query": """
        query SearchTeacher($text: String!, $schoolID: ID!) {
            newSearch {
                teachers(query: {text: $text, schoolID: $schoolID}) {
                    edges {
                        node {
                            id
                            firstName
                            lastName
                            department
                            avgRating
                            avgDifficulty
                            numRatings
                            wouldTakeAgainPercent
                            legacyId
                        }
                    }
                }
            }
        }
        """,
        "variables": {
            "text": name,
            "schoolID": UOFA_SCHOOL_ID
        }
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic dGVzdDp0ZXN0",
        "User-Agent": "Mozilla/5.0",
    }
    
    data = json.dumps(query).encode()
    req = urllib.request.Request(RMP_API, data=data, headers=headers, method="POST")
    
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode())
            edges = result.get("data", {}).get("newSearch", {}).get("teachers", {}).get("edges", [])
            return [e["node"] for e in edges]
    except Exception as e:
        print(f"  ERROR searching '{name}': {e}")
        return []

def get_professor_ratings(prof_id):
    """Get detailed ratings for a professor."""
    query = {
        "query": """
        query GetProfessor($id: ID!) {
            node(id: $id) {
                ... on Teacher {
                    id
                    firstName
                    lastName
                    department
                    avgRating
                    avgDifficulty
                    numRatings
                    wouldTakeAgainPercent
                    teacherRatingTags {
                        tagName
                        tagCount
                    }
                    courseCodes {
                        courseName
                        courseCount
                    }
                    ratings(first: 20) {
                        edges {
                            node {
                                comment
                                date
                                class
                                helpfulRating
                                clarityRating
                                difficultyRating
                                ratingTags
                                wouldTakeAgain
                                grade
                                isForOnlineClass
                                thumbsUpTotal
                                thumbsDownTotal
                            }
                        }
                    }
                }
            }
        }
        """,
        "variables": {
            "id": prof_id
        }
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic dGVzdDp0ZXN0",
        "User-Agent": "Mozilla/5.0",
    }
    
    data = json.dumps(query).encode()
    req = urllib.request.Request(RMP_API, data=data, headers=headers, method="POST")
    
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read().decode())
            return result.get("data", {}).get("node", {})
    except Exception as e:
        print(f"  ERROR getting ratings: {e}")
        return {}

def prof_to_markdown(prof_data):
    """Convert professor data to markdown."""
    lines = []
    name = f"{prof_data.get('firstName', '')} {prof_data.get('lastName', '')}"
    lines.append(f"## {name}")
    lines.append(f"**Department:** {prof_data.get('department', 'N/A')}")
    lines.append(f"**Overall Rating:** {prof_data.get('avgRating', 'N/A')}/5")
    lines.append(f"**Difficulty:** {prof_data.get('avgDifficulty', 'N/A')}/5")
    lines.append(f"**Would Take Again:** {prof_data.get('wouldTakeAgainPercent', 'N/A')}%")
    lines.append(f"**Number of Ratings:** {prof_data.get('numRatings', 0)}")
    lines.append("")
    
    # Tags
    tags = prof_data.get("teacherRatingTags", [])
    if tags:
        lines.append("**Common Tags:**")
        for tag in sorted(tags, key=lambda x: x.get("tagCount", 0), reverse=True)[:8]:
            lines.append(f"- {tag['tagName']} ({tag['tagCount']})")
        lines.append("")
    
    # Courses
    courses = prof_data.get("courseCodes", [])
    if courses:
        lines.append("**Courses Taught:**")
        for c in courses:
            lines.append(f"- {c['courseName']} ({c['courseCount']} ratings)")
        lines.append("")
    
    # Top ratings
    ratings = prof_data.get("ratings", {}).get("edges", [])
    if ratings:
        lines.append("### Selected Reviews")
        lines.append("")
        for r in ratings[:10]:
            review = r["node"]
            course = review.get("class", "Unknown")
            grade = review.get("grade", "N/A")
            helpful = review.get("helpfulRating", "N/A")
            clarity = review.get("clarityRating", "N/A")
            diff = review.get("difficultyRating", "N/A")
            comment = review.get("comment", "")
            wta = "Yes" if review.get("wouldTakeAgain") == 1 else "No" if review.get("wouldTakeAgain") == 0 else "N/A"
            date = review.get("date", "")[:10]
            
            lines.append(f"**{course}** | Quality: {helpful}/5 | Difficulty: {diff}/5 | Grade: {grade} | Would Take Again: {wta} | {date}")
            if comment:
                lines.append(f"> {comment}")
            lines.append("")
    
    return "\n".join(lines)

def main():
    print("=== Scraping RateMyProfessors for UofA CS ===")
    
    all_profs = {}
    
    for name in PROFESSORS:
        print(f"Searching: {name}")
        results = search_professor(name)
        
        if not results:
            print(f"  Not found")
            continue
        
        # Find CS/Computing Science professor
        prof = None
        for r in results:
            dept = (r.get("department") or "").lower()
            if "comput" in dept or "cs" in dept or "cmput" in dept:
                prof = r
                break
        
        if not prof and results:
            prof = results[0]  # Take first result
        
        if prof:
            print(f"  Found: {prof['firstName']} {prof['lastName']} - {prof.get('department', 'N/A')} ({prof.get('numRatings', 0)} ratings, {prof.get('avgRating', 'N/A')}/5)")
            
            # Get detailed ratings
            detailed = get_professor_ratings(prof["id"])
            if detailed:
                all_profs[name] = detailed
                md = prof_to_markdown(detailed)
                safe_name = name.replace(" ", "_").lower()
                with open(os.path.join(OUTPUT_DIR, f"{safe_name}.md"), "w") as f:
                    f.write(md)
            else:
                all_profs[name] = prof
            
            time.sleep(0.5)
        else:
            print(f"  No CS prof found")
        
        time.sleep(0.5)
    
    # Save combined JSON
    with open(os.path.join(OUTPUT_DIR, "all_professors.json"), "w") as f:
        json.dump(all_profs, f, indent=2, default=str)
    
    # Generate summary markdown
    lines = ["# UofA CS Professor Ratings (RateMyProfessors)", ""]
    lines.append("| Professor | Rating | Difficulty | Would Take Again | # Ratings |")
    lines.append("|-----------|--------|------------|-----------------|-----------|")
    
    for name, data in sorted(all_profs.items(), key=lambda x: x[1].get("avgRating", 0), reverse=True):
        rating = data.get("avgRating", "N/A")
        diff = data.get("avgDifficulty", "N/A")
        wta = data.get("wouldTakeAgainPercent", -1)
        wta_str = f"{wta:.0f}%" if isinstance(wta, (int, float)) and wta >= 0 else "N/A"
        num = data.get("numRatings", 0)
        lines.append(f"| {name} | {rating}/5 | {diff}/5 | {wta_str} | {num} |")
    
    lines.append("")
    
    with open(os.path.join(OUTPUT_DIR, "summary.md"), "w") as f:
        f.write("\n".join(lines))
    
    print(f"\n=== Done! Scraped {len(all_profs)} professors ===")

if __name__ == "__main__":
    main()
