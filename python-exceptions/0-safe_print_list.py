#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """print list safely"""
    i = 0
    number_printed = 0

    for item in my_list:
        if i < x:
            try:
                print(item, end="")
                number_printed += 1
            except IndexError:
                pass
            i += 1
    print("")
    return (number_printed)
