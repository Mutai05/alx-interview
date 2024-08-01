#!/usr/bin/python3
"""
0-island_perimeter
"""
def island_perimeter(grid):
    """
    Calculate the perimeter of the island in a grid.
    
    Args:
    grid (list of list of int): 2D list representing the grid where 1's are land and 0's are water.
    
    Returns:
    int: The perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # land cell
                # Check all four directions
                if i == 0 or grid[i - 1][j] == 0:  # top edge
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:  # bottom edge
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # left edge
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:  # right edge
                    perimeter += 1

    return perimeter
