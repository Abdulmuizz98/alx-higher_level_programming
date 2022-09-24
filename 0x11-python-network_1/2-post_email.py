#!/usr/bin/python3
"""
A Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response
(decoded in utf-8)
"""

if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    from sys import argv

    url = argv[1]
    email_payload = argv[2]

    data = urlencode({'email': email_payload}).encode('ascii')
    req = Request(url, data)

    with urlopen(req) as response:
        all_page = response.read()

    print(all_page.decode())
