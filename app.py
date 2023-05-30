from flask import Flask, request, jsonify
import requests
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import io
from PIL import Image
import time


app = Flask(__name__)

def predict_image(image, model):
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
    documentasi = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Machine Learning Model API Documentation</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </head>
    <body>
        <div class="container">
            <h1 class="display-4">Machine Learning Model API Documentation</h1>

            <div class="mt-4">
                <h3>Endpoint: /rice-leaf</h3>

                <p><strong>Description:</strong> This endpoint allows you to make predictions using the trained machine learning model on image inputs.</p>
            </div>

            <div class="mt-4">
                <h4>Request:</h4>
                <div class="mt-2">
                    <ul>
                        <li>Method: POST</li>
                        <li>Content-Type: multipart/form-data</li>
                    </ul>
                </div>

                <h5>Form Parameters:</h5>
                <table class="table table-bordered mt-2">
                    <tr>
                        <th>Parameter</th>
                        <th>Type</th>
                        <th>Description</th>
                    </tr>
                    <tr>
                        <td>image</td>
                        <td>file</td>
                        <td>The image file for prediction.</td>
                    </tr>
                </table>

                <p><strong>Example Request:</strong></p>
                <pre class="pre-scrollable">
                POST /rice-leaf
                Content-Type: multipart/form-data

                [image file]
                </pre>
            </div>

            <div class="mt-4">
                <h4>Response:</h4>
                <div class="mt-2">
                    <ul>
                        <li>Content-Type: application/json</li>
                    </ul>
                </div>

                <h5>Body Parameters:</h5>
                <table class="table table-bordered mt-2">
                    <tr>
                        <th>Parameter</th>
                        <th>Type</th>
                        <th>Description</th>
                    </tr>
                    <tr>
                        <td>prediction</td>
                        <td>String</td>
                        <td>The predicted class label for the input image.</td>
                    </tr>
                </table>

                <p><strong>Example Response:</strong></p>
                <pre class="pre-scrollable">
                HTTP/1.1 200 OK
                Content-Type: application/json

                {
                "prediction": "0"
                }
                </pre>
            </div>

            <div class="mt-4">
                <h4>Error Responses:</h4>
                <ul>
                    <li>HTTP/1.1 400 Bad Request:
                        <ul>
                            <li>Description: Invalid request body or unsupported image format.</li>
                            <li>Example Response:</li>
                        </ul>
                        <pre class="pre-scrollable">
                        HTTP/1.1 400 Bad Request
                        Content-Type: application/json

                        {
                            "error": "Invalid request body or unsupported image format."
                        }
                        </pre>
                    </li>
                    <li>HTTP/1.1 500 Internal Server Error:
                        <ul>
                            <li>Description: An error occurred while processing the prediction.</li>
                            <li>Example Response:</li>
                        </ul>
                        <pre class="pre-scrollable">
                        HTTP/1.1 500 Internal Server Error
                        Content-Type: application/json

                        {
                            "error": "An error occurred while processing the prediction."
                        }
                        </pre>
                    </li>
                </ul>
            </div>
        </div>
    </body>
    </html>
    """
    return documentasi

@app.post('/rice-leaf')
def riceLeaf():
    try:
        json_data = request.get_json()
        image_url = json_data.get('image', '')
        response = requests.get(image_url)
        
        if response.status_code == 200:
            image_bytes = response.content
            image = Image.open(io.BytesIO(image_bytes))

            model = tf.keras.models.load_model('model/modelv5.h5')
            predict, accuracy, time_predict = predict_image(image, model)
        
            return jsonify({
                "prediction": int(predict),
                "accuracy" : float(accuracy),
                "time_predict": float(time_predict)
            })

        else:
            return jsonify({'error': 'Failed to fetch image from URL'})

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8881, debug=True)