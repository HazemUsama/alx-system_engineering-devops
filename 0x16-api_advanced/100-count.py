#!/usr/bin/python3
"""Script to show the titles of all hot articles for a given subreddit"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
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
        line = post.get("data", {}).get("title", "")
        for word in word_list:
            count = line.count(word.lower())
            if count == 0:
                continue
            if word.lower() not in word_count:
                word_count[word.lower()] = 0
            word_count[word.lower()] += count

    after = results.json().get("data", {}).get("after", None)
    if after is None:
        word_count = dict(sorted(word_count.items(),
                                 key=lambda item: (item[1], item[0]),
                                 reverse=True))
        for key, value in word_count.items():
            print("{}: {}".format(key, value))
    else:
        count_words(subreddit, word_list, after)
