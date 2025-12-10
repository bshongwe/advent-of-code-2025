"""
Advent of Code 2025 - Day 10: Factory
Linear algebra over GF(2) - Gaussian elimination
"""

import re
from itertools import product

def parse_machine(line):
    """
    Parse a machine line into target, buttons
    """
    lights_match = re.search(r'\[([.#]+)\]', line)
    target = [1 if c == '#' else 0 for c in lights_match.group(1)]
    
    buttons = []
    for match in re.finditer(r'\(([0-9,]+)\)', line):
        indices = [int(x) for x in match.group(1).split(',')]
        buttons.append(indices)
    
    return target, buttons

def solve_gf2_minimum(target, buttons):
    """
    Find minimum button presses using
    Gaussian elimination and checking
    all solutions in solution space
    """
    n_lights = len(target)
    n_buttons = len(buttons)
    
    # Build augmented matrix
    matrix = []
    for light_idx in range(n_lights):
        row = []
        for button in buttons:
            row.append(1 if light_idx in button else 0)
        row.append(target[light_idx])
        matrix.append(row)
    
    # Keep original for verification
    original_matrix = [row[:] for row in matrix]
    
    # Gaussian elimination to RREF
    pivot_col = []
    pivot_row = 0
    
    for col in range(n_buttons):
        # Find pivot
        found = False
        for row in range(pivot_row, n_lights):
            if matrix[row][col] == 1:
                matrix[pivot_row], matrix[row] = matrix[row], matrix[pivot_row]
                found = True
                break
        
        if not found:
            continue
        
        pivot_col.append(col)
        
        # Eliminate all other 1s in column
        for row in range(n_lights):
            if row != pivot_row and matrix[row][col] == 1:
                for c in range(n_buttons + 1):
                    matrix[row][c] ^= matrix[pivot_row][c]
        
        pivot_row += 1
    
    # Check for inconsistency
    # No solution if any row has 0...0 | 1
    for row in range(pivot_row, n_lights):
        if matrix[row][-1] == 1:
            return None
    
    # Find free variables
    free_vars = [col for col in range(n_buttons) if col not in pivot_col]
    
    if not free_vars:
        # Unique solution
        solution = [0] * n_buttons
        for row, col in enumerate(pivot_col):
            solution[col] = matrix[row][-1]
        return sum(solution)
    
    # Try alternative combinations
    min_presses = float('inf')
    
    for free_values in product([0, 1], repeat=len(free_vars)):
        solution = [0] * n_buttons
        
        # Set free variables
        for i, var_col in enumerate(free_vars):
            solution[var_col] = free_values[i]
        
        # Compute dependent variables
        for row, col in enumerate(pivot_col):
            val = matrix[row][-1]
            # Subtract contribution from free variables
            for c in range(n_buttons):
                if c != col:
                    val ^= (matrix[row][c] * solution[c])
            solution[col] = val
        
        # Verify solution
        state = [0] * n_lights
        for btn_idx, press in enumerate(solution):
            if press == 1:
                for light in buttons[btn_idx]:
                    state[light] ^= 1
        
        if state == target:
            min_presses = min(min_presses, sum(solution))
    
    return min_presses if min_presses != float('inf') else None

def solve_factory(filename):
    """Solve all machines and return total minimum button presses"""
    with open(filename) as f:
        lines = [line.strip() for line in f if line.strip()]
    
    total_presses = 0
    
    for i, line in enumerate(lines, 1):
        target, buttons = parse_machine(line)
        min_presses = solve_gf2_minimum(target, buttons)
        
        if min_presses is not None:
            print(f"Machine {i}: {min_presses} presses")
            total_presses += min_presses
        else:
            print(f"Machine {i}: No solution!")
            return None
    
    return total_presses

# Solve for Part 1
result = solve_factory('solution.csv')
print(f"\n{'='*50}")
print(f"Total minimum button presses: {result}")
