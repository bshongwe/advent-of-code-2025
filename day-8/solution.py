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
        
        return True
    
    def get_component_sizes(self):
        """Get sizes of all connected components"""
        components = defaultdict(int)
        for i in range(len(self.parent)):
            root = self.find(i)
            components[root] += 1
        return list(components.values())

def solve_playground(filename):
    """Solve the junction box connection problem"""
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
    
    # Process the 1000 shortest edges (not just successful connections)
    connections_attempted = 0
    connections_made = 0
    
    for dist, i, j in edges[:1000]:  # Only look at first 1000 edges
        connections_attempted += 1
        
        # Try to connect these two boxes
        if uf.union(i, j):
            connections_made += 1
            if connections_made <= 10:
                print(f"Connection {connections_made}: boxes {i} and {j}, distance {dist:.2f}")
    
    print(f"\nConnections attempted: {connections_attempted}")
    print(f"Successful connections made: {connections_made}")
    
    # Get sizes of all circuits
    component_sizes = uf.get_component_sizes()
    component_sizes.sort(reverse=True)
    
    print(f"Number of circuits: {len(component_sizes)}")
    print(f"Circuit sizes: {component_sizes[:10]}")
    
    # Multiply the three largest
    if len(component_sizes) >= 3:
        result = component_sizes[0] * component_sizes[1] * component_sizes[2]
        print(f"\nThree largest circuits: {component_sizes[0]}, {component_sizes[1]}, {component_sizes[2]}")
        print(f"Product: {result}")
        return result
    else:
        return 0

# Solve the puzzle
result = solve_playground('solution.csv')
print(f"\nAnswer: {result}")
