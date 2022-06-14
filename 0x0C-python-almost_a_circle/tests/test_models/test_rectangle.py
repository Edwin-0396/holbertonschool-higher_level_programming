#!/usr/bin/python3
"""
    Module to test Rectangle class
"""


import unittest
from models.rectangle import Rectangle
from io import StringIO
from contextlib import redirect_stdout
import os


class TestRectangle(unittest.TestCase):
    """
        Test class for Rectangle class
    """
    def test_rect_1(self):
        rect_test = Rectangle(1, 2)
        self.assertEqual(rect_test.width, 1)
        self.assertEqual(rect_test.height, 2)

    def test_rect_2(self):
        rect_test = Rectangle(1, 2, 3)
        self.assertEqual(rect_test.width, 1)
        self.assertEqual(rect_test.height, 2)
        self.assertEqual(rect_test.x, 3)

    def test_rect_3(self):
        rect_test = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect_test.width, 1)
        self.assertEqual(rect_test.height, 2)
        self.assertEqual(rect_test.x, 3)
        self.assertEqual(rect_test.y, 4)

    def test_rect_4(self):
        rect_test = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect_test.width, 1)
        self.assertEqual(rect_test.height, 2)
        self.assertEqual(rect_test.x, 3)
        self.assertEqual(rect_test.y, 4)
        self.assertEqual(rect_test.id, 5)

    def test_rect_5(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            Rectangle(0, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(-1, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, -1)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 1, -1)

    def test_rect_area(self):
        test_rect = Rectangle(4, 5)
        self.assertEqual(test_rect.area(), 20)

    def test_rect_str(self):
        test_rect = Rectangle(1, 2, 0, 0, 1012)
        ret = "[Rectangle] (1012) 0/0 - 1/2"
        self.assertEqual(test_rect.__str__(), ret)

    def test_rect_display(self):
        test_rect = Rectangle(2, 2)
        ret = "##\n##\n"
        with redirect_stdout(StringIO()) as f:
            test_rect.display()
        s = f.getvalue()
        self.assertEqual(ret, s)

    def test_rect_display_x(self):
        test_rect = Rectangle(2, 2, 2)
        ret = "  ##\n  ##\n"
        with redirect_stdout(StringIO()) as f:
            test_rect.display()
        s = f.getvalue()
        self.assertEqual(ret, s)

    def test_rect_display_xy(self):
        test_rect = Rectangle(2, 2, 2, 2)
        ret = "\n\n  ##\n  ##\n"
        with redirect_stdout(StringIO()) as f:
            test_rect.display()
        s = f.getvalue()
        self.assertEqual(ret, s)

    def test_rect_todictionary(self):
        test_rect = Rectangle(1, 2, 3, 4, 5)
        ret = {'x': 3, 'y': 4, 'id': 5, 'height': 2, 'width': 1}
        self.assertEqual(test_rect.to_dictionary(), ret)

    def test_rect_update_empty(self):
        test_rect = Rectangle(1, 1)
        dict_1 = test_rect.to_dictionary()
        test_rect.update()
        dict_2 = test_rect.to_dictionary()
        self.assertEqual(dict_1, dict_2)

    def test_rect_update_id(self):
        test_rect = Rectangle(1, 1)
        dict_1 = test_rect.to_dictionary()
        test_rect.update(89)
        dict_2 = test_rect.to_dictionary()
        self.assertNotEqual(dict_1, dict_2)
        self.assertEqual(test_rect.id, 89)

    def test_rect_update_id_w(self):
        test_rect = Rectangle(1, 1)
        dict_1 = test_rect.to_dictionary()
        test_rect.update(89, 5)
        dict_2 = test_rect.to_dictionary()
        self.assertNotEqual(dict_1, dict_2)
        self.assertEqual(test_rect.id, 89)
        self.assertEqual(test_rect.width, 5)

    def test_rect_update_id_w_h(self):
        test_rect = Rectangle(1, 1)
        dict_1 = test_rect.to_dictionary()
        test_rect.update(89, 5, 6)
        dict_2 = test_rect.to_dictionary()
        self.assertNotEqual(dict_1, dict_2)
        self.assertEqual(test_rect.id, 89)
        self.assertEqual(test_rect.width, 5)
        self.assertEqual(test_rect.height, 6)
   
    def test_rect_update_id_w_h_x(self):
        test_rect = Rectangle(1, 1)
        dict_1 = test_rect.to_dictionary()
        test_rect.update(89, 5, 6, 2)
        dict_2 = test_rect.to_dictionary()
        self.assertNotEqual(dict_1, dict_2)
        self.assertEqual(test_rect.id, 89)
        self.assertEqual(test_rect.width, 5)
        self.assertEqual(test_rect.height, 6)
        self.assertEqual(test_rect.x, 2)
   
    def test_rect_update_id_w_h_x_y(self):
        test_rect = Rectangle(1, 1)
        dict_1 = test_rect.to_dictionary()
        test_rect.update(89, 5, 6, 2, 3)
        dict_2 = test_rect.to_dictionary()
        self.assertNotEqual(dict_1, dict_2)
        self.assertEqual(test_rect.id, 89)
        self.assertEqual(test_rect.width, 5)
        self.assertEqual(test_rect.height, 6)
        self.assertEqual(test_rect.x, 2)
        self.assertEqual(test_rect.y, 3)

    def test_rect_kupdate_id(self):
        test_rect = Rectangle(1, 1)
        dict_1 = test_rect.to_dictionary()
        test_rect.update(**{"id": 89})
        dict_2 = test_rect.to_dictionary()
        self.assertNotEqual(dict_1, dict_2)
        self.assertEqual(test_rect.id, 89)

    def test_rect_kupdate_id_width(self):
        test_rect = Rectangle(1, 1)
        dict_1 = test_rect.to_dictionary()
        test_rect.update(**{"id": 89, "width": 5})
        dict_2 = test_rect.to_dictionary()
        self.assertNotEqual(dict_1, dict_2)
        self.assertEqual(test_rect.id, 89)
        self.assertEqual(test_rect.width, 5)

    def test_rect_kupdate_id_width_height(self):
        test_rect = Rectangle(1, 1)
        dict_1 = test_rect.to_dictionary()
        test_rect.update(**{"id": 89, "width": 5, "height": 6})
        dict_2 = test_rect.to_dictionary()
        self.assertNotEqual(dict_1, dict_2)
        self.assertEqual(test_rect.id, 89)
        self.assertEqual(test_rect.width, 5)
        self.assertEqual(test_rect.height, 6)

    def test_rect_kupdate_id_width_height_x(self):
        test_rect = Rectangle(1, 1)
        dict_1 = test_rect.to_dictionary()
        test_rect.update(**{"id": 89, "width": 5, "height": 6, "x": 7})
        dict_2 = test_rect.to_dictionary()
        self.assertNotEqual(dict_1, dict_2)
        self.assertEqual(test_rect.id, 89)
        self.assertEqual(test_rect.width, 5)
        self.assertEqual(test_rect.height, 6)
        self.assertEqual(test_rect.x, 7)

    def test_rect_kupdate_id_width_height_x_y(self):
        test_rect = Rectangle(1, 1)
        dict_1 = test_rect.to_dictionary()
        test_rect.update(**{"id": 89, "width": 5, "height": 6, "x": 7, "y": 8})
        dict_2 = test_rect.to_dictionary()
        self.assertNotEqual(dict_1, dict_2)
        self.assertEqual(test_rect.id, 89)
        self.assertEqual(test_rect.width, 5)
        self.assertEqual(test_rect.height, 6)
        self.assertEqual(test_rect.x, 7)
        self.assertEqual(test_rect.y, 8)

    def test_rect_create_id(self):
        test_rect = Rectangle(1, 1)
        new_rect = test_rect.create(**{"id": 95})
        self.assertIsNot(test_rect, new_rect)
        self.assertEqual(new_rect.id, 95)

    def test_rect_create_id_width(self):
        test_rect = Rectangle(1, 1)
        new_rect = test_rect.create(**{"id": 95, "width": 5})
        self.assertIsNot(test_rect, new_rect)
        self.assertEqual(new_rect.id, 95)
        self.assertEqual(new_rect.width, 5)

    def test_rect_create_id_width_height(self):
        test_rect = Rectangle(1, 1)
        new_rect = test_rect.create(**{"id": 95, "width": 5, "height": 6})
        self.assertIsNot(test_rect, new_rect)
        self.assertEqual(new_rect.id, 95)
        self.assertEqual(new_rect.width, 5)
        self.assertEqual(new_rect.height, 6)

    def test_rect_create_id_width_height_x(self):
        test_rect = Rectangle(1, 1)
        new_rect = test_rect.create(**{"id": 95, "width": 5, "height": 6, "x": 7})
        self.assertIsNot(test_rect, new_rect)
        self.assertEqual(new_rect.id, 95)
        self.assertEqual(new_rect.width, 5)
        self.assertEqual(new_rect.height, 6)
        self.assertEqual(new_rect.x, 7)

    def test_rect_create_id_width_height_x_y(self):
        test_rect = Rectangle(1, 1)
        new_rect = test_rect.create(**{"id": 95, "width": 5, "height": 6, "x": 7, "y": 8})
        self.assertIsNot(test_rect, new_rect)
        self.assertEqual(new_rect.id, 95)
        self.assertEqual(new_rect.width, 5)
        self.assertEqual(new_rect.height, 6)
        self.assertEqual(new_rect.x, 7)
        self.assertEqual(new_rect.y, 8)

    def test_rect_savetofile_none(self):
        ret = "[]"
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            s = (file.read())
        self.assertEqual(ret, s)
        os.remove("Rectangle.json")

    def test_rect_savetofile_empty(self):
        ret = "[]"
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            s = (file.read())
        self.assertEqual(ret, s)
        os.remove("Rectangle.json")

    def test_rect_savetofile_something(self):
        ret = '[{"x": 6, "y": 8, "id": 10, "height": 4, "width": 2}]'
        r1 = Rectangle(2, 4, 6, 8, 10)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as file:
            s = (file.read())
        self.assertEqual(ret, s)
        os.remove("Rectangle.json")

    def test_rect_loadfromfile_nofile(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass
        test_list = Rectangle.load_from_file()
        self.assertEqual(test_list, [])

    def test_rect_loadfromfile(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r1])
        test_list = Rectangle.load_from_file()
        self.assertEqual(test_list[0].to_dictionary(), r1.to_dictionary())
        os.remove("Rectangle.json")

if __name__ == '__main__':
    unittest.main()