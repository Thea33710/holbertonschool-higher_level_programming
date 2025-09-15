#!/usr/bin/python3

"""
Class 6-square

This class defines a square by a size.
"""


class Square:

    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):

        """
        Initializes the square with a given size.

        Args:
            size (int): The size of the square.
            position (tuple of int): set the position of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        self.size = size
        self.position = position

    @property
    def size(self):

        """Returns the size"""

        return self.__size

    @property
    def position(self):

        """Returns position"""

        return self.__position

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

    @position.setter
    def position(self, value):

        """
        Set the position of the square.

        Args:
            value (tuple of int): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """

        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):

        """Returns the current square area."""

        return self.__size * self.__size

    def my_print(self):

        """Prints a square."""

        if (self.size == 0):
            print()

        else:
            for y in range(self.position[1]):
                print()

            for i in range(self.size):

                for u in range(self.position[0]):
                    print(" ", end="")

                print("#" * self.size)
