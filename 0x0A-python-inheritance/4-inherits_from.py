#!/usr/bin/python3
"""Module to see if instance of child class"""


def inherits_from(obj, a_class):
    """Returns true if instance of the inherited class"""
    return (isinstance(obj, a_class) and type(obj) != a_class)
