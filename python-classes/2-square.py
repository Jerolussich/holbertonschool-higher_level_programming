#!/usr/bin/python3


class Square:
    def __init__(self, _size=0):
        """initliaze class"""
        if not isinstance(_size, int):
            raise TypeError("size must be an integer")
        else:
            if _size < 0:
                raise ValueError("size must be >= 0")
            self._size = _size
