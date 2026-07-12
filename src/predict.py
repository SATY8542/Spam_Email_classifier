import os
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "spam_classifier.pkl")

model = joblib.load(MODEL_PATH)

def predict_message(message):
    prediction = model.predict([message])[0]
    confidence = model.predict_proba([message]).max()
    return prediction, confidence