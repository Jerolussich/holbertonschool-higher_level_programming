#!/usr/bin/python3
"""shebang"""


def add_integer(a, b=98):
    """add integer safely"""
    if type(a) is not int and type(a) is not float or if a is None:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    c = a + b
    return (c)
