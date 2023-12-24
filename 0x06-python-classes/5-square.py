#!/usr/bin/python3

""" define a type class square """


class Square:
    """ representing the class square """

    def __init__(self, size=0):
        """ initializing a new obj with content of instance.

        args:
            size (int): size of square.
        """
        self.__size = size

    @property
    def size(self):
        """ get function """

        return self.__size

    @size.setter
    def size(self, value):
        """  value : value to update the private attribute """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """ function that cal area of a square """

        return self.__size * self.__size

    def my_print(self):
        """ function that prints square in char form """

        for i in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")

        if self.__size == 0:
            print("")
