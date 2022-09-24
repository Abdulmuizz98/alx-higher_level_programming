#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request
to the URL and displays the body of the response
(decoded in utf-8).
"""

if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib.error import URLError, HTTPError
    from sys import argv

    req = argv[1]
    try:
        with urlopen(req) as response:
            all_page = response.read()
    except HTTPError as e:
        print(f"Error code: {e.code}")
    else:
        print(all_page.decode())
