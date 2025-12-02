#!/usr/bin/env python3
"""
Advent of Code 2025 - Day Generator Script
Automatically creates a new day folder with empty solution files
following the established naming convention.
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

def main():
    """Main function."""
    if len(sys.argv) != 2:
        print("Usage: python generate_day.py <day_number>")
        print("Example: python generate_day.py 3")
        sys.exit(1)
    
    try:
        day_number = int(sys.argv[1])
        if day_number < 1 or day_number > 25:
            print("❌ Day number must be between 1 and 25")
            sys.exit(1)
    except ValueError:
        print("❌ Day number must be a valid integer")
        sys.exit(1)
    
    print(f"🎄 Generating Advent of Code 2025 - Day {day_number}")
    print("=" * 50)
    
    success = create_day_structure(day_number)
    
    if success:
        print("=" * 50)
        print("Next steps:")
        print(f"1. cd day-{day_number}")
        print("2. Add your puzzle input to solution.csv (already created, gitignored)")
        print("3. Start coding your solution!")
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
