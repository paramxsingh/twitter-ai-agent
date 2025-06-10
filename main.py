from twitter.poster import post_tweet
from ai.content_generator import generate_tweet

if __name__ == '__main__':
    tweet = generate_tweet()
    post_tweet(tweet)