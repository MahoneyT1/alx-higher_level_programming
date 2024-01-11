#!/usr/bin/python3
""" funtion that reads js file """
import json


def load_from_json_file(filename):
    """function that creates an Object from a JSON file.

    Args:
        filename(path): param1
    Return:
        read
    """
    with open(filename) as f:
        g = json.load(f)
        return g
