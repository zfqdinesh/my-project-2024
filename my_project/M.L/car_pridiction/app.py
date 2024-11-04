from flask import Flask, request, render_template, jsonify
import joblib
import numpy as np

# Create Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('car_model.pkl')

@app.route('/')
def car_pridiction():
    return render_template('car_pridiction.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the form
    top_speed = float(request.form['top_speed'])
    engine_power = float(request.form['engine_power'])
    price = float(request.form['price'])
    
    # Prepare input data for prediction
    input_data = np.array([[top_speed, engine_power, price]])
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    return jsonify({'predicted_car': prediction})

if __name__ == '__main__':
    app.run(port=5001)
