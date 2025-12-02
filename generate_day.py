#!/usr/bin/env python3
"""
Advent of Code 2025 - Day Generator Script
Automatically creates a new day folder with empty solution files
following the established naming convention.

Can be run with:
- No arguments: Auto-detects next day based on current date and existing folders
- Day number: Creates specific day (python3 generate_day.py 5)
"""

import os
import sys
from pathlib import Path
from datetime import datetime

def create_day_structure(day_number):
    """Create a new day folder with empty solution files."""
    
    # Get the script directory (repo root)
    repo_root = Path(__file__).parent
    
    # Create day folder name
    day_folder = repo_root / f"day-{day_number}"
    
    # Check if folder already exists
    if day_folder.exists():
        print(f"❌ Day {day_number} folder already exists: {day_folder}")
        return False
    
    # Create the day folder
    day_folder.mkdir(exist_ok=True)
    print(f"📁 Created folder: {day_folder}")
    
    # File templates based on your naming convention
    files_to_create = [
        "solution.py",
        "solution-part2.py", 
        "solution.rs",
        "solution-part2.rs",
        "solution.csv"
    ]
    
    # Python template
    python_template = '''"""
Advent of Code 2025 - Day {day}
"""

def solve():
    """Solve the puzzle."""
    pass

if __name__ == "__main__":
    result = solve()
    print(f"Result: {{result}}")
'''

    # Rust template
    rust_template = '''// Advent of Code 2025 - Day {day}

fn solve() -> i32 {{
    // TODO: Implement solution
    0
}}

fn main() {{
    let result = solve();
    println!("Result: {{}}", result);
}}
'''
    
    # Create each file
    for filename in files_to_create:
        file_path = day_folder / filename
        
        if filename.endswith('.py'):
            content = python_template.format(day=day_number)
        elif filename.endswith('.rs'):
            content = rust_template.format(day=day_number)
        elif filename.endswith('.csv'):
            content = ""  # Empty CSV file for puzzle input
        else:
            content = ""
            
        file_path.write_text(content)
        print(f"📄 Created file: {file_path.name}")
    
    print(f"✅ Day {day_number} structure created successfully!")
    print(f"📍 Location: {day_folder}")
    return True

def get_existing_days():
    """Get a list of existing day numbers."""
    repo_root = Path(__file__).parent
    existing_days = []
    
    for item in repo_root.iterdir():
        if item.is_dir() and item.name.startswith("day-"):
            try:
                day_num = int(item.name.split("-")[1])
                existing_days.append(day_num)
            except (ValueError, IndexError):
                continue
    
    return sorted(existing_days)

def determine_next_day():
    """Determine the next day to generate based on date and existing folders."""
    now = datetime.now()
    
    # Advent of Code runs December 1-25
    if now.month == 12 and 1 <= now.day <= 25:
        current_aoc_day = now.day
    else:
        # If not in December 1-25, just generate next sequential day
        existing_days = get_existing_days()
        if not existing_days:
            return 1
        return max(existing_days) + 1
    
    existing_days = get_existing_days()
    
    # Check if today's AoC day already exists
    if current_aoc_day in existing_days:
        print(f"📋 Day {current_aoc_day} (today) already exists!")
        
        # Check if we're missing any previous days
        missing_days = []
        for day in range(1, current_aoc_day):
            if day not in existing_days:
                missing_days.append(day)
        
        if missing_days:
            print(f"🔍 Missing previous days: {missing_days}")
            return min(missing_days)
        
        # All previous days exist, generate tomorrow if valid
        next_day = current_aoc_day + 1
        if next_day <= 25:
            print(f"⏭️  Generating tomorrow's day: {next_day}")
            return next_day
        else:
            print("🎄 All 25 days of Advent of Code are done!")
            return None
    
    # Today's AoC day doesn't exist, generate it
    print(f"📅 Generating today's day: {current_aoc_day}")
    return current_aoc_day

def main():
    """Main function."""
    # Check if day number is provided as argument
    if len(sys.argv) == 1:
        # No argument provided - auto-detect next day
        day_number = determine_next_day()
        auto_mode = True
    elif len(sys.argv) == 2:
        # Day number provided as argument
        try:
            day_number = int(sys.argv[1])
            if day_number < 1 or day_number > 25:
                print("❌ Day number must be between 1 and 25")
                sys.exit(1)
            auto_mode = False
        except ValueError:
            print("❌ Day number must be a valid integer")
            sys.exit(1)
    else:
        print("Usage:")
        print("  python3 generate_day.py          # Auto-generate next day")
        print("  python3 generate_day.py <day>    # Generate specific day")
        print("Example: python3 generate_day.py 3")
        sys.exit(1)
    
    if day_number > 25:
        print("❌ Advent of Code only goes up to day 25!")
        sys.exit(1)
    
    existing_days = get_existing_days()
    
    print("🎄 Advent of Code 2025 Day Generator")
    print("=" * 50)
    
    if auto_mode:
        now = datetime.now()
        print(f"📅 Today: {now.strftime('%B %d, %Y')}")
        if existing_days:
            print(f"📁 Existing days: {', '.join(map(str, existing_days))}")
        print(f"🎯 Auto-generating: Day {day_number}")
    else:
        print(f"🎯 Generating: Day {day_number} (manual)")
    
    print("=" * 50)
    
    success = create_day_structure(day_number)
    
    if success:
        print("=" * 50)
        print("Next steps:")
        print(f"1. cd day-{day_number}")
        print("2. Add your puzzle input to solution.csv (already created, gitignored)")
        print("3. Start coding your solution!")
        
        if auto_mode:
            print(f"\n💡 Tip: Run 'python3 generate_day.py' again tomorrow for day {day_number + 1}")
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
