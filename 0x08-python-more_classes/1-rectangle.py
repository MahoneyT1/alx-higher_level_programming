#!/usr/bin/python3
"""

definning a class rectangle.

"""

class Rectangle:
    """ representation of the class rectangle """

    def __init__(self, width=0, height=0):
        """ 
        initializing new obj.

        args:
            width (int): parameter 1
            height (int): parameter 2

        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ func that gets or returns width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ func that sets or modify width """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ func that gets or return height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ func that sets or modify height """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
