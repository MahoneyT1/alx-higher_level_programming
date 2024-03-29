#!/usr/bin/python3
import urllib.request
from sys import argv

"""
a Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in the
header of the response.
"""

url = argv[1]

with urllib.request.urlopen(url) as response:
    if 'X-Request-Id' in response.headers:
        me = response.headers['X-Request-Id']
        print(me)
