#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """ Function that returns new dict with all
    values mult by 2
    """

    if a_dictionary:
        new_dict = dict()

        for k, v in a_dictionary.copy().items():
            new_dict[k] = v * 2

    return new_dict
