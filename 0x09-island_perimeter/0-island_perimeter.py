#!/usr/bin/python3

"""
This module provides the function `island_perimeter`
"""


def island_perimeter(grid: list):
    """
    Calculates and returns the perimeter of an island in `grid`
    """
    if grid is None:
        return 0
    if len(grid) == 0:
        return 0
    perimeter = 0
    rows = len(grid)
    columns = len(grid[0])
    if all([all(row) for row in grid]):
        return 2 * (rows + columns)
    onLand = False
    paths_to_follow = []
    paths_followed = []
    i, j = 0, 0
    while i < rows:
        j = 0
        while j < columns:

            cell_perimeter = 0
            if grid[i][j]:
                paths_followed.append((i, j))
                if i - 1 >= 0:
                    if not grid[i - 1][j]:
                        cell_perimeter += 1
                    else:
                        path = (i - 1, j)
                        if (path not in paths_followed and
                                path not in paths_to_follow):
                            paths_to_follow.append(path)
                else:
                    cell_perimeter += 1
                if i + 1 < rows:
                    if not grid[i + 1][j]:
                        cell_perimeter += 1
                    else:
                        path = (i + 1, j)
                        if (path not in paths_followed and
                                path not in paths_to_follow):
                            paths_to_follow.append(path)
                else:
                    cell_perimeter += 1
                if j - 1 >= 0:
                    if not grid[i][j - 1]:
                        cell_perimeter += 1
                    else:
                        path = (i, j - 1)
                        if (path not in paths_followed and
                                path not in paths_to_follow):
                            paths_to_follow.append(path)
                else:
                    cell_perimeter += 1
                if j + 1 < columns:
                    if not grid[i][j + 1]:
                        cell_perimeter += 1
                    else:
                        path = (i, j + 1)
                        if (path not in paths_followed and
                                path not in paths_to_follow):
                            paths_to_follow.append(path)
                else:
                    cell_perimeter += 1
            perimeter += cell_perimeter
            if cell_perimeter >= 3:
                if not len(paths_to_follow):
                    onLand = True
                if onLand and not len(paths_to_follow):
                    return perimeter
                else:
                    onLand = True
            elif not onLand:
                perimeter -= cell_perimeter
                paths_to_follow = []
                if len(paths_followed):
                    paths_followed.pop()
            if onLand and len(paths_to_follow):
                next = paths_to_follow.pop()
                paths_followed = list(set(paths_followed))
                paths_to_follow = list(set(paths_to_follow))
                i, j = next
                continue
            onLand = False
            if not onLand and perimeter:
                return perimeter
            j += 1
        i += 1

    return 0
