#!/usr/bin/python3
"""Pascal's triangle generator."""


def pascal_triangle(n):
    """Generate Pascal's triangle up to n rows."""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        previous_row = triangle[-1]
        next_row = [1]

        for j in range(len(previous_row) - 1):
            next_row.append(previous_row[j] + previous_row[j + 1])

        next_row.append(1)
        triangle.append(next_row)

    return triangle
