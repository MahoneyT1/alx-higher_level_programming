#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""

import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    # use the parse to urlencode the param
    # you want to parse
    data = urllib.parse.urlencode({'email': email})

    # encoding it with utf-8
    data = data.encode('utf-8')

    # objectify the url and the params
    req = urllib.request.Request(url, data=data, method='post')

    # open the url and decode the response
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
