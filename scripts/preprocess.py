import pandas as pd
import re
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)  # Remove URLs
    text = re.sub(r'\@\w+|\#','', text)  # Remove mentions and hashtags
    text = re.sub(r'[^A-Za-z0-9\s]', '', text)  # Remove special characters
    text = text.lower()
    text = " ".join([word for word in text.split() if word not in stop_words])
    return text

def preprocess_data(file_path):
    df = pd.read_csv(file_path)
    df['cleaned_text'] = df['text'].apply(clean_text)
    df.to_csv('data/processed_tweets.csv', index=False)

if __name__ == "__main__":
    preprocess_data('data/raw_tweets.csv')
