#!/usr/bin/python3

"""
Class 4-rectangle

This class defines a rectangle.
"""


class Rectangle:

    """Defines a rectangle."""

    def __init__(self, width=0, height=0):

        """
        Initializes the rectangle with a given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """

        self.width = width
        self.height = height

    @property
    def width(self):

        """Returns the width"""

        return self.__width

    @property
    def height(self):

        """Returns the height"""

        return self.__height

    @width.setter
    def width(self, value):

        """
        Set the width of the rectangle.

        Args:
            value (int): the new width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):

        """
        Set the height of the rectangle.

        Args:
            value (int): the new height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):

        """Returns the area of the rectangle."""

        return self.__width * self.__height

    def perimeter(self):

        """Returns the perimeter of the rectangle."""

        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):

        """Prints the rectangle with the character #."""

        if self.__width == 0 or self.__height == 0:
            return ""

        lines = []
        for i in range(self.height):
            lines.append("#" * self.width)

        return "\n".join(lines)

    def __repr__(self):

        """Returns a string representation of the rectangle."""

        return f"Rectangle({self.width}, {self.height})"
