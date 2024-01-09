#!/usr/bin/python3
""" define a class checking function """


def is_same_class(obj, a_class):
    """ A function that return True if obj is a an obj of the,
        same cls.

    Args:
        obj(obj): param 1 object to check
        a_class(cls): param 2 class to check.

    Returns:
        True if obj(any)is object of the same class
        False if it is not.

    """
    if type(obj) == a_class:
        return True
    else:
        return False
