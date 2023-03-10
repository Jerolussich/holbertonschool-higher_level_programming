#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """print matrix integers"""
    column_idx = 0
    row_idx = 0
    size_row = len(matrix) - 1
    size_column = len(matrix[0]) - 1

    if size_row == -1 or size_column == -1:
        print("")
        return
    while row_idx <= size_row:
        while column_idx <= size_column:
            if column_idx != size_column:
                print("{:d} ".format(matrix[row_idx][column_idx]), end="")
            else:
                print("{:d}".format(matrix[row_idx][column_idx]), end="\n")
            column_idx += 1
        column_idx = 0
        row_idx += 1
