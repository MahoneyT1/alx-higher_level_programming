#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """ Function that prints array of int backwards """
    newList = []
    newList = my_list

    lent_of_list = len(newList) - 1

    for i in range(lent_of_list + 1, 0, - 1):
        print("{}".format(i))