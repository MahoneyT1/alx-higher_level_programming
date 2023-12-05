#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    if not matrix:
        print()

    else:
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                print("{}".format(matrix[row][col]), end=" "\
                        if col != len(matrix[row]) - 1 \
                        else "\n")
        print()
