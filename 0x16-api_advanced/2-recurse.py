#!/usr/bin/python3
"""Script to show the titles of all hot articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return the list of titles"""
    results = requests.get("https://www.reddit.com/r/{}/hot.json"
                           .format(subreddit),
                           params={"after": after},
                           allow_redirects=False,
                           headers={'User-Agent': '/u/Hazemusama'})

    if results.status_code != 200:
        return None

    posts = results.json().get("data", {}).get("children", {})
    for post in posts:
        hot_list.append(post.get("data", {}).get("title", ""))

    after = results.json().get("data", {}).get("after", None)
    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
