#!/usr/bin/python3
"""Write a class Student that defines a student"""


class Student:
    """ representation of student class."""
    def __init__(self, first_name, last_name, age):
        """ initialization of new objs.

        Args:
            first_name(string): param 1
            last_name(string): param 2
            age(int):param 3
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
