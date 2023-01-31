#!/bin/usr/python3

def print_square(size):

    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size == 0:
        return
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
