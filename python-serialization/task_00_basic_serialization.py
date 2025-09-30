#!/usr/bin/python3

"""
A module that adds the functionality to serialize a Python
dictionary to a JSON file and deserialize the JSON
file to recreate the Python Dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Parameters:
    - data (dict): The dictionary to serialize.
    - filename (str): The name of the file to save the JSON data to.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def load_and_deserialize(filename):
    """
    Load JSON data from a file and deserialize it to a Python dictionary.

    Parameters:
    - filename (str): The name of the file to read the JSON data from.

    Returns:
    - dict: The deserialized dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
