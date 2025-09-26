#!/usr/bin/python3

"""A geometry class."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that inherits from Rectangle."""

    def __init__(self, size):
        """
        Initializes a square with a given size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
