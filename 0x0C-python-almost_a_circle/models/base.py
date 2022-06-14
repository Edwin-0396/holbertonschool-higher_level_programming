#!/usr/bin/python3

"""Models base"""
import json

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

	@staticmethod
	def to_json_string(list_dictionaries):
		if list_dictionaries is None or list_dictionaries == "":
			list_dictionaries = "[]"
			return list_dictionaries
		return json.dumps(list_dictionaries)

	@classmethod
	def save_to_file(cls, list_objs):
		dict = []
		createfile = cls.name + ".json"
		if list_objs is None:
			with open(createfile, "w", encoding='utf-8') as f:
				f.write(cls.to_json_string(list_objs))

		for element in list_objs:
			dict.append(element.to_dictionary())

		with open(createfile, "w", encoding='utf-8') as f:
				f.write(cls.to_json_string(dict))

	@staticmethod
	def from_json_string(json_string):
		str_list = []
		if json_string is None or json_string == "":
			return str_list
		str_list = json.loads(json_string)
		return str_list

	@classmethod
	def create(cls, **dictionary):