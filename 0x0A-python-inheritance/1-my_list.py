#!/usr/bin/python3
""" A class that inherit from list """


class MyList(list):
    """ Representation of my iheritted class"""
    pass

    def print_sorted(self):
        """A method that prints a list in ascending order """
        print(sorted(self))
