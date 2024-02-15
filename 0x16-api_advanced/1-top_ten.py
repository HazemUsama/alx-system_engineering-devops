#!/usr/bin/python3
"""Script to show first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """Return the title of the top subs"""
    results = requests.get("https://www.reddit.com/r/{}/top.json"
                           .format(subreddit),
                           params={"limit": 10},
                           allow_redirects=False,
                           headers={'User-Agent': '/u/Hazemusama'})

    if results.status_code != 200:
        print("None")
    else:
        posts = results.json().get("data", {}).get("children", {})
        for post in posts:
            print(post.get("data", {}).get("title", ""))
