import streamlit as st
import pandas as pd
from src.predict import predict_message
from src.batch_predict import batch_prediction

st.title("📧 Spam Email Classifier")

option = st.sidebar.selectbox(
    "Choose Prediction Mode",
    ["Single Prediction", "Batch Prediction"]
)

if option == "Single Prediction":

    text = st.text_area("Enter Email or SMS")

    if st.button("Predict"):

        label, confidence = predict_message(text)

        st.success(f"Prediction : {label}")
        st.write(f"Confidence : {confidence:.2%}")

else:

    uploaded_file = st.file_uploader(
        "Upload CSV",
        type=["csv"]
    )

    if uploaded_file:

        df = pd.read_csv(uploaded_file)

        st.write("Uploaded Data")
        st.dataframe(df)

        if st.button("Run Batch Prediction"):

            result = batch_prediction(df)

            st.success("Prediction Completed")

            st.dataframe(result)

            csv = result.to_csv(index=False).encode("utf-8")

            st.download_button(
                "Download Results",
                csv,
                "prediction.csv",
                "text/csv"
            )