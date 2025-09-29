#!/usr/bin/python3

"""A module with a class Student."""


class Student:
    """A student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary of the student."""
        keys_order = ['age', 'last_name', 'first_name']
        result = {}

        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            for key in keys_order:
                if key in attrs and hasattr(self, key):
                    result[key] = getattr(self, key)
        else:
            for key in keys_order:
                if hasattr(self, key):
                    result[key] = getattr(self, key)
        return result
