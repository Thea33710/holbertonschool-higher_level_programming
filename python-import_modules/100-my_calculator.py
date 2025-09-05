#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys

    argc = len(sys.argv) - 1

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]

    if op not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if op == "+":
        print(f"{a} + {b} = {calculator_1.add(a, b)}")

    elif op == "-":
        print(f"{a} - {b} = {calculator_1.sub(a, b)}")

    elif op == "*":
        print(f"{a} * {b} = {calculator_1.mul(a, b)}")

    elif op == "/":
        if b == 0:
            print("Error: division by zero")
            exit(1)
        print(f"{a} / {b} = {calculator_1.div(a, b)}")
