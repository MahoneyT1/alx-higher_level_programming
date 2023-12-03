#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argument = 0
    length = len(sys.argv)

    if length == 0:
        argument = 0
        print("{} arguments.".format(argument))

    elif length == 1:
        argument += 1

    print(f"{argument} argument:")

    elif length > 1:
        for i in range(1, len(sys.argv)):
        argument += 1

    print(f"{argument} arguments:")

    for i in range(1, length):
        print(f"{i}:", sys.argv[i])
