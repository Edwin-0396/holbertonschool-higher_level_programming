#!/usr/bin/python3

"""class Rectangle that defines a rectangle by: (based on 0-rectangle.py"""


class Rectangle:
    """Class that defines a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Class instance"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """class property"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    @property
    def width(self):
        """width property"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Width setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__width = value

    def area(self):
        """defines area width * height"""
        return (self.__height * self.__width)

    def perimeter(self):
        """defines perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self) -> str:
        """Str metrhod to print a str of the rectangle class"""
        str_draw = ""
        if self.__width == 0 or self.__height == 0:
            return str_draw
        for row in range(self.__height):
            for column in range(self.__width):
                str_draw += str(self.print_symbol)
            str_draw += '\n'
        str_draw = str_draw[0:-1]
        return str_draw

    def __repr__(self) -> str:
        """Print a representation of the class"""
        str_draw = rep = 'Rectangle(' + str(self.width) + \
            ',' + str(self.height) + ')'
        return str_draw

    def __del__(self):
        """method to delete an instance"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method to check which instance area is greater"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """class method to change the area"""
        return cls(size, size)
