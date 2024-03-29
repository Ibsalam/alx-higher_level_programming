#!/usr/bin/python3
"""Defines a matrix division function."""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Parameters:
    matrix (list of lists): The matrix to be divided.
    div (int or float): The number to divide all elements of the matrix.

    Returns:
    list of lists: The new matrix with elements rounded to 2 decimal places.

    Raises:
    TypeError: If matrix is not a list of lists of integers/floats, if rows have different sizes,
               or if div is not a number.
    ZeroDivisionError: If div is equal to 0.

    Example:
    >>> matrix = [
    ...     [1, 2, 3],
    ...     [4, 5, 6]
    ... ]
    >>> matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    >>> print(matrix)
    [[1, 2, 3], [4, 5, 6]]
    """
    if not all(isinstance(row, list) and all(isinstance(x, (int, float)) for x in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return (result_matrix)
