#!/usr/bin/python3
"""Module to recursively query the Reddit API and return the titles of all hot posts."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetch all hot articles from a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the hot article titles.
        after (str): The pagination key to fetch more posts.

    Returns:
        list: A list of all hot article titles, or None if an invalid subreddit is provided.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36",
        "Accept": "application/json",
        "Referer": "https://www.google.com"
    }
    
    params = {}
    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                hot_list.append(post['data']['title'])
            
            # Check if there is another page of results
            after = data['data'].get('after')
            if after:
                return recurse(subreddit, hot_list, after)  # Recursively call for the next page
            else:
                return hot_list  # No more pages, return the list of titles
        except ValueError:
            return None
    else:
        return None

