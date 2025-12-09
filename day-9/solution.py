"""
Advent of Code 2025 - Day 9 Part 2
"""

def point_in_polygon(x, y, polygon):
    """Ray casting algorithm to check if point is inside polygon"""
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0]
    
    for i in range(1, n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    
    return inside

def is_on_perimeter(x, y, red_tiles):
    """Check if point is on the perimeter between consecutive red tiles"""
    n = len(red_tiles)
    for i in range(n):
        x1, y1 = red_tiles[i]
        x2, y2 = red_tiles[(i + 1) % n]
        
        if x1 == x2 and x == x1:  # Vertical line
            if min(y1, y2) <= y <= max(y1, y2):
                return True
        elif y1 == y2 and y == y1:  # Horizontal line
            if min(x1, x2) <= x <= max(x1, x2):
                return True
    return False

def is_valid_tile(x, y, red_set, red_tiles_list):
    """Check if tile is red or green (on perimeter or inside)"""
    if (x, y) in red_set:
        return True
    if is_on_perimeter(x, y, red_tiles_list):
        return True
    if point_in_polygon(x, y, red_tiles_list):
        return True
    return False

def solve_movie_theater_part2(filename):
    """Find largest rectangle using only red and green tiles"""
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    
    red_tiles = []
    for line in lines:
        x, y = map(int, line.split(','))
        red_tiles.append((x, y))
    
    print(f"Total red tiles: {len(red_tiles)}")
    
    red_set = set(red_tiles)
    
    # Find largest rectangle
    max_area = 0
    best_pair = None
    checked = 0
    
    for i in range(len(red_tiles)):
        for j in range(i + 1, len(red_tiles)):
            checked += 1
            if checked % 10000 == 0:
                print(f"Checked {checked} pairs, best so far: {max_area}")
            
            x1, y1 = red_tiles[i]
            x2, y2 = red_tiles[j]
            
            if x1 == x2 or y1 == y2:
                continue
            
            min_x, max_x = min(x1, x2), max(x1, x2)
            min_y, max_y = min(y1, y2), max(y1, y2)
            
            # Quick area check - skip if can't beat current max
            potential_area = (max_x - min_x + 1) * (max_y - min_y + 1)
            if potential_area <= max_area:
                continue
            
            # Check if all tiles in rectangle are valid
            valid = True
            for x in range(min_x, max_x + 1):
                if not valid:
                    break
                for y in range(min_y, max_y + 1):
                    if not is_valid_tile(x, y, red_set, red_tiles):
                        valid = False
                        break
            
            if valid:
                area = potential_area
                if area > max_area:
                    max_area = area
                    best_pair = ((x1, y1), (x2, y2))
                    print(f"New best: {max_area} at {best_pair}")
    
    if best_pair:
        print(f"\nLargest valid rectangle:")
        print(f"  Corner 1: {best_pair[0]}")
        print(f"  Corner 2: {best_pair[1]}")
        print(f"  Area: {max_area}")
    
    return max_area

# Solve and print result
result = solve_movie_theater_part2('solution.csv')
print(f"\nAnswer: {result}")
