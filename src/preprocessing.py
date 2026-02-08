import pandas as pd
from textblob import TextBlob
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def analyze_sentiment(text):
    """
    Returns the polarity score of the text using TextBlob.
    Score ranges from -1 (Negative) to 1 (Positive).
    """
    return TextBlob(str(text)).sentiment.polarity

def preprocess_and_merge(price_df, news_df):
    """
    Merges price and news data, applies sentiment analysis, 
    and normalizes features.
    """
    # Ensure Date format consistency
    price_df['Date'] = pd.to_datetime(price_df['Date'])
    news_df['Date'] = pd.to_datetime(news_df['Date'])
    
    # Analyze sentiment
    print("Calculating sentiment scores...")
    news_df['Sentiment_Score'] = news_df['Headline'].apply(analyze_sentiment)
    
    # Merge datasets
    merged = pd.merge(price_df, news_df, on='Date', how='inner')
    
    # Feature Engineering: Moving Averages
    merged['MA7'] = merged['Close'].rolling(window=7).mean()
    merged['MA30'] = merged['Close'].rolling(window=30).mean()
    
    # Handle NaN values created by rolling windows
    merged.dropna(inplace=True)
    
    return merged

def prepare_lstm_data(data, lookback=60, target_col='Close'):
    """
    Prepares data for LSTM model (X=window, y=target).
    Input data should be a numpy array or dataframe.
    """
    X, y = [], []
    for i in range(lookback, len(data)):
        X.append(data[i-lookback:i])
        y.append(data[i, 0]) # Assuming target_col is at index 0 after scaling
        
    return np.array(X), np.array(y)

if __name__ == "__main__":
    from data_loader import fetch_crypto_data, fetch_news_data
    
    price = fetch_crypto_data()
    news = fetch_news_data()
    processed = preprocess_and_merge(price, news)
    
    print(f"Processed Data: {processed.shape}")
    print(processed.head())
