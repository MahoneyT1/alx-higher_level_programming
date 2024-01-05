#!/usr/bin/python3
""" definning a class rectangle """


class Rectangle:
    """ representation of the class rectangle """
    def __init__(self, width=0, height=0):
        """
        initializing new obj.
        args:
        width (int): parameter 1.
        height (int): parameter 2.

        Raise Exception:
                    if ValueError or TypeError.
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """ func that gets or returns width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ func that sets or modify width """

        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("must be >= 0")
        else:
            raise ValueError("width must be an integer")

    @property
    def height(self):
        """ func that gets or returns height attribute """
        return self.__width

    @height.setter
    def height(self, value):
        """ func that sets or modify height """

        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("message width must be an integer")
