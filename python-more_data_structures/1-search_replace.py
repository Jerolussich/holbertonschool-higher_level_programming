#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """search value and replace"""
    new_list = my_list[:]
    counter = 0

    for item in new_list:
        if item == search:
            new_list[counter] = replace
        counter += 1
    return (new_list)
