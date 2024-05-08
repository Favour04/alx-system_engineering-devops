#!/usr/bin/python3
import json
import urllib.request
"""
    module contain the function defination
"""


def number_of_subscribers(subreddit):
    """
        Function to return number of suscribers
        on a subreddit
    """
    req = urllib.request.Request('https://reddit.com/r/' +
                                 f'{subreddit}' + '/about.json')
    try:
        with urllib.request.urlopen(req) as response:
            status_code = response.getcode()

            if status_code == 200:
                fetched_data = response.read()
                fetched_data = fetched_data.decode('utf-8')
                fetched_data = json.loads(fetched_data)

                if 'data' in fetched_data:
                    if 'subscribers' in fetched_data['data']:
                        count = fetched_data['data']['subscribers']
                        return count
            else:
                return 0
    except Exception as e:
        return 0
