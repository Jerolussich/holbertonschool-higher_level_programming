#!/usr/bin/python3
"""rectangle.py"""

from models.base import Base


class Rectangle(Base):
    """class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize rectangle"""

        super().__init__(id)
        self.validator("width", width)
        self.__width = width
        self.validator("height", height)
        self.__height = height
        self.validator("x", x)
        self.__x = x
        self.validator("y", y)
        self.__y = y

    @property
    def width(self):
        """get width"""
        return self.__width

    @property
    def height(self):
        """get height"""
        return self.__height

    @property
    def x(self):
        """get x"""
        return self.__x

    @property
    def y(self):
        """get y"""
        return self.__y

    @width.setter
    def width(self, value):
        """set width"""
        self.validator("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        """set height"""
        self.validator("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        """set x"""
        self.validator("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        """set y"""
        self.validator("y", value)
        self.__y = value

    def validator(self, name="", value=0):
        """validates inputs given"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if name == "width" and value <= 0 or name == "height" and value <= 0:
            raise ValueError(f"{name} must be > 0")
        if name == "x" and value < 0 or name == "y" and value < 0:
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        """get area of rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """prints rectangle in stdout"""
        for counter in range(self.__y):
            print("")

        for counter in range(self.height):
            for counter in range(self.x):
                print(" ", end="")
            for counter in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """print string attributes"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.y} -\
{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """update attributes"""
        counter = -1
        size = len(args)

        if size != 0:
            if size > 0:
                self.id = args[0]

            if size > 1:
                self.height = args[1]

            if size > 2:
                self.width = args[2]

            if size > 3:
                self.x = args[3]

            if size > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                counter += 1
                setattr(self, key, value)

    def to_dictionary(self):
        """returns a dict"""
        d = {}
        d['id'] = self.id
        d['width'] = self.width
        d['height'] = self.height
        d['x'] = self.x
        d['y'] = self.y
        return d
