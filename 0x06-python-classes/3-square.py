#!/usr/bin/python3

""" declare a class Square """


class Square:
    """ represent a square """

    def __init__(self, size=0):
        """ initilizing of obj of a new instance.

        args:
            size (int): size of a square.
        """
        self.__size = size

        try:
            if not isinstance(self.__size, int):
                raise TypeError("size must be an integer")

            if size < 0:
                raise ValueError

        except ValueError:
            raise ValueError("size must be >= 0")

    def area(self):
        self.area = self.__size * self.__size
        return self.area
