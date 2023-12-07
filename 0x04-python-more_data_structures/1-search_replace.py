#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []

    for elem in my_list.copy():
        if elem == search:
            elem = replace
            new_list.append(elem)

        else:
            new_list.append(elem)

    return new_list
