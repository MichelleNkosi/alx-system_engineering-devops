#!/usr/bin/python3
"""Module to query the Reddit API and get the number of subscribers."""
import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers, or 0 if subreddit is invalid.
    """
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36",
        "Accept": "application/json",
        "Referer": "https://www.google.com"
    }

    response = requests.get(url, headers=headers, allow_redirects=True)

    print("Response Status Code:", response.status_code)  # Debugging line
    print("Redirected URL:", response.url)  # Show where it's redirected to

    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    return 0

