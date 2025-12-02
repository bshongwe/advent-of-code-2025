def is_invalid_id_part2(num):
    """Check if a number is invalid (pattern repeated at least twice)"""
    s = str(num)
    length = len(s)
    
    # Try all possible pattern lengths (from 1 to length/2)
    # Pattern must repeat at least twice, so max pattern length is length/2
    for pattern_length in range(1, length // 2 + 1):
        # Check if this pattern length divides evenly into total length
        if length % pattern_length == 0:
            pattern = s[:pattern_length]
            
            # Check if the entire string is this pattern repeated
            num_repetitions = length // pattern_length
            if pattern * num_repetitions == s:
                return True
    
    return False

def solve_gift_shop_part2(input_string):
    """Find sum of all invalid IDs in the given ranges (Part 2)"""
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
            if is_invalid_id_part2(num):
                total_sum += num
    
    return total_sum

# # Example test
# example_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659,
# 824824821-824824827,2121212118-2121212124"""

# result = solve_gift_shop_part2(example_input)
# print(f"Example result: {result}")

# Actual puzzle input
with open('solution.csv', 'r') as f:
    puzzle_input = f.read()

answer = solve_gift_shop_part2(puzzle_input)
print(f"The sum of all invalid IDs is: {answer}")