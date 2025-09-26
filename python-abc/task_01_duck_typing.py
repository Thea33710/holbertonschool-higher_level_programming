#!/usr/bin/python3

from abc import ABC, abstractmethod
import math
"""Abstract base class."""


class Shape(ABC):
    """A class that inherite from ABC."""

    @abstractmethod
    def area(self):
        """A method to put in sublcasses."""
        pass

    @abstractmethod
    def perimeter(self):
        """A method to put in sublcasses."""
        pass


"""A circle class."""


class Circle(Shape):
    """A circle class that inherite from Shape."""

    def __init__(self, radius):
        """A initiator for circle."""
        self.radius = radius

    def area(self):
        """The area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """The perimeter of the circle."""
        return 2 * math.pi * self.radius


"""A Rectangle class."""


class Rectangle(Shape):
    """A Rectangle class that inherite from Shape."""

    def __init__(self, width, height):
        """A initiator for Rectangle."""
        self.width = width
        self.height = height

    def area(self):
        """The area of the Rectangle."""
        return self.width * self.height

    def perimeter(self):
        """The perimeter of the Rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Some informations."""
    print(f"Area: {shape.area():}")
    print(f"Perimeter: {shape.perimeter():}")
