#!/usr/bin/python3



def safe_print_integer_err(value):
    """ a function that prints an integer """

    try:
        print("{:d}".format(value))
        return True

    except Exception as e:
        print("Exception: ", e)
        return False
