#!/usr/bin/python3

"""
Learn how to serialize and deserialize
custom Python objects using the pickle module.
"""

import pickle
import os


class CustomObject:
    """A class for on object."""

    def __init__(self, name: str, age: int, is_student: bool):
        """A constructor."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display objest's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance of the
        object and save it to the provided filename.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Serialization failed: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Load and return an instance of the
        CustomObject from the provided filename.
        """
        if not os.path.exists(filename):
            return None

        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
                else:
                    return None
        except Exception as e:
            print(f"Deserialization failed: {e}")
            return None
