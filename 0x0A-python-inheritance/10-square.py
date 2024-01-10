#!/usr/bin/python3
"""A class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """representation of square and Rectangle"""

    def __init__(self, size):
        """ initializing obj with attributes.

        Args:
            size (int): para1 size of square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Method that returns area of a square"""
        return self.__size * self.__size
