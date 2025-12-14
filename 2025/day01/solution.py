#!/usr/bin/env python3
"""
Template for Advent of Code solutions
Copy this file to start a new day's solution
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import aoc
cd
def parse_input(input_text):
    """Parse the input text into a useful format"""
    lines = input_text.strip().split('\n')
    rotations = [
        (-1 if x[0] == 'L' else 1 if x[0] == 'R' else 0) * int(x[1:])
        for x in lines
    ]
    return rotations

def part1(data):
    """Solve part 1 of the problem"""
    START_POS = 50
    TOTAL_POS = 100
    pos = START_POS
    password = 0
    for move in data:
        pos = (pos + move) % TOTAL_POS
        if pos == 0:
            password += 1
    return password

def part2(data):
    """Solve part 2 of the problem"""
    START_POS = 50
    TOTAL_POS = 100
    pos = START_POS
    password = 0
    for move in data:
        # Increment password by one for every full rotation within the move
        rotation = abs(move) // TOTAL_POS
        password += rotation
        # Update position
        new_pos = (pos + move) % TOTAL_POS
        # Check if we crossed the zero point
        if new_pos == 0 and pos != 0:
            password += 1
        elif (move > 0 and new_pos < pos) or (move < 0 and new_pos > pos and pos != 0):
            password += 1
        pos = new_pos
    return password

def main():
    # Read input
    input_text = aoc.read_input()
    data = parse_input(input_text)
    
    # Solve parts
    result1 = part1(data)
    result2 = part2(data)
    
    print(f"Part 1: {result1}")
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()
