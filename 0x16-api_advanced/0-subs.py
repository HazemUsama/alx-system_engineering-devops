#!/usr/bin/python3
"""Script to show how many subs in a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subs"""
    results = requests.get("https://www.reddit.com/r/{}/about.json"
                           .format(subreddit),
                           headers={'User-agent': 'Mozilla/5.0'},
                           allow_redirects=False)

    return results.get("data", {}).get("subscribers", 0)
