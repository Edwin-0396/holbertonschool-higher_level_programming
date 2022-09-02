#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests as req

    resp = req.get("https://intranet.hbtn.io/status")
    resp = resp.text
    print("Body response:")
    print("\t- type: {}".format(type(resp)))
    print("\t- content: {}".format(resp))
