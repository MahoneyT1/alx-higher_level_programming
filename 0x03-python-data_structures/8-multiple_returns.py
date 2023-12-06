#!/usr/bin/python3

def multiple_returns(sentence):
    """ A function that returns both lengeth of a string and the first char """

    length = len(sentence)

    if length <= 0:
        first_char == 0
        return first_char

    else:
        # use a for loop to check the first char of the string

        for first in sentence:
            first_char = sentence[0]
            return (length, first_char)
