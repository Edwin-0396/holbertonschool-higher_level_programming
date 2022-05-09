#!/usr/bin/python3
def no_c(my_string):

    for i in range(0, len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            my_string[i] = ""
            return my_string
