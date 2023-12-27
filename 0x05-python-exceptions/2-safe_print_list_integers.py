#!/usr/bin/python3



def safe_print_list_integers(my_list=[], x=0):
    """ a function that prints x integers."""

    count = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                count += 1
                print("{:d}".format(my_list[i]), end="")

            else:
                continue

        except IndexError:
            raise Exception("Index Error")
    print()
    return count
