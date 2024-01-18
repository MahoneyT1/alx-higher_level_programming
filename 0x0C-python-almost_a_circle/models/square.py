#!/usr/bin/python3
""" define a class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """representation of square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialization of new objects with attributes

        Args:
            size (int): size of square, param 1
            x (int, optional): param 2, Defaults to 0.
            y (int, optional): param 3, Defaults to 0.
            id (int, optional): param 4. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter method

        Returns:
            int: returns width
        """
        return self.width

    @size.setter
    def size(self, new_size):
        """setter method

        Args:
            new_size (int): sets new values
        """
        self.width = new_size
        self.height = new_size

    def __str__(self):
        """string representation of a class

        Returns:
            str: dict of all instances
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.size)

    def update(self, *args, **kwargs):
        """methods to update attribtues.
        args:
            *args:int: parameter to collect any input
            **kwargs:int: collecting data that has key/pair values.
        """
        if args and len(args) != 0:
            count = 0
            for arg in args:
                if count == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.size = arg

                elif count == 2:
                    self.x = arg

                elif count == 3:
                    self.y = arg

                count += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v

                elif k == "size":
                    self.size = v

                elif k == "x":
                    self.x = v

                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """method that converts strings to dictionary

        Returns:
            dict representation of class
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
