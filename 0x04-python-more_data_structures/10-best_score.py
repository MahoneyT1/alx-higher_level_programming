#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        for k in a_dictionary.keys():
            if k:
                for k, v in max(a_dictionary.items()):
                    return v
            else:
                return None

    else:
        return None
