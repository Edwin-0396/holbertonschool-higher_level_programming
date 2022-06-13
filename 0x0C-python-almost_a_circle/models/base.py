#!/usr/bin/python3

"""Models base"""

class Base:
	"""Class base
	Attr:
	__nb_objects: number of instances
	"""
	__nb_objects = 0

	def __init__(self, id=None):
		"""instance attribute
		args:
		id: id of the current element
		"""
		if id is not None:
			self.id = id
		else:
			Base.__nb_objects += 1
			self.id = Base.__nb_objects
