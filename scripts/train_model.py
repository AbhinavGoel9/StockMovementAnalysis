import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def train_model(file_path):
    df = pd.read_csv(file_path)
    df['movement'] = df['sentiment_score'].apply(lambda x: 1 if x > 0 else 0)  # Binary classification: Up (1), Down (0)
    
    X = df['sentiment_score'].values.reshape(-1, 1)
    y = df['movement']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    print(classification_report(y_test, y_pred))

    return model

if __name__ == "__main__":
    train_model('data/sentiment_tweets.csv')
