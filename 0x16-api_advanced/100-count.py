#!/usr/bin/python3
"""Module to recursively query the Reddit API and count occurrences of keywords in hot post titles."""
import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
    """Recursively fetch all hot articles from a subreddit and count the occurrences of words.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count in the hot article titles.
        hot_list (list): Accumulates the hot post titles from the Reddit API (used for recursion).
        after (str): The pagination key to fetch more posts.

    Returns:
        None: Prints the count of each keyword in descending order.
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
                hot_list.append(post['data']['title'].lower())

            after = data['data'].get('after')
            if after:
                return count_words(subreddit, word_list, hot_list, after)  # Recursively call for the next page
            else:
                # Count occurrences of each word in the word list
                word_count = {}
                for word in word_list:
                    word_count[word.lower()] = 0  # Initialize all word counts to 0
                    for title in hot_list:
                        word_count[word.lower()] += title.split().count(word.lower())

                # Filter out words with a count of 0 and sort by count, then alphabetically
                sorted_words = sorted(
                    ((word, count) for word, count in word_count.items() if count > 0),
                    key=lambda x: (-x[1], x[0])
                )

                # Print the results
                for word, count in sorted_words:
                    print(f"{word}: {count}")

        except ValueError:
            return None
    else:
        return None

