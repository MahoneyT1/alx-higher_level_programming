#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """ a function that prints a dictionary by ordered keys """

    for i, j in sorted(a_dictionary):
        print("{}: {}".format(i, j))
