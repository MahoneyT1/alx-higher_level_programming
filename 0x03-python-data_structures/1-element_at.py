#!/usr/bin/python3

def element_at(my_list, idx):
    current_list = []

    for i in range(len(my_list)):
        current_list.append(my_list[i])

    for n in current_list:
        if current_list[n] == current_list[idx]:
            return current_list[n]
