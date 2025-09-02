#!/usr/bin/python3
def uppercase(str):
    i = 0
    while i < len(str):
        char = str[i]
        if 97 <= ord(char) <= 122:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
        i += 1
    print()
