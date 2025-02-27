#!/usr/bin/python3
"""Module to query the Reddit API and print titles of the first 10 hot posts."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None: If the subreddit is invalid or there is an error.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36",
        "Accept": "application/json",
        "Referer": "https://www.google.com"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            hot_posts = data['data']['children']
            for post in hot_posts[:10]:
                print(post['data']['title'])
        except ValueError:
            print(None)
    else:
        print(None)

