#!/usr/bin/python3
"""
Module 5-text_indentation

Ce module contient la fonction text_indentation qui imprime
un text avec 2 nouvelles lignes après chacun de ces
charactères ".", "?", ":".
"""


def text_indentation(text):

    """
    Print a text with 2 new lines after each of these
    characters: ".", "?" and ":".

    Args:
        text (a string): the text to indented.

    Raises:
        TypeError: If text is not a string

    Returns:
        Nothing.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']

    result = []
    temp = ""

    for char in text:
        temp += char
        if char in separators:
            result.append(temp.strip())
            temp = ""

    if temp.strip():
        result.append(temp.strip())

    for i, sentence in enumerate(result):
        print(sentence)

        if i != len(result) - 1:
            print()
