#!/usr/bin/python3
"""
A python script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    from urllib.request import urlopen

    req = "https://alx-intranet.hbtn.io/status"
    with urlopen(req) as response:
        all_page = response.read()

    print("Body response:")
    print(f"\t- type: {type(all_page)}")
    print(f"\t- content: {all_page}")
    print(f"\t- utf8 content: {all_page.decode()}")
