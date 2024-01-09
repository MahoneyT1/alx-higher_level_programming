#!/usr/bin/python3
""" write a classs that inherit from parent class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ representation of Rectangle"""

    def __init__(self, width, height):
        """ initialization of obj.
        Args:
            width(int): param 1
            height(int): param 2
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
