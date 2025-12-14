"""
Common utilities for Advent of Code solutions
"""

def read_input(filename="input.txt"):
    """Read input file and return as string"""
    with open(filename, 'r') as f:
        return f.read().strip()

