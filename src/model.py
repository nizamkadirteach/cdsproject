import torch
import torch.nn as nn
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from torch.utils.data import DataLoader, TensorDataset

class CryptoLSTM(nn.Module):
    def __init__(self, input_dim, hidden_dim, num_layers, output_dim):
        super(CryptoLSTM, self).__init__()
        self.hidden_dim = hidden_dim
        self.num_layers = num_layers
        
        self.lstm = nn.LSTM(input_dim, hidden_dim, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)
        
    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_dim).requires_grad_()
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_dim).requires_grad_()
        
        out, (hn, cn) = self.lstm(x, (h0.detach(), c0.detach()))
        out = self.fc(out[:, -1, :]) 
        return out

def train_model(X_train, y_train, input_dim=1, hidden_dim=32, num_layers=2, output_dim=1, epochs=100):
    model = CryptoLSTM(input_dim=input_dim, hidden_dim=hidden_dim, num_layers=num_layers, output_dim=output_dim)
    criterion = torch.nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    
    # Convert to Tensors
    X_train = torch.from_numpy(X_train).type(torch.Tensor)
    y_train = torch.from_numpy(y_train).type(torch.Tensor)
    
    hist = np.zeros(epochs)
    
    print("Training LSTM model...")
    for t in range(epochs):
        y_train_pred = model(X_train)
        
        loss = criterion(y_train_pred, y_train)
        hist[t] = loss.item()
        
        if t % 10 == 0:
            print(f"Epoch {t} MSE: {loss.item()}")
            
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
    return model, hist

if __name__ == "__main__":
    # Dummy test to ensure import works
    print("Model module loaded.")
