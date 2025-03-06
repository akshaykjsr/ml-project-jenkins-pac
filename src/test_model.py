import pickle
import numpy as np

# Load Trained Model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Generate Test Data
X_test = np.random.rand(5, 5)

# Predict Using Model
predictions = model.predict(X_test)
print("✅ Model Integration Test Passed. Predictions:", predictions)
