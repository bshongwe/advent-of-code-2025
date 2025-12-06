"""
Advent of Code 2025 - Day 6
"""

def solve_cephalopod_worksheet_v3(filename):
    """Solve using right-to-left cephalopod math"""
    with open(filename, 'r') as f:
        lines = [line.rstrip('\n') for line in f.readlines()]
    
    max_width = max(len(line) for line in lines)
    lines = [line.ljust(max_width) for line in lines]
    num_rows = len(lines)
    
    # Read right-to-left, column by column
    col_idx = max_width - 1
    problems = []
    
    while col_idx >= 0:
        # Skip separator columns (all spaces)
        while col_idx >= 0 and all(lines[row][col_idx] == ' ' for row in range(num_rows)):
            col_idx -= 1
        
        if col_idx < 0:
            break
        
        # Extract a problem (collect columns until we hit a separator)
        problem_cols = []
        while col_idx >= 0 and not all(lines[row][col_idx] == ' ' for row in range(num_rows)):
            column = [lines[row][col_idx] for row in range(num_rows)]
            problem_cols.append(column)
            col_idx -= 1
        
        # problem_cols now contains columns from right-to-left
        # Each column represents one number (read top-to-bottom)
        # Last column has the operator at the bottom
        
        numbers = []
        operation = None
        
        for col in problem_cols:
            # Read top to bottom to form a number
            number_str = ''
            for i in range(len(col) - 1):  # Exclude last row
                if col[i] != ' ':
                    number_str += col[i]
            
            if number_str:
                numbers.append(int(number_str))
            
            # Get operation from last row
            if col[-1] in ['+', '*']:
                operation = col[-1]
        
        if numbers and operation:
            problems.append((numbers, operation))
    
    # Calculate grand total
    grand_total = 0
    
    for prob_idx, (numbers, operation) in enumerate(problems, 1):
        result = numbers[0]
        for num in numbers[1:]:
            if operation == '+':
                result += num
            elif operation == '*':
                result *= num
        
        print(f"Problem {prob_idx}: {' {} '.format(operation).join(map(str, numbers))} = {result}")
        grand_total += result
    
    return grand_total

result = solve_cephalopod_worksheet_v3('solution.csv')
print(f"\nGrand Total: {result}")
