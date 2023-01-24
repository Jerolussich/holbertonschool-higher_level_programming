#!/usr/bin/python3


def safe_print_division(a, b):
    """safe print division"""
    c = 0

    try:
        c = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(c))
        return (c)
