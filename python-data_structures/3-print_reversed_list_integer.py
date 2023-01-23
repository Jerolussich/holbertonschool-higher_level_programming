#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """print reversed list integer"""

    if my_list is None:
        return

    size = len(my_list) - 1

    for number in my_list:
        print("{:d}".format(my_list[size]))
        size -= 1
