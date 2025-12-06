"""
Advent of Code 2025 - Day 6
"""

def solve_worksheet_simple(filename):
    """
    Simplified solution assuming clear column separation
    """
    with open(filename, 'r') as f:
        lines = [line.rstrip('\n') for line in f.readlines()]
    
    # Pad lines to same width
    max_width = max(len(line) for line in lines)
    lines = [line.ljust(max_width) for line in lines]
    
    # Split by empty columns
    problems = []
    current_problem = []
    
    for col_idx in range(max_width):
        column = [line[col_idx] for line in lines]
        
        # Check if column is empty
        if all(c == ' ' for c in column):
            if current_problem:
                problems.append(current_problem)
                current_problem = []
        else:
            current_problem.append(column)
    
    # Handle last problem
    if current_problem:
        problems.append(current_problem)
    
    # Process each problem
    grand_total = 0
    
    for prob_idx, problem in enumerate(problems, 1):
        # Combine columns and extract data
        rows = [''.join(col).strip() for col in zip(*problem)]
        rows = [r for r in rows if r]
        
        operation = rows[-1]
        numbers = [int(r) for r in rows[:-1]]
        
        # Calculate
        result = numbers[0]
        for num in numbers[1:]:
            if operation == '+':
                result += num
            elif operation == '*':
                result *= num
        
        print(f"Problem {prob_idx}: {numbers} {operation} = {result}")
        grand_total += result
    
    return grand_total

# Run solution
result = solve_worksheet_simple('solution.csv')
print(f"\nGrand Total: {result}")
