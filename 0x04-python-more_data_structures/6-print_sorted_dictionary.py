#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """ a function that prints a dictionary by ordered keys """

    if a_dictionary:

        for i, j in sorted(a_dictionary.copy().items()):
            print("{}: {}".format(i, j))

    else:
        return None
