#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    """delete key and value"""
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
