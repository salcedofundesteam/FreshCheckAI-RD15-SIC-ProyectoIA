import os
import numpy as np
from flask import Flask, render_template, request, jsonify
try:
    from tensorflow.keras.models import load_model
    from tensorflow.keras.preprocessing import image
except ImportError:
    print("TensorFlow not found. Predictions will not work, but UI will load.")
    load_model = None
    image = None

from PIL import Image
import io

app = Flask(__name__)

# Load Model
MODEL_PATH = "clasificador_frutas.h5"
model = None
try:
    if load_model:
        model = load_model(MODEL_PATH)
        print("Model loaded successfully!")
    else:
        print("Skipping model load due to missing TensorFlow.")
except Exception as e:
    print(f"Error loading model: {e}")


# Class names (from Testing.py)
CLASSES = [
    "Manzana fresca",
    "Banana fresca",
    "Naranja fresca",
    "Manzana podrida",
    "Banana podrida",
    "Naranja podrida",
    "Manzana verde",
    "Banana verde",
    "Naranja verde"
]

def prepare_image(img_bytes):
    img = Image.open(io.BytesIO(img_bytes))
    img = img.resize((150, 150))
    img = img.convert('RGB')
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return jsonify({'error': 'Model not loaded'}), 500
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    try:
        img_bytes = file.read()
        processed_img = prepare_image(img_bytes)
        prediction = model.predict(processed_img)
        predicted_class = CLASSES[np.argmax(prediction)]
        confidence = float(np.max(prediction))
        
        return jsonify({
            'class': predicted_class,
            'confidence': confidence
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
