#!/usr/bin/python3

def element_at(my_list, idx):
    current_list = []
    n = idx
    lent_of_my_list = len(my_list) - 1

    if idx < 0:
        return None

    elif idx > lent_of_my_list:
        return None

    else:
        for i in range(len(my_list)):
            current_list.append(my_list[i])

        for i in range(len(current_list)):
            if i == n:
                return (current_list[i])
