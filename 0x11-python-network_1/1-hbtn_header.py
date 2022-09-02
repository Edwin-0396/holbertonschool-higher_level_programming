#!/usr/bin/python3

if __name__ == "__main__":
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.read()
        print(response.info().get('X-Request-Id'))
