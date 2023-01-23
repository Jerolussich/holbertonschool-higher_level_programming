#!/usr/bin/python3


def uniq_add(my_list=[]):
    """add numbers once"""
    used_numbers = []
    sum = 0

    for item in my_list:
        if item not in used_numbers:
            used_numbers.append(item)
            sum += item
    return (sum)
