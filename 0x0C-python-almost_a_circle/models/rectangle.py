#!/usr/bin/python3

"""module for rectangle class"""
from models.base import Base


class Rectangle(Base):
    """A class named Rectangle
    Attributes:
    attr1(id): id of object
    attr2(width): rectangle width
    attr3(height): rectangle height
    attr4(x): number of spaces before rectangle
    attr5(y): number of newlines before rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instance of Rectangle class"""
        self.staticfunc(width, "width")
        self.staticfunc(height, "height")
        self.staticfunc(x, "x")
        self.staticfunc(y, "y")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @staticmethod
    def staticfunc(value, name_met):
        """staticfunc to manage the errors"""
        if type(value) is not int:
            raise TypeError(f"{name_met} must be an integer")
        if value <= 0 and name_met in ("width", "height"):
            raise ValueError(f"{name_met} must be > 0")
        if value < 0 and name_met in ("x", "y"):
            raise ValueError(f"{name_met} must be >= 0")

    def area(self):
        """Returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the instance with the character #"""
        if self.__y > 0:
            for i in range(self.__y):
                print()

        for row in range(self.__height):
            if self.__x > 0:
                print(" " * self.__x, end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns a string representation of a Rectangle"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y}\
 - {self.__width}/{self.__height}")

    @property
    def width(self):
        """Returns width of instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width of class instance"""
        self.staticfunc(value, "width")
        self.__width = value

    @property
    def height(self):
        """Returns height of instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height of class instance"""
        self.staticfunc(value, "height")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        """Returns x of instance"""
        self.staticfunc(value, "x")
        self.__x = value

    @property
    def y(self):
        """Returns y of instance"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y of class instance"""
        self.staticfunc(value, "y")
        self.__y = value

    def update(self, *args, **kwargs):
        """Updates attributes"""
        if len(args) == 0:
            for key in kwargs:
                setattr(self, key, kwargs[key])

        else:
            tupla = [
                "id",
                "width",
                "height",
                "x",
                "y"
            ]
            for i in range(len(args)):
                setattr(self, tupla[i], args[i])

    def to_dictionary(self):
        """return a dictionary"""
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
