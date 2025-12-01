def count_zeros_during_rotation(start, direction, distance):
    """Count how many times the dial points at 0 during a rotation"""
    zero_count = 0
    
    if direction == 'L':
        # Moving left (decreasing)
        for i in range(1, distance + 1):
            position = (start - i) % 100
            if position == 0:
                zero_count += 1
    else:  # direction == 'R'
        # Moving right (increasing)
        for i in range(1, distance + 1):
            position = (start + i) % 100
            if position == 0:
                zero_count += 1
    
    return zero_count

def solve_dial_puzzle_part2(rotations):
    position = 50
    total_zero_count = 0
    
    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])
        
        # Count zeros during this rotation
        zeros_during = count_zeros_during_rotation(position, direction, distance)
        total_zero_count += zeros_during
        
        # Update position
        if direction == 'L':
            position = (position - distance) % 100
        else:  # direction == 'R'
            position = (position + distance) % 100
    
    return total_zero_count

# Read your puzzle input
with open('solution.csv', 'r') as f:
    rotations = [line.strip() for line in f.readlines()]

password = solve_dial_puzzle_part2(rotations)
print(f"The password is: {password}")