#!/usr/bin/python3

if __name__ == "__main__":
    import requests as req
    import sys

    resp = req.get(sys.argv[1])
    print(resp.headers['X-Request-Id'])
