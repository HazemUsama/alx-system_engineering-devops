#!/usr/bin/python3
"""Script to show first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """Return the title of the top subs"""
    if subreddit is None or type(subreddit) is not str:
        return 0

    results = requests.get("https://www.reddit.com/r/{}/top.json"
                           .format(subreddit),
                           params={"limit": 10})

    posts = results.json().get("data", {}).get("children", {})
    if posts is {}:
        print("None")
    else:
        for post in posts:
            print(post.get("data", {}).get("title", ""))
