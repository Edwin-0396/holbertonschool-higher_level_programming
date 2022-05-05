#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    addition_of_arguments = 0
    for i in range(1, len(sys.argv)):
        addition_of_arguments += int(sys.argv[i])
    print(addition_of_arguments)
