#!/usr/bin/python3

if __name__ == "__main__":
    import requests as req
    import sys

    response = req.get(sys.argv[1])
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
