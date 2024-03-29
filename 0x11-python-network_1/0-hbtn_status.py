#!/usr/bin/python3
import urllib.request

""" A python script that fetches https:alx-intranet.hbtn.io/status """

if __name__ == '__main__':
    custom_request = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(custom_request) as response:
        data = response.read()
        print('Body response:')
        print("\t - type: {}", type(data))
        print("\t - content: {}", data)
        print("\t - utf8 content: {}", data.decode('utf-8'))
