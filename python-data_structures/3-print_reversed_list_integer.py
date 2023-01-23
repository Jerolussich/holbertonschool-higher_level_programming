#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """print reversed list integer"""
    size = len(my_list) - 1

    if my_list == -1:
        return
    for number in my_list:
        print("{:d}".format(my_list[size]))
        size -= 1
