#!/usr/bin/python3
"""Script to show first 10 hot posts listed for a given subreddit"""
import requests
import os


def top_ten(subreddit):
    """Return the title of the top subs"""
    results = requests.get("https://www.reddit.com/r/{}/top.json"
                           .format(subreddit),
                           headers={'User-Agent': '/u/Hazemusama'},
                           params={"limit": 10})

    posts = results.json().get("data", {}).get("children")
    if not posts:
        print("None")
    else:
        for post in posts:
            print(post.get("data", {}).get("title", ""))
