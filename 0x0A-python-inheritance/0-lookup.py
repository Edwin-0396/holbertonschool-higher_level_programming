#!/usr/bin/python3
"""Define the lookup module"""


def lookup(obj):
    """Return a valid list of attributes of the object"""
    return dir(obj)
