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
            name (str): always a string.
            value (int): a positive integer.

        Raises:
            TypeError: If value is not a integer.
            ValueError: If value is less or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
