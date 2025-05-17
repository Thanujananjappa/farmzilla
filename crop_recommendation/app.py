import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Ensure correct path

from flask import Flask, render_template, request
from crop_recommendation.crop_model import recommend_crop  # Correct import

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        # Get the input values from the form
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        # Call the recommend_crop function from crop_model.py
        crop = recommend_crop(N, P, K, temperature, humidity, ph, rainfall)
        
        # Pass the result to the result.html template
        return render_template('result.html', crop=crop)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
