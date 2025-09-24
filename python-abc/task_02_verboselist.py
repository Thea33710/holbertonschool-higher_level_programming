#!/usr/bin/env python3

"""A class that extends the Python list class."""


class VerboseList(list):
    """A class that inherits from list."""
    def append(self, item):
        """A function that add an item to the list."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """A function that extend the list."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """A functions that remove an item."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item from the list."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
