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

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


"""A rectangle class."""


class Rectangle(BaseGeometry):

    """A class that inherits from BaseGeometry"""

    def __init__(self, width, height):

        """
        Initializes a rectangle with a given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):

        """Returns the area of the rectangle."""

        return self.__width * self.__height

    def __str__(self):

        """Return the rectangle description: [Rectangle] <width>/<height>."""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)


"""A square class."""


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
        super().__init__(size, size)
        self.__size = size

    def area(self):

        """Returns the area of the square."""

        return self.__size * self.__size
