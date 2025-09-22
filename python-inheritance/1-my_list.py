#!/usr/bin/python3

"""A module for a class MyList."""


class MyList(list):

    """A class that inherit of list."""

    def print_sorted(self):

        """Prints the list, but sorted (ascending sort)."""

        print(sorted(self))
