#!/usr/bin/python3
"""
a Python script that takes in a URL, sends
"""
import urllib.request
from sys import argv
import urllib.error


if __name__ == "__main__":
    url = argv[1]

    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
