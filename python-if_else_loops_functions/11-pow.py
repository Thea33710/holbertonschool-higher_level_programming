#!/usr/bin/env python3
def pow(a, b):
    result = 1
    if b < 0:
        a = 1 / a
        b = -b
    while b > 0:
        result *= a
        b -= 1
    return result
