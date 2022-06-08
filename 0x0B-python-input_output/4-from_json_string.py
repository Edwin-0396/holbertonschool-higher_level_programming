#!/usr/bin/python3

"""Module to get object from json"""
import json


def from_json_string(my_str):
    """get json from objet
    Args:
    my_str: object to get json from"""

    return json.loads(my_str)
