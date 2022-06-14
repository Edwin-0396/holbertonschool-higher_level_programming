#!/usr/bin/python3
"""
    Module to test Square class
"""


import unittest
from models.square import Square
from io import StringIO
from contextlib import redirect_stdout
import os


class TestSquare(unittest.TestCase):
    """
        Test class for Square class
    """
    def test_square_1(self):
        square_test = Square(1)
        self.assertEqual(square_test.width, 1)
        self.assertEqual(square_test.height, 1)
        self.assertEqual(square_test.size, 1)

    def test_square_2(self):
        square_test = Square(1, 2)
        self.assertEqual(square_test.width, 1)
        self.assertEqual(square_test.height, 1)
        self.assertEqual(square_test.size, 1)
        self.assertEqual(square_test.x, 2)

    def test_square_3(self):
        square_test = Square(1, 2, 3)
        self.assertEqual(square_test.width, 1)
        self.assertEqual(square_test.height, 1)
        self.assertEqual(square_test.size, 1)
        self.assertEqual(square_test.x, 2)
        self.assertEqual(square_test.y, 3)

    def test_square_4(self):
        square_test = Square(1, 2, 3, 4)
        self.assertEqual(square_test.width, 1)
        self.assertEqual(square_test.height, 1)
        self.assertEqual(square_test.size, 1)
        self.assertEqual(square_test.x, 2)
        self.assertEqual(square_test.y, 3)
        self.assertEqual(square_test.id, 4)

    def test_square_5(self):
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -1)
        with self.assertRaises(ValueError):
            Square(1, 1, -1)

    def test_square_area(self):
        test_square = Square(4)
        self.assertEqual(test_square.area(), 16)

    def test_square_str(self):
        test_square = Square(1, 0, 0, 1012)
        ret = "[Square] (1012) 0/0 - 1"
        self.assertEqual(test_square.__str__(), ret)

    def test_square_display(self):
        test_square = Square(2)
        ret = "##\n##\n"
        with redirect_stdout(StringIO()) as f:
            test_square.display()
        s = f.getvalue()
        self.assertEqual(ret, s)

    def test_square_display_x(self):
        test_square = Square(2, 2)
        ret = "  ##\n  ##\n"
        with redirect_stdout(StringIO()) as f:
            test_square.display()
        s = f.getvalue()
        self.assertEqual(ret, s)

    def test_square_display_xy(self):
        test_square = Square(2, 2, 2)
        ret = "\n\n  ##\n  ##\n"
        with redirect_stdout(StringIO()) as f:
            test_square.display()
        s = f.getvalue()
        self.assertEqual(ret, s)

    def test_square_todictionary(self):
        test_square = Square(1, 2, 3, 4)
        ret = {'id': 4, 'x': 2, 'size': 1, 'y': 3}
        self.assertEqual(test_square.to_dictionary(), ret)

    def test_square_update_empty(self):
        test_square = Square(1)
        dict_1 = test_square.to_dictionary()
        test_square.update()
        dict_2 = test_square.to_dictionary()
        self.assertEqual(dict_1, dict_2)

    def test_square_update_id(self):
        test_square = Square(1)
        dict_1 = test_square.to_dictionary()
        test_square.update(89)
        dict_2 = test_square.to_dictionary()
        self.assertNotEqual(dict_1, dict_2)
        self.assertEqual(test_square.id, 89)

    def test_square_update_id_s(self):
        test_square = Square(1)
        dict_1 = test_square.to_dictionary()
        test_square.update(89, 5)
        dict_2 = test_square.to_dictionary()
        self.assertNotEqual(dict_1, dict_2)
        self.assertEqual(test_square.id, 89)
        self.assertEqual(test_square.size, 5)

    def test_square_update_id_s_x(self):
        test_square = Square(1)
        dict_1 = test_square.to_dictionary()
        test_square.update(89, 5, 6)
        dict_2 = test_square.to_dictionary()
        self.assertNotEqual(dict_1, dict_2)
        self.assertEqual(test_square.id, 89)
        self.assertEqual(test_square.size, 5)
        self.assertEqual(test_square.x, 6)
   
    def test_square_update_id_s_x_y(self):
        test_square = Square(1)
        dict_1 = test_square.to_dictionary()
        test_square.update(89, 5, 6, 2)
        dict_2 = test_square.to_dictionary()
        self.assertNotEqual(dict_1, dict_2)
        self.assertEqual(test_square.id, 89)
        self.assertEqual(test_square.size, 5)
        self.assertEqual(test_square.x, 6)
        self.assertEqual(test_square.y, 2)

    def test_square_kupdate_id(self):
        test_square = Square(1)
        dict_1 = test_square.to_dictionary()
        test_square.update(**{"id": 89})
        dict_2 = test_square.to_dictionary()
        self.assertNotEqual(dict_1, dict_2)
        self.assertEqual(test_square.id, 89)

    def test_square_kupdate_id_size(self):
        test_square = Square(1, 1)
        dict_1 = test_square.to_dictionary()
        test_square.update(**{"id": 89, "size": 5})
        dict_2 = test_square.to_dictionary()
        self.assertNotEqual(dict_1, dict_2)
        self.assertEqual(test_square.id, 89)
        self.assertEqual(test_square.size, 5)

    def test_square_kupdate_id_size_x(self):
        test_square = Square(1, 1)
        dict_1 = test_square.to_dictionary()
        test_square.update(**{"id": 89, "size": 5, "x": 6})
        dict_2 = test_square.to_dictionary()
        self.assertNotEqual(dict_1, dict_2)
        self.assertEqual(test_square.id, 89)
        self.assertEqual(test_square.size, 5)
        self.assertEqual(test_square.x, 6)

    def test_square_kupdate_id_size_x_y(self):
        test_square = Square(1, 1)
        dict_1 = test_square.to_dictionary()
        test_square.update(**{"id": 89, "size": 5, "x": 6, "y": 7})
        dict_2 = test_square.to_dictionary()
        self.assertNotEqual(dict_1, dict_2)
        self.assertEqual(test_square.id, 89)
        self.assertEqual(test_square.size, 5)
        self.assertEqual(test_square.x, 6)
        self.assertEqual(test_square.y, 7)

    def test_square_create_id(self):
        test_square = Square(1, 1)
        new_square = test_square.create(**{"id": 95})
        self.assertIsNot(test_square, new_square)
        self.assertEqual(new_square.id, 95)

    def test_square_create_id_size(self):
        test_square = Square(1)
        new_square = test_square.create(**{"id": 95, "size": 5})
        self.assertIsNot(test_square, new_square)
        self.assertEqual(new_square.id, 95)
        self.assertEqual(new_square.size, 5)

    def test_square_create_id_size_x(self):
        test_square = Square(1, 1)
        new_square = test_square.create(**{"id": 95, "size": 5, "x": 6})
        self.assertIsNot(test_square, new_square)
        self.assertEqual(new_square.id, 95)
        self.assertEqual(new_square.size, 5)
        self.assertEqual(new_square.x, 6)

    def test_square_create_id_size_x_y(self):
        test_square = Square(1, 1)
        new_square = test_square.create(**{"id": 95, "size": 5, "x": 6, "y": 7})
        self.assertIsNot(test_square, new_square)
        self.assertEqual(new_square.id, 95)
        self.assertEqual(new_square.size, 5)
        self.assertEqual(new_square.x, 6)
        self.assertEqual(new_square.y, 7)

    def test_square_savetofile_none(self):
        ret = "[]"
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            s = (file.read())
        self.assertEqual(ret, s)
        os.remove("Square.json")

    def test_square_savetofile_empty(self):
        ret = "[]"
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            s = (file.read())
        self.assertEqual(ret, s)
        os.remove("Square.json")

    def test_square_savetofile_something(self):
        ret = '[{"id": 4, "x": 2, "size": 1, "y": 3}]'
        r1 = Square(1, 2, 3, 4)
        Square.save_to_file([r1])
        with open("Square.json", "r") as file:
            s = (file.read())
        self.assertEqual(ret, s)
        os.remove("Square.json")

    def test_square_loadfromfile_nofile(self):
        try:
            os.remove("Square.json")
        except:
            pass
        test_list = Square.load_from_file()
        self.assertEqual(test_list, [])

    def test_square_loadfromfile(self):
        r1 = Square(1, 2, 3, 4)
        Square.save_to_file([r1])
        test_list = Square.load_from_file()
        self.assertEqual(test_list[0].to_dictionary(), r1.to_dictionary())
        os.remove("Square.json")

if __name__ == '__main__':
    unittest.main()