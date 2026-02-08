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

def preprocess_and_merge(price_df, news_df, fng_df=None):
    """
    Merges price, news, and optional FNG data.
    """
    # Ensure Date format consistency
    price_df['Date'] = pd.to_datetime(price_df['Date'])
    news_df['Date'] = pd.to_datetime(news_df['Date'])
    
    # Analyze sentiment (simulated/news)
    # print("Calculating sentiment scores...")
    if 'Sentiment_Score' not in news_df.columns:
         news_df['Sentiment_Score'] = news_df['Headline'].apply(analyze_sentiment)
    
    # Merge Price and News
    merged = pd.merge(price_df, news_df[['Date', 'Sentiment_Score']], on='Date', how='inner')
    
    # Merge FNG if available
    if fng_df is not None and not fng_df.empty:
        fng_df['Date'] = pd.to_datetime(fng_df['Date'])
        merged = pd.merge(merged, fng_df[['Date', 'FNG_Value']], on='Date', how='inner')
    
    # Feature Engineering
    # Use min_periods=1 to allow calculation on smaller datasets (for testing/early data)
    merged['MA7'] = merged['Close'].rolling(window=7, min_periods=1).mean()
    merged['MA30'] = merged['Close'].rolling(window=30, min_periods=1).mean()
    
    # merged.dropna(inplace=True) # data might be scarce in testing
    # Only drop if critical features are missing
    merged.dropna(subset=['Close', 'Sentiment_Score'], inplace=True)
    
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
