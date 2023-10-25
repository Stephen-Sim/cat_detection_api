from flask import Flask, request, jsonify, make_response
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
from PIL import Image

import numpy as np
import base64
import io

app = Flask(__name__)

# Load pre-trained model
model = MobileNetV2(weights='imagenet')

def is_cat(image_data):
    try:
        # Create a BytesIO object
        image_io = io.BytesIO(image_data)

        # Load the image using PIL
        pil_image = Image.open(image_io)

        # Resize the image to match the input shape expected by the model
        pil_image = pil_image.resize((224, 224))

        # Convert the PIL image back into an array
        img = image.img_to_array(pil_image)
        x = np.expand_dims(img, axis=0)
        x = preprocess_input(x)

        preds = model.predict(x)
        results = decode_predictions(preds, top=3)[0]

        for entry in results:
            if entry[1] == 'tabby' or entry[1] == 'tiger_cat':
                return True

        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if data:
            image_data = data['image']
            image_data = base64.b64decode(image_data)
            if is_cat(image_data):
                result = True
            else:
                result = False
            return make_response(jsonify({'result': result}), 200)
        else:
            return make_response(jsonify({'error': 'No image data received'}), 400)
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)
    

if __name__ == '__main__':
    app.run(debug=True)
