#!/usr/bin/python3
"""shebang"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """returns exception"""
        raise Exception("area is not implemented")

    def integer_validator(self, name, value):
        """checks value given"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class Rectangle"""

    def __init__(self, width, height):
        """initialices class"""
        self.__width__ = width
        self.__height__ = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
