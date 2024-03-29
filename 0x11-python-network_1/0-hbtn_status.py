#!/usr/bin/python3
import urllib.request


custom_request = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(custom_request) as response:
    html = response.read()
    print("Body response:")
    print("\t - type:", type(html))
    print("\t - content:", data)
    print("\t - utf8 content:", htlm.decode('utf-8'))
