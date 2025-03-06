import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

# Generate synthetic dataset
X, y = make_classification(n_samples=100, n_features=5, random_state=42)

# Train Logistic Regression Model
model = LogisticRegression()
model.fit(X, y)

# Save Model to File
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model training completed. Saved as model.pkl")
