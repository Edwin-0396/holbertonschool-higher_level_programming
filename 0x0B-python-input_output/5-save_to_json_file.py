#!/usr/bin/python3

"""module with function to save to json file"""

import json


def save_to_json_file(my_obj, filename):
    """save to json file
    Args:
    my_obj: obj to save
    filename: file to save to
    """

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
