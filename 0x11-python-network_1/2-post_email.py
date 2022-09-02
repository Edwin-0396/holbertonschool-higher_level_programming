#!/usr/bin/python3

if __name__ == "__main__":

    import urllib.request
    import sys

    data = urllib.parse.urlencode({'email': sys.argv[2]})
    url = sys.argv[1]

    data = data.encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
