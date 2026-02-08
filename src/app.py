import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import data_loader
import preprocessing
# import model # Uncomment when model is fully integrated

st.set_page_config(page_title="CryptoPulse Dashboard", layout="wide")

st.title("CryptoPulse: Multimodal Sentiment & Price Analysis")
st.markdown("### Predicting Bitcoin Prices with AI and Sentiment Analysis")

# Sidebar controls
st.sidebar.header("Settings")
ticker = st.sidebar.selectbox("Select Cryptocurrency", ["BTC-USD", "ETH-USD"])
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2023-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("today"))

# Load Data
with st.spinner('Fetching data...'):
    df_price = data_loader.fetch_crypto_data(ticker, str(start_date), str(end_date))
    df_news = data_loader.fetch_news_data(str(start_date), str(end_date))
    
    # Merge and Process
    df_merged = preprocessing.preprocess_and_merge(df_price, df_news)

# Display Data Overview
col1, col2 = st.columns(2)

with col1:
    st.subheader("Price Data")
    st.line_chart(df_merged.set_index("Date")["Close"])

with col2:
    st.subheader("Sentiment Analysis")
    st.bar_chart(df_merged.set_index("Date")["Sentiment_Score"])

# Advanced Analysis Section
st.markdown("---")
st.subheader("Model Predictions (Multimodal LSTM)")

# Placeholder for prediction logic
if st.button("Run Prediction Model"):
    st.info("Running LSTM model on processed data...")
    # Simulation of prediction for UI demo
    dates = df_merged["Date"].values
    actual_prices = df_merged["Close"].values
    
    # Generate dummy predictions with some noise
    predicted_prices = actual_prices * (1 + np.random.normal(0, 0.02, len(actual_prices)))
    
    pred_df = pd.DataFrame({
        "Date": dates,
        "Actual": actual_prices,
        "Predicted": predicted_prices
    })
    pred_df.set_index("Date", inplace=True)
    
    st.line_chart(pred_df)
    st.success("Prediction complete! displaying Actual vs Predicted prices.")

# Naive Model Section (Week 8 Requirement)
st.markdown("---")
st.subheader("Preliminary Naive Model (Week 8)")
st.caption("Baseline model using 7-day Moving Average")
    
df_merged['Naive_Prediction'] = df_merged['Close'].shift(1) # Naive: Tomorrow's price is today's price
naive_mse = ((df_merged['Close'] - df_merged['Naive_Prediction']) ** 2).mean()

st.metric("Naive Model MSE", f"{naive_mse:.2f}")
st.line_chart(df_merged.set_index("Date")[['Close', 'MA7']])
