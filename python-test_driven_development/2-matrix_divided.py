#!/usr/bin/python3
"""shebang"""


def matrix_divided(matrix, div):
    """divide safely"""
    row = len(matrix)
    row_size = len(matrix[0])
    new_matrix = [[0 for col in range(row_size)] for row in range(row)]

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(row):
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    for index, item in enumerate(matrix):
        for index2, sub_item in enumerate(item):
            if type(sub_item) is not int and type(sub_item) is not float:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")

            new_matrix[index][index2] = round((sub_item / div), 2)
    return (new_matrix)
