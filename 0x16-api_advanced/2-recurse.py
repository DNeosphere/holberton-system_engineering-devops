#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""
import json
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ recursively """
    if after is None:
        return hot_list

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'linux:com.myapp:v.1'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url=url, headers=headers, params=params)

    if response.status_code == 404:
        return None

    response = response.json()
    for post in response.get('data').get('children'):
        hot_list.append(post.get('data').get('title'))
    after = response.get('data').get('after')
    return recurse(subreddit, hot_list, after)
