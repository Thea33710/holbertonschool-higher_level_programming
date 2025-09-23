#!/usr/bin/env python3

from abc import ABC, abstractmethod
"""Abstract base class."""


class Animal(ABC):
    """A class animal."""

    @abstractmethod
    def sound(self):
        """A method to put in sublcasses."""

        pass


"""A dog class."""


class Dog(Animal):
    """A dog that inherits from Animal."""

    def sound(self):
        """The dog's sound."""

        return "Bark"


"""A cat class."""


class Cat(Animal):
    """A cat class that inherits from Animal."""

    def sound(self):
        """the cat's sound."""

        return "Meow"
