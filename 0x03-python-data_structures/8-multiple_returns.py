#!/usr/bin/python3

def multiple_returns(sentence):
    """ A function that returns both lengeth of a string and the first char """

    length_of_string = len(sentence)

    if length_of_string <= 0:
        first_char = None
        return first

    else:
        # use a for loop to check the first char of the string

        for first in sentence:
            if first > 0:
                first_char = sentence[0]
                return (length_of_string, first_char)
