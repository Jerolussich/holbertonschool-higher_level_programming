#!/usr/bin/python3
"""shebang"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square"""

    def __init__(self, size):
        """function to initialize square and rectangle"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns area"""
        return self.__size * self.__size

    def __str__(self):
        """returns in string format the atributes"""
        return f"[Square] {self.__width__}/{self.__height__}"
