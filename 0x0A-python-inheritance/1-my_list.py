#!/usr/bin/python3

class Mylist(list):
    """A class named Mylist
    Attributes:
    attr1(print_sorted): print sorted list
    """

    def print_sorted(self):
        """Print instance"""
        print(sorted(self))
