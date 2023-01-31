#!/usr/bin/python3
"""shebang"""


class Rectangle:
    """rectangle class"""

    def __init__(self, __width=0, __height=0):
        """initializes"""
        self.__dict__ = {}
        if type(__height) is not int:
            raise TypeError("height must be an integer")
        if __height < 0:
            raise ValueError("height must be >= 0")
        self.__height = __height
        if type(__width) is not int:
            raise TypeError("width must be an integer")
        if __width < 0:
            raise ValueError("width must be >= 0")
        self.__width = __width

    @property
    def width(self):
        return (self.__width)

    @property
    def height(self):
        return (self.__height)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
