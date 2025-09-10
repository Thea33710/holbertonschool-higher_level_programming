#!/usr/bin/python3
"""
Fonction add_integer

Cette fonction ajoute deux nombres,
en s'assurant qu'ils sont des entiers ou des flottants,
avec conversion des flottants en entiers, et lève une
exception si les types sont invalides.
"""


def add_integer(a, b=98):
    """
    Additionne deux nombres entiers ou flottants.

    Args:
        a (int ou float): Le premier nombre.
        b (int ou float, optionnel): Le second nombre, par défaut 98.

    Raises:
        TypeError: Si a ou b ne sont ni int ni float.

    Returns:
        int: La somme de a et b, après conversion en entier.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
