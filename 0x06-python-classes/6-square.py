#!/usr/bin/python3
""" delare a class type square """


class Square:
    """ blue_print of type square """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ function that gets the atttribut size """
        return self.__size

    @property
    def position(self, value):
        """ function that gets the attri of position """
        return self.__position

    @size.setter
    def size(self, value):
        """ setter that sets value is > 0 """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """ sets the value if it is tuple and int """

        if not isinstance(value, tuple) and len(value) == 2 and\
                all(isinstance(item, int) for item in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ returns size of a square """
        return self.__size * self.__size

    def my_print(self):
        """ func that prints # at the index of position """

        if self.__size == 0:
            print("")

        [print("", end="") for i in range(self.__position[1])]

        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for j in range(self.__size)]
            print("")
