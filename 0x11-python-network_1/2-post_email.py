#!/usr/bin/python3
""" Python script that takes in a URL and an email, sends
a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)

"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    # encode the data to post

    email = email.encode('utf-8')

    with urllib.request.urlopen(url, data=email) as response:
        res = response.read().decode('utf-8')
        print(res)
