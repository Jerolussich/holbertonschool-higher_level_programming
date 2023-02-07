#!/usr/bin/python3
"""shebang"""


def read_file(filename=""):
    """Reads file"""
    with open(filename, 'r') as fin:
        print(fin.read())
