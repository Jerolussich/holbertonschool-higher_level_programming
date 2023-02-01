#!/bin/usr/python3
"""shebang"""


class Rectangle:
    """rectangle class"""
    number_of_instances = 0

    def __init__(self, __width=0, __height=0):
        """initializes"""
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
        Rectangle.number_of_instances += 1

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
        """return area of object"""
        return (self.__height * self.__width)

    def perimeter(self):
        """return perimeter of object"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (self.__height * 2 + self.__width * 2)

    def __str__(self):
        """define string representation object"""
        string = ""
        if (self.__height == 0 or self.__width == 0):
            print("")
        for i in range(self.__height):
            for j in range(self.__width):
                string += "#"
            if (i != self.__height - 1):
                string += "\n"
        return (string)

    def __repr__(self):
        """return object atribute representation"""
        return (f"Rectangle({self.__width}, {self.__height}, {self.number_of_instances})")

    def __del__(self):
        """"delete object"""
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        print("Bye rectangle...")
