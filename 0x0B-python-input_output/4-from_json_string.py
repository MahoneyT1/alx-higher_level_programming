#!/usr/bin/python3
"""represented by a JSON string"""
import json


def from_json_string(my_str):
    """ function that returns an object (Python data structure),
    represented by a JSON string.

    Args:
        my_str(jason string): param 1
    Return:
        an object in python data-structure
    """

    py_ob = json.loads(my_str)
    return py_ob
