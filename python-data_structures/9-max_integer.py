#!/usr/bin/python3

def max_integer(my_list=[]):
    """find biggest int"""
    number = 0

    for item in my_list:
        if number < item:
            number = item
    return (number)
