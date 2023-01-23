#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """print square matrix"""
    new_matrix = []

    for row in matrix:
        sub_list = []
        for item in row:
            sub_list.append((item ** 2))
        new_matrix.append((sub_list))
    return (new_matrix)
