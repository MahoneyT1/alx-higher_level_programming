#!/usr/bin/python3

def safe_print_integer(value):
    """ Write a function that prints an integer """
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True

    except TypeError:
            return False
