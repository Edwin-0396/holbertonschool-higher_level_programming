#!/usr/bin/python3
"""This module contain the write function"""


def write_file(filename="", text=""):
    """This function writes into text file
    Args:
    filename: file to wirte to
    text: text to write
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
