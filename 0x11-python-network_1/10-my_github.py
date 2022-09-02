#!/usr/bin/python3
""" script that takes in a URL, sends a request to the
URL and displays the body of the response"""

if __name__ == "__main__":
    import sys
    import requests
    from requests.auth import HTTPBasicAuth

    basic = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get('https://api.github.com/user', auth=basic)
    req_dict = req.json()
    print(req_dict.get('id'))
