#!/usr/bin/python3

i = 0
while i <= 98:
    if i == 98:
        print("{:d} = 0x{:x}".format(i, i))
    else:
        print("{:d} = 0x{:x}, ".format(i, i), end="")
    i += 1
