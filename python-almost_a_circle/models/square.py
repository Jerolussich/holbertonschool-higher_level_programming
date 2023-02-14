#!/usr/bin/python3
"""square.py"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializer for square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """print string attributes"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """"size setter"""
        super().validator("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update attributes"""

        counter = -1
        size = len(args)

        if size != 0:
            if size > 0:
                self.id = args[0]

            if size > 1:
                self.width = args[1]

            if size > 2:
                self.x = args[2]

            if size > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                counter += 1
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        d = {}
        d['id'] = self.id
        d['x'] = self.x
        d['size'] = self.size
        d['y'] = self.y
        return d
