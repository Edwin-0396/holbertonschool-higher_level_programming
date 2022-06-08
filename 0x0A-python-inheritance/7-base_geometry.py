#!/usr/bin/python3
"""Module to create an empty class"""


class BaseGeometry():
    """An class named BaseGeometry
    Attributes:
    attr1(area): Raises an exception
    """

    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates input"""
        if not isinstance(value, int):
            raise TypeError(f"{value} must be an integer")

        if value <= 0:
            raise ValueError(f"{value} must be greater than 0")
