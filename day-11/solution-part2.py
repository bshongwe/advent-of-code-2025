"""
Advent of Code 2025 - Day 11 Part 2
Count distinct directed paths
"""


import sys
import re
from functools import lru_cache

def parse_lines(lines):
    graph = {}
    for line in lines:
        line = line.strip()
        if not line or ':' not in line:
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

def sccs_on_reachable(graph, start):
    # Tarjan's SCC limited to nodes reachable from start
    reachable = find_reachable(graph, start)
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
    return sccs, reachable

def has_infinite_paths(graph, start, target):
    # determine if any cycle reachable from start can reach target
    sccs, reachable = sccs_on_reachable(graph, start)
    nodes_in_cycle = set()
    for comp in sccs:
        if len(comp) > 1:
            nodes_in_cycle.update(comp)
        else:
            v = comp[0]
            if v in graph and v in graph[v]:
                nodes_in_cycle.add(v)
    # for each cycle node, check if it can reach target
    for node in nodes_in_cycle:
        stack = [node]
        seen = set()
        while stack:
            x = stack.pop()
            if x in seen:
                continue
            seen.add(x)
            if x == target:
                return True
            for y in graph.get(x, []):
                if y in reachable and y not in seen:
                    stack.append(y)
    return False

def count_paths_visiting_both(graph, start="svr", target="out", a="dac", b="fft"):
    # quick checks
    reachable = find_reachable(graph, start)
    if target not in reachable:
        return 0
    # if infinite paths that can reach target, we can't return a finite count
    if has_infinite_paths(graph, start, target):
        return float('inf')

    @lru_cache(maxsize=None)
    def dfs(node, seen_a, seen_b):
        # seen flags are ints 0/1 to allow caching
        if node == target:
            return 1 if (seen_a and seen_b) else 0
        total = 0
        for nxt in graph.get(node, []):
            na = seen_a or (nxt == a)
            nb = seen_b or (nxt == b)
            total += dfs(nxt, na, nb)
        return total

    # initial seen flags: node "svr" might itself be dac/fft, but usually not; handle generally
    init_a = (start == a)
    init_b = (start == b)
    return dfs(start, init_a, init_b)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 solution-part2.py solution.csv")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    graph = parse_lines(lines)
    result = count_paths_visiting_both(graph, "svr", "out", "dac", "fft")
    if result == float('inf'):
        print("Infinite number of valid paths (cycle reachable to out).")
    else:
        print(result)
