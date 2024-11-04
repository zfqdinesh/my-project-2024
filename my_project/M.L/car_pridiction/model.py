import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv('data.csv')

# Features and target variable
X = df[['Top Speed (km/h)', 'Engine Power (HP)', 'Price']]
y = df['Car Name']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'car_model.pkl')

print("Model trained and saved.")
