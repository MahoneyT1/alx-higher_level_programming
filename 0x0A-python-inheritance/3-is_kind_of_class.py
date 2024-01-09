#!/usr/bin/python3
"""Function that checks for instance """


def is_kind_of_class(obj, a_class):
    """A function if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class.

    Args:
        obj (any): param 1 to be checked if is isntance.
        a_class (class): subject to be evaluated with.

    Return:
        True if isinstance.
        False if not.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
