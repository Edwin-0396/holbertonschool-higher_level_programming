#!/usr/bin/python3

"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Function to print the pascal triangle
    Args:
    n: number of rows
    """
    if n <= 0:
        return []
    pascal = []
    row = []
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(i):
                row.append(sum(pascal[-1][j:j+2]))
        pascal.append(row)
    return pascal
