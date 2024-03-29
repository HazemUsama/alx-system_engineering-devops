#!/usr/bin/python3
"""Script to show how many subs in a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subs"""
    results = requests.get("https://www.reddit.com/r/{}/about.json"
                           .format(subreddit),
                           headers={'User-Agent': '/u/Hazemusama'}).json()

    return results.get("data", {}).get("subscribers", 0)
