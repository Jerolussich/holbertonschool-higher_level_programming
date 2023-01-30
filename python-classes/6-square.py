#!/usr/bin/python3
"""shebang"""


class Square:
    """square class"""

    def __init__(self, _size=0, _position=(0, 0)):
        """initialize class"""
        self._size = _size
        self._position = _position

    @property
    def size(self):
        return self._size

    @property
    def position(self):
        return self._position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @position.setter
    def position(self, value):
        if value[0] is not int and value[1] is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (len(value)) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self._size = value

    def area(self):
        """return square area"""
        return self._size ** 2

    def my_print(self):
        """print square"""
        if self._size == 0:
            print("")
            return

        if self._position[1] > 0:
            for i in range(self._position[1]):
                print("")

        for row in range(self._size):

            if self._position[1] <= self._position[0]:
                for i in range(self._position[0]):
                    print("_", end="")

            for i in range(self._size):
                print("#", end="")
            print("")
