#!/usr/bin/python3

"""Module for a sqaure class"""

from models.rectangle import Rectangle

class Square(Rectangle):
	def __init__(self, size, x=0, y=0, id=None):
		super().__init__(size, size, x, y, id)

	def __str__(self):
		return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

	@property
	def size(self):
		return self.width
	
	@size.setter
	def size(self, value):
		self.width = value
		self.height = value

	def update(self, *args, **kwargs):
		if len(args) == 0:
			for key in kwargs:
				setattr(self, key, kwargs[key]) 

		else:
			tupla = [
				"id",
				"size",
				"x",
				"y"
			]
			for i in range(len(args)):
				setattr(self, tupla[i], args[i])
	
	def to_dictionary(self):
		return vars(self)

