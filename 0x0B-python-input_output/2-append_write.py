#!/usr/bin/python3
""" An append to a file function """


def append_write(filename="", text=""):
    """ function that appends at the end of a file.

    Args:
        filename(Text-file): file to append to.
        text(string): string to append.
    """

    with open(filename, mode="a", encoding="utf-8") as doc2:
        return doc2.write(text)
