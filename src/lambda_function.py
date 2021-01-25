import pandas as pd
import random


def get_tweet(tweets_file, excluded_tweets=None):
    '''
    Get a random tweet from the list of tweets
    Args:
        tweets_file: Path to the csv file containing the tweets
        excluded_tweets: tweepy.models.ResultSet object with the latest published tweets to exclude
    '''
    possible_tweets = list(pd.read_csv(tweets_file)['tweets'])
    
    if excluded_tweets:
        recent_tweets = [tweeted.text[:50] for tweeted in excluded_tweets]
        possible_tweets = [tweet for tweet in possible_tweets if tweet[:50] not in recent_tweets]

    selected_tweet = random.choice(possible_tweets)

    return selected_tweet


def lambda_handler(event, context):
    print("Get credentials")
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    print("Authenticate")
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    print("Get tweet from csv file")
    tweets_file = "../data/tweets.csv"
    recent_tweets = api.user_timeline()[:7]
    tweet = get_tweet(tweets_file, recent_tweets)

    print(f"Post tweet: {tweet}")
    api.update_status(tweet)

    return {"statusCode": 200, "tweet": tweet}