#!/usr/bin/python3

a = 0
b = 0

while a <= 9:
    print(f"{a}{b}, ", end="")
    b += 1

    if a == 9 and b > 9:
        print()

    if b > 9:
        b = 0
        a += 1
