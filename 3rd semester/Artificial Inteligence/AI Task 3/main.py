    import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn import model_selection
from torch.utils.data import DataLoader, Dataset
import pandas as pd

input_size = 7
num_classes = 8
num_epochs = 50
batch_size = 4
learning_rate = 0.5

dataset = pd.read_table("data.txt", delimiter='\t', header=None)
dataset[8] = pd.factorize(dataset[8])[0]

X = dataset.iloc[:, 1:8].values
print(X)
y = dataset.iloc[:, 8:9].values
print(y)
y = y.ravel()


X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.15, random_state=0, shuffle=True, stratify=y)
X_train, X_val, y_train, y_val = model_selection.train_test_split(X_train, y_train, test_size=0.1, random_state=0, stratify=y_train)


class TestDataset(Dataset):
    def __init__(self, X, y):
        self.features = torch.tensor(X, dtype=torch.float32)
        self.labels = torch.tensor(y, dtype=torch.int64)

    def __getitem__(self, index):
        x = self.features[index]
        y = self.labels[index]
        return x, y

    def __len__(self):
        return self.labels.shape[0]


train_ds = TestDataset(X_train, y_train)
val_ds = TestDataset(X_val, y_val)
test_ds = TestDataset(X_test, y_test)

train_loader = DataLoader(
    dataset=train_ds,
    batch_size=batch_size,
    shuffle=True,
)

val_loader = DataLoader(
    dataset=val_ds,
    batch_size=batch_size,
    shuffle=False,
)

test_loader = DataLoader(
    dataset=test_ds,
    batch_size=batch_size,
    shuffle=False,
)


class ClassificationMLP(nn.Module):
    def __init__(self, input_size, num_classes):
        super().__init__()

        self.all_layers = torch.nn.Sequential(

            torch.nn.Linear(input_size, 16),
            torch.nn.ReLU(),

            torch.nn.Linear(16, num_classes),
            torch.nn.ReLU()
        )

    def forward(self, x):
        output = self.all_layers(x)
        return output


def compute_accuracy(model, dataloader):
    model = model.eval()

    correct = 0
    total_examples = 0

    for idx, (features, labels) in enumerate(dataloader):
        with torch.no_grad():
            output = model(features)

        predictions = torch.argmax(output, dim=1)

        compare = labels == predictions
        correct += torch.sum(compare)
        total_examples += len(compare)

    return correct / total_examples


model = ClassificationMLP(input_size, num_classes)
optimizer = torch.optim.SGD(model.parameters(), learning_rate)

for epoch in range(num_epochs):

    model = model.train()
    for batch_idx, (features, labels) in enumerate(train_loader):
        output = model(features)

        print(labels)
        loss = F.cross_entropy(output, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        print(f"Epoch: {epoch + 1:03d}/{num_epochs:03d}"
              f" | Batch {batch_idx:03d}/{len(train_loader):03d}"
              f" | Train/Val Loss: {loss:.2f}")

    train_acc = compute_accuracy(model, train_loader)
    val_acc = compute_accuracy(model, val_loader)
    print(f"Train Accuracy: {train_acc * 100}% | Value Accuracy: {val_acc * 100}%")

torch.save(model.state_dict(), 'model.ckpt')