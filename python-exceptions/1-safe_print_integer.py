#!/usr/bin/bash


def safe_print_integer(value):
    """safe print integer"""
    try:
        print("{:d}".format(value))
        return (True)
    except Exception:
        return (False)
