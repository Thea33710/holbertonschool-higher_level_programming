#!/usr/bin/python3
def print_last_digit(number):
    nb = number

    if number >= 0:
        nb = nb % 10

    elif number < 0:
        nb = (-number) % 10

    print(f"{nb}", end="")
    return nb
