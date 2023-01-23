#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """print sorted dict"""
    list_sorted = []

    sorted_dict = dict(sorted(a_dictionary.items(), key=lambda item: item[0]))

    for key, value in sorted_dict.items():
        print("{}: {}".format(key, value))
