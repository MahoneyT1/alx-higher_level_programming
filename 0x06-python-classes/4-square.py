#!/usr/bin/python3
""" declare square cls"""


class Square:
    """ represent the class"""

    def __init__(self, size=0):
        """ initialize obj of instance.

        args:
            size (int): size of sqaure.

        """

        self.__size = size

    @property
    def size(self):
        """ getter function to get __size """
        return self.__size

    @size.setter
    def size(self, value):
        """ method to modify __self """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """ method that cal square """
        return self.__size * self.__size
