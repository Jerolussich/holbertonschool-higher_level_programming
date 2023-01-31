#!/usr/bin/python3
"""shebang"""


class Rectangle:
    """class rectangle"""

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
            raise ValueError("heightmust be >= 0")
        self.__height = value

    def area(self):
        """returns area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """returns perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (self.__height * 2 + self.__width * 2)

    def __str__(self):
        """returns string format object"""

        string = ""

        if (self.__height == 0 or self.__width == 0):
            print("")
        for i in range(self.__height):
            for j in range(self.__width):
                string += "#"
            if (i != self.__height - 1):
                string += "\n"
        return (string)
