#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_list = []

    for row in matrix.copy():
        new_row = []

        for col in row.copy():
            new_row.append(col ** 2)
        new_list.append(new_row)

    return new_list
