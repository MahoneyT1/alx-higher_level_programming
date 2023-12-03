#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import calculator_1
    import sys

    lent_of_arg = len(argv) - 1

    if lent_of_arg < 3:
        print(print("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        sys.exit(1)

    elif lent_of_arg >= 3:
        if argv[2] == '+':
            sum = calculator_1.add(int(argv[1]), int(argv[3]))
            print("{} + {} = {}".format(argv[1], argv[3], sum))

        elif argv[2] == '-':
            sum = calculator_1.sub(int(argv[1]), int(argv[3]))
            print("{} + {} = {}".format(argv[1], argv[3], sum))


        elif argv[2] == "*":
            sum = calculator_1.mul(int(argv[1]), int(argv[3]))
            print("{} + {} = {}".format(argv[1], argv[3], sum))


        elif argv[2] == '/':
            sum = calculator_1.div(int(argv[1]), int(argv[3]))
            print("{} + {} = {}".format(argv[1], argv[3], sum))

        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
