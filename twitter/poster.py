from twitter.auth import get_api

def post_tweet(content):
    api = get_api()
    api.update_status(content)