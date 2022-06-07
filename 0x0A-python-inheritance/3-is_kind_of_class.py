#!/usr/bin/python3
"""Module to see the kind of an obj"""


def is_kind_of_class(obj, a_class):
    """Object an instance of the a_class as inherited class"""
    return (isinstance(obj, a_class))
