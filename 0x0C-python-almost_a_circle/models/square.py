#!/usr/bin/python3

"""Module for a sqaure class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A class named Square
    Attributes:
    attr1(id): id of object
    attr2(width): square width
    attr3(height): square height
    attr4(x): number of spaces before square
    attr5(y): number of spaces before square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes instance of Square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string representation of Square class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Returns the size of the object"""
        return self.width

    @size.setter
    def size(self, value):
        """Returns the size of the object"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes"""
        if len(args) == 0:
            for key in kwargs:
                setattr(self, key, kwargs[key])

        else:
            tupla = [
                "id",
                "size",
                "x",
                "y"
            ]
            for i in range(len(args)):
                setattr(self, tupla[i], args[i])

    def to_dictionary(self):
        """return format of dictionary"""
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
