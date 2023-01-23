#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """multiply dict values by 2"""
    new_dictionary = a_dictionary.copy()

    for key, value in new_dictionary.items():
        new_dictionary[key] = value * 2
    return (new_dictionary)
