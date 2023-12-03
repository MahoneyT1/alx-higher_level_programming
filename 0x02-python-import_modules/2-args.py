#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """Print the number of and list of arguments."""

    argument = 0
    len_o_av = len(sys.argv) - 1

    if len_o_av == 0:
        argument = 0
        print("{} arguments.".format(argument))

    elif len_o_av == 1:
        for i in range(1, len(sys.argv)):
            argument += 1
            print("{} argument:".format(argument))
            print("{}: ".format(i), sys.argv[i])

    elif len_o_av > 1:
        for i in range(1, len(sys.argv)):
            argument += 1

        print("{} argument:".format(argument))

        for i in range(1, len(sys.argv)):
            print("{}: ".format(i), sys.argv[i])
