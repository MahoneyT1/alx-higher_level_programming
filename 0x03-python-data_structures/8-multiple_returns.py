#!/usr/bin/python3

def multiple_returns(sentence):
    """ A function that returns both lengeth of a string and the first char """
    
    if not sentence:
        return None

    else:
        length_of_string = len(sentence)

        # use a for loop to check the first char of the string

        for first in sentence:
            if first == sentence[0]:
                return (length_of_string, first)