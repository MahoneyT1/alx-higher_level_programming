#!/usr/bin/python3
""" write a function thatreads froma file """


def read_file(filename=""):
    """ Function that opens a file in a read mode,
    prints to stdout.

    Args:
        filename(text-file): file to read from as param 1.
    """

    with open(filename, mode='r', encoding='utf-8') as doc:
        print(doc.read())
