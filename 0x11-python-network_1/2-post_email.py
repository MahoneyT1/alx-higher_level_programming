#!/usr/bin/python3
<<<<<<< HEAD
""" Python script that takes in a URL and an email, sends
a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)

"""
import urllib.request
from sys import argv

=======
"""Sends a POST request to a given URL with a given email.
Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""

import urllib.request
import urllib.parse
from sys import argv


>>>>>>> a49b4acb0542e44542865210272f43ebe7ea6e21
if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

<<<<<<< HEAD
    # encode the data to post

    email = email.encode('utf-8')

    with urllib.request.urlopen(url, data=email) as response:
        res = response.read().decode('utf-8')
        print(res)
=======
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
>>>>>>> a49b4acb0542e44542865210272f43ebe7ea6e21
