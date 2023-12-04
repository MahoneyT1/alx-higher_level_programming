#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    rl = []
    lent = len(my_list)

    for i in range(lent - 1, -1, -1):
        rl.append(my_list[i])

    for i in rl:
        print("{:d}".format(i))
