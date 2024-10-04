#!/usr/bin/python3
"""
Module pascal_triangle(n): Generates Pascal's triangle of size n
"""


def pascal_triangle(n):
    """
    Generates a Pascal's Triangle of size n.

    Args:
        n (int): The number of rows in Pascal's Triangle.

    Returns:
        List of lists of integers representing Pascal's Triangle.
        Returns an empty list if n <= 0.
    """
    triangle = []
    if n <= 0:
        return triangle

    # Initialize the triangle with the appropriate number of rows
    for i in range(n):
        triangle.append([1] * (i + 1))

    # Fill in the values for each row based on the previous row
    for row in range(2, n):
        for col in range(1, row):
            triangle[row][col] = triangle[row - 1][col - 1] + triangle[row - 1][col]

    return triangle


if __name__ == "__main__":
    print(pascal_triangle(5))
