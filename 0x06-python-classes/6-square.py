#!/usr/bin/python3

"""Module that creates a class named square"""

from re import U


class Square:
    """A class named square
    Attributes:
    attr1 (size): size of square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
        size (int): size for __size attribute of class instance
        """
        self.__size = size
        self__position = position

    def area(self):
        """Determine the area of the square
        Returns:
        int: The size of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """Get the size of the class"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the class"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints in stdout the square with #"""
        if self.__size > 0:
            for row in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for column in range(self.__position[0]):
                    print(" ", end="")
                for colum in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()

    @property
    def position(self):
        """get the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0] != int or type(value[1] != 1)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
