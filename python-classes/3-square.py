#!/usr/bin/python3
"""shebang"""


class Square:
    """square class"""

    def __init__(self, size=0):
        """initialize class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size

    def area(self):
        """define area"""
        return (self.__size * self.__size)
