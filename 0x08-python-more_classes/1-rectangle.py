#!/usr/bin/python3

"""class Rectangle that defines a rectangle by: (based on 0-rectangle.py"""


class Rectangle:
    """Class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Class instance"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width property"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """class property"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
