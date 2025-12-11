"""""
Advent of Code 2025 - Day 11: Reactor
Count distinct directed paths
"""""

import sys
import re
from functools import lru_cache

def parse_lines(lines):
    graph = {}
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if ':' not in line:
            continue
        name, rest = line.split(':', 1)
        outs = [t for t in rest.strip().split() if t]
        graph[name.strip()] = outs
    return graph

def find_reachable(graph, start):
    seen = set()
    stack = [start]
    while stack:
        n = stack.pop()
        if n in seen:
            continue
        seen.add(n)
        for nxt in graph.get(n, []):
            if nxt not in seen:
                stack.append(nxt)
    return seen

def count_paths(graph, start="you", target="out"):
    reachable = find_reachable(graph, start)
    if target not in reachable:
        return 0

    # Run Tarjan's SCC on nodes reachable
    # from start to find cycles
    index = {}
    lowlink = {}
    stack = []
    onstack = set()
    indices = [0]
    sccs = []

    def strongconnect(v):
        index[v] = indices[0]
        lowlink[v] = indices[0]
        indices[0] += 1
        stack.append(v)
        onstack.add(v)
        for w in graph.get(v, []):
            if w not in reachable:
                continue
            if w not in index:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif w in onstack:
                lowlink[v] = min(lowlink[v], index)
        if lowlink[v] == index[v]:
            comp = []
            while True:
                w = stack.pop()
                onstack.remove(w)
                comp.append(w)
                if w == v:
                    break
            sccs.append(comp)

    for node in list(reachable):
        if node not in index:
            strongconnect(node)

    # SCC with length>1 or a self-loop is a cycle
    nodes_in_cycle = set()
    for comp in sccs:
        if len(comp) > 1:
            nodes_in_cycle.update(comp)
        else:
            v = comp[0]
            # self-loop
            if v in graph and v in graph[v]:
                nodes_in_cycle.add(v)

    # Cycle node reaching target via infinite paths
    for node in nodes_in_cycle:
        # DFS from node to reach target
        # Staying within reachable set
        stack = [node]
        seen = set()
        while stack:
            x = stack.pop()
            if x in seen:
                continue
            seen.add(x)
            if x == target:
                return float('inf')
            for y in graph.get(x, []):
                if y in reachable and y not in seen:
                    stack.append(y)

    # No cycles reach target -> finite paths
    # Use memoized DFS
    @lru_cache(maxsize=None)
    def dfs(u):
        if u == target:
            return 1
        total = 0
        for v in graph.get(u, []):
            total += dfs(v)
        return total

    return dfs(start)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 solution.py solution.csv")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    graph = parse_lines(lines)
    result = count_paths(graph, "you", "out")
    if result == float('inf'):
        print("Infinite number of paths (reachable cycle leads to out).")
    else:
        print(result)
