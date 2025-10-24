#!/usr/bin/python3
"""Function that queries the Reddit API"""
import requests


def top_ten(subreddit):
    """Prints titles of first 10 hot posts for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'linux:0:1.0 (by /u/JuiceExtension6952)'}
    params = {"limit": 10}
    
    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)
        
        # Check if request was successful and subreddit exists
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            
            if len(posts) == 0:
                print("None")
            else:
                for post in posts[:10]:
                    print(post['data']['title'])
        else:
            print("None")
            
    except Exception:
        print("None")
