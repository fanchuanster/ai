import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
import sys

mlflow.set_tracking_uri("http://127.0.0.1:5000")
# mlflow.set_tracking_uri("file:///C:/Users/donwen/Desktop/tm/ai/mlflow/mlruns")

# Set experiment name to organize runs
mlflow.set_experiment("IrisClassifierExperiment")

# Get max_iter from CLI args
max_iter = int(sys.argv[1]) if len(sys.argv) > 1 else 100

# Load data
X, y = load_iris(return_X_y=True)
model = LogisticRegression(max_iter=max_iter)
model.fit(X, y)

# Predict and calculate accuracy
predictions = model.predict(X)
accuracy = accuracy_score(y, predictions)

# Log parameters, metrics, and model (MLflow run is already active)
mlflow.log_param("max_iter", max_iter)
mlflow.log_metric("accuracy", accuracy)
mlflow.sklearn.log_model(model, "iris_model")

print(f"Logged run with accuracy: {accuracy}")
