#!/usr/bin/python3

"""module with function to get object from json file"""

import json


def load_from_json_file(filename):
    """get object form json file
    Args:
    filename: file to get from
    """

    with open(filename, encoding='utf-8') as file:
        return json.loads(file.read())
