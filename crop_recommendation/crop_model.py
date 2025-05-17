# crop_model.py

import joblib
import numpy as np

# Load the pre-trained model (modeljob.pkl)
model = joblib.load('crop_model.joblib')

# Define the function for recommending a crop based on input features
def recommend_crop(nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall):
    # Prepare input features for prediction (needs to be in the same order as trained model)
    input_features = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])
    
    # Predict the recommended crop
    prediction = model.predict(input_features)
    
    # Return the predicted crop
    return prediction[0]
