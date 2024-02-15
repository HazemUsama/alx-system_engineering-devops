#!/usr/bin/python3
"""Script to show how many subs in a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subs"""
    if subreddit is None or type(subreddit) is not str:
        return 0

    results = requests.get("https://www.reddit.com/r/{}/about.json"
                           .format(subreddit))

    subs = results.json().get("data", {}).get("subscribers", 0)
    return subs
