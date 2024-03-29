#!/usr/bin/python3
import urllib.request


custom_request = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(custom_request) as response:
    cus_data = response.read()
    print("Body response:")
    print("\t- type:", type(cus_data))
    print("\t- content:", cus_data)
    print("\t- utf8 content:", cus_data.decode('utf-8'))
