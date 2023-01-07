#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    args = sys.argv
    if len(args) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operators = ["+", "-", "*", "/"]
    if args[2] not in operators:
        print("Unkown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(args[1])
    b = int(args[3])
    operator = args[2]
    if operator == "+":
        print("{} {} {} = {}".format(a, operator, b, add(a, b)))
    elif operator == "-":
        print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
    elif operator == "*":
        print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
    elif operator == "/":
        print("{} {} {} = {}".format(a, operator, b, div(a, b)))
