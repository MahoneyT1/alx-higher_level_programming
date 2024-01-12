#!/usr/bin/python3
"""
define a function that adds two int
"""


def add_integer(a, b=98):
    """Addition function of two integers.
    Args:
        a (int or float): The first number to be added.
        b (int or float, optional): Second number.

    Raises:
        TypeError: If either `a` or `b` is not an int & float.

    Returns:
        int: The addition of `a` and `b` as an integer.
    """
    sum = 0
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    sum = (int(a) + int(b))
    return sum
