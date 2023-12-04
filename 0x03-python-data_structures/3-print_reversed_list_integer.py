#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    newList = []
    newList = my_list

    i = len(my_list) - 1

    while i >= 0:
        print("{:d}".format(newList[i]))
        i -= 1
