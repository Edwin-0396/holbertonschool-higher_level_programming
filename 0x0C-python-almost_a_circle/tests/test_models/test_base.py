#!/usr/bin/python3


""""Module test for base class"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):

	"""Test cases for the Base class"""

	base_1 = Base()
	base_2 = Base()
	base_3 = Base(5)

	def test_base_create(self):
		self.assertEqual(self.base_1.id, 1)

	def test_base_update_id(self):
		self.assertEqual(self.base_2.id, 2)

	def test_base_id(self):
		self.assertEqual(self.base_3.id, 5)

	def test_base_tojsonstringnone(self):
		ret = "[]"
		test_list = self.base_1.to_json_string(None)
		self.assertEqual(ret, test_list)

	def test_base_tojsonstringempty(self):
		ret = "[]"
		test_list = self.base_1.to_json_string([])
		self.assertEqual(ret, test_list)

	def test_base_tojsonstringdict(self):
		test_dict = [{'id': 7}]
		ret = "[{\"id\": 7}]"
		self.assertEqual(self.base_1.to_json_string(test_dict), ret)

	def test_base_fromjsonstringnone(self):
		ret = []
		test_list = self.base_1.from_json_string(None)
		self.assertEqual(ret, test_list)

	def test_base_fromjsonstringempty(self):
		ret = []
		test_list = self.base_1.from_json_string("[]")
		self.assertEqual(ret, test_list)

	def test_base_fromjsonstringdict(self):
		ret = [{'id': 7}]
		test_dict = "[{\"id\": 7}]"
		self.assertEqual(self.base_1.from_json_string(test_dict), ret)


if __name__ == '__main__':
	unittest.main()
