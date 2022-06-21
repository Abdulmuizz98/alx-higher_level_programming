#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers. """
    for i in matrix:
        num = 0
        lim = len(i) - 1
        while num <= lim:
            print("{:d}".format(i[num]), end=" " if (num != lim) else "")
            num += 1
        print("")
