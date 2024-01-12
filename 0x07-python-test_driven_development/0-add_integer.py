#!/usr/bin/python3
"""

define a function that adds two int

"""

def add_integer(a, b=98):

    """ function that adds two integers.

    args:
        a (int or float): parameter 1.
        b (int or float) - optional: parameter 2.

    raise exception:
        if typeError or valueError.

    """
    sum = 0

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    sum = (int(a) + int(b))

    return sum
