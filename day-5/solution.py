"""
Advent of Code 2025 - Day 5
"""

def parse_input(filename):
    """
    Parse ranges and ingredient IDs
    """
    with open(filename, 'r') as f:
        content = f.read().strip()
    
    # Split by blank line
    parts = content.split('\n\n')
    ranges_section = parts[0]
    ids_section = parts[1]
    
    # Parse ranges
    ranges = []
    for line in ranges_section.split('\n'):
        start, end = map(int, line.split('-'))
        ranges.append((start, end))
    
    # Parse ingredient IDs
    ingredient_ids = [int(line) for line in ids_section.split('\n')]
    
    return ranges, ingredient_ids

def is_fresh(ingredient_id, ranges):
    """
    Check if ingredient ID falls within any fresh range
    """
    for start, end in ranges:
        if start <= ingredient_id <= end:
            return True
    return False

def count_fresh_ingredients(filename):
    """Count how many available ingredients are fresh"""
    ranges, ingredient_ids = parse_input(filename)
    
    fresh_count = 0
    for ingredient_id in ingredient_ids:
        if is_fresh(ingredient_id, ranges):
            fresh_count += 1
            print(f"Ingredient ID {ingredient_id} is fresh")
        else:
            print(f"Ingredient ID {ingredient_id} is spoiled")
    
    return fresh_count

# Run solution
result = count_fresh_ingredients('solution.csv')
print(f"\nTotal fresh ingredients: {result}")
