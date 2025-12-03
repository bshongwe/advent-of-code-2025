def find_max_joltage_part2(bank):
    """Find the maximum joltage by selecting exactly 12 batteries"""
    n = len(bank)
    num_to_select = 12
    num_to_skip = n - num_to_select
    
    if num_to_skip == 0:
        return int(bank)
    
    # Greedy approach: at each step, choose the largest digit we can
    # while ensuring we have enough digits remaining
    result = []
    start_pos = 0
    
    for i in range(num_to_select):
        # How many more digits do we need after this one?
        remaining_needed = num_to_select - i - 1
        # Latest position we can start from (must leave enough for remaining)
        latest_pos = n - remaining_needed - 1
        
        # Find the maximum digit in the valid range
        max_digit = '0'
        max_pos = start_pos
        
        for pos in range(start_pos, latest_pos + 1):
            if bank[pos] > max_digit:
                max_digit = bank[pos]
                max_pos = pos
        
        result.append(max_digit)
        start_pos = max_pos + 1
    
    return int(''.join(result))

def solve_escalator_part2(input_string):
    """Find the total output joltage from all banks (Part 2)"""
    banks = input_string.strip().split('\n')
    total_joltage = 0
    
    for bank in banks:
        bank = bank.strip()
        if bank:
            max_joltage = find_max_joltage_part2(bank)
            total_joltage += max_joltage
            print(f"Bank {bank}: max joltage = {max_joltage}")
    
    return total_joltage

# Example test
# example_input = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111"""

# result = solve_escalator_part2(example_input)
# print(f"\nExample total output joltage: {result}")

# For your actual puzzle input
with open('solution.csv', 'r') as f:
    puzzle_input = f.read()

answer = solve_escalator_part2(puzzle_input)
print(f"\nThe total output joltage is: {answer}")