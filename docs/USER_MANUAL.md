# 📘 CryptoPulse: User Manual

## 1. Getting Started

### Prerequisites
Ensure you have Python 3.8+ installed.

### Installation
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/nizamkadirteach/cdsproject.git
    cd cdsproject
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Launching the App
Run the following command in your terminal:
```bash
streamlit run src/app.py
```
A browser window will automatically open at `http://localhost:8501`.

---

## 2. Dashboard Features

### 🏠 Sidebar Controls
- **Asset Ticker:** Choose between BTC, ETH, SOL, or XRP.
- **Date Range:** Select the historical period for analysis.
- **Data Streams:** Toggle the "Fear & Greed Index" on/off.
- **Indicators:** Enable/Disable Moving Averages (MA7, MA30) and Bollinger Bands.

### 📉 Tab 1: Technical Analysis
- **Main Chart:** Interactive candlestick chart. Use your mouse to zoom, pan, or hover for specific price details.
- **Volume & Sentiment:** Lower chart showing trading volume overlaid with the Fear & Greed Index (Yellow Line).

### 🔮 Tab 2: AI Forecast
- **Neural Engine:** Displays the model's confidence logic.
- **Forecast Slider:** Choose how many days into the future to predict (1-30 days).
- **Generate Prediction:** Click to run the LSTM model inference.

### 💾 Tab 3: Data Export
- **Download CSV:** Click the button to download the fully processed dataset (Prices + Sentiment + Indicators) for your own Excel/Python analysis.

---

## 3. Data Management
If you need to regenerate the raw data files:
1.  Open your terminal in the project root.
2.  Run: `python src/save_data.py`
3.  Check the `data/` folder for fresh CSVs.

---

## 4. Troubleshooting
- **"No Market Data Found":** Check your internet connection (Yahoo Finance API requires it).
- **App Crashing:** Run `pip install -r requirements.txt` again to ensure all libraries are up to date.
