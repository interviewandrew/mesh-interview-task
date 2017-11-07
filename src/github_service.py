#!/usr/bin/env python3

'''
Simple set of tools to interface with and wrap the github api for us.
'''

import json
import requests

USER_URL_BASE = "https://api.github.com/users/%s"
USER_REPO_BASE = "https://api.github.com/users/%s/repos"
REPO_PR_URL_BASE = "https://api.github.com/repos/%s/%s/pulls"
REPO_COMMIT_URL_BASE = "https://api.github.com/repos/%s/%s/commits"

# TODO error handling and logging around this, should be a real method somewhere
g = lambda url: json.loads(requests.get(url).text)

def get_user_data(user_name='interviewandrew'):
    try:
        user_info = g(USER_URL_BASE % user_name)
        return user_info
    except requests.HTTPError as err:
        print(err) # or log properly.

def get_repos_for_user(user_name='interviewandrew'):
    try:
        return g(USER_REPO_BASE % user_name)
    except requests.HTTPError as err:
        print(err)

def get_commits(user_name, repo_name):
    try:
        return g(REPO_COMMIT_URL_BASE % (user_name, repo_name))
    except requests.HTTPError as err:
        print(err)

def get_pull_requests(user_name, repo_name):
    try:
        return g(REPO_PR_URL_BASE % (user_name, repo_name))
    except requests.HTTPError as err:
        print(err)

if __name__ == '__main__':
    print("I'm a module, not a script")
