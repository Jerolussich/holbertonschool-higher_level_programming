#!/usr/bin/puthon3


def multiply_list_map(my_list=[], number=0):
    """returns a list with all values multiplied by a number"""
    new_list = list(map(lambda item: item * number, my_list))
    return (new_list)
