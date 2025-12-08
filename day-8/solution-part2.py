import math
from collections import defaultdict

"""
Advent of Code 2025 - Day 8
"""

def distance(p1, p2):
    """Calculate Euclidean distance between two 3D points"""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

class UnionFind:
    """Union-Find data structure for tracking connected components"""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.num_components = n
    
    def find(self, x):
        """Find root of x with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """Union two sets, return True if they were different sets"""
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False  # Already in same set
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        self.num_components -= 1
        return True
    
    def get_component_sizes(self):
        """Get sizes of all connected components"""
        components = defaultdict(int)
        for i in range(len(self.parent)):
            root = self.find(i)
            components[root] += 1
        return list(components.values())

def solve_playground_part2(filename):
    """Solve Part 2: Find the last connection to make one circuit"""
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    
    # Parse junction box positions
    boxes = []
    for line in lines:
        x, y, z = map(int, line.split(','))
        boxes.append((x, y, z))
    
    n = len(boxes)
    print(f"Total junction boxes: {n}")
    
    # Calculate all pairwise distances
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(boxes[i], boxes[j])
            edges.append((dist, i, j))
    
    # Sort edges by distance
    edges.sort()
    
    print(f"Total possible connections: {len(edges)}")
    
    # Use Union-Find to track connections
    uf = UnionFind(n)
    
    # Keep connecting until we have one component
    connections_made = 0
    last_connection = None
    
    for dist, i, j in edges:
        # Try to connect these two boxes
        if uf.union(i, j):
            connections_made += 1
            last_connection = (i, j, dist)
            
            if connections_made <= 10:
                print(f"Connection {connections_made}: boxes {i} and {j}, distance {dist:.2f}, components: {uf.num_components}")
            
            # Check if we're done (all in one circuit)
            if uf.num_components == 1:
                print(f"\nAll boxes connected after {connections_made} connections!")
                break
    
    if last_connection:
        i, j, dist = last_connection
        x1, y1, z1 = boxes[i]
        x2, y2, z2 = boxes[j]
        
        print(f"\nLast connection:")
        print(f"  Box {i} at ({x1}, {y1}, {z1})")
        print(f"  Box {j} at ({x2}, {y2}, {z2})")
        print(f"  Distance: {dist:.2f}")
        
        result = x1 * x2
        print(f"\nProduct of X coordinates: {x1} * {x2} = {result}")
        return result
    
    return 0

# Solve the puzzle
result = solve_playground_part2('solution.csv')
print(f"\nAnswer: {result}")
