from scripts.scraper import authenticate_twitter, fetch_tweets
from scripts.preprocess import preprocess_data
from scripts.sentiment_analysis import analyze_sentiment
from scripts.train_model import train_model

def main():
    # Scrape Tweets
    API_KEY = "your_api_key"
    API_SECRET = "your_api_secret"
    ACCESS_TOKEN = "your_access_token"
    ACCESS_SECRET = "your_access_secret"

    api = authenticate_twitter(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    fetch_tweets(api, query="StockMarket", count=200)

    # Preprocess Data
    preprocess_data('data/raw_tweets.csv')

    # Sentiment Analysis
    analyze_sentiment('data/processed_tweets.csv')

    # Train and Evaluate Model
    train_model('data/sentiment_tweets.csv')

if __name__ == "__main__":
    main()
