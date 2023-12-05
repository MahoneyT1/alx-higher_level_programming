#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    # Loop through the first list
    if not matrix:
        print()

    else:
        for i in range(len(matrix)):
            for j in range(0, len(matrix[i])):
                print("{}".format(matrix[i][j]), end=" " if j != len(matrix[i]) -1 else"")
            print()
