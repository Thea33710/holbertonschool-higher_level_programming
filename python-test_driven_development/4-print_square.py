#!/usr/bin/python3
"""
Module 4-print_square

Ce module contient la fonction print_square qui imprime
un carré.
"""


def print_square(size):

    """
    Print a square with a size.

    Args:
        size (an integer): the size of the square.

    Raises:
        TypeError: If size is not an integer,
        TypeError: If size is a float and less than zero,
        ValueError: if size is egual or less than zero

    Returns:
        None.
    """

    if size is None:
        raise TypeError(
            "print_square() missing 1 required positional argument: 'size'"
        )

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
