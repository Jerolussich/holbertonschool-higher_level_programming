#!/usr/bin/python3
"""shebang"""


class Square:
    """square"""

    def __init__(self, size=0):
        """initliaze class"""
        self.__size = size

    @property
    def size(self):
        """return area"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns areas"""
        return self.__size ** 2
