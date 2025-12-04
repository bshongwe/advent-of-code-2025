"""
Advent of Code 2025 - Day 4
"""

def count_accessible_rolls(grid):
    rows = len(grid)
    cols = len(grid[0])
    accessible_count = 0
    
    # Directions for 8 adjacent positions (including diagonals)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    for i in range(rows):
        for j in range(cols):
            # Check if current position has a roll of paper
            if grid[i][j] == '@':
                # Count adjacent rolls
                adjacent_rolls = 0
                
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    # Check if position is within bounds
                    if 0 <= ni < rows and 0 <= nj < cols:
                        if grid[ni][nj] == '@':
                            adjacent_rolls += 1
                
                # A roll is accessible if it has fewer than 4 adjacent rolls
                if adjacent_rolls < 4:
                    accessible_count += 1
    
    return accessible_count

# Read your puzzle input
with open('solution.csv', 'r') as f:
    grid = [line.strip() for line in f.readlines()]

result = count_accessible_rolls(grid)
print(f"Number of accessible rolls: {result}")
