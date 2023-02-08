#!/usr/bin/python3
"""Defines a pascal triangle function."""


def pascal_triangle(n):
    """Computes a lists of lists of integers representing pascal's triangle.

    Args:
        n: the base of the triangle.
    """
    if n <= 0:
        return []
    
    triangles = [[1]]
    while len(triangle) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) -1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
