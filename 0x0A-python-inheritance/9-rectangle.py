#!/usr/bin/python3

"""Module to create an empty class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns area of instance"""
        return self.__width * self.__height

    def __str__(self):
        """return area representation"""
        return f"[Rectangle] {self.__width}/{self.__height}"
