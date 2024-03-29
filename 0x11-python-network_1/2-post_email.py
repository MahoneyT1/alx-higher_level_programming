#!/usr/bin/python3
"""
a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response
(decoded in utf-8)
"""
import urllib.request
from urllib import parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}

    # use the parse to urlencode the param
    # you want to parse
    data = urllib.parse.urlencode(email)

    # encoding it with utf-8
    data = data.encode('utf-8')

    # objectify the url and the params
    req = urllib.request.Request(url, params=data)

    # open the url and decode the response
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
