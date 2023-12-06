#!/usr/bin/python3

def multiple_returns(sentence):
    """ A function that returns both lengeth of a string and the first char """

    if not sentence:
        sentence = None
        return sentence

    if sentence:
        length = len(sentence)

        # use a for loop to check the first char of the string

        for first in sentence:
            first_char = sentence[0]
            return (length, first_char)
