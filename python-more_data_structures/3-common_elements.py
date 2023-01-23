#!/usr/bin/python3


def common_elements(set_1, set_2):
    """ returns a set of common elements in two sets"""
    new_set = []

    for item_1 in set_1:
        for item_2 in set_2:
            if item_2 in set_1 and item_2 not in new_set:
                new_set.append(item_2)

    return (new_set)
