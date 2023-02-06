#!/usr/bin/python3
"""shebang"""


def inherits_from(obj, a_class):
    """check if obj inherits"""
    if type(obj) is not a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
