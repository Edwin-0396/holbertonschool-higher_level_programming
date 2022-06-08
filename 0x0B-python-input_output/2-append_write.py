#!/usr/bin/python3
"""Module with a function to append text"""


def append_write(filename="", text=""):
    """append text to the end
    Args:
    filename: name of file to append text to
    text: text to append
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
