#!/usr/bin/python3
""" A function that writes to a file """


def write_file(filename="", text=""):
    """ That writes to a Text-file.

    Args:
        filename(Text-file): file to write to.
        text(string); string to write.
    """
    with open(filename, mode='w', encoding="utf-8") as doc1:
        return doc1.write(text)
