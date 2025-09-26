#!/usr/bin/python3

"""Abstract base class."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """A class that inherits from ABC."""

    @abstractmethod
    def area(self):
        """A method to put in subclasses."""
        raise Exception("area() is not implemented")

    @abstractmethod
    def perimeter(self):
        """A method to put in subclasses."""
        raise Exception("perimeter() is not implemented")


class Circle(Shape):
    """A circle class that inherits from Shape."""

    def __init__(self, radius):
        """A initializer for circle."""
        if radius <= 0:
            raise ValueError("The radius must be a positive integer")
        self.radius = radius

    def area(self):
        """The area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """The perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """A Rectangle class that inherits from Shape."""

    def __init__(self, width, height):
        """A initializer for Rectangle."""
        self.width = width
        self.height = height

    def area(self):
        """The area of the Rectangle."""
        return self.width * self.height

    def perimeter(self):
        """The perimeter of the Rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Some information."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
