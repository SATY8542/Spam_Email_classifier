import joblib
import pandas as pd

model = joblib.load("models/spam_classifier.pkl")

def batch_prediction(df):
    df["Prediction"] = model.predict(df["message"])
    return df