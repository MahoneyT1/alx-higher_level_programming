#!/usr/bin/python3
import sys



def safe_print_integer_err(value):
    """ a function that prints an integer """

    try:
        fv = "{:d}".format(value)
        print(fv)
        return True

    except Exception as e:
        print(f"Exception:{e}", file=sys.stderr)
        return False
