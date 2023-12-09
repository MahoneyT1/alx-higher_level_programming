#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:

        for v in max(a_dictionary.items()):
            return v

    else:
        return None
