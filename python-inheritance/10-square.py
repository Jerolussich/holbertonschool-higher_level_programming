#!/usr/bin/python3
"""shebang"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """returns area"""
        return (self.__width__ * self.__height__)

    def integer_validator(self, name, value):
        """validates input given"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class Rectangle"""

    def __init__(self, width, height):
        """Function to initilize rectangle"""
        super().integer_validator("width", width)
        self.__width__ = width
        super().integer_validator("height", height)
        self.__height__ = height

    def area(self):
        """returns area"""
        return self.__width__ * self.__height__

    def __str__(self):
        """returns atributes in string format"""
        return f"[rectangle]<{self.__width__}>/<{self.__height__}>"


class Square(Rectangle):
    """class Square"""

    def __init__(self, size):
        """function to initialize square and rectangle"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns area"""
        return self.__size * self.__size
