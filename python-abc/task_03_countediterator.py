#!/usr/bin/env python3

"""A CountedIterator class."""


class CountedIterator:
    """A class that extends the built-in iterator obtained from the iter function."""

    def __init__(self, iterable):
        """A function initiator."""
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """The iter function."""
        return self

    def __next__(self):
        """Override the next method."""
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """A method to retrieve and print the number of items that have been fetched."""
        return self.count
