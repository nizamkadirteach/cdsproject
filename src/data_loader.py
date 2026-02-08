import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def fetch_crypto_data(ticker="BTC-USD", start_date="2020-01-01", end_date=None):
    """
    Fetches historical OHLCV data from Yahoo Finance.
    """
    if end_date is None:
        end_date = datetime.now().strftime("%Y-%m-%d")
    
    print(f"Fetching {ticker} data from {start_date} to {end_date}...")
    data = yf.download(ticker, start=start_date, end=end_date)
    
    # Flatten multi-index columns if present (yfinance update)
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)
    
    data.reset_index(inplace=True)
    return data

def fetch_news_data(start_date="2020-01-01", end_date=None):
    """
    Simulates fetching news headlines for demonstration purposes.
    In a real scenario, this would hit NewsAPI or similar.
    Returns a DataFrame with 'Date' and 'Headline'.
    """
    if end_date is None:
        end_date = datetime.now().strftime("%Y-%m-%d")
        
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    date_range = pd.date_range(start, end)
    
    # Mock headlines for simulation
    bullish_templates = [
        "Bitcoin hits new all-time high!",
        "Institutional investors flocking to crypto.",
        "Regulatory approval for Bitcoin ETF imminent.",
        "Tech giant announces crypto integration.",
        "Crypto market sees massive gains."
    ]
    bearish_templates = [
        "Bitcoin crashes below support levels.",
        "Government announces strict crypto ban.",
        "Major exchange hacked, funds stolen.",
        "Experts warn of crypto bubble bursting.",
        "Market sentiment turns negative on inflation fears."
    ]
    neutral_templates = [
        "Bitcoin stable around current levels.",
        "Analysts discuss future of blockchain.",
        "Crypto conference scheduled for next week.",
        "New updates released for Ethereum network.",
        "Trading volume remains average today."
    ]
    
    headlines = []
    dates = []
    
    for date in date_range:
        # Randomly assign a sentiment bias to the day
        daily_sentiment = np.random.choice(['bull', 'bear', 'neutral'], p=[0.4, 0.3, 0.3])
        
        if daily_sentiment == 'bull':
            daily_headline = np.random.choice(bullish_templates)
        elif daily_sentiment == 'bear':
            daily_headline = np.random.choice(bearish_templates)
        else:
            daily_headline = np.random.choice(neutral_templates)
            
        dates.append(date)
        headlines.append(daily_headline)
        
    return pd.DataFrame({'Date': dates, 'Headline': headlines})

if __name__ == "__main__":
    # Test the functions
    df_price = fetch_crypto_data()
    print(f"Price Data: {df_price.shape}")
    print(df_price.head())
    
    df_news = fetch_news_data()
    print(f"News Data: {df_news.shape}")
    print(df_news.head())
