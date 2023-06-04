from flask import Flask, request, jsonify
import requests
import tensorflow as tf
import numpy as np
import io
from PIL import Image
import time


app = Flask(__name__)
model = tf.keras.models.load_model('model/modelv5.h5')


def predict_image(image):
    image = image.resize((150, 150))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)

    start_time = time.time()
    prediction = model.predict(image)
    end_time = time.time()
    time_predict = end_time - start_time

    predicted_class = np.argmax(prediction)
    accuracy = np.max(prediction) * 100
    accuracy = int(accuracy) if accuracy.is_integer() else round(accuracy, 2)

    return predicted_class, accuracy, time_predict


@app.get('/')
def index():
    return "TaniTama Indonesia"


@app.post('/predict')
def riceLeaf():
    try:
        json_data = request.get_json()
        image_url = json_data.get('image', '')
        response = requests.get(image_url)

        if response.status_code == 200:
            image_bytes = response.content
            image = Image.open(io.BytesIO(image_bytes))

            predict, accuracy, time_predict = predict_image(image)

            return jsonify({
                "prediction": int(predict),
                "accuracy": float(accuracy),
                "time_predict": float(time_predict)
            })

        else:
            return jsonify({'error': 'Failed to fetch image from URL'})

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8881)
