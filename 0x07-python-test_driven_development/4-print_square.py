#!/usr/bin/python3

from lib2to3.pgen2.token import LESS


def print_square(size):
    """ Function that prints a square.
    Args:
    size (int): size of square
    """
    if type(size) is str:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) is not int or size != size:
        raise TypeError("size must be an integer")

    if size > 0:
        for row in range(size):
            for column in range(size):
                print("#", end="")
            print()
