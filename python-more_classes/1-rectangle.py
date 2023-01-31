#!/usr/bin/python3
"""shebang"""


class Rectangle:
    """rectangle class"""

    def __init__(self, _width=0, _height=0):
        """initializes"""
        self.__dict__ = {}
        self._height = _height
        self._width = _width

    @property
    def width(self):
        return (self._width)

    @property
    def height(self):
        return (self._height)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("heightmust be >= 0")
        self._height = value
