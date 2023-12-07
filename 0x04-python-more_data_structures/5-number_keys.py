#!/usr/bin/python3

def number_keys(a_dictionary):
    """ A function that returns the number of keys in a dictionary """
    num_of_keys = 0

    for i in a_dictionary.keys():
        num_of_keys += 1

    return num_of_keys
