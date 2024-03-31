#!/usr/bin/python3

""" Please list 10 commits (from the most recent to oldest) of the
repository “rails” by the user “rails” You must use the GitHub API,
here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""

import requests
from sys import argv

if __name__ == '__main__':
    repo_name = argv[1]
    user = argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(user, repo_name)

    res = requests.get(url)

    if res.status_code == 200:
        commits = res.json()[:10]
    
    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print('{}: {}'.format(sha, author_name))
