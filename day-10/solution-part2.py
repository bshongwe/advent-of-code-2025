"""
Advent of Code 2025 - Day 10 Part 2
Gaussian elimination with exact arithmetic
"""

import re
from fractions import Fraction

def parse_machine(line):
    buttons = []
    for match in re.finditer(r'\(([0-9,]+)\)', line):
        indices = [int(x) for x in match.group(1).split(',')]
        buttons.append(indices)
    
    joltage_match = re.search(r'\{([0-9,]+)\}', line)
    targets = [int(x) for x in joltage_match.group(1).split(',')]
    
    return buttons, targets

def build_coefficient_matrix(buttons, targets):
    """
    Build coefficient matrix where
    A[i][j] = 1 if button j affects counter i
    """
    rows = len(targets)
    cols = len(buttons)
    matrix = [[0] * cols for _ in range(rows)]
    
    for btn_idx, counters in enumerate(buttons):
        for counter_idx in counters:
            if counter_idx < rows:
                matrix[counter_idx][btn_idx] = 1
    
    return matrix

def reduced_row_echelon(coefficients, targets):
    """
    Convert to reduced row echelon form using
    exact rational arithmetic
    """
    num_rows = len(coefficients)
    num_vars = len(coefficients[0])
    num_cols = num_vars + 1
    
    # Build augmented matrix with Fraction for exact arithmetic
    matrix = []
    for row in range(num_rows):
        matrix_row = []
        for col in range(num_vars):
            matrix_row.append(Fraction(coefficients[row][col]))
        matrix_row.append(Fraction(targets[row]))
        matrix.append(matrix_row)
    
    pivot_row = 0
    pivot_columns = []
    pivot_rows = []
    
    for col in range(num_vars):
        # Find pivot
        candidate_row = pivot_row
        while candidate_row < num_rows and matrix[candidate_row][col] == 0:
            candidate_row += 1
        
        if candidate_row == num_rows:
            continue
        
        # Swap rows if needed
        if candidate_row != pivot_row:
            matrix[pivot_row], matrix[candidate_row] = matrix[candidate_row], matrix[pivot_row]
        
        # Scale pivot row
        pivot_value = matrix[pivot_row][col]
        for c in range(col, num_cols):
            matrix[pivot_row][c] /= pivot_value
        
        # Eliminate other rows
        for row in range(num_rows):
            if row == pivot_row:
                continue
            factor = matrix[row][col]
            if factor == 0:
                continue
            for c in range(col, num_cols):
                matrix[row][c] -= factor * matrix[pivot_row][c]
        
        pivot_columns.append(col)
        pivot_rows.append(pivot_row)
        pivot_row += 1
        if pivot_row == num_rows:
            break
    
    # Check for inconsistency
    has_solution = True
    for row in range(num_rows):
        all_zero = all(matrix[row][col] == 0 for col in range(num_vars))
        if all_zero and matrix[row][num_vars] != 0:
            has_solution = False
            break
    
    return matrix, pivot_columns, pivot_rows, has_solution

def compute_bounds(buttons, targets):
    """
    Compute upper bounds for each button
    """
    bounds = []
    for button in buttons:
        if not button:
            bounds.append(0)
        else:
            min_target = min(targets[counter] for counter in button if counter < len(targets))
            bounds.append(min_target)
    return bounds

def solve_machine_exact(buttons, targets):
    """
    Solve using exact Gaussian elimination
    """
    if not buttons:
        return 0 if all(t == 0 for t in targets) else float('inf')
    
    coefficients = build_coefficient_matrix(buttons, targets)
    matrix, pivot_columns, pivot_rows, has_solution = reduced_row_echelon(coefficients, targets)
    
    if not has_solution:
        return float('inf')
    
    num_vars = len(buttons)
    free_variables = [i for i in range(num_vars) if i not in pivot_columns]
    bounds = compute_bounds(buttons, targets)
    
    best = float('inf')
    
    def assign_pivot_values(assignment):
        """
        Assign values to pivot variables based on free variables
        """
        augmented_col = len(matrix[0]) - 1
        for idx, pivot_col in enumerate(pivot_columns):
            row_idx = pivot_rows[idx]
            value = matrix[row_idx][augmented_col]
            
            for free_var in free_variables:
                coeff = matrix[row_idx][free_var]
                if coeff != 0:
                    value -= coeff * assignment[free_var]
            
            if value.denominator != 1 or value < 0:
                return None
            
            assignment[pivot_col] = int(value)
        
        return assignment
    
    def search(free_idx, assignment, current_sum):
        nonlocal best
        
        if current_sum >= best:
            return
        
        if free_idx == len(free_variables):
            final_assignment = assign_pivot_values(assignment[:])
            if final_assignment is not None:
                # Verify bounds
                if all(0 <= final_assignment[i] <= bounds[i] for i in range(num_vars)):
                    best = min(best, sum(final_assignment))
            return
        
        var_index = free_variables[free_idx]
        max_value = bounds[var_index]
        
        for value in range(max_value + 1):
            assignment[var_index] = value
            search(free_idx + 1, assignment, current_sum + value)
        
        assignment[var_index] = 0
    
    if not free_variables:
        # Unique solution
        assignment = [0] * num_vars
        final_assignment = assign_pivot_values(assignment)
        if final_assignment and all(0 <= final_assignment[i] <= bounds[i] for i in range(num_vars)):
            return sum(final_assignment)
        return float('inf')
    
    assignment = [0] * num_vars
    search(0, assignment, 0)
    
    return best if best != float('inf') else 0

def solve_factory_part2(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f if line.strip()]

    total = 0
    for line in lines:
        buttons, targets = parse_machine(line)
        result = solve_machine_exact(buttons, targets)
        total += result

    return total

result = solve_factory_part2('solution.csv')
print(result)
