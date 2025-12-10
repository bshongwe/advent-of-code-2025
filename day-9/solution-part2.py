"""
Advent of Code 2025 - Day 9 Part 2
Determine the largest rectangle that
can be formed using only red and
green tiles.
"""

def solve_movie_theater_part2(filename):
    with open(filename, 'r') as f:
        red = [tuple(map(int, line.strip().split(','))) for line in f if line.strip()]
    
    n = len(red)
    
    def area(a, b):
        return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
    
    def bounds(a, b):
        return ((min(a[0], b[0]), min(a[1], b[1])), (max(a[0], b[0]), max(a[1], b[1])))
    
    def intersecting_line(la, lb, rect_bounds):
        min_pt, max_pt = rect_bounds
        min_x, min_y = min_pt
        max_x, max_y = max_pt
        
        lmin_x = min(la[0], lb[0])
        lmax_x = max(la[0], lb[0])
        lmin_y = min(la[1], lb[1])
        lmax_y = max(la[1], lb[1])
        
        # Vertical line in grid
        if la[0] == lb[0]:
            return (((lmin_y < min_y and lmax_y > min_y) or
                     (lmin_y < max_y and lmax_y > max_y) or
                     (lmin_y >= min_y and lmax_y <= max_y)) and
                    la[0] > min_x and la[0] < max_x)
        
        # Horizontal line in grid
        if la[1] == lb[1]:
            return (((lmin_x < min_x and lmax_x > min_x) or
                     (lmin_x < max_x and lmax_x > max_x) or
                     (lmin_x >= min_x and lmax_x <= max_x)) and
                    la[1] > min_y and la[1] < max_y)
        
        return False
    
    # Generate rectangles sorted by area
    # Sorted by area descending
    rectangles = []
    for i in range(n):
        for j in range(i + 1, n):
            if red[i][0] != red[j][0] and red[i][1] != red[j][1]:
                rectangles.append((area(red[i], red[j]), i, j))
    
    rectangles.sort(reverse=True)
    
    # Find first valid
    for a, i, j in rectangles:
        rect_bounds = bounds(red[i], red[j])
        
        valid = True
        for k in range(n):
            la = red[k]
            lb = red[(k + 1) % n]
            if intersecting_line(la, lb, rect_bounds):
                valid = False
                break
        
        if valid:
            print(f"Found: area={a}, corners={red[i]}, {red[j]}")
            return a
    
    return 0

# Solve and print result
result = solve_movie_theater_part2('solution.csv')
print(result)
