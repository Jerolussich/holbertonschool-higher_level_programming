#!/usr/bin/python3

def append_write(filename="", text=""):
    """function that appends"""
    with open(filename, "a+") as fin:
        fin.write(text)
        fin.close()
    return len(text)
