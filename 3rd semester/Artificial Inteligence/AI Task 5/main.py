
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data

df = pd.read_csv('airline-passengers.csv')
timeseries = np.array(df['Passengers'], dtype=np.float32)

train_size = int(len(timeseries) * 0.67)
test_size = len(timeseries) - train_size
train, test = timeseries[:train_size], timeseries[train_size:]


def create_dataset(dataset, lookback):
    X, y = [], []
    for i in range(len(dataset) - lookback):
        feature = dataset[i:i + lookback]
        target = dataset[i + 1:i + lookback + 1]
        X.append(feature)
        y.append(target)
    X = np.array(X)
    y = np.array(y)
    return torch.tensor(X), torch.tensor(y)


lookback = 4
X_train, y_train = create_dataset(train, lookback=lookback)
X_test, y_test = create_dataset(test, lookback=lookback)


class AirModel(nn.Module):
    def __init__(self, hidden_size, num_layers):
        super().__init__()
        self.lstm = nn.LSTM(input_size=1, hidden_size=hidden_size, num_layers=num_layers, batch_first=True)
        self.linear = nn.Linear(hidden_size, 6)
        self.linear1 = nn.Linear(6, 1)

    def forward(self, x):
        x, _ = self.lstm(x)
        x = self.linear(x)
        x = self.linear1(x)
        return x


# hyperparameters
batch_size = 6
hidden_size = 18
num_layers = 1
learning_rate = 0.001
n_epochs = 1500

model = AirModel(hidden_size, num_layers)
optimizer = optim.Adam(model.parameters(), lr=learning_rate)
loss_fn = nn.MSELoss()
loader = data.DataLoader(data.TensorDataset(X_train, y_train), shuffle=True, batch_size=batch_size)

for epoch in range(n_epochs):
    model.train()
    for X_batch, y_batch in loader:
        n1, n2 = X_batch.shape
        X_batch = X_batch.view(n1, n2, 1)
        y_pred = model(X_batch)
        y_pred = y_pred.view(n1, n2)
        loss = loss_fn(y_pred, y_batch)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    if epoch % 100 != 0:
        continue
    model.eval()
    with torch.no_grad():
        X_batch = X_train
        n1, n2 = X_batch.shape
        X_batch = X_batch.view(n1, n2, 1)
        y_pred = model(X_batch)
        y_pred = y_pred.view(n1, n2)
        train_rmse = np.sqrt(loss_fn(y_pred, y_train))
        X_batch = X_test
        n1, n2 = X_batch.shape
        X_batch = X_batch.view(n1, n2, 1)
        y_pred = model(X_batch)
        y_pred = y_pred.view(n1, n2)
        test_rmse = np.sqrt(loss_fn(y_pred, y_test))
    print("Epoch %d: train RMSE %.4f, test RMSE %.4f" % (epoch, train_rmse, test_rmse))

with torch.no_grad():
    X_batch = X_test
    n1, n2 = X_batch.shape
    X_batch = X_batch.view(n1, n2, 1)
    y_pred = model(X_batch)
    y_pred = y_pred.view(n1, n2)

y_true = test[4:]
yp1 = y_pred.cpu().numpy()[:, -1]

plt.figure(1)
plt.plot(y_true, 'r')
plt.plot(yp1, 'b')
plt.show()

