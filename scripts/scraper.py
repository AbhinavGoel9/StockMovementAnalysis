import tweepy
import pandas as pd

def authenticate_twitter(api_key, api_secret, access_token, access_secret):
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret)
    return tweepy.API(auth, wait_on_rate_limit=True)

def fetch_tweets(api, query, count=100):
    tweets = []
    for tweet in tweepy.Cursor(api.search_tweets, q=query, lang="en", tweet_mode="extended").items(count):
        tweets.append({'created_at': tweet.created_at, 'text': tweet.full_text, 'user': tweet.user.screen_name})
    return pd.DataFrame(tweets)

if __name__ == "__main__":
    # Replace with your API keys
    API_KEY = "your_api_key"
    API_SECRET = "your_api_secret"
    ACCESS_TOKEN = "your_access_token"
    ACCESS_SECRET = "your_access_secret"

    api = authenticate_twitter(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    data = fetch_tweets(api, query="StockMarket", count=200)
    data.to_csv('data/raw_tweets.csv', index=False)
