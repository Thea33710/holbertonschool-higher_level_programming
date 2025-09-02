#!/usr/bin/env python3
def fizzbuzz():
    i = 1
    while i <= 100:

        if (i % 3) == 0 and (i % 5) == 0:
            print("FizzBuzz ")

        elif (i % 3) == 0:
            print("Fizz ")

        elif (i % 5) == 0:
            print("Buzz ")

        else:
            print(f"{i} ")

        i += 1
