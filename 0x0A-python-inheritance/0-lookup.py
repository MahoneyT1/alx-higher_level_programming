#!/usr/bin/python3
""" Write a function that returns the list of available,
attributes and methods of an object.
"""


def lookup(obj):
    """Function that prints bultins func.
    args:
        obj(object):paramerer to list the builtins.

    Return:
        a list of avaiilable attributes of argument.
    """
    return dir(obj)
