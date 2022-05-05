#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    Number_of_arguments = len(sys.argv)
    if Number_of_arguments <= 1:
        print(f"0 arguments.")
    else:
        if len(sys.argv) == 2:
            print(f"{len(sys.argv) - 1} argument:\n{len(sys.argv) - 1}:\
 {sys.argv[1]}")
        elif len(sys.argv) > 2:
            print(f"{len(sys.argv) - 1} arguments:")
            for i in range(1, len(sys.argv)):
                print(f"{i}: {sys.argv[i]}")
