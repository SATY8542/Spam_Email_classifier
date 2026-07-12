# 📧 Spam Email Classifier

A Machine Learning project that classifies Email/SMS messages as **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP) and a Naive Bayes classifier. The application is built with **Python** and **Streamlit** for an interactive web interface.

---

## 🚀 Features

- Predict whether a message is **Spam** or **Ham**
- Text preprocessing using NLTK
- TF-IDF Vectorization
- Naive Bayes Machine Learning Model
- Confidence Score for predictions
- Interactive Streamlit Web Application
- Easy-to-use interface

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit
- Joblib

---

## 📂 Project Structure

```
Spam_Email_Classifier/
│
├── data/
│   └── spam.csv
│
├── models/
│   └── spam_classifier.pkl
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── predict.py
│   └── utils.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dataset

The project uses the **SMS Spam Collection Dataset**, which contains labeled SMS messages.

Columns:
- **v1** → Label (Spam/Ham)
- **v2** → Message Text

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/SATY8542/Spam_Email_classifier.git
```

Move into the project folder:

```bash
cd Spam_Email_classifier
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Train the Model

Run the training script:

```bash
python src/train.py
```

This will create:

```
models/spam_classifier.pkl
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open the URL shown in the terminal (usually):

```
http://localhost:8501
```

---

## 📸 Application Preview

### Home Page

- Enter an Email or SMS
- Click **Predict**
- View Prediction and Confidence Score

Example:

```
Input:
Congratulations! You won ₹10000.

Prediction:
Spam

Confidence:
95%
```

---

## 📈 Machine Learning Workflow

1. Load Dataset
2. Text Preprocessing
3. TF-IDF Feature Extraction
4. Model Training
5. Prediction
6. Streamlit Deployment

---

## 🔮 Future Improvements

- Batch CSV Prediction
- Model Comparison (Naive Bayes, Logistic Regression, SVM)
- Word Cloud Visualization
- Confusion Matrix
- Classification Report
- Email Statistics Dashboard
- Streamlit Cloud Deployment

---

## 👨‍💻 Author

**Satyendra Singh**

GitHub:
https://github.com/SATY8542

---

## 📄 License

This project is created for educational and learning purposes.