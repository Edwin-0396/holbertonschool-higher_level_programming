#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout
    Args:
    filename (str): Filename
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
