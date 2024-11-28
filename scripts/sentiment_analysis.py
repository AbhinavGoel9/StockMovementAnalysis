import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyze_sentiment(file_path):
    sia = SentimentIntensityAnalyzer()
    df = pd.read_csv(file_path)
    df['sentiment_score'] = df['cleaned_text'].apply(lambda x: sia.polarity_scores(x)['compound'])
    df.to_csv('data/sentiment_tweets.csv', index=False)

if __name__ == "__main__":
    analyze_sentiment('data/processed_tweets.csv')
