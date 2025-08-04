# train_and_save_model.py

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
import os

# Dummy dataset (replace with your real one if needed)
data = {
    'feature1': [0, 1, 2, 3, 4],
    'feature2': [5, 4, 3, 2, 1],
    'label': [0, 1, 0, 1, 0]
}
df = pd.DataFrame(data)

# Split features and labels
X = df[['feature1', 'feature2']]
y = df['label']

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model
model_path = os.path.join("app", "model.pkl")
joblib.dump(model, model_path)

print(f"Model saved to {model_path}")
