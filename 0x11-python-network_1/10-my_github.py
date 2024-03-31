#!/usr/bin/python3

""" a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]

    authen = (username, password)

    url = 'https://api.github.com/user'

    res = requests.get(url, auth=authen)

    if res.status_code == 200:
        print(res.json()['id'])
    else:
        print('None')
