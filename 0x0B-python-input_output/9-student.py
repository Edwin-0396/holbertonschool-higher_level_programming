#!/usr/bin/python3

"""Module that defines a class student"""


class Student:
    """"Class named Student

    Attributes:
    first name: first name of student
    last name: last name of student
    age: age of student
    """

    def __init__(self, first_name, last_name, age):
        """Instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self):
            """Dictionary represetation of student"""
            return self.__dict__
