#!/usr/bin/python3

"""A module with a class Student."""


class Student:
    """A student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary of the student."""
        return self.__dict__
