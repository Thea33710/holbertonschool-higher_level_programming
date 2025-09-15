#!/usr/bin/python3

"""
Class 4-square

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

        self.size = size


    @property
    def size(self):

        """Returns the size"""

        return self.__size


    @size.setter
    def size(self, value):

        """
        Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value


    def area(self):

        """Returns the current square area."""

        return self.__size * self.__size
