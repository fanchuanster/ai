import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.pytorch
import pandas as pd
import numpy as np

# Set experiment (or use default)
mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("PyTorchIris")

# Define simple PyTorch model
class IrisNet(nn.Module):
    def __init__(self):
        super(IrisNet, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(4, 16),
            nn.ReLU(),
            nn.Linear(16, 3)
        )

    def forward(self, x):
        return self.net(x)

# Load and preprocess data
iris = load_iris()
X = StandardScaler().fit_transform(iris.data)
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.long)

# Start MLflow run
with mlflow.start_run():
    model = IrisNet()
    loss_fn = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)

    mlflow.log_param("lr", 0.01)
    mlflow.log_param("epochs", 50)

    # Training loop
    for epoch in range(50):
        optimizer.zero_grad()
        outputs = model(X_train_tensor)
        loss = loss_fn(outputs, y_train_tensor)
        loss.backward()
        optimizer.step()

        mlflow.log_metric("loss", loss.item(), step=epoch)

    # Evaluation
    X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
    preds = torch.argmax(model(X_test_tensor), dim=1).numpy()
    acc = accuracy_score(y_test, preds)
    mlflow.log_metric("test_accuracy", acc)

    # Log model
    mlflow.pytorch.log_model(model, "model")

    print(f"Test Accuracy: {acc}")
