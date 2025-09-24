#!/usr/bin/env python3

"""A mixed class swim"""


class SwimMixin:
    """A mixed class swim"""
    def swim(self):
        print("The creature swims!")


"""A mixed class fly."""


class FlyMixin:
    """A mixed class fly."""
    def fly(self):
        print("The creature flies!")


"""A dragon class."""


class Dragon(SwimMixin, FlyMixin):
    """A dragon class."""
    def roar(self):
        print("The dragon roars!")
