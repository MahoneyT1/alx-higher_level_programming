#!/usr/bin/python3

""" define a class"""


class Square:
    """ represent a square """
    def __init__(self, size=0):
        """ initailizing new object with instances.

        args:
            size (int): size of a new Square.
        """

        self.__size = size

        try:
            if not isinstance(self.__size, int):
                raise TypeError("size must be an integer")

            if size < 0:
                raise ValueError
        except ValueError:
            raise ValueError("size must be >= 0")
