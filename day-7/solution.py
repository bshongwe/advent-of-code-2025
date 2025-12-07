"""
Advent of Code 2025 - Day 7
"""

def solve_tachyon_manifold(filename):
    """
    Simulate tachyon beam splitting through the manifold
    and count number of splits.
    """
    with open(filename, 'r') as f:
        grid = [line.rstrip('\n') for line in f.readlines()]
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Find starting position of beam (marked 'S')
    start_col = None
    for col in range(cols):
        if grid[0][col] == 'S':
            start_col = col
            break
    
    if start_col is None:
        return 0
    
    # Track active beams, all beams move downward
    beams = [(1, start_col)]

    # Track which positions have already been processed
    # Mark S as visited
    visited = set()
    visited.add((0, start_col))
    
    split_count = 0
    
    while beams:
        new_beams = []
        
        for row, col in beams:
            # Check if out of bounds
            if row < 0 or row >= rows or col < 0 or col >= cols:
                continue
            
            # Check if position has been processed
            if (row, col) in visited:
                continue
            visited.add((row, col))
            
            cell = grid[row][col]
            
            # If hits a splitter
            if cell == '^':
                split_count += 1
                # Create two new beams from left and right of splitter
                # Both move downward from next row
                new_beams.append((row + 1, col - 1))
                new_beams.append((row + 1, col + 1))
            else:
                # Continue downward
                new_beams.append((row + 1, col))
        
        beams = new_beams
    
    return split_count

# Solve puzzle
result = solve_tachyon_manifold('solution.csv')
print(f"The beam is split {result} times")
