#!/usr/bin/python3

"""Module to get the json serialization for a class"""


def class_to_json(obj):
    """Returns the dictionary description of object
Args:
obj (object): object to return dictionary description  of
"""
    return obj.__dict__
