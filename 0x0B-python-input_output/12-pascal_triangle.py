#!/usr/bin/python3
""" Pascal’s triangle """


def pascal_triangle(n):
    """ A function that returns a list of lists of integers,
    representing the Pascal’s triangle of n.

    Args:
        n (int): param 1

    Return:
        a list of lists of integers.
    """

    if n < 0:
        return []
    else:
        new_tri = []
        for i in range(n):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = new_tri[i - 1][i - j] + new_tri[i - 1][j]
            new_tri.append(row)
        return new_tri
