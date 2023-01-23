#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """adds tuple ints"""
    size_a = len(tuple_a) - 1
    size_b = len(tuple_b) - 1

    a1 = tuple_a[0] if size_a != - 1 else 0
    a2 = tuple_a[1] if size_a == 1 else 0
    b1 = tuple_b[0] if size_b != - 1 else 0
    b2 = tuple_b[1] if size_b == 1 else 0
    return (a1 + b1, a2 + b2)
