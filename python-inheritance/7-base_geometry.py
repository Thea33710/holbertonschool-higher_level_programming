#!/usr/bin/python3

"""A geometry class."""


class BaseGeometry:

    """A geometry class."""

    def area(self):

        """Raises an Exception with a message."""

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

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
