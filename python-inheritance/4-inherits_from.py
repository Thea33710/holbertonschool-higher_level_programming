#!/usr/bin/python3

def inherits_from(obj, a_class):

    """
    Function that returns True if the object is an instance of
    an inherit class of the specified class, otherwise False.
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
