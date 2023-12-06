#!/usr/bin/python3

def multiple_returns(sentence):
    """ A function that returns both lengeth of a string and the first char """

    if not sentence:
        sentence = None
        return sentence

    if sentence:
        length = len(sentence)

    else:
        length = 0

    return(length, sentence if not sentence else sentence[0])
