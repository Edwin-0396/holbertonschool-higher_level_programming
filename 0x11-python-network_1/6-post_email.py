#!/usr/bin/python3

if __name__ == "__main__":
    import requests as req
    import sys

    email = {'email': sys.argv[2]}
    r = req.post(sys.argv[1], data=email)
    print(r.text)
