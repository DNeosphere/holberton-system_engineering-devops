#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""
import json
import requests


def top_ten(subreddit):
    """ top ten """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'linux:com.myapp:v.1'}
    params = {'limit': 10}

    response = requests.get(url=url, headers=headers, params=params)

    if response.status_code == 404:
        print('None')
        return

    post_list = response.json().get('data').get('children')

    for post in post_list:
        print(post.get('data').get('title'))
