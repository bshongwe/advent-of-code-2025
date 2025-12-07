#!/usr/bin/env python3
"""
Auto README Updater for Advent of Code 2025
Automatically fetches puzzle details and updates README.md
"""

import sys
import re
import requests
from pathlib import Path
from datetime import datetime
from bs4 import BeautifulSoup

def fetch_puzzle_info(day, year=2025):
    """Fetch puzzle title and description from Advent of Code"""
    url = f"https://adventofcode.com/{year}/day/{day}"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return None, None
            
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract title from h2 tag
        title_element = soup.find('h2')
        if title_element:
            title = title_element.get_text().replace('--- Day ', '').replace(' ---', '').strip()
            # Remove day number prefix if present
            title = re.sub(r'^\d+:\s*', '', title)
        else:
            title = f"Day {day} Challenge"
            
        # Extract first paragraph of description
        article = soup.find('article', class_='day-desc')
        if article:
            first_p = article.find('p')
            if first_p:
                description = first_p.get_text().strip()
                # Truncate if too long
                if len(description) > 100:
                    description = description[:97] + "..."
            else:
                description = "Solve the daily coding challenge"
        else:
            description = "Solve the daily coding challenge"
            
        return title, description
        
    except Exception as e:
        print(f"⚠️  Could not fetch puzzle info: {e}")
        return None, None

def estimate_difficulty(title, description):
    """Estimate difficulty based on keywords in title/description"""
    text = (title + " " + description).lower()
    
    # Difficulty indicators
    easy_words = ['count', 'find', 'simple', 'basic', 'list']
    medium_words = ['grid', 'path', 'navigate', 'calculate', 'parse']
    hard_words = ['optimize', 'algorithm', 'complex', 'recursive', 'dynamic']
    very_hard_words = ['graph', 'tree', 'shortest', 'minimum', 'maximum']
    
    score = 2  # Default medium
    
    for word in easy_words:
        if word in text:
            score -= 0.5
            
    for word in medium_words:
        if word in text:
            score += 0.2
            
    for word in hard_words:
        if word in text:
            score += 0.8
            
    for word in very_hard_words:
        if word in text:
            score += 1.2
    
    # Convert to star rating
    if score <= 1.5:
        return "⭐⭐☆☆☆"
    elif score <= 2.5:
        return "⭐⭐⭐☆☆"
    elif score <= 3.5:
        return "⭐⭐⭐⭐☆"
    else:
        return "⭐⭐⭐⭐⭐"

def auto_update_daily_log(day):
    """Automatically fetch and update daily log entry"""
    print(f"🔍 Fetching puzzle info for Day {day}...")
    
    title, description = fetch_puzzle_info(day)
    if not title or not description:
        print(f"❌ Could not fetch puzzle info for Day {day}")
        return False
        
    difficulty = estimate_difficulty(title, description)
    print(f"📊 Estimated difficulty: {difficulty}")
    
    return update_daily_log(day, title, description, difficulty)

def update_daily_log(day, title, description, difficulty="⭐⭐⭐☆☆"):
    """Update the daily log section in README.md"""
    repo_root = Path(__file__).parent
    readme_path = repo_root / "README.md"
    
    if not readme_path.exists():
        print("❌ README.md not found")
        return False
        
    content = readme_path.read_text()
    
    # Check if entry already exists
    if f"### Day {day} (Dec {day}, 2025)" in content:
        print(f"ℹ️  Day {day} entry already exists")
        return True
    
    # Create the new daily log entry
    new_entry = f"""### Day {day} (Dec {day}, 2025)
- **Challenge**: {title}
- **Part 1**: {description}
- **Part 2**: [Enhanced version - update after completing]
- **Languages**: Python ⏳, Rust ⏳
- **Time to Solve**: [Your time here]
- **Difficulty**: {difficulty}

"""
    
    # Find where to insert the new entry (before Goals section)
    goals_marker = "## 🎯 Goals"
    
    if goals_marker in content:
        content = content.replace(goals_marker, f"{new_entry}{goals_marker}")
        
        # Update timestamp
        current_date = datetime.now().strftime("%B %d, %Y")
        timestamp_pattern = r"\*Last updated: [^*]+\*"
        new_timestamp = f"*Last updated: {current_date}*"
        content = re.sub(timestamp_pattern, new_timestamp, content)
        
        readme_path.write_text(content)
        print(f"✅ Added Day {day} daily log entry: {title}")
        return True
    else:
        print("⚠️  Could not find insertion point in README.md")
        return False

