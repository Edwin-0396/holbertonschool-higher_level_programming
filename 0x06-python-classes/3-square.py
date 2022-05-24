#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Represents a square
    Attributes:
            __size (int): size of a side of the square
    """

    def __init__(self, size=0):
        """
        Args:
        size (int): size for __size attribute of class instance
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area based on size of square
        Returns:
        int: The return value. Returns the area
        """
        return self.__size * self.__size
