"""
Advent of Code 2025 - Day 7
"""

def solve_quantum_tachyon_manifold(filename):
    """
    Count timelines in quantum tachyon manifold
    """
    with open(filename, 'r') as f:
        grid = [line.rstrip('\n') for line in f.readlines()]
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Find starting position (S)
    start_col = None
    for col in range(cols):
        if grid[0][col] == 'S':
            start_col = col
            break
    
    if start_col is None:
        return 0
    
    # Track number of timelines at each position
    # current[col] = number of timelines at this column in current row
    current = [0] * cols
    current[start_col] = 1
    
    # Process row by row
    for row in range(1, rows):
        next_row = [0] * cols
        
        for col in range(cols):
            if current[col] == 0:
                continue
            
            num_timelines = current[col]
            prev_cell = grid[row - 1][col]
            
            # Check what was at previous position
            if prev_cell == '^':
                # This position receives timelines from splitter above
                # But first check if left or right of splitter
                pass
            
            # Check current cell
            curr_cell = grid[row][col]
            
            if curr_cell == '^':
                # Split: send timelines left and right
                if col - 1 >= 0:
                    next_row[col - 1] += num_timelines
                if col + 1 < cols:
                    next_row[col + 1] += num_timelines
            else:
                # Continue down
                next_row[col] += num_timelines
        
        current = next_row
    
    # Total timelines is sum of all active timelines
    return sum(current)

# Solve puzzle
result = solve_quantum_tachyon_manifold('solution.csv')
print(f"Total number of timelines: {result}")
