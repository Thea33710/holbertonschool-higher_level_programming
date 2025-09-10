#!/usr/bin/python3
"""
Module 2-matrix_divided

Ce module contient la fonction matrix_divided qui divise
tous les éléments d'une matrice par un diviseur donné.
"""


def matrix_divided(matrix, div):

    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int/float): The divisor.

    Raises:
        TypeError: If matrix elements are not lists of ints/floats,
                   or if rows are not the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.

    Returns:
        New matrix with elements divided by div, rounded to 2 decimals.
    """

    if (not isinstance(matrix, list) or len(matrix) == 0):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        new_matrix.append(new_row)

    return new_matrix
