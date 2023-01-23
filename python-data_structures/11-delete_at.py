#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    """delete list at index"""
    list_size = len(my_list)

    if idx >= list_size or idx < 0 or list_size == 0:
        return (my_list)
    del my_list[idx]
    return (my_list)
