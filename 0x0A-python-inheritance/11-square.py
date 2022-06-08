#!/usr/bin/python3

"""This module creates a named square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """An class named BaseGeometry
    Attributes:
    attr1(area): Raises an exception
    """

    def __init__(self, size):
        """Initializes an instance"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return a string for the area"""
        return f"[Square] {self.__size}/{self.__size}"
