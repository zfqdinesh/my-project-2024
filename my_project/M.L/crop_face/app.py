from flask import Flask, request, render_template, send_file
import cv2
import numpy as np
from PIL import Image
import io
import base64

app = Flask(__name__)

# Load the face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

@app.route('/')
def index():
    return render_template('crop_face.html')  # Ensure this is in a 'templates' folder

@app.route('/upload', methods=['POST'])
def upload_image():
    # Get the image data from the request
    image_data = request.form.get('imageData')
    filter_type = request.form.get('filter')

    if not image_data:
        return "No image data", 400

    # Decode the image data
    image_data = image_data.split(",")[1]
    image_bytes = base64.b64decode(image_data)
    image_np = np.array(Image.open(io.BytesIO(image_bytes)))

    # Apply the selected filter
    if filter_type == "gray":
        image_np = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
    elif filter_type == "blur":
        image_np = cv2.GaussianBlur(image_np, (15, 15), 0)
    elif filter_type == "edges":
        image_np = cv2.Canny(image_np, 100, 200)

    # Convert the processed image back to RGB if it was converted to grayscale
    if len(image_np.shape) == 2:  # Check if the image is grayscale
        image_np = cv2.cvtColor(image_np, cv2.COLOR_GRAY2BGR)

    # Convert the processed image back to an image and send it to the user
    processed_image = Image.fromarray(image_np)
    img_io = io.BytesIO()
    processed_image.save(img_io, 'JPEG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(port=5002)
