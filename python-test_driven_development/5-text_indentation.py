#!/usr/bin/python3
"""shebang"""


def text_indentation(text):
    """indents text with certain chars"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in text:
        if char in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            raise TypeError("text must be a string")

        if char == " " and stat == 1:
            continue
        elif char.isupper() is True:
            print(char, end="")
            stat = 0
        else:
            print(char, end="")

        if char == "." or char == "," or char == "?" or char == ":":
            print("\n")
            stat = 1
    return ""
