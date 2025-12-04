"""
Advent of Code 2025 - Day 4
"""

def count_adjacent_rolls(grid, i, j):
    """
    Count rolls of paper adjacent to position (i, j)
    """
    rows = len(grid)
    cols = len(grid[0])
    
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    adjacent_count = 0
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < rows and 0 <= nj < cols:
            if grid[ni][nj] == '@':
                adjacent_count += 1
    
    return adjacent_count

def find_accessible_rolls(grid):
    """
    Find all currently accessible rolls (< 4 adjacent rolls)
    """
    rows = len(grid)
    cols = len(grid[0])
    accessible = []
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '@':
                if count_adjacent_rolls(grid, i, j) < 4:
                    accessible.append((i, j))
    
    return accessible

def remove_rolls_iteratively(grid_input):
    """
    Keep removing accessible rolls until none are left
    """
    # 1. Convert to mutable list of lists
    grid = [list(row) for row in grid_input]
    
    total_removed = 0
    
    while True:
        # 2. Find all currently accessible rolls
        accessible = find_accessible_rolls(grid)
        
        if not accessible:
            # 2.1 No more rolls can be removed
            break
        
        # 2.2 Remove all accessible rolls
        for i, j in accessible:
            grid[i][j] = '.'
        
        total_removed += len(accessible)
        print(f"Removed {len(accessible)} rolls (total so far: {total_removed})")
    
    return total_removed

# 3. Reads CSV puzzle input
with open('solution.csv', 'r') as f:
    grid = [line.strip() for line in f.readlines()]

result = remove_rolls_iteratively(grid)
print(f"\nTotal rolls removed: {result}")
