import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from joblib import dump

# Step 1: Load dataset
data = pd.read_csv('crop_data.csv')  # This is your renamed Kaggle CSV file

# Step 2: Split into features and label
X = data.drop('label', axis=1)
y = data['label']

# Step 3: Split into training/testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the RandomForest model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Step 5: Save the model
dump(model, 'crop_model.joblib')

# Optional: Print accuracy
y_pred = model.predict(X_test)
print(f"✅ Model trained and saved. Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
