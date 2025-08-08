# 🐾 Animal Image Classifier (Flask + TensorFlow + Ngrok)

This project is a web-based **Animal Image Classifier** built using **Flask**, **TensorFlow**, and **Ngrok**.  
It allows users to upload images of animals and get predictions using two different trained models.

The app runs **locally**, but is made publicly accessible using a secure **Ngrok URL**.

---

## 🚀 Features

- Upload an animal image via a simple web interface
- Choose between two classifiers:
  - **VGG16-based model**
  - **Custom team-trained model**
- View predictions and confidence levels instantly
- Clean and responsive UI with live preview
- Hosted via **Ngrok** for easy sharing and testing

---

## 📂 Project Structure

```
project/
│
├── model/
│   ├── model_3.keras        # Team-trained model (expects 64x64 images)
│   └── model_4.keras        # VGG16-based model (expects 128x128 images)
│
├── static/
│   ├── css/
│   │   └── style.css        # Styling for the UI
│   └── js/
│       └── script.js        # Frontend logic (preview, upload, fetch)
│
├── templates/
│   ├── index.html           # Main web interface
│   └── about.html           # About team and project
│
├── app.py                   # Main Flask application
└── README.md                # This file
```

---

## ⚙️ Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/animal-classifier.git
cd animal-classifier
```

### 2. Install required packages

Make sure you have Python 3.x installed. Then install dependencies:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install flask tensorflow pillow pyngrok
```

### 3. Setup Ngrok

You need to sign up at [https://ngrok.com](https://ngrok.com) to get your **auth token**.

Add the token in your `app.py`:

```python
ngrok.set_auth_token("YOUR_AUTH_TOKEN")
```

This allows Ngrok to generate a secure public link for your app.

---

### 4. Run the App

Start the Flask app:

```bash
python app.py
```

You'll see a message like:

```
🚀 App is live at: https://random-subdomain.ngrok.io
```

Click the link to open the web app.

---

## 📷 Sample Use

1. Upload an animal image (JPEG, PNG, etc.)
2. Click either:
   - **Classify VGG16** – to use the VGG16 model
   - **Team Classify** – to use your custom model
3. See prediction results with confidence and probabilities
4. Click **Clear** to reset the interface

---

## 🧠 Models Info

| Model Name  | File            | Input Shape   | Description                  |
| ----------- | --------------- | ------------- | ---------------------------- |
| Team Model  | `model_3.keras` | (64, 64, 3)   | Custom CNN trained by team   |
| VGG16 Model | `model_4.keras` | (128, 128, 3) | Transfer learning with VGG16 |

---

## 🛰 Deployment Summary

### 1. **Model Preparation**

Two models were trained and saved in Keras format:

- `model_4.keras`: VGG16 model (input size 128×128)
- `model_3.keras`: Custom team CNN (input size 64×64)

Both models classify images into 10 categories.

### 2. **Flask Web Application**

The backend serves prediction routes for both models. Each route dynamically resizes images to the model’s expected input shape.

### 3. **Frontend Interface**

HTML + CSS + JS frontend allows image uploads, live preview, and model selection. Results are shown side by side.

### 4. **Ngrok Hosting**

Ngrok was used to expose the local server with:

```python
ngrok.set_auth_token("YOUR_AUTH_TOKEN")
```

This enables a secure public URL for demo and access.

### ✅ Final Outcome

A fully functional web app for real-time animal image classification using two models.

---

## 👥 About the Team

Built by:

- Sam
- Alex
- Nicolas

> Learn more on the [About Us](/about) page!

---

## ✅ Future Improvements

- Allow drag-and-drop image uploads
- Add support for additional models
- Host permanently using cloud platforms (e.g. AWS, Heroku)
- Due to the issue of big size of mode_4.keras i include the file downloading link
- Download the model to your folder then add it inside model folder and run the app
