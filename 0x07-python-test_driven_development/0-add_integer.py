#!/usr/bin/python3

"""This module has a fuction to add two integers"""


def add_integer(a, b=98):
    """ Function that adds two string.
    Args:
        a (int): First addend.
        b (int): Second addend, set to zero.
    Returns:
        int: The return value. The sum
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if a is None:
        raise TypeError("a must be an integer")
    if type(a) and type(b) is int or type(a) and\
            type(b) is float and type(b) is not float('nan'):
        return int(a) + int(b)
    return 0
