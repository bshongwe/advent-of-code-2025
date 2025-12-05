"""
Advent of Code 2025 - Day 5
"""

def parse_ranges(filename):
    """
    Parse ranges and ingredient IDs
    """
    with open(filename, 'r') as f:
        content = f.read().strip()
    
    # Get only the first section (before blank line)
    ranges_section = content.split('\n\n')[0]
    
    # Parse ranges
    ranges = []
    for line in ranges_section.split('\n'):
        start, end = map(int, line.split('-'))
        ranges.append((start, end))
    
    return ranges

def merge_ranges(ranges):
    """Merge overlapping ranges to avoid counting duplicates"""
    if not ranges:
        return []
    
    # Sort ranges by start position
    sorted_ranges = sorted(ranges)
    
    merged = [sorted_ranges[0]]
    
    for current_start, current_end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]
        
        # Check if current range overlaps or is adjacent to last range
        if current_start <= last_end + 1:
            # Merge by extending the last range
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            # No overlap, add as new range
            merged.append((current_start, current_end))
    
    return merged

def count_fresh_ids(filename):
    """
    Count all ingredient IDs considered fresh by all ranges
    """
    ranges = parse_ranges(filename)
    
    # Merge overlapping ranges
    merged = merge_ranges(ranges)
    
    # Count total IDs in all merged ranges
    total_count = 0
    for start, end in merged:
        count = end - start + 1
        total_count += count
        print(f"Range {start}-{end}: {count} IDs")
    
    return total_count

# Run solution
result = count_fresh_ids('solution.csv')
print(f"\nTotal fresh ingredient IDs: {result}")
