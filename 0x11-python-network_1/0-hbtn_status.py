#!/usr/bin/python3
""" A python script that fetches https:alx-intranet.hbtn.io/status """
import urllib.request



if __name__ == '__main__':
    custom_request = urllib.request.Request(
            'https://alx-intranet.hbtn.io/status')

    with urllib.request.urlopen(custom_request) as response:
        data = response.read()
        print('Body response:')
        print("\t - type: {}".format(type(data)))
        print("\t - content: {}".format(data))
        print("\t - utf8 content: {}".format(data.decode('utf-8')))
