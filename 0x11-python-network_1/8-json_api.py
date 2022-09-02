#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

if __name__ == "__main__":
    import requests as req
    import sys

    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    r = req.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        json_dict = r.json()
        if len(json_dict.keys()) > 0:
            print("[{}] {}".format(json_dict.get('id'), json_dict.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
