import os
import pandas as pd
from datetime import datetime
import data_loader
import preprocessing

def save_data():
    print("🚀 Starting Data Generation Process...")
    
    # 1. Undefine Paths
    RAW_DIR = "data/raw"
    PROC_DIR = "data/processed"
    
    os.makedirs(RAW_DIR, exist_ok=True)
    os.makedirs(PROC_DIR, exist_ok=True)
    
    # 2. Fetch Raw Data
    print("\n[1/3] Fetching Raw Data...")
    start_date = "2020-01-01"
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # Market Data
    df_price = data_loader.fetch_crypto_data("BTC-USD", start_date, end_date)
    price_path = f"{RAW_DIR}/btc_price.csv"
    df_price.to_csv(price_path, index=False)
    print(f"   - Saved Price Data: {price_path} ({len(df_price)} rows)")
    
    # News Data
    df_news = data_loader.fetch_news_data(start_date, end_date)
    news_path = f"{RAW_DIR}/news_sentiment.csv"
    df_news.to_csv(news_path, index=False)
    print(f"   - Saved News Data: {news_path} ({len(df_news)} rows)")
    
    # FNG Data
    df_fng = data_loader.fetch_fear_and_greed_index(limit=2000)
    fng_path = f"{RAW_DIR}/fear_greed_index.csv"
    df_fng.to_csv(fng_path, index=False)
    print(f"   - Saved FNG Data: {fng_path} ({len(df_fng)} rows)")
    
    # 3. Process and Merge
    print("\n[2/3] Processing & Merging Data...")
    processed_df = preprocessing.preprocess_and_merge(df_price, df_news, df_fng)
    
    # Add Technical Indicators (same as app.py)
    processed_df['SMA20'] = processed_df['Close'].rolling(window=20).mean()
    processed_df['STD20'] = processed_df['Close'].rolling(window=20).std()
    processed_df['BB_Upper'] = processed_df['SMA20'] + (processed_df['STD20'] * 2)
    processed_df['BB_Lower'] = processed_df['SMA20'] - (processed_df['STD20'] * 2)
    
    proc_path = f"{PROC_DIR}/multimodal_dataset_final.csv"
    processed_df.to_csv(proc_path, index=False)
    print(f"   - Saved Processed Data: {proc_path} ({len(processed_df)} rows)")
    
    print("\n✅ Data Generation Complete!")

if __name__ == "__main__":
    save_data()
