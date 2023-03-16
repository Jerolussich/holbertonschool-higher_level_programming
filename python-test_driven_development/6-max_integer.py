#!/usr/bin/python3

def max_integer(list=[]):

    if len(list) == 0:
        return None

    for index, item in enumerate(list):
        if type(item) is not int:
            raise TypeError("List contains non int values")
        if index == 0:
            number = item
        if (item > number):
            number = item

    print(number)
    return (number)
