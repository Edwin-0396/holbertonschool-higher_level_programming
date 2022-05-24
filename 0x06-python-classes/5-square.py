#!/usr/bin/python3
"""Square class definition"""


class Square:
    """class Square

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
        """determine the area of square

        Returns:
        int: Return the area
        """
        return self.__size * self.__size

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
        self.__size

    def my_print(self):
        """Print in stdout the square with #"""
        if self.__size > 0:
            for row in range(self.__size):
                for column in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
