#!/usr/bin/python3
"""shebang"""


def write_file(filename="", text=""):
    """truncates file or creates and writes"""
    with open(filename, "w+") as fin:
        fin.write(text)
        fin.close()
    return len(text)
