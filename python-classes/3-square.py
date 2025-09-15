#!/usr/bin/python3

"""
Class 3-square

This class defines a square by a size.
"""


class Square:

    """Defines a square."""

    def __init__(self, size=0):

        """
        Initializes the square with a given size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):

        """Returns the current square area."""

        return self.__size * self.__size
