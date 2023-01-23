#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """divide list ints by 2"""
    new_list = []
    i = 0

    for item in my_list:
        if item % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
        i += 1
    return (new_list)
