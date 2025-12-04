#!/usr/bin/env python3
"""
READM    # Find where to insert the new entry (before Goals section)
    insert_marker = "\n## 🎯 Goals"
    
    if insert_marker in content:
        content = content.replace(insert_marker, f"\n{new_entry}## 🎯 Goals")
        readme_path.write_text(content)
        print(f"✅ Added Day {day} daily log entry")
        return True
    else:
        print("⚠️  Could not find insertion point in README.md")
        return Falselper Script
Helps update the daily log and progress in README.md
"""

import sys
from pathlib import Path
from datetime import datetime

def update_daily_log(day, title, description, difficulty="⭐⭐⭐☆☆"):
    """Update the daily log section in README.md"""
    repo_root = Path(__file__).parent
    readme_path = repo_root / "README.md"
    
    if not readme_path.exists():
        print("❌ README.md not found")
        return False
        
    content = readme_path.read_text()
    
    # Create the new daily log entry with the specific difficulty rating
    new_entry = f"""### Day {day} (Dec {day}, 2025)
- **Challenge**: {title}
- **Part 1**: {description}
- **Part 2**: [Enhanced version - update after completing]
- **Languages**: Python ⏳, Rust ⏳
- **Time to Solve**: [Your time here]
- **Difficulty**: {difficulty}

"""
    
    # Find where to insert the new entry (before the Goals section)
    goals_marker = "## 🎯 Goals"
    
    if goals_marker in content:
        content = content.replace(goals_marker, f"{new_entry}{goals_marker}")
        readme_path.write_text(content)
        print(f"✅ Added Day {day} daily log entry")
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
    
    # Update progress tracker
    if part == 1:
        # Mark part 1 completed
        search_pattern = f"- [ ] **Day {day}**"
        replace_pattern = f"- [x] **Day {day}** - ⭐"
    else:
        # Mark both parts completed
        search_pattern = f"- [x] **Day {day}** - ⭐"
        replace_pattern = f"- [x] **Day {day}** - ⭐⭐"
    
    if search_pattern in content:
        content = content.replace(search_pattern, replace_pattern)
        
        # Update stats
        stars = content.count("⭐⭐") * 2 + content.count("⭐") - content.count("⭐⭐")
        days = content.count("- [x]")
        
        # Update statistics section
        old_stats = "**Total Stars**: 4/50 ⭐\n- **Days Completed**: 2/25"
        new_stats = f"**Total Stars**: {stars}/50 ⭐\n- **Days Completed**: {days}/25"
        content = content.replace(old_stats, new_stats)
        
        readme_path.write_text(content)
        print(f"✅ Marked Day {day} Part {part} as completed")
        return True
    else:
        print(f"⚠️  Could not find Day {day} in progress tracker")
        return False

def main():
    if len(sys.argv) < 2:
        print("README Update Helper")
        print("\nUsage:")
        print("  python3 update_readme.py add <day> '<title>' '<description>' [difficulty]")
        print("  python3 update_readme.py complete <day> [part]")
        print("\nExamples:")
        print("  python3 update_readme.py add 3 'Grid Walker' 'Navigate through a 2D grid'")
        print("  python3 update_readme.py complete 3 1")
        print("  python3 update_readme.py complete 3 2")
        return
    
    action = sys.argv[1]
    
    if action == "add" and len(sys.argv) >= 5:
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
