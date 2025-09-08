#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    a_dictionary = {
     'I': 1,
     'V': 5,
     'X': 10,
     'L': 50,
     'C': 100,
     'D': 500,
     'M': 1000,
    }

    total = 0
    prev = 0

    for char in reversed(roman_string):
        value = a_dictionary.get(char, 0)
        if value < prev:
            total -= value
        else:
            total += value
        prev = value

    return total
