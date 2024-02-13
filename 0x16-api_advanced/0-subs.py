#!/usr/bin/python3
"""
This module queries the Reddit API for the number of subscriptions
for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a fiven subreddit

    Return:
        subscriber count or 0 if no subscribers"""
    headers = {'User-Agent': 'RedditSubs'}
    subreddit = subreddit
    url = 'https://www.reddit.com/r'
    full_url = '{}/{}/about.json'.format(url, subreddit)
    response = requests.get(full_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers_count = data['data']['subscribers']
        return subscribers_count
    else:
        return 0
