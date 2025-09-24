#!/usr/bin/env python3

"""A class for fishes."""


class Fish:
    """A class for a fish."""
    def swim(self):
        """A fish swimming."""
        print("The fish is swimming")

    def habitat(self):
        """The habitat of the fish."""
        print("The fish lives in water")


"""A class for birds."""


class Bird:
    """A class for a bird."""
    def fly(self):
        """A bird flying."""
        print("The bird is flying")

    def habitat(self):
        """The habitat of the bird."""
        print("The bird lives in the sky")


"""A class FlyingFish."""


class FlyingFish(Fish, Bird):
    """A flying fish class."""
    def fly(self):
        """A flying fish flying."""
        print("The flying fish is soaring!")

    def swim(self):
        """A flying fish swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """The habitat of the flying fish."""
        print("The flying fish lives both in water and the sky!")
