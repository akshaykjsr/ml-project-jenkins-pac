import pickle
import numpy as np

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Generate test data
X_test = np.random.rand(5, 5)

# Predict
predictions = model.predict(X_test)
print("✅ Model Integration Test Passed. Predictions:", predictions)
