#!/usr/bin/python3
"""Square class definition"""


class Square:
    """ A class named Square

            Attributes:
            attr1 (size): size of square
    """

    def __init__(self, size=0):
        """
        Args:
        size (int): size for __size attribute of class instance
        """
        self.__size = size

    def area(self):
        """ Determine the area of the square
        Returns:
        int: Return the area
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Get the size of the class instance"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the class instance"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
