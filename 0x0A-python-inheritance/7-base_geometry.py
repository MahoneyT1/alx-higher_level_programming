#!/usr/bin/python3
"""create a class baseGeometry"""


class BaseGeometry:
    """class geometry obj
    """
    def area(self):
        """not implemented yet

        Raises:
            Exception: area not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates value

        Args:
            name (string): name is always a string - param 1
            value (int): to be checked - param 2

        Raise:
            Exceptions: if value is not integer
            Exceptions: if is less or qual 0
        """

        if type(value)!= int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
