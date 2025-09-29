#!/usr/bin/python3

"""A module that creates an Object from a JSON file."""


def load_from_json_file(filename):
    """A function that creates an Object from a JSON file."""
    import json
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
