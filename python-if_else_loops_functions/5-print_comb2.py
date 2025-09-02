#!/usr/bin/python3

a = 0
b = 0

while a <= 9:
    if a != 9 and b <= 9:
        print(f"{a}{b}, ", end="")

    elif a == 9 and b == 9:
        print(f"{a}{b}")
    b += 1

    if b > 9:
        b = 0
        a += 1
