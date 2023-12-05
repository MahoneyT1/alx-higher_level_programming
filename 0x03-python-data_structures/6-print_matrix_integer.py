#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    # Loop through the first list
    for row in matrix:

        # Loop through row in matrix:

        for elem in row:
            print("{:d}".format(elem), end=' ')

        # Print space each time it loops

        print()
