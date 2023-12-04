#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    nL = []

    for i in range(len(my_list)):
        nL.append(my_list[i])

    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list

    else:
        for i in range(len(my_list)):
            if i == idx:
                nL[i] = element
        return nL
