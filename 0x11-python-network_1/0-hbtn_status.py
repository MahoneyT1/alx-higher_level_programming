#!/usr/bin/python3

"""
A python script that fetches https:alx-intranet.hbtn.io/status
uses package urllib
only import urllib
"""

if __name__ == '__main__':

    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')
    as response:
        data = response.read()

    print('Body response:$')
    print("\t - type: {}$".format(type(data)))
    print("\t - content: {}$".format(data))
    print("\t - utf8 content: {}$".format(data.decode('utf-8')))
