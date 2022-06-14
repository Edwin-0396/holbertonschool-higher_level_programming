#!/usr/bin/python3

"""module for rectangle class"""

from abc import abstractstaticmethod
from termios import VSTART
from models.base import Base


class Rectangle(Base):
	def __init__(self, width, height, x=0, y=0, id=None):
		self.staticfunc(width, "width")
		self.staticfunc(height, "height")
		self.staticfunc(x, "x")
		self.staticfunc(y, "y")
		self.__width = width
		self.__height = height
		self.__x = x
		self.__y = y
		super().__init__(id)

	@staticmethod
	def staticfunc(value, name_met):
		if type(value) is not int:
			raise TypeError(f"{name_met} must be an integer")
		if value <= 0 and name_met in ("width", "height"):
			raise ValueError(f"{name_met} must be > 0")
		if value < 0 and name_met in ("x", "y"):
			raise ValueError(f"{name_met} must be >= 0")

	def area(self):
		return self.__width * self.__height

	def display(self):
		if self.__y > 0:
			for i in range(self.__y):
				print()

		for row in range(self.__height):
			if self.__x > 0:
				print(" " * self.__x, end="")
			for column in range(self.__width):
				print("#", end="")
			print()

	def __str__(self):
		return f"[Rectangle] ({self.id}) {self.x}/\
	{self.y} - {self.width}/{self.height}"

	@property
	def width(self):
		return self.__width

	@width.setter
	def width(self, value):
		self.staticfunc(value, "width")
		self.__width = value

	@property
	def height(self):
		return self.__height

	@height.setter
	def height(self, value):
		self.staticfunc(value, "height")
		self.__height = value

	@property
	def x(self):
		return self.__x

	@x.setter
	def x(self, value):
		self.staticfunc(value, "x")
		self.__x = value

	@property
	def y(self):
		return self.__y

	@y.setter
	def y(self, value):
		self.staticfunc(value, "y")
		self.__y = value

	def update(self, *args, **kwargs):
		if len(args) == 0:
			for key in kwargs:
				setattr(self, key, kwargs[key]) 

		else:
			tupla = [
				"id",
				"width",
				"height",
				"x",
				"y"
			]
			for i in range(len(args)):
				setattr(self, tupla[i], args[i])

	def to_dictionary(self):
		return vars(self)

