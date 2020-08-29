#!/usr/bin/env python3

import os, time
import twython

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

if __name__ == "__main__":
    twitter = twython.Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    for friend_id in twitter.get_friends_ids()['ids']:
        print(f"Disabling retweets for {friend_id}")
        twitter.update_friendship(user_id=friend_id, retweets=False)
        time.sleep(5)
