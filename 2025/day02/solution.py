#!/usr/bin/env python3
"""
Template for Advent of Code solutions
Copy this file to start a new day's solution
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import aoc

def parse_input(input_text):
    """Parse the input text into a useful format"""
    # Split input into ranges
    ranges = input_text.strip().split(',')
    # Convert to list of tuples
    ranges = [
        tuple(map(int, r.split('-')))
        for r in ranges
    ]
    # Convert to list of range objects
    ranges = [range(start, end + 1) for start, end in ranges]
    return ranges

def part1(data):
    """Solve part 1 of the problem"""
    invalids = []
    for rng in data:
        for num in rng:
            num_str = str(num)
            mid = len(num_str) // 2
            if num_str[:mid] == num_str[mid:]:
                invalids.append(num)
    return sum(invalids)

def part2(data):
    """Solve part 2 of the problem"""
    # TODO: Implement part 2
    return 0

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
