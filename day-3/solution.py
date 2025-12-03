"""
Advent of Code 2025 - Day 3
"""

def find_max_joltage(bank):
    """Find the maximum joltage from a bank by selecting two batteries"""
    max_joltage = 0
    
    # Try all pairs of positions (i, j) where i < j
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            # Form the two-digit number using batteries at positions i and j
            joltage = int(bank[i] + bank[j])
            max_joltage = max(max_joltage, joltage)
    
    return max_joltage

def solve_escalator(input_string):
    """Find the total output joltage from all banks"""
    banks = input_string.strip().split('\n')
    total_joltage = 0
    
    for bank in banks:
        bank = bank.strip()
        if bank:
            max_joltage = find_max_joltage(bank)
            total_joltage += max_joltage
            print(f"Bank {bank}: max joltage = {max_joltage}")
    
    return total_joltage

# Example test
# example_input = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111"""

# result = solve_escalator(example_input)
# print(f"\nExample total output joltage: {result}")

# For your actual puzzle input
with open('solution.csv', 'r') as f:
    puzzle_input = f.read()

answer = solve_escalator(puzzle_input)
print(f"\nThe total output joltage is: {answer}")
    
