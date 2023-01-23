#!/usr/bin/python3


def no_c(my_string):
    """remove all c chars"""
    idx = 0
    new_string = ""

    for letter in my_string:
        if letter == 'c' or letter == "C":
            continue
        new_string += letter
    return (new_string)
