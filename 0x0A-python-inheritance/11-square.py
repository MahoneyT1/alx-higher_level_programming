#!/usr/bin/python3

"""A class the rep ogbonna"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """representation of class"""
    def __init__(self, size):
        """ initializing obj.

        Args:
            size (int): checkes if
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Method that cal for area"""

        return self.__size * self.__size