def mark_day_completed(day, part=1):
    """Mark a day as completed in the progress tracker"""
    repo_root = Path(__file__).parent
    readme_path = repo_root / "README.md"
    
    if not readme_path.exists():
        print("❌ README.md not found")
        return False
        
    content = readme_path.read_text()
    
    # Get the challenge title and part 1 description from daily log
    title_pattern = f"### Day {day} \(Dec {day}, 2025\)\n- \*\*Challenge\*\*: ([^\n]+)\n- \*\*Part 1\*\*: ([^\n]+)"
    title_match = re.search(title_pattern, content)
    if title_match:
        challenge_title = title_match.group(1)
        part1_desc = title_match.group(2)
        
        # Extract description from challenge title if it has " - "
        if " - " in challenge_title:
            description = challenge_title.split(" - ", 1)[1]
        else:
            # Use Part 1 description as fallback, but clean it up
            if "..." not in part1_desc and len(part1_desc) < 60:
                description = part1_desc
            else:
                # For very long or truncated descriptions, create a simple one
                simple_descriptions = {
                    "Printing Department": "Navigate printing department challenges",
                    "Cafeteria": "Solve cafeteria logistics puzzle",
                    "Grid Walker": "Navigate through a 2D grid",
                    "Trash Compactor": "Cephalopod math worksheet",
                    "Laboratories": "Laboratory challenges"
                }
                description = simple_descriptions.get(challenge_title, "")
    else:
        challenge_title = f"Day {day}"
        description = ""
    
    # Always use the description from Daily Log, don't preserve existing ones
    
    # Update progress tracker - handle various formats
    day_pattern = f"- \[[x ]\] \*\*Day {day}\*\*[^\n]*"
    
    if part == 1:
        # Mark part 1 completed
        new_entry = f"- [x] **Day {day}** - ⭐ {challenge_title} - *{description}*" if description else f"- [x] **Day {day}** - ⭐ {challenge_title}"
    else:
        # Mark both parts completed  
        new_entry = f"- [x] **Day {day}** - ⭐⭐ {challenge_title} - *{description}*" if description else f"- [x] **Day {day}** - ⭐⭐ {challenge_title}"
    
    # Replace the entire day line (only first occurrence to avoid duplicates)
    if re.search(day_pattern, content):
        content = re.sub(day_pattern, new_entry, content, count=1)
        
        # Update stats - only count stars in Progress Tracker section
        progress_section = content.split("## 📊 Progress Tracker")[1].split("## 🏃 Running Solutions")[0]
        double_stars = progress_section.count("⭐⭐")
        single_stars = progress_section.count("⭐") - (double_stars * 2)
        stars = (double_stars * 2) + single_stars
        days = progress_section.count("- [x]")
        
        # Find and update statistics
        stats_pattern = r"\*\*Total Stars\*\*: \d+/\d+ ⭐\n- \*\*Days Completed\*\*: \d+/\d+"
        new_stats = f"**Total Stars**: {stars}/24 ⭐\n- **Days Completed**: {days}/12"
        content = re.sub(stats_pattern, new_stats, content)
        
        # Update timestamp
        current_date = datetime.now().strftime("%B %d, %Y")
        timestamp_pattern = r"\*Last updated: [^*]+\*"
        new_timestamp = f"*Last updated: {current_date}*"
        content = re.sub(timestamp_pattern, new_timestamp, content)
        
        readme_path.write_text(content)
        print(f"✅ Marked Day {day} Part {part} as completed")
        return True
    else:
        print(f"⚠️  Could not find Day {day} in progress tracker")
        return False

def main():
    if len(sys.argv) < 2:
        print("Auto README Updater for Advent of Code 2025")
        print("\nUsage:")
        print("  python3 update_readme.py auto <day>     # Auto-fetch puzzle info")
        print("  python3 update_readme.py add <day> '<title>' '<description>' [difficulty]")
        print("  python3 update_readme.py complete <day> [part]")
        print("\nExamples:")
        print("  python3 update_readme.py auto 5")
        print("  python3 update_readme.py complete 5 1")
        return
    
    action = sys.argv[1]
    
    if action == "auto" and len(sys.argv) >= 3:
        day = int(sys.argv[2])
        auto_update_daily_log(day)
        
    elif action == "add" and len(sys.argv) >= 5:
        day = int(sys.argv[2])
        title = sys.argv[3]
        description = sys.argv[4]
        difficulty = sys.argv[5] if len(sys.argv) > 5 else "⭐⭐⭐☆☆"
        update_daily_log(day, title, description, difficulty)
        
    elif action == "complete" and len(sys.argv) >= 3:
        day = int(sys.argv[2])
        part = int(sys.argv[3]) if len(sys.argv) > 3 else 1
        mark_day_completed(day, part)
        
    else:
        print("❌ Invalid arguments. Use --help for usage information.")

if __name__ == "__main__":
    main()
