from flask import Flask, request, render_template
import pandas as pd
import os

app = Flask(__name__)

# Function to process the sales data
def process_sales_data(file_path):
    df = pd.read_csv(file_path)
    df['Total Sales'] = df['Price'] * df['Quantity']
    total_sales = df['Total Sales'].sum()
    total_quantity = df['Quantity'].sum()
    average_price = df['Price'].mean()
    
    summary = {
        "Total Sales": total_sales,
        "Total Quantity Sold": total_quantity,
        "Average Price per Product": average_price
    }

    return summary

# Home route
@app.route('/')
def index():
    return render_template('data_procesing.html')

# Upload route
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    if file:
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)

        # Process the uploaded file
        result = process_sales_data(file_path)

        return render_template('results.html', summary=result)

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')  # Create uploads folder if it doesn't exist
    app.run(port=5003)
