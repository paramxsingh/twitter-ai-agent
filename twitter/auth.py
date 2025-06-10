import tweepy
from config import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET

def get_api():
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    return tweepy.API(auth)