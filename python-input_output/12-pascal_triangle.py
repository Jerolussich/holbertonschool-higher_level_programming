#!/usr/bin/python3
"""shebang"""


def pascal_triangle(n):
    """create pascal triangle"""

    list = [[0 for _ in range(-1, i)] for i in range(n)]
    new_list = list[:]

    for count in range(n):

        new_list[count][0] += 1

        for index, item in enumerate(list[count]):
            if count == 2 and index >= 1 and len(new_list[count]) - 1 != index:
                new_list[count][index] += new_list[count -
                                                   1][index - 1] + new_list[count - 1][index - 1]
            elif count >= 2 and index >= 1 and len(new_list[count]) - 1 == index:
                new_list[count][index] += 1
            elif count > 2 and index >= 1 and len(new_list[count]) - 1 != index:
                new_list[count][index] += new_list[count -
                                                   1][index] + new_list[count - 1][index - 1]

        if count == 1:
            new_list[count][1] += 1

        list = new_list[:]

    return new_list
