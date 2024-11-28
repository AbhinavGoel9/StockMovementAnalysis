# Stock Movement Analysis Based on Social Media Sentiment

## **Overview**
This project predicts stock price movements by analyzing social media sentiment. Using machine learning and natural language processing (NLP), the system scrapes real-time data from platforms like Twitter, preprocesses the data, performs sentiment analysis, and forecasts potential stock movements.

The project is divided into three main components:
1. **Data Scraping:** Collecting social media discussions related to the stock market.
2. **Sentiment Analysis:** Deriving sentiment polarity (positive, neutral, negative) from user-generated content.
3. **Stock Movement Prediction:** Using sentiment data to predict whether a stock will move up or down.

---

## **Repository Structure**
```plaintext
StockMovementAnalysis/
├── data/               # Folder for raw and processed data
├── models/             # Folder to save trained machine learning models
├── notebooks/          # Jupyter notebooks for interactive demonstrations
├── scripts/            # Python scripts for automation
├── outputs/            # Folder for generated results and visualizations
├── README.md           # Project instructions (this file)
├── requirements.txt    # Python dependencies for the project
├── report.pdf          # Detailed report on the project workflow and results
└── main.py             # Main script to run the project
```

---

## **Features**
- Scrape stock-related social media data from **Twitter**.
- Perform **sentiment analysis** using VADER (Valence Aware Dictionary for Sentiment Reasoning).
- Train and evaluate a machine learning model to predict stock price movement based on sentiment data.

---

## **Setup Instructions**

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/your-username/StockMovementAnalysis.git
cd StockMovementAnalysis
```

### **Step 2: Install Dependencies**
Ensure you have Python 3.8+ installed. Install the required libraries:
```bash
pip install -r requirements.txt
```

### **Step 3: Add API Keys**
For Twitter scraping, replace placeholders in `scripts/scraper.py` with your API credentials:
```python
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_SECRET = "your_access_secret"
```

### **Step 4: Run the Project**
You can run the project in two ways:
1. **Using the Main Script:**
   ```bash
   python main.py
   ```
   This will execute the full pipeline: data scraping → preprocessing → sentiment analysis → model training and evaluation.

2. **Using Jupyter Notebooks:**
   Navigate to the `notebooks/` directory and explore individual steps interactively:
   - `scraping.ipynb`
   - `preprocessing.ipynb`
   - `sentiment_analysis.ipynb`
   - `model_training.ipynb`

---

## **Key Components**

### **1. Data Scraping**
- Scrapes tweets from stock-related Twitter accounts using the Tweepy API.
- Outputs raw data to `data/raw_tweets.csv`.

### **2. Data Preprocessing**
- Cleans the scraped data by removing:
  - URLs, hashtags, mentions, and special characters.
  - Stopwords to focus on meaningful words.
- Saves processed data to `data/processed_tweets.csv`.

### **3. Sentiment Analysis**
- Performs sentiment analysis using the VADER sentiment analyzer.
- Adds a sentiment score column (`sentiment_score`) to the dataset.
- Outputs sentiment-analyzed data to `data/sentiment_tweets.csv`.

### **4. Stock Movement Prediction**
- Trains a Random Forest Classifier on sentiment scores.
- Labels stocks as:
  - `1` (Up) if the sentiment is positive.
  - `0` (Down) if the sentiment is negative or neutral.
- Outputs the trained model to `models/stock_predictor.pkl`.

---

## **Outputs**
- **Visualizations:**
  - Sentiment distribution charts.
  - Confusion matrix and classification reports for model evaluation.
- **Evaluation Metrics:**
  - Accuracy, precision, recall, F1-score.

---

## **File Descriptions**

| **File/Folder**     | **Description**                                                                                   |
|----------------------|---------------------------------------------------------------------------------------------------|
| `data/`             | Stores raw, processed, and sentiment-analyzed datasets.                                           |
| `models/`           | Stores trained machine learning models.                                                          |
| `notebooks/`        | Contains Jupyter notebooks for scraping, preprocessing, sentiment analysis, and model training.   |
| `scripts/`          | Contains Python scripts (`scraper.py`, `preprocess.py`, `sentiment_analysis.py`, `train_model.py`).|
| `outputs/`          | Stores visualizations and results generated during analysis.                                      |
| `requirements.txt`  | Lists all Python dependencies required for the project.                                           |
| `main.py`           | The main script to automate the entire workflow.                                                 |
| `report.pdf`        | PDF report documenting the project’s workflow, challenges, and results.                          |

---

## **Evaluation Metrics**
The model is evaluated using:
- **Accuracy:** Percentage of correct predictions.
- **Precision:** Correct positive predictions divided by total positive predictions.
- **Recall:** Correct positive predictions divided by actual positives.
- **F1-Score:** Harmonic mean of precision and recall.

---

## **Future Scope**
- Integrate additional data sources like Reddit (via PRAW) and Telegram (via Telethon).
- Use advanced NLP models (e.g., Transformers) for better sentiment understanding.
- Incorporate historical stock price data to enhance predictions.
- Develop a web app for real-time predictions.


```
