#!/usr/bin/python3
"""
Module 3-say_my_name

Ce module contient la fonction say_my_name qui écrit
le nom et le prénom.
"""


def say_my_name(first_name, last_name=""):

    """
    Write the firt name and the last name.

    Args:
        first_name (a string): The name to print.
        last_name (a string): The last name to print.

    Raises:
        TypeError: If first_name or last_name are not string,

    Returns:
        Nothing.
    """
    if first_name is None and last_name == "":
        break

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
