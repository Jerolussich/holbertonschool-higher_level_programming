#!/usr/bin/python3
"""shebang"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """initliazes class"""
        self.__width__ = width
        self.__height__ = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def __str__(self):
        """prints string representation"""
        return f"[rectangle]<{self.__width__}>/<{self.__height__}>"
