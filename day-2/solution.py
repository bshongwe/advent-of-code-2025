def is_invalid_id(num):
    """Check if a number is invalid (pattern repeated twice)"""
    s = str(num)
    length = len(s)
    
    # Must have even length to be repeated twice
    if length % 2 != 0:
        return False
    
    # Split in half and check if both halves are identical
    mid = length // 2
    first_half = s[:mid]
    second_half = s[mid:]
    
    return first_half == second_half

def solve_gift_shop(input_string):
    """Find sum of all invalid IDs in the given ranges"""
    # Parse the input
    ranges = input_string.strip().split(',')
    
    total_sum = 0
    
    for range_str in ranges:
        range_str = range_str.strip()
        if not range_str:
            continue
            
        # Parse the range
        start, end = map(int, range_str.split('-'))
        
        # Check each ID in the range
        for num in range(start, end + 1):
            if is_invalid_id(num):
                total_sum += num
    
    return total_sum

# Example test
# example_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659,
# 824824821-824824827,2121212118-2121212124"""

# result = solve_gift_shop(example_input)
# print(f"Example result: {result}")

# For your actual puzzle input
with open('solution.csv', 'r') as f:
    puzzle_input = f.read()

answer = solve_gift_shop(puzzle_input)
print(f"The sum of all invalid IDs is: {answer}")