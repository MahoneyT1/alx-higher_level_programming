#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    newList = my_list
    lent_of_list = len(newList) - 1

    # check if idx is negative and return curent-list

    if idx < 0:
        return my_list

    elif idx > lent_of_list:
        return my_list

    else:
        # now replace the value at the index of idx

        for i in range(len(newList)):
            if i == idx:
                newList[i] = element

        return newList
