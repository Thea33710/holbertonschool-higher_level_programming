#!/usr/bin/python3

"""A geometry class."""


class BaseGeometry:
    """A geometry class."""

    def area(self):
        """
        Raises an Exception with a message.

        Raises:
            Exception: If the area is not in the subclass.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value.

        Args:
            name: always a string.
            value: a positive integer.

        Raises:
            TypeError: If value is not a integer.
            ValueError: If value is less or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initializes a rectangle with a given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
