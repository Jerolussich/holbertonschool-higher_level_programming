#!/usr/bin/python3
"""shebang"""


class Square:
    """square class"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize class"""
        self.__size = size
        if type(position[0]) is not int and type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (len(position)) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if value[0] is not int and value[1] is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (len(value)) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = value

    def area(self):
        """return square area"""
        return self.__size ** 2

    def my_print(self):
        """print square"""
        if self.__size == 0:
            print("")
            return

        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print("")

        for row in range(self.__size):

            if self.__position[1] <= self.__position[0]:
                for i in range(self.__position[0]):
                    print(" ", end="")

            for i in range(self.__size):
                print("#", end="")
            print("")
