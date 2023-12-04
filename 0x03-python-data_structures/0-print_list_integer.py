#!/usr/bin/python3

def print_list_integer(my_list=[]):
    newList = []

    for i in range(0, len(my_list)):
        newList.append(my_list[i])

    for i in range(len(newList)):
        print("{}".format(newList[i]))
