#!/usr/bin/python3

a = 0

while a <= 9:
    b = a + 1
    while b <= 9:
        if a == 8 and b == 9:
            print(f"{a}{b}")

        else:
            print(f"{a}{b}, ", end="")

        b += 1
    a += 1
    