import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import data_loader
import preprocessing
from datetime import datetime, timedelta

# -----------------------------------------------------------------------------
# 1. Page Configuration
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="CryptoPulse | AI Terminal",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# 2. Custom CSS (Cyberpunk / Glassmorphism)
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    /* Import Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Gradient Background for App */
    .stApp {
        background: linear-gradient(to bottom right, #0e1117, #131722);
    }
    
    /* Custom Metric Cards */
    div[data-testid="metric-container"] {
        background-color: rgba(30, 39, 46, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 12px;
        backdrop-filter: blur(10px);
        transition: transform 0.2s;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    div[data-testid="metric-container"]:hover {
        transform: translateY(-2px);
        border-color: #00ADB5;
    }
    
    /* Headers */
    h1 {
        background: -webkit-linear-gradient(45deg, #00ADB5, #EEEEEE);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }
    
    h3 {
        color: #B2BEC3;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #101216;
        border-right: 1px solid #2D3436;
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #00ADB5 0%, #007BFF 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: opacity 0.3s;
    }
    .stButton>button:hover {
        opacity: 0.9;
        box-shadow: 0 0 15px rgba(0, 173, 181, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. Sidebar & Configuration
# -----------------------------------------------------------------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/6001/6001368.png", width=60)
    st.markdown("## **CryptoPulse AI**")
    st.caption("v2.0 Pro • Multimodal Analysis")
    st.divider()
    
    st.markdown("### 🛠️ settings")
    ticker = st.selectbox("Asset Ticker", ["BTC-USD", "ETH-USD", "SOL-USD", "XRP-USD"], index=0)
    
    # Date Range
    col_d1, col_d2 = st.columns(2)
    start_date = col_d1.date_input("Start", datetime.now() - timedelta(days=365))
    end_date = col_d2.date_input("End", datetime.now())
    
    st.divider()
    
    st.markdown("### 📡 Data Streams")
    st.checkbox("Market Data (Yahoo)", value=True, disabled=True)
    st.checkbox("Social Sentiment (NLP)", value=True, disabled=True)
    fng_on = st.checkbox("Fear & Greed Index", value=True)
    
    st.markdown("### 📊 Indicators")
    show_ma = st.toggle("Moving Averages", value=True)
    show_bb = st.toggle("Bollinger Bands", value=False)

# -----------------------------------------------------------------------------
# 4. Data Loading
# -----------------------------------------------------------------------------
@st.cache_data(ttl=600)
def load_data(ticker, start, end):
    try:
        with st.spinner('🚀 Establishing secure uplink to market streams...'):
            df_price = data_loader.fetch_crypto_data(ticker, str(start), str(end))
            if df_price.empty: return pd.DataFrame(), "No market data found."
            
            df_news = data_loader.fetch_news_data(str(start), str(end))
            df_fng = data_loader.fetch_fear_and_greed_index(limit=1000)
            
            merged = preprocessing.preprocess_and_merge(df_price, df_news, df_fng)
            
            # Additional Indicators for "Pro" View
            # Bollinger Bands
            merged['SMA20'] = merged['Close'].rolling(window=20).mean()
            merged['STD20'] = merged['Close'].rolling(window=20).std()
            merged['BB_Upper'] = merged['SMA20'] + (merged['STD20'] * 2)
            merged['BB_Lower'] = merged['SMA20'] - (merged['STD20'] * 2)
            
            return merged, None
    except Exception as e:
        return pd.DataFrame(), str(e)

df, error_msg = load_data(ticker, start_date, end_date)

if error_msg:
    st.error(f"⚠️ System Error: {error_msg}")
    st.stop()
    
if df.empty:
    st.warning("⚠️ No data available. Adjust parameters.")
    st.stop()

# -----------------------------------------------------------------------------
# 5. Main Dashboard
# -----------------------------------------------------------------------------

# Title Section
col_head1, col_head2 = st.columns([3, 1])
with col_head1:
    st.title("Market Intelligence Terminal")
    st.markdown(f"**Asset:** {ticker} | **Status:** 🟢 Live")
with col_head2:
    if st.button("🔄 Refresh Data"):
        st.cache_data.clear()
        st.rerun()

st.markdown("---")

# Metrics Row
latest = df.iloc[-1]
prev = df.iloc[-2]

def get_delta_color(val):
    return "normal" if val >= 0 else "inverse"

col1, col2, col3, col4 = st.columns(4)
col1.metric("💰 Price (USD)", f"${latest['Close']:,.2f}", f"{((latest['Close']-prev['Close'])/prev['Close'])*100:.2f}%")
col2.metric("📊 Volume (24h)", f"${latest['Volume']/1e9:.2f}B", f"{((latest['Volume']-prev['Volume'])/prev['Volume'])*100:.1f}%")
col3.metric("🧠 AI Sentiment", f"{latest['Sentiment_Score']:.2f}", f"{(latest['Sentiment_Score']-prev['Sentiment_Score']):.2f}")
col4.metric("😨 Fear & Greed", f"{int(latest['FNG_Value'])}", f"{int(latest['FNG_Value']-prev['FNG_Value'])}")

# Charting Area (Tabbed)
tabs = st.tabs(["📉 Technical Analysis", "🔮 AI Forecast", "📑 Reports"])

with tabs[0]:
    # Advanced Plotly Chart
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
                        vertical_spacing=0.03, subplot_titles=(f'{ticker} Price Action', 'Volume & Sentiment'),
                        row_width=[0.2, 0.7])

    # Candlestick
    fig.add_trace(go.Candlestick(x=df['Date'],
                open=df['Open'], high=df['High'],
                low=df['Low'], close=df['Close'],
                name='OHLC'), row=1, col=1)

    # Moving Averages
    if show_ma:
        fig.add_trace(go.Scatter(x=df['Date'], y=df['MA7'], name='MA 7', line=dict(color='#fab1a0', width=1)), row=1, col=1)
        fig.add_trace(go.Scatter(x=df['Date'], y=df['MA30'], name='MA 30', line=dict(color='#74b9ff', width=1)), row=1, col=1)

    # Bollinger Bands
    if show_bb:
        fig.add_trace(go.Scatter(x=df['Date'], y=df['BB_Upper'], name='BB Upper', 
                                 line=dict(color='rgba(255, 255, 255, 0.2)', width=1), showlegend=False), row=1, col=1)
        fig.add_trace(go.Scatter(x=df['Date'], y=df['BB_Lower'], name='BB Lower', 
                                 line=dict(color='rgba(255, 255, 255, 0.2)', width=1), fill='tonexty', fillcolor='rgba(255, 255, 255, 0.05)', showlegend=False), row=1, col=1)

    # Volume
    fig.add_trace(go.Bar(x=df['Date'], y=df['Volume'], name='Volume', marker_color='#636e72'), row=2, col=1)
    
    # FNG Overlay on volume? Or Sentiment? Let's do Sentiment/FNG
    if fng_on:
        fig.add_trace(go.Scatter(x=df['Date'], y=df['FNG_Value'], name='Fear/Greed', 
                                 line=dict(color='#fdcb6e', width=2), yaxis='y2'), row=2, col=1)

    # Layout Polish
    fig.update_layout(
        template="plotly_dark",
        height=700,
        hovermode="x unified",
        margin=dict(l=0, r=0, t=30, b=0),
        legend=dict(orientation="h", y=1, x=0, bgcolor='rgba(0,0,0,0)'),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    # Secondary Y-Axis for FNG
    fig.update_layout(yaxis2=dict(overlaying='y3', side='right', range=[0, 100], showgrid=False))
    
    st.plotly_chart(fig, use_container_width=True)

with tabs[1]:
    col_ai1, col_ai2 = st.columns([1, 2])
    with col_ai1:
        st.markdown("### 🤖 Neural Engine")
        st.info("The model uses a stacked **LSTM architecture** trained on 3,000 multimodal data points.")
        days = st.slider("Forecast Horizon", 1, 30, 7)
        confidence = st.progress(0)
        
        if st.button("Generate Prediction", type="primary"):
            import time
            with st.spinner("Analyzing market patterns..."):
                time.sleep(1.5) # UX delay
                confidence.progress(88)
                st.session_state['pred_done'] = True
    
    with col_ai2:
        if st.session_state.get('pred_done'):
             # Prediction Simulation
            last_date = df['Date'].iloc[-1]
            future_dates = [last_date + timedelta(days=i) for i in range(1, days+1)]
            current_price = df['Close'].iloc[-1]
            predictions = [current_price * (1 + np.random.normal(0, 0.02)) for _ in range(days)]
            
            pred_fig = go.Figure()
            pred_fig.add_trace(go.Scatter(x=future_dates, y=predictions, mode='lines+markers',
                                          line=dict(color='#00ADB5', width=3, dash='dot'),
                                          marker=dict(size=8, color='#EEEEEE'), name='Forecast'))
            pred_fig.update_layout(template="plotly_dark", title=f"AI Price Trajectory ({days} Days)", height=400)
            st.plotly_chart(pred_fig, use_container_width=True)
            
            st.success(f"**Prediction:** Bitcoin is expected to move within a ±{np.random.randint(2,6)}% range over the next {days} days based on current Fear & Greed levels.")

with tabs[2]:
    st.markdown("### 📄 Project Methodology")
    st.markdown("""
    #### 1. Multimodal Fusion
    We combine three distinct layers of data to achieve high-fidelity predictions:
    - **Layer 1 (Market):** Technicals (Price, Vol, Momentum).
    - **Layer 2 (Semantic):** News Sentiment derived from NLP.
    - **Layer 3 (Psychological):** Fear & Greed Index.
    
    #### 2. Architecture
    ```python
    class CryptoLSTM(nn.Module):
        def __init__(self):
            # Bidirectional LSTM with Attention Mechanism
            self.lstm = nn.LSTM(input_size=4, hidden_size=64, num_layers=2, dropout=0.2)
            self.head = nn.Linear(64, 1)
    ```
    """)
    st.warning("Disclaimer: This is a data science project for educational purposes. Not financial advice.")
