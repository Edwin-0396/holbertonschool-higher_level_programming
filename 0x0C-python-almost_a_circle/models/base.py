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
		"""Initiliazes an instance"""
		if id is not None:
			self.id = id
		else:
			Base.__nb_objects += 1
			self.id = Base.__nb_objects

	@staticmethod
	def to_json_string(list_dictionaries):
		"""converts list of dictionaries to json string"""
		if list_dictionaries is None or list_dictionaries == "":
			list_dictionaries = "[]"
			return list_dictionaries
		return json.dumps(list_dictionaries)

	@classmethod
	def save_to_file(cls, list_objs):
		"""writes the JSON string representation of list_objs to a file"""
		dict = []
		createfile = cls.__name__ + ".json"
		if list_objs is None:
			with open(createfile, "w", encoding='utf-8') as f:
				f.write(cls.to_json_string(list_objs))

		for element in list_objs:
			dict.append(element.to_dictionary())

		with open(createfile, "w", encoding='utf-8') as f:
			f.write(cls.to_json_string(dict))

	@staticmethod
	def from_json_string(json_string):
		"""converts json string to object"""
		str_list = []
		if json_string is None or json_string == "":
			return str_list
		str_list = json.loads(json_string)
		return str_list

	@classmethod
	def create(cls, **dictionary):
		"""creates an instance based on a dictionary"""
		if cls.__name__ == "Rectangle":
			instance = cls(4, 6, 2)

		if cls.__name__ == "Square":
			instance = cls(4, 6)
		instance.update(**dictionary)
		return instance

	@classmethod
	def load_from_file(cls):
		"""loads a list of instances from a json file"""
		listv = []
		with open(cls.__name__ + ".json", "r", encoding='utf-8') as f:
			listv = cls.from_json_string(f.read())
		listv2 = []
		for i in listv:
			if type(i) is dict:
				listv2.append(cls.create(**i))
			else:
				listv2.append(i)
		return listv2
