# Model Card: CryptoPulse LSTM

## Model Details
- **Name:** CryptoPulse Multimodal Predictor
- **Version:** 2.0
- **Type:** Stacked Long Short-Term Memory (LSTM) Neural Network
- **Framework:** PyTorch
- **Date:** February 2026

## Intended Use
- **Primary Use Case:** Predicting the next day's closing price of Bitcoin (BTC-USD) based on historical market data and sentiment indices.
- **Intended Users:** Financial analysts, data scientists, and crypto enthusiasts.
- **Out of Scope:** High-frequency trading (HFT) or multi-asset portfolio optimization.

## Data Sources
The model consumes a multimodal feature vector $x_t$ consisting of:
1.  **Market Data:** OHLCV (Open, High, Low, Close, Volume) from Yahoo Finance.
2.  **Sentiment Data:** Polarity scores (-1 to +1) derived from simulated financial news headlines.
3.  **Psychological Data:** Fear & Greed Index (0-100) from Alternative.me API.

## Model Architecture
The system utilizes a Stacked LSTM architecture to capture temporal dependencies in the time-series data.

```python
class CryptoLSTM(nn.Module):
    def __init__(self):
        super(CryptoLSTM, self).__init__()
        # Layer 1 & 2: Stacked LSTM
        # Input Dim: 4 (Price, Vol, Sentiment, FNG)
        # Hidden Dim: 32
        # Layers: 2
        self.lstm = nn.LSTM(input_dim=4, hidden_dim=32, num_layers=2, batch_first=True)
        
        # Output Layer: Fully Connected
        self.fc = nn.Linear(32, 1)
```

## Training Procedure
- **Optimizer:** Adam (`torch.optim.Adam`)
- **Learning Rate:** 0.01
- **Loss Function:** Mean Squared Error (MSE)
- **Epochs:** 100
- **Batching:** Full-batch gradient descent (for stability on this dataset size).
- **Train/Test Split:** 80% Training / 20% Testing (Time-ordered split).

## Hyperparameters
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Lookback Window | 60 Days | Keras/PyTorch standard for capturing quarterly trends. |
| Hidden Units | 32 | Sufficient capacity without overfitting small datasets. |
| Dropout | 0.0 | Not applied (low complexity model). |
| Sequence Length | 60 | Matches lookback window. |

## Evaluation Results
- **Metric:** Mean Squared Error (MSE)
- **Performance:**
    - Baseline (Price Only): 0.042
    - **Multimodal (Price + FNG): 0.032**
- **Improvement:** ~24% reduction in error with sentiment integration.

## Limitations
- **Simulated News:** The current NLP component uses synthetic headlines for demonstration.
- **Stationarity:** The model assumes some degree of market stationarity which may not hold during black swan events.
