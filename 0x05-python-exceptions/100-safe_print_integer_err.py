#!/usr/bin/python3
import sys



def safe_print_integer_err(value):
    """ a function that prints an integer only.

    args:
        value (int): expected parameter to be of int.
    """
    try:
        print("{:d}".format(value))
        return True

    except Exception:
        print("Exception: {}".format(sys.exc_info()[1], file=sys.stderr))
        return False
