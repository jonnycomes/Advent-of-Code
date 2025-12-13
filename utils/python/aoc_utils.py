"""
Common utilities for Advent of Code solutions
"""

def read_input(filename="input.txt"):
    """Read input file and return as string"""
    with open(filename, 'r') as f:
        return f.read().strip()

def read_lines(filename="input.txt"):
    """Read input file and return as list of lines"""
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def read_integers(filename="input.txt"):
    """Read input file and return as list of integers (one per line)"""
    return [int(line.strip()) for line in read_lines(filename)]

def read_grid(filename="input.txt"):
    """Read input file as a 2D grid (list of lists)"""
    return [list(line) for line in read_lines(filename)]

def print_grid(grid):
    """Pretty print a 2D grid"""
    for row in grid:
        print(''.join(str(cell) for cell in row))

def manhattan_distance(p1, p2):
    """Calculate Manhattan distance between two points"""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def get_neighbors_4(x, y, max_x=None, max_y=None):
    """Get 4-directional neighbors (up, down, left, right)"""
    neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    if max_x is not None and max_y is not None:
        neighbors = [(nx, ny) for nx, ny in neighbors 
                    if 0 <= nx < max_x and 0 <= ny < max_y]
    return neighbors

def get_neighbors_8(x, y, max_x=None, max_y=None):
    """Get 8-directional neighbors (including diagonals)"""
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            neighbors.append((x + dx, y + dy))
    
    if max_x is not None and max_y is not None:
        neighbors = [(nx, ny) for nx, ny in neighbors 
                    if 0 <= nx < max_x and 0 <= ny < max_y]
    return neighbors

# Direction vectors for common movements
DIRECTIONS = {
    'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0),
    'NE': (1, -1), 'NW': (-1, -1), 'SE': (1, 1), 'SW': (-1, 1),
    '^': (0, -1), 'v': (0, 1), '>': (1, 0), '<': (-1, 0)
}
