#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """function that prints an integer only.

    if Value error occurs a correspoinding
    message is printed to standard error.

    Args:
        value (int): expected parameter to be of int.

    Returns:
        True if success else False.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1], \
                sys.stderr))
        return(False)
