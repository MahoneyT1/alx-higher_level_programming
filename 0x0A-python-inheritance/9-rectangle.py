#!/usr/bin/python3
"""A class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representation of both Rectangle and BaseGeometry"""

    def __init__(self, width, height):
        """Initilization of obj with attributes.

        Args:
            width (int): param 1
            height (int): param 2
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method that cal the Area of a rectangle"""

        return self.__width * self.__height

    def __str__(self):
        mystring + "[" + str(self.__class__.__name__) + "] "
        mystring += str(self.__width) + "/" + str(self.__height)
        return mystring
