#!/usr/bin/python3

""" a class Square that defines a square """


class Square:
    def __init__(self, size=0):
        """ privating he variable size """

        self.__size = size

        try:
            if not isinstance(self.__size, int):
                raise TypeError("size must be an integer")

            if size < 0:
                raise ValueError
        except ValueError:
            raise ValueError("size must be >= 0")
