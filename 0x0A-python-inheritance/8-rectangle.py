#!/usr/bin/python3
"""Module to create an empty class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """An class named BaseGeometry
    Attributes:
    attr1(width): Width of rectangle
    attr2(height): height of rectangle
    """

    def __init__(self, width, height):
        """initializes an instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
