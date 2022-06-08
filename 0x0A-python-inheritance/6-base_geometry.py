#!/usr/bin/python3
"""Module to create a class named BaseGeometry"""


class BaseGeometry():
    """An class named BaseGeometry
    Attributes:
    attr1(area): Raises an exception
    """

    def area(self):
        raise Exception("area() is not implemented")
