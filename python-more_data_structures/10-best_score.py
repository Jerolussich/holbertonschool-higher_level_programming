#!/usr/bin/python3


def best_score(a_dictionary):
    """returns a key with the biggest integer value"""
    biggest_number = 0
    biggest_key = ""

    if a_dictionary is None:
        return (None)
    for key in a_dictionary:
        if a_dictionary[key] > biggest_number:
            biggest_number = a_dictionary[key]
            biggest_key = key
    return (biggest_key)
