#!/usr/bin/python3
"""Function that check is a class is a subclass"""


def inherits_from(obj, a_class):
    """A function that checks for obj type.

    Args:
        obj (_type_): param 1 obect to be checked
        a_class (_type_): param 2 class to check if is iherited from

    Returns:
        True if it a subclass
        False if not
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
