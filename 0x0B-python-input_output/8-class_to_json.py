#!/usr/bin/python3
""" Write a function that returns destription"""


def class_to_json(obj):
    """ return obj description.

    Args:
        obj(any): param 1
    """

    return obj.__dict__
