#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """function that prints an integer only.

    If Value error occurs a correspoinding
    message is printed to standard error.

    Args:
        value (int): expected parameter to be of int.

    Returns:
        If TypeError or ValueError - False.
        else - True
    """
    try:
        print("{:d}".format(value))
        return (True)
    except(TypeError, ValueError):
        print("Exception:", sys.exc_info()[1], file=sys.stderr)
        return (False)
