#!/usr/bin/python3
"""This module queries the Reddit API"""
import requests


def top_ten(subreddit):
    """Returns the top 10 hot post for a given subreddit"""
    headers = {'User-Agent': 'RedditSubs'}
    subreddit = subreddit
    url = 'https://www.reddit.com/r'
    full_url = '{}/{}/hot.json?limit=10'.format(url, subreddit)

    response = requests.get(full_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        for post in posts:
            print(post['data']['title'])
    else:
        print('None')
