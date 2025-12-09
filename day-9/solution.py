"""
Advent of Code 2025 - Day 9
"""

def solve_movie_theater(filename):
    """Find the largest rectangle with red tiles at opposite corners"""
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    
    # Parse red tile positions
    red_tiles = []
    for line in lines:
        x, y = map(int, line.split(','))
        red_tiles.append((x, y))
    
    print(f"Total red tiles: {len(red_tiles)}")
    
    # Find the largest rectangle
    max_area = 0
    best_pair = None
    
    # Check all pairs of red tiles
    n = len(red_tiles)
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = red_tiles[i]
            x2, y2 = red_tiles[j]
            
            # They can be opposite corners if they have different x and y
            if x1 != x2 and y1 != y2:
                # Calculate area INCLUDING the corner tiles
                width = abs(x2 - x1) + 1
                height = abs(y2 - y1) + 1
                area = width * height
                
                if area > max_area:
                    max_area = area
                    best_pair = (red_tiles[i], red_tiles[j])
    
    if best_pair:
        print(f"\nLargest rectangle:")
        print(f"  Corner 1: {best_pair[0]}")
        print(f"  Corner 2: {best_pair[1]}")
        print(f"  Width: {abs(best_pair[1][0] - best_pair[0][0]) + 1}")
        print(f"  Height: {abs(best_pair[1][1] - best_pair[0][1]) + 1}")
        print(f"  Area: {max_area}")
        return max_area
    else:
        print("No valid rectangle found!")
        return 0

# Solve the puzzle
result = solve_movie_theater('solution.csv')
print(f"\nAnswer: {result}")
