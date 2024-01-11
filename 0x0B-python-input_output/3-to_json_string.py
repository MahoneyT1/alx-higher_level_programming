#!/usr/bin/python3
""" json file representation """
import json


def to_json_string(my_obj):
    """ function that returns the JSON representation of an object (string).

    Args:
        my_obj(list):param 1

    Return:
        A json representation of a object.
    """

    json_r = json.dumps(my_obj)
    return json_r
