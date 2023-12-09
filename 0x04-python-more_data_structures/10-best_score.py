#!/usr/bin/python3

def best_score(a_dictionary):
    """ A function that returns a key with the biggest integer value """

    if a_dictionary:
        get_max = max(a_dictionary, key=a_dictionary.get)
        return get_max

    else:
        return None
