#!/usr/bin/python3
""" create a class of called base classs """


class Base:
    """ Representation of the Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initialises new object with attributes.
        Args:
            id (int): param 1. check if it None,
            if yes assign it to the attribute.
        """

        if not id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ method that returns the JSON string representation,
        of list_dictionaries.
        Args:
            list_dictionaries(list): converts it to json
        Returns: a json representation of a list.
        """

        if list_dictionaries is None or list_dictionaries == []:
            return []

        else:
            hold = json.dumps(list_dictionaries)
            return hold
