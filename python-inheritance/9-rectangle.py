#!/usr/bin/python3
"""shebang"""


class BaseGeometry:
    """BaseGeometry"""

    def area(self):
        """returns area"""
        return (self.__width__ * self.__height__)

    def integer_validator(self, name, value):
        """integer validator given"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """rectangle"""

    def __init__(self, width, height):
        """initialize class"""
        self.__width__ = width
        self.__height__ = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def __str__(self):
        """print string representation"""
        return f"[rectangle] {self.__width__}/{self.__height__}"
