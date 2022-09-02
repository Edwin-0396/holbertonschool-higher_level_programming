#!/usr/bin/python3

if __name__ == "__main__":

    import urllib.request
    import sys

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print(html.decode('utf-8'))

    except urllib.error.HTTPError as e:
        print(f"Error code: {e.status}")
