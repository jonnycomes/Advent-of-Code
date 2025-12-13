#!/usr/bin/env python3
"""
Template for Advent of Code solutions
Copy this file to start a new day's solution
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'utils', 'python'))
from aoc_utils import read_input, read_lines

def parse_input(input_text):
    """Parse the input text into a useful format"""
    lines = input_text.strip().split('\n')
    # TODO: Parse input according to problem requirements
    return lines

def part1(data):
    """Solve part 1 of the problem"""
    # TODO: Implement part 1
    return 0

def part2(data):
    """Solve part 2 of the problem"""
    # TODO: Implement part 2
    return 0

def main():
    # Read input
    input_text = read_input()
    data = parse_input(input_text)
    
    # Solve parts
    result1 = part1(data)
    result2 = part2(data)
    
    print(f"Part 1: {result1}")
    print(f"Part 2: {result2}")

if __name__ == "__main__":
    main()
