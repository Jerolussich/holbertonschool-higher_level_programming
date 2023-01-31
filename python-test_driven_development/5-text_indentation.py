#!/bin/usr/python3
"""shebang"""


def text_indentation(text):
    """indents text with certain chars"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in text:
        print(char, end="")
        if char == "." or char == "," or char == "?":
            print("\n")
