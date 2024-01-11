#!/usr/bin/python3
""" Function that writes to text files"""
import json


def save_to_json_file(my_obj, filename):
    """ Function that writes an Object to a text file,
    using a JSON representation.

    Args:
        my_obj(text-file): param 1
        filename(path): param 2
    """

    with open(filename, "w") as js:
        json.dump(my_obj, js)
