#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Function that setts or modify height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Function that returns area of rectangle."""
        sum = self.__height * self.__width
        return sum

    def perimeter(self):
        """Function that returns perimeter of a rectangle."""
        if self.__width and self.__height == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__height + self.__width)
            return perimeter

    def __str__(self)-> str:
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__height == 0 or self.__width == 0:
            return('')

        new_list = []
        for i in range(self.__height):
            [new_list.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                new_list.append('\n')

        return( ''.join(new_list))
