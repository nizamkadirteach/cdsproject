# CryptoPulse: Multimodal Sentiment & Price Analysis

## Project Overview
**CryptoPulse** is a comprehensive data science project designed to predict cryptocurrency price movements by integrating quantitative market data with qualitative sentiment analysis from news and social media.

## Project Description
Cryptocurrency markets are highly volatile and sensitive to public sentiment. This project leverages:
1.  **Market Data:** Historical OHLCV (Open, High, Low, Close, Volume) data for major cryptocurrencies (e.g., Bitcoin, Ethereum).
2.  **Sentiment Data:** Real-time analysis of news headlines and social media posts (e.g., Twitter/X, Reddit).
3.  **Multimodal Learning:** A deep learning model (LSTM/GRU) that fuses time-series data with sentiment embeddings to forecast price trends.

The project features an interactive **Web Dashboard** for real-time visualization and model inference.

## Team Members
1.  **Alice Zheng** (Student ID: 100XXXX)
2.  **Bob Chen** (Student ID: 100XXXX)
3.  **Charlie Davis** (Student ID: 100XXXX)
4.  **Diana Lim** (Student ID: 100XXXX)

## Directory Structure
- `data/`: Raw and processed datasets.
- `notebooks/`: EDA and model prototyping.
- `src/`: Source code for data pipelines, modeling, and the web app.
- `report/`: LaTeX source for the final project report.
- `slides/`: LaTeX Beamer source for presentations.

## Setup & Usage
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/nizamkadirteach/cdsproject.git
    cd cdsproject
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the Web App:**
    ```bash
    streamlit run src/app.py
    ```
