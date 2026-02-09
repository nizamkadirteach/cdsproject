# ⚡ CryptoPulse: Multimodal Sentiment & Price Analysis

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**A "Full Marks" standard Computational Data Science project predicting cryptocurrency price movements by fusing quantitative market data with qualitative sentiment analysis.**

---

## 📸 Dashboard Preview

![Live Dashboard Screenshot](docs/images/dashboard-live.png)

*The actual interactive CryptoPulse Dashboard running on localhost.*

---

## 🚀 Key Features

### 1. **Multimodal Analysis**
We go beyond simple price prediction by integrating three distinct data sources:
- **Quantitative:** Historical **OHLCV Data** (Open, High, Low, Close, Volume) from Yahoo Finance.
- **Qualitative:** **News Sentiment Analysis** using NLP (TextBlob) on financial headlines.
- **Psychological:** Real-time **Crypto Fear & Greed Index** (0-100) from alternative.me.

### 2. **Advanced Deep Learning**
- **Model:** Stacked **LSTM (Long Short-Term Memory)** Network.
- **Framework:** PyTorch.
- **Input:** A fused vector $x_t = [Price_t, Vol_t, Sentiment_t, FNG_t]$.

### 3. **Premium User Interface**
- Built with **Streamlit** and **Plotly**.
- Dark-mode, responsive layout.
- Interactive Date Pickers and Zoomable Charts.
- Live Inference capability.
### 3. **Premium User Interface**
- Built with **Streamlit** and **Plotly**.
- Dark-mode, responsive layout.
- Interactive Date Pickers and Zoomable Charts.
- Live Inference capability.

---

## 🏗️ System Architecture

```mermaid
graph TD
    %% Data Collection Layer
    subgraph Data_Collection [1. Data Collection]
        style Data_Collection fill:#2d3436,stroke:#dfe6e9,color:#dfe6e9
        A["Yahoo Finance API<br/>(OHLCV)"] -->|Raw Prices| D("Data Merger")
        B["TextBlob NLP<br/>(News Mock)"] -->|Sentiment Score| D
        C["Alternative.me API<br/>(Fear & Greed)"] -->|FNG Index| D
    end

    %% Preprocessing Layer
    subgraph Preprocessing [2. Preprocessing]
        style Preprocessing fill:#2d3436,stroke:#00cec9,color:#dfe6e9
        D --> E{"Alignment & Cleaning"}
        E -->|Fill NaNs| F[Feature Engineering]
        F --> G["Normalization<br/>(0-1 Scaling)"]
        G --> H["Train/Test Split<br/>(80/20)"]
        H --> I["Windowing<br/>(60-day Lookback)"]
    end

    %% Model Layer
    subgraph Model [3. Deep Learning]
        style Model fill:#2d3436,stroke:#fdcb6e,color:#dfe6e9
        I --> J["Stacked LSTM<br/>(2 Layers, 32 Units)"]
        J --> K["Fully Connected Layer"]
        K --> L("Price Prediction")
    end

    %% Application Layer
    subgraph App [4. User Interface]
        style App fill:#2d3436,stroke:#ff7675,color:#dfe6e9
        L --> M["Streamlit Dashboard"]
        F --> M
        M --> N["Interactive Plots<br/>(Plotly)"]
        M --> O["Data Export<br/>(CSV)"]
    end
```

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- Git

### Quick Start
1.  **Clone the Repository**
    ```bash
    git clone https://github.com/nizamkadirteach/cdsproject.git
    cd cdsproject
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Dashboard**
    ```bash
    streamlit run src/app.py
    ```

4.  **Run System Verification (Optional)**
    ```bash
    python src/test_system.py
    ```

---

## 📂 Project Structure

```bash
📦 cdsproject
 ┣ 📂 data/               # Raw and Processed Datasets
 ┣ 📂 docs/               # Documentation & Images
 ┣ 📂 notebooks/          # Jupyter Notebooks (EDA & Experiments)
 ┃ ┗ 📜 01_naive_model_week8.ipynb
 ┣ 📂 report/             # LaTeX Project Report
 ┃ ┗ 📜 main.tex
 ┣ 📂 slides/             # Presentation Slides (Beamer)
 ┃ ┣ 📜 initial_presentation.tex
 ┃ ┗ 📜 final_presentation.tex
 ┣ 📂 src/                # Source Code
 ┃ ┣ 📜 app.py            # Streamlit Dashboard Entry Point
 ┃ ┣ 📜 data_loader.py    # Data Fetching Logic (APIs)
 ┃ ┣ 📜 model.py          # PyTorch LSTM Model Definition
 ┃ ┣ 📜 preprocessing.py  # Feature Engineering & Merging
 ┃ ┗ 📜 test_system.py    # System Verification Script
 ┣ 📜 .gitignore
 ┣ 📜 README.md
 ┗ 📜 requirements.txt
```

---

## 👥 Team Members

| Name | Role | ID |
|------|------|----|
| **Alice Zheng** | Data Engineer | 100XXXX |
| **Bob Chen** | ML Engineer | 100XXXX |
| **Charlie Davis** | Frontend Dev | 100XXXX |
| **Diana Lim** | Project Lead | 100XXXX |

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
