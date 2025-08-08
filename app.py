import os
from flask import Flask, request, jsonify, render_template
from pyngrok import ngrok
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import io

# Load models
team_model = load_model("model/model_3.keras")  # Team model
vgg_model = load_model("model/model_4.keras")  # VGG16 model

class_names = [
    "butterfly",
    "cat",
    "chicken",
    "cow",
    "dog",
    "elephant",
    "horse",
    "sheep",
    "spider",
    "squirrel",
]

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


def preprocess_image(file, target_size):
    image = Image.open(io.BytesIO(file.read())).convert("RGB")
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = image / 255.0
    return image


@app.route("/predict/<model_type>", methods=["POST"])
def predict(model_type):
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]

    try:
        # Determine target size based on model
        if model_type == "vgg":
            target_size = (128, 128)
            image = preprocess_image(file, target_size)
            prediction = vgg_model.predict(image)[0]
        elif model_type == "team":
            target_size = (64, 64)
            image = preprocess_image(file, target_size)
            prediction = team_model.predict(image)[0]
        else:
            return jsonify({"error": "Invalid model type"}), 400

        top_index = int(np.argmax(prediction))
        result = {
            "prediction": class_names[top_index],
            "confidence": float(prediction[top_index]),
            "all_probs": {
                class_names[i]: float(prediction[i]) for i in range(len(class_names))
            },
        }
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Run Flask app with ngrok
ngrok.set_auth_token(
    "310eChYZMr5MUtpbGjmT6LytdLx_5wFHwXiVDoMLo3bHbEVTM"
)  # Replace this
public_url = ngrok.connect(5000)
print(f"🚀 App is live at: {public_url}")
app.run(port=5000)
