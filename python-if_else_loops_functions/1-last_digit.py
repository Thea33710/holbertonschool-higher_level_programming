#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
nb = number

if number >= 0:
    nb = nb % 10

elif number > 0:
    nb = (-number) % 10

if nb > 5:
    print(f"Last digit of {number} is {nb} and is greater than 5")

elif nb == 0:
    print(f"Last digit of {number} is {nb} and is 0")

elif nb < 6:
    print(f"Last digit of {number} is {nb} and is less than 6 and not 0")
