#!/usr/bin/python3
"""This module recursively queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list of titles of
    all hot articles for the given subreddit
    """
    if hot_list is None:
        return None

    if len(hot_list) >= 1000:
        return hot_list

    headers = {'User-Agent': 'RedditSubs'}
    subreddit = subreddit
    url = 'https://www.reddit.com/r'
    full_url = '{}/{}/hot.json'.format(url, subreddit)

    response = requests.get(full_url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        after = data.get('data', {}).get('after')

        # Append titles to hot_list
        for post in posts:
            hot_list.append(post['data']['title'])
        return recurse(subreddit, hot_list, after)
    else:
        return None
