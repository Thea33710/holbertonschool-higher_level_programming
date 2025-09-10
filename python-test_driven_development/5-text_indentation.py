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
        None.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sentence = ""
    result = ""
    i = 0
    while i < len(text):
        if text[i] == " ":
            j = i

            while j < len(text) and text[j] == " ":
                j += 1

            if j < len(text) and text[j] in ".?:":
                i = j
                continue

        result += text[i]
        i += 1

    text = result

    for i in range(len(text)):
        sentence += text[i]

        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print(sentence.strip(), end="")
            print()
            print()
            sentence = ""

    print(sentence.strip(), end="")
