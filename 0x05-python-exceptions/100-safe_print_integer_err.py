#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """ a function that prints an integer """

    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            raise TypeError
    except TypeError:
        print("Exception: ", sys.stderr)
        return False
