"""
Advent of Code 2025 - Day 12: Christmas Tree Farm
Efficient present packing with greedy placement
"""

import sys

def parse_input(filename):
    with open(filename) as f:
        sections = f.read().strip().split('\n\n')
    
    # Parse shapes
    shapes = {}
    for block in sections[:-1]:
        lines = block.strip().split('\n')
        idx = int(lines[0].rstrip(':'))
        shape = []
        for line in lines[1:]:
            shape.append(list(line))
        shapes[idx] = shape
    
    # Parse regions
    regions = []
    for line in sections[-1].strip().split('\n'):
        parts = line.split(':')
        dims = parts[0].strip().split('x')
        width, height = int(dims[0]), int(dims[1])
        counts = list(map(int, parts[1].strip().split()))
        regions.append((width, height, counts))
    
    return shapes, regions

def get_shape_coords(shape):
    """Extract (row, col) coordinates of # cells"""
    coords = []
    for r, row in enumerate(shape):
        for c, cell in enumerate(row):
            if cell == '#':
                coords.append((r, c))
    return coords

def normalize_coords(coords):
    """Shift coords so min row and col are 0"""
    if not coords:
        return []
    min_r = min(r for r, c in coords)
    min_c = min(c for r, c in coords)
    return tuple(sorted((r - min_r, c - min_c) for r, c in coords))

def get_orientations(shape):
    """Get all unique orientations of a shape"""
    coords = get_shape_coords(shape)
    orientations = set()
    
    # Try all rotations and flips
    current = coords
    for _ in range(4):
        orientations.add(normalize_coords(current))
        current = [(c, -r) for r, c in current]  # Rotate 90°
    
    # Flip and try again
    current = [(r, -c) for r, c in coords]
    for _ in range(4):
        orientations.add(normalize_coords(current))
        current = [(c, -r) for r, c in current]
    
    return list(orientations)

def can_fit(grid, coords, r, c, width, height):
    """Check if shape can be placed at position"""
    for dr, dc in coords:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= height or nc < 0 or nc >= width or grid[nr][nc]:
            return False
    return True

def place_shape(grid, coords, r, c):
    """Place shape on grid"""
    for dr, dc in coords:
        grid[r + dr][c + dc] = True

def solve_region_fast(width, height, shapes, counts):
    """Fast greedy approach - try to place largest shapes first"""
    # Quick area check
    total_area = width * height
    required_area = sum(len(get_shape_coords(shapes[i])) * count 
                       for i, count in enumerate(counts) if i < len(shapes))
    if required_area > total_area:
        return False
    
    # Build present list sorted by size (largest first)
    presents = []
    for shape_idx, count in enumerate(counts):
        if shape_idx < len(shapes):
            size = len(get_shape_coords(shapes[shape_idx]))
            for _ in range(count):
                presents.append((size, shape_idx))
    
    presents.sort(reverse=True)  # Largest first
    
    if not presents:
        return True
    
    grid = [[False] * width for _ in range(height)]
    
    # Try to place each present greedily
    for size, shape_idx in presents:
        placed = False
        orientations = get_orientations(shapes[shape_idx])
        
        # Try each orientation
        for coords in orientations:
            if placed:
                break
            # Try each position
            for r in range(height):
                if placed:
                    break
                for c in range(width):
                    if can_fit(grid, coords, r, c, width, height):
                        place_shape(grid, coords, r, c)
                        placed = True
                        break
        
        if not placed:
            return False
    
    return True

def solve_puzzle(filename):
    shapes, regions = parse_input(filename)
    
    count = 0
    for i, (width, height, counts) in enumerate(regions, 1):
        if solve_region_fast(width, height, shapes, counts):
            count += 1
        
        # Progress indicator
        if i % 50 == 0:
            print(f"Processed {i}/{len(regions)} regions, {count} fit so far")
    
    return count

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 solution.py solution.csv")
        sys.exit(1)
    
    result = solve_puzzle(sys.argv[1])
    print(f"Regions that fit all presents: {result}")